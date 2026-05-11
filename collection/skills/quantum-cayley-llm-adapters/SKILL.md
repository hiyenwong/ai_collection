---
name: quantum-cayley-llm-adapters
description: "Quantum-enhanced LLM methodology using Cayley-parameterized unitary adapters executed on real quantum hardware. Demonstrates 1.4% perplexity improvement on Llama 3.1 8B with only 6K quantum parameters on 156-qubit IBM QPU. Use when: implementing quantum LLM adapters, running quantum circuits for AI, Cayley parameterization, barren plateau mitigation, quantum-classical hybrid LLM, quantum hardware AI execution, unitary adapters, quantum utility path, SmolLM2 experiments, noise-expressivity phase transition."
---

# Quantum Cayley LLM Adapters

Quantum-enhanced LLM methodology via Cayley-parameterized unitary adapters. First demonstration of quantum circuit execution improving LLM performance on real 156-qubit hardware.

## Activation Keywords

- quantum cayley adapters
- quantum LLM enhancement
- Cayley unitary adapters
- quantum hardware LLM
- barren plateau mitigation
- quantum AI execution
- quantum utility path
- noise-expressivity transition
- quantum-classical hybrid LLM
- unitary adapter LLM

## Core Architecture

### Three-Stage Design

1. **Frozen LLM Base**: Pre-trained LLM (Llama 3.1 8B, SmolLM2) with frozen weights
2. **Cayley Unitary Adapters**: Inserted into projection layers, parameterized via Cayley transform
3. **Real QPU Execution**: IBM Quantum System Two (156 qubits) for end-to-end inference

### Cayley Parameterization

```
U = (I - A)(I + A)^(-1)
```

Where A is skew-Hermitian matrix. Guarantees unitarity without constraints, avoiding barren plateau problem inherent in naive quantum parameterizations.

## Key Findings

### Llama 3.1 8B Results
- **Perplexity improvement**: 1.4% with only 6,000 quantum parameters
- **Compression recovery**: 83% recovery of compression-induced degradation
- **Hardware**: Validated on 156-qubit IBM Quantum System Two

### SmolLM2 Systematic Study
- Monotonic perplexity improvement with unitary block dimension
- Correct answers to questions classical baselines fail
- Noise-expressivity phase transition identifies quantum utility path

### Technical Insights
- **No barren plateau**: Cayley parameterization avoids gradient vanishing
- **Efficient scaling**: 6K parameters for 8B model (~0.000075% overhead)
- **Hardware validated**: Real QPU execution, not simulation
- **Phase transition**: Sharp noise-expressivity boundary defines scalability path

## Implementation Pattern

### Adapter Placement

```python
# Insert Cayley adapters into frozen projection layers
def apply_cayley_adapter(projection_layer, quantum_circuit):
    # Freeze original weights
    for param in projection_layer.parameters():
        param.requires_grad = False
    
    # Insert Cayley unitary adapter
    cayley_params = skew_hermitian_matrix(qubit_count)
    unitary = cayley_transform(cayley_params)
    
    # Execute on QPU
    return quantum_execute(unitary, projection_layer)
```

### Circuit Design Principles
- Keep circuit depth below noise threshold
- Scale unitary block dimension systematically
- Monitor noise-expressivity phase transition
- Use Cayley transform to guarantee unitarity

## When to Use

- Implementing quantum-enhanced LLM inference
- Need to mitigate barren plateaus in quantum ML
- Running quantum circuits for AI on real hardware
- Hybrid quantum-classical model development
- Compressing large models with quantum adapters
- Testing quantum utility for practical AI tasks

## Limitations

- Requires access to quantum hardware (IBM QPU demonstrated)
- Current improvements modest (1.4% at small scale)
- Noise limits practical qubit counts
- Classical preprocessing required for adapter integration
- Only validated on specific model architectures

## Related Research

- Quantum-classical hybrid neural networks
- Barren plateau mitigation strategies
- Parameter-efficient LLM fine-tuning (LoRA, Adapters)
- Quantum machine learning expressivity
- Noisy intermediate-scale quantum (NISQ) algorithms

## References

- arXiv:2605.05914v1 - Quantum-enhanced Large Language Models on Quantum Hardware via Cayley Unitary Adapters
- Authors: Borja Aizpurua, Sukhbinder Singh, Augustine Kshetrimayum, Saeed S. Jahromi, Roman Orus
- Published: May 7, 2026
- Subjects: Quantum Physics (quant-ph), Artificial Intelligence (cs.AI), Machine Learning (cs.LG)
