import torch
# ----------------------------
# Explicit Cross-Entropy Loss
# ----------------------------

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

def cross_entropy(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """
    Explicit implementation of cross-entropy for classification.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    log_probs = get_log_probs(logits)                     # (N,C)
    # Gather log-probability of the true class for each example
    n = targets.shape[0]
    true_log_probs = log_probs[torch.arange(n), targets]    # (N,)

    loss = -true_log_probs.mean()
    return loss

def prob_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """
    Another implementation of cross-entropy loss using probabilities.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    probs = torch.softmax(logits, dim=1)                    # (N,C)
    n = targets.shape[0]
    true_probs = probs[torch.arange(n), targets]            # (N,)
    loss = -true_probs.mean()
    return loss

def reinforce_loss(logits: torch.Tensor, targets: torch.Tensor, rollout_size=8) -> torch.Tensor:
    """
    Cross-entropy loss with log-probability correction.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    probs = torch.softmax(logits, dim=1)                    # (N,C)
    log_probs = get_log_probs(logits)                     # (N,C)

    n = targets.shape[0]
    # Sample rollout_size samples from the predicted distribution
    probs_clone = probs.clone()
    sampled_indices = torch.multinomial(probs_clone, num_samples=rollout_size, replacement=True)  # (N, rollout_size)
    # Estimate proportion of the target from each rollout
    target_one_hot = torch.zeros_like(probs).scatter_(1, targets.unsqueeze(1), 1.0)  # (N,C)
    sampled_target_probs = target_one_hot.gather(1, sampled_indices)  # (N, rollout_size)
    correction = sampled_target_probs.mean(dim=1)            # (N,)
    # For the samples that match the target, compute sum of log-probs and then divide by the correction factor
    true_log_probs = log_probs[torch.arange(n), targets]    # (N,)
    true_log_probs = true_log_probs * correction  # (N,)
    loss = -true_log_probs.mean()
    return loss

def reinforce_with_baseline_loss(logits: torch.Tensor, targets: torch.Tensor, rollout_size=8) -> torch.Tensor:
    """
    Cross-entropy loss with log-probability correction and baseline subtraction.

    logits: (N, C) unnormalized scores
    targets: (N,) integer class labels in [0, C-1]
    """
    probs = torch.softmax(logits, dim=1)                    # (N,C)
    log_probs = get_log_probs(logits)                     # (N,C)

    n = targets.shape[0]
    # Sample rollout_size samples from the predicted distribution
    probs_clone = probs.clone()
    sampled_indices = torch.multinomial(probs_clone, num_samples=rollout_size, replacement=True)  # (N, rollout_size)
    # Compute reward N, rollout_size 1/0 if they match the target
    rewards = (sampled_indices == targets.unsqueeze(1)).float()  # (N, rollout_size)
    advantage = rewards - rewards.mean(dim=1, keepdim=True)  # (N, rollout_size)
    loss = advantage * log_probs.gather(1, sampled_indices)  # (N, rollout_size)
    loss = -loss.mean()
    return loss

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
    probs_clone = probs.clone()
    sampled_indices = torch.multinomial(probs_clone, num_samples=rollout_size, replacement=True)  # (N, rollout_size)
    # Compute reward N, rollout_size 1/0 if they match the target
    rewards = (sampled_indices == targets.unsqueeze(1)).float()  # (N, rollout_size)
    advantage = (rewards - rewards.mean(dim=1, keepdim=True)) / (rewards.std(dim=1, keepdim=True) + 1e-5)  # (N, rollout_size)
    loss = advantage * log_probs.gather(1, sampled_indices)  # (N, rollout_size)
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