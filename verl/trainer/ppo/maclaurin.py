import torch
import math

_LOG_HALF = -0.6931471805599453  # log(0.5)

def _log1mexp(x: torch.Tensor) -> torch.Tensor:
    """
    x <= 0, return log(1 - exp(x)) in a numerically stable way.
    """
    return torch.where(
        x < _LOG_HALF,
        torch.log1p(-torch.exp(x)),
        torch.log(-torch.expm1(x)),
    )

def _logcomb_int_scalar(N: int, k: int, device) -> torch.Tensor:
    """
    log( C(N, k) ) as a float64 tensor scalar on given device.
    """
    Nf = torch.tensor(float(N), device=device, dtype=torch.float64)
    kf = torch.tensor(float(k), device=device, dtype=torch.float64)
    return torch.lgamma(Nf + 1.0) - torch.lgamma(kf + 1.0) - torch.lgamma(Nf - kf + 1.0)

def maclaurin_weights(C: torch.Tensor, n: int, T: int) -> torch.Tensor:
    """
    Batch compute (w_success, w_fail) for each problem.

    Args:
      C: (m,) tensor, number of successes (correct) for each problem
      n: int, total number of attempts per problem (batch size)
      T: int, Maclaurin truncation order (T > 0)

    Returns:
      w_succ: (m,) tensor
      w_fail: (m,) tensor

    Usage (for each problem i):
      g_hat[i] = w_success[i] * sum_{succ} S + w_fail[i] * sum_{fail} S
      where S is the score vector = grad log p (summed over samples)
    """
    assert T > 0, "T must be > 0"
    assert n >= 0, "n must be >= 0"
    if C.dim() != 1:
        raise ValueError("C must be a 1D (m,) Tensor")

    device = C.device
    m = C.numel()
    N = int(n)

    # Edge case: n=0
    if N == 0:
        z = torch.zeros((m,), device=device, dtype=torch.float64)
        return z, z

    # Validate C
    C_int = C.to(torch.int64)
    if torch.any(C_int < 0) or torch.any(C_int > N):
        raise ValueError("Elements in C must satisfy 0 <= C[i] <= n")

    # w_success = 1/N (same for all problems)
    w_succ = torch.full((m,), 1.0 / N, device=device, dtype=torch.float64)

    # Number of failures: f = N - C
    f = (N - C_int).to(torch.int64)

    # When k>=2 terms don't exist, w_fail=0
    if T < 2 or N < 2:
        w_fail = torch.zeros((m,), device=device, dtype=torch.float64)
        return w_succ, w_fail

    # K_i = min(T, f_i, N) for each problem; since f_i <= N, this is equivalent to min(T, f_i)
    K = torch.minimum(f, torch.tensor(T, device=device, dtype=torch.int64))

    # r_2 = C(f-1,1)/C(N-1,1) = (f-1)/(N-1)
    r = (f.to(torch.float64) - 1.0) / (float(N - 1))

    # Kahan summation (element-wise)
    sum_r = torch.zeros((m,), device=device, dtype=torch.float64)
    c = torch.zeros((m,), device=device, dtype=torch.float64)

    # Loop k=2..min(T, N) (avoid updating r_{k+1} when k=N to prevent N-k=0)
    k_max = min(T, N)
    for k in range(2, k_max + 1):
        active = K >= k  # Only problems with K_i >= k contribute this term

        # Kahan: sum_r += r (only for active problems)
        y = r - c
        tmp = sum_r + y
        c_new = (tmp - sum_r) - y
        sum_r = torch.where(active, tmp, sum_r)
        c = torch.where(active, c_new, c)

        # Update to r_{k+1}: r *= (f-k)/(N-k)
        if k < k_max:
            # Note: for active problems, f >= k, so (f-k) is non-negative where needed
            factor = (f.to(torch.float64) - float(k)) / float(N - k)
            r = r * factor

    # w_fail = -(1/N) * sum_{k=2..K} r_k
    w_fail = -(sum_r / float(N))

    return w_succ, w_fail

def maclaurin_weights_loo(C: torch.Tensor, n: int, T: int):
    """
    Leave-one-out baseline version for Maclaurin (failure-series) weights.

    Returns:
      w_succ: (m,) float64
      w_fail: (m,) float64

    Use:
      adv = w_succ[:,None]*P + w_fail[:,None]*(1-P)
    """
    assert T > 0, "T must be > 0"
    assert n >= 0, "n must be >= 0"
    if C.dim() != 1:
        raise ValueError("C must be 1D (m,)")

    device = C.device
    m = C.numel()
    N = int(n)

    if N == 0:
        z = torch.zeros((m,), device=device, dtype=torch.float64)
        return z, z

    C_int = C.to(torch.int64)
    if torch.any(C_int < 0) or torch.any(C_int > N):
        raise ValueError("need 0 <= C[i] <= n")

    # base (k=1) RL term
    w_succ = torch.full((m,), 1.0 / N, device=device, dtype=torch.float64)
    w_fail = torch.zeros((m,), device=device, dtype=torch.float64)

    if T < 2 or N < 2:
        return w_succ, w_fail

    # failures per prompt
    F = (N - C_int).to(torch.int64)
    Ff = F.to(torch.float64)

    # LOO baseline only defined when C(N,k) > 1  <=>  k < N
    k_max = min(T, N - 1)
    if k_max < 2:
        # (e.g., N=2) nothing to do
        # If T>=N, we still may want to include original k=N term below.
        pass

    for k in range(2, k_max + 1):
        # scalar log( C(N,k) - 1 ) computed stably
        logM = _logcomb_int_scalar(N, k, device)          # log C(N,k)
        # log(C(N,k)-1) = logM + log(1 - exp(-logM))
        logMm1 = logM + _log1mexp(-logM)

        # logA = log C(F,k) for each prompt (mask invalid F<k)
        valid = F >= k
        if not torch.any(valid):
            continue

        lg_k1 = torch.lgamma(torch.tensor(float(k) + 1.0, device=device, dtype=torch.float64))

        logA = torch.full((m,), float("-inf"), device=device, dtype=torch.float64)
        Fv = Ff[valid]
        logA[valid] = torch.lgamma(Fv + 1.0) - lg_k1 - torch.lgamma(Fv - float(k) + 1.0)

        # ratio = C(F,k)/(C(N,k)-1)
        ratio = torch.zeros((m,), device=device, dtype=torch.float64)
        ratio[valid] = torch.exp(logA[valid] - logMm1)

        # w_succ += ratio / N
        w_succ = w_succ + ratio / float(N)

        # w_fail += ratio*(1/N - 1/F)  (only valid has F>=k>=2 so safe)
        invF = torch.zeros((m,), device=device, dtype=torch.float64)
        invF[valid] = 1.0 / Ff[valid]
        w_fail = w_fail + ratio * (1.0 / float(N) - invF)

    # If T >= N: k=N term exists in the original Maclaurin series,
    # but LOO baseline for k=N is undefined (only one tuple). So we keep the original k=N term.
    if T >= N and N >= 2:
        all_fail = (F == N).to(torch.float64)  # only when every sample failed
        w_fail = w_fail - all_fail / float(N)

    return w_succ, w_fail

def vr_cond_weights(C: torch.Tensor, n: int):
    """
    Compute variance-reduced conditional weights.

    For a group with a correct and b incorrect (a + b = n):
      - Each correct sample gets weight: b / (a * (a + b))
      - Each incorrect sample gets weight: -1 / (a + b)

    Special case: if a = 0, incorrect weight is still -1/(a+b)

    Args:
      C: (m,) tensor, number of successes (correct) for each problem
      n: int, total number of attempts per problem

    Returns:
      w_succ: (m,) tensor, weight for each success
      w_fail: (m,) tensor, weight for each failure
    """
    if C.dim() != 1:
        raise ValueError("C must be a 1D (m,) Tensor")

    device = C.device
    m = C.numel()
    N = int(n)

    # Edge case: n=0
    if N == 0:
        z = torch.zeros((m,), device=device, dtype=torch.float64)
        return z, z

    # Validate C
    C_int = C.to(torch.int64)
    if torch.any(C_int < 0) or torch.any(C_int > N):
        raise ValueError("Elements in C must satisfy 0 <= C[i] <= n")

    # a = number of correct, b = number of incorrect
    a = C.to(torch.float64)
    b = float(N) - a

    # w_fail = -1 / (a + b) = -1 / N
    w_fail = torch.full((m,), -1.0 / float(N), device=device, dtype=torch.float64)

    # w_succ = b / (a * (a + b)) = b / (a * N)
    # When a = 0, we set w_succ = 0 (no successes to weight anyway)
    w_succ = torch.zeros((m,), device=device, dtype=torch.float64)
    valid = a > 0
    w_succ[valid] = b[valid] / (a[valid] * float(N))

    return w_succ, w_fail

def _logfact_upto(n: int, device) -> torch.Tensor:
    # log_fact[i] = log(i!)
    x = torch.arange(n + 1, device=device, dtype=torch.float64)
    return torch.lgamma(x + 1.0)

def _logcomb_from_logfact(a_int: torch.Tensor, k: int, log_fact: torch.Tensor) -> torch.Tensor:
    """
    log C(a,k) for integer a (tensor), return -inf if invalid (a<k or a<0).
    a_int: int64 tensor
    """
    out = torch.full(a_int.shape, float("-inf"), device=a_int.device, dtype=torch.float64)
    if k < 0:
        return out
    valid = (a_int >= k) & (a_int >= 0)
    if torch.any(valid):
        a = a_int[valid]
        out[valid] = log_fact[a] - log_fact[k] - log_fact[a - k]
    return out

def _AF_AS(
    F: torch.Tensor,
    S: torch.Tensor,
    n: int,
    k: int,
    log_fact: torch.Tensor,
    log_denom_k: torch.Tensor | None = None,
):
    """
    Stable computation for A_F, A_S contributions.

    This function returns:
        AF_contrib = A_F / (k * C(n,k))
        AS_contrib = A_S / (k * C(n,k))

    where A_F, A_S are defined in the paper (eq. 84,85) with denominator C(n-k, k).

    Args:
      F, S: (m,) int64, failures and successes per prompt (F+S = n)
      n: total samples per prompt
      k: order
      log_fact: log factorial table (size n+1) on device
      log_denom_k: optional scalar tensor = log(k*C(n,k)) on device (float64)

    Returns:
      AF_contrib, AS_contrib: (m,) float64
    """
    device = F.device
    m = F.numel()

    # disjoint-tuples baseline defined only when C(n-k,k) > 0  <=>  n >= 2k
    if n < 2 * k:
        z = torch.zeros((m,), device=device, dtype=torch.float64)
        return z, z

    # log C(n-k, k)
    logDen = log_fact[n - k] - log_fact[k] - log_fact[n - 2 * k]  # scalar float64 tensor

    # log(k * C(n,k))   (avoid math.comb -> float)
    if log_denom_k is None:
        logCnk = log_fact[n] - log_fact[k] - log_fact[n - k]      # scalar
        logk = torch.log(torch.tensor(float(k), device=device, dtype=torch.float64))
        log_denom_k = logCnk + logk                               # scalar

    # accumulate in log-space: log(sum exp(.))
    log_AF = torch.full((m,), float("-inf"), device=device, dtype=torch.float64)
    log_AS = torch.full((m,), float("-inf"), device=device, dtype=torch.float64)

    for t in range(0, k):
        # AF term (paper eq.84):
        #   C(F-1,t) * C(S,k-1-t) * C(F-1-t,k) / C(n-k,k)
        # then divided by (k*C(n,k)) => subtract log_denom_k as well
        lt = (
            _logcomb_from_logfact(F - 1, t, log_fact)
            + _logcomb_from_logfact(S, (k - 1 - t), log_fact)
            + _logcomb_from_logfact(F - 1 - t, k, log_fact)
            - logDen
            - log_denom_k
        )
        log_AF = torch.logaddexp(log_AF, lt)

        # AS term (paper eq.85):
        #   C(F,t) * C(S-1,k-1-t) * C(F-t,k) / C(n-k,k)
        # then divided by (k*C(n,k))
        lt2 = (
            _logcomb_from_logfact(F, t, log_fact)
            + _logcomb_from_logfact(S - 1, (k - 1 - t), log_fact)
            + _logcomb_from_logfact(F - t, k, log_fact)
            - logDen
            - log_denom_k
        )
        log_AS = torch.logaddexp(log_AS, lt2)

    AF_contrib = torch.exp(log_AF)
    AS_contrib = torch.exp(log_AS)

    # exp(-inf)=0 already, but keep safety for NaN/inf
    AF_contrib = torch.where(torch.isfinite(AF_contrib), AF_contrib, torch.zeros_like(AF_contrib))
    AS_contrib = torch.where(torch.isfinite(AS_contrib), AS_contrib, torch.zeros_like(AS_contrib))

    return AF_contrib, AS_contrib


def maclaurin_weights_cross_fitted(C: torch.Tensor, n: int, T: int):
    """
    Stable cross-fitted baseline weights consistent with paper (81)-(86) / your (74).

    For each k>=2:
      w_fail += -( C(F-1,k-1) / (k*C(n,k)) ) + ( A_F / (k*C(n,k)) )
      w_succ += + ( A_S / (k*C(n,k)) )

    plus k=1 RL term:
      w_succ += 1/n

    Notes:
      - When n < 2k, disjoint-tuples baseline is undefined (C(n-k,k)=0). We fallback to baseline-free
        signal term for that k (same behavior as your current code).
    """
    assert T > 0, "T must be > 0"
    device = C.device
    N = int(n)

    # Edge case
    if N == 0:
        z = torch.zeros_like(C, dtype=torch.float64, device=device)
        return z, z

    C_int = C.to(torch.int64)
    F = (N - C_int)          # failures
    S = C_int                # successes

    m = C.numel()
    log_fact = _logfact_upto(N, device)

    # k=1 RL term: success weight 1/n, fail weight 0
    w_succ = torch.full((m,), 1.0 / float(N), device=device, dtype=torch.float64)
    w_fail = torch.zeros((m,), device=device, dtype=torch.float64)

    k_max = min(T, N)
    for k in range(2, k_max + 1):
        # log(k * C(n,k))
        logCnk = log_fact[N] - log_fact[k] - log_fact[N - k]  # scalar
        logk = torch.log(torch.tensor(float(k), device=device, dtype=torch.float64))
        log_denom_k = logCnk + logk

        # signal term: C(F-1,k-1)/(k*C(n,k))   (avoid huge cF then divide)
        log_cF = _logcomb_from_logfact(F - 1, k - 1, log_fact)  # (m,)
        sig = torch.exp(log_cF - log_denom_k)
        sig = torch.where(torch.isfinite(sig), sig, torch.zeros_like(sig))
        w_fail -= sig

        # baseline terms (only when n>=2k): add A_F/(k*C(n,k)) to fail, A_S/(k*C(n,k)) to succ
        if N >= 2 * k:
            AF_contrib, AS_contrib = _AF_AS(F, S, N, k, log_fact, log_denom_k=log_denom_k)
            w_fail += AF_contrib
            w_succ += AS_contrib
        # else: fallback baseline-free for this k (do nothing)

    return w_succ, w_fail

def c_sub_TN(
    K: torch.Tensor,   # (m,) int64 successes per prompt
    N: int,
    T: int,
    log_fact: torch.Tensor,  # from _logfact_upto(N, device)
) -> torch.Tensor:
    """
    Compute c_{T,N}(K) in eq. (51) stably, vectorized over prompts.

    c_{T,N}(K) = 1/C(N,T) * sum_{k=1..min(T,K)} (1/k) * C(K-1,k-1) * C(F, T-k)
    with F = N-K, and c(0)=0.
    """
    device = K.device
    K = K.to(torch.int64)
    m = K.numel()

    # edge cases
    if T <= 0 or N <= 0:
        return torch.zeros((m,), device=device, dtype=torch.float64)

    F = (N - K).to(torch.int64)

    # log C(N,T) (scalar)
    logC_NT = log_fact[N] - log_fact[T] - log_fact[N - T]

    # log-sum-exp accumulator
    log_sum = torch.full((m,), float("-inf"), device=device, dtype=torch.float64)

    k_max = min(T, N)
    for k in range(1, k_max + 1):
        # term exists only if k<=K and T-k<=F; invalids become -inf via _logcomb_from_logfact
        log_term = (
            _logcomb_from_logfact(K - 1, k - 1, log_fact)         # log C(K-1,k-1)
            + _logcomb_from_logfact(F, T - k, log_fact)           # log C(F, T-k)
            - logC_NT                                             # / C(N,T)
            - torch.log(torch.tensor(float(k), device=device, dtype=torch.float64))  # / k
        )
        log_sum = torch.logaddexp(log_sum, log_term)

    c = torch.exp(log_sum)
    c = torch.where(torch.isfinite(c), c, torch.zeros_like(c))

    # enforce c(0)=0
    c = torch.where(K > 0, c, torch.zeros_like(c))
    return c


def oversample_subset_vr_weights(
    K: torch.Tensor,   # (m,) successes per prompt (int64 ok)
    N: int,
    T: int,
    beta: float = 1.0,
) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Return (w_succ, w_fail) per prompt for the estimator:
      g_sub,vr = c_{T,N}(K) * Σ_R - beta * (1/N) * Σ_all

    So per-sample weights are:
      success: c_{T,N}(K) - beta/N
      failure: -beta/N
    """
    device = K.device
    log_fact = _logfact_upto(N, device)
    c = c_sub_TN(K.to(torch.int64), N, T, log_fact)  # (m,) float64

    base = float(beta) / float(N)
    w_fail = torch.full_like(c, -base, dtype=torch.float64)
    w_succ = c - base
    return w_succ, w_fail
