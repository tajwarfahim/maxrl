#!/usr/bin/env python3
"""
Train a ResNet-32 on CIFAR-10 using PyTorch, now with Weights & Biases logging.

Usage:
    python train_resnet32_cifar10.py --data-dir ./data --epochs 200 --wandb
"""

import argparse
import os
import random
from tqdm import tqdm
import math
from datasets import load_dataset
import torchvision.models as models

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import (
    MultiStepLR,
    CosineAnnealingLR,
)
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision import transforms as T

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
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


# -------------------------
# Data
# -------------------------

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

    elif dataset_name == "cifar100":
        train_set = datasets.CIFAR100(data_dir, train=True, download=True,
                                      transform=train_transform)
        test_set  = datasets.CIFAR100(data_dir, train=False, download=True,
                                      transform=test_transform)

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
        test_set, batch_size=5000, shuffle=False,
        num_workers=num_workers, pin_memory=True
    )

    print("Num train batches: ", len(train_loader))
    print("Num test batches: ", len(test_loader))

    return train_loader, test_loader


# -------------------------
# Training / Evaluation
# -------------------------
def cross_entropy_loss(logits, targets):
    ce_loss = F.cross_entropy(logits, targets)
    return ce_loss.mean()


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
    parser.add_argument("--dataset-name", type=str, default="imagenet256")
    parser.add_argument("--epochs", type=int, default=200)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--model-type", type=str, default="resnet")
    parser.add_argument("--model-depth", type=int, default=50)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--lr_scheduler", type=str, default="cosine_with_warmup")
    parser.add_argument("--advantage-type", type=str, default="grpo")
    parser.add_argument("--momentum", type=float, default=0.9)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--milestones", type=int, nargs="+", default=[30, 60, 80])
    parser.add_argument("--gamma", type=float, default=0.1)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--no-amp", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--checkpoint-dir", type=str, default="/home/ftajwar/checkpoints_resnet32")
    parser.add_argument("--wandb", action="store_true", help="Enable wandb logging")
    parser.add_argument("--wandb-project", type=str, default="resnet32-cifar10")
    parser.add_argument("--wandb_runname", type=str, default="rl_training")
    parser.add_argument("--wandb-entity", type=str, default=None)
    parser.add_argument("--num_test_rollouts_per_example", type=int, default=1024)
    parser.add_argument("--eval_every_k", type=int, default=5000, help="Run validation every K optimizer steps")
    parser.add_argument("--max_grad_norm", type=float, default=1e5)
    return parser.parse_args()


def count_params(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total, trainable


def main():
    print("Starting script...")

    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

    args = parse_args()
    set_seed(args.seed)
    device = get_device()

    print("Starting training...")

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

    elif args.dataset_name == "imagenet32":
        num_classes = 1000

    elif args.dataset_name == "imagenet256":
        num_classes = 1000 

    else:
        raise ValueError(
            f"Given dataset name {args.dataset_name} is not supported yet."
        )
    
    # different resnet model
    if args.dataset_name == "imagenet256":
        model = models.resnet50(num_classes=1000)

    # custom resnet model for 32x32 images
    elif args.model_type == "resnet":
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
    
    total, trainable = count_params(model)

    print(f"Model: {model.__class__.__name__}")
    print(f"Total parameters: {total:,}")
    print(f"Trainable parameters: {trainable:,}")

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

    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=args.lr,
        momentum=0.9,
        weight_decay=1e-4,
        nesterov=False,
    )

    advantage_type = args.advantage_type

    print("Loss type: ", advantage_type)

    if args.lr_scheduler == "cosine":
        scheduler = CosineAnnealingLR(
            optimizer,
            T_max=(args.epochs * len(train_loader)),
            eta_min=(args.lr * 1e-4),
        )

    elif args.lr_scheduler == "multi_step":
        scheduler = MultiStepLR(optimizer, milestones=args.milestones, gamma=args.gamma)

    elif args.lr_scheduler == "cosine_with_warmup":
        total_steps = args.epochs * len(train_loader)
        warmup_steps = 5 * len(train_loader)   # 5 epochs

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

    best_acc = 0.0
    global_step = 0
    
    val_loss, val_acc, val_passk = evaluate(
        model, test_loader, criterion, device,
        num_validation_rollouts=args.num_test_rollouts_per_example
    )

    print(
        f"Before any training: "
        f"val_loss={val_loss:.4f}, val_acc={val_acc*100:.2f}%"
    )

    if val_acc > best_acc:
        best_acc = val_acc

    if args.wandb:
        wandb.log(
            {
                "val/loss": val_loss,
                "val/acc": val_acc,
                **{f"val/{k}": v for k, v in val_passk.items()},
                "step": 0,
                "epoch": 0,
            }
        )

    for epoch in range(1, args.epochs + 1):
        running_loss, correct, total = 0, 0, 0

        for batch_idx, (inputs, targets) in enumerate(train_loader):
            model.train()

            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad(set_to_none=True)

            logits = model(inputs)
            loss = cross_entropy_loss(logits, targets)

            loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)

            optimizer.step()
            scheduler.step()

            # 🔥 Increment step AFTER optimizer update
            global_step += 1

            # --- train metrics ---
            running_loss += loss.item() * targets.size(0)
            correct += logits.argmax(1).eq(targets).sum().item()
            total += targets.size(0)

            # -------------------------------
            # ✅ STEP-ALIGNED EVALUATION
            # -------------------------------
            if global_step % args.eval_every_k == 0:
                print(f"Running validation at step {global_step}")

                val_loss, val_acc, val_passk = evaluate(
                    model, test_loader, criterion, device,
                    num_validation_rollouts=args.num_test_rollouts_per_example
                )

                print(
                    f"[step {global_step}] "
                    f"train_loss={running_loss/total:.4f}, "
                    f"val_loss={val_loss:.4f}, val_acc={val_acc*100:.2f}%"
                )

                if val_acc > best_acc:
                    best_acc = val_acc

                if args.wandb:
                    wandb.log(
                        {
                            "train/loss": running_loss / total,
                            "train/acc": correct / total,
                            "lr": optimizer.param_groups[0]["lr"],
                            "train/grad_norm": grad_norm.item(),
                            "val/loss": val_loss,
                            "val/acc": val_acc,
                            **{f"val/{k}": v for k, v in val_passk.items()},
                            "step": global_step,
                            "epoch": epoch,
                        }
                    )
            
            else:
                if args.wandb:
                    wandb.log(
                        {
                            "train/loss": running_loss / total,
                            "train/acc": correct / total,
                            "lr": optimizer.param_groups[0]["lr"],
                            "train/grad_norm": grad_norm.item(),
                            "step": global_step,
                            "epoch": epoch,
                        }
                    )



    # --- W&B: finish and save best model artifact ---
    if args.wandb:
        wandb.summary["best_val_acc"] = best_acc

    print(f"Training complete. Best accuracy: {best_acc*100:.2f}%")


if __name__ == "__main__":
    main()
