---
name: qlam-quantum-attention-memory
description: "QLAM: Quantum Long-Attention Memory methodology for long-sequence token modeling. Combines quantum linear algebra with attention mechanisms to overcome O(n²) scaling of transformer attention. Based on arXiv:2605.13833."
---

# QLAM: Quantum Long-Attention Memory for Long-Sequence Modeling

Quantum Long-Attention Memory (QLAM) methodology for efficient long-range dependency modeling using quantum computing primitives (arXiv:2605.13833).

## Core Problem

Transformers suffer from O(n²) complexity in attention for long sequences. State-space models (SSMs) provide alternatives but struggle with certain memory-intensive tasks. QLAM leverages quantum superposition and interference to encode long-range dependencies more efficiently.

## Key Innovation

### Quantum Attention via Block Encodings

QLAM encodes the attention matrix as a block-encoded quantum state:
- Token embeddings are mapped to quantum states via amplitude encoding
- Attention scores are computed via quantum inner products (swap test or Hadamard test)
- The resulting attention distribution is sampled via quantum measurement

### Memory Compression

- Long sequences are compressed into quantum states with O(log n) qubits
- Quantum Random Access Memory (QRAM) enables O(1) access to any token
- Temporal dependencies are encoded in entanglement patterns

## Mathematical Framework

### Block Encoded Attention

Given token embeddings x₁, ..., xₙ ∈ ℝᵈ:

1. **Amplitude Encoding**: |ψᵢ⟩ = Σⱼ xᵢⱼ/||xᵢ|| |j⟩
2. **Quantum Attention Score**: ⟨ψᵢ|ψⱼ⟩ computed via Hadamard test
3. **Softmax via Quantum Sampling**: e^{⟨ψᵢ|ψⱼ⟩}/Σₖ e^{⟨ψᵢ|ψₖ⟩}

### Complexity Analysis

- Classical attention: O(n²d)
- QLAM attention: O(log n · poly(d)) with QRAM
- Memory: O(n·d) classical → O(log n · d) quantum

## Implementation Patterns

### Pattern 1: Quantum-Enhanced Attention Layer

```python
from unitaria import BlockEncoding
import numpy as np

class QLAMAttention:
    """Quantum Long-Attention Memory layer."""
    
    def __init__(self, d_model, n_qubits):
        self.d_model = d_model
        self.n_qubits = n_qubits  # log(sequence_length)
    
    def forward(self, x):
        # Encode tokens as quantum states
        states = self.amplitude_encode(x)
        # Compute attention via quantum inner products
        attn_scores = self.quantum_inner_product(states)
        # Sample from quantum distribution
        output = self.quantum_sample(attn_scores, x)
        return output
```

### Pattern 2: Hybrid Classical-Quantum Memory

For NISQ-era deployment:
- Use classical attention for short-range (window < W)
- Use quantum attention for long-range dependencies
- Combine via weighted sum: attn = α·attn_classical + (1-α)·attn_quantum

## Activation Keywords

- qlam
- quantum attention
- quantum long-attention memory
- long sequence modeling quantum
- quantum transformer attention
- 量子注意力

## Usage Guidelines

### When to Use

1. **Very long sequences** (n > 10K tokens)
2. **Memory-intensive tasks** where classical SSMs fail
3. **Research/prototyping** on quantum-classical hybrid systems

### Prerequisites

- Understanding of block encodings (see `unitaria-quantum-linear-algebra`)
- Access to quantum simulator or hardware
- Linear algebra foundations (matrix operations, spectral theory)

### Limitations

- Requires QRAM for theoretical speedup (not yet practical)
- NISQ-era implementations need hybrid classical-quantum approach
- Quantum measurement introduces stochasticity

## Related Skills

- `unitaria-quantum-linear-algebra` - Block encoding foundation
- `quantum-neural-network-designer` - QNN architecture design
- `spiking-transformer-unification` - Alternative attention unification

## arXiv Reference

- arXiv: 2605.13833v1
- Title: "QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling"
- Published: 2026-05-13
- Categories: cs.LG, cs.CV
