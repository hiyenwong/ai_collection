---
name: sparse-mamba-quantum-decoder
description: "Sparse Mamba decoder architecture for quantum error correction on surface codes. Uses Mamba state-space models for efficient defect-centric syndrome decoding. Use when: quantum error correction, surface code decoding, neural decoders, QEC syndrome processing, Mamba models for quantum, defect-centric decoding, quantum machine learning."
---

# Sparse Mamba Quantum Decoder

## Overview

Sparse Mamba decoder (arXiv:2605.17156) applies Mamba state-space models for efficient quantum error correction (QEC) syndrome decoding on surface codes. The key innovation is defect-centric processing that sparsely focuses computation on error syndromes rather than full lattice processing.

## Key Principles

### Defect-Centric Processing
- Only process syndrome locations with detected defects
- Skip empty regions of the syndrome lattice
- Reduces computational complexity from O(L^2) to O(d) where d = defect count

### Mamba State-Space Architecture
- Replaces attention with selective state-space models (SSMs)
- Captures long-range syndrome correlations with linear complexity
- Maintains temporal coherence across QEC rounds

### Surface Code Integration
- Maps surface code stabilizer measurements to syndrome sequences
- Handles both X and Z stabilizer channels
- Outputs Pauli frame corrections

## Implementation Workflow

### Step 1: Syndrome Extraction
```python
def extract_syndrome(stabilizer_measurements):
    """Convert stabilizer measurements to syndrome bits."""
    syndromes = []
    for i in range(1, len(stabilizer_measurements)):
        current = stabilizer_measurements[i]
        previous = stabilizer_measurements[i-1]
        syndrome = current ^ previous  # XOR for change detection
        syndromes.append(syndrome)
    return syndromes
```

### Step 2: Defect Detection
```python
def find_defects(syndromes, threshold=0.5):
    """Identify defect locations from syndrome data."""
    defects = []
    for t, syn in enumerate(syndromes):
        for loc, val in enumerate(syn):
            if val > threshold:
                defects.append((t, loc))
    return defects
```

### Step 3: Sparse Mamba Processing
```python
import torch
from mamba_ssm import Mamba

class SparseMambaDecoder(torch.nn.Module):
    def __init__(self, d_model=128, d_state=16):
        super().__init__()
        self.embedding = torch.nn.Linear(2, d_model)  # (time, location)
        self.mamba = Mamba(d_model=d_model, d_state=d_state)
        self.decoder = torch.nn.Linear(d_model, 3)  # X, Y, Z correction
    
    def forward(self, defects):
        # Embed defect locations
        x = self.embedding(torch.tensor(defects, dtype=torch.float32))
        # Process through Mamba SSM
        x = self.mamba(x)
        # Decode to Pauli corrections
        corrections = self.decoder(x.mean(dim=1))
        return corrections
```

### Step 4: Correction Application
```python
def apply_correction(corrections, current_state):
    """Apply Pauli frame corrections to quantum state."""
    for loc, correction in enumerate(corrections):
        pauli_type = torch.argmax(correction).item()
        if pauli_type == 0:  # X correction
            current_state.apply_x(loc)
        elif pauli_type == 1:  # Y correction
            current_state.apply_y(loc)
        elif pauli_type == 2:  # Z correction
            current_state.apply_z(loc)
    return current_state
```

## Performance Characteristics

- **Time Complexity**: O(d * L) where d = defects, L = code distance
- **Memory**: O(d) for sparse defect representation
- **Accuracy**: Comparable to MWPM decoder, better than belief propagation at high error rates
- **Latency**: Sub-microsecond decoding for d=13 surface code

## Error Handling

### High Defect Density
- If defect density exceeds ~10%, fall back to full-lattice processing
- Consider switching to larger code distance

### Decoder Failure
- Implement confidence scoring on decoder outputs
- Use multiple decoder rounds for critical corrections
- Maintain syndrome history for post-hoc analysis

## Related Work
- Minimum Weight Perfect Matching (MWPM) decoder
- Union-Find decoder
- Neural belief propagation decoders
- Transformer-based QEC decoders

## References
- Paper: arXiv:2605.17156 - Sparse Mamba Decoder for QEC
- Mamba: arXiv:2312.00752 - Mamba State Space Models
- Surface Codes: Fowler et al. (2012)
