---
name: divide-et-impera-modular-qnn
description: "Use when training QNNs under qubit limits. Split circuit into sub-VQCs plus stitching MLP."
category: ai_collection
---

# Divide et Impera Quantum Neural Networks for Modular Hybrid Architectures

**Paper**: Divide et Impera quantum neural networks for modular hybrid computing architectures (arXiv: 2610.09623, Casciaro, Amendola, Mascherpa, Caruso — Univ. Florence, 2026-10-07)
**Category**: Quantum (quant-ph) × Systems Engineering (modular architectures) — Thursday crossover

## Activation

- quantum neural network, QNN training, qubit limit, register reduction
- divide and conquer, modular quantum, distributed quantum computing
- hybrid quantum-classical, VQC ensemble, circuit splitting

## Problem

NISQ devices are noisy and qubit-limited; deep/wide QNN circuits are infeasible. Need QML models with reduced quantum register + fewer gates **without restricting the executable circuit class or degrading performance**.

## Method

**Divide-et-impera training**: decompose a Q-qubit circuit into k sub-circuits of size q_i < Q, each an independent VQC processing a feature subset:

```
z = ⊙_j VQC_j(x_{I_j}; θ_j)        # concatenate quantum embeddings
ŷ = MLP(z; θ_pred)                  # shallow classical stitching layer
```

- **Same parameter count when sub-circuits share a regular ansatz and index sets partition features** — parameters are redistributed, not added
- Each sub-circuit: angle encoding + 2-angle variational rotations + nearest-neighbor CNOT entanglement chain; data re-uploading scheme
- When features can't be hand-partitioned: apply **PCA** to get independent features (Φ = FX), then **sliding-window selection** over PCA components ordered by explained variance
- Computation distributes across multiple QPU calls → cheaper, less noise accumulation per circuit, suitable for modular quantum architectures interconnected via high-speed links

## Results (real-world tasks: EV charging station status + global air quality index)

- Base hybrid model **outperforms both classical implementations with fewer parameters**
- Isolating temporal information in distinct circuits + delegating interpretation to the classical part beats processing it in one quantum circuit (sequence-sensitive and unified-state variants lose)
- Noise robustness: noiseless score 53.86 → depolarizing channel 60.8, bit-flip 68 (contained degradation; two-qubit gate error dominates and defines the error cut-off region)
- Feature separation brings consistent improvements **even when initial decomposability assumptions are not met** (air quality case)

## Reusable Patterns

### Pattern 1 — Embedding-then-stitch decomposition
Replace one wide VQC with k narrow VQCs whose outputs are concatenated and passed to a shallow classical MLP. The quantum layer learns local representations; the classical layer handles global interaction. Parameter-neutral when ansätze are regular and partitions don't overlap.

### Pattern 2 — PCA + sliding-window auto-partitioning
When no semantic feature grouping exists: PCA → independent components ordered by explained variance → sliding windows as candidate subsets I_j. Generalizes the split to arbitrary tabular problems.

### Pattern 3 — Temporal features in separate circuits
Keep time-derived features in their own VQC(s) rather than merging into the state circuit; let the classical stitching layer interpret them. More resilient representation than single-circuit processing.

### Pattern 4 — Two-qubit-gate error budget
Noise-response heatmaps show 2-qubit gate error rates dominate the degradation boundary. When designing modular circuits, budget entangling gates first — they set the viable error-rate region (benchmarked against IBM_KYIV error rates).

## Related

- [[split-ensemble-qrc-training]] — split-ensemble for quantum reservoirs
- [[coupling-aware-subqubo-selection]] — splitting large QUBOs into sub-problems
- [[modular-hiqs-quantum-control]] — distributed control architecture
