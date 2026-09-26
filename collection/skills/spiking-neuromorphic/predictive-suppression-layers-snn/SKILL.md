---
name: predictive-suppression-layers-snn
description: Predictive coding layer variants for communication-efficient spiking neural networks — a per-layer predictor transmits only "surprising" spikes, via signed spiking residuals (error units) or an error-magnitude-driven gate that suppresses predictable activity (predictive suppression, including strictly event-driven hard-STE and respike binary variants). Achieves ~3× reduction in communicated inter-layer activity while increasing task accuracy, with metrics that decouple local processing cost (E_local) from communication cost (E_comm). Use when optimizing SNN inter-core/wireless communication overhead, designing predictive coding layers for neuromorphic hardware, energy-constrained IoT edge inference, or when total-spike-count minimization is the wrong objective because communication dominates the energy budget. Activation: SNN communication efficiency, predictive coding spiking layers, event-driven gating, surprise encoding, neuromorphic inter-core communication, E_comm metrics, N-MNIST SHD.
license: MIT
metadata:
  arxiv_id: "2609.21583"
  published: "2026-09-18"
  authors: "Aidin Attar, Michele Rossi (University of Padova)"
  tags: [spiking-neural-networks, predictive-coding, communication-efficiency, neuromorphic, event-driven, iot-edge]
---

# Predictive Suppression Layers for Communication-Efficient SNNs

Source: arXiv:2609.21583 (2026-09-18) — Attar & Rossi, Univ. of Padova. EWSN workshop
(Neuromorphic Physical Layer Signal Processing for Wireless Systems).

## Motivation: Split the Cost Model

Standard SNN energy accounting uses **total spike count**, but that conflates two costs
that are not interchangeable on real hardware:

```
E_total = E_local + E_comm
```

- `E_local`: local processing activity (encoding, prediction) — cheap, stays on-core.
- `E_comm`: activity communicated across layers/cores/wireless links — expensive.

On many-core neuromorphic chips and IoT nodes, communication dominates the energy budget
(IoT nodes: comms ≈ most of consumed energy). A design that *adds* local computation to
*subtract* channel traffic is the right trade in these regimes. Define a cost ratio ρ =
communication weight / local weight; predictive suppression crosses break-even vs. a
matched SNN baseline at **ρ* ≈ 2.1** — above it, predictive suppression is cheaper.

## Architecture: Two Variants, One Predictor Block

Each predictive layer learns a predictor of its own input/latent activity, producing a
residual `e_ℓ[t]`; prediction error magnitude `m_ℓ[t]` drives the layer's output.

### 1. Error Units (direct predictive coding)
Transmit the signed residual as spikes (negative errors need a second population):

```
y_ℓ[t] = LIF( [relu(e_ℓ[t]) ; relu(−e_ℓ[t])] )
```

### 2. Predictive Suppression (residual as control signal) — the stronger variant
Use residual magnitude as an error-driven gate on the latent spike train:

```
g_ℓ[t] = clamp(1 − e^(−α m_ℓ[t]), g_min, 1)      # α = 10, g_min = 0.05
y_ℓ[t] = g_ℓ[t] · z_ℓ[t]                          # graded amplitude-modulated spikes
```

Predictable input → gate closes toward g_min, spikes suppressed; surprising input → gate
opens, spikes forwarded. The communicated signal is *graded* (continuous gate × binary
spikes) — the downstream layer remains a normal spiking LIF consumer.

### 3. Strictly Event-Driven Binary Variants
- **hard-STE**: `y_ℓ[t] = 1[g_ℓ[t] ≥ θ] z_ℓ[t]` — binary forward pass, gradients flow
  through the continuous gate via straight-through estimator. θ = 0.3 (N-MNIST), 0.1 (SHD).
- **respike**: `y_ℓ[t] = LIF(γ g_ℓ[t] z_ℓ[t])`, γ = 4 — re-binarizes the graded current
  through a LIF, yielding a conventional SNN block.

### Training Objective

```
L = L_task + β (L_pred + λ L_rate),   β = 0.1, λ = 2
L_rate = [0.05 − r̄_pred]₊²            # prevents predictor collapse to silence
```

The min-rate regularizer is essential — without it the predictor can trivially suppress
everything.

## Key Results (N-MNIST, SHD)

- **~3× reduction in communicated activity** while *increasing* task accuracy on both
  datasets (predictive suppression variant).
- First suppression layer: message carries **7× less weighted activity** than baseline
  (198 vs. 1397) with linear-probe accuracy on the compressed message ≈ the full
  representation — the gate removes only what the downstream decoder doesn't need.
- **Selectivity is prediction-driven, not random**: communicated activity rises
  monotonically with prediction-error magnitude; surprise-selectivity index SSI ≈ 0.75,
  redundant-communication fraction RCF ≈ 0.07. (A random gate could compress while wasting
  activity on predictable inputs — this diagnostic rules that out.)
- **Temporal transfer (SHD)**: error-units variant performs poorly; the error is more
  useful as a *control signal* (gate) than as the message itself. Binary variant choice is
  dataset-dependent, not universal.

## Evaluation Metrics (reusable protocol)

1. Report `E_local` and `E_comm` separately, never total spike count alone.
2. **Linear-probe decodability** of the communicated message vs. full local representation
   at each layer (channel preserves task information).
3. **Surprise-selectivity index (SSI)** and **redundant-communication fraction (RCF)**:
   communicated activity as a function of prediction-error magnitude must be monotone.
4. Weighted cost `C(ρ)` curves vs. the matched SNN baseline across communication/local
   cost ratios ρ; report break-even ρ*.

## When To Use

- Communication-dominated regimes: many-core neuromorphic hardware (inter-core
  fan-out), wireless feature transmission to a decision point, IoT edge nodes.
- Any SNN where you want output features that are *more linearly decodable* — the gate
  doubles as a redundancy filter that improves representation power.
- As a layer primitive to compose (feedforward here; top-down/iterative and convolutional
  gates are stated future work).

## Pitfalls

- Predictive coding **increases total spiking activity** (the predictor is extra local
  work) — it is a win only when ρ > ρ* ≈ 2.1. Never sell it as spike-count minimization.
- Graded gate output is not a pure binary event stream; if the substrate demands strict
  events, use hard-STE or respike and re-tune θ/γ per dataset.
- Without the min-rate regularizer the predictor collapses and the channel silences.
- Error-units (transmitting residuals directly) generalize worse on temporal data than
  gating the latent train.

## Related

- Classical Rao–Ballard predictive coding (transmit only what higher areas cannot predict)
  recast as a *hardware communication* principle.
- Complements spike-sparsity optimization: orthogonal axis — sparsity cuts activity,
  suppression cuts *redundant communicated* activity.
