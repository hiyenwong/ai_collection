---
name: bf-osd-qldpc-decoding
description: "Best-First Ordered Statistics Decoding (BF-OSD) methodology for quantum LDPC codes. Explores error-candidate space by traversing in order of decreasing likelihood rather than brute-force enumeration. Invokes OSD after fixed BP iterations instead of waiting for BP convergence. Achieves same performance as BP+OSD with 1/100th query budget under circuit-level noise. Use when: quantum error correction decoding, QLDPC code design, belief propagation post-processing, OSD optimization, list decoding for quantum codes, circuit-level noise regime, syndrome-based decoding."
metadata:
  arxiv_id: "2605.25777"
  published: "2026-05-25"
  authors: "Michele Banfi, Marco Ferrari, Antonino Favano, Alberto Tarable, Luca Barletta"
  tags: [quantum, error-correction, statistics, decoding, qldpc, osd, belief-propagation]
---

# BF-OSD QLDPC Decoding

## Core Methodology

Best-First OSD (BF-OSD) improves quantum LDPC code decoding by replacing brute-force candidate enumeration with likelihood-ordered traversal.

### Key Innovation: Best-First Search

Traditional OSD enumerates a pre-selected subset of error candidates. BF-OSD:
1. Traverses the error-candidate space in order of decreasing likelihood
2. Returns the most probable syndrome-consistent candidate found
3. Explores 1/100th of the query budget for equivalent performance

### BP+OSD Pipeline Modification

Conventional pipeline: Run BP until convergence → invoke OSD if needed.
BF-OSD pipeline: Run BP for fixed small iterations → always invoke OSD.

**Rationale**: Under circuit-level noise, BP is particularly unreliable. Waiting for convergence wastes cycles. Fixed-iteration BP + BF-OSD is more efficient.

## Algorithm Steps

1. **BP Phase**: Run belief propagation for fixed N iterations (typically N=5-10)
2. **OSD Initialization**: Extract most probable error pattern from BP output
3. **Best-First Traversal**: Build priority queue of error candidates ordered by likelihood
4. **Candidate Expansion**: Pop highest-likelihood candidate, check syndrome consistency
5. **Termination**: Return first syndrome-consistent candidate (or after budget exhaustion)

## When to Use

- **QLDPC code decoding**: Primary use case for any quantum LDPC code
- **Circuit-level noise**: Especially effective when BP alone fails under realistic noise
- **Bivariate Bicycle codes**: Validated on BB codes with Monte Carlo simulations
- **Any BP+OSD pipeline**: Direct drop-in replacement for conventional OSD

## Performance Characteristics

- **Query budget**: 1/100th of conventional BP+OSD for same performance
- **Complexity**: O(k log k) where k = number of candidates explored
- **Memory**: Priority queue overhead vs. fixed list in conventional OSD

## Error Handling

- **BF-OSD exhausts budget**: Fall back to conventional OSD with expanded list
- **BP fails to produce initial candidate**: Initialize OSD from minimum-weight error
- **Degenerate codes**: Leverage degeneracy to accept multiple equivalent solutions
