---
name: quantispect-structure-aware-3d-cnn-predecoder

description: >
  Structure-aware lightweight 3D CNN pre-decoder for scalable surface code quantum error correction.
  Use when designing or benchmarking neural QEC decoders for surface codes, implementing spatio-temporal
  syndrome processing, replacing dense 3D convolutions with factorized branches, or co-designing
  lightweight pre-decoders with classical matching decoders. Trigger words: QuantiSpect, surface code
  neural decoder, 3D CNN QEC, FastHyperBlock, quantum error correction pre-decoder, spatio-temporal
  syndrome decoder, lightweight neural decoder.
---

# QuantiSpect: Structure-Aware Lightweight 3D CNN Pre-Decoder for Surface Codes

## Core Idea

Replace expensive dense 3D convolutions in a surface-code neural pre-decoder with **FastHyperBlocks** that factor the spatio-temporal syndrome volume into three lightweight, structure-aware branches. The resulting **QuantiSpect** model preserves (or improves) decoding accuracy while dramatically cutting parameters and MACs, and it pairs with a classical minimum-weight perfect matching (MWPM) decoder to handle residual errors.

## Problem

- Dense 3D CNNs for surface-code decoding scale poorly: parameter count and compute grow rapidly with receptive field.
- Prior art (e.g., the **Accurate** baseline) used stacked standard 3×3×3 convolutions to obtain large receptive fields, yielding ~1.80 M parameters.
- For real-time QEC and large code distances, a smaller, faster neural pre-decoder with the same accuracy is needed.

## Solution (arXiv:2607.18204, 2026-07-20)

### 1. Input/Output Tensor

| Tensor | Shape | Meaning |
|--------|-------|---------|
| Input | `(B, 4, T, D, D)` | Batch × 4 channels (residual syndromes: X-space, Z-space, X-time, Z-time) × syndrome rounds `T = d_m` × spatial lattice `D × D` |
| Output | `(B, 4, T, D, D)` | Per-voxel correction maps for space-like X/Z and time-like X/Z errors |

The data pipeline and residual-syndrome construction are inherited from the Accurate baseline; only the CNN architecture changes.

### 2. QuantiSpect Architecture

Three stages:

1. **Stem** — `Conv3D(4 → C, 3×3×3) → GroupNorm → GELU`
2. **Main body** — `N` identical FastHyperBlock residual blocks
3. **Head** — `GroupNorm → Conv3D → GELU → Conv3D`

Default hyperparameters:

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Input / output channels | — | 4 / 4 |
| Hidden dimension | `C` | 96 |
| Mid dimension | `C_mid` | 144 |
| Mixing groups | `G` | 6 |
| Number of blocks | `N` | 5 |
| Gate reduction ratio | `r` | 4 |
| Dropout probability | `p_drop` | 0.02 |
| Total parameters | — | ~0.663 M |
| Receptive field | `R` | 13 |

### 3. FastHyperBlock

Each block decomposes a full 3D convolution into three parallel, structure-aware branches, then fuses them with a channel gate and residual connection.

**Pre-expansion:**
- `GroupNorm → Conv3D 1×1×1 (C → C_mid) → GELU`
- Spatial/temporal operations run in the larger `C_mid` space; residual path stays at `C`.

**Three parallel branches:**

| Branch | Kernel | Role | Parameters |
|--------|--------|------|------------|
| Spatial | `(1, 3, 3)` depthwise | Local planar syndrome patterns | `C_mid × 9` |
| Temporal | `(3, 1, 1)` depthwise | Cross-round dynamics, measurement faults | `C_mid × 3` |
| Mixed | `(3, 3, 3)` grouped (`G` groups) | Joint spatio-temporal correlations | `C_mid × 27 / G` |

**Fusion:**
- Sum branch outputs → `Conv3D 1×1×1` projection
- **Squeeze-and-Excitation (SE)** channel gate: global pooling → FC(`C/r`) → FC(`C`) → sigmoid → channel-wise rescale
- `GroupNorm`
- Residual connection back to the `C`-dimensional input

**Receptive field:**

```
R = 1 + 2 + 2N   (kernel-3 stem + two voxels per FastHyperBlock)
```

With `N = 5`, `R = 13`. Each FastHyperBlock contributes about 128 k parameters.

## Key Results

### Accuracy vs Efficiency

- **QuantiSpect (R=13)** matches the **Accurate** baseline at the same receptive field.
- **~2.71× parameter reduction**: 0.663 M vs 1.80 M.
- **~2.84× MAC reduction** per voxel.

### Logical Error Rate Improvement

When QuantiSpect is used as a pre-decoder and residual errors are passed to PyMatching:

- Up to **~1.85× lower logical error rate** than uncorrelated PyMatching at code distance `d = 13`, physical error `p = 0.5%`.
- Up to **~3.11× faster PyMatching decode** at `d = 23` (smaller matching graph after pre-decoding).

### Scaled Variant: QuantiSpect-21

- `N = 10` blocks → receptive field `R = 21`.
- Only **1.18 M parameters**.
- Raises the circuit-level threshold to **~0.80%** under the evaluated noise model.

## When to Use

- Building a **lightweight neural pre-decoder** for surface or toric codes.
- Need to **scale receptive field** without dense 3D convolution cost.
- Want to **accelerate classical MWPM/union-find** by reducing the residual graph size.
- Co-designing **latency-constrained QEC decoders** for large code distances.
- Porting syndrome decoding to **edge/neuromorphic accelerators** where parameter count matters.

## Pitfalls

- FastHyperBlock assumes **spatial isotropy** of the syndrome lattice; may need adaptation for anisotropic or color-code geometries.
- The SE gate and grouped convolutions require channel counts divisible by `G` and `r`; choose `C` and `C_mid` accordingly.
- Performance is validated for surface-code residual syndromes; re-train and re-calibrate for other code families or noise models.
- A matching decoder is still required for the residual error graph; QuantiSpect is a **pre-decoder**, not a standalone decoder.

## Implementation Checklist

- [ ] Implement residual-syndrome extraction from syndrome history (4 channels: X-space, Z-space, X-time, Z-time).
- [ ] Build FastHyperBlock: pre-expansion, three depthwise/grouped branches, SE gate, GroupNorm, residual.
- [ ] Stack `N` blocks with stem/head; verify receptive field `R = 1 + 2 + 2N`.
- [ ] Train with cross-entropy on error-correction labels from simulated circuit-level noise.
- [ ] Evaluate logical error rate and compare against MWPM baseline.
- [ ] Benchmark inference latency and parameter count; iterate on `C`, `C_mid`, `G`, and `N`.

## Related Skills

- [[neural-decoder-quantum-error-correction]] — General neural decoder patterns for topological codes
- [[ml-quantum-error-correction]] — ML-assisted QEC including DiffQEC and RL control
- [[quantum-error-correction-methods]] — Broader QEC patterns and code families
- [[adaptive-syndrome-skipping-surface-gkp]] — Syndrome adaptive gain control for surface/GKP codes
- [[real-time-qec-system-stack]] — Real-time QEC system architecture and latency budgets

## Key Paper

- **"QuantiSpect: A Structure-Aware Lightweight 3D CNN Pre-Decoder for Scalable Surface Code Quantum Error Correction"**  
  Pan Gao, Xu-Sheng Xu, Ji-Ze Han, Jing-Wei Wen, Ling Qian, Xu-Dong Lv, Run-Qing Zhang, Xiao-Xiao Hu, Gui-Lu Long  
  arXiv:2607.18204 [quant-ph], 2026-07-20

## Session Notes

- Created from 2026-07-22 daily research cron job.
- Methodology extracted from the arXiv HTML version of the paper.
