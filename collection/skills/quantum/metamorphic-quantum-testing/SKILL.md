---
name: metamorphic-quantum-testing
description: "Physics-based metamorphic testing framework for Variational Quantum Circuits (VQCs). Addresses the oracle problem in quantum testing by deriving test oracles from quantum mechanical properties. Use when: testing VQEs/QAOA circuits, verifying quantum circuit implementations, building quantum software testing infrastructure. Source: MetaMorphQ (arXiv:2606.28742, 2026-06-27)."
activation: quantum testing, metamorphic testing, VQE testing, quantum circuit verification, VQC testing, quantum oracle problem
---

# Physics-Based Metamorphic Testing for Quantum Circuits

## Problem Statement

Testing Variational Quantum Eigensolvers (VQEs) and other variational quantum circuits faces the **oracle problem**: the ground-state energy they compute is itself unknown, making it impossible to verify correctness against a known expected value. Traditional convergence-based testing is unreliable due to optimization instability and high false-positive rates.

## Solution: MetaMorphQ Framework

Derive test oracles **directly from quantum mechanical properties** of the circuit, creating metamorphic relations that must hold regardless of the specific problem instance.

## Five Physics-Based Metamorphic Relations

### MR1: Parameter-Shift Invariance
For any parametrized rotation gate R(θ), shifting the parameter by 2π should produce identical results:
VQE(θ) ≈ VQE(θ + 2π)
Test: Run VQE with θ and θ+2π, verify energy difference < ε

### MR2: Gate Commutation Equivalence
For commuting gates A and B ([A,B] = 0):
⟨ψ|AB|ψ⟩ = ⟨ψ|BA|ψ⟩
Test: Execute circuit with AB order vs BA order, verify outputs match within tolerance

### MR3: Hamiltonian Symmetry
If Hamiltonian H has symmetry operation S (SHS† = H):
E(S|ψ⟩) = E(|ψ⟩)
Test: Apply symmetry transformation to initial state, verify same energy result

### MR4: Eigenvalue Scaling
For scaled Hamiltonian αH:
E(αH) = α · E(H)
Test: Scale Hamiltonian by factor α, verify energy scales accordingly

### MR5: Basis Transformation Consistency
For unitary basis change U:
E(U†HU) = E(H)
Test: Transform Hamiltonian basis, verify energy invariance

## Implementation Pattern

```python
class MetaMorphQTester:
    def __init__(self, vqe_circuit, hamiltonian, tolerance=1e-6):
        self.vqe = vqe_circuit
        self.H = hamiltonian
        self.tol = tolerance

    def test_parameter_shift(self, theta):
        """MR1: Test 2π periodicity of rotation parameters"""
        e1 = self.vqe.run(theta)
        e2 = self.vqe.run(theta + 2*np.pi)
        return abs(e1 - e2) < self.tol

    def test_gate_commutation(self, gate_a, gate_b):
        """MR2: Test commuting gate equivalence"""
        result_ab = self.vqe.run(order=[gate_a, gate_b])
        result_ba = self.vqe.run(order=[gate_b, gate_a])
        return abs(result_ab - result_ba) < self.tol

    def test_hamiltonian_scaling(self, alpha):
        """MR4: Test energy scales with Hamiltonian scaling"""
        e_original = self.vqe.run(self.H)
        e_scaled = self.vqe.run(alpha * self.H)
        return abs(e_scaled - alpha * e_original) < self.tol * abs(e_original)

    def run_full_suite(self):
        """Execute all metamorphic relations"""
        results = {
            'parameter_shift': self.test_parameter_shift(np.pi/4),
            'gate_commutation': self.test_gate_commutation('X', 'Z'),
            'hamiltonian_scaling': self.test_hamiltonian_scaling(2.0),
        }
        return all(results.values()), results
```

## Key Advantages

1. **No oracle needed**: Tests correctness without knowing expected outputs
2. **Physics-grounded**: Relations derived from fundamental quantum mechanics
3. **Reliable**: Low false-positive rate compared to convergence-based testing
4. **Composable**: Relations can be combined for comprehensive test suites
5. **Framework-agnostic**: Works with any VQE/QAOA implementation

## Applicable To

- VQE (Variational Quantum Eigensolver) implementations
- QAOA (Quantum Approximate Optimization Algorithm) circuits
- Any parametrized quantum circuit with rotation gates
- Quantum chemistry simulation pipelines
- Quantum optimization workflows

## Trigger Patterns

- Building quantum software testing infrastructure
- Verifying quantum circuit implementations
- Debugging VQE/QAOA convergence issues
- Quality assurance for quantum applications
- Testing quantum circuit compilation/transpilation