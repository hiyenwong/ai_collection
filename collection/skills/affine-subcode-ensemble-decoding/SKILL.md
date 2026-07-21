---
name: affine-subcode-ensemble-decoding
description: "Affine Subcode Ensemble Decoding methodology for degeneracy-aware quantum error correction. Improves belief-propagation (BP) decoding of quantum LDPC codes by leveraging affine subcode structure to handle degeneracy. Use when: quantum error correction, QLDPC decoding, belief propagation, degeneracy, ensemble decoding, quantum LDPC codes, fault-tolerant quantum computing, syndrome decoding, CSS codes."
---

# Affine Subcode Ensemble Decoding for Degeneracy-Aware QEC

Quantum low-density parity-check (QLDPC) codes are promising for low-overhead fault-tolerant quantum computing, but **degeneracy** impairs convergence of standard belief-propagation (BP) decoding. This methodology uses **affine subcode ensemble decoding** to improve BP performance.

## Core Problem

Standard BP decoding for QLDPC codes fails because:
- Multiple error patterns produce the same syndrome (degeneracy)
- BP treats all patterns as equally likely, ignoring redundancy
- Causes convergence failure even for correctable errors

## Methodology

### Step 1: Identify Affine Subcodes

For syndrome `s`, decompose the code:
```
C_s = {e | H*e = s} = e_0 + C_0
```
where `e_0` is a particular solution and `C_0` is the kernel (code space).

### Step 2: Ensemble Decoding

1. Generate multiple affine subcode representatives
2. Run BP on each representative independently
3. Aggregate results across the ensemble
4. Select the most probable correction

### Step 3: Degeneracy-Aware Message Passing

Modify BP update rules:
```
m_{i->j} = f(messages) * degeneracy_weight
```
where `degeneracy_weight` penalizes messages ignoring equivalent error patterns.

## Implementation Pattern

```python
import numpy as np
from scipy.sparse import csr_matrix

class AffineSubcodeDecoder:
    def __init__(self, H, max_iter=50, ensemble_size=10):
        self.H = H
        self.max_iter = max_iter
        self.ensemble_size = ensemble_size
    
    def find_particular_solution(self, syndrome):
        """Find one solution e_0 such that H*e_0 = syndrome (GF(2))."""
        # Gaussian elimination over GF(2)
        pass
    
    def generate_affine_subcodes(self, syndrome, n_samples):
        """Generate multiple affine subcode representatives."""
        e_0 = self.find_particular_solution(syndrome)
        subcodes = [e_0]
        for _ in range(n_samples - 1):
            c_0 = self._sample_code_space()
            subcodes.append(e_0 ^ c_0)
        return subcodes
    
    def decode(self, syndrome, channel_probs):
        """Ensemble decoding with degeneracy awareness."""
        subcodes = self.generate_affine_subcodes(syndrome, self.ensemble_size)
        results = []
        for subcode in subcodes:
            result = self._bp_decode(subcode, channel_probs)
            results.append(result)
        return self._aggregate_results(results)
    
    def _bp_decode(self, initial_guess, channel_probs):
        """Standard BP with degeneracy-modified update rules."""
        pass
```

## Key Advantages

1. **Handles degeneracy explicitly** - unlike standard BP
2. **Ensemble approach** - robust across error configurations
3. **Compatible with existing QLDPC codes** - CSS, hypergraph, BB codes
4. **Parallelizable** - each ensemble member decodes independently

## Applications

- Surface code decoding
- Hypergraph product codes
- Bivariate bicycle (BB) codes
- Any QLDPC code where degeneracy impairs BP convergence

## Verification

Test decoder with known syndrome-error pairs:
1. Generate random errors below code threshold
2. Compute syndrome: `s = H*e`
3. Run decoder: `e_hat = decode(s)`
4. Check: `H*(e XOR e_hat) = 0` (logical equivalence)

## References

- arXiv: 2605.06547v1 (2026)
- Belief propagation for quantum error correction
- QLDPC code constructions (Panteleev & Kalachev)
