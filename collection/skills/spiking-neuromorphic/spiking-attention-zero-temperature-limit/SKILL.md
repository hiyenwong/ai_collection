---
name: spiking-attention-zero-temperature-limit
description: Spiking attention as zero-T limit of two-level systems.
category: ai_collection
---

# Spiking Attention as the Zero-Temperature Limit of Two-Level Systems

**Paper**: Softmax-Free Attention in Spiking Transformers as the Zero-Temperature Limit of Two-Level Systems
**arXiv**: 2610.15968 (Sotero, Taghipour, Sanchez-Bornot — Univ. Calgary Hotchkiss Brain Institute + Ulster, 11 Oct 2026)
**Categories**: cs.LG, cs.NE, q-bio.NC

## When to Use

- Analyzing spiking Transformer attention (Spikformer, Spike-driven Transformer, SpikeGPT, QKFormer) from a thermodynamic/statistical-mechanical angle
- Diagnosing or fixing surrogate-gradient vanishing in hard-threshold networks
- Choosing/tuning the surrogate slope α as a principled control variable rather than a heuristic
- Estimating the physical energy floor of spiking attention layers
- Extending the softmax-Boltzmann/Hopfield attention framework to softmax-free architectures

## Core Contribution

Removing softmax is not a temperature change — it is an **ensemble change**. Softmax attention is the Boltzmann measure of ONE coupled N-state categorical system (keys compete through shared partition function Z_i). Deleting the shared denominator decouples the keys into a **product of N independent two-level systems**, one per query-key pair, and splits the single temperature into a forward value (0) and a backward value (1/α).

### The exact correspondence

| Object | Softmax attention | Spiking attention |
|---|---|---|
| Ensemble | one coupled N-state categorical (Potts-like) | product of N two-level systems |
| Energies | E_ij = -s_ij, s_ij = q_iᵀk_j/√d_k | pair gap Δ_ij = θ - γ·s_ij (θ threshold, γ gain) |
| Normalizer | shared Z_i = Σ_j e^{-βE_ij} | per-site z_ij = 1 + e^{-β_s Δ_ij} (no coupling) |
| Measure | A_ij = e^{-βE_ij}/Z_i | p_ij = σ(β_s(γs_ij - θ)) — Fermi-Dirac ≡ logistic |
| Operating point | β = 1 (finite, entropy-bearing T) | forward T_s → 0; backward T_eff = 1/α |
| Deployed operator | continuous weights | a_ij = Θ(γs_ij - θ) ∈ {0,1} = **exact T→0 limit** |

Key identity: `lim_{β_s→∞} σ(β_s·u_ij) = Θ(u_ij)`, u_ij = γs_ij - θ. The hard spike IS the zero-temperature occupation.

**Backward temperature**: differentiating the two-level occupation at β_s = α gives ∂p/∂s = αγ·σ'_α(γs_ij - θ) — the standard fast-sigmoid surrogate gradient is exactly the two-level score-gradient evaluated at finite backward temperature T_eff = 1/α. Forward pass runs at T=0, gradients at T=1/α.

**Why the softmax framework breaks**: binary a_ij vectors have exact zeros and row-mass ∈ {0..N}, not 1. No finite β and normalizer Z_i can reproduce them. Row-normalizing the spike pattern gives an infinite-temperature measure on a zero-temperature-selected support — outside the one-parameter softmax family entirely.

## Consequence 1: Ordered-Phase Pinning

- Binary entropy S̄⁽²⁾ → 0 and order parameter φ⁽²⁾ = 1 - S̄⁽²⁾/ln2 → 1 for **every input** — the forward pass is strictly pinned in the frozen ordered phase
- This single fact explains BOTH spiking attention's defining properties:
  - **Sparsity/efficiency**: frozen {0,1} states = the multiplication-free regime
  - **Optimization difficulty**: true gradient of a frozen state is zero; all learning flows through the surrogate band |γs_ij - θ| < O(1/α)
- Empirical signature: trained networks **actively evacuate the trainable band**. Active-pair fraction scales as α^{-1.51} (power-law fit), not the naive geometric α^{-1.00} — the network pushes scores away from the threshold to minimize entropy, self-deepening its own vanishing-gradient regime
- Energy efficiency and optimization difficulty are two faces of one zero-temperature limit

## Consequence 2: Landauer Floor Shift (postulate, falsifiable)

- Softmax First Law of Learning: -ΔL ≈ T·(⟨S⟩_init - ⟨S⟩_final) + ΔI(Ŷ;Y), bound -ΔL ≥ T|Δ⟨S⟩|
- Spiking: per-input entropy is pinned ⟹ heat term collapses to trivial -ΔL ≥ 0
- Cost shifts to the **across-ensemble spike-pattern entropy** S_spk = (1/|N|) Σ_n H_bin(π_n), π_n = dataset-level firing probability of attention neuron n over all heads/layers
- New First Law: -ΔL ≈ T_eff·(S_spk^init - S_spk^final) + ΔI(Ŷ;Y), floor -ΔL ≥ T_eff|ΔS_spk|
- Physical energy floor: E_attn ≥ C_AP·n̄ where C_AP = energetic cost of one action potential, n̄ = mean spike count — independent of synaptic weight magnitudes
- Local per-input entropy frozen ≠ global pattern uninformative: learning selectively tunes WHICH attention neurons fire per input, driving S_spk down

## Experimental Validation (CIFAR-10, compact 2-block spiking Transformer, d=64, 4 heads)

1. **Order parameter**: spiking model pinned near φ⁽²⁾=1 at native operating point (star); softmax baseline shows full disordering crossover with T=1 deep inside it
2. **Schottky anomaly**: spiking specific heat rises from 0, single interior peak at T_c, decays to 0 — the classical fingerprint of a two-level DOF. A coupled categorical system cannot produce this per-pair profile. Operating point sits on the cold flank of T_c
3. **Trainability vs α**: accuracy peaks at intermediate backward temperature, collapses at large α (surrogate band narrows + pinning pushed scores out of band); small α slightly degrades via architectural bias (broad surrogate ≈ poor approximation of hard forward map)
4. **Entropy trajectory**: S̄⁽²⁾ flat at ~hundredths of nats all run (pinned); S_spk falls from ~0.43 nats in exact alignment with evaluation loss — confirms the First-Law postulate qualitatively (quantitative Landauer test left open: needs direct ΔI measurement)

Config: 4 timesteps, θ=1, γ=1, LIF soft-reset, AdamW 1e-3, 100 epochs, α sweep 2→100 (7 levels), β_s sweep 0.1→100, softmax T sweep 0.01→10.

## Practical Guidance

1. **Treat α as a physical temperature** — schedule it. Cooling α upward toward the hard threshold during training = simulated annealing. Start broad (high backward-T), cool gradually
2. **Avoid large α early**: pinning evacuates the |u|<1/α band, so steep surrogates train only a vanishing subset of pairs
3. **Audit gradient support**: measure the active-band fraction (pairs with |γs-θ|<1/α) during training; exponent steeper than -1 confirms self-evacuation and predicts stall
4. **For energy estimates**: use the activity floor C_AP·n̄ — spike count, not MAC counts alone, is the thermodynamic currency
5. **Hybrid operators**: partial cross-key renormalization would move the architecture off the T=0 endpoint back toward finite-temperature softmax dynamics — a principled efficiency/trainability dial
6. The framework applies to ANY hard-threshold unit trained by continuous surrogates (not just attention)

## Related Skills

- `winner-take-all-spiking-transformer-language` — WTA spiking transformer (cited as ref [6])
- `spiking-transformer-effective-dimension` — theory of spiking transformers
- `attention-sink-structural`, `phase-transition-attention-bayesian` — attention phase structure
- `surrogate-gradient-snn-training` — the α machinery this paper re-derives thermodynamically

## Key Equations

```
p_ij(β_s) = e^{-β_s Δ}/(1+e^{-β_s Δ}) = σ(β_s(γs_ij - θ)),  Δ_ij = θ - γs_ij
lim_{β_s→∞} p_ij = Θ(γs_ij - θ) = a_ij          # spike = zero-T occupation
∂p_ij/∂s_ij |_{β_s=α} = αγ σ'_α(γs_ij - θ)      # surrogate = finite-T gradient
φ⁽²⁾ → 1, S̄⁽²⁾ → 0  (β_s→∞)                     # ordered-phase pinning
-ΔL ≈ T_eff(S_spk^init - S_spk^final) + ΔI;  E_attn ≥ C_AP·n̄
```
