---
name: density-matrix-propagation-qec-decoding
description: "Optimal decoding methodology for quantum error correction using density matrix propagation through circuit-level noise. Enables ML-decoding benchmarking with pruning techniques and rigorous bounds for repetition codes and cellular automaton codes. Activation: density matrix propagation, optimal decoding, ML decoding, QEC benchmarking, BP+OSD accuracy, circuit-level noise decoding, quantum decoder benchmark, syndrome history propagation, pruning bounds, logical error rate, repetition code decoding, cellular automaton code"
metadata:
  arxiv_id: "2606.14455"
  published: "2026-06-12"
  authors: "Anthony Benois, Pierre Cussenot, Grégoire Misguich, Nicolas Sangouard, Kiara Hansenne"
  tags: [quantum, error-correction, decoding, density-matrix, circuit-noise, ML-decoding]
---

# Density Matrix Propagation QEC Decoding

## Description

Optimal (maximum-likelihood) decoding benchmark for quantum error correction under circuit-level noise. Propagates density matrix through full memory experiments and computes optimal decoding decisions for each syndrome history, with pruning techniques that have rigorous bounds.

## Activation Keywords
- density matrix propagation
- optimal decoding QEC
- ML decoding benchmark
- circuit-level noise decoding
- BP+OSD accuracy
- quantum decoder benchmark
- syndrome history propagation
- pruning bounds QEC
- logical error rate benchmark
- repetition code optimal decoding
- cellular automaton code decoding
- 最优解码 密度矩阵
- 量子纠错解码

## Core Methodology

### Problem
Circuit-level noise introduces temporal correlations and degeneracy, making optimal ML decoding computationally intractable. Practical decoders (MWPM, BP+OSD, Tesseract, Planar) use heuristics, making it hard to quantify suboptimality.

### Solution: Density Matrix Propagation

1. **Full density matrix propagation**: Propagate density matrix through entire memory experiment
2. **Optimal decision per syndrome**: Compute ML decoding decision for each syndrome history
3. **Pruning with bounds**: Introduce pruning techniques with rigorous bounds to access larger numbers of syndrome-extraction rounds

### Key Findings

| Decoder | Repetition Code | Cellular Automaton Code |
|---------|----------------|------------------------|
| MWPM | Near optimal | Significant deviation |
| BP+OSD | Near optimal | Deteriorates at experimental noise |
| Tesseract | Near optimal | Significant deviation |
| Planar | Near optimal | Significant deviation |

### Pruning Insight
At low physical error rates, only a narrow fraction of syndrome histories contributes significantly to the logical error rate.

## Usage Patterns

### Pattern 1: Benchmark QEC Decoders
When evaluating a QEC decoder's performance under circuit-level noise:
1. Implement density matrix propagation for small code instances
2. Compute optimal ML decisions for all syndrome histories
3. Compare practical decoder outputs against optimal baseline
4. Use pruning to extend to larger syndrome-extraction rounds

### Pattern 2: Assess Decoder Suboptimality
To quantify how far a practical decoder is from optimal:
1. Run optimal decoding benchmark on representative noise regimes
2. Compare logical error rates: P_decoder / P_optimal
3. Identify noise regimes where deviation becomes significant

### Pattern 3: Pruning for Scalability
When optimal decoding is needed for larger codes:
1. Apply pruning techniques with rigorous bounds
2. Focus computational effort on high-contribution syndrome histories
3. Verify bound satisfaction at target accuracy

## Instructions for Agents

### Step 1: Identify Code and Noise Model
- Target code (repetition, surface, cellular automaton, etc.)
- Circuit-level noise parameters (gate errors, measurement errors, idling errors)
- Number of syndrome-extraction rounds

### Step 2: Set Up Density Matrix Propagation
- Initialize density matrix for code state
- Apply circuit operations with noise channels
- Track syndrome extraction outcomes
- Propagate through full memory experiment depth

### Step 3: Compute Optimal Decoding
- For each syndrome history, compute posterior probability distribution
- Select ML decoding decision (most likely logical state)
- Track logical error rate across experiments

### Step 4: Apply Pruning (for scalability)
- Identify low-contribution syndrome histories
- Apply pruning threshold with rigorous error bounds
- Verify pruning doesn't compromise accuracy target

### Step 5: Compare Practical Decoders
- Run MWPM, BP+OSD, Tesseract, Planar decoders on same data
- Compare logical error rates vs optimal baseline
- Report degradation factors per noise regime

## Error Handling
### Computational Intractability
If density matrix propagation exceeds memory/compute:
- Use pruning to reduce state space
- Focus on small code instances for benchmarking
- Apply tensor network compression if applicable

### Bound Violation
If pruning bounds are not satisfied:
- Lower pruning threshold
- Verify numerical precision
- Use exact computation for critical syndrome histories

## References
- arXiv: 2606.14455v1
- Decoders benchmarked: MWPM, BP+OSD, Tesseract, Planar
- Codes tested: repetition code, cellular automaton code
