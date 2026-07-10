---
name: coherence-law-noisy-equivariant-qnn-trainability
description: "Coherence law for trainability in noisy equivariant quantum neural networks. U(1)-equivariant QNNs with light-cone gradient confinement, sector coherence rate as Rayleigh quotient, and open-system training law. Use when designing symmetric QNNs for noisy hardware, analyzing gradient survival under decoherence, or building noise-resilient quantum neural architectures."
metadata:
  arxiv_id: "2606.30688"
  published: "2026-06-30"
  authors: "Hassan Ugail, Newton Howard"
  categories: "quant-ph, cs.AI, cs.LG, math-ph"
  tags: [quantum-neural-networks, equivariant, trainability, decoherence, coherence-law, noise-resilience]
---

# Coherence Law for Noisy Equivariant QNN Trainability

## Description

Methodology for predicting and ensuring trainability of symmetry-equivariant quantum neural networks under decoherence. Introduces sector coherence as the quantity linking equivariant architecture, open-system dynamics, and noisy trainability.

## Activation Keywords
- equivariant quantum neural network
- coherence law trainability
- noisy QNN gradient
- symmetry-protected QNN
- decoherence gradient survival
- light-cone gradient confinement
- sector coherence rate
- 对称量子神经网络训练性
- 噪声等效量子网络
- noise-resilient QNN

## Core Theory

### Light-Cone Gradient Confinement
For U(1)-equivariant brickwork circuits conserving a charge:
- Causality confines the gradient to the backward light cone of the readout
- Gradient lives within the active charge sector
- Lower bound on noiseless gradient is independent of total qubit count

### Sector Coherence Rate
Defined as a Rayleigh quotient of the noise generator along the gradient-carrying mode:
- Captures decay of off-diagonal sector modes that the projected readout observes
- Determines gradient survival rate under noise
- Outperforms standard channel diagnostics (worst-case dephasing rate, etc.)

### Open-System Training Law
Perturbative analysis yields a leading-order training law:
- Finite-noise degradation follows a single accumulated variable
- Built from noise depth × coherence contraction coefficient
- Achieved R² = 0.979 in density-matrix simulations

## Key Findings

### Correlated Dephasing Test
- Correlated dephasing channel has large worst-case rate but near-zero aligned rate
- Training law correctly predicts no gradient loss
- Demonstrates sector coherence > standard channel diagnostics

### Two-Effect Framework
1. **Causality effect**: Fixes WHERE the gradient can live (backward light cone)
2. **Coherence effect**: Determines HOW FAST it decays (contraction of off-diagonal modes)

## Usage Patterns

### Pattern 1: Designing Noise-Resilient Equivariant QNNs
When building QNNs with symmetry constraints:
1. Choose equivariant architecture (e.g., U(1)-equivariant brickwork)
2. Identify the conserved quantity (charge, particle number, etc.)
3. Compute the sector coherence rate as Rayleigh quotient of noise generator
4. Use training law to predict gradient survival under target noise model
5. Optimize circuit depth to stay within coherence threshold

### Pattern 2: Diagnosing QNN Trainability Failure
When a QNN stops training on noisy hardware:
1. Map the noise channel to its generator representation
2. Compute the aligned coherence rate for your readout
3. If rate ≈ 0: gradient is preserved (look for other training issues)
4. If rate >> 0: gradient decays exponentially with circuit depth
5. Consider correlated noise channels that may have better aligned rates

### Pattern 3: Selecting Optimal Noise Channel
When choosing between noise mitigation strategies:
1. Don't just minimize worst-case dephasing rate
2. Minimize the readout-visible aligned coherence rate
3. A channel with high worst-case but low aligned rate may be preferable
4. This enables "noise shaping" — steering noise into sector-invisible directions

## Methodology

### Computing the Aligned Coherence Rate

```python
import numpy as np
from scipy.linalg import eig

def aligned_coherence_rate(noise_generator, gradient_direction):
    """Compute the Rayleigh quotient of noise generator along gradient mode.
    
    Args:
        noise_generator: Lindbladian superoperator matrix
        gradient_direction: Vector in the active charge sector
        
    Returns:
        Aligned coherence rate (scalar)
    """
    # Rayleigh quotient: <ψ|L|ψ> / <ψ|ψ>
    numerator = gradient_direction.conj() @ (noise_generator @ gradient_direction)
    denominator = gradient_direction.conj() @ gradient_direction
    return np.real(numerator / denominator)
```

### Light-Cone Reduction

The noiseless gradient is pinned to the sector-restricted backward light cone:
- Identify readout operator O and its charge sector
- Trace causal paths backward from O through the circuit
- Only gates within this cone contribute to the gradient
- Reduces effective circuit size from N to O(√N) for 1D circuits

### Open-System Perturbative Analysis

1. Start with noiseless equivariant QNN: ρ → U(θ)ρU†(θ)
2. Add weak noise channel: ρ → (I - εL)U(θ)ρU†(θ)
3. Expand gradient to first order in ε
4. Leading-order degradation: ε × aligned_coherence_rate
5. Total degradation after D layers: ε × D × rate

## Pitfalls

### Pitfall 1: Wrong Noise Channel Diagnostic
Standard diagnostics (diamond norm, worst-case rate) don't predict QNN trainability. Use sector coherence rate instead.

### Pitfall 2: Ignoring Readout Projection
The readout operator projects into specific charge sectors. Only coherence within the observed sector matters.

### Pitfall 3: Assuming All Equivariant Architectures Behave the Same
The training law is derived for U(1)-equivariant brickwork circuits. Other symmetries (SU(2), SO(3)) may have different coherence structures.

### Pitfall 4: Extrapolating Beyond Weak Noise
The perturbative analysis assumes weak noise (ε << 1). Strong noise requires non-perturbative density-matrix simulations.

## Cross-References
- Related to `quantum-neural-barren-plateau` (Pattern 7: noise-induced trainability — coherence law is the complementary criterion)
- Related to `qml-expressivity-trainability` (QML expressivity analysis)
- Related to `noise-aware-quantum-testing` (noise-aware testing)
- Related to `qml-advantage-noisy-qubits` (quantum ML advantage under noise)
