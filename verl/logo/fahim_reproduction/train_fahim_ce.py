#!/usr/bin/env python3
"""
Train a ResNet-32 on CIFAR-10 using PyTorch, now with Weights & Biases logging.

Usage:
    python train_resnet32_cifar10.py --data-dir ./data --epochs 200 --wandb
"""

import argparse
import os
import random

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

def train_one_epoch(model, loader, criterion, optimizer, device, epoch, scaler, use_amp):
    model.train()
    running_loss, correct, total = 0.0, 0, 0

    for batch_idx, (inputs, targets) in enumerate(loader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad(set_to_none=True)

        if use_amp:
            with torch.cuda.amp.autocast():
                outputs = model(inputs)
                loss = criterion(outputs, targets)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        wandb.log({
            "train/loss_step": running_loss
        })

    return running_loss / total, correct / total


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
    parser.add_argument("--data-dir", type=str, default="/home/ftajwar/data/cifar10")
    parser.add_argument("--dataset-name", type=str, default="cifar10")
    parser.add_argument("--epochs", type=int, default=200)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--model-type", type=str, default="resnet")
    parser.add_argument("--model-depth", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--lr_scheduler", type=str, default="cosine")
    parser.add_argument("--momentum", type=float, default=0.9)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--milestones", type=int, nargs="+", default=[100, 150])
    parser.add_argument("--gamma", type=float, default=0.1)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--no-amp", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--checkpoint-dir", type=str, default="/home/ftajwar/checkpoints_resnet32")
    parser.add_argument("--wandb", action="store_true", help="Enable wandb logging")
    parser.add_argument("--wandb-project", type=str, default="cifar_logp")
    parser.add_argument("--wandb_runname", type=str, default="cross_entropy_training")
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
        ).to(device)

    elif args.model_type == "cnn":
        model = SmallCNN(
            num_classes=num_classes,
        ).to(device)
    
    else:
        raise ValueError(
            f"Given model type {args.model_type} is not supported."
        )
    
    criterion = nn.CrossEntropyLoss()

    optimizer = optim.AdamW(
        model.parameters(), lr=args.lr,
    )

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
            device, epoch, scaler, use_amp
        )
        
        val_loss, val_acc, val_passk = evaluate(
            model,
            test_loader,
            criterion,
            device,
            num_validation_rollouts=args.num_test_rollouts_per_example,
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
                    # "lr": optimizer.param_groups[0]["lr"],
                    # "epoch": epoch,
                    # "Step": epoch*len(train_loader),
                }
            )

        is_best = val_acc > best_acc
        if is_best:
            best_acc = val_acc

        # save_checkpoint(
        #     {
        #         "epoch": epoch,
        #         "model_state_dict": model.state_dict(),
        #         "optimizer_state_dict": optimizer.state_dict(),
        #         "scheduler_state_dict": scheduler.state_dict(),
        #         "best_acc": best_acc,
        #         "args": vars(args),
        #     },
        #     is_best,
        #     args.checkpoint_dir
        # )

    # --- W&B: finish and save best model artifact ---
    if args.wandb:
        wandb.summary["best_val_acc"] = best_acc

    print(f"Training complete. Best accuracy: {best_acc*100:.2f}%")


if __name__ == "__main__":
    main()