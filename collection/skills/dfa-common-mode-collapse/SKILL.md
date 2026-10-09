---
name: dfa-common-mode-collapse
description: Mean-error-driven representation collapse in DFA training.
category: ai_collection
trigger_words: direct feedback alignment, DFA, feedback alignment, common mode, representation collapse, gate participation, mean-covariance decomposition, biologically plausible learning, credit assignment, tanh saturation, plateau stall, random feedback
---

# Common-Mode Collapse and Recovery in Direct Feedback Alignment

Methodology from "Common-Mode Collapse and Recovery in Direct Feedback Alignment" (arXiv:2609.31589, cs.LG/cs.NE, 25 Sep 2026; Varun Reddy, Bernardo L. Sabatini, Houman Safaai — Kempner Institute & Harvard Medical School Neurobiology).

## When to Use
- Diagnosing early-training plateaus/stalls in direct feedback alignment (DFA), layerwise feedback alignment (FA), or random-feedback training where loss sticks near the constant class-prior predictor
- Designing biologically plausible learning rules that broadcast a global teaching signal (relevant to neuromodulatory/reward-modulated plasticity: shared signals vs input-dependent plasticity)
- Analyzing representation collapse: hidden activities becoming nearly parallel across inputs, units saturating, gates vanishing
- Choosing interventions: error centering, prior-bias initialization, input centering, feedback gain tuning

## Core Mechanism
DFA trains hidden layers with a FIXED random projection of the output error:
```
δℓ(x) = ϕ'(aℓ(x)) ⊙ Bℓ e(x)     # Bℓ fixed random, e = ŷ − y (logit error)
ΔWℓ = −η ⟨δℓ h⊤ℓ−1⟩ ,  Δbℓ = −η ⟨δℓ⟩
```
**The common mode**: with one-hot targets and initial predictions ≈ 1/2, the error has a large MEAN component ē shared across all inputs (∥ē∥ ≈ C(1/2−1/C) for balanced sigmoid). Random feedback sends it to every hidden unit with a random coefficient; combined with mean presynaptic activity h̄, this forms a RANK-ONE update.

## Exact Mean–Covariance Decomposition (Proposition 1)
```
ΔWℓ = −η Cov(δℓ, hℓ−1) − η δ̄ℓ h̄⊤ℓ−1      # classical Sejnowski 1977 split
δ̄ℓ = γ̄ℓ ⊙ Bℓ ē + rℓ ,   rℓ = (γℓ−γ̄ℓ) ⊙ Bℓ ẽ
```
- Rank-one term δ̄ℓ h̄⊤ drives preactivation means: `dμℓᵢ/dt = −η sech²(μℓᵢ)(Bℓē)ᵢ(Hℓ−1+1)` for tanh
- Drift direction: units move toward ±saturation ⇒ gate energy ϕ'² concentrates on few units ⇒ collapse
- Why random feedback is vulnerable: BP has B_L ∝ W_out⊤ giving a positive-semidefinite RESTORING term for the mean logits; random Bℓ averages to zero systematic correction. Only the readout's learning of the class prior ends the drive.

## Diagnostics (measure these)
1. **Shared vs input-dependent error**: ∥ē∥ (mean over probe) vs RMS ∥ẽ∥ — collapse tracks ∥ē∥ decay (1.278→0.10 in 100 updates while ∥ẽ∥ stays ~0.9)
2. **Gate participation ratio**: pℓ = Σᵢuᵢ² / (dℓ Σᵢuᵢ²) with u = mean squared activation sensitivity ϕ'²; collapses toward 1/dℓ (one unit dominates all gating). More informative than cosine under uncentered inputs.
3. **Mean pairwise hidden cosine** across inputs (representation parallelism; 0.99+ during plateau)
4. **Gradient cosine + projected descent**: cos αℓ between DFA estimate and true BP gradient; anti-aligned during stall
5. **Delivered dose**: κℓ(t) = g Σₛ<t ⟨ēₛ, ê₀⟩(Hₛ+1) along the initial mean-error direction

## Collapse Number (initialization estimate)
```
κ̂ℓ = g∥ē₀∥(H₃−1(0)+1) / (σ'eff (H_L(0)+1)(ηout/η))
σ'eff = (1/2 − 1/C)/ln(C−1)          # effective sigmoid slope, balanced classes
pℓ ~ (15/8)·√(2/π)/κℓ  at large dose   # predicted participation minimum
```
- Invariant to jointly scaling both learning rates; gain and initial mean error enter only through product g∥ē₀∥
- Reduced model (Gaussian quadrature over evolving preactivation distributions, σℓ² propagated from layer 1, NO fitted parameters) predicts participation minima across 48 settings: r = 0.91

## Key Empirical Results (MNIST 3×300 tanh MLP, sigmoid/BCE — Nøkland's protocol)
| Finding | Numbers |
|---|---|
| Plateau | loss at class-prior level for hundreds of steps; accuracy ≈ chance |
| Collapse | min variance across inputs → 0.028 of initial (BP: 0.83); gate participation falls every layer, deepest worst |
| Decodability SURVIVES | ridge readout at collapse checkpoint: 88.6% (init: 89.3%) — but continued readout learns to only 20.0% vs 63.4% from init features |
| Amplitude bottleneck | collapsed features 5.9× smaller RMS ⇒ effective readout rate ~35× lower; rescaling features restores 80.1% |
| Plateau scaling | T_plateau ∝ a^(−0.40) ηout^(−0.60) with a = ηhid·g (exponents sum ≈ −1) |
| Adam | learns faster despite DEEPER collapse (117 vs 537 updates to learn; min participation 0.046) — coordinatewise normalization bypasses amplitude bottleneck |
| Generalizes | layerwise FA (cos 0.991), 6-layer MLP (L4-6 cos 1.000), CNN (participation 0.021), CIFAR-10 (participation 0.009 vs 0.756 BP) |

## Interventions (ranked by mechanism fit)
1. **Center the broadcast error** (subtract ⟨e⟩ before projecting through Bℓ): removes the rank-one mean drive entirely. Prevents sustained collapse even for sign-error feedback (cos 0.96→0.03, acc 0.75→0.90). ⚠ With ReLU/GELU/linear units can push loss ABOVE constant-predictor baseline — combine with input centering.
2. **Prior-bias initialization**: b_out = logit(π_c) = ln[π_c/(1−π_c)] (class-prior calibration, cf. focal-loss prior init). Suppresses drive, speeds learning (690→370 steps to 50% acc), zero training cost. Insufficient alone on CIFAR-10 CNN.
3. **Input centering + frozen hidden biases**: per-pixel centering protects layer 1; together they prevent collapse throughout (only one alone is partial).
4. **Feature rescaling on collapsed checkpoints**: divide centered features by RMS + transform readout to preserve predictions → recovers 80.1% (post-hoc fix for amplitude bottleneck).
5. **Muon-style orthogonalization** of hidden updates reduces collapse; **error-side second-moment conditioning** (Safaai 2026) can retain high cosine but hurt accuracy.
6. **Weaker feedback gain** (g=0.03): prevents collapse but SLOWS learning (1897 vs 537 updates) — less collapse ≠ faster learning; saturation boosts H, accelerating the readout's prior fit.

## Persistent common mode (does not decay)
Sign-error feedback (DRTP-like) broadcasts sign(e) = 1−2y with population mean 1−2π that NEVER shrinks as the readout learns. Collapse persists through 3000 updates (prior-bias init does NOT help). Subtracting the batch mean is the only effective fix here. General rule: any broadcast signal with a nonzero, non-decaying mean will collapse saturating hidden units.

## Scope & Limits
- Evidence from small nets, plain SGD, fixed rates; adaptive optimizers shorten the transient
- Reduced model captures collapse onset but NOT participation rebound (recovery involves changing participating-unit identities, covariance regrowth, alignment rise at fixed participation)
- Imbalanced softmax restores collapse even with standardized inputs (0.938 cosine at 0.7 class-0 sampling); large input means (CIFAR-10) drive layer-1 collapse under any readout
- Open neuroscience question: do biological circuits regulate the balance between shared (neuromodulatory) teaching signals and input-dependent plasticity? Centered modulatory signals already recognized in reward-dependent plasticity (Frémaux 2010, Gerstner 2018)

## Implementation Checklist
```python
# 1. Decompose your broadcast learning signal: e = mean + fluctuation
# 2. Track ||mean signal|| decay, gate participation p_l, hidden cosine
# 3. If plateau near prior-loss: check rank-one term δ̄h̄ᵀ dominance
# 4. Intervene: center e (after checking nonlinearity), or init readout at logit(prior)
# 5. For non-decaying signals (sign errors): batch-mean subtraction is mandatory
# 6. Verify recovery: participation rebound + gradient cosine rise, not just loss
```

## Related Skills
- `local-gradient-approximations-rnn` — dynamics of local approximate gradient rules
- `three-factor-snn-learning` — neuromodulatory three-factor rules (where common-mode signals arise)
- `backprop-brain-hierarchy-misalignment` — biological plausibility of credit assignment
- Code: github.com/KempnerInstitute/DFA-Stall (upon release)
