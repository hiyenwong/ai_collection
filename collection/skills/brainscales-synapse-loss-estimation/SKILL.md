---
name: brainscales-synapse-loss-estimation
description: Use when mapping SNN models to crossbar neuromorphic hardware to predict synapse loss. Binomial-cascade method.
category: ai_collection
---

# BrainScaleS Synapse Loss Estimation (Binomial-Cascade Method)

**Source**: Vogginger & Mayr (TU Dresden), "Synapse Loss Estimation for the BrainScaleS Wafer-scale Neuromorphic System", arXiv:2610.07321 (Oct 2026, cs.ET/cs.NE).

## Problem

Mapping computational-neuroscience network models to crossbar-based neuromorphic hardware (BrainScaleS wafer, but also any hierarchical circuit-switched SNN substrate) causes **synapse loss**: some model synapses find no hardware synapse, due to (a) structural limits (synapse drivers, address decoders) and (b) mapping-algorithm shortcomings. Synapse loss silently distorts connectivity — critical when reproducing biological measurements or running parameter sweeps.

## Hardware Model (BrainScaleS-1 / HICANN)

- 1 wafer = 384 HICANN ASICs (16 unusable → 368), ~200k neurons, ~44M synapses, 10,000× faster than biological real-time.
- Each HICANN: 512 neuron circuits (AdEx model, conductance-based synapses), 114,688 synapses, 56×4=224 synapse drivers per side boundary... 224 drivers total per HICANN (4 quadrants × 56).
- Crossbar: synapse driver (row periphery) → synapse matrix (256×224 per block) → neuron column.
- **Distributed 2b/4b address decoding**: 6-bit spike address split — 2 MSB decoded per half synapse row (strobe patterns A/B/C/D in the driver), 4 LSB decoded per synapse (4-bit SRAM + comparator). One 4-bit address (15) reserved to disable synapses (weight-0 leaks current) and address 0 reserved for DLL locking → only **59 of 64 addresses usable per routing source**.
- Up to 64 neuron circuits combine into one compound neuron → up to 14,336 input synapses per logical neuron.
- Synapse driver chains limited (software default 3, max 5) — signal quality degrades beyond.
- Mapping pipeline: (1) neuron placement → (2) merger-tree routing (≤64 neurons per horizontal bus) → (3) external input placement → (4) wafer routing (horizontal→vertical buses, sparse crossbar switches S=8/S=32) → (5) HICANN synapse routing (driver requirement calc → driver assignment → synapse assignment) → (6) parameter transformation (calibration, 4-bit weights + row-wise gmax).
- Synapses with identical (target neuron, synapse type, 2-MSB pattern) are **equivalent** — implemented by the same hardware synapses. This equivalence is the key compression the analysis exploits.

## Method 1: Maximum Lossless Network Size (bottom-up expectation)

For uniform random connectivity (n sources → N_nrn targets, connection probability p), synapse counts per target follow **Binomial(n, p)**. Four steps, each a probability convolution:

1. **Per-pattern synapse distribution**: for one 2-MSB pattern (16 sources), k synapses arrive with B(k|n=16,p). For all N_nrn targets simultaneously: F(k|n,p,N) = F(k|n,p)^N (iid product).
2. **Max-synapse distribution**: P_Smax(k) = F(k)^N − F(k−1)^N. Convert to **half-row demand** per pattern via the neuron-size-dependent capacity S_{H,nrn} (Table: neuron size 4→1, 8→2, 12→3, 16→4, 32→8, 64→16 synapses per half row per target). P_H,pattern(k) sums P_Smax over the capacity window of the k-th row.
3. **Convolve 4 patterns**: P_H(k) = Σ_{k1+k2+k3+k4=k} Π_i P_H,pattern_i(k_i) — the demand in half rows for one routing source (64 addresses).
4. **Driver demand**: 4 half rows per driver → P_D(k); expectation E[D] = Σ k·P_D(k).
5. **Capacity division**: E[routing sources] = min(224/E[D], 224); max source neurons = E[routing sources] × 64 (or ×59 with constraints).

## Method 2: Synapse Loss Estimation (top-down marginal gain)

Reverse view — assign D drivers per routing source, count what cannot be realized:

1. **Survival function**: G(k|n,p) = 1 − F(k|n,p) = P(more than k synapses per neuron).
2. **Synapse gain of the k-th half row** (zero-based): ΔS_pattern(k) = Σ_{i=k·S_H}^{(k+1)·S_H−1} G(i|n,p) · N_nrn — the expected extra synapses realized by adding one half row to that pattern.
3. **Optimal allocation**: pool gains of all 4 patterns, sort descending (ΔS_sorted), take the top 4·D — S_realized(D) = Σ_{i<4D} ΔS_sorted(i), S_lost(D) = Σ_{i≥4D} ΔS_sorted(i). Relative loss ν = S_lost/(S_realized+S_lost).
4. **Driver distribution across L routing sources**: L ≤ 224 → D_ceil=⌈224/L⌉ to (224 mod L) sources, D_floor to the rest; L > 224 → surplus sources get 0 drivers (all their synapses lost).

## Key Results

- **Largest lossless recurrent networks**: neuron size 8 wins for p<0.02 (>12,000 neurons); size 12 for 0.02≤p≤0.08; size 16 for p≥0.08 (3,360–6,720 neurons). No single neuron size is optimal — search per (size, p).
- **Driver limit dominates**: once routing sources > 224 drivers, loss is unavoidable (visible as kinks in loss curves at network sizes 6,720 / 8,960 / 13,216).
- **Tolerating ≤1% loss** allows much larger networks than the strict lossless bound, especially for p≤0.2.
- **Theory vs MappingTool reality**: matches well for networks >20K neurons; for 6–16K the actual loss is much HIGHER than estimated — caused by sparsity of synapse-driver switches (1 of 8 present) making bus→driver assignment fail for whole routing sources. On-wafer routing loss is always much smaller than driver-limit loss.
- **Architecture insight**: full 6-bit in-synapse decoding (as in BrainScaleS-2) supports larger lossless networks and lower loss for p≤0.2, at silicon-area cost. The 2b/4b split is a flexibility-vs-area tradeoff; the method quantifies it.

## Reusable Patterns

- **Binomial-cascade resource estimation**: any hierarchical hardware where a random demand (binomial per unit) passes through levels with capacity c_k and grouping factor g can use the same F^N → max-distribution → convolution → expectation pipeline. Replace binomial with any discrete distribution (e.g., PyNN FixedNumberPre connectors).
- **Marginal-gain greedy allocation**: sorting ΔS gain curves descending and taking the top 4D items is optimal allocation of half rows to patterns — reusable for any shared-resource capacity problem.
- **Benchmark for mapping software**: the estimate is a lower bound on achievable loss; real mapping with per-source variation can beat the identical-gain assumption.
- **Design-space exploration**: use per-HICANN capacity models to compare address-decoding schemes before tape-out (2b/4b vs 6-bit, switch sparsity patterns).

## Limitations

- Ignores inter-HICANN wafer routing and vertical-bus→driver switch sparsity (the main source of theory-reality gap at mid sizes).
- Assumes homogeneous neuron size per HICANN, single synapse type per routing source, static synapses (no STP variants), identical gain distributions across sources.
- Uniform-random connectivity only; structured networks (L2/3 cortical models) need adapted capacity models.

## Related

- Petrovici et al. 2014 (loss compensation), Partzsch & Schüffny 2015 (hierarchical design formalism), Jeltsch 2014 (mapping algorithms), BrainScaleS-2 (6-bit decoding adopted), DarwinWafer (Zhu et al. 2025, wafer-scale mouse/zebrafish models).

**Activation**: neuromorphic, synapse loss, BrainScaleS, crossbar, wafer-scale, SNN mapping, hardware-software codesign, address decoding, routing resource, binomial estimate
