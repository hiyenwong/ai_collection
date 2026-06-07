---
name: quantum-block-encoding-difference-of-gaussian
description: "Quantum block encoding methodology for Difference-of-Gaussian (DoG) operators on periodic grids. Implements Linear Combination of Unitaries (LCU) framework without black-box oracles. Activation: quantum block encoding, DoG operator, quantum machine learning, quantum signal processing."
---

# Quantum Block Encoding of Difference-of-Gaussian Operators

Methodology for constructing explicit quantum block encodings of Difference-of-Gaussian (DoG) operators on periodic grids using Linear Combination of Unitaries (LCU) framework.

## Overview

The DoG operator is widely used in:
- Image processing (feature and edge detection)
- Quantum machine learning
- Finite-difference methods (Laplacian-of-Gaussian approximations)

This skill implements an explicit block encoding that achieves constant subnormalization factor λ=2, independent of grid size N, spatial dimension D, and stencil width.

## Core Technique

### DoG Decomposition
The DoG admits natural decomposition to two normalized Gaussian distributions:

```
DoG = Gaussian(σ₁) - Gaussian(σ₂)
```

Each Gaussian is preparable by explicit efficient circuits, with negation encoded using a single Pauli-Z gate on a branch-indicator qubit.

### LCU Framework Mapping
The block encoding maps directly to Linear Combination of Unitaries without requiring:
- Signed amplitude loading
- Quantum random-access memory
- Black-box oracles

### Key Properties

| Property | Value | Independence |
|----------|-------|--------------|
| Subnormalization λ | 2 | Grid size N, dimension D, stencil width |
| Success probability | Exact closed-form via power spectrum | Input signal dependent |
| Scaling | O(h⁴) | Grid spacing h (fine grid limit) |

## Activation Keywords

- quantum block encoding
- DoG operator
- difference-of-gaussian quantum
- quantum signal processing
- LCU framework
- quantum machine learning encoding

## Tools Used

- exec: Run quantum circuit simulations
- write: Generate circuit descriptions
- read: Load operator specifications

## Implementation

### Circuit Structure

```
[Gaussian Prep 1] ──┐
                    ├── [Controlled-SWAP] ── [Pauli-Z branch] ── Output
[Gaussian Prep 2] ──┘
```

### Step 1: Gaussian State Preparation
Prepare two normalized Gaussian distributions with different scale parameters σ₁ and σ₂.

### Step 2: Branch Indicator Setup
Initialize branch qubit in |+⟩ state to enable superposition.

### Step 3: Controlled Operation
Apply controlled-SWAP or multiplexed rotation based on branch qubit state.

### Step 4: Phase Kickback
Apply Pauli-Z on branch indicator to encode the subtraction (difference).

### Step 5: Uncomputation
Uncompute Gaussian preparations and measure branch qubit for success probability.

## Mathematical Foundation

### Diagonalization
The DoG operator is diagonalized by the discrete Fourier basis:

```
DoG = F⁻¹ · diag(DoĜ(k)) · F
```

where DoĜ(k) is the transfer function in frequency domain.

### Success Probability
Exact closed-form expression:

```
P_success = Σₖ |signal̂(k)|² · |DoĜ(k)|² / ||DoG||²
```

Weighted by input signal's power spectrum.

### Frequency Response
Tunable wide-stencil bandpass filter controlled by two Gaussian scale parameters:
- σ₁: Inner Gaussian width
- σ₂: Outer Gaussian width

## Usage Patterns

### Pattern 1: Basic DoG Encoding
```python
# Prepare grid parameters
N = 2^n  # Grid points (power of 2)
D = 2    # Spatial dimensions
sigma1 = 1.0
sigma2 = 2.0

# Build block encoding
encoding = DoGBlockEncoding(N, D, sigma1, sigma2)
circuit = encoding.build_circuit()
```

### Pattern 2: Quantum Machine Learning Feature Detection
```python
# For QML applications
from quantum_block_encoding import DoGEncoder

encoder = DoGEncoder(grid_size=256, dimensions=2)
encoded_features = encoder.encode_image_quantum(image_data)
```

### Pattern 3: Finite Difference Laplacian Approximation
```python
# Approximate Laplacian-of-Gaussian
sigma_ratio = 1.6  # Optimal for edge detection
operator = DifferenceOfGaussian(sigma, sigma * sigma_ratio)
block_encoded_op = operator.to_block_encoding()
```

## Configuration

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| N | int | 256 | Grid points per dimension (power of 2) |
| D | int | 2 | Spatial dimensions |
| sigma1 | float | 1.0 | Inner Gaussian scale |
| sigma2 | float | 2.0 | Outer Gaussian scale |
| periodic | bool | True | Periodic boundary conditions |

### Scale Parameter Selection

For edge detection: σ₂/σ₁ ≈ 1.6 (Marr-Hildreth optimal)
For feature detection: σ₂/σ₁ ≈ 2.0 to 4.0

## References

- arXiv:2604.09538 - "Explicit Block Encoding of Difference-of-Gaussian Operators on a Periodic Grid"
- Childs et al. - "Quantum linear systems algorithm" (LCU framework)
- Low & Chuang - "Hamiltonian simulation by qubitization"

## Related Skills

- quantum-signal-processing
- quantum-machine-learning
- quantum-circuit-optimization

## Notes

- Requires discrete Fourier transform implementation
- Success probability scales with signal frequency content
- Optimal for smooth signals with localized features
- Compatible with quantum singular value transformation (QSVT)
