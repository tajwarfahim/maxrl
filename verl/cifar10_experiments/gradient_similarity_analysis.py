#!/usr/bin/env python3
"""
Dataset-level gradient similarity on ImageNet-1k (256x256)

Fixes:
- same 10k images
- same model init
- same BN state
- same action samples
"""

import torch
import torch.nn.functional as F
import torchvision.transforms as T
import random
import numpy as np
from torch.utils.data import DataLoader, Subset
from datasets import load_dataset
from torchvision import models
from typing import Tuple

############################################
# Reproducibility
############################################

def set_seed(seed=0):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

############################################
# HF ImageNet wrapper
############################################

class HFImageNet(torch.utils.data.Dataset):
    def __init__(self, split, transform, hf):
        self.ds = hf[split]
        self.t = transform

    def __len__(self):
        return len(self.ds)
    
    def __getitem__(self,i):
        x = self.t(self.ds[i]["image"])
        y = self.ds[i]["label"]
        return x,y

############################################
# Deterministic transform
############################################

def imagenet_transform():
    mean, std = (0.485,0.456,0.406), (0.229,0.224,0.225)
    return T.Compose(
        [
            T.Resize(256),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(mean,std),
        ]
    )

############################################
# Fixed subset
############################################

def fixed_subset(dataset, n, seed=0):
    g=torch.Generator().manual_seed(seed)
    idx=torch.randperm(len(dataset),generator=g)[:n].tolist()
    return Subset(dataset,idx)

############################################
# Loss utilities
############################################

def take_actions_and_log_probs_multi(logits, num_samples_per_example):
    """
    inputs: (B, C, H, W)
    returns:
        actions_flat:    (B*K, 1)  long
        log_probs_flat:  (B*K,)    float
    """                         # (B, A)
    probs = F.softmax(logits, dim=1)                # (B, A)

    # Sample K actions from each row
    actions = torch.multinomial(
        probs, num_samples=num_samples_per_example, replacement=True
    )                                               # (B, K)

    log_probs_all = F.log_softmax(logits, dim=1)    # (B, A)
    chosen_log_probs = log_probs_all.gather(1, actions)  # (B, K)

    actions_flat = actions.view(-1, 1)              # (B*K, 1)
    log_probs_flat = chosen_log_probs.view(-1)      # (B*K,)

    return actions_flat, log_probs_flat


def calculate_advantage(
    actions,
    targets,
    num_samples_per_example,
    advantage_type="grpo",
    epsilon=1e-6,
    use_baseline=True,
    max_k=None,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Vectorized advantage computation.

    actions: (B*K, 1) long
    targets: (B*K,)   long  (targets_expanded)
    returns:
        advantages: (B*K,) float
        loss_mask:  (B*K,) float (currently all ones)
    """
    device = actions.device
    actions_flat = actions.squeeze(1)  # (N,)
    N = actions_flat.shape[0]
    K = num_samples_per_example
    if N % K != 0:
        raise ValueError(
            f"Number of actions ({N}) not divisible by num_samples_per_example ({K})."
        )
    B = N // K

    # rewards: 1 if action == target, else 0
    rewards = (actions_flat == targets).float()  # (N,)
    rewards = rewards.view(B, K)                 # (B, K)

    mean_reward = rewards.mean(dim=1, keepdim=True)              # (B, 1)
    sqrt_mean_reward = torch.sqrt(mean_reward)
    # Use population std (ddof=0) to match np.std default
    std_reward = rewards.std(dim=1, unbiased=False, keepdim=True)  # (B, 1)

    denom_std = std_reward + epsilon
    denom_mean = mean_reward + epsilon
    denom_sqrt_mean = sqrt_mean_reward + epsilon

    if advantage_type == "grpo":
        advantages = (rewards - mean_reward) / denom_std

    elif advantage_type == "one_sided_grpo":
        advantages = (rewards - mean_reward) / denom_sqrt_mean

    elif advantage_type == "p_normalization":
        advantages = ((rewards - mean_reward) / denom_std) / denom_mean

    elif advantage_type == "reinforce_without_baseline":
        advantages = rewards

    elif advantage_type == "reinforce_with_baseline":
        advantages = rewards - mean_reward

    elif advantage_type == "reinforce_with_p_normalization":
        advantages = (rewards - mean_reward) / denom_mean

    elif advantage_type == "conditional_expectation":
        advantages = rewards / denom_mean

    elif advantage_type == "maclaurin":
        # k values
        device = rewards.device
        B, K = rewards.shape

        # failures
        F = rewards < 0.5
        F_num = F.sum(dim=1)                  # (B,)

        T = min(max_k, K) if max_k is not None else K
        ks = torch.arange(2, T + 1, device=device)    # (T-1,)
        k = ks.unsqueeze(0)                           # (1, T-1)
        Fk = F_num.unsqueeze(1)                       # (B, 1)

        # valid where F >= k
        valid = Fk >= k

        # log C(F,k)
        log_num = (
            torch.lgamma(Fk + 1)
        - torch.lgamma(k + 1)
        - torch.lgamma(Fk - k + 1)
        )

        # log C(K,k)
        Kt = torch.tensor(K, device=device)
        log_den = (
            torch.lgamma(Kt + 1)
        - torch.lgamma(k + 1)
        - torch.lgamma(Kt - k + 1)
        )

        # log ratio
        log_ratio = log_num - log_den

        # if k > F: ratio = 0
        log_ratio = torch.where(
            valid, log_ratio, torch.full_like(log_ratio, -float("inf"))
        )

        ratio = torch.exp(log_ratio)          # (B, T-1)

        # ---- signal term ----
        signal_sum = ratio.sum(dim=1)         # (B,)
        signal_term = torch.ones_like(rewards)

        mask_fail_prompt = F_num > 0
        if mask_fail_prompt.any():
            signal_per_fail = -signal_sum / F_num.clamp(min=1)   # (B,)
            signal_per_fail = signal_per_fail.unsqueeze(1)      # (B,1)
            signal_per_fail = signal_per_fail.expand(-1, K)     # (B,K)
            signal_term[F] = signal_per_fail[F] * K

        # ---- baseline ----
        baseline_term = torch.zeros_like(rewards)
        if use_baseline:
            baseline_sum = ratio.sum(dim=1) / K      # (B,)
            baseline_term = baseline_sum.unsqueeze(1).expand(-1, K) * K

        advantages = signal_term + baseline_term

        # ---- perfect prompts (no failures) must have zero advantage ----
        perfect = (F_num == 0)
        if perfect.any():
            advantages[perfect.unsqueeze(1).expand(-1, K)] = 0.0

    elif advantage_type == "pkpo":
        import math
        def correct_advantage(n, c, k):
            k_minus_1 = torch.full_like(c, k - 1, dtype=torch.long, device=device)
            n_minus_c = -c + n
            term1 = torch.tensor([math.comb(int(up), int(down)) 
                                for up, down in zip(n_minus_c, k_minus_1)], device=device)
            term2 = math.comb(n - 1, k - 1)
            return term1 / term2
        C = rewards.sum(dim=1) # (B,)
        n = K
        k = max_k if max_k is not None else K
        advantages = correct_advantage(n, C, k).unsqueeze(1).expand(rewards.shape) * rewards  # shape: (m, n)
        if n > 1 and use_baseline:
            sum_per_group = advantages.sum(dim=1, keepdim=True)  # shape: (m, 1)
            advantages = (advantages * n - sum_per_group) / (n - 1)  # shape: (m, n)

    else:
        raise ValueError(
            f"Given advantage type {advantage_type} is not supported."
        )

    advantages = advantages.view(N).to(device)         # (B*K,)
    loss_mask = torch.ones_like(advantages).detach()   # (B*K,)

    return advantages, loss_mask


def calculate_loss(
    logits,
    targets,
    num_train_rollouts_per_example,
    advantage_type,
    max_k,
):
    if advantage_type == "cross_entropy":
        return F.cross_entropy(logits, targets).mean()
    
    actions_flat, log_probs_flat = take_actions_and_log_probs_multi(
        logits=logits,
        num_samples_per_example=num_train_rollouts_per_example,
    )

    targets_expanded = targets.repeat_interleave(num_train_rollouts_per_example)  # (B*K,)

    advantages, loss_mask = calculate_advantage(
        actions=actions_flat,                   # (B*K,1)
        targets=targets_expanded,               # (B*K,)
        num_samples_per_example=num_train_rollouts_per_example,
        advantage_type=advantage_type,
        use_baseline=True,
        max_k=max_k,
    )

    loss = -advantages.detach() * log_probs_flat * loss_mask
    loss = loss.sum() / loss_mask.sum()

    return loss

############################################
# Gradient accumulation
############################################

def zero_like(model):
    return [torch.zeros_like(p,device="cpu") for p in model.parameters()]

def accumulate(model,acc):
    for i,p in enumerate(model.parameters()):
        if p.grad is not None:
            acc[i]+=p.grad.detach().cpu()

def flatten(acc):
    return torch.cat([a.reshape(-1) for a in acc])

############################################
# Dataset gradient
############################################

def dataset_grad(
    model,
    loader,
    loss_type,
    K,
    max_k,
    device,
    seed,
):
    model.train()     # freeze BatchNorm
    acc = zero_like(model)
    total = 0
    gen = torch.Generator(device=device).manual_seed(seed)

    for x,y in loader:
        x, y = x.to(device), y.to(device)
        total += y.size(0)

        model.zero_grad()
        logits=model(x)

        loss = calculate_loss(
            logits=logits,
            targets=y,
            num_train_rollouts_per_example=K,
            advantage_type=loss_type,
            max_k=max_k,
        )

        loss.backward()
        accumulate(model,acc)

    for i in range(len(acc)):
        acc[i] /= total

    return flatten(acc)

############################################
# Similarity
############################################

def cosine(a,b):
    return torch.dot(a,b)/(a.norm()*b.norm()+1e-12)

############################################
# Main
############################################

def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--num-images", type=int, default=10000)
    parser.add_argument("--K", type=int, default=131072)
    parser.add_argument("--seed", type=int, default=0)
    args=parser.parse_args()

    set_seed(args.seed)
    device="cuda" if torch.cuda.is_available() else "cpu"

    print("Loading ImageNet-256…")
    hf=load_dataset("benjamin-paine/imagenet-1k-256x256")
    ds=HFImageNet("train",imagenet_transform(),hf)
    ds=fixed_subset(ds,args.num_images,seed=123)

    loader = DataLoader(
        ds,
        batch_size=64,
        shuffle=False,
        num_workers=4,
        pin_memory=True,
    )

    model = models.resnet50(num_classes=1000).to(device)

    # losses = [
    #     "cross_entropy",
    #     "grpo",
    #     "one_sided_grpo",
    #     "reinforce_without_baseline",
    #     "reinforce_with_baseline",
    #     "reinforce_with_p_normalization",
    #     "maclaurin_1",
    #     "maclaurin_128",
    #     "maclaurin_2048",
    #     "maclaurin_4096",
    #     "maclaurin_8192",
    # ]

    losses = [
        "cross_entropy",
        "reinforce_with_baseline 16",
        "reinforce_with_baseline 128",
        "reinforce_with_baseline 1024",
        "reinforce_with_baseline 8192",
        "reinforce_with_baseline 16384",
        "reinforce_with_baseline 32768",
        "reinforce_with_baseline 65536",
        "reinforce_with_baseline 131072",
    ]

    grads = {}

    for loss_type in losses:
        print("Computing", loss_type)

        if loss_type != "cross_entropy":
            _loss_type = loss_type.split()[0]
            _K = int(loss_type.split()[-1])

        else:
            _loss_type = loss_type
            _K = args.K

        # grads[loss_type] = dataset_grad(
        #     model=model,
        #     loader=loader,
        #     loss_type=(
        #         "maclaurin" 
        #         if loss_type.startswith("maclaurin")
        #         else loss_type
        #     ),
        #     K=args.K,
        #     max_k=max_k,
        #     device=device,
        #     seed=args.seed,
        # )

        grads[loss_type] = dataset_grad(
            model=model,
            loader=loader,
            loss_type=_loss_type,
            K=_K,
            max_k=None,
            device=device,
            seed=args.seed,
        )

    print("\nGradient similarity:\n")

    for i in range(len(losses)):
        for j in range(i+1,len(losses)):
            a, b = losses[i], losses[j]
            print(f"{a:20s} vs {b:20s}  cos={cosine(grads[a],grads[b]):.6f}  L2={(grads[a]-grads[b]).norm():.3e}")

if __name__=="__main__":
    main()
