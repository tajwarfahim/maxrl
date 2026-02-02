import math
import random
from dataclasses import dataclass

from datasets import load_dataset

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from torch.optim.lr_scheduler import (
    MultiStepLR,
    CosineAnnealingLR,
)

from typing import Tuple, Optional

from verl.cifar10_experiments.plots.resnet import ResNetCIFAR
from torchvision import models

import wandb
from tqdm import tqdm
import argparse


import random
from torch.utils.data import Subset
# ----------------------------
# Config
# ----------------------------
from torch.utils.data import Dataset
import numpy as np

from datasets import DatasetDict
import matplotlib.pyplot as plt
from pathlib import Path
import json

def subset_imagenet_classes(hf_ds: DatasetDict, k: int, seed: int = 42, strategy: str = "first"):
    """
    Returns (hf_ds_subset, label2new, chosen_labels)
    - hf_ds_subset: filtered + remapped labels in [0..k-1]
    - strategy: "first" uses labels 0..k-1, "random" picks k labels uniformly
    """
    assert "train" in hf_ds and "validation" in hf_ds

    rng = random.Random(seed)

    # Choose which original labels to keep
    if strategy == "first":
        chosen = list(range(k))
    elif strategy == "random":
        chosen = rng.sample(range(1000), k)
        chosen.sort()
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    chosen_set = set(chosen)
    label2new = {old: new for new, old in enumerate(chosen)}

    def keep(example):
        return example["label"] in chosen_set

    def remap(example):
        example["label"] = label2new[example["label"]]
        return example

    hf_train = hf_ds["train"].filter(keep)
    hf_val   = hf_ds["validation"].filter(keep)

    hf_train = hf_train.map(remap)
    hf_val   = hf_val.map(remap)

    return DatasetDict(train=hf_train, validation=hf_val), label2new, chosen


class HFImageNet32(Dataset):
    def __init__(self, hf_ds, transform=None):
        self.ds = hf_ds
        self.transform = transform

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, idx):
        item = self.ds[idx]
        img = item["image"]      # PIL Image
        label = item["label"]    # int in [0, 999]

        if self.transform:
            img = self.transform(img)

        return img, label

@dataclass
class Config:
    project: str = "final_p_vs_grad_norm_imagenet256"
    run_name: str = "baseline-small-cnn-ce-8-rollouts"
    batch_size: int = 32
    num_workers: int = 4
    lr: float = 0.1
    weight_decay: float = 5e-4
    num_epochs: int = 5
    seed: int = 42
    log_interval: int = 1  # steps
    model_save_path: str = "/tmp/best_model.pth"
    # loss_type: str = "reinforce"  # options: cross_entropy
    loss_type: str = "cross_entropy"  # options: log_prob, prob, reinforce, reinforce_with_baseline
    rollout_size: int = 8  # for logprob_correction loss
    dataset: str = "cifar100"
    scheduler: str = "cosine_with_warmup"      # "none" | "cosine"
    warmup_epochs: int = 5         # 0 to disable warmup
    min_lr: float = 1e-6           # cosine floor
    eval_interval: int = 1500   # run validation every N train steps
    max_k: Optional[int] = None




# ----------------------------
# Reproducibility
# ----------------------------
def set_seed(seed: int = 42):
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = False
    torch.backends.cudnn.benchmark = True


# ----------------------------
# Small CNN for CIFAR-10
# ----------------------------
class SmallCNN(nn.Module):
    def __init__(self, num_classes: int = 10):
        super().__init__()
        # 3x32x32 -> 64x8x8 after 3 conv blocks + pooling
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),  # 32x32x32
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),  # 32x16x16

            nn.Conv2d(32, 64, kernel_size=3, padding=1),  # 64x16x16
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),  # 64x8x8

            nn.Conv2d(64, 128, kernel_size=3, padding=1),  # 128x8x8
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
        )
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),  # 128x1x1
            nn.Flatten(),
            nn.Linear(128, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x




# ----------------------------
# Accuracy helper
# ----------------------------
@torch.no_grad()
def accuracy(logits: torch.Tensor, targets: torch.Tensor) -> float:
    preds = logits.argmax(dim=1)
    correct = (preds == targets).float().sum()
    return (correct / targets.size(0)).item()


# ----------------------------
# Data loaders
# ----------------------------
class HFImageNet(torch.utils.data.Dataset):
    def __init__(self, split, transform, hf_ds):
        self.ds = hf_ds[split]
        self.transform = transform

        print("Number of classes: ", self.get_num_classes())

    def __len__(self) -> int:
        return len(self.ds)

    def __getitem__(self, idx):
        img = self.ds[idx]["image"]   # PIL image
        label = self.ds[idx]["label"]
        img = self.transform(img)
        
        return img, label
    
    def get_num_classes(self) -> int:
        return self.ds.features["label"].num_classes
    

def get_dataloaders(dataset_name, data_dir, batch_size=128, num_workers=4):
    # --------------------
    # Dataset statistics
    # --------------------
    if dataset_name == "cifar10":
        mean = (0.4914, 0.4822, 0.4465)
        std  = (0.2023, 0.1994, 0.2010)

    elif dataset_name == "cifar100":
        mean = (0.5071, 0.4865, 0.4409)
        std  = (0.2673, 0.2564, 0.2762)

    elif dataset_name == "imagenet32":
        # Standard ImageNet normalization
        mean = (0.485, 0.456, 0.406)
        std  = (0.229, 0.224, 0.225)

    elif dataset_name == "imagenet256":
        # Standard ImageNet normalization
        mean = (0.485, 0.456, 0.406)
        std  = (0.229, 0.224, 0.225)

    else:
        raise ValueError(f"Dataset {dataset_name} not supported.")

    # --------------------
    # Transforms
    # --------------------
    if dataset_name != "imagenet256":
        train_transform = transforms.Compose(
            [
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(mean, std),
            ]
        )

        test_transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(mean, std),
            ]
        )

    else:
        train_transform = transforms.Compose(
            [
                # Random crop to 224x224 from 256x256
                transforms.RandomResizedCrop(224, scale=(0.08, 1.0)),
                # Standard horizontal flip
                transforms.RandomHorizontalFlip(p=0.5),
                # Convert to tensor
                transforms.ToTensor(),
                # Standard ImageNet normalization
                transforms.Normalize(
                    mean=mean,
                    std=std,
                ),
            ]
        )

        test_transform = transforms.Compose(
            [
                # Resize smaller side to 256 (already the case, but safe)
                transforms.Resize(256),
                # Center crop to 224
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=mean,
                    std=std,
                ),
            ]
        )

    # --------------------
    # CIFAR (torchvision)
    # --------------------
    if dataset_name == "cifar10":
        train_set = datasets.CIFAR10(data_dir, train=True, download=True,
                                     transform=train_transform)
        test_set  = datasets.CIFAR10(data_dir, train=False, download=True,
                                     transform=test_transform)
        num_classes = 10

    elif dataset_name == "cifar100":
        train_set = datasets.CIFAR100(data_dir, train=True, download=True,
                                      transform=train_transform)
        test_set  = datasets.CIFAR100(data_dir, train=False, download=True,
                                      transform=test_transform)
        
        num_classes = 100

    # --------------------
    # ImageNet-1k-32×32 (Hugging Face)
    # --------------------
    elif dataset_name == "imagenet32":
        print("Loading imagenet 32 x 32 ...")

        hf_ds = load_dataset("benjamin-paine/imagenet-1k-32x32")

        train_set = HFImageNet(
            split="train", 
            transform=train_transform, 
            hf_ds=hf_ds,
        )

        test_set = HFImageNet(
            split="validation", 
            transform=test_transform,
            hf_ds=hf_ds,
        )

        num_classes = 1000


    elif dataset_name == "imagenet256":
        print("Loading imagenet 256 x 256 ...")

        hf_ds = load_dataset("benjamin-paine/imagenet-1k-256x256")

        train_set = HFImageNet(
            split="train", 
            transform=train_transform, 
            hf_ds=hf_ds,
        )

        test_set = HFImageNet(
            split="validation", 
            transform=test_transform,
            hf_ds=hf_ds,
        )

        num_classes = 1000

    else:
        raise ValueError(f"Dataset {dataset_name} not supported.")
    
    print("Num train examples: ", len(train_set))
    print("Num test examples: ", len(test_set))


    # --------------------
    # DataLoaders
    # --------------------
    train_loader = DataLoader(
        train_set, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True
    )
    test_loader = DataLoader(
        test_set, batch_size=1000, shuffle=False,
        num_workers=num_workers, pin_memory=True
    )

    print("Num train batches: ", len(train_loader))
    print("Num test batches: ", len(test_loader))

    return train_loader, test_loader, num_classes


# def get_dataloaders(cfg: Config):
#     transform_train = transforms.Compose([
#         transforms.RandomCrop(32, padding=4),
#         transforms.RandomHorizontalFlip(),
#         transforms.ToTensor(),
#         transforms.Normalize(
#             mean=(0.4914, 0.4822, 0.4465),
#             std=(0.2023, 0.1994, 0.2010),
#         ),
#     ])

#     transform_test = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(
#             mean=(0.4914, 0.4822, 0.4465),
#             std=(0.2023, 0.1994, 0.2010),
#         ),
#     ])

#     if cfg.dataset.lower() in ["imagenet32", "imagenet-1k-32x32"]:
#         hf_ds = load_dataset("benjamin-paine/imagenet-1k-32x32")
#         hf_ds, _, chosen = subset_imagenet_classes(
#             hf_ds, k=cfg.imagenet_k, seed=cfg.seed, strategy=cfg.imagenet_subset_strategy
#         )

#         num_classes = cfg.imagenet_k

#         train_dataset = HFImageNet32(hf_ds["train"], transform_train)
#         val_dataset   = HFImageNet32(hf_ds["validation"], transform_test)
#         print("Train dataset size:", len(train_dataset), "val dataset size:", len(val_dataset), "num classes:", num_classes)

#     elif cfg.dataset.lower() == "cifar10":
#         train_dataset = datasets.CIFAR10(
#             root="./data", train=True, download=True, transform=transform_train
#         )
#         val_dataset = datasets.CIFAR10(
#             root="./data", train=False, download=True, transform=transform_test
#         )        
#         num_classes = 10
#     elif cfg.dataset.lower() == "cifar100":
#         train_dataset = datasets.CIFAR100(
#             root="./data", train=True, download=True, transform=transform_train
#         )
#         val_dataset = datasets.CIFAR100(
#             root="./data", train=False, download=True, transform=transform_test
#         )
#         num_classes = 100

#     train_loader = DataLoader(
#         train_dataset,
#         batch_size=cfg.batch_size,
#         shuffle=True,
#         num_workers=cfg.num_workers,
#         pin_memory=True,
#     )
#     val_loader = DataLoader(
#         val_dataset,
#         batch_size=cfg.batch_size,
#         shuffle=False,
#         num_workers=cfg.num_workers,
#         pin_memory=True,
#     )
#     return train_loader, val_loader, num_classes


# ----------------------------
# Loss calculation
# ----------------------------

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


# ----------------------------
# Train / Eval loops
# ----------------------------
def train_one_epoch(model, optimizer, scheduler, train_loader, val_loader, device, epoch, cfg: Config, global_step=0):
    model.train()
    running_loss = 0.0
    running_correct = 0
    running_total = 0
    for step, (images, targets) in tqdm(enumerate(train_loader), 
                                       desc=f"Epoch {epoch+1} Training", 
                                       total=len(train_loader)):
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)
        logits = model(images)

        loss = calculate_loss(
            logits=logits,
            targets=targets,
            num_train_rollouts_per_example=cfg.rollout_size,
            advantage_type=cfg.loss_type,
            max_k=cfg.max_k,
        )

        loss.backward()

        # Optional grad clipping
        grad_norm = 0.0
        total_norm = 0.0
        for p in model.parameters():
            if p.grad is not None:
                param_norm = p.grad.data.norm(2)
                total_norm += param_norm.item() ** 2
        grad_norm = math.sqrt(total_norm) if total_norm > 0 else 0.0

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
        optimizer.step()
        if scheduler:
            scheduler.step()
        global_step += 1

        batch_size = targets.size(0)
        running_loss += loss.item() * batch_size
        running_correct += (logits.argmax(dim=1) == targets).sum().item()
        running_total += batch_size

        if (step + 1) % cfg.log_interval == 0:
            train_acc = running_correct / running_total
            train_loss = running_loss / running_total
            lr = optimizer.param_groups[0]["lr"]

            wandb.log(
                {
                    "train/loss_step": train_loss,
                    "train/acc_step": train_acc,
                    "train/grad_norm": grad_norm,
                    "train/lr": lr,
                    "train/epoch": epoch + (step + 1) / len(train_loader),
                }
            )

        if (global_step % cfg.eval_interval) == 0:
            val_loss, val_acc = evaluate(model, val_loader, device, epoch + global_step / len(train_loader))
            compute_p_vs_grad(model, val_loader, device, epoch, optimizer, global_step, cfg)
            model.train()  # important: go back to train mode after eval
    
    # Running in the end
    val_loss, val_acc = evaluate(model, val_loader, device, epoch + global_step / len(train_loader))
    model.train()       

    epoch_loss = running_loss / running_total
    epoch_acc = running_correct / running_total
    return epoch_loss, epoch_acc, global_step, val_loss, val_acc


def compute_p_vs_grad(model, val_loader, device, epoch, optimizer, global_step, cfg):
    model.eval()
    pass_rates, grad_norms = [], []
    for images, targets in tqdm(val_loader, desc="Validation", total=len(val_loader)):
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        for i in range(images.shape[0]):
            optimizer.zero_grad()
            image, target = images[i], targets[i]
            logits = model(image[None,:])

            loss = calculate_loss(
                logits=logits,
                targets=targets[i].view(1),
                num_train_rollouts_per_example=cfg.rollout_size,
                advantage_type=cfg.loss_type,
                max_k=cfg.max_k,
            )


            loss.backward()
            
            # Optional grad clipping
            grad_norm = 0.0
            total_norm = 0.0
            for p in model.parameters():
                if p.grad is not None:
                    param_norm = p.grad.data.norm(2)
                    total_norm += param_norm.item() ** 2
            grad_norm = math.sqrt(total_norm) if total_norm > 0 else 0.0

            # COmpute probability
            probs = torch.softmax(logits, dim=1).squeeze()             # (N,C)
            # Compute pass@1 which is the value of the max logits
            pass_rate = probs[target.item()]
            pass_rates.append(pass_rate.item())
            grad_norms.append(grad_norm)

    data_path, plot_path = _save_p_vs_grad(pass_rates, grad_norms, cfg, global_step)


def _save_p_vs_grad(pass_rates, grad_norms, cfg, global_step):
    # directories
    out_dir = Path("p_vs_grad")
    plot_dir = Path("plots")
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_dir.mkdir(parents=True, exist_ok=True)

    loss_type = str(cfg.loss_type)
    step = int(global_step)

    # --------
    # save data
    # --------
    pass_arr = np.asarray(pass_rates, dtype=np.float32)
    grad_arr = np.asarray(grad_norms, dtype=np.float32)
    data_path = out_dir / f"p_vs_grad__loss={loss_type}__step={step}.npz"
    np.savez_compressed(
        data_path,
        pass_rates=pass_arr,
        grad_norms=grad_arr,
        loss_type=loss_type,
        global_step=step,
    )
    # optional: small json "index" you can grep later
    index_path = out_dir / "index.jsonl"
    with index_path.open("a") as f:
        f.write(json.dumps({
            "loss_type": loss_type,
            "global_step": step,
            "path": str(data_path),
            "n": int(pass_arr.size),
        }) + "\n")

    # --------
    # save plot
    # --------
    fig = plt.figure()
    plt.scatter(pass_arr, grad_arr, s=6)
    plt.xlabel("P(correct class)")
    plt.ylabel("Grad L2 norm")
    plt.title(f"p_vs_grad | loss={loss_type} | step={step}")
    plt.tight_layout()

    plot_path = plot_dir / f"scatter__loss={loss_type}__step={step}.png"
    print(f"  Saving p vs grad plot to: {plot_path}")
    plt.savefig(plot_path, dpi=200)
    plt.close(fig)

    return str(data_path), str(plot_path)


@torch.no_grad()
def evaluate(model, val_loader, device, epoch, ks=[1, 4, 16, 64, 256, 1024]):
    model.eval()
    total_loss = 0.0
    total_correct = 0
    total_samples = 0
    pass_at_k = {k: 0 for k in ks}

    for images, targets in tqdm(val_loader, desc="Validation", total=len(val_loader)):
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        logits = model(images)
        loss = F.cross_entropy(logits, targets)

        batch_size = targets.size(0)
        total_loss += loss.item() * batch_size
        total_correct += (logits.argmax(dim=1) == targets).sum().item()
        # COmpute probability
        probs = torch.softmax(logits, dim=1)                    # (N,C)
        # Compute pass@1 which is the value of the max logits
        pass_rate = probs[torch.arange(batch_size), targets]            # (N,)
        for k in ks:
            pass_at_k[k] += (1 - (1 - pass_rate)**k).sum().item()


        total_samples += batch_size

    avg_loss = total_loss / total_samples
    avg_acc = total_correct / total_samples
    pass_at_k_log = {k: pass_at_k[k] / total_samples for k in ks}

    log = {"val/loss": avg_loss, "val/acc": avg_acc, "val/epoch": epoch}
    for k in ks:
        log[f"val/pass@{k}"] = pass_at_k_log[k]
    wandb.log(log)

    return avg_loss, avg_acc


# ----------------------------
# Main
# ----------------------------
def main():
    cfg = Config()
    parser = argparse.ArgumentParser()
    parser.add_argument("--loss-type", type=str, default=cfg.loss_type,
                        help="Type of loss to use: cross_entropy, reinforce, reinforce_with_baseline, grpo")
    parser.add_argument("--rollout-size", type=int, default=cfg.rollout_size,)
    parser.add_argument("--batch-size", type=int, default=cfg.batch_size,)
    parser.add_argument("--lr", type=float, default=cfg.lr,)
    parser.add_argument("--scheduler", type=str, default="cosine_with_warmup")
    parser.add_argument("--warmup_epochs", type=int, default=cfg.warmup_epochs)
    parser.add_argument("--min_lr", type=float, default=cfg.min_lr)

    parser.add_argument("--max-k", type=int, default=None)

    parser.add_argument("--dataset", type=str, default="imagenet256",)
    parser.add_argument("--depth", type=int, default=32,)
    parser.add_argument("--imagenet_k", type=int, default=1000,
                    help="If >0 and dataset is imagenet32, keep only K classes (e.g., 10/100/500).")
    parser.add_argument("--imagenet_subset_strategy", type=str, default="first",
                        choices=["first", "random"],
                        help="How to pick K classes: first or random.")

    
    args = parser.parse_args()
    cfg.loss_type = args.loss_type
    cfg.rollout_size = args.rollout_size
    cfg.batch_size = args.batch_size
    cfg.lr = args.lr
    cfg.dataset = args.dataset
    cfg.depth = args.depth
    cfg.scheduler = args.scheduler
    cfg.warmup_epochs = args.warmup_epochs
    cfg.min_lr = args.min_lr
    cfg.imagenet_k = args.imagenet_k
    cfg.imagenet_subset_strategy = args.imagenet_subset_strategy
    cfg.max_k = args.max_k

    cfg.run_name = f"{cfg.loss_type}-{cfg.imagenet_k}"


    print("Config:")
    print(cfg)


    set_seed(cfg.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Init wandb
    wandb.init(
        project=cfg.project,
        name=cfg.run_name,
        config={
            "batch_size": cfg.batch_size,
            "lr": cfg.lr,
            "weight_decay": cfg.weight_decay,
            "num_epochs": cfg.num_epochs,
            "model": "ResNet",
            "dataset": cfg.dataset,
            "rollout_size": cfg.rollout_size,
            "dataset": cfg.dataset,
            "loss_type": cfg.loss_type,
            "depth": cfg.depth,
        },
    )

    train_loader, val_loader, num_classes = get_dataloaders(
        dataset_name=cfg.dataset,
        data_dir=None,
        batch_size=cfg.batch_size,
    )

    model = models.resnet50(num_classes=num_classes).to(device)

    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=args.lr,
        momentum=0.9,
        weight_decay=1e-4,
        nesterov=False,
    )

    advantage_type = args.loss_type

    print("Loss type: ", advantage_type)

    if cfg.scheduler == "cosine":
        scheduler = CosineAnnealingLR(
            optimizer,
            T_max=(args.epochs * len(train_loader)),
            eta_min=(args.lr * 1e-4),
        )

    elif cfg.scheduler == "multi_step":
        scheduler = MultiStepLR(optimizer, milestones=args.milestones, gamma=args.gamma)

    elif cfg.scheduler == "cosine_with_warmup":
        total_steps = cfg.num_epochs * len(train_loader)
        warmup_steps = len(train_loader)   # 1 epoch

        def lr_lambda(step):
            if step < warmup_steps:
                return step / warmup_steps
            else:
                progress = (step - warmup_steps) / (total_steps - warmup_steps)
                return 0.5 * (1.0 + math.cos(math.pi * progress))

        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    else:
        raise ValueError(
            f"Given lr scheduler {args.lr_scheduler} is not supported yet."
        )
    
    best_val_acc = 0.0
    
    global_step = 0
    for epoch in tqdm(range(cfg.num_epochs), desc="Training Epochs", total=cfg.num_epochs):

        train_loss, train_acc, global_step, val_loss, val_acc = train_one_epoch(
            model, optimizer, scheduler, train_loader, val_loader, device, epoch, cfg, global_step
        )

        wandb.log(
            {
                "train/loss_epoch": train_loss,
                "train/acc_epoch": train_acc,
                "epoch": epoch + 1,
            }
        )

        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                    "epoch": epoch + 1,
                    "best_val_acc": best_val_acc,
                    "config": cfg.__dict__,
                },
                cfg.model_save_path,
            )
            print(f"  Saved new best model with val acc={best_val_acc:.4f}")

    print(f"\nTraining finished. Best val acc: {best_val_acc:.4f}")
    wandb.finish()


if __name__ == "__main__":
    main()
