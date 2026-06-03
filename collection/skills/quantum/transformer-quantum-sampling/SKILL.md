---
name: transformer-quantum-sampling
description: "QiankunNet-QSCI hybrid quantum-classical framework combining transformer neural networks with quantum sampling for strongly correlated electronic structure calculations on NISQ devices"
category: quantum-computing
version: 1.0.0
arxiv: "2605.24617"
created: "2026-05-26"
---

# Transformer-Quantum Sampling (QiankunNet-QSCI)

## Overview

QiankunNet-QSCI is a hybrid quantum-classical framework that combines efficient quantum sampling with transformer neural networks to solve strongly correlated electronic structure problems on NISQ devices. The framework uses a unitary selected configuration interaction (USCI) ansatz to identify chemically significant electronic configurations on quantum hardware, then employs a transformer model to learn from sparse quantum data and reconstruct the complete electronic wavefunction with high fidelity.

## Key Concepts

### 1. USCI Ansatz for Quantum Sampling

The Unitary Selected Configuration Interaction (USCI) ansatz is specifically designed for quantum sampling on NISQ devices. It identifies the most chemically significant electronic configurations by:

- Constructing a parameterized unitary circuit that prepares superpositions of important configurations
- Measuring configuration amplitudes through repeated sampling
- Selecting configurations above a significance threshold
- Reducing circuit depth compared to full state preparation

### 2. Transformer Wavefunction Reconstruction

The transformer component (QiankunNet) learns from sparse quantum sampling data:

- **Input**: Sparse configuration amplitudes from quantum processor
- **Architecture**: Attention-based transformer that captures long-range electron correlations
- **Output**: Complete electronic wavefunction reconstruction
- **Key insight**: Transformers naturally capture the non-local correlations in quantum many-body systems

### 3. Hybrid Quantum-Classical Workflow

```
Classical initialization → Quantum USCI sampling → Classical transformer learning → Wavefunction reconstruction
```

The workflow:
1. Classical pre-processing identifies initial active space
2. Quantum processor (Zuchongzhi 3.1) performs USCI sampling on ~40-114 qubits
3. Sparse but critical quantum data is fed to transformer
4. Transformer infers and reconstructs complete wavefunction
5. Results validated against DMRG benchmarks

## Application

This skill captures patterns from recent research at the intersection of quantum computing and machine learning for computational chemistry:

- **Quantum advantage pathway**: Using NISQ devices for specific subroutines (sampling) where they excel, while using classical ML for the reconstruction task
- **Error mitigation**: Sparse sampling reduces exposure to quantum noise
- **Scalability**: Demonstrated on 40-qubit ferredoxin and 114-electron nitrogenase P-cluster

## Usage Patterns

### Pattern 1: Hybrid QML for Scientific Computing
When designing quantum-classical hybrid algorithms:
1. Identify quantum subroutines that provide advantage (sampling, state preparation)
2. Use classical ML (transformers, neural networks) for tasks requiring large data processing
3. Design data flow between quantum and classical components carefully

### Pattern 2: NISQ-Efficient Electronic Structure
For quantum chemistry on NISQ devices:
1. Use sparse sampling strategies rather than full state tomography
2. Leverage attention mechanisms for capturing long-range correlations
3. Validate against established classical methods (DMRG, FCI)

## Key Results

| System | Qubits | Result |
|--------|--------|--------|
| [2Fe-2S] ferredoxin | 40 | Chemical accuracy achieved |
| Nitrogenase P-cluster | 114 e⁻ / 73 orbitals | 12 milli-Hartree agreement with DMRG |

## Activation

Triggered by discussions of:
- Quantum machine learning for chemistry
- Transformer models for wavefunction reconstruction
- Hybrid quantum-classical algorithms
- NISQ-era electronic structure calculations
- QiankunNet, USCI ansatz
- 量子机器学习，量子化学计算，混合量子经典算法

## References

- arXiv: 2605.24617
- Authors: Xiongzhi Zeng, Ming Gong, Jian-Wei Pan, Jinlong Yang, et al.
- Quantum processor: Zuchongzhi 3.1
