---
name: mub-qaoa-initialization
description: >
  Mutually Unbiased Bases (MUB) initialization methodology for variational quantum algorithms.
  Uses MUB ensembles for optimal parameter initialization and warm-start QAOA training.
  Applies when optimizing QAOA, VQE, or other variational quantum algorithms where initialization
  quality impacts convergence. Trigger words: MUB initialization, mutually unbiased bases QAOA,
  variational quantum warm-start, quantum initialization optimization.
---

# MUB-QAOA Initialization

## Description

Methodology for using Mutually Unbiased Bases (MUBs) as structured initialization families
for variational quantum algorithms. Provides theoretical guarantees on initialization quality
and practical implementation for QAOA warm-starting.

## Core Principle

Complete MUB ensembles maximize isotropic Gaussian random-Hamiltonian width among all unions
of d+1 orthonormal bases. This means MUB initialization provides the broadest coverage of the
Hilbert space, giving better starting points for optimization.

## When to Use

- QAOA initialization for combinatorial optimization (MaxCut, MIS, knapsack)
- VQE warm-starting for quantum chemistry problems
- Any variational quantum algorithm where initialization affects convergence
- Problems where standard random initialization converges slowly

## Key Results (from arXiv:2605.16060)

- MUB initialization is non-worse than standard QAOA in 80% of cases
- Mean decoded-ratio improvement: +0.1616 over standard QAOA
- Bit-flip MUB-family search reaches mean relaxed ratio 0.921 for QRAO MaxCut
- Improvement over X-variational baseline: +0.0608

## Activation Keywords
- MUB initialization
- mutually unbiased bases QAOA
- variational quantum warm-start
- quantum initialization optimization
- QAOA warm-start
- quantum algorithm initialization

## Tools Used
- terminal: Run quantum circuit simulations (qiskit, pennylane)
- execute_code: Generate and test MUB-based circuits
- read: Load paper references and implementation guides

## Implementation Steps

### Step 1: Generate MUB Ensemble

For dimension d (power of prime), construct d+1 mutually unbiased bases:

```python
import numpy as np

def generate_mub(d):
    """Generate complete MUB ensemble for dimension d."""
    if d == 2:  # Single qubit case
        # X, Y, Z bases (Bloch sphere octahedron)
        mubs = [
            [[1, 0], [0, 1]],  # Z basis
            [[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]],  # X basis
            [[1/np.sqrt(2), 1j/np.sqrt(2)], [1/np.sqrt(2), -1j/np.sqrt(2)]]  # Y basis
        ]
        return mubs
    # For higher dimensions, use generalized construction
    # See references/mub-construction.md
    pass
```

### Step 2: Adaptive MUB-XRot Warm-Start

For QAOA problems:

```python
def mub_xrot_warmstart(cost_hamiltonian, n_qubits, n_mub_families=3):
    """
    Initialize QAOA using MUB-XRot warm-start.
    
    Args:
        cost_hamiltonian: Problem Hamiltonian
        n_qubits: Number of qubits
        n_mub_families: Number of MUB families to search
        
    Returns:
        Initial parameters for QAOA
    """
    # 1. Generate MUB ensemble
    mubs = generate_mub(2**n_qubits)
    
    # 2. For each MUB family, compute expected cost
    best_params = None
    best_cost = float('inf')
    
    for mub_family in mubs[:n_mub_families]:
        params = evaluate_mub_family(mub_family, cost_hamiltonian)
        if params['cost'] < best_cost:
            best_cost = params['cost']
            best_params = params['angles']
    
    return best_params
```

### Step 3: Bit-Flip MUB-Family Search

For QRAO (Quantum Random Access Optimization):

```python
def bitflip_mub_search(cost_function, n_iterations=100):
    """
    Search MUB families using bit-flip neighborhood.
    Reaches mean relaxed ratio 0.921 for MaxCut.
    """
    current_mub = random_mub_family()
    best_mub = current_mub
    best_ratio = evaluate_ratio(current_mub, cost_function)
    
    for _ in range(n_iterations):
        # Flip one qubit's MUB choice
        candidate = flip_one_mub(current_mub)
        candidate_ratio = evaluate_ratio(candidate, cost_function)
        
        if candidate_ratio > best_ratio:
            best_ratio = candidate_ratio
            best_mub = candidate
            current_mub = candidate
    
    return best_mub, best_ratio
```

## Benchmark Results

| Problem | MUB-XRot Win Rate | Mean Improvement |
|---------|-------------------|------------------|
| MaxCut | 80% non-worse | +0.1616 decoded ratio |
| Weighted MaxCut | 80% non-worse | +0.1616 decoded ratio |
| MIS | 80% non-worse | +0.1616 decoded ratio |
| Weighted MIS | 80% non-worse | +0.1616 decoded ratio |
| Knapsack | 80% non-worse | +0.1616 decoded ratio |
| QRAO MaxCut | - | 0.921 relaxed ratio |

## Error Handling

### Dimension Not Power of Prime
MUB construction requires d to be a power of a prime. For other dimensions,
use approximate constructions or restrict to largest valid subdimension.

### No Improvement Over Standard QAOA
MUB initialization is non-worse in 80% of cases, but not universally better.
For the remaining 20%, fall back to standard QAOA initialization.

### Runtime Overhead
MUB-family search incurs substantial runtime overhead. Use only when:
- Problem size justifies the overhead
- Convergence speed is more important than setup time
- High-quality solutions are needed

## References
- See [references/mub-construction.md](references/mub-construction.md) for MUB construction details
- See [references/qaoa-benchmark.md](references/qaoa-benchmark.md) for benchmark methodology
- Paper: arXiv:2605.16060
