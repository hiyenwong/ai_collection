---
name: coset-based-qldpc-codes
description: "Coset-based quantum LDPC code construction methodology — generalizes two-block group algebra (2BGA) codes using group action on cosets of subgroups, expanding search space for new quantum LDPC codes. Use for quantum error correction code design, qLDPC code search, syndrome extraction scheduling."
metadata:
  arxiv_id: "2606.17268"
  published: "2026-06-15"
  authors: "Arda Aydin, Itzhak Tamo, Alexander Barg"
---

# Coset-based Quantum LDPC Codes

## Core Methodology

### Construction Framework
- **Group action on cosets**: Replaces regular group actions of 2BGA codes, significantly expanding search space
- Yields new qLDPC codes outside the 2BGA family with improved parameters
- **Discovered codes**: Weight-6 [[48,8,6]], [[96,8,10]], [[224,12,16]]; Weight-8 [[84,16,8]], [[112,16,10]], [[128,16,12]], [[168,16,15]]

### Syndrome Extraction
- Maximally packed schedule of depth w+2 (including initialization and measurement)
- Works for any code in the family with maximum stabilizer weight w
- Competitive with BB codes under circuit-level noise with BP-OSD decoding

### Performance
- Weight-6 family threshold: ≈0.65%
- Weight-8 family threshold: ≈0.35%

## Activation Keywords
- Coset qLDPC, group algebra codes
- Quantum LDPC construction, syndrome extraction
- Two-block codes, qLDPC code search
- 量子LDPC码，余集码构造

## Usage Patterns

### Pattern 1: Code Construction via Group Action on Cosets
When searching for new qLDPC codes: use group action on cosets of subgroups instead of regular group action to expand the code search space beyond 2BGA codes.

### Pattern 2: Syndrome Extraction Scheduling
For any qLDPC code with maximum stabilizer weight w: use the w+2 depth maximally packed syndrome extraction schedule including initialization and measurement steps.

### Pattern 3: Code Covering Sequences
Use the group-theoretic framework to generate sequences of graph-based covers of 2BGA codes — recovers and extends recent code construction results.

## Pitfalls
- Computer search required — no closed-form parameter prediction
- BP-OSD decoder performance may differ for non-sparse stabilizer weights
- Thresholds computed under standard circuit-level noise model — hardware-specific noise may differ
