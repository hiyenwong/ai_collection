---
name: motif-embedded-spiking-networks
description: Use for motifs and hubs shaping spiking coherence resonance.
category: ai_collection
tags: [neuroscience, spiking-neural-networks, network-motifs, coherence-resonance, scale-free, izhikevich, stochastic-dynamics]
arxiv_id: 2610.00616
paper_title: Stochastic Dynamics of Large-Scale Motif-Embedded Spiking Neuronal Networks
paper_url: https://arxiv.org/abs/2610.00616
companion_arxiv_id: 2610.00597
companion_paper: Stochastic dynamics and synchronization in motif-based neuronal networks
authors: Gurpreet Jagdev, Richard Bertram, Na Yu
published: 2026-09-30
---

# Motif-Embedded Spiking Networks: Local Structure × Global Topology

Factorial simulation methodology for separating how **local motif arrangement** and **global degree structure** jointly shape noise-driven coherent spiking. Companion papers arXiv:2610.00616 (ER/SF embedding + ablation) and arXiv:2610.00597 (six motif classes + heterogeneity).

## Core Methodology

### 1. Four-Architecture Factorial Design

The central trick: hold the **motif skeleton identical** while varying background topology, and hold **synapse count matched** between motif and non-motif networks.

| Network | Background | Motifs | Purpose |
|---------|-----------|--------|---------|
| ER | Erdős-Rényi, p≈0.05 | none | homogeneous control |
| ERM | Erdős-Rényi | M2/M3a/M3b/M3c/M4 | motif effect in homogeneous bg |
| SF | Barabási-Albert, m=50 | none | hub-centred control |
| SFM | Barabási-Albert | same skeleton as ERM | motif effect in hub bg |

- N=1000 neurons, synapse-count parity enforced: non-motif controls use `p̄ ≥ p`, `m̄ ≥ m` (e.g. ERM w_intra=1, w_inter=0.25 → ER effective w̄_inter≈0.266, p̄_exc≈0.0511).
- Intra-motif edges are negligible in degree statistics (≤2 outgoing vs ≈50 inter-motif), so degree distributions overlap between motif/non-motif pairs — isolating *arrangement*, not degree.

### 2. Neuron and Synapse Model (Izhikevich + STDP)

```
dv_i = (0.04v² + 5v + 140 − u + I_i + I_syn)dt + D dW_i    # D = intrinsic noise level
du_i = a(bv − u)dt
if v ≥ v_th: v ← c, u ← u + d
```
- Excitatory heterogeneous (a=0.02, b=0.2, c=−65+15r², d=8−6r², r~U[0,1]) — biases toward regular-spiking; inhibitory fast-spiking (a=0.1, d=2).
- I_i = max{0, Z_i}, Z_i ~ N(µ_I, σ_I²) — applied-current heterogeneity control.
- Synaptic current split into 3 streams with independent weights/decays/delays: inhibitory (w=2, τ=6ms), inter-motif (τ=3ms), intra-motif (w=1, τ=4ms, 0 delay). Delta-pulse + exponential decay per spike.
- All excitatory synapses carry STDP (τ_pre=τ_post=20ms, dA_pre=0.01, dA_post=−0.012, w_max=10).
- Euler–Maruyama, dt=0.5ms, T=2000ms, discard 200ms transient, ≥30 trials, Brian2.

### 3. Coherence Metric: Spectral SNR (Coherence Resonance)

CR = non-monotonic SNR(D) peaking at intermediate noise D*. From population spike train r(t) binned into PSTH:
```
SNR(D) = sqrt( (1/M) Σ_{m∈W} |DFT{r}[m]|² / D² )
```
W = window of M bins centred on dominant spectral peak m*. Also compute **per-motif SNR** (PSTH of each motif instance, averaged per class) — network-level and motif-level views need not agree.

Signal transmission: 20 neurons driven by 300 Poisson afferents (25 Hz, two 25ms epochs), quantify normalized cross-correlation C(τ) between afferent rate λ(t) and population response, peak lag + peak amplitude. Permutation test (10⁴ permutations) for significance.

### 4. Causal Controls: Rewiring and Ablation

**Motif rewiring** — randomly rearrange intra-motif synapses *preserving number and weight*: distinguishes "arrangement matters" from "strong local coupling matters".

**Hub ablation triad** — remove top 7.5% excitatory neurons by degree (hub), same count random (node control), or same synapse count random (edge control). Hub-specific damage beyond cell/synapse loss proves hub-centred organization contributes.

## Key Findings

1. **All four architectures show coherence resonance**; motif embedding shifts SNR curve up and D* left. Gain larger in ER background (+10.7% SNR*) than SF (+2.9%) — strong local structure compensates more for a weak background.
2. **SF/SFM ≫ ER/ERM in absolute coherence** (SNR* ≈ 74 vs 29) and signal transmission: SFM responds in ~50ms at ~47Hz vs ERM ~100ms at ~12Hz; C(τ)≈0.9@40-50ms vs 0.6@90-100ms.
3. **Motif coherence ranking is stable**: M2 (bidirectional pair) > M3c (type-2 recurrent FFL) ≳ M3b > M3a > M4 (bi-parallel), across topologies and w_intra. Companion paper links M2/M3c high coherence to spike doublets (short ISIs).
4. **Arrangement ≠ strength**: rewiring M2/M3c (preserving synapse count+weight) gives the largest SNR reductions; rewiring M3a/M4 *increases* coherence. No motif is uniformly pro- or anti-coherent.
5. **Hubs are load-bearing**: hub ablation drops SNR* 20→11 vs node 17 / edge 13; PSTH peak 50→10Hz, latency 50→100ms. SF advantage is partly hub integrity.
6. **Density vs strength asymmetry**: raising connection probability p_exc converges ER/SF curves (homogenization); raising coupling strength w_inter amplifies their separation (exponential-like SF rise vs linear ER).
7. **Coupling-ratio regimes**: with fixed total strength w_intra+w_inter=60, SFM advantage is largest in inter-motif-dominated coupling and vanishes at w_intra/w_inter=10 (both ≈420). M3a/M4 peak at balanced ratios; M2/M3b/M3c grow monotonically toward intra-dominated.
8. Companion: **heterogeneity** (applied-current σ_I) lowers peak coherence and shifts optimum toward stronger noise; **network size** enhances coherence with saturation.

## Reusable Patterns

- **Factorial structure dissection**: impose local structure identically across two global topologies, synapse-match all controls, then rewiring/ablation to break confounds. Directly portable to connectome analysis, reservoir design, neuromorphic topology selection.
- **Spectral-SNR coherence**: cheap CR quantification for any population spike train; per-cluster SNR decomposes global effects.
- **Effective-coupling matching** (Eq. 7): weighted-average w̄ to compare motif vs non-motif networks fairly.
- **Hub-ablation triad**: hub vs node-matched vs edge-matched removal — template for proving hub-specific contributions in any biological network.

## Pitfalls

- Dense connectivity (p_exc > 0.2) destroys excitability (tonic spiking) — keep below saturation.
- Motif-embedding transmission gains are small vs trial variability; report as trends unless permutation-tested.
- Smaller networks (N=500, p=0.02, w_intra=1.75) needed to make rewiring effects visible — effect size depends on regime.
- Current-based synapses + Izhikevich omit conductance biophysics; conclusions are about arrangement/topology, not spike-waveform detail.

## Related Skills

- [[synaptic-motif-mean-field]] — mean-field derivation for correlated synaptic motifs (complementary theory track)
- [[noise-accelerated-kramers-neural-manifold]] — single-neuron CR via Kramers escape
- [[balanced-network-scaling-conductance]] — heterogeneous connectivity scaling
- [[connectome-wiring-statistics-control]] — separating wiring specificity from statistical controls
