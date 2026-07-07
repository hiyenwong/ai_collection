---
name: qfi-stabilizer-framework
description: "Quantum Fisher Information framework for stabilizer codes — constructing nonlocal observables with extensive QFI density for quantum metrology. Maps stabilizer generators to dual Ising spins whose correlators equal string order parameters, converting hidden nonlocal order into metrologically accessible observables. Use when analyzing quantum metrology in stabilizer systems, computing QFI bounds, studying string order parameters, evaluating monitored cluster codes or toric code for sensing, or identifying phase transitions via QFI scaling."
---

# QFI-Stabilizer Framework

Systematic framework for constructing nonlocal observables with extensive quantum Fisher information (QFI) density in stabilizer codes. Based on Lira-Solanilla et al. (2026), arXiv:2604.15268.

## Core Idea

The framework maps stabilizer generators to dual Ising spins whose correlators equal **string order parameters**, converting hidden nonlocal order into a metrologically accessible observable. This enables identifying metrologically useful states in stabilizer codes and detecting phase transitions via QFI scaling.

## Key Results

1. **Extensive QFI regime**: Long-range string order prevails → QFI scales as O(N), enabling Heisenberg-limited metrology
2. **Intensive QFI regime**: Competing single-site measurements destroy long-range order → QFI scales as O(1)
3. **Transition detection**: The QFI scaling transition serves as an order parameter for measurement-induced phase transitions

## Mathematical Framework

### Stabilizer Code Setup

Given a stabilizer code on N qubits with stabilizer generators {g₁, g₂, ..., gₖ}:

```
S = ⟨g₁, g₂, ..., gₖ⟩ ⊂ P_N
```

where P_N is the N-qubit Pauli group.

### Dual Ising Spin Mapping

Map stabilizer generators to dual Ising spins σᵢ such that:

```
g_i → σ_i^z  (Pauli-Z in dual space)
```

String operators in the original space map to correlation functions in the dual Ising model:

```
O_string = ∏_{i∈region} g_i  ↔  ⟨∏_{i∈region} σ_i^z⟩
```

### QFI Computation

For a pure stabilizer state |ψ⟩ and observable A:

```
F_Q[|ψ⟩, A] = 4(⟨A²⟩ - ⟨A⟩²) = 4 Var(A)
```

For mixed states ρ:

```
F_Q[ρ, A] = 2 ∑_{i,j} (λ_i - λ_j)²/(λ_i + λ_j) |⟨i|A|j⟩|²
```

where ρ = ∑ᵢ λᵢ |i⟩⟨i|.

### Extensive QFI Observable Construction

1. Identify string order parameter O in dual Ising model
2. Map back to Pauli string in stabilizer code: A = ∏_{j∈S} P_j
3. Compute QFI: F_Q/N → finite constant in thermodynamic limit (extensive regime)

## Application Examples

### Monitored Cluster Codes

1D cluster state with random single-site Z measurements at rate p:

- **Low p (p < p_c)**: Extensive QFI regime, long-range string order preserved
- **High p (p > p_c)**: Intensive QFI regime, string order destroyed
- **Critical point p_c**: Measurement-induced phase transition

### Toric Code

Toric code with single-site measurements:

- **Topological phase**: Noncontractible loop operators yield extensive QFI
- **Trivial phase**: QFI becomes intensive after sufficient measurements
- **QFI scaling**: Detects topological order breakdown

## Workflow

### Step 1: Identify Stabilizer Code

Determine stabilizer generators for the target code (cluster, toric, surface, CSS, etc.).

### Step 2: Construct Dual Model

Map stabilizer generators to dual Ising spins. Identify string order parameters in the dual model.

### Step 3: Build Observable

Map string order parameter back to physical Pauli string operator A.

### Step 4: Compute QFI

Evaluate F_Q[A] for the stabilizer state. Check scaling with system size N:

- **F_Q/N → const > 0**: Extensive regime (metrologically useful)
- **F_Q/N → 0**: Intensive regime (not useful for enhanced metrology)

### Step 5: Scan Parameters

Vary control parameters (measurement rate, noise strength, etc.) to identify transitions in QFI scaling.

## Python Reference Implementation

```python
import numpy as np
from scipy.sparse import csr_matrix

def pauli_string_expectation(stabilizers, observable, n_qubits):
    """Compute expectation value of Pauli string in stabilizer state."""
    # Check if observable commutes with all stabilizers
    # If yes, expectation is ±1 depending on stabilizer signs
    # If no, expectation is 0
    for s in stabilizers:
        if not commutes(s, observable):
            return 0.0
    return 1.0  # Assumes +1 eigenstate

def qfi_pure_stabilizer(stabilizers, observable, n_qubits):
    """Compute QFI for pure stabilizer state and Pauli observable."""
    exp_A = pauli_string_expectation(stabilizers, observable, n_qubits)
    exp_A2 = pauli_string_expectation(stabilizers, observable @ observable, n_qubits)
    # For Pauli strings, A² = I, so ⟨A²⟩ = 1
    return 4.0 * (1.0 - exp_A ** 2)

def commutes(p1, p2):
    """Check if two Pauli strings commute."""
    # Count anticommuting single-qubit pairs
    anticomm = 0
    for a, b in zip(p1, p2):
        if a != 'I' and b != 'I' and a != b:
            anticomm += 1
    return anticomm % 2 == 0

def string_order_parameter(length, dual_model, position=0):
    """Compute string order parameter in dual Ising model."""
    # For 1D cluster state dual: ⟨σ_i^z (∏_{k=i+1}^{j-1} σ_k^x) σ_j^z⟩
    return np.prod([dual_model[k] for k in range(position, position + length)])
```

## Practical Tips

1. **Cluster state**: String order parameter = ⟨Z_i (∏ X_k) Z_j⟩, maps to ⟨σ_i^z σ_j^z⟩ in dual
2. **Toric code**: Noncontractible loop operators → Wilson loops in dual gauge theory
3. **CSS codes**: Separate X-type and Z-type string orders
4. **Finite-size scaling**: Use F_Q/N vs 1/N plots to extrapolate thermodynamic limit
5. **Witness bound**: F_Q ≤ N · max eigenvalue gap provides necessary condition for entanglement

## Related Concepts

- **Quantum metrology**: Heisenberg scaling vs shot-noise scaling
- **String order parameters**: Hidden order in SPT phases
- **Measurement-induced phase transitions**: Entanglement transitions under monitoring
- **Stabilizer formalism**: Gottesman-Knill theorem, Clifford circuits
- **Ising duality**: Kramers-Wannier duality, gauge theories

## References

- Lira-Solanilla et al., "Assembling Extensive Quantum Fisher Information in Stabilizer Systems", arXiv:2604.15268 (2026)
- Pezzè & Smerzi, "Quantum metrology with nonclassical states", Rev. Mod. Phys. 90, 035005 (2018)
- Sonner et al., "String order parameters and quantum metrology", Phys. Rev. Lett. (related context)
