---
name: engram-resource-competition-allocation
description: Theory of engram cell allocation via resource competition.
category: ai_collection
trigger: engram cell allocation, hippocampal memory allocation, place field expansion, mutual information neural resource allocation, memory forgetting theory, context probability engram, sparse memory code optimization
---

# Engram Resource-Competition Allocation Theory

Information-theoretic framework from Chiba & Teramae (arXiv:2609.32620, Sep 2026) explaining how hippocampal CA1 allocates limited neurons between spatial and contextual information, predicting non-monotonic engram allocation as a function of context occurrence probability, with a discontinuous phase transition derived analytically via KKT conditions.

## Core Idea

Engram cells in CA1 are recruited from place cells. When a place cell becomes an engram cell for a context, its place field **expands** (experimentally observed, relative increase α), degrading spatial resolution. Memory allocation is therefore a **resource-allocation optimization**: limited neurons must be split between encoding *where* (spatial information) and *what context* (contextual/episodic information). Solving this optimization yields the fraction f_s of place cells recruited per context s.

## The Model

**Setup**
- M+1 contexts C_s (s=0 home cage, p_0 excluded from engram), occurrence probabilities p_s; positions x uniform over area S; s ⊥ x.
- N place cells; disjoint engram sets Λ_s with fractions f_s = |Λ_s|/N; Σf_s ≤ 1.
- Place fields: isotropic 2D Gaussians with width σ_i(s)² = σ² if i ∉ Λ_s, else σ²(1+α) — engram recruitment expands the field in the associated context by factor (1+α).

**Information measures (per observed spike)**
- Spatial: I_space = I(x; X | s) — conditional MI between position and firing-neuron index X.
- Contextual: I_context = I(s; X | x) ≥ I(s; X) (lower bound used; valid because s ⊥ x makes both vanish in the reference network with f_s = 0).
- Total (weighted, since x continuous / s discrete are incommensurable): I_total = W·I_space + I_context, W = relative importance of spatial information.

**Optimization problem**

maximize over {f_s}:
ΔI_total^LB(α, {f_s}, {p_s}, W) = W·ΔI_space + ΔI(s; X)

subject to: 0 ≤ f_s ≤ 1 (s = 1..M), Σ_s f_s ≤ 1 (disjointness).

Crucially, f_s* depends on the **entire distribution** {p_s}, not only p_s — this is what creates inter-context competition.

## Key Results

1. **Non-monotonic allocation**: optimal engram fraction f_s(p_s) rises discontinuously from 0 at a critical p_s, peaks at intermediate probability, then *decreases* for highly frequent contexts.
   - Low p_s → no allocation (memories of rarely-visited environments waste resources; below critical probability, allocation is exactly zero — discontinuous transition).
   - High p_s → allocation shrinks because expanded place fields destroy too much spatial information for a frequently-experienced context.
2. **Competition is essential**: removing the Σf_s ≤ 1 constraint (Appendix B control) makes f_s(p_s) monotonically decreasing — the non-monotonicity and discontinuous transition arise purely from inter-context competition for limited resources.
3. **Analytic phase boundary** (no-engram phase vs. engram phase), derived via KKT conditions on the f_s*=0 solution:
   **W ≥ 1 − α / [(1+α)·log(1+α)]** ⟹ no engram cells allocated for ANY {p_s} (sufficient condition).
   - Stronger contextual input (larger α) pushes the critical W higher: engram formation survives even when spatial accuracy matters more.
   - At f_s=0 the gradient is ∂ΔI/∂f_s = [(1−W)(1+α)log(1+α)]·p_s − (1+α·p_s)·log(1+α·p_s) ≤ 0 for all p_s.
4. **Numerics**: phase diagram in (α, W) plane with color log10(f_max); analytic boundary Eq.(12) matches numerical transition accurately.

## Biological Interpretation

- **Memory consolidation**: frequent contexts consolidate to neocortex, reducing hippocampal dependence — explains decreasing f_s at high p_s.
- **Memory forgetting**: as effective p_s decays over time since last exposure, the theory predicts engram allocation gradually shrinks then vanishes below the critical probability — an information-theoretic account of forgetting (dynamic-setting extension is future work).
- Sparse engram recruitment is optimal, not accidental: resource limits make sparse codes information-theoretically optimal.

## Reusable Methodological Patterns

### Pattern 1: Resource-constrained representation allocation via MI
When a coding resource (neurons, bits, memory slots) serves multiple competing variables, formulate max Σ-scaled-ΔMI subject to a budget constraint Σf_s ≤ 1. The optimum depends on the full prior distribution {p_s}, inducing competition. Applicable to: memory systems, sensor allocation, cache partitioning, mixture-of-experts capacity allocation.

### Pattern 2: Phase-boundary derivation via KKT at the zero-allocation solution
To determine when *no* allocation to any consumer is optimal: set all f_s*=0 (forces multiplier μ=0), evaluate ∂objective/∂f_s at 0, require ≤ 0 for all priors p_s, then bound the worst case (typically p_s → 0 using (1+αp)log(1+αp)/p ≤ ... style inequalities). This yields a closed-form sufficient condition in the parameter plane.

### Pattern 3: Expansion-cost trade-off
A unit committed to context s pays a precision cost (field expansion by (1+α)) on the *other* axis of information. Model both information gains and losses in the same objective (ΔI vs. reference network with no allocation), never just the gain.

### Pattern 4: Discontinuous transitions from competition
Discontinuous (first-order-like) transitions in allocation fractions emerge from global budget coupling — not present when consumers are independent. Diagnostic: remove the coupling constraint; if the transition disappears, competition is the mechanism.

## Implementation Sketch

```python
# Core optimization (scipy)
# Variables: f = [f_1..f_M], parameters alpha, W, priors p
# ΔI_space(f_s) computed from Gaussian field model (analytic expression in paper SM)
# ΔI(s;X) via Bayes: P(i|s) = ∫ dx P(x) P(i|x,s), P(i) = Σ_s p_s P(i|s)
# objective(f) = W * ΔIspace(f) + ΔIcontext(f)   [lower bound]
# constraints: 0 ≤ f_s, Σ f_s ≤ 1
from scipy.optimize import minimize
res = minimize(lambda f: -objective(f), x0, method='SLSQP',
               bounds=[(0,1)]*M,
               constraints=[{'type':'ineq','fun': lambda f: 1-f.sum()}])
# Phase check: no-engram iff W >= 1 - alpha/((1+alpha)*log(1+alpha))
import numpy as np
no_engram_phase = W >= 1 - alpha/((1+alpha)*np.log1p(alpha))
```

Sweep p_s ∈ (0, 0.5] across random prior realizations to reproduce the non-monotonic f_s(p_s) cloud (Fig. 2, α=0.5, W=0.1, M=10).

## Experimental Predictions (testable)

1. Engram fraction vs. context occurrence probability is **non-monotonic** (peak at intermediate p_s) — not yet tested experimentally.
2. Below a critical p_s, engram allocation is exactly **zero** (discontinuous).
3. Increasing spatial-task demands (reward requires accurate localization → raise W) shrinks and eventually eliminates engram recruitment.
4. Weakening contextual input (lower α) eliminates engram allocation at lower W.

## Limitations

- Disjoint engram sets assumed (real neurons can belong to multiple contexts).
- Homogeneous σ; place/engram may form a continuum, not two populations.
- Lower bound on ΔI: tightness unknown.
- Stationary priors; dynamic/learning-setting extension open.
- MI-optimal representation may not equal behaviorally optimal retrieval (open link to memory-guided behavior).

## Sources

- arXiv:2609.32620 — Chiba K, Teramae J-n. "Space versus Context: Competition for limited neural resources determines engram cell allocation in the hippocampus" (q-bio.NC, 26 Sep 2026)
- Related local skills: `multisensory-learning-engram-recruitment`, `user-as-engram-hippocampal-memory-architecture`, `efficient-coding-criticality`
