---
name: quantum-signal-processing-orthogonal-polynomials
description: >
  Implement Quantum Signal Processing (QSP) using orthogonal polynomial theory.
  Derive QSP angles analytically for Hermite, Jacobi, and Rogers-Szego polynomial families.
  Achieve O(log(1/ε)) gate complexity for ε-approximation of smooth functions via Hermite series expansion.
  Use when implementing QSP circuits, finding QSP angles, approximating functions via quantum signal processing,
  or connecting orthogonal polynomials to quantum algorithms. arXiv: 2605.05321
---

# Quantum Signal Processing via Orthogonal Polynomials

Quantum Signal Processing (QSP) embeds polynomial transformations into quantum circuits.
This skill provides the analytical framework for finding QSP angles using orthogonal polynomial theory.

## Core Result

QSP angles can be derived **analytically** (not numerically) for families of orthogonal polynomials:
- **Hermite polynomials** → Gaussian-weighted function approximation
- **Jacobi polynomials** → Bounded interval transformations
- **Rogers-Szegő polynomials** → Unit circle / phase-based transformations

**Key theorem**: An ε-approximation of a smooth function can be block-encoded using
**O(log(1/ε))** gates via its Hermite series expansion.

## QSP Basics

QSP implements a polynomial transformation P(x) on a quantum computer:

```
U(θ₀, θ₁, ..., θ_d) = e^{iθ₀Z} · W(x) · e^{iθ₁Z} · W(x) · ... · e^{iθ_dZ}
```

where W(x) is a signal oracle and θ_k are the QSP angles to be determined.

The achievable polynomials are characterized by their **orthogonality** or **biorthogonality**
with respect to a linear functional admitting an integral representation.

## Analytical Angle-Finding

### General Approach

For a target polynomial P(x) of degree d:

1. **Express P(x)** in an orthogonal polynomial basis {φ_k(x)}
2. **Map basis coefficients** to QSP angles via the orthogonality measure
3. **Construct circuit** with O(d) = O(log(1/ε)) gates

### Hermite Polynomials

For functions f: ℝ → [-1, 1] with Gaussian weight:

```python
import numpy as np
from scipy.special import hermite, roots_hermite

def hermite_qsp_angles(f, degree, weight_fn=None):
    """Compute QSP angles for Hermite polynomial approximation."""
    # Get Hermite-Gauss quadrature points
    x, w = roots_hermite(degree + 1)
    
    # Compute Hermite coefficients via quadrature
    coeffs = []
    for k in range(degree + 1):
        H_k = hermite(k)
        c_k = np.sum(w * f(x) * H_k(x)) / np.sqrt(np.pi * 2**k * np.math.factorial(k))
        coeffs.append(c_k)
    
    # Map coefficients to QSP angles
    # Phase angles θ_k determined by the recurrence relation
    angles = hermite_to_qsp_phases(coeffs)
    return angles
```

### Jacobi Polynomials

For functions on [-1, 1] with weight (1-x)^α(1+x)^β:

```python
from scipy.special import roots_jacobi

def jacobi_qsp_angles(f, degree, alpha=0, beta=0):
    """Compute QSP angles for Jacobi polynomial approximation."""
    x, w = roots_jacobi(degree + 1, alpha, beta)
    
    # Compute Jacobi coefficients
    coeffs = []
    for k in range(degree + 1):
        # P_k^{(α,β)} evaluated at quadrature points
        P_k = eval_jacobi(k, alpha, beta, x)
        c_k = np.sum(w * f(x) * P_k)
        coeffs.append(c_k)
    
    angles = jacobi_to_qsp_phases(coeffs, alpha, beta)
    return angles
```

### Rogers-Szegő Polynomials

For phase-based transformations on the unit circle:

```python
def rogers_szego_qsp_angles(f, degree, q_param=0.5):
    """Compute QSP angles for Rogers-Szegő polynomial approximation."""
    # Rogers-Szegő polynomials are orthogonal on the unit circle
    # with weight related to the q-parameter
    angles = rs_to_qsp_phases(f, degree, q_param)
    return angles
```

## Gate Complexity

| Approximation | Gate Complexity | Polynomial Family |
|--------------|-----------------|-------------------|
| ε-approximation of smooth f | **O(log(1/ε))** | Hermite |
| Degree-d polynomial | O(d) | Any orthogonal family |
| Bandlimited function | O(B · log(1/ε)) | Sinc/Whittaker |

The O(log(1/ε)) scaling for Hermite expansions is **exponentially better** than naive approaches.

## Practical Implementation

### Step 1: Choose Polynomial Family

- **Unbounded domain** → Hermite polynomials
- **Bounded interval [-1,1]** → Jacobi polynomials (includes Legendre, Chebyshev as special cases)
- **Phase/unit circle** → Rogers-Szegő polynomials

### Step 2: Compute Expansion Coefficients

Use numerical quadrature with the appropriate weight function:

```python
def compute_orthogonal_coefficients(f, poly_family, degree, **kwargs):
    """General coefficient computation for orthogonal polynomial expansion."""
    x, w = quadrature_points(poly_family, degree, **kwargs)
    coeffs = []
    for k in range(degree + 1):
        phi_k = eval_orthogonal_poly(k, poly_family, x, **kwargs)
        norm_sq = norm_squared(k, poly_family, **kwargs)
        c_k = np.sum(w * f(x) * phi_k) / norm_sq
        coeffs.append(c_k)
    return np.array(coeffs)
```

### Step 3: Convert to QSP Angles

The key innovation: analytical conversion from polynomial coefficients to QSP angles
via the orthogonality structure, avoiding numerical optimization.

### Step 4: Build QSP Circuit

```python
def build_qsp_circuit(angles, signal_oracle):
    """Build QSP circuit from computed angles."""
    circuit = QuantumCircuit(n_qubits)
    
    # Initial phase
    circuit.rz(2 * angles[0], target_qubit)
    
    # Alternating signal oracle and phase rotations
    for k in range(1, len(angles)):
        signal_oracle(circuit)
        circuit.rz(2 * angles[k], target_qubit)
    
    return circuit
```

## Applications

1. **Hamiltonian simulation**: e^{-iHt} approximated via Chebyshev (Jacobi special case)
2. **Matrix functions**: f(A) via orthogonal polynomial expansion
3. **Quantum machine learning**: Kernel functions via QSP
4. **Quantum linear systems**: 1/x approximation via orthogonal polynomials

## Key Theoretical Results

1. **Characterization theorem**: Achievable QSP polynomials ↔ orthogonal/biorthogonal families
2. **Analytical angle formula**: Explicit expressions for Hermite, Jacobi, Rogers-Szegő
3. **Complexity bound**: O(log(1/ε)) gates for smooth function approximation via Hermite
4. **Integral representation**: Orthogonality measure admits integral form → analytical angles

## Activation Keywords

- quantum signal processing QSP
- QSP angle finding
- orthogonal polynomial quantum
- Hermite polynomial quantum circuit
- Jacobi polynomial QSP
- Rogers-Szego quantum
- quantum function approximation
- block encoding polynomial
- 量子信号处理
- QSP 角度
- 正交多项式量子

## Related Skills

- `quantum-number-theory-algorithms`: Quantum algorithms with number-theoretic foundations
- `quantum-ml-patterns`: Quantum machine learning using polynomial kernels
- `physics-guided-neural-networks`: Orthogonal polynomials in physics-informed models
