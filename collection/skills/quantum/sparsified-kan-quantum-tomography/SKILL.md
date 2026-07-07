---
name: sparsified-kan-quantum-tomography
description: "Sparsified Kolmogorov-Arnold Networks (KAN) for interpretable quantum state tomography. Uses KAN not only as a regressor but as an inspectable reconstruction rule whose internal organization can be checked against known Pauli structure. Validated on 3-qubit GHZ family with all 63 non-identity Pauli expectation values. arXiv:2606.11814"
category: "quantum-computing"
metadata:
  arxiv_id: "2606.11814"
  authors: "Xinge Wu, Huaxin Wang, Jiajun Liu"
  published: "2026-06-10"
---

## Context

Machine learning approaches to quantum state tomography achieve high reconstruction fidelity but the physical structure used by the trained model remains implicit. This paper demonstrates that sparsified Kolmogorov-Arnold Networks (KAN) can serve as interpretable reconstruction rules whose internal structure can be validated against known Pauli operator structure.

## Core Methodology

1. **Sparsified KAN architecture**: Kolmogorov-Arnold Networks with sparsity regularization for interpretable quantum state reconstruction
2. **Pauli structure validation**: Internal KAN weights can be checked against known Pauli operator structure to verify physical consistency
3. **GHZ-family benchmark**: Controlled 3-qubit GHZ state family used as benchmark where all 63 non-identity Pauli expectation values are known
4. **Interpretability over fidelity**: Trade-off between reconstruction fidelity and interpretability is explicitly studied

## Implementation Steps

1. Prepare quantum state family (e.g., GHZ states with varying parameters)
2. Measure all Pauli expectation values (63 for 3-qubit system)
3. Train sparsified KAN to predict expectation values from state parameters
4. Analyze internal KAN structure for correspondence with Pauli operator algebra
5. Validate physical consistency of learned weights against known symmetries

## Pitfalls

- **Sparsity-fidelity tradeoff**: Higher sparsity may reduce reconstruction fidelity
- **Pauli basis completeness**: Need all 4^n - 1 non-identity Pauli measurements for full tomography
- **Interpretability limit**: KAN structure may not directly map to Pauli structure for complex states

## Verification

- Verify KAN predictions match measured Pauli expectations within statistical error
- Check that learned KAN structure respects known symmetries of the state family
- Compare with standard maximum likelihood tomography for fidelity validation

## Activation

Kolmogorov-Arnold Network, KAN, quantum tomography, interpretable ML, Pauli structure, GHZ state, sparse network
