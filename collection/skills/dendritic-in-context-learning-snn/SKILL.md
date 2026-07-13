---
name: dendritic-in-context-learning-snn
description: "DendriCL: dendritic in-context learning in a single-layer compartmental spiking neural network. Shows that the subthreshold dynamics of a single apical dendritic compartment is structurally identical to leaky online Widrow-Hoff LMS, collapsing general-purpose in-context learning (ICL) to a single layer with frozen synapses -- no attention, no depth, no inference-time plasticity. Solves Garg-2022 ICL at super-dimensional task sizes where dense Transformers grok and fail. Applicable to: biologically-plausible SNN, compartmental neuron models, in-context learning mechanisms, online LMS / adaptive filtering, single-layer architectures, mechanistic interpretability of ICL, grokking avoidance, neuromorphic spiking control."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.02283"
  published: "2026-07-02"
  authors: "Juwei Shen, Yujie Wu, Changwen Chen"
  tags: [spiking-neural-networks, in-context-learning, compartmental-neuron, apical-dendrite, online-lms, widrow-hoff, single-layer, mechanistic-interpretability, grokking, garg-2022, neuromorphic]
---

# DendriCL: Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**arXiv**: [2607.02283](https://arxiv.org/abs/2607.02283) | **Published**: 2026-07-02 | **Category**: cs.NE

## Core Contribution

Demonstrates that **in-context learning (ICL) does not require attention, depth, or inference-time synaptic plasticity**. A single compartmental spiking neuron whose **apical dendritic membrane potential implements an online Widrow-Hoff LMS recurrence** is sufficient. The algorithm is *structurally embedded in the dynamics*, not implicitly discovered by training — verified by a linear probe recovering the reference online-LMS trajectory at **R² = 0.93**.

Prior SNN compartmental models route adaptation through inference-time plasticity and treat the apical dendrite as a passive conduit for teacher/error signals. DendriCL inverts this: the apical compartment is an **active online estimator** whose subthreshold dynamics *are* the learning rule.

## Architecture (three-compartment pyramidal unit)

Each of `d_model = 384` parallel pyramidal-like units has:
- **Basal dendrite**: feedforward projection of the input token `x_t`
- **Apical dendrite**: persistent multi-dimensional subthreshold voltage `u_A` (NOT reset by spikes)
- **LIF soma**: integrates basal + apical, spikes at threshold `θ`

### Equations

```
u_B(t)   = W_B x_t                                    (basal projection)
u_A(t+1) = α u_A(t) + γ e_t W_A x_t                    (apical online-LMS)   (1)
v_soma   = g_B u_B + g_A W_out u_A                   (soma integration)
spike if v_soma ≥ θ; readout active only at query position
```

- `e_t = y_t − W_out u_A(t)` is the prediction error at the labeled context pair
- Synapses `W_A, W_B, W_out` are **frozen at inference** — no weight update
- `u_A` initialized to 0 and evolves continuously across the whole context

### Core mechanism: Apical ≡ Leaky Online LMS

With `W_A = I` and absorbing output projection into readout, the apical update reduces to classical leaky Widrow-Hoff LMS:

```
u_A(t+1) = α u_A(t) + γ e_t x_t
```

**Theorem** (classical LMS convergence, Widrow & Hoff 1960): for `0 < γ < 2/d` and suitable `α`, the apical state satisfies `E‖u_A(k) − w‖ → 0`, i.e. it tracks the true task parameter `w`. DendriCL's contribution is **structural** — this update is embedded in the compartmental architecture and BPTT only tunes `(α, γ, W_A, W_B)`.

## Training & Hyperparameters

- BPTT end-to-end over `(α, γ, W_A, W_B, W_out)`; synapses then frozen
- `d_model = d_apical = 384`, ~0.75M total params
- Membrane: `τ = 4, θ = 1`; arctan spike approximation (Neftci 2019)
- Optimizer: **AdamW, lr = 1e-3**, weight decay
- Initialization: `α̃ = 2.2` (so `α ≈ 0.9` at start), `γ̃ = 0` (so `γ ≈ 0.1` at start); `W` drawn `N(0, 1/d_apical)`

## Benchmark: Garg-2022 ICL

- Linear regression: `w ∼ N(0, I_d)`, `x_i ∼ N(0, I_d)`, `y_i = wᵀ x_i + ε_i`, context length `k = 2d`
- Evaluated at `d ∈ {5, 10, 15, 20, 25, 30, 40, 50}`
- DendriCL R²: `0.807 ± 0.005` (d=5) → `0.820 ± 0.005*` (d=20) at 0.75M params

### Key results
- **Seed-stable at super-d**: Dense Transformers exhibit grokking-style bimodality and **fail past d=40**; DendriCL converges smoothly and monotonically (σ ≤ 0.005 per step) at all tested d
- **Mechanistic verification**: linear probe of apical trajectory into reference online-LMS estimate gives **R² = 0.93** at d=20 — ICL capacity is quantitatively explained by apical encoding quality
- **Depth ablation**: L=1 matches L=2 at d=20 (0.820 vs 0.793) — single layer sufficient
- **Spike cost**: ~17k spikes/forward pass at d=20; apical compartment itself never spikes (subthreshold state); ~85% soma sparsity
- **Width cliff**: `d_apical ≤ 384` all train; `d_apical ≥ 512` diverge (frozen `γ=0` recovers R²≈0.50 even at 768, isolating pathology to apical recurrence). Matches LMS stability bound `γ < 2/(d+2)`

## When to Use This Skill

- Designing biologically-plausible SNNs that must do few-shot / in-context learning
- Replacing Transformer/SSM ICL with a single-layer, energy-efficient, mechanistically-transparent substrate
- Avoiding grokking instability in super-dimensional ICL regimes
- Building neuromorphic controllers where synapse updates at inference are undesirable
- Mechanistic interpretability studies: probing apical membrane to read out the embedded algorithm

## Implementation Checklist

1. Build a 3-compartment spiking unit: basal (W_B projection), apical (persistent u_A), LIF soma
2. Implement apical recurrence exactly as Eq (1) — this IS the learning rule
3. Freeze all synaptic weights after BPTT training
4. Run Garg-2022 protocol: token format `[x_i; y_i; flag_i]`; readout only at query
5. Validate with a linear probe: ridge-regress apical trajectory → reference online-LMS estimate; expect R² ≥ 0.9
6. Keep `d_apical ≤ ~30×d` to stay inside LMS stability region

## Biological Grounding

- Anatomically: apical-basal-soma layout = cortical layer-5 pyramidal neuron (Larkum 2013)
- Apical subthreshold Ca²⁺ plateaus persist 100+ ms; apical-basal coincidence at soma
- Hypothesis (falsifiable via in-vivo recording): cortex implements ICL via apical-LMS dynamics

## Extensions (from paper)

- **Kernel apical**: replace `W_A x_t` with `φ(x_t)` (e.g. ReLU(W1 x_t) or random-feature) → Bayes-optimal if φ includes true nonlinearity
- **Multi-branch apical**: K parallel apical branches, each its own LMS → piecewise-linear estimator
- **Nonlinear readout**: keep apical linear, add small nonlinear `g(u_A)` readout

## Pitfalls

- Do NOT reset apical state on spike — persistence across context is what carries the algorithm
- LMS equivalence holds for the apical compartment only; LIF reset is a separate readout path
- Theorem requires `γ < 2/d`; BPTT may push `γ` unstable if `d_apical ≫ d` → training divergence
- Only validated on Garg synthetic function classes; language/vision ICL unaddressed
