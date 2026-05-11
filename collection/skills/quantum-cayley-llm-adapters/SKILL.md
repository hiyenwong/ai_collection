---
name: quantum-cayley-llm-adapters
description: "Cayley-parameterized unitary adapters for quantum-enhanced LLM fine-tuning. Insert quantum circuit blocks into frozen LLM projection layers to improve perplexity with minimal parameters. Use when: quantum-enhanced LLM, quantum adapters for LLM, Cayley unitary adapter, quantum LLM fine-tuning, parameter-efficient quantum LLM, QPU inference for LLM."
---

# Quantum Cayley LLM Adapters

## Description

Insert Cayley-parameterized unitary quantum circuit adapters into frozen LLM projection layers (e.g., MLP up_proj/down_proj, attention o_proj) to achieve parameter-efficient quantum enhancement. Demonstrated 1.4% perplexity improvement on Llama 3.1 8B with only 6,000 quantum parameters on real 156-qubit IBM hardware.

## Activation Keywords

- quantum-enhanced LLM
- quantum adapters for LLM
- Cayley unitary adapter
- quantum LLM fine-tuning
- parameter-efficient quantum LLM
- QPU inference for LLM
- quantum adapter layers
- quantum MLP adapter

## Core Methodology

### Cayley Parameterization

Use Cayley transform to parameterize unitary matrices without exponential overhead:

```
U = (I - A)(I + A)^{-1}
```

where A is a skew-Hermitian matrix (A† = -A). This ensures unitarity by construction and avoids the barren plateau problem common in VQCs.

### Adapter Architecture

1. **Location**: Insert into frozen pre-trained LLM projection layers (MLP or attention)
2. **Structure**: Replace classical linear projection `W @ x` with `U @ x` where U is a quantum circuit
3. **Freeze strategy**: Keep all original LLM weights frozen; only train quantum adapter parameters
4. **Parameter count**: O(n²) classical vs O(log n) quantum for n-dimensional projection

### Implementation Pattern

```python
# Pseudocode for Cayley adapter in LLM projection layer
class CayleyQuantumAdapter:
    def __init__(self, dim, n_qubits):
        # Map dim-dimensional input to n_qubit quantum state
        self.n_qubits = n_qubits
        self.dim = dim
        # Cayley-parameterized unitary circuit
        self.skew_params = nn.Parameter(torch.zeros(n_params))
    
    def forward(self, x):
        # 1. Encode classical input into quantum state (amplitude/angle encoding)
        q_state = self.encode(x)
        # 2. Apply Cayley-parameterized unitary
        q_out = self.cayley_unitary(q_state, self.skew_params)
        # 3. Measure and decode back to classical
        return self.measure(q_out)
```

### Key Findings from arXiv:2605.05914

1. **Monotonic scaling**: Perplexity improves monotonically with unitary block dimension
2. **Compression recovery**: Recovers 83% of compression-induced degradation
3. **Noise-expressivity phase transition**: Sharp boundary identifies qubit count needed for quantum utility
4. **Real hardware validated**: End-to-end inference on 156-qubit IBM System Two (not simulation)
5. **Parameter efficiency**: 6,000 quantum params vs 8B classical params (0.000075% overhead)

### Design Principles

- Use angle encoding for text embeddings into quantum states
- Cayley transform avoids barren plateaus better than standard VQC parameterization
- Start with small adapter blocks (8-16 qubits) and scale monotonically
- Monitor noise-expressivity phase transition to determine viable qubit scale
- Freeze all classical LLM weights; only optimize quantum adapter

## Error Handling

- **QPU timeout**: Fall back to simulator for debugging, then validate on real hardware
- **Barren plateau**: If training stalls, reduce circuit depth or increase Cayley regularization
- **Noise degradation**: Use error mitigation (ZNE, PEC) if device noise exceeds expressivity threshold

## Resources

- arXiv: https://arxiv.org/abs/2605.05914v1
- IBM Quantum System Two (156-qubit superconducting processor)
- Llama 3.1 8B as primary target model
