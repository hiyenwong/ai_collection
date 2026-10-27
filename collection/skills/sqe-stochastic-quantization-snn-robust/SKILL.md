---
name: sqe-stochastic-quantization-snn-robust
description: Use when defending SNNs via stochastic input encoding.
category: ai_collection
tags: [neuroscience, spiking-neural-networks, adversarial-robustness, input-encoding, stochastic-quantization, poisson-encoding, defense, csq]
arxiv_id: 2610.01558
paper_title: "Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks"
paper_url: https://arxiv.org/abs/2610.01558
authors: Yujia Liu, Peiyu Liu, Yajing Zheng, Tiejun Huang
published: 2026-10-01
---

# Stochastic Quantization Encoding (SQE): Controllable Randomness Defense for SNNs

**Liu et al. (Peking University), arXiv:2610.01558 [cs.NE] 01 Oct 2026.** Input-level adversarial defense for SNNs: inject *controlled* randomness at the encoding stage, orthogonal to (and composable with) training-based defenses.

## Core Insight

Poisson encoding's robustness advantage over direct encoding comes from **inherent randomness**, not spike statistics. SQE interpolates the full spectrum between the two standard encodings with a single integer knob — the quantization scale N — giving a principled clean-accuracy ↔ robustness trade-off.

## The SQE Encoding Rule

For normalized pixel x_i ∈ [0,1] and quantization scale N ∈ ℤ⁺, at each time step t sample **independently**:

```
s_i⁰[t] ∈ { ⌊x_i·N⌋/N,  ⌈x_i·N⌉/N }        (adjacent quantization levels)

P(s_i⁰[t] = ⌈x_i·N⌉/N) = {x_i·N}          (fractional part)
P(s_i⁰[t] = ⌊x_i·N⌋/N) = 1 − {x_i·N}
```

Special case: if x_i·N ∈ ℤ exactly, encode s_i⁰[t] = x_i deterministically for all t.

Repeat over T time steps → stochastic encoded sequence. This is **stochastic rounding lifted to a temporal encoding**.

## Four Theorems (the theoretical core)

| # | Statement | Consequence |
|---|-----------|-------------|
| **T1 Unbiasedness** | 𝔼[s_i⁰[t]] = x_i; time-average → x_i as T→∞ | Input intensity preserved in expectation — clean accuracy survives |
| **T2 Randomness bound** | 0 ≤ Var[s_i⁰[t]] ≤ **1/(4N²)** | N *monotonically* controls encoding randomness (max variance at half-quantization points) |
| **T3 Poisson limit** | N = 1 ⇒ levels are {0,1} | **Reduces exactly to Poisson encoding** |
| **T4 Direct limit** | N → ∞ ⇒ Var → 0 | **Reduces to direct encoding** |

⇒ SQE is a **general encoding framework**: Poisson and direct encoding are its two extremes. Robustness is a decreasing function of N; clean accuracy increasing in N.

## Training: Straight-Through Estimator

The discrete sampling is non-differentiable. Forward pass performs stochastic quantization; backward pass propagates gradients **through the encoding layer unchanged** (Bengio-style STE). No surrogate gradient needed at the encoder.

## Reference Implementation

```python
import torch

class SQE(torch.autograd.Function):
    """Stochastic quantization encoding, N-controlled randomness."""
    @staticmethod
    def forward(ctx, x, N, T):
        # x: (B, C, H, W) in [0,1]; returns (T, B, C, H, W)
        with torch.no_grad():
            xn = x * N
            lower = torch.floor(xn) / N
            upper = torch.ceil(xn) / N
            p_upper = xn - torch.floor(xn)              # {x·N}
            # Bernoulli choice per timestep; exact-grid points are deterministic
            u = torch.rand(T, *x.shape, device=x.device)
            is_exact = (xn == torch.floor(xn))
            choice = (u < p_upper.unsqueeze(0)) & ~is_exact.unsqueeze(0)
            s = torch.where(choice, upper.unsqueeze(0), lower.unsqueeze(0))
            s = torch.where(is_exact.unsqueeze(0), x.unsqueeze(0), s)
        return s

    @staticmethod
    def backward(ctx, g):
        return g.sum(0), None, None  # STE: identity gradient, averaged over T

def sqe_encode(x, N, T):
    return SQE.apply(x, N, T)
```

## Key Experimental Results (CIFAR-10/100, T=8, ε=8/255, VGG-11 & WRN-16 SNNs)

**Composability with training defenses (VGG-11 CIFAR-10, avg acc over RFGSM/PGD10/PGD30/PGD50/APGD10):**

| Training | direct enc | SQE (N=2) | Gain |
|----------|-----------|-----------|------|
| Vanilla | 0.004% | 9.78% | +9.8 |
| AT | 15.67% | 25.27% | +9.6 |
| RAT | 16.58% | **30.51%** | +13.9 |
| SR (sparse-reg) | 9.98% | 26.03% | +16.1 |
| TGO | 0.09% | 14.75% | +14.7 |

WRN-16 + RAT: 17.60% → **34.07%** average robustness (+17%), at <5% clean cost. APGD10 with RAT: 17.31% → 43.41%.

**vs Poisson encoding (the trade-off frontier):**

| Encoding | Clean | WB APGD10 | BB APGD10 |
|----------|-------|-----------|-----------|
| direct | 90.85 | 0.00 | 18.84 |
| SQE (N=2) | **87.36** | 16.82 | **74.95** |
| Poisson | 81.67 | 29.11 | 76.15 |

⇒ Poisson wins white-box (most randomness), but SQE matches it **black-box** while keeping ~6% more clean accuracy. N=2 (CIFAR-10) / N=3 (CIFAR-100) are the sweet spots.

**Ablation confirms theory:** N=2→8 raises clean accuracy ~5% but collapses robustness to ~0 — exactly the monotone trade-off Theorem 2 predicts.

## When to Use

- Defending SNN image classifiers where adversarial training is already in place (SQE stacks — input-level vs training-level)
- Deployments where black-box robustness matters (SQE ≈ Poisson there, with much better clean accuracy)
- Studying *why* encoding affects SNN robustness: randomness at input layer attenuates transfer of small adversarial perturbations into spike statistics
- Neuromorphic hardware with stochastic encoders (Poisson generators already exist; SQE with N≥2 is a small modification)

## Biological Interpretation

N plays the role of **population size in population coding** (Georgopoulos): large populations average out trial-to-trial noise (stable representation, large N), small populations stay noisy (random representation, small N). SQE's knob is a computable analog of population-size-mediated representational stability.

## Limitations

- White-box robustness still below Poisson (attacker can exploit partial determinism)
- ~1-3% clean accuracy cost on CIFAR-10, ~5% on CIFAR-100 (vanilla training)
- Only image classification validated; temporal/streaming SNN inputs untested
- Randomness at encoding does not protect against adaptive attackers who average multiple stochastic passes (EOT-style)

## Related Skills

- `spike-ptsd-adversarial` — the attack side (Spike-Triggered Decoupled attacks on SNNs); SQE is a direct countermeasure class
- `trainability-iqp-born-machines` — other uses of controlled stochasticity in differentiable pipelines
