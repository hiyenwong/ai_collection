---
name: scalable-quaternary-mp-qec-decoding
description: >
  Scalable quaternary message-passing decoding for Quantum Error Correction (QEC).
  Use when: (1) designing QEC decoders for surface codes, (2) implementing Belief
  Propagation for quantum codes, (3) analyzing MP decoder scalability, (4) studying
  dilution methods for quantum decoding. Covers quaternary Min-Sum decoder, graph
  dilution, and finite-length threshold analysis. Trigger: quantum error correction
  decoding, message passing QEC, belief propagation decoder, 量子纠错解码.
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.24177"
  published: "2026-05-26"
  authors: "Boqing Zhang, Henry D. Pfister, Hanwen Yao, Siyuan Niu"
  tags: [quantum, error-correction, message-passing, belief-propagation, dilution, surface-code, decoding]
---

# Scalable Quaternary Message-Passing Decoding for QEC

## Core Innovation

The **dilution method** enables quaternary Min-Sum (MS) decoders to exhibit an
apparent depolarizing threshold of 16% up to distance 20, outperforming Minimum-Weight
Perfect Matching (MWPM) in finite-length regimes.

## Key Results

### Dilution Method
- Quaternary MS decoder under dilution: 16% apparent depolarizing threshold (d ≤ 20)
- For X-noise: worst-case complexity O(N log² d)
- Outperforms BP-OSD at d = 65
- Observed ~9% threshold may correspond to true asymptotic threshold

### Why Dilution Works
- Graph-dilution argument: reduces short cycles that cause MP divergence
- MP algorithms genuinely scale when dilution breaks problematic graph topology
- Provides interpretability bridge between theory and practice

### Complexity Advantage
| Decoder | Complexity | Threshold |
|---------|-----------|-----------|
| MS + dilution | O(N log² d) | ~9-16% |
| BP-OSD | O(N²) | ~10% |
| MWPM | O(N³) | ~11% |

## Application Pattern

### When to Use
- Designing scalable QEC decoders for large surface codes
- Implementing belief propagation for quantum LDPC codes
- Analyzing when MP decoding can scale to large distances
- Comparing decoder performance across code distances

### Dilution Implementation Pattern

```python
def dilute_syndrome_graph(syndrome, check_matrix, dilution_factor=0.5):
    """Apply graph dilution to improve MP decoder convergence."""
    # Randomly remove edges from factor graph
    # Preserves long-range correlations while breaking short cycles
    diluted_checks = []
    for i, check in enumerate(check_matrix):
        if np.random.random() > dilution_factor:
            diluted_checks.append(check)
    return np.array(diluted_checks)

def quaternary_min_sum(syndrome, check_matrix, max_iter=50):
    """Quaternary Min-Sum decoder with dilution."""
    # Initialize messages
    # Iterative message passing on diluted graph
    # Apply min-sum update rule for quaternary alphabet
    pass  # See references for full implementation
```

## Activation Keywords
- quantum error correction decoding
- message passing QEC
- belief propagation decoder
- quaternary min-sum decoder
- dilution method QEC
- 量子纠错解码
- 消息传递解码
