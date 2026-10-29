---
name: snn-privacy-temporal-dynamics
description: "Use when SNN privacy matters. Burst dynamics cut leakage."
category: ai_collection
tags: [spiking-neural-networks, privacy, membership-inference, neuromorphic-security, adex-neurons, temporal-dynamics]
trigger_words: [snn privacy, membership inference spiking, neuromorphic privacy, adex bursting, temporal encoding privacy, burst firing leakage]
---

# SNN Privacy via Temporal Dynamics Design

**Source:** Moshruba & Parsa, "Characterizing Privacy Leakage in Spiking Neural Networks: A Systematic Analysis of Temporal Dynamics, Stochasticity, Neuronal Dynamics and Learning Mechanisms" (arXiv:2610.36243, Oct 2026, cs.NE, George Mason University).

## Core Claim

SNN privacy is **NOT an inherent property of spikes**. Membership-inference (MIA) leakage is a product of three separable factors: (1) how temporal activity is **generated** (input encoding vs intrinsic neuron dynamics), (2) how it is **organized** in time (burst arrangement, not noise), and (3) how it is **learned** (optimization paradigm sets the baseline leakage). Privacy can be engineered: adaptive intrinsic bursting (AdEx) reduces leakage while preserving accuracy — no privacy-performance tradeoff.

## Controlled Factor-Separation Framework

The paper's methodological core: when changing firing behavior in an SNN, four properties change simultaneously — stochasticity, spike timing, neuronal response, and the learning problem. Only a common-framework factor separation can attribute the privacy effect:

| Factor | Manipulation | Controlled | Varied |
|---|---|---|---|
| Temporal representation | Rate vs Poisson-Burst vs Delayed-Burst input encoding | LIF arch, training, attack | spike train organization |
| Stochasticity | temporal jitter, input noise, spike-train noise | firing pattern structure | randomness magnitude |
| Intrinsic dynamics | LIF vs AdEx (burst/delayed-burst regimes) | input encoding, arch size | neuron model internals |
| Learning | backprop (BPTT+surrogate) vs evolutionary (EONS) vs DPSGD | temporal dynamics, attack | optimization paradigm |

## MIA Evaluation Protocol (reproducible)

- **Attack:** Shokri black-box shadow-model MIA, fixed across all conditions. 3 shadow models trained on disjoint splits; member (IN) / non-member (OUT) labels from shadow training sets.
- **Attack feature:** the model representation — for SNNs, the **final membrane-potential at the last simulation timestep**.
- **Attack classifier:** class-specific RBF-SVM, trained per class label on pooled shadow representations.
- **Metric:** direction-invariant MIA AUC = **max(AUC, 1−AUC)**; 0.5 = chance. Always report this form — raw AUC below 0.5 is NOT stronger privacy (the attack decision can be flipped).
- **Utility:** test-set classification accuracy. Report the (accuracy, AUC) pair, never AUC alone.

## Finding 1 — Burst Input Encodings Reduce Leakage at Utility Cost

Under a fixed LIF architecture (membrane decay β=0.95), switching input encoding from Rate to burst-based dynamics:
- F-MNIST: MIA AUC 0.534 → 0.502 (Poisson-Burst) — near chance.
- Breast Cancer: 0.543 → 0.500 (Delayed-Burst).
- Accuracy cost: −5.89% relative (Breast Cancer, DB), up to −15.28% (CIFAR-10, DB).
Rate coding preserves input information best; clustered/delayed spikes make temporal integration harder for downstream LIF.

## Finding 2 — Heterogeneous Dynamics: Moderate Mixes Win, Non-Monotonic

Assign each input dimension d a FIXED dynamics z_d ∈ {Rate, PB, DB} with proportions [π_R, π_PB, π_DB] (assignment frozen through train/test/attack):
- 90R/10DB on Iris: only −0.34% relative accuracy vs homogeneous Rate, while reducing leakage.
- 80R/20PB on Iris: −11.86% accuracy — too much heterogeneity.
- Leakage reduction is **not monotonic** in heterogeneity amount — it depends on the specific temporal composition. Moderate diversity disrupts member-specific response patterns; excessive diversity distorts representations without extra privacy.

## Finding 3 — Stochasticity Is NOT the Mechanism (critical negative result)

Three perturbation types fail to reproduce the burst-encoding privacy gain:
- **Temporal jitter** (spike shifts δ ∈ {−1,+1} timesteps, count-preserving, no collisions): non-monotonic leakage effect, utility drops.
- **Input noise** (pre-encoding): some leakage reduction, but the three dynamics keep distinct responses at all noise levels.
- **Spike-train noise** (post-encoding): stronger reduction only under heavy corruption, still dynamics-dependent.
Conclusion: privacy comes from **how spikes are ARRANGED in time**, not from randomness. Do not equate "noisy SNN" with "private SNN".

## Finding 4 — AdEx Intrinsic Dynamics: Privacy at No Accuracy Cost (headline result)

Generate the burst patterns INSIDE the neuron (AdEx: exponential spike initiation + adaptation variable) instead of at the input:

AdEx equations: C·dV/dt = −g_L(V−E_L) + g_L·ΔT·exp((V−V_T)/ΔT) − w + I; τ_w·dw/dt = a(V−E_L) − w; on spike: V←V_reset, w←w+b.

Regime parameterizations (paper's setup):
- **Burst:** V_T=0.45, τ_w=30, a=0.005, V_reset=0.30, b=0.08 → temporally clustered firing episodes.
- **Delayed-Burst:** V_T=0.54, τ_w=90, a=0.03, b=0.10, V_reset=0.34 → sparse late-onset clusters.

Result: across all 5 datasets (MNIST, F-MNIST, CIFAR-10, Iris, Breast Cancer) and all 3 dynamics, AdEx **lowers MIA AUC while preserving or improving accuracy** vs LIF. The external-encoding tradeoff disappears when the same temporal patterns emerge from internal membrane/adaptation dynamics. Trainable via BPTT + surrogate gradients despite the reset discontinuity.

## Finding 5 — Learning Algorithm Sets the Baseline Leakage

- **Backprop (surrogate-gradient BPTT):** MIA AUC decreases progressively Rate → PB → DB (burst dynamics improve privacy).
- **Evolutionary (EONS/TENNLab, fitness = accuracy):** Rate baseline ALREADY at MIA AUC ≈ 0.5 (chance) — near-ideal privacy with zero temporal engineering. Burst dynamics then only COST utility (Iris DB: −27.3% relative vs −13.8% under BP; BP compensates via gradient access to temporal structure, evolution cannot).
- Design rule: if the training paradigm already yields near-chance leakage, temporal-dynamics privacy interventions are pointless — check the baseline first.

## Finding 6 — Formal DP Interacts With Dynamics (DPSGD)

DPSGD (Opacus, ε = 0.5–2.0, δ=1e-5, max grad norm 1.0) perturbs optimization, NOT the representation:
- At equal ε, dynamics retain DIFFERENT utility: Delayed-Burst recovers to Rate accuracy as ε relaxes (its sensitivity was representation-corruption-dependent); Poisson-Burst stays ~7pp below Rate even at relaxed ε — its intrinsic stochasticity (random burst occurrence AND size) compounds with injected noise at any stage.
- Noise effect depends on the STAGE it enters: representation-level noise (Finding 3) vs update-level noise (DPSGD) produce different per-dynamics outcomes.

## Design Guidance (decision table)

| Goal | Do this | Why |
|---|---|---|
| Privacy with zero utility cost | AdEx neurons in Burst/Delayed-Burst regimes | intrinsic dynamics cut leakage, keep accuracy |
| Near-chance leakage, small models | Evolutionary training (EONS) | baseline AUC ≈ 0.5 without temporal tricks |
| Keep Rate coding + some privacy | moderate per-dimension heterogeneity (e.g. 90R/10DB) | disrupts member patterns, minimal utility loss |
| Formal (ε,δ) guarantee | DPSGD — but pick Delayed-Burst over Poisson-Burst | bounded-delay dynamics recover utility as ε relaxes |
| Avoid | assuming spikes/stochasticity = privacy | disproven by factor separation |

## Reproduction Anchors

- Models: conv-SNN 2×conv(32,64)+FC1000+LIF (MNIST/FMNIST); 4×conv(64,64,128,128)+BN+FC(1024,512) (CIFAR-10); FC1000+LIF (tabular). β=0.95.
- Datasets: MNIST, F-MNIST, CIFAR-10, Iris, Breast Cancer Wisconsin (80/20, seed 42, StandardScaler).
- Direction-invariant AUC reporting; 3 random seeds; shadow/target share temporal assignment within a run.

## Relation to Prior SNN Privacy Literature

Earlier comparative claims ("SNNs more private than ANNs") are conditioned on configuration: leakage varies with data modality (Li et al.), simulation latency (Guan et al. — resilience DECREASES with latency), surrogate-gradient choice and quantization (Moshruba et al.), neuron model (ADPSNN/RADP-SNN), and federated aggregation stage (PriSparK). This paper supplies the missing mechanism-level explanation linking those observations.
