---
name: geometric-quantum-indeterminacy
description: >
  Geometric formulation of quantum indeterminacy using convex geometry in phase space
  and symplectic topology methods. Derives standard uncertainty inequalities from first
  principles without relying on statistical descriptors like variance or covariance.
  Use when: analyzing quantum uncertainty, studying phase space geometry of quantum states,
  applying symplectic topology to quantum mechanics, deriving uncertainty relations
  geometrically, computing symplectic capacities, or working with convex bodies in
  quantum phase space. Triggers: quantum indeterminacy, geometric uncertainty,
  symplectic capacity, phase space geometry, convex quantum, uncertainty relations
  derivation, symplectic topology quantum, Mahler volume quantum.
---

# Geometric Quantum Indeterminacy

Geometric formulation of quantum indeterminacy based on convex geometry in phase space
and symplectic topology (arXiv: 2605.01103v1, Maurice de Gosson).

## Core Principle

Standard uncertainty inequalities (Heisenberg, Robertson-Schrodinger) emerge as necessary
consequences of convex geometry in phase space, without relying on statistical descriptors
(variance, covariance, expectation values).

## Key Concepts

### Quantum State as Convex Body

A quantum state corresponds to a convex body Ω in phase space R^{2n}:
- Position-momentum uncertainty defines the shape of Ω
- The body must satisfy symplectic constraints
- Pure states correspond to minimal-volume convex bodies

### Symplectic Capacity

The fundamental geometric quantity replacing variance:
- c(Ω) = symplectic capacity of the convex body Ω
- For any quantum state: c(Ω) >= h/2 (Planck constant)
- This geometric constraint implies all standard uncertainty relations

### John Ellipsoid Method

For a convex body Ω in phase space:
1. Find the John ellipsoid E (maximal volume ellipsoid contained in Ω)
2. The ellipsoid's axes give the principal uncertainties
3. The product of conjugate axis lengths >= h/2

## Workflow

### Step 1: Define the Phase Space Region

Given a quantum state (wavefunction ψ or density matrix ρ):
```python
import numpy as np
from scipy.spatial import ConvexHull

def state_to_phase_space_points(psi, n_points=1000):
    """Sample Wigner function to get phase space boundary points."""
    # Compute Wigner function on grid
    # Extract level set corresponding to state support
    # Return boundary points as convex body approximation
    pass
```

### Step 2: Compute Convex Hull

```python
def compute_convex_body(points):
    """Compute convex hull of phase space points."""
    hull = ConvexHull(points)
    return hull
```

### Step 3: Calculate Symplectic Capacity

For 2D phase space (1 degree of freedom):
```python
def symplectic_capacity_2d(convex_body):
    """Compute symplectic capacity as area/(2*pi*hbar)."""
    area = convex_body.volume  # 2D "volume" = area
    return area / (2 * np.pi * hbar)
```

For higher dimensions, use the Gromov width:
- Find the largest symplectic ball that embeds into Ω
- The radius squared gives the capacity

### Step 4: Derive Uncertainty Relations

From symplectic capacity c(Ω):
- Δx · Δp >= h/2 follows from c(Ω) >= h/2
- Robertson-Schrodinger relation follows from ellipsoid geometry
- Generalized uncertainty relations follow from symplectic invariants

## Mathematical Framework

### Symplectic Form

On R^{2n} with coordinates (x_1, ..., x_n, p_1, ..., p_n):
```
ω = Σ dx_i ∧ dp_i
```

### Symplectic Transformations

Linear transformations S preserving ω:
```
S^T J S = J, where J = [[0, I], [-I, 0]]
```

### Gromov's Non-Squeezing Theorem

A ball B^{2n}(r) can be symplectically embedded into a cylinder
Z^{2n}(R) = B^2(R) × R^{2n-2} if and only if r <= R.

This is the geometric origin of the uncertainty principle.

## Applications

### 1. Quantum State Classification

Classify states by their symplectic invariants:
- Gaussian states: ellipsoidal convex bodies
- Non-Gaussian states: more complex convex bodies
- Entangled states: non-factorizable convex bodies

### 2. Uncertainty Quantification

For any observable, derive tight bounds:
```python
def geometric_uncertainty(observable, convex_body):
    """Compute uncertainty bound from geometry."""
    # Project convex body onto observable's direction
    # Width of projection gives uncertainty
    pass
```

### 3. Quantum-Classical Boundary

The transition from quantum to classical:
- Quantum: convex bodies with c(Ω) >= h/2
- Classical: convex bodies with c(Ω) -> 0
- Semiclassical: c(Ω) ≈ h/2

## Pitfalls

- Symplectic capacity is NOT the same as volume
- The John ellipsoid may not capture all quantum features
- For mixed states, the convex body is larger than for pure states
- Numerical computation of symplectic capacity in high dimensions is challenging

## References

- de Gosson, M. (2026). "On Quantum Indeterminacy." arXiv:2605.01103v1
- Gromov, M. (1985). "Pseudoholomorphic curves in symplectic manifolds."
- Hofer, H., Zehnder, E. (2011). "Symplectic Invariants and Hamiltonian Dynamics."
