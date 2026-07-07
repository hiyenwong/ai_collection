---
name: "quantum-limited-subdiffraction-telescopy"
description: "Quantum-limited subdiffraction telescopy using genuine multi-telescope interference. Proves pairwise measurements insufficient for higher-order image moment estimation at quantum limit. Constructs array-SPADE measurements attaining optimal QFI scaling up to finite-array cutoff. Applicable to quantum metrology, astronomical imaging, quantum network telescopy, and spatial-mode demultiplexing."
metadata:
  arxiv_id: "2606.27276"
  published: "2026-06-25"
  authors: "Yujie Zhang, Yunkai Wang, Wilson Wu, Thomas Jennewein"
  tags: [quantum, information-theory, telescopy, quantum-fisher-information, SPADE, multi-telescope, interferometry, imaging]
---

# Quantum-Limited Subdiffraction Telescopy via Multi-Telescope Interference

## Overview

Conventional stellar interferometry reconstructs incoherent sources from pairwise mutual coherences. For generic image-moment estimation, pairwise measurements are **not sufficient** for quantum-limited subdiffraction imaging.

## Core Theory

### Quantum Fisher Information Scaling

For an N-telescope array observing weak incoherent light from a generic extended source:

- **QFI scaling of image moments**: derived up to cutoff **2N-2**
- **Pairwise measurements** attain full-array QFI scaling only up to **second order**
- Higher-order moment estimation at the quantum limit requires **genuinely multi-telescope interference**

### Key Result

| Measurement Type | Max Order Attaining Full QFI |
|-----------------|------------------------------|
| Telescope pairs | 2nd order |
| Full N-array | 2N-2 |

The gap between pairwise and full-array capability grows with array size.

### array-SPADE Construction

Inspired by spatial-mode demultiplexing (SPADE) from single-aperture subdiffraction imaging:

1. Construct array-SPADE measurements
2. Attain optimal QFI scaling up to finite-array cutoff
3. Embeddable in ancilla- and memory-assisted quantum-network architectures for long-baseline telescopy

## Methodology

### When Pairwise Is Insufficient

1. Determine the order of image moment to estimate
2. If order > 2, pairwise coherence measurements lose QFI scaling
3. Design multi-telescope interference measurement

### array-SPADE Implementation Steps

1. Map each telescope's optical mode to the array-SPADE basis
2. Perform joint measurement across all N modes simultaneously
3. Extract image moments up to order 2N-2
4. Use ancilla-assisted protocols for long-baseline operation

## Pitfalls

- **Pairwise sufficiency misconception**: Many papers assume pairwise coherence measurements are sufficient for arbitrary resolution enhancement — this paper proves they are not for higher-order moments
- **Memory requirement**: Multi-telescope interference requires quantum memory/ancilla for long baselines where light arrives asynchronously
- **Finite cutoff**: QFI scaling has fundamental cutoff at 2N-2 for N telescopes — cannot estimate arbitrarily high-order moments regardless of measurement sophistication

## Related Papers

- SPADE (single-aperture spatial-mode demultiplexing)
- Quantum Fisher Information estimation under decoherence
- Multi-mode entangling-gate synthesis in trapped-ion systems (2606.27266)

## Activation

Keywords: quantum telescopy, subdiffraction imaging, quantum Fisher information, array-SPADE, multi-telescope interference, stellar interferometry, image-moment estimation, quantum-limited resolution, spatial-mode demultiplexing
