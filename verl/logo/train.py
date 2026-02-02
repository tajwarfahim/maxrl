import math
import random
from dataclasses import dataclass

from datasets import load_dataset

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from verl.logo.resnet import ResNetCIFAR

import wandb
from tqdm import tqdm
import argparse

# from losses import logprob_loss, prob_loss, reinforce_loss, reinforce_with_baseline_loss
from verl.logo.losses import cross_entropy, reinforce_loss, reinforce_with_baseline_loss, grpo_loss, p_normalization
import random
from collections import defaultdict
from torch.utils.data import Subset
# ----------------------------
# Config
# ----------------------------
from torch.utils.data import Dataset
import numpy as np
from PIL import Image

from datasets import DatasetDict

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
    project: str = "imagenet_logp_daman_code_resnet_50"
    run_name: str = "baseline-small-cnn-ce-8-rollouts"
    batch_size: int = 256
    num_workers: int = 4
    lr: float = 0.1
    weight_decay: float = 5e-4
    num_epochs: int = 100
    seed: int = 42
    log_interval: int = 1  # steps
    model_save_path: str = "/tmp/best_model.pth"
    # loss_type: str = "reinforce"  # options: cross_entropy
    loss_type: str = "log_prob"  # options: log_prob, prob, reinforce, reinforce_with_baseline
    rollout_size: int = 8  # for logprob_correction loss
    dataset: str = "cifar100"
    scheduler: str = "cosine"      # "none" | "cosine"
    warmup_epochs: int = 5         # 0 to disable warmup
    min_lr: float = 1e-6           # cosine floor
    eval_interval: int = 2000   # run validation every N train steps




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
def get_dataloaders(cfg: Config):
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=(0.4914, 0.4822, 0.4465),
            std=(0.2023, 0.1994, 0.2010),
        ),
    ])

    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            mean=(0.4914, 0.4822, 0.4465),
            std=(0.2023, 0.1994, 0.2010),
        ),
    ])

    if cfg.dataset.lower() in ["imagenet32", "imagenet-1k-32x32"]:
        hf_ds = load_dataset("benjamin-paine/imagenet-1k-32x32")
        hf_ds, _, chosen = subset_imagenet_classes(
            hf_ds, k=cfg.imagenet_k, seed=cfg.seed, strategy=cfg.imagenet_subset_strategy
        )

        num_classes = cfg.imagenet_k

        train_dataset = HFImageNet32(hf_ds["train"], transform_train)
        val_dataset   = HFImageNet32(hf_ds["validation"], transform_test)
        print("Train dataset size:", len(train_dataset), "val dataset size:", len(val_dataset), "num classes:", num_classes)

    elif cfg.dataset.lower() == "cifar10":
        train_dataset = datasets.CIFAR10(
            root="./data", train=True, download=True, transform=transform_train
        )
        val_dataset = datasets.CIFAR10(
            root="./data", train=False, download=True, transform=transform_test
        )        
        num_classes = 10
    elif cfg.dataset.lower() == "cifar100":
        train_dataset = datasets.CIFAR100(
            root="./data", train=True, download=True, transform=transform_train
        )
        val_dataset = datasets.CIFAR100(
            root="./data", train=False, download=True, transform=transform_test
        )
        num_classes = 100

    train_loader = DataLoader(
        train_dataset,
        batch_size=cfg.batch_size,
        shuffle=True,
        num_workers=cfg.num_workers,
        pin_memory=True,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=cfg.batch_size,
        shuffle=False,
        num_workers=cfg.num_workers,
        pin_memory=True,
    )
    return train_loader, val_loader, num_classes


# ----------------------------
# Train / Eval loops
# ----------------------------
def train_one_epoch(model, optimizer, scheduler, train_loader, val_loader, device, epoch, loss_fn, cfg: Config, global_step=0):
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

        loss = loss_fn(logits, targets)
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
            val_loss, val_acc = evaluate(model, val_loader, device, epoch + global_step / len(train_loader), loss_fn)
            model.train()  # important: go back to train mode after eval
    
    # Running in the end
    val_loss, val_acc = evaluate(model, val_loader, device, epoch + global_step / len(train_loader), loss_fn)
    model.train()       

    epoch_loss = running_loss / running_total
    epoch_acc = running_correct / running_total
    return epoch_loss, epoch_acc, global_step, val_loss, val_acc


@torch.no_grad()
def evaluate(model, val_loader, device, epoch, loss_fn, ks=[1, 4, 16, 64, 256, 1024]):
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
    parser.add_argument("--loss_type", type=str, default=cfg.loss_type,
                        help="Type of loss to use: cross_entropy, reinforce, reinforce_with_baseline, grpo")
    parser.add_argument("--rollout_size", type=int, default=cfg.rollout_size,)
    parser.add_argument("--batch_size", type=int, default=cfg.batch_size,)
    parser.add_argument("--lr", type=float, default=cfg.lr,)
    parser.add_argument("--scheduler", type=str, default="cosine_with_warmup")
    parser.add_argument("--warmup_epochs", type=int, default=cfg.warmup_epochs)
    parser.add_argument("--min_lr", type=float, default=cfg.min_lr)

    parser.add_argument("--dataset", type=str, default="cifar100",)
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



    if cfg.loss_type in ["reinforce", "reinforce_with_baseline", "grpo", "p_normalization"]:
        # cfg.run_name = f"{cfg.loss_type}-bs{cfg.batch_size}-lr{cfg.lr}-rs{cfg.rollout_size}-d{args.depth}-{cfg.dataset}"
        cfg.run_name = f"{cfg.imagenet_k}-{cfg.loss_type}-rs{cfg.rollout_size}_1e-6"
    else:
        # cfg.run_name = f"{cfg.loss_type}-bs{cfg.batch_size}-lr{cfg.lr}-d{args.depth}-{cfg.dataset}"
        cfg.run_name = f"{cfg.imagenet_k}-{cfg.loss_type}"


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

    train_loader, val_loader, num_classes = get_dataloaders(cfg)

    model = ResNetCIFAR(depth=cfg.depth, num_classes=num_classes).to(device)

    # optimizer = torch.optim.Adam(
    #     model.parameters(),
    #     lr=cfg.lr,
    #     weight_decay=cfg.weight_decay,
    # )

    # if cfg.scheduler == "cosine":
    #     total_steps = cfg.num_epochs * len(train_loader)  # compute this
    #     scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
    #         optimizer,
    #         T_max=total_steps,
    #         eta_min=cfg.min_lr,
    #     )
    # else:
    #     scheduler = None

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
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer,
            T_max=(args.epochs * len(train_loader)),
            eta_min=(args.lr * 1e-4),
        )

    elif cfg.scheduler == "multi_step":
        scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=args.milestones, gamma=args.gamma)

    elif cfg.scheduler == "cosine_with_warmup":
        total_steps = cfg.num_epochs * len(train_loader)
        warmup_steps = len(train_loader)   # 1 epochs

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


    if cfg.loss_type == "cross_entropy":
        loss_fn = lambda x, y: cross_entropy(x, y)
    elif cfg.loss_type == "reinforce":
        loss_fn = lambda x, y: reinforce_loss(x, y, rollout_size=cfg.rollout_size)
    elif cfg.loss_type == "reinforce_with_baseline":
        loss_fn = lambda x, y: reinforce_with_baseline_loss(x, y, rollout_size=cfg.rollout_size)
    elif cfg.loss_type == "grpo":
        loss_fn = lambda x, y: grpo_loss(x, y, rollout_size=cfg.rollout_size)
    elif cfg.loss_type == "p_normalization":
        loss_fn =lambda x, y: p_normalization(x, y, rollout_size=cfg.rollout_size)
    else:
        raise ValueError(f"Unknown loss type: {cfg.loss_type}")
    
    global_step = 0
    for epoch in tqdm(range(cfg.num_epochs), desc="Training Epochs", total=cfg.num_epochs):

        train_loss, train_acc, global_step, val_loss, val_acc = train_one_epoch(
            model, optimizer, scheduler, train_loader, val_loader, device, epoch, loss_fn, cfg, global_step
        )
        # val_loss, val_acc = evaluate(model, val_loader, device, epoch + 1, loss_fn)

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
