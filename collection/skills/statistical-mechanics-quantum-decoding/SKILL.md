---
name: statistical-mechanics-quantum-decoding
description: "Statistical mechanics, tensor network, and AI approaches for maximum likelihood quantum error correction decoding. Use when analyzing or implementing QEC decoders, mapping quantum decoding to spin models, using tensor networks for syndrome decoding, or designing neural network decoders for quantum error correction. Covers the unified MLD framework bridging statistical physics, tensor contraction, and machine learning perspectives."
---

# Statistical Mechanics Quantum Decoding

## Core Concept

Maximum Likelihood Decoding (MLD) is the optimal strategy for quantum error correction, but is #P-hard in general. Three complementary approaches approximate or solve MLD:

1. **Statistical Mechanics**: Maps MLD to partition functions of disordered spin models
2. **Tensor Networks**: Approximate contraction on factor graphs yields near-MLD accuracy
3. **Artificial Intelligence**: Neural decoders (autoregressive, transformer) learn MLD distributions

## Statistical Mechanics Approach

### Spin Model Mapping

The QEC decoding problem maps to a disordered spin system:

- **Surface code** → Random-bond Ising model
- **Logical error probability** → Disorder-averaged partition function
- **Error threshold** → Phase transition temperature

### Key Steps

1. Map syndrome configuration to spin configuration
2. Construct Hamiltonian with disorder from syndrome
3. Evaluate partition function Z(β) at inverse temperature β
4. Identify logical operator with minimum free energy
5. Phase transition point = error threshold

### Threshold Estimation

Use Nishimori line: exp(-2βJ) = p/(1-p) where p is physical error rate. The intersection of paramagnetic and spin-glass phases gives the threshold.

## Tensor Network Approach

### Factor Graph Construction

1. Build factor graph from parity check matrix H
2. Assign tensors to variable nodes (qubits) and check nodes (stabilizers)
3. Contract tensor network to compute marginal probabilities

### Contraction Strategy

- **Small code distance**: Exact contraction (exponential in boundary)
- **Large code distance**: Approximate contraction (CTMRG, PEPS methods)
- **Complexity**: O(χ^d) where χ is bond dimension, d is code distance

## AI-Based Decoding

### Architecture Patterns

1. **Autoregressive models**: Generate error configurations conditioned on syndrome
2. **Recurrent transformers**: Process syndrome sequences for circuit-level noise
3. **Graph neural networks**: Encode code topology for flexible decoding

### Training Pipeline

1. Generate syndrome-error pairs via simulation
2. Train model to predict P(error | syndrome)
3. Decode by selecting most likely logical class

## Three-Approach Integration

| Approach | Accuracy | Complexity | Hardware |
|----------|----------|------------|----------|
| Statistical Mechanics | Exact (small codes) | Exponential | Classical |
| Tensor Networks | Near-MLD | Poly(χ, d) | Classical |
| AI/Neural | Data-dependent | Inference-time | GPU/TPU |

## Usage Patterns

### Pattern 1: Statistical Mechanics Decoder

When the code is small and exact threshold estimation is needed:

1. Construct spin Hamiltonian from stabilizer generators
2. Use Monte Carlo or transfer matrix to evaluate partition function
3. Extract logical error rate from free energy landscape

### Pattern 2: Tensor Network Decoder

When near-optimal accuracy is needed for moderate code distances:

1. Build tensor network from parity check matrix
2. Choose bond dimension based on available compute
3. Contract using optimized algorithms (e.g., boundary MPS)
4. Extract marginals for decision

### Pattern 3: Neural Network Decoder

When fast real-time decoding is needed:

1. Choose architecture (CNN for surface code, transformer for circuit-level)
2. Generate training dataset with realistic noise model
3. Train with cross-entropy or contrastive loss
4. Deploy with batching for throughput

## Error Handling

### MLD Intractability

For large codes, exact MLD is #P-hard. Fall back to:
- Tensor network approximation (accuracy vs speed tradeoff)
- Neural decoder (requires training data, fast inference)
- Belief propagation (suboptimal but very fast)

### Tensor Network Convergence

If tensor network contraction doesn't converge:
- Reduce bond dimension (sacrifices accuracy)
- Use simplified contraction order
- Switch to neural decoder

## Resources

- arXiv:2605.17230 - Maximum Likelihood Decoding of Quantum Error Correction Codes (review)
- Nishimori line analysis for threshold estimation
- Tensor network libraries: `quimb`, `cotengra`
- QEC simulation: `stim`, `pymatching`
