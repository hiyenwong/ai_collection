---
name: gradient-tunneling-nmc-feedback-learning
description: Use when training spiking microcircuits/reservoirs online. Causality-gradient feedback learning without surrogate gradients.
trigger: gradient tunneling, NMC feedback learning, temporal credit assignment, spike-timing dependent learning, online SNN training, causality gradient, lead-lag expansion, eligibility trace, neural microcircuit, reservoir feedback training
category: ai_collection
---

# Gradient Tunneling (GT) — Spike-Timing-Dependent Feedback Learning for Neural Microcircuits

**Source**: arXiv:2609.08070v2 (2026-09-10) — Zhang, Liu, Lu, Liu, Dong, Tian, Zhu, Hu, Schuller (Beijing Institute of Technology / TUM).
Code: https://github.com/OskajhZ/NMC-Gradient-Tunneling

Solves the two-decade-old **NMC feedback learning problem**: Maass et al. (2007) proved sparse feedback connections endow a neural microcircuit with universal computational power, but no practical learning rule for those feedback weights existed. GT provides it — gradient-based, yet derived purely from local pre/post-synaptic spike timing (no surrogate gradients, no BPTT computation graph).

## 1. Core Reframing: Temporal Credit Assignment → State Separation

The current neural state is a **combination of state components**, partially determined by attenuated effects of historical perturbations. Credit assignment becomes: **extract and amplify, through trainable feedback connections, those state components that were induced by historical perturbations and are critical for the task**. This reinforces trajectories from historical perturbations toward task-required terminal states, reshaping the dynamics — instead of tracking gradients through a computation graph (BPTT) or differentiating through spike discontinuities (surrogate gradients).

## 2. Theoretical Foundation (3 components)

### 2.1 Intrinsic Stochastic Rate-Coding (stochastic NMC model)
For an LIF population near the edge of chaos, decompose membrane dynamics:
- Recurrent component: `r_l[n] = W_rec · x̃_l[n−1]` — autocorrelation vanishes rapidly with lag (Sompolinsky chaos) → **functionally equivalent to white noise injection**.
- Autonomous component: `a_l[n] = γ·v_l[n−1] − diag(v_th)·x_l[n−1]` — preserves neuronal state.

Within a **stationary window** W (hyperparameter), spike events are Bernoulli realizations and the firing rate estimated by an **Iterative Moving Average (IMA) filter** approximates the mathematical expectation of spiking. Verified via Wiener-Khinchin: post-training recurrent component has uniform power spectrum + zero autocorrelation at nonzero lags — the white-noise approximation survives training-induced drift.

### 2.2 Lead-Lag Expansion
Within the stationary window, conceptually expand the NMC into a **static two-layer feedforward net**: the *lead* layer (current spikes x_l[n]) and the *lag* layer (feedback signals f_l[n] drawn from previous spiking state x_l[n−1]). Only causality between current and lagged spikes needs consideration — structural recurrence is temporarily set aside.

### 2.3 Causality-Gradient Theorem
**Theorem 1**: The Jacobian of postsynaptic firing rate w.r.t. presynaptic firing rate equals a difference of conditional firing probabilities:
```
∂E[X_l^i]/∂E[X_{l−1}^j] = P(X_l^i=1 | X_{l−1}^j=1) − P(X_l^i=1 | X_{l−1}^j=0)
```
Assumption: invariance of conditional firing mechanism — presynaptic neurons converging on a common target must not be strongly recurrently interconnected (enforced by the sparse *uniform* feedback scheme: pick widely-spaced neurons).

**Theorem 2 (implementable form)**: The gradient is the expectation of a local spike-timing process:
```
s_l^{i,j}[n] = (X_l^i[n] − X_l^i[n−m]) · X_{l−1}^j[n] · (1 − X_{l−1}^j[n−m])
E[s_l^{i,j}[n]] = ∂E[X_l^i]/∂E[X_{l−1}^j]  /  (µ_{l−1}^j (1 − µ_{l−1}^j))
```
Conditions: (C1) strict stationarity of spike processes; (C2) conditional-firing invariance; (C3) rapid decorrelation with time lag (emerges at edge of chaos).

## 3. GT Algorithm (3 steps)

**Step 0 — Causality matrix** (mini-batch extension of s, spike-count smoothing window W=3):
```
S_l^m[n] = [Σ_{j=0}^{W−1} x_l^m[n−j] − Σ_{k=0}^{W−1} x_l^m[n−W−k]] · x_{l−1}^m[n−W+1] ∘ (1 − x_{l−1}^m[n−W])
```

**Step 1 — Local tracing** (during forward pass, track with IMA filter F_α):
- presynaptic firing rate `µ_{l−1}[n] = F_α(x_{l−1}[n])`
- causality estimate `Ŝ_l[n] = F_α(S_l[n])`
- **eligibility trace**: `E_l = Ŝ_l ∘⁻¹ (1 − M_{l−1})` where M = synaptic-form (broadcast) of µ — echoes biological eligibility traces (e-prop lineage).
- **Jacobian trace**: `Ĵ_{l−1} = E_l ∘⁻¹ M_{l−1}`

**Step 2 — Global tunneling** (learning signals tunnel through the recurrent population):
- Recursive backprop of learning signal: `L_{l−1} = (L_l)^T · Ĵ_{l−1}` — same shape as a weight-matrix transpose product, but built from spike timing.
- Weight update (SGD/AdamW): `W_{l−1} ← W_{l−1} − η · Σ_m (L̃_l^m ∘ E_l^m) ∘⁻¹ W_{l−1}` where L̃ is the synaptic form of L. Only initially non-zero (sparse) weights update — connectivity structure frozen to initialization.

**Step 3 — Firing-rate regularization**: `R_l = (1/2d_l) Σ_i (µ_l^i − µ̄_l)²` toward target rate µ̄. Essential: ultra-low firing rates give tiny denominators `µ(1−µ)` and blow up gradient estimation error.

**Sparse uniform feedback scheme**: feedback channels `f_l,k[n] = x̃_{l, k·⌊d_l/(d_f−1)⌋+s}[n−1]` — take d_f spikes from equidistant (widely separated) neurons of the previous step. Distance-based W_rec (3D Euclidean embedding) weakens correlations with distance, satisfying Theorem-1 invariance. Feedback ratio ~10% typical; higher ratios lower loss but destabilize training by violating the invariance condition.

## 4. Verified Results

| Experiment | Result |
|---|---|
| Jacobian estimation (stationary) | GT-estimated Jacobian trace ≈ numerically-differentiated (r≈1), beats zero-recurrence LIF baseline |
| Non-stationary EEG (SEED, frozen readout) | Loss/accuracy improve consistently → gradient estimation accurate under strong non-stationarity |
| T-maze evidence integration | Terminal-only supervision works; Lyapunov-tuned LSM fails; trained NMC behaves as finite-state machine with high-certainty readout on low-dimensional manifold |
| Incremental add (noise robustness) | Transcends memory limit to L=75 (SNR ≈ −44.76 dB) where LSM diverges permanently |
| SHD speech (1000 LIF neurons) | 73.61% — beats e-prop 67.54% (p=0.0041) and FPTT 67.24% (p=0.0089), no surrogate gradients; below pp-prop |
| SEED / DEAP EER (LibEER standard) | Best all 4 SEED metrics (acc 60.22%), best DEAP-V acc 73.93%, best DEAP-A P/R/F1 |
| Efficiency | Trainable recurrent connections = 0.43% of full SRNN; ~2.0× faster than LTC-SNN+FPTT, 6.9× faster than SRNN+D-RTRL |

**Warm-up / curriculum effect**: incrementally increasing sequence length L (15→75) converges to far lower error than direct training at L=75 — state separation is bounded by fading memory, so first establish feedback connectivity within the intrinsic timescale, then extend. Generalizable curriculum rule for any fading-memory learner.

**Nested sub-network emergence**: the sparse feedback neurons form an interconnected functional core (trainable weights); sub-network readout ≈ full-model accuracy, peripheral readout degrades sharply. Matches biology of distributed mixed selectivity / neural manifolds (sparse manifold-bound neurons inside a broader circuit).

## 5. Why It Matters (interpretation)

- **Bridges gradient learning vs. spike-timing**: operates on *distributional parameters of spiking activity* (firing-rate expectations), not on spike events — reconciling gradient-based optimization with STDP-style local plasticity and the NGRAD hypothesis (gradient ≈ activity differences, here estimated without explicit perturbation).
- **Biological hypothesis**: cortex could implement supervised dynamic reshaping using only locally available pre/post-synaptic spike events.
- **Neuromorphic fit**: stochastic computing + sparse feedback align with robustness/efficiency requirements of neuromorphic hardware.
- Each update step simultaneously shapes the global attractor AND optimizes terminal output; only weight changes benefiting both accumulate — implicit selection pressure lets robust feedback emerge without direct output feedback.

## 6. Limitations & Extensions

- Fading memory bounds state separation horizon for long/complex sequences (mitigate via warm-up curriculum).
- No spatial feature-extraction frontend → unsuited as-is for high-dimensional visual streams (DVS); pair with a convolutional encoder.
- Stationary-window breakdown boundary not theoretically characterized — keep window ≪ input length for bursty inputs.
- **Future — Spiking Neural Circuits (SNCs)**: stack multiple NMCs hierarchically; GT learning signals backpropagate across NMCs, enabling supervised hierarchical systems. The feedback NMC is the minimal SNC realization.

## 7. Implementation Checklist (PyTorch)

1. LIF population, Dale-compliant, embedded in 3D Euclidean cube (edge 8–10) → distance-based W_rec (frozen), threshold v_th=10 shared.
2. Feedback channels per Eq. 9 (uniform stride over previous spikes, ratio ~10%), trainable W_{l,f} folded into generalized input weight W_{l−1}.
3. Track causality matrix S (W=3 smoothing) and presynaptic rates with IMA filter α set by stationary window length.
4. On downstream signal arrival: build eligibility trace E and Jacobian trace Ĵ; tunnel L recursively; update W with AdamW + rate regularization (β).
5. Stationary window: half the decision/relevant block for evidence tasks; ≈ clip length for time-invariant features on non-stationary streams; as narrow as possible when target position is unknown.
6. Curriculum: ramp sequence length; halve learning rate per phase.

## Related Skills
- `surrogate-gradient-snn-training` — mainstream differentiable-graph alternative
- `event-driven-eligibility-propagation`, `three-factor-snn-learning` — e-prop family contrast
- `cortical-microcircuit-information-flux` — NMC reservoir analysis
- `working-memory-heterogeneous-delays` — fading-memory extension tricks
