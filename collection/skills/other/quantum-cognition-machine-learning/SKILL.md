---
name: quantum-cognition-machine-learning
description: "Extreme Quantum Cognition Machines (EQCM) methodology — quantum learning architectures for deliberative decision making that tolerate noisy and contradictory training data using fixed quantum dynamics with dynamical attention."
tags: ["quantum", "cognition", "decision-making", "machine-learning", "reservoir-computing"]
---

# Quantum Cognition Machine Learning

## Description
Extreme Quantum Cognition Machines (EQCM) methodology — quantum learning architectures inspired by the quantum cognition paradigm, closely related to quantum extreme learning and quantum reservoir computing. Fixed quantum dynamics generates a nonlinear feature map, learning is confined to a linear readout, and a dynamical attention mechanism modulates quantum evolution via input-dependent Hamiltonian interactions. Based on arXiv:2603.05430.

## Activation Keywords
- extreme quantum cognition
- quantum cognition machine learning
- quantum reservoir decision making
- quantum extreme learning
- dynamical attention quantum
- 量子认知机器学习
- quantum deliberative decision
- noisy training data quantum

## Tools Used
- exec: Run quantum simulation (Qiskit, PennyLane)
- read/write: Process training data, store results
- search: Find related quantum cognition papers

## Core Concepts

### Quantum Cognition Paradigm
Models cognitive processes using quantum probability theory rather than classical probability. Key phenomena captured:
- Order effects in decision making
- Violation of sure-thing principle
- Contextuality and interference effects
- Non-commutative question sequences

### EQCM Architecture
1. **Fixed Quantum Dynamics**: Hamiltonian H generates unitary evolution U(t) = exp(-iHt/ℏ)
2. **Nonlinear Feature Map**: Input states |ψ(x)⟩ evolved → |ψ'(x)⟩ = U(t)|ψ(x)⟩
3. **Linear Readout**: Observable ⟨O⟩ = ⟨ψ'(x)|O|ψ'(x)⟩ trained classically
4. **Dynamical Attention**: Input-dependent interaction term H_int(x) modulates evolution

### Relationship to Existing Methods
| Method | Feature Map | Training | Dynamics |
|--------|------------|----------|----------|
| Extreme Learning Machine | Random fixed | Linear readout | Classical |
| Quantum Reservoir Computing | Quantum evolution | Linear readout | Fixed quantum |
| EQCM | Quantum + Attention | Linear readout | Adaptive quantum |

## Instructions for Agents

### Step 1: Identify Decision-Making Problem
Suitable for:
- Decisions with contradictory/noisy training data
- Problems exhibiting contextuality or order effects
- Tasks where classical probability fails (conjunction fallacy, etc.)

### Step 2: Design Hamiltonian
```
H = H_0 + H_int(x)
H_0 = Fixed system Hamiltonian (quantum dynamics)
H_int(x) = Input-dependent interaction (attention mechanism)
```

### Step 3: Prepare Input States
Map input features x to quantum states:
- Amplitude encoding: |ψ(x)⟩ = Σᵢ xᵢ|i⟩/‖x‖
- Angle encoding: |ψ(x)⟩ = ⊗ⱼ R(θⱼ(xⱼ))|0⟩

### Step 4: Evolve and Measure
```
|ψ_out⟩ = exp(-i(H_0 + H_int(x))t)|ψ_in⟩
Output: ⟨ψ_out|O_k|ψ_out⟩ for observables {O_k}
```

### Step 5: Train Readout
Classical linear model: ŷ = W·⟨O⟩ + b
- Use ridge regression or least squares
- Only W and b are trained (quantum part is fixed)

## Error Handling

### Barren Plateaus
EQCM avoids barren plateaus because:
- Only readout layer is trained (no gradient through quantum circuit)
- Fixed dynamics provides stable feature map
- Attention mechanism is input-dependent, not parameterized

### Noisy Training Data
- Quantum superposition naturally averages over noisy samples
- Reservoir dynamics provides regularization
- Linear readout is robust to feature-space noise

## Limitations

- Requires quantum hardware or simulation for feature map
- Classical simulation scales exponentially with qubit count
- Readout capacity limited by number of measurable observables

## Resources

- arXiv:2603.05430 — Extreme Quantum Cognition Machines
- Fujii & Nakajima (2017) — Quantum reservoir computing
- Biamonte et al. — Quantum machine learning review

## Related Skills
- quantum-reservoir-computing: QRC for temporal processing
- quantum-neural-architecture: QNN design patterns
- quantum-cognition: Quantum modeling of cognitive processes
