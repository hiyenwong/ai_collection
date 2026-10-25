---
name: purin-synaptic-efficacy-ann
description: Use when adding short-term synaptic plasticity to CNNs.
category: ai_collection
---

# Purin — Split Synaptic Efficacy + Bounded Short-Term Factor for Standard ANNs

**Source**: arXiv:2609.31235, Zishu Liu, Chunbo Luo (Univ. of Exeter), Christos Grecos (UW-Parkside), cs.AI cross-listed, 25 Sep 2026

## Core Idea

Import **short-term synaptic plasticity into ordinary CNNs/MLPs** — no spikes, no discrete time-steps, no extra preprocessing — by (1) splitting each neuron's weight into pre- and post-synaptic efficacy matrices and (2) adding an activation-dependent bounded multiplicative factor that evolves within a training batch and decays back to baseline. Fully backpropagation-compatible.

```
Y = g_stp ⊙ W_out ⊙ f(W_in X)          # neuron equation (Hadamard ⊙)
```

- **W_in**: input-side efficacy (standard trainable weight, updated by BP = long-term plasticity)
- **W_out**: output-side efficacy (presynaptic terminal strength), trainable, **constrained non-negative** so it scales f(·) without flipping sign; init U(0.9, 1.1); **disabled (=1) in the last FC layer** for stability
- **g_stp**: bounded short-term factor, per-channel in conv layers (C elements), per-neuron in FC layers
- **f(·) = Leaky ReLU(α=0.01)**, reinterpreted as a *signed magnitude function*: activity deviation from baseline firing rate (>0 excitatory-like, <0 inhibitory-like), NOT an instantaneous firing rate

## The Two Key Abstractions

1. **Time-interval abstraction** (the enabling move): a still image = information presented over a short interval (justified by RSVP psychophysics — visual recognition unfolds over ~a presentation interval, not an instant). Within one batch, long-term weights W_in/W_out are frozen (long-term plasticity hasn't occurred yet) while g_stp drifts with incoming activity. Batch completion = long-term update event; g_stp then resets. This imports temporal dynamics into feedforward nets without spike encoding or RNN machinery.
2. **Split-synapse abstraction**: biological chemical synapses have pre- AND post-synaptic components; ANNs collapse both into one matrix, discarding presynaptic enhancement/attenuation. W_out restores the output-side pathway.

## g_stp Dynamics (verified stable)

```python
# per-sample forward update (conv: channel-mean of f(W_in X); λ=1e-4)
g_new = g_old + λ * s / N

# per-sample recovery toward default d=1.0 (b = batch size)
g' = g + (d - g) * (1 - exp(-1/b))      # ⇒ (g' - d) = (g - d)·exp(-1/b)

# bounds: clip g to [0.8, 1.2] (mild modulation, prevents blow-up)
# reset g to 1.0 at epoch end and before train/val/test to prevent leakage
```

Distance to default shrinks geometrically by exp(−1/b) per sample — provable recovery, no oscillation.

## Backprop Gradients (mechanism is differentiable end-to-end)

```
Δw_out_i = Σ_j (∂L/∂y_j) · g_stp_i · f(Σ win_i x_i)          # g_stp scales long-term update
Δwin_i   = Σ_j (∂L/∂y_j) · g_stp_i · w_out_i · f'(·) · x_i   # both factors enter input gradient
# conv: ΔW_out = g_stp * Σ (f(W_in X) ⊙ ∂L/∂Y)  (g_stp shared within channel)
```

## Deliberate Exclusions (each with a reason)

- **No bias vector**: bias ≈ instantaneous firing threshold — meaningless under the time-interval abstraction (they tried to find a biological reading, failed honestly, dropped it)
- **No dropout**: random masks make input sums stochastic → g_stp would update on corrupted activity
- **No batch norm**: isolates the mechanism's effect (also why "matched baselines" exist — see below)

## Results (honest-reporting protocol worth copying)

**Problem they self-identified**: vanilla vs Purin+Purin models differ in input scaling ([0,1] vs [−1,1]), activation (ReLU vs Leaky ReLU), dropout, BN — 4 confounders. Vanilla comparisons are NOT fair.

**Matched baselines** (same scaling/activation/dropout=off/BN=off): Purin wins on **all 4 datasets × 3 architectures**:
- VGG11: UCM 51.3→68.2 (+16.9), Oxford102 10.5→23.8 (+13.3), CIFAR-100 33.3→39.8, AID 50.2→57.8
- GoogLeNet: UCM 49.9→74.0 (+24.1), CIFAR-100 39.2→52.8 (+13.6) — Purin largely *replaces* BN's benefit in BN-free nets
- AlexNet: UCM 61.3→72.2, Oxford102 16.6→26.8 (+10.2)

**Ablation**: split weights (B) deliver most of the gain (+4% or more nearly everywhere); g_stp adds +0.2–5% on top (C).

**g_stp variant sweep** (VGG11/GoogLeNet, CIFAR-100+UCM): random U(0.8,1.2) per sample (A) always worst — up to 18% worse for GoogLeNet ⇒ **g_stp ≠ noise; the activity-dependence is the point**. Exponential recovery + bounded range (their variant E) best and most consistent.

**SE-block control**: matched GoogLeNet+SE (conv-inserted or original placement) lands 13–25% below GoogLeNet+Purin ⇒ g_stp⊙W_out is NOT a weak SE-style channel recalibration.

**Cost**: extra params < 0.2% (AlexNet 0.016%, VGG11 0.008%, GoogLeNet 0.12%). Overhead per layer: conv `1/(C_in·k²)`, FC `1/N_in`.

**Residual viability** (supplement): ResNet20-like, Purin on 1×1 residual paths: 69.35% vs 69.53% vanilla CIFAR-10 — no severe degradation. Residual form: `Y = g⊙W⊙(f_end(W_in X) + X_res)`.

**Limitations stated**: not tested on modern residual/transformer stacks at scale; gains inconsistent vs *vanilla* (only consistent vs *matched*); g_stp curves drift upward within batch (traced to Leaky ReLU's 0.01 negative scaling weakening negative updates).

## Reusable Patterns

1. **Split-weight neuron drop-in**: `nn.Linear`/`nn.Conv2d` → W·x becomes `g ⊙ W_out ⊙ f(W_in·x)` with W_out non-negative (softplus param) — 3-line change, <0.2% params
2. **Interval abstraction**: any within-batch stateful factor (plasticity, gain, fatigue) for feedforward nets — define batch boundary as the "long-term event", reset state there
3. **Bounded activity-dependent factor with geometric recovery**: `g ← clip(g + λ·mean(f(z)), lo, hi)` + `g ← g + (d−g)(1−exp(−1/b))` — stable by construction
4. **Confounder audit + matched-baseline construction**: enumerate every unintended difference (scaling, activation, regularization), rebuild the baseline holding those fixed, THEN claim mechanism credit
5. **"Is it just X?" control experiments**: random-factor variant and SE-block substitution directly test whether the mechanism reduces to noise or to known attention/gating — generalize this disproof pattern to any new modulation mechanism
6. **Disable mechanism in final layer**: stability-first placement (W_out=g=1 in the classifier head)

## When to Use / Extend

- Brain-inspired augmentation of CNNs where SNN conversion is undesirable (no spike encoding, BP-native)
- Studying whether short-term plasticity (Tsodyks-Markram style) can be lifted into rate-based ANNs — this is the cleanest BP-compatible formulation to date
- Open extensions: residual/transformer stacks (paper only sketches ResNet20), recurrent variants where g_stp interacts with real temporal inputs, replacing hand-set [0.8,1.2] bounds with learned per-layer bounds

**Activation**: synaptic efficacy modulation, short-term plasticity ANN, split weight matrix, bounded activity-dependent factor, time-interval abstraction, biology-inspired CNN, backprop-compatible plasticity, presynaptic output-side efficacy, matched baseline confounding audit, Purin mechanism
