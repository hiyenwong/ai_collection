---
name: splitting-variational-quantum-algorithm
description: "Operator-splitting variational quantum algorithm (sVQA) for simulating nonlinear quantum equations on quantum computers. Decomposes state-dependent nonlinear evolution into linear substeps (implementable as fixed unitaries) and nonlinear variational corrections (measurement-based). Use when: (1) simulating nonlinear differential equations on quantum hardware, (2) implementing nonlinear quantum dynamics via VQA, (3) handling state-dependent interactions that cannot be unitary, (4) designing operator-splitting quantum algorithms. Activation: splitting VQA, nonlinear quantum simulation, operator splitting, variational quantum algorithm, nonlinear Dirac equation"
metadata:
  arxiv_id: "2606.08053"
  published: "2026-06-06"
  authors: "Qian Zuo, Ying He, Xiaofei Zhao"
  tags: ["variational-quantum-algorithm", "operator-splitting", "nonlinear-simulation", "dirac-equation", "quantum-dynamics"]
---

# Splitting Variational Quantum Algorithm (sVQA)

## Core Methodology

Addresses the fundamental challenge of implementing **nonlinear quantum evolution** on quantum computers: state-dependent nonlinear interactions cannot be directly encoded as fixed unitary circuits. The solution decomposes the evolution into:

1. **Linear substep**: Implemented as fixed unitary circuit (e.g., via QFT and spinor-Fourier propagator)
2. **Nonlinear variational correction**: Reformulated as measurement-based variational update

### Key Innovations

1. **Operator splitting for VQA**: Extends classical split-operator methods to the variational quantum setting
2. **Measurement-based nonlinear update**: Nonlinear correction expressed through overlap, self-channel, and cross-channel observables
3. **Spinor-Fourier representation**: Joint position-spin register preserves spin-momentum coupling and mass-induced spin evolution

### Application: Nonlinear Dirac Equation

The nonlinear Dirac equation (NLDE) describes relativistic fermions with nonlinear self-interaction. The time-discrete update depends on the intermediate spinor state, preventing direct unitary implementation.

**Decomposition**:
- **Linear Dirac substep**: Split-operator method with QFT for momentum-space operations
- **Nonlinear variational correction**: Small set of observables measured and fed back into variational optimization

## Agent Workflow

### Step 1: Identify Equation Structure

For the target nonlinear PDE:
- Separate into linear operator (L) and nonlinear operator (N(ψ))
- Linear part must be implementable as unitary circuit
- Nonlinear part must be expressible via measurable observables

### Step 2: Design Linear Substep Circuit

For the linear operator:
1. Map to quantum register (position + internal degrees of freedom)
2. Implement via Trotter splitting or exact diagonalization
3. Use QFT for momentum-space operations when applicable

### Step 3: Design Nonlinear Variational Correction

For the nonlinear term:
1. Identify the observables needed (overlap integrals, expectation values)
2. Design measurement circuits for each observable
3. Feed measurement results into classical optimizer
4. Variational update approximates the nonlinear evolution

### Step 4: Iterate Time Steps

For each time step:
1. Apply linear circuit
2. Measure observables
3. Compute variational correction
4. Apply correction circuit
5. Repeat for next time step

## Implementation Patterns

### Pattern 1: Split-Operator VQA for Nonlinear Schrödinger

- Linear: kinetic energy (via QFT) + potential (diagonal in position basis)
- Nonlinear: |ψ|²ψ term measured via density observables
- Variational ansatz: parameterized quantum circuit with sufficient expressivity

### Pattern 2: Dirac-sVQA for Relativistic Equations

- Linear: Dirac operator (spin-momentum coupling + mass term)
- Nonlinear: state-dependent interaction term
- Register: joint position-spin qubit encoding
- Observables: overlap, self-channel, cross-channel measurements

## Error Handling

### Measurement Noise
- Nonlinear correction depends on precise observable estimation
- Use sufficient measurement shots for statistical accuracy
- Consider error mitigation for observable estimation

### Ansatz Expressivity
- Variational ansatz must be expressive enough to capture nonlinear dynamics
- Use problem-informed ansatz design (e.g., symmetry-preserving circuits)
- Monitor approximation error over time evolution

### Long-Time Stability
- Variational error can accumulate over many time steps
- Monitor conserved quantities (norm, energy) as stability diagnostics
- Consider adaptive time-stepping based on error estimates

## Pitfalls

- **Nonlinearity is approximated, not exact**: The variational correction is an approximation — accuracy depends on ansatz expressivity and measurement precision
- **State-dependent updates break unitarity**: This is the fundamental challenge — the splitting approach circumvents it but introduces variational error
- **Resource estimates scale with nonlinearity complexity**: More complex nonlinear terms require more observables and measurements
