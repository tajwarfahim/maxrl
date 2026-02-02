#!/usr/bin/env python3
"""
Train a ResNet-32 on CIFAR-10 using PyTorch, now with Weights & Biases logging.

Usage:
    python train_resnet32_cifar10.py --data-dir ./data --epochs 200 --wandb
"""

import argparse
import os
import random
import numpy as np
from tqdm import tqdm
from typing import Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import (
    MultiStepLR,
    CosineAnnealingLR,
)
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# --- W&B ---
import wandb

# ResNet model
from resnet import ResNetCIFAR

# CNN model
# from verl.cifar10_experiments.cnn_model import SmallCNN


# -------------------------
# Utils
# -------------------------

def set_seed(seed: int = 42):
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


# -------------------------
# Data
# -------------------------

def get_dataloaders(dataset_name, data_dir, batch_size=128, num_workers=4):
    if dataset_name == "cifar10":
        mean = (0.4914, 0.4822, 0.4465)
        std = (0.2023, 0.1994, 0.2010)

    elif dataset_name == "cifar100":
        mean = (0.5071, 0.4865, 0.4409)
        std  = (0.2673, 0.2564, 0.2762)

    else:
        raise ValueError(
            f"Given dataset name {dataset_name} is not supported yet."
        )

    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    if dataset_name == "cifar10":
        train_set = datasets.CIFAR10(
            root=data_dir, train=True, download=True, transform=train_transform
        )
        test_set = datasets.CIFAR10(
            root=data_dir, train=False, download=True, transform=test_transform
        )

    elif dataset_name == "cifar100":
        train_set = datasets.CIFAR100(
            root=data_dir, train=True, download=True, transform=train_transform
        )
        test_set = datasets.CIFAR100(
            root=data_dir, train=False, download=True, transform=test_transform
        )

    else:
        raise ValueError(
            f"Given dataset name {dataset_name} is not supported yet."
        )

    train_loader = DataLoader(
        train_set, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True
    )
    test_loader = DataLoader(
        test_set, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=True
    )
    return train_loader, test_loader


# -------------------------
# Training / Evaluation
# -------------------------
def take_actions_and_log_probs_multi(model, inputs, num_samples_per_example):
    """
    inputs: (B, C, H, W)
    returns:
        actions_flat:    (B*K, 1)  long
        log_probs_flat:  (B*K,)    float
    """
    logits = model(inputs)                          # (B, A)
    probs = F.softmax(logits, dim=1)                # (B, A)

    # Sample K actions from each row
    actions = torch.multinomial(
        probs, num_samples=num_samples_per_example, replacement=True
    )                                               # (B, K)

    log_probs_all = F.log_softmax(logits, dim=1)    # (B, A)
    # Get log prob of each sampled action: gather along class dimension
    chosen_log_probs = log_probs_all.gather(1, actions)  # (B, K)

    # Flatten to match your old (N = B*K) interface
    actions_flat = actions.view(-1, 1)              # (B*K, 1)
    log_probs_flat = chosen_log_probs.view(-1)      # (B*K,)

    return actions_flat, log_probs_flat


def calculate_advantage(
    actions,
    targets,
    num_samples_per_example,
    advantage_type="grpo",
    epsilon=1e-6,
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
    # Use population std (ddof=0) to match np.std default
    std_reward = rewards.std(dim=1, unbiased=False, keepdim=True)  # (B, 1)

    denom_std = std_reward + epsilon
    denom_mean = mean_reward + epsilon

    if advantage_type == "grpo":
        advantages = (rewards - mean_reward) / denom_std
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
    else:
        raise ValueError(
            f"Given advantage type {advantage_type} is not supported."
        )

    advantages = advantages.view(N).to(device)         # (B*K,)
    loss_mask = torch.ones_like(advantages).detach()   # (B*K,)

    return advantages, loss_mask


def get_log_probs(logits: torch.Tensor) -> torch.Tensor:
    """
    Compute log-probabilities from logits in a numerically stable way.

    logits: (N, C) unnormalized scores
    returns: (N, C) log-probabilities
    """
    max_logits, _ = logits.max(dim=1, keepdim=True)         # (N,1)
    shifted_logits = logits - max_logits                    # (N,C)
    exp_shifted = torch.exp(shifted_logits)                 # (N,C)
    sum_exp = exp_shifted.sum(dim=1, keepdim=True)          # (N,1)
    log_probs = shifted_logits - torch.log(sum_exp + 1e-12) # (N,C)
    return log_probs


def grpo_loss(logits: torch.Tensor, targets: torch.Tensor, rollout_size=8) -> torch.Tensor:
    """
    GRPO loss with log-probability correction and baseline subtraction.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    probs = torch.softmax(logits, dim=1)      # (N,C)
    log_probs = get_log_probs(logits)                     # (N,C)

    n = targets.shape[0]
    # Sample rollout_size samples from the predicted distribution
    probs_clone = probs.clone().detach()
    sampled_indices = torch.multinomial(probs_clone, num_samples=rollout_size, replacement=True)  # (N, rollout_size)
    # Compute reward N, rollout_size 1/0 if they match the target
    rewards = (sampled_indices == targets.unsqueeze(1)).float()  # (N, rollout_size)
    advantage = (rewards - rewards.mean(dim=1, keepdim=True)) / (rewards.std(dim=1, keepdim=True) + 1e-5)  # (N, rollout_size)
    loss = advantage.detach() * log_probs.gather(1, sampled_indices)  # (N, rollout_size)
    loss = -loss.mean()
    return loss


def p_normalization(logits: torch.Tensor, targets: torch.Tensor, rollout_size=8) -> torch.Tensor:
    """
    P-Normalization loss.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    probs = torch.softmax(logits, dim=1)      # (N,C)
    log_probs = get_log_probs(logits)                     # (N,C)

    n = targets.shape[0]
    # Sample rollout_size samples from the predicted distribution
    probs_clone = probs.clone()
    sampled_indices = torch.multinomial(probs_clone, num_samples=rollout_size, replacement=True)  # (N, rollout_size)
    # Compute reward N, rollout_size 1/0 if they match the target
    # Rewards should be binary 0/1 as float
    rewards = (sampled_indices == targets.unsqueeze(1)).float()  # (N, rollout_size)
    advantage = (rewards - rewards.mean(dim=1, keepdim=True)) / (rewards.mean(dim=1, keepdim=True) + 1e-5)  # (N, rollout_size)
    loss = advantage * log_probs.gather(1, sampled_indices)  # (N, rollout_size)
    loss = -loss.mean()
    return loss


def train_one_epoch(model, loader, criterion, optimizer, device, epoch,
                    scaler, use_amp, num_samples_per_example, advantage_type):
    model.train()
    running_loss, correct, total = 0.0, 0, 0

    for batch_idx, (inputs, targets) in tqdm(enumerate(loader), total=len(loader)):
        inputs, targets = inputs.to(device), targets.to(device)

        optimizer.zero_grad(set_to_none=True)

        if use_amp:
            raise ValueError("We are not supporting amp right now.")
        else:
            # # One forward pass on original batch
            actions_flat, log_probs_flat = take_actions_and_log_probs_multi(
                model=model,
                inputs=inputs,
                num_samples_per_example=num_samples_per_example,
            )

            # Expand targets cheaply (no extra model compute)
            targets_expanded = targets.repeat_interleave(num_samples_per_example)  # (B*K,)

            advantages, loss_mask = calculate_advantage(
                actions=actions_flat,                   # (B*K,1)
                targets=targets_expanded,               # (B*K,)
                num_samples_per_example=num_samples_per_example,
                advantage_type=advantage_type,
            )

            loss = -advantages.detach() * log_probs_flat * loss_mask
            loss = loss.sum() / loss_mask.sum().item()

            loss.backward()
            optimizer.step()

            ## Daman 
            # logits = model(inputs)

            # loss = p_normalization(
            #     logits=logits,
            #     targets=targets,
            #     rollout_size=num_samples_per_example,
            # # )

            # loss.backward()
            # optimizer.step()

        # Metrics: same logic as before but on expanded tensors
        running_loss += loss.item() * inputs.shape[0] * num_samples_per_example  # N = B*K
        # predicted = actions_flat.squeeze(1)                 # (B*K,)
        total += inputs.shape[0]
        # correct += predicted.eq(targets_expanded).sum().item()
        correct += 0.0

        wandb.log({
            "train/loss_step": running_loss
        })

    return running_loss / total, correct / total

@torch.no_grad()
def alternate_evaluate(model, val_loader, device, epoch, loss_fn, ks=[1, 4, 16, 64, 256, 1024]):
    model.eval()
    total_loss = 0.0
    total_correct = 0
    total_samples = 0
    pass_at_k = {k: 0 for k in ks}

    for images, targets in tqdm(val_loader, desc="Validation", total=len(val_loader)):
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        logits = model(images)
        loss = loss_fn(logits, targets)

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
    avg_passk = {f"pass@{k}": pass_at_k[k] / total_samples for k in ks}

    return avg_loss, avg_acc, avg_passk


@torch.no_grad()
def evaluate(model, loader, criterion, device, num_validation_rollouts):
    model.eval()
    running_loss = 0.0
    total = 0
    correct = 0

    # ks = [1, 2, 4, 8, ...]
    ks = []
    k = 1
    while k <= num_validation_rollouts:
        ks.append(k)
        k *= 2
    ks_tensor = torch.tensor(ks, device=device, dtype=torch.float32)  # (K,)

    passk_sum = torch.zeros(len(ks), device=device)  # (K,)

    for inputs, targets in loader:
        inputs, targets = inputs.to(device), targets.to(device)

        outputs = model(inputs)
        loss = criterion(outputs, targets)

        running_loss += loss.item() * inputs.size(0)

        # -------- Accuracy --------
        _, predicted = outputs.max(1)
        correct += predicted.eq(targets).sum().item()

        # -------- Vectorized pass@k --------
        probs = F.softmax(outputs, dim=1)                      # (B, C)
        p_correct = probs.gather(1, targets[:, None]).squeeze(1)  # (B,)

        # Shape trick:
        # p_correct -> (B, 1)
        # ks_tensor -> (1, K)
        # result    -> (B, K)
        passk_batch = 1.0 - (1.0 - p_correct[:, None]) ** ks_tensor[None, :]
        passk_sum += passk_batch.sum(dim=0)

        total += targets.size(0)

    avg_loss = running_loss / total
    avg_acc = correct / total
    avg_passk = {f"pass@{k}": passk_sum[i].item() / total for i, k in enumerate(ks)}

    return avg_loss, avg_acc, avg_passk


def save_checkpoint(state, is_best, checkpoint_dir):
    os.makedirs(checkpoint_dir, exist_ok=True)
    latest_path = os.path.join(checkpoint_dir, "checkpoint_latest.pth")
    torch.save(state, latest_path)
    if is_best:
        best_path = os.path.join(checkpoint_dir, "checkpoint_best.pth")
        torch.save(state, best_path)


# -------------------------
# Main
# -------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, default="./data")
    parser.add_argument("--dataset-name", type=str, default="cifar100")
    parser.add_argument("--num_samples_per_example", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=1000)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--model-type", type=str, default="resnet")
    parser.add_argument("--model-depth", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--lr_scheduler", type=str, default="cosine")
    parser.add_argument("--advantage-type", type=str, default="grpo")
    parser.add_argument("--momentum", type=float, default=0.9)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--milestones", type=int, nargs="+", default=[100, 150])
    parser.add_argument("--gamma", type=float, default=0.1)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--no-amp", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--checkpoint-dir", type=str, default="/tmp/checkpoints_resnet32")
    parser.add_argument("--wandb", action="store_true", help="Enable wandb logging")
    parser.add_argument("--wandb-project", type=str, default="cifar_logp")
    parser.add_argument("--wandb_runname", type=str, default="rl_training")
    parser.add_argument("--wandb-entity", type=str, default=None)
    parser.add_argument("--num_test_rollouts_per_example", type=int, default=131072)
    return parser.parse_args()


def main():
    args = parse_args()
    set_seed(args.seed)
    device = get_device()

    # --- W&B init ---
    if args.wandb:
        wandb.init(
            project=args.wandb_project,
            entity=args.wandb_entity,
            name=args.wandb_runname,
            config=vars(args),
        )

    train_loader, test_loader = get_dataloaders(
        args.dataset_name, args.data_dir, args.batch_size, args.num_workers
    )

    if args.dataset_name == "cifar10":
        num_classes = 10
    elif args.dataset_name == "cifar100":
        num_classes = 100
    else:
        raise ValueError(
            f"Given dataset name {args.dataset_name} is not supported yet."
        )
    
    if args.model_type == "resnet":
        model_depth = args.model_depth
        model = ResNetCIFAR(
            depth=model_depth,
            num_classes=num_classes,
        )

    elif args.model_type == "cnn":
        model = SmallCNN(
            num_classes=num_classes,
        )

    else:
        raise ValueError(
            f"Given model type {args.model_type} is not supported."
        )

    # ---- Multi-GPU support (DataParallel) ----
    if torch.cuda.is_available():
        if torch.cuda.device_count() > 1:
            print(f"Using {torch.cuda.device_count()} GPUs with DataParallel")
            model = nn.DataParallel(model)
        else:
            print("Using a single GPU")
        model = model.to(device)
    else:
        print("Using CPU only")
    
    criterion = nn.CrossEntropyLoss()

    optimizer = optim.AdamW(
        model.parameters(), lr=args.lr,
    )

    num_samples_per_example = args.num_samples_per_example
    advantage_type = args.advantage_type

    if args.lr_scheduler == "cosine":
        scheduler = CosineAnnealingLR(
            optimizer,
            T_max=args.epochs,
        )
    elif args.lr_scheduler == "multi_step":
        scheduler = MultiStepLR(optimizer, milestones=args.milestones, gamma=args.gamma)
    else:
        raise ValueError(
            f"Given lr scheduler {args.lr_scheduler} is not supported yet."
        )

    use_amp = torch.cuda.is_available() and not args.no_amp
    scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

    best_acc = 0.0

    for epoch in range(1, args.epochs + 1):
        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer,
            device, epoch, scaler, use_amp, 
            num_samples_per_example, advantage_type
        )

        # val_loss, val_acc, val_passk = alternate_evaluate(
        #     model,
        #     test_loader,
        #     criterion,
        #     device,
        #     num_validation_rollouts=args.num_test_rollouts_per_example,
        # )
        val_loss, val_acc, val_passk = alternate_evaluate(
            model=model,
            val_loader=test_loader,
            device=device,
            epoch=epoch,
            loss_fn=torch.nn.CrossEntropyLoss(),
        )

        scheduler.step()

        print(
            f"Epoch [{epoch}/{args.epochs}] "
            f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc*100:.2f}% | "
            f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc*100:.2f}%"
        )

        # --- W&B logging ---
        if args.wandb:
            wandb.log(
                {
                    "val/loss": val_loss,
                    "val/acc": val_acc,
                    **{f"val/{k}": v for k, v in val_passk.items()},
                }
            )

        is_best = val_acc > best_acc
        if is_best:
            best_acc = val_acc

        if isinstance(model, nn.DataParallel):
            model_state_dict = model.module.state_dict()
        else:
            model_state_dict = model.state_dict()

        save_checkpoint(
            {
                "epoch": epoch,
                "model_state_dict": model_state_dict,
                "optimizer_state_dict": optimizer.state_dict(),
                "scheduler_state_dict": scheduler.state_dict(),
                "best_acc": best_acc,
                "args": vars(args),
            },
            is_best,
            args.checkpoint_dir
        )

    # --- W&B: finish and save best model artifact ---
    if args.wandb:
        wandb.summary["best_val_acc"] = best_acc

    print(f"Training complete. Best accuracy: {best_acc*100:.2f}%")


if __name__ == "__main__":
    main()