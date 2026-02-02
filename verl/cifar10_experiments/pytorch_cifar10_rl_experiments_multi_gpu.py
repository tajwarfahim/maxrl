#!/usr/bin/env python3
"""
DDP training of ResNet-32 / SmallCNN on CIFAR-10/100 with vectorized advantage.

Example:
    torchrun --nproc_per_node=2 train_resnet32_cifar10_ddp.py \
        --data-dir ./data --epochs 200 --batch-size 128 --wandb
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
from torch.utils.data.distributed import DistributedSampler
from torchvision import datasets, transforms

import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

# --- W&B ---
import wandb

# ResNet model
from verl.cifar10_experiments.resnet_model import ResNetCIFAR

# CNN model
from verl.cifar10_experiments.cnn_model import SmallCNN


# -------------------------
# Utils
# -------------------------

def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def init_distributed_mode(args):
    """
    Initialize torch.distributed if launched with torchrun / distributed.launch.
    If not, we just run in single-process mode (world_size=1).
    """
    if 'RANK' in os.environ and 'WORLD_SIZE' in os.environ:
        args.rank = int(os.environ['RANK'])
        args.world_size = int(os.environ['WORLD_SIZE'])
        args.local_rank = int(os.environ.get('LOCAL_RANK', 0))
        args.distributed = True
    else:
        # Fallback to single-process
        args.rank = 0
        args.world_size = 1
        args.local_rank = 0
        args.distributed = False

    if torch.cuda.is_available():
        torch.cuda.set_device(args.local_rank)

    if args.distributed:
        dist.init_process_group(backend='nccl', init_method='env://')
        dist.barrier()


def is_main_process(args):
    return args.rank == 0


def cleanup_distributed():
    if dist.is_available() and dist.is_initialized():
        dist.destroy_process_group()


def get_device(args):
    if torch.cuda.is_available():
        return torch.device(f"cuda:{args.local_rank}")
    else:
        return torch.device("cpu")


# -------------------------
# Data
# -------------------------

def get_dataloaders(
    dataset_name,
    data_dir,
    batch_size=128,
    num_workers=4,
    distributed=False,
    rank=0,
    world_size=1,
):
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

    # DistributedSampler for training
    train_sampler = None
    if distributed:
        train_sampler = DistributedSampler(
            train_set,
            num_replicas=world_size,
            rank=rank,
            shuffle=True,
        )

    train_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=(train_sampler is None),
        sampler=train_sampler,
        num_workers=num_workers,
        pin_memory=True,
    )

    # For validation we just use a regular DataLoader on each process.
    # Optionally, you could use a DistributedSampler and all_reduce metrics.
    test_loader = DataLoader(
        test_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
    )

    return train_loader, test_loader, train_sampler


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


def train_one_epoch(
    model,
    loader,
    criterion,
    optimizer,
    device,
    epoch,
    scaler,
    use_amp,
    num_samples_per_example,
    advantage_type,
    args,
):
    model.train()
    running_loss, correct, total = 0.0, 0.0, 0.0

    if is_main_process(args):
        data_iter = tqdm(loader, total=len(loader), desc=f"Train Epoch {epoch}")
    else:
        data_iter = loader

    for batch_idx, (inputs, targets) in enumerate(data_iter):
        inputs, targets = inputs.to(device, non_blocking=True), targets.to(device, non_blocking=True)
        optimizer.zero_grad(set_to_none=True)

        if use_amp:
            raise ValueError("We are not supporting amp right now.")
        else:
            actions_flat, log_probs_flat = take_actions_and_log_probs_multi(
                model=model,
                inputs=inputs,
                num_samples_per_example=num_samples_per_example,
            )

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

        # Metrics
        batch_loss = loss.item()
        running_loss += batch_loss * actions_flat.size(0)  # N = B*K
        predicted = actions_flat.squeeze(1)                # (B*K,)
        total += targets_expanded.size(0)
        correct += predicted.eq(targets_expanded).sum().item()

    # Aggregate metrics across processes
    if args.distributed and dist.is_initialized():
        metrics = torch.tensor(
            [running_loss, correct, total],
            dtype=torch.float64,
            device=device,
        )
        dist.all_reduce(metrics, op=dist.ReduceOp.SUM)
        running_loss, correct, total = metrics.tolist()

    avg_loss = running_loss / max(total, 1.0)
    avg_acc = correct / max(total, 1.0)

    return avg_loss, avg_acc


@torch.no_grad()
def evaluate(model, loader, criterion, device, args):
    model.eval()
    running_loss, correct, total = 0.0, 0.0, 0.0

    if is_main_process(args):
        data_iter = tqdm(loader, total=len(loader), desc="Eval")
    else:
        data_iter = loader

    for inputs, targets in data_iter:
        inputs, targets = inputs.to(device, non_blocking=True), targets.to(device, non_blocking=True)
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        running_loss += loss.item() * inputs.size(0)
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    # Aggregate metrics across processes
    if args.distributed and dist.is_initialized():
        metrics = torch.tensor(
            [running_loss, correct, total],
            dtype=torch.float64,
            device=device,
        )
        dist.all_reduce(metrics, op=dist.ReduceOp.SUM)
        running_loss, correct, total = metrics.tolist()

    avg_loss = running_loss / max(total, 1.0)
    avg_acc = correct / max(total, 1.0)

    return avg_loss, avg_acc


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
    parser.add_argument("--data-dir", type=str, default="/home/ftajwar/data/cifar10")
    parser.add_argument("--dataset-name", type=str, default="cifar10")
    parser.add_argument("--num_samples_per_example", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=200)
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
    parser.add_argument("--checkpoint-dir", type=str, default="/home/ftajwar/checkpoints_resnet32")
    parser.add_argument("--wandb", action="store_true", help="Enable wandb logging")
    parser.add_argument("--wandb-project", type=str, default="resnet32-cifar10")
    parser.add_argument("--wandb_runname", type=str, default="cross_entropy_training")
    parser.add_argument("--wandb-entity", type=str, default=None)

    # For torch.distributed.launch / torchrun
    parser.add_argument("--local_rank", type=int, default=0)

    return parser.parse_args()


def main():
    args = parse_args()
    init_distributed_mode(args)

    # Make seeds rank-dependent so each worker has different RNG streams
    set_seed(args.seed + args.rank)

    device = get_device(args)

    # --- W&B init (main process only) ---
    if args.wandb and is_main_process(args):
        wandb.init(
            project=args.wandb_project,
            entity=args.wandb_entity,
            name=args.wandb_runname,
            config=vars(args),
        )

    train_loader, test_loader, train_sampler = get_dataloaders(
        args.dataset_name,
        args.data_dir,
        args.batch_size,
        args.num_workers,
        distributed=args.distributed,
        rank=args.rank,
        world_size=args.world_size,
    )

    if args.dataset_name == "cifar10":
        num_classes = 10
    elif args.dataset_name == "cifar100":
        num_classes = 100
    else:
        raise ValueError(
            f"Given dataset name {args.dataset_name} is not supported yet."
        )

    # Model
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

    model = model.to(device)

    if args.distributed:
        model = DDP(
            model,
            device_ids=[args.local_rank] if torch.cuda.is_available() else None,
            output_device=args.local_rank if torch.cuda.is_available() else None,
            find_unused_parameters=False,
        )

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
        # DistributedSampler requires setting epoch for proper shuffling
        if train_sampler is not None:
            train_sampler.set_epoch(epoch)

        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer,
            device, epoch, scaler, use_amp,
            num_samples_per_example, advantage_type, args
        )

        val_loss, val_acc = evaluate(model, test_loader, criterion, device, args)

        scheduler.step()

        if is_main_process(args):
            print(
                f"Epoch [{epoch}/{args.epochs}] "
                f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc*100:.2f}% | "
                f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc*100:.2f}%"
            )

            # --- W&B logging ---
            if args.wandb:
                wandb.log({
                    "train/loss": train_loss,
                    "train/acc": train_acc,
                    "val/loss": val_loss,
                    "val/acc": val_acc,
                    "lr": optimizer.param_groups[0]["lr"],
                    "epoch": epoch,
                })

            is_best = val_acc > best_acc
            if is_best:
                best_acc = val_acc

            # Save checkpoint (use underlying module when in DDP)
            if isinstance(model, DDP):
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
    if args.wandb and is_main_process(args):
        wandb.summary["best_val_acc"] = best_acc
        print(f"Training complete. Best accuracy: {best_acc*100:.2f}%")

    cleanup_distributed()


if __name__ == "__main__":
    main()
