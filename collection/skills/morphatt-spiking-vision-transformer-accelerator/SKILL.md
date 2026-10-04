---
name: morphatt-spiking-vision-transformer-accelerator
description: ASIC for Spiking ViT MHSA via Q(KV) reordering + AND-popcount. Use for SViT hardware design.
category: ai_collection
trigger: spiking vision transformer accelerator, neuromorphic ASIC, spiking multi-head self-attention hardware, AND-popcount attention, edge AI low power, Spike-Driven Transformer v2 acceleration, multiplier-free attention engine, reparameterization convolution hardware
---

# MorphAtt: Neuromorphic ASIC Accelerator for Spiking Vision Transformer Attention

**Source**: Putra, Jafari Rad, Shafique — "MorphAtt: A Neuromorphic Accelerator for Efficient Multi-Head Attention Processing in Spiking Vision Transformers" (arXiv:2609.33207, NYU Abu Dhabi, Sep 2026; 32nm CMOS synthesis)

## Core Idea

A digital ASIC that runs Spiking Vision Transformer (SViT) inference — including multi-head self-attention (MHSA) AND reparameterization convolutions (RepConv, required by Spike-Driven Transformer v2 / SDTv2) — at **20.3–29.1 TOPS/W under 39–55 mW**, an order of magnitude below prior SViT accelerators (FPGA designs >4 W, ASIC designs >200 mW). Three innovations: (1) cascade architecture SpikeQKV → SpikeAtten → RepConv with dedicated inter-module buffers eliminating off-chip traffic; (2) **Q(KᵀV) operation reordering cutting attention complexity O(N²D) → O(ND²)** (~3× for N=196, D=64); (3) fully **multiplier-free attention** via bitwise AND + pop-count on binary spikes.

## Architecture (three cascaded modules + buffers)

1. **SpikeQKV** (spiking Q/K/V generator): three parallel pipelines.
   - *SpikeGen* converts real-valued tokens to spikes with LIF neurons; membrane update `U[t] = U[t-1] + x[t] − (U[t-1] − U_rst)/τ` with **τ=2 so 1/τ becomes a right-shift (≫1)** — no division unit. Threshold → spike into TempSpike buffer; History buffer keeps residual potential; shift-register alignment packs rows into H×D bit streams (T×N×(H×D)).
   - *RepConv* inside SpikeQKV computes local spatial dependencies over sparse spikes.
   - *Head Separator* isolates per-head N×D Q slices and transposes K/V on-the-fly for column-wise streaming into Single-Head buffers (SH_Q/SH_K/SH_V, T×(N×D) per head).
2. **SpikeAtten** (spiking MHSA engine) — only 209 µW (96% power reduction vs multiplier-based attention ≈5.2 mW @ 8-bit):
   - *SHSA (Single-Head Self-Attention)*: Step 1 — KᵀV via bitwise AND + pop-count (binary spikes, no multipliers); Step 2 — gated Query multiplication: accumulator adds a KᵀV row only when Query shift-register MSB=1 AND OR-reduction of the KᵀV row ≠ 0, else **dynamic bypass + sleep mode** (skip switching power); Step 3 — per-head attention outputs buffered (N×D each).
   - *Concat* unit time-multiplexes H heads into one N×(H×D) BuffAtten; post-attention SpikeGen re-converts accumulated real values back to spikes (LIF).
   - Per-op energy: AND+popcount ≈ **12 fJ vs ~500 fJ for a multiply** in 32nm.
3. **RepConv** (reparameterization conv pipeline, 8 stages: ReshapeIn, SpikeConv1D, BatchNorm | Padding, Conv2D, Conv1D, BatchNorm | ReshapeOut): FSM + parameterized S×S systolic array; Conv1D spike-conditional accumulation (idle PE on spike=0); Conv2D 3×3 output-stationary systolic with on-the-fly sliding-window extraction. Extra cost of RepConv support: only 1.267 mW (3.3%) + 42.6 kµm².

## Synthesis Results (32nm CMOS, 100 MHz, SDTv2 on CIFAR-100; H=8, N=196, D=64, T=4)

| Metric | Sequential mode | Pipeline mode |
|---|---|---|
| Throughput | 792.6 GOPS | 1605 GOPS |
| Power | 38.96 mW | 55.12 mW |
| Energy efficiency | 20.3 TOPS/W | 29.1 TOPS/W |
| Area | 1.5 mm² | 1.5 mm² |

Power breakdown: SpikeQKV 51.6% (20.1 mW), memories 44.6%, SpikeAtten 0.6%, RepConv 3.2%. Area: memories ~51%, compute ~49% — balanced by dataflow-driven buffer sizing. Worst-case numbers (125°C, HVT cells); expect 20–25 mW effective at 25–85°C. Timing slack: RepConv/SHSA can clock to 135 MHz → +35% throughput headroom.

## Comparison Anchors (Table 1 of paper)

- FPGA SViT accelerators (SpikeTA, FireFly-T, Li 2024): 300 GOPS–29 TOPS but >4 W → <1 TOPS/W.
- ASIC (VESTA, Bishop, Fang 2025, Xu 2024-3D): ≥4 TOPS, <1 W, up to 27.9 TOPS/W.
- MorphAtt: competitive throughput at 10–100× lower power → best TOPS/W in class for tightly-constrained edge vision.

## Reusable Design Patterns

- **O(N²D)→O(ND²) via right-to-left associativity** Q(KᵀV): generic trick for token-rich (N≫D) edge workloads — works in ANY attention accelerator, spiking or not; the spiking case additionally makes the inner product AND+popcount.
- **τ=2 → shift instead of divide** for LIF: choose membrane time constant as power of two to replace division with shifts.
- **Gated accumulation with sleep mode**: skip switching power when either operand row is inactive (spike sparsity → energy, not just FLOP, savings).
- **Cascaded modules with inter-module buffers** (QKV_Buffers, Data_Buffer) sized to dataflow to avoid off-chip DRAM round-trips; 49/51 compute/memory area balance as the design target.
- **Post-attention re-spiking**: accumulated real values must pass through an LIF SpikeGen before further spiking stages — precision boundary between attention (real accumulators) and spike domain (binary).

## When to Apply

- Designing low-power accelerators for SViTs (Spikformer, SDT/SDTv2, SpikingResformer) at the edge (mobile robots, always-on vision).
- Estimating energy budget: attention can be near-free (0.6% of power) once multiplier-free; LIF/spike generation and memory dominate — optimize SpikeGen first, not attention.
- Any binary-operand matmul (hashing, binary networks) benefits from the AND+popcount + gated-accumulate pattern.

## Limitations

- Synthesis-level evaluation only (RTL → Design Compiler), no silicon; toggle rates from SDTv2/CIFAR-100 simulation.
- Binary spikes only — no multi-bit spiking support (unlike SpikeTA's 10-bit path).
- Fixed head/tile sizing tuned to SDTv2 geometry; other SViT variants need re-tiling.
- Pipeline-mode power (55 mW) still worst-case-corner; temperature derating assumed, not measured.

## Related Skills

- `snn-streaming-qubit-readout` — SNN hardware at the physics boundary
- `spiker-ll-snn-accelerator`, `suprasnn-synapse-level-snn-accelerator` — FPGA SNN accelerators
- `quantized-snn-hardware-optimization` — behavior-aware quantization for SNN hardware
- `stochastic-computing-snn-accelerator` — ReSCom stochastic-computing SNN ASIC pattern
