# QMaxCal: Girsanov's Theorem for Open Quantum Control

## Source
arXiv:2606.19947 — "QMaxCal: Path-Space Regularization for Open Quantum Control via Girsanov's Theorem" (Moody, Mensch, Cheng, Bolhuis, Welling, June 2026)

## Core Idea

When an open quantum system is continuously monitored, measurement records are stochastic processes. Two systems sharing the same decoherence channels but experiencing different noise have records that differ only in drift terms. **Girsanov's theorem** gives a closed-form, differentiable KL divergence estimator between their trajectories.

### Girsanov KL Estimator
```
dKL/dθ = E[∫₀ᵀ (drift₁(t) - drift₂(t))² dt]
```

### Path-Space Regularization

Instead of parameter-space regularization (common in VQAs):
1. Generate reference trajectory from known-good policy
2. Generate candidate trajectory from policy being optimized  
3. Compute path-space KL using Girsanov estimator
4. Optimize: min_θ [Cost(π_θ) + λ·KL(π_θ || π_ref)]

### Advantages
- **Noise-aware**: Explicitly accounts for decoherence channels (unlike GRAPE/CRAB)
- **Closed-form differentiable**: No Monte Carlo trajectory averaging needed
- **Continuous monitoring compatible**: Works with real-time measurement records

### Key Use Cases
- Decoherence-aware control policy optimization
- Continuous monitoring systems
- Robust control under environmental noise
- Trajectory-space regularization for VQA

## Related Skills
- [[qmaxcal-open-quantum-control]] — Full skill for this methodology
- [[quantum-robust-control]] — Robust control engineering
- [[universally-robust-quantum-control]] — Noise-agnostic control
