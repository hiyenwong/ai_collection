---
name: latent-kinetic-ising-spike-trains
description: >
  SpiKIsing latent-variable kinetic Ising framework for inferring directed
  effective connectivity from continuous-time spike trains. Use when analyzing
  neural spike train data, reconstructing functional/effective connectivity,
  applying kinetic Ising models to neural data, or separating network dynamics
  from single-neuron refractory effects.
metadata:
  arxiv_id: "2609.17213"
  published: "2026-09-15"
  authors: "Davide Ghio, David Saad"
  tags: [spike-train-analysis, kinetic-ising-model, effective-connectivity, variational-inference, point-process, dale-principle, computational-neuroscience]
---

# Latent Kinetic Ising Models of Neural Spike Trains (SpiKIsing)

## Overview

**Core innovation**: SpiKIsing separates two levels of description that conventional kinetic-Ising inference from spike trains conflates:
1. **Latent network dynamics**: A discrete-time asymmetric kinetic Ising model (binary states s_i(t) ∈ {0,1}) describes *collective* network activity and the directed couplings J_ij of interest.
2. **Emission process**: Continuous-time, history-dependent point processes generate the *observed* spikes conditional on the latent states, explicitly modeling refractoriness and post-spike recovery.

This resolves the central pathology of binned kinetic-Ising inference: with binning, single-neuron history effects (refractoriness, recovery) get spuriously attributed to network interactions, and within-bin spike timing is discarded. In SpiKIsing, J_ij describes directed collective dynamics; the emission model absorbs single-neuron temporal effects.

**Key result**: In a variational mean-field EM scheme, the entire point-process likelihood enters the latent-state update as a single **effective observation field** — the log-likelihood ratio between active and inactive latent states. This preserves the algebraic structure of kinetic-Ising inference while letting precise continuous spike times inform it.

**Validation**: On spike trains from a conductance-based LIF network (substantial model mismatch — voltage-dependent conductances, synaptic delays, continuous membrane dynamics, none of which are in the model class), SpiKIsing recovered recurrent connection support at ROC area 0.88 and correctly classified ALL 40 neurons' excitatory/inhibitory identity (30 E + 10 I) via outgoing interaction sums S_j.

## Generative Model

### Latent dynamics (discrete time, asymmetric kinetic Ising)
```
P(s(t) | s(t-1)) = Π_i exp[s_i(t)·H_i(t)] / (1 + exp H_i(t))
H_i(t) = h_i + Σ_j J_ij · s_j(t-1)          # first-order Markov, conditionally independent
```
- J_ii = 0 (self-history delegated to emission), J asymmetric (non-equilibrium class)
- θ_lat = {J, h}: N²  parameters, time-independent
- s_i(τ) ≡ s_i(⌊τ⌋): latent state constant within interval [t, t+1); continuous time measured in latent time-step units

### Emission layer (continuous-time point process)
Conditional on latent trajectory, spikes independent across neurons — all observed correlations arise through interacting latent dynamics:
```
λ_i(τ) = 0                                  if Δ_i(τ) ≤ 0        (absolute refractory)
       = λ_i^-                              if Δ_i(τ) > 0, s_i(τ)=0   (inactive: low rate)
       = λ_i^+ · ρ_i(Δ_i(τ))               if Δ_i(τ) > 0, s_i(τ)=1   (active: high rate × recovery)
Δ_i(τ) = τ - τ*_i(τ) - τ_i^abs              # elapsed beyond refractory
ρ_i(δ) = δ / (δ + c_i)                      # phenomenological recovery kernel (monotone, tractable)
```
- θ_obs = {λ^+, λ^-, c, τ^abs}: λ^- ≪ λ^+ typically; c_i controls recovery timescale (ρ(c_i)=1/2); c_i=0 → instantaneous recovery
- Spike history carried continuously ACROSS latent-interval boundaries (Δ_i defined from most recent spike in whole recording)

### Interval likelihood decomposition
Per interval [t, t+1), with exposure quantities computable ANALYTICALLY from observed spike times:
- E_i^t = ∫ 1[Δ_i(u)>0] du                  (non-refractory exposure)
- A_i^t = ∫ ρ_i(Δ_i(u))·1[Δ_i(u)>0] du     (recovery-weighted exposure)
- C_i^t = Σ_{spikes in [t,t+1)} log ρ_i(Δ_i(τ_k))  (recovery contribution)

```
ln P(τ_i^t | s_i(t)) = n_i^t·ln λ_i^- − λ_i^-·E_i^t              if s_i(t)=0
                     = n_i^t·ln λ_i^+ + C_i^t − λ_i^+·A_i^t      if s_i(t)=1
```

## Variational Inference (nMF-EM)

### Free energy
Marginal likelihood requires summing over 2^NT latent trajectories → intractable. Use fully factorized posterior Q with magnetizations m_i(t) = Q(s_i(t)=1):
```
F_nMF = L_obs + L_lat^nMF + S_Q
L_obs = Σ_{i,t} [(1-m_i)·(n_i^t ln λ^- − λ^- E^t) + m_i·(n_i^t ln λ^+ + C^t − λ^+ A^t)]
L_lat^nMF = Σ_{i,t} [m_i(t)·η_i(t) − ln(1+exp η_i(t))],  η_i(t) = h_i + Σ_j J_ij m_j(t-1)
```
⚠️ Eq. (20) is a rigorous variational bound, but the nMF replacement E[log(1+exp H)] ≈ log(1+exp η) is NOT — F_nMF is not guaranteed to stay a lower bound. Higher-order (TAP-like) corrections are the natural extension.

### Effective observation field (central result)
```
h_i^obs(t) = ∂L_obs/∂m_i(t) = ln [P(τ_i^t|s_i=1) / P(τ_i^t|s_i=0)]
           = n_i^t·ln(λ_i^+/λ_i^-) + C_i^t − λ_i^+·A_i^t + λ_i^-·E_i^t
```
Positive values favour the active latent state. ALL information the point-process emission supplies to the latent Ising variable is this single field per (i,t).

### E-step
Full stationary update (forward–backward sweeps to convergence):
```
m_i(t) = σ[η_i(t) + h_i^obs(t) + R_i(t)]
R_i(t) = Σ_k J_ki·[m_k(t+1) − σ(η_k(t+1))]     # backward reaction term
```
Cheaper causal forward-only filter (drops R_i, single pass, NOT a stationary point of F_nMF):
```
m_i(t) = σ[η_i(t) + h_i^obs(t)]     (m_i(0) = σ(h_i^obs(0)))
```
Appendix C quantifies the accuracy cost; default in experiments is forward-only.

### M-step
- Coupling gradient: ∂F/∂J_ij = Σ_t m_j(t−1)·[m_i(t) − σ(η_i(t))]
- Local fields: per-neuron 1D root-finding of stationarity Σ_t σ(h_i + Σ_j J_ij m_j(t−1)) = Σ_t m_i(t)
- Firing rates closed-form: λ_i^+ = Σ_t m_i(t)·n_i^t / Σ_t m_i(t)·A_i^t;  λ_i^- analogous with (1−m_i) and E^t
- Recovery c_i: gradient ascent (analytic derivatives of A, C)
- τ^abs: fixed if known, or 1D profile maximization of observation likelihood
- ⚠️ Use the **centred parametrization** (Appendix D) for M-step stability — the raw 0/1 parametrization has non-zero presynaptic temporal means → poor conditioning

## MAP Inference with Structured Priors

### Sparse connectivity (Laplace / L1)
P(J) ∝ exp[−γ₁ Σ|J_ij|] → proximal (soft-thresholding) update after gradient step J̃ = J + αG:
```
J_ij^new = sign(J̃_ij)·max(0, |J̃_ij| − α·γ₁)
```
Sets weak couplings exactly to zero without post-hoc thresholding. Elastic-Net (extra L2) in Appendix E.

### Dale-consistent connectivity (hierarchical)
Latent identity z_j ∈ {−1,+1} per presynaptic neuron (excitatory/inhibitory), variational probability φ_j = Q_j(z_j=+1):
```
φ_j = σ[ ln(P(z_j=+1)/P(z_j=−1)) + β·Σ_i J_ij ]      # evidence accumulated across ALL outgoing couplings
```
- γ₁ (sparsity) cancels from the φ update — only sign-asymmetry β matters
- Effective asymmetric penalties: γ̃_j^+ = γ₁ + β(1−φ_j), γ̃_j^- = γ₁ + βφ_j → proximal update with sign-dependent thresholds
- β=0 recovers the symmetric Laplace prior
- Strict Dale is NOT imposed: J is an *effective* interaction (coarse-graining, unobserved inputs, mismatch can flip signs); the prior allows finite-probability violations
- With uniform identity prior: φ_j = σ(βS_j), S_j = Σ_i J_ij → thresholding φ_j at 1/2 ≡ classifying by sign(S_j)

## Validation Results

### Matched-model (N=100, g=1, T=50k)
- MSE(J) decreases systematically with recording length for all coupling strengths g ∈ tested range; joint learning of J, h, λ^+, λ^-, c converges (different timescales, transient non-monotonicity possible); ΔF_nMF saturation is a convergence diagnostic
- Sparse prior: ROC AUC for non-zero-interaction classification 0.79 (T=10⁴) → 0.99 (T=8×10⁴)
- Dale prior on 80%E/20%I network with UNINFORMATIVE prior: type assignments converge to ground truth; sign accuracy → perfect at longest recordings

### Conductance-based LIF mismatch test (the decisive experiment)
- 30 E + 10 I neurons, sparse recurrent connectivity, external Poisson drive, 98 s recording, Δt = 10 ms latent interval, forward-only scheme
- Reference matrix W_ij = z_j·p_ij·g_ij (signed conductance) — compare STRUCTURE not values (J is effective interaction between latent states, not a conductance)
- Connection support: ROC 0.88 overall (0.879 E-sources / 0.883 I-sources)
- Type classification: ALL 40/40 correct via sign of S_j (every E neuron S_j>0, every I neuron S_j<0), despite individual couplings not sign-consistent

## Implementation Checklist

1. Choose latent interval Δt (paper: 10 ms for LIF data) — sensitivity to this choice is an OPEN question
2. Precompute per-interval quantities E_i^t, A_i^t, C_i^t from spike times (closed-form for ρ(δ)=δ/(δ+c), Appendix A)
3. Initialize m_i(t) (e.g., from spike counts), J, h, emission params away from trivial fixed points
4. Iterate: E-step (forward-only for speed, forward–backward for accuracy) → M-step (centred parametrization!) → optional proximal updates with γ₁, β
5. Monitor ΔF_nMF for convergence; validate on held-out spike trains before trusting an expressive emission model
6. Interpret J as EFFECTIVE interaction; evaluate support (|J| ranking) and presynaptic sign (S_j), not numerical conductance agreement

## Pitfalls

- **Binning conflation**: never interpret binned kinetic-Ising self-couplings as network effects — that is exactly the bias SpiKIsing removes by construction
- **nMF breaks the bound**: E[log(1+exp H)] ≈ log(1+exp η) makes F_nMF not a strict lower bound; at stronger coupling consider TAP corrections
- **Forward-only ≠ stationary**: the cheap filter is an extra approximation beyond nMF; check Appendix C-level agreement if accuracy matters
- **Raw 0/1 parametrization**: poorly conditioned (non-zero presynaptic temporal means) — always centre
- **τ^abs identifiability**: profile-estimate it; fixing it wrong distorts recovery-weighted exposures
- **Discrete latent clock**: results depend on Δt; continuous-time latent dynamics is an open extension
- **Emission over-flexibility**: a neural-network-parametrized ρ_i can fit noise or absorb temporal structure into emission instead of network — regularize and held-out validate

## Applications & Extensions

- Direction: continuous-time latent dynamics (no imposed clock) retaining point-process observations
- Direction: TAP / higher-order dynamical mean-field corrections at stronger coupling
- Direction: flexible ρ_i via constrained basis or NN parametrization (with regularization + held-out evaluation)
- Use cases: effective connectivity from high-density MEA / Neuropixels recordings; cross-condition network comparison; drug-response circuit characterization; closed-loop experiment design (generative model to simulate population activity)

## Related Skills

- `mea-array-spiking-rvq-motif-transformer` — discrete generative spike models on MEAs (complementary: motif-vocabulary vs latent-Ising)
- `gtas-generative-spike-train-model` — alternative generative spike-train formalism
- `binary-spiking-causal-models` — causal analysis of binary spiking networks
- `latency-communication-neural-ensembles` — related effective-connectivity inference

## Source

arXiv:2609.17213 — "Latent kinetic Ising models of neural spike trains", Davide Ghio & David Saad (Aston University), cond-mat.dis-nn / q-bio.NC crossover, submitted 2026-09-15. CC BY 4.0.
