---
name: statistical-quantum-phase-estimation
description: "Statistical Quantum Phase Estimation (SQPE) methodology with extensions for early fault-tolerant quantum computers. Addresses practical limitations of SQPE including negative Pauli weights, overlap estimation requirements, and circuit sample optimization. Use when: quantum phase estimation, ground state energy estimation, early fault-tolerant quantum computing, CDF-based spectral analysis, changepoint detection for quantum states, Fourier series symmetry optimization, Qiskit quantum simulation."
---

# Statistical Quantum Phase Estimation (SQPE) Extensions

Methodology from arXiv:2605.18876 (Surana & Allen, 2026).

## Problem

Standard SQPE estimates ground state energy (GSE) by:
1. Estimating the cumulative distribution function (CDF) of Hamiltonian spectral density
2. Using Fourier approximation of CDF
3. Identifying first jump discontinuity → GSE

**Limitations addressed**:
- Requires positive Pauli weights (unrealistic for general Hamiltonians)
- Requires good estimate of overlap between trial and true ground state (hard to obtain)
- Requires many circuit runs/samples

## Extensions

### 1. Negative Pauli Weights

Generalize random compilation procedure for Hamiltonians with negative Pauli weights in LCU decomposition:

```
Original: H = Σ w_i P_i with w_i > 0 (positive Pauli weights)
Extended: H = Σ w_i P_i with w_i ∈ R (any real weights)
```

Uses modified LCU decomposition that handles arbitrary signs.

### 2. Changepoint Detection (No Overlap Estimate Needed)

Replace overlap-dependent GSE determination with changepoint detection method:

```
1. Estimate CDF at multiple energy points
2. Apply statistical changepoint detection on CDF values
3. First detected changepoint → Ground State Energy
4. No prior overlap estimate required
```

This is more practical as overlap estimation is a chicken-and-egg problem.

### 3. Fourier Series Symmetry (2x Sample Reduction)

Exploit symmetry of Fourier series to reduce circuit runs:

```
Standard: N circuit runs per energy point
Optimized: N/2 circuit runs (exploit real/imaginary symmetry of Fourier coefficients)
Accuracy: Same GSE estimation accuracy
```

## Implementation Pattern (Qiskit)

```python
from qiskit import QuantumCircuit
import numpy as np

def sqpe_changepoint(hamiltonian_terms, trial_state, n_samples_per_point=100):
    """SQPE with changepoint detection, no overlap estimate needed."""
    # 1. Build Fourier-approximated CDF circuits
    # 2. Handle negative Pauli weights via generalized LCU
    # 3. Measure CDF at energy grid points
    # 4. Apply changepoint detection to find first jump
    # 5. Return GSE estimate
    pass
```

## Key Parameters

| Parameter | Description | Recommended |
|-----------|-------------|-------------|
| `n_ancillae` | Number of ancilla qubits per run | Few (2-4) |
| `circuit_depth` | Depth per circuit run | Short (early FTQC friendly) |
| `n_samples` | Samples per energy point | Halved via Fourier symmetry |
| `changepoint_threshold` | Sensitivity for jump detection | Tune per problem |

## Comparison with Standard QPE

| Aspect | Standard QPE | SQPE (this paper) |
|--------|-------------|-------------------|
| Ancillae | O(n) | Few (2-4) |
| Circuit depth | Long | Short |
| Overlap needed | Yes | No (changepoint) |
| Pauli weights | N/A | Any sign |
| Sample efficiency | Baseline | 2x improvement |

## Activation

Keywords: statistical quantum phase estimation, SQPE, ground state energy, changepoint detection, LCU decomposition, Pauli weights, Fourier symmetry, early fault-tolerant quantum computing, CDF spectral analysis
