---
name: quantum-hilbert-prototype-learning
category: quantum
description: Geometric prototype learning in quantum Hilbert space using Matrix Product States (MPS). Lifts prototype-based ML from classical feature space to quantum Hilbert space, enabling explainable classification and clustering via quantum state geometry.
version: "1.0"
tags: [quantum-machine-learning, matrix-product-states, prototype-learning, hilbert-space, explainable-ai]
source: "arxiv:2605.17895"
arxiv_id: "2605.17895"
date: "2026-05-22"
---

# Quantum Hilbert Prototype Learning

## Overview

This methodology introduces a prototype-based learning scheme where class representatives are encoded as generative **Matrix Product States (MPS)** in quantum Hilbert space. Classification and clustering are performed through geometric measures of quantum states, lifting prototype learning from classical feature space to the quantum domain.

## Core Innovation

### Quantum Prototype Encoding
- Class prototypes = generative MPS (tensor network states)
- Data samples and prototypes live in the **same Hilbert space**
- Enables geometric comparison via quantum state measures

### Geometric Classification
```
For input data x:
1. Encode x as quantum state |ψ_x⟩ in Hilbert space
2. Compare with each prototype |φ_c⟩ (MPS for class c)
3. Assign class: argmax_c |⟨φ_c|ψ_x⟩|²  (Born rule probability)
```

## Mathematical Framework

### Matrix Product States (MPS)
```
|φ⟩ = Σ_{i₁,...,iₙ} A¹[i₁] A²[i₂] ... Aⁿ[iₙ] |i₁...iₙ⟩
```
- Each class c has its own MPS with tensors {Aᶜ,ᵏ}
- Bond dimension χ controls expressivity vs efficiency
- MPS enables efficient representation of high-dimensional quantum states

### Geometric Measures
1. **Overlap (fidelity)**: |⟨φ|ψ⟩|² — probability of measuring prototype state
2. **Trace distance**: D(ρ, σ) = ½ Tr|ρ - σ|
3. **Bures distance**: D_B(ρ, σ) = √(2(1 - √F(ρ, σ)))
4. **Hilbert-Schmidt distance**: ||ρ - σ||_HS

### Quantum Probability
- Classification probability: P(c|x) = |⟨φ_c|ψ_x⟩|²
- Born rule as decision function
- Naturally normalized probabilities

## Algorithm

### Training Phase
```
Input: Labeled dataset {(x_i, y_i)}
Output: MPS prototypes {|φ_c⟩} for each class c

1. Initialize MPS prototypes (random or PCA-based)
2. For each epoch:
   a. Encode batch data as quantum states
   b. Compute overlaps with current prototypes
   c. Update MPS tensors to maximize correct classification
   d. Apply "attraction" effect: pull prototypes toward correct samples
3. Apply dimensionality reduction via prototype distances
```

### Inference Phase
```
Input: New sample x
Output: Predicted class ĉ

1. Encode x → |ψ_x⟩
2. Compute |⟨φ_c|ψ_x⟩|² for all classes c
3. Return argmax_c |⟨φ_c|ψ_x⟩|²
```

## Key Discovery: Attraction Effect

- Quantum-probabilistic prototypes exhibit natural **attraction** to data points
- This emerges from the geometry of Hilbert space
- Enables effective learning without explicit gradient-based optimization

## Dimensionality Reduction

- Based on **prototype distances** in Hilbert space
- Projects high-dimensional quantum states to lower-dimensional representations
- Preserves classification-relevant structure

## Benchmarks

- **Fashion-MNIST**: Outperforms classical prototype approaches
- **ECG dataset**: Competitive with black-box neural networks
- **Advantage**: Explainability — can inspect prototype states directly

## Applications

1. **Explainable quantum ML**: Prototype states are interpretable
2. **Small datasets**: MPS requires fewer parameters than full neural networks
3. **Clustering**: Natural extension — no labels needed
4. **Anomaly detection**: Low overlap with all prototypes → anomaly

## Implementation Patterns

### Pattern 1: MPS Classification
```python
# Pseudocode
def quantum_prototype_classify(data, prototypes):
    encoded = encode_to_quantum_state(data)
    probs = [abs(inner_product(encoded, proto))**2 for proto in prototypes]
    return argmax(probs)
```

### Pattern 2: Prototype Update
```python
# Attraction-based update
def update_prototype(proto, samples, lr):
    for sample in samples:
        proto += lr * (sample - proto) * overlap(proto, sample)
    proto = normalize(proto)
```

## Advantages over Classical Prototypes

| Aspect | Classical | Quantum Hilbert |
|--------|-----------|-----------------|
| Representation | Feature vectors | Quantum states (MPS) |
| Similarity | Euclidean/Cosine | Fidelity/Overlap |
| Explainability | Limited | High (inspect quantum state) |
| Expressivity | Linear | Non-linear (Hilbert space geometry) |

## Pitfalls

- **State preparation**: Encoding classical data to quantum states has overhead
- **Bond dimension**: Too small → underfitting; too large → computational cost
- **MPS limitation**: Not all quantum states are well-approximated by MPS
- **Classical simulation**: MPS simulation scales as O(nχ²) — needs quantum hardware for large systems

## References

- arXiv:2605.17895 - "Geometric Prototype Learning in Quantum Hilbert Space with MPS"
- Matrix Product States / Tensor Networks
- Quantum Machine Learning survey papers
