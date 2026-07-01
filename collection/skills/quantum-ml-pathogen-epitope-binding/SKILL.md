---
name: quantum-ml-pathogen-epitope-binding
description: "Parameterized quantum circuits for classifying pathogen epitope-receptor binding strength using hybrid QML. Studies entanglement gate topology effects on vaccine design classification tasks. Activation: quantum ML, pathogen epitope, vaccine design, PQC, binding classification, entanglement topology"
---

## Quantum ML for Pathogen Epitope-Receptor Binding

**Source**: arXiv:2606.28655
**Title**: Exploring the Effects of Entanglement on Quantum Machine Learning of Pathogen Epitope-Receptor Binding
**Authors**: Brisebois, Aspen Erlandsson, Dominguez, Luis Pablo Gonzalez, Prajapati, Shivansi

## Overview

Parameterized quantum circuits (PQCs) for hybrid quantum machine learning to classify strong vs. weak epitope-receptor binding in Porcine Reproductive and Respiratory Syndrome (PRRS) vaccine design. Studies how entanglement gate number and topology in feature maps affect classification performance.

## Core Methodology

### 1. Hybrid QNN Architecture
- **PQC Feature Map**: Parameterized quantum circuits with configurable entanglement topology
- **Fixed QNN Workflow**: Hybrid quantum-classical neural network for classification
- **Binary Classification**: Strong vs. weak epitope-receptor binding

### 2. Entanglement Topology Study
- **Variable Gate Count**: Number of two-qubit entangling gates in feature map
- **Variable Topology**: Connectivity pattern of entangling gates (linear, circular, all-to-all)
- **Optimization Challenges**: Barren plateaus from deep circuits on NISQ devices

### 3. Application: PRRS Vaccine Design
- Porcine Reproductive and Respiratory Syndrome vaccine target identification
- Classifying epitope-receptor binding strength
- Data-driven approach for vaccine candidate selection

## Implementation Steps

```python
# Pseudo-workflow
1. Encode epitope-receptor features into quantum states via PQC
2. Configure entanglement topology (linear/circular/all-to-all)
3. Set number of two-qubit entangling gates
4. Apply fixed QNN layers (parameterized quantum gates)
5. Measure output qubits for classification
6. Classical post-processing for binding strength prediction
7. Optimize parameters via hybrid gradient descent
```

## Key Findings

- Entanglement gate topology significantly affects classification accuracy
- Too many entangling gates → barren plateaus (gradient vanishing)
- Optimal topology depends on data complexity and hardware constraints
- NISQ devices require careful depth management

## Pitfalls

- Barren plateaus with deep entangling circuits
- NISQ noise limits practical circuit depth
- Topology optimization is empirical — no theoretical guarantee
- Training scale can introduce optimization challenges

## Applications

- Vaccine design and epitope selection
- Drug-target binding affinity prediction
- Protein-protein interaction classification
- Pathogen-host interaction modeling
