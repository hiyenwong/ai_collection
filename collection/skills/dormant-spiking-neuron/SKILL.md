---
name: dormant-spiking-neuron
description: "Dormant Spiking Neuron (DSN) methodology from arXiv:2610.21748 (NeurIPS 2026). State-driven postsynaptic sparsity for SNNs: an irreversibly-closing dormancy gate D_t = D_{t-1}·Theta(V_{t-1} - D_th) prunes subthreshold dynamics of deeply inhibited neurons (44% of ResNet-18 units sit at V_m ≤ 0), trained end-to-end via BPTT with surrogate gradients through both the spike and dormancy Heavisides. Use when building energy-efficient SNNs, reducing synaptic operations beyond input-driven (presynaptic) sparsity, combining event-driven spiking with neuron-state gating, or analyzing membrane-potential distributions / postsynaptic computational overhead. Activation: spiking neural network efficiency, dormant neuron, state-driven sparsity, membrane potential threshold, surrogate gradient BPTT, neuromorphic energy reduction, postsynaptic gating, dynamic pruning."
---

# Dormant Spiking Neuron (DSN)

Source: arXiv:2610.21748 (NeurIPS 2026), Ma et al., UESTC. Code: https://github.com/Ruichen0424/DSN

## Problem: postsynaptic subthreshold overhead

SNN efficiency normally comes from **input-driven (presynaptic) sparsity**: computation triggers only on arriving spikes, skipping inactive weight-matrix *rows*. But a receiving neuron still runs membrane integration + leakage at **every** timestep even when it will never fire.

Measured on an ImageNet-trained ResNet-18 SNN, the membrane-potential CDF splits into three regions:
- ~26% active spiking region (near/above threshold)
- ~30% subthreshold active (0 < V_m < V_th, may spike soon)
- **44% deeply inhibited (V_m ≤ 0)** — negligible firing probability, yet full state-update cost every timestep

This is *chronic, per-instance* waste that static pruning (removing neurons by dataset-level firing rate) cannot see: the redundant set changes per input sample.

## Mechanism: irreversible dormancy gate

Per-neuron binary gate D_n^t ∈ {0,1}, integrated into LIF dynamics as a 4-step per-timestep pipeline:

1. **Dormancy gate update**: `D_n^t = D_n^{t-1} · Θ(V_n^{t-1} − D_th)` — multiplicative AND makes closure **irreversible** for the rest of the sample's forward pass (D_0 = 1, V_0 = 0). D_th < 0 is a predefined negative threshold.
2. **Potential integration** (only if active): `H_n^t = f(V_n^{t-1}) + W_n S_{n-1}^t`, f(V)=τ⁻¹V for LIF.
3. **Gated firing**: `S_n^t = D_n^t · Θ(H_n^t − V_th)` — dormant neurons can never fire again, so their membrane updates need not execute at all.
4. **Reset**: `V_n^t = H_n^t (1 − S_n^t) + V_reset · S_n^t`.

Two Heavisides (spike firing, dormancy gate) → both get surrogate derivatives in backward.

## Orthogonal sparsity = multiplicative savings

- Input-driven sparsity skips weight-matrix **rows** (presynaptic spike absence)
- DSN state-driven sparsity skips weight-matrix **columns** (postsynaptic dormancy)
- Combined: `SOPs_DSN = MACs · Σ_t (R_t · D_t)` — the two rates multiply. Order-of-operations: check D first, then skip both integration and the row-sparse gather for that column.

This is the key structural insight: DSN is *not* another pruning method. It exploits instance-level transient redundancy (per-sample dormancy masks), not dataset-level chronic redundancy. Layer-wise Jaccard similarity of dormancy masks across inputs is < 0.2 in 12+ layers of ResNet-34, i.e. masks are highly sample-specific — exactly what static pruning (similarity ≡ 1) cannot capture.

## BPTT with surrogate gradients (the load-bearing part)

Static post-hoc thresholding (ITO) fails on nonstationary streams: early inhibition does not imply future unimportance; a dormant neuron is permanently silenced, so prematurely gating a critical neuron destroys late-arriving features. Therefore **train the dormancy policy itself**:

Forward: exact Heavisides. Backward: substitute σ′(x) = α·σ(x)(1−σ(x)) with α = 4.0 (sigmoid surrogate, same for spike and dormancy).

Error-term recurrence (the four coupled deltas that make it work):

```
δ_H = δ_S · [D^t · σ'_s(H − V_th)] + δ_V · (1 − S^t)        # spike path gated by D
δ_S = W_{n+1}^T δ_{H,n+1}                                    # spatial layer-to-layer
δ_V = δ_D^{t+1} · [D^t · σ'_d(V − D_th)] + δ_{H}^{t+1} · f'(V)  # dormancy gate is differentiable-in-time
δ_D = δ_D^{t+1} · Θ(V^t − D_th) + δ_S · Θ(H^t − V_th)        # gate passes error while open
```

The δ_D recurrence is the novel piece vs. standard surrogate-gradient SNN training: gradient flows *through the gate state across timesteps* (via Θ(V−D_th) on the δ_D path and σ'_d on the δ_V path), so the network learns which neurons may safely go dormant without cutting critical information flow. Weight gradient: ∂L/∂W_n = Σ_t δ_H^t (S_{n-1}^t)^T.

## Results

| Setting | Cost ↓ | Accuracy |
|---|---|---|
| CIFAR10 ResNet-18 (BPTT) | ~50% | 95.34 (base 95.64) |
| DVS-Gesture SD-T-2-256 (BPTT) | 42% | 96.88 (base 96.88, no loss) |
| DVS-CIFAR10 (BPTT) | 52% | 77.9 (base 78.1) |
| ImageNet ResNet-18 (BPTT) | ~73% | 64.44 (+1.34 over 63.10 base) |
| ImageNet ResNet-34 (BPTT) | ~64% | 69.63 (+0.21 over 69.42) |

- Beats SOTA static pruning (AT-LIF ↓77%@59.61, UniSparse ↓78%@61.89) at comparable cost: DSN gets 64.44% at ↓~73%.
- D_th sweep: −0.01 gives max sparsity (↓71% on CIFAR-10, ↓73% DVS) with −0.3pp accuracy; −1.0 is conservative (↓21–38%).
- Hardware: 1-bit dormancy mask per neuron gates off 32-bit weight-memory accesses; recent SPU designs (Zhou et al. 2026) exploit both spike and neuron sparsity, <0.06 pJ/SOP.
- Neuronal Computational Utilization (NCU) stays high across layers — dormancy removes deeply-inhibited updates without suppressing active firing.

## Implementation recipe (SpikingJelly-style)

1. Add a boolean `dormant` buffer per neuron layer, init True (=active), plus D_th (start −0.05).
2. Per timestep: `dormant &= (V_prev >= D_th)`; where dormant, skip integration (zero H, V frozen at last value), force S=0.
3. Register a custom autograd Function replacing both Θ's with sigmoid surrogate α=4 in backward; route gradient through the dormant-mask path per the δ_D recurrence (treat the mask check as Θ(V−D_th)).
4. Train from scratch (BPTT paradigm) rather than ITO on nonstationary/event data; fine-tune from a pretrained SNN checkpoint if the dataset is small (DVS-Gesture protocol).
5. Report SOPs as `MACs · Σ_t R̄_t·D̄_t` to capture the multiplicative effect; measure layer-wise dormancy-mask Jaccard to verify instance-adaptivity.

## Pitfalls

- **Irreversibility is per-sample, not forever** — gates reset each forward. But within a sample, a wrongly-dormant neuron is unrecoverable; only BPTT training mitigates this, not post-hoc ITO.
- ITO mode is safe only on quasi-stationary inputs; prefer BPTT for event streams.
- D_th is a global constant, not learned — tuning range [−1.0, −0.01]; deeper negatives = fewer dormant neurons.
- Hard reset (V_reset=0), τ=2.0, V_th=1.0 across all their experiments — deviate cautiously.
- The 44% deeply-inhibited figure is from ImageNet ResNet-18; measure your own V_m distribution before assuming the same split.
