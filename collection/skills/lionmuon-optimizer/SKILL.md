---
name: lionmuon-optimizer
category: deep-learning
description: LionMuon optimizer methodology - alternating between spectral (Muon) and sign-based (Lion) updates on a fixed period for compute-efficient large-scale training
trigger: LionMuon, sign-based optimizer, Muon optimizer, spectral descent, sign descent, alternating optimizer, optimizer period, dual-EMA momentum
---

# LionMuon: Alternating Spectral and Sign Descent for Efficient Training

Methodology for combining strong spectral optimization (Muon) with cheap sign-based updates (Lion) via alternating periods, achieving Pareto-dominant training efficiency.

## Core Problem

Sign-based optimizers (Lion, Signum) produce cheap per-step updates but weaker directions. Muon's spectral matrix-sign update gives much stronger direction at substantially higher per-step cost. Neither alone achieves the compute-loss Pareto frontier.

## Key Methodology

### 1. Alternating Update Scheme
- Alternate between Lion and Muon updates on a fixed period P
- Lion step (cheap, fast): standard sign-based update with momentum
- Muon step (expensive, strong): spectral matrix-sign via Newton-Schulz iteration
- At P=2, LionMuon Pareto-dominates Muon, Lion, Signum, and AdamW at 124M/355M/720M scale

### 2. Shared Dual-EMA Momentum Buffer
- Both Lion and Muon share a single dual-EMA momentum buffer
- Optimizer state memory matches Lion, exactly half of AdamW
- No additional memory overhead despite alternating between two optimizer types

### 3. SignMuon Variant
- Simpler single-EMA variant of LionMuon
- Already outperforms pure Muon standalone
- Useful as a lighter-weight alternative when dual-EMA is unnecessary

### 4. Complexity Theory
- Proves sharp complexity bounds under heavy-tailed noise
- Bounds governed by period-averaged smoothness and noise
- Interpolates between Muon's and Lion's constants
- Predicts compute-optimal period P for given architecture/dataset
- Theoretical conditions for when LionMuon outruns both Muon and Lion

## Implementation Pattern

```python
class LionMuon:
    """Alternating Lion-Muon optimizer with shared momentum."""
    def __init__(self, params, period=2, lr=1e-3, beta1=0.9, beta2=0.99):
        # Shared dual-EMA momentum buffer
        self.momentum = {p: (torch.zeros_like(p), torch.zeros_like(p)) for p in params}
        self.period = period
        self.step_count = 0
    
    def step(self):
        self.step_count += 1
        if self.step_count % self.period == 0:
            # Muon step: spectral matrix-sign (expensive but strong)
            self.muon_update()
        else:
            # Lion step: sign-based (cheap, fast)
            self.lion_update()
```

## When to Use

- Large-scale model training where both compute efficiency and optimization quality matter
- When AdamW memory overhead is a bottleneck (LionMuon uses half the memory)
- Training at 100M-1B+ parameter scale where optimizer cost becomes significant
- When you want Muon-quality updates without paying full per-step cost

## Key Parameters

- **Period P**: Controls Lion:Muon ratio. P=2 means alternating every step. Larger P = more Lion steps.
- **Dual-EMA betas**: (beta1, beta2) for momentum smoothing, same as AdamW
- **Learning rate**: Similar range to AdamW/Lion

## Performance

- Reaches lower validation loss at lower compute than Muon, Lion, Signum, AdamW
- Advantage persists across model scales (124M → 720M)
- 50% optimizer memory vs AdamW

## Code

https://github.com/brain-lab-research/lion-muon

## Reference

arXiv: 2605.19811v1 - "LionMuon: Alternating Spectral and Sign Descent for Efficient Training"
