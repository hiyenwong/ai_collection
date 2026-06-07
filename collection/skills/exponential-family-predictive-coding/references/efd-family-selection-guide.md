# EFD Family Selection Guide for Predictive Coding

| EFD Family | Best For | Natural Parameter | Sufficient Statistics | FEP-PC Notes |
|-----------|----------|-------------------|----------------------|--------------|
| Poisson | Spike counts, discrete neural events | log(λ) | count | Good for spike-train prediction errors |
| Gamma | Positive continuous (firing rates, concentration) | -1/β, α/β | x, log(x) | Enforces non-negativity; skewed responses |
| Beta | Proportions/bounded variables (0,1) | logit(α/β), logit(β/α) | log(x), log(1-x) | Useful for normalized neural activity |
| Gaussian | Continuous (baseline case) | μ/σ², -1/(2σ²) | x, x² | Special case of EFD; recovers standard PC |
| Von Mises | Circular (orientation tuning, phase) | κ·cos(μ), κ·sin(μ) | cos(x), sin(x) | For directional/phase-coded neurons |

## Selection Heuristics

1. **Firing rates ≥ 0** → Gamma (not Gaussian)
2. **Spike counts** → Poisson
3. **Bounded activity (attention, gating)** → Beta
4. **Orientation/phase coding** → Von Mises
5. **Mixed populations** → Different layers use different EFDs (heterogeneous network)

## Implementation Notes

- FEP-PC correspondence maintained up to **second cumulant** for all EFD families
- Higher cumulants require additional terms beyond standard PC update rules
- Gamma and Poisson most common in biological neural modeling
- Von Mises specialized but critical for sensory cortex orientation columns

## Local Plasticity Rules (2026-06-01)

From EFD variational free energy gradient:
```
Δw_ij ∝ E_q[∂log q/∂w_ij · (log p(x|z) + log p(z) - log q(z))]
```

Key: purely local signals (pre-synaptic activity × prediction error). No backprop needed.

## Paper Reference

arXiv:2605.30882 — Kataoka & Doya (2026)
