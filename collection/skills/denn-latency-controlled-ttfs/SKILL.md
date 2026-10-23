---
name: denn-latency-controlled-ttfs
description: DeNN closed-form spike time gives design-time SNN latency bounds.
category: ai_collection
---

# Delay Neural Networks: Analytically Controlled Latency for Temporal-Coded Spiking Models

**Source**: A. Gattepaille (I3S, UCA CNRS), A. Muzy (ILLS), arXiv:2610.19732, submitted 14 Oct 2026, cs.NE.

## Core Insight

Classical SNN latency is emergent and only measurable post hoc; no TTFS model before this work allowed a **target latency to be specified and guaranteed analytically at design time**. DeNN (Delay Neural Network) computes spike times in closed form — bypassing membrane-potential thresholding entirely — so latency bounds follow from parameter bounds (Theorem 3.2), enforceable **after training** via a single hyperparameter R ∈ [0,1] per layer.

First work to analyze the accuracy-latency tradeoff on a truly temporal event-based dataset (Google Speech Commands subset) in the TTFS + synaptic-delay framework (prior TTFS work was validated almost exclusively on static MNIST/CIFAR).

## Methodology

### 1. event2time preprocessing (ISI encoding)

Convert event streams to TTFS-compatible single-spike times via inverse average inter-spike intervals:

```
ISI_i = (t_i^last − t_i^first) / (n_i − 1)      # per neuron
# windowed: each time p·N input neurons have spiked, freeze an "image" I_s
# of current average ISIs; 0 spikes → ∞, 1 spike → 0. Repeat over the sample.
```

Why: TTFS assumes one informative spike per neuron; raw event streams violate this. ISI per window restores the single-time representation while preserving temporal structure (frequency coding cannot distinguish a periodic spiker from a burst of high information; ISI coding can).

### 2. DeNN spike-time computation (closed form)

Post-synaptic spike time for image I_s, with κ(x) = e^(−x) (earlier = more important):

```
t_j = τ + o_j
o_j = Σ_i sign(d̃_ij) · κ(z_i + d_ij − z_q) − κ(z_i + c − z_q)
d_ij = c·exp(d̃_ij²)      # learnable synaptic delay (d̃_ij real)
τ = t_q + n_E·[κ(min_i z_i + min_ij d_ij − z_q) − κ(min_i z_i + c − z_q)]
# z: standardized ISIs; z_q: q-th quantile cutoff (ignore spikes after it)
# τ guarantees causality: every post-synaptic spike > t_q
```

### 3. Long-term memory (learnable α, ν timesteps)

```
δ_j^h = z_j[I_s] − z_j[I_{s−h}]
m_j^h = sign(δ_j^h)·(e^(−|δ_j^h|) − 1)
M_j = Σ_{h=s−ν}^{s−1} m_j^h · α_{j}^{−s+ν+h+1}
t_j^e = t_j + M_j            # α is an (N, ν) learnable matrix
```

### 4. Decoding & training

Pseudo-probability over T images: π_c ∝ Σ_s e^(−t_k^e[I_s]) (earlier output spikes = higher class evidence), trained with plain cross-entropy + Adam. Fully differentiable in spike time.

## Latency Control (the core contribution)

**Theorem 3.2** (per-layer): with κ = e^(−x), latency L_j = t_j^e − t_q satisfies

L_j^min ≤ L_j ≤ L_j^max where the bounds depend on (o_j, M_j, α, d_ij, n_E, z_q).

Choose target latency → bound the parameters:
- |d_ij| ≤ −log( ... ) − c·log( ... )   (clamps synaptic delays)
- |α_j| ≤ (L_j − o_j − M_j − n_E·e^{...}) / min(s,ν)

**Hyperparameter R** (post-training knob): L_j = L_j^min + R·(L_j^max − L_j^min). **Lemma 3.3**: if α has a symmetric distribution, it suffices to bound d_ij alone, with an O(1) bound involving √(R(1−e^(−c)))+e^(−c).

Network latency = max over output-layer neurons of the final image's spike time; worst case = R=1 in every layer.

## Empirical Results (GSC 10-class subset, speech2spikes + event2time, ν=50)

| Architecture | Accuracy | L_network | R |
|---|---|---|---|
| 60-128-128-128-10 | 92.56% | 1663 ms | 0.1 (uniform) |
| 60-128-128-10 | 90.81% | 2341 ms | 0.1 |
| per-layer R (0.11,0.044,0.103,0.0091) | **94.25%** | **1477 ms** | tuned |
| + confidence early-exit θ=0.7 | **94.25%** | **1248 ms** | — |

(1-second audio inputs → decision ~477 ms after input end, on average.)

Findings:
- Per-layer R tuning beats uniform R: layer-wise latency budgets matter (the theorem is layer-local; deep stacks accumulate τ's causality overestimation).
- 3-hidden-layer model's latency was NOT monotone in R — theorem holds layer-to-layer but not network-globally; deeper DeNNs complicate analytic tradeoffs.
- Long-term memory concentrates in a handful of neurons per layer (importance metric |m·α|/Δt); with more neurons, memory allocates to fewer of them.
- Confidence thresholding (π_c > θ → early classification) compounds latency savings without accuracy loss.

## Reusable Patterns

1. **Design-time latency guarantees** for event-driven SNNs: derive closed-form spike times → parameter bounds → post-hoc clamp; no retraining needed.
2. **event2time/ISI windowing** to reuse TTFS models on streaming event data (DVS, audio spikes) without abandoning one-spike-per-neuron semantics.
3. **Causality constant τ**: shift layers past the last integrated input by worst-case excitation — simple but overestimates; expect latency inflation in depth.
4. **Per-layer latency budgets** + confidence early-exit as a practical latency-reduction recipe for real-time neuromorphic deployment.
5. **Rank-order importance analysis** (rank-change attribution per memory term) as an interpretability probe for learned temporal structure.

## Limitations / Open

- Theorem is per-layer; network-level monotonicity breaks in depth (observed empirically).
- Analyzed only on a 10-class GSC subset; broader event-based benchmarks pending.
- Comparison to rate-coded SNNs / ANN-SNN conversion (which achieves 1-timestep latency on static data) is orthogonal — those inject an artificial time axis.

**Activation**: TTFS, time-to-first-spike, spiking neural network latency, delay neural network, DeNN, synaptic delay learning, event2time, ISI encoding, neuromorphic speech, Google Speech Commands, real-time inference guarantee, latency accuracy tradeoff
