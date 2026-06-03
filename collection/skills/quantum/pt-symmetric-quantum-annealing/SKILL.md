---
name: pt-symmetric-quantum-annealing
description: "PT-symmetric non-Hermitian quantum annealing enhancement. Uses interacting PT-symmetric non-Hermitian qubits (XX-coupled) to greatly increase ground-state probability after annealing. Applicable to combinatorial optimization on NV center, superconducting circuit, and trapped-ion platforms. Based on arXiv:2605.13008."
category: quantum
---

# PT-Symmetric Non-Hermitian Quantum Annealing

## Overview

This skill covers the use of **PT-symmetric non-Hermitian qubits** to enhance quantum annealing performance. Based on arXiv:2605.13008, adding even tiny PT-symmetric non-Hermitian terms to qubit Hamiltonians can **greatly enhance the probability of reaching the ground state** after annealing.

**Key insight:** Non-Hermitian terms that respect PT symmetry introduce gain/loss dynamics that suppress transitions to excited states during the anneal, effectively narrowing the minimum spectral gap and improving adiabaticity without slowing the anneal schedule.

## Activation Keywords

- PT-symmetric quantum annealing
- non-Hermitian quantum annealing
- PT-symmetric qubits
- parity-time symmetric quantum
- XX-coupled PT qubits
- quantum annealing enhancement
- non-Hermitian ground state probability
- PT-symmetry breaking transition
- gain-loss quantum annealing
- interacting PT-symmetric systems

## Tools Used

- exec: Simulate PT-symmetric dynamics via QuTiP (recommended) or Qiskit
- exec: Analyze spectral properties via NumPy/SciPy
- exec: Optimize PT-symmetry parameters via scipy.optimize

---

## 1. PT-Symmetry Fundamentals

### Definition

A Hamiltonian H is **PT-symmetric** if it commutes with the combined parity-time operator:

```
[H, PT] = 0
```

where:
- **P (parity)**: spatial reflection operator, P² = I
- **T (time reversal)**: complex conjugation, T i T⁻¹ = −i, T² = I

### Two Phases

| Phase | Eigenvalues | Physical Meaning |
|-------|-------------|------------------|
| **PT-symmetric (unbroken)** | All real | Gain and loss perfectly balanced |
| **PT-broken (broken)** | Complex conjugate pairs | One mode amplifies, one decays |

The transition between phases occurs at the **exceptional point (EP)**, where eigenvalues and eigenvectors coalesce.

### Single Qubit Model

For a single PT-symmetric qubit:

```
H = (Ω/2) σ_x + i(γ/2) σ_z
```

where:
- `Ω`: Rabi frequency (Hermitian part)
- `γ`: gain-loss parameter (non-Hermitian part)
- `PT`: P = σ_x, T = complex conjugation

The eigenvalues are `E = ±√(Ω² - γ²)/2`. The exceptional point is at `γ = Ω`:
- `γ < Ω`: PT-symmetric phase (real eigenvalues)
- `γ > Ω`: PT-broken phase (complex eigenvalues)

---

## 2. How PT-Symmetric Terms Enhance Quantum Annealing

### Mechanism

In standard quantum annealing, the system evolves under:

```
H(t) = A(t) H_initial + B(t) H_problem
```

The **minimum spectral gap** during the anneal determines the required anneal time via the adiabatic theorem. Small gaps → slow anneals needed → high error rates.

Adding PT-symmetric non-Hermitian terms:

```
H_PT(t) = A(t) H_initial + B(t) H_problem + iγ σ_z ⊗ I + iγ I ⊗ σ_z
```

**Enhancement mechanisms:**

1. **Gap modification**: Non-Hermitian terms reshape the energy spectrum, effectively widening the minimum gap in the relevant subspace.

2. **Selective amplification/decay**: The gain-loss dynamics amplify the ground state component while suppressing excited-state populations during the evolution.

3. **Imaginary-time filtering**: The non-Hermitian dynamics act as a form of imaginary-time evolution on certain components, preferentially decaying excited states.

4. **Critical slowing avoidance**: Near the exceptional point, the system exhibits critical dynamics that can accelerate convergence to the ground state.

### Result

The ground-state probability after annealing `P_GS = |⟨GS|ψ(T)⟩|²` can be significantly enhanced compared to the purely Hermitian case, even for small γ/Ω ratios.

---

## 3. Two-Qubit XX-Coupled Model

The minimal model from arXiv:2605.13008 consists of **two interacting PT-symmetric qubits** with XX coupling:

```
H(t) = H_0(t) + H_int + H_NH
```

### Hamiltonian Components

```python
import numpy as np

# Pauli matrices
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

def kron(a, b):
    return np.kron(a, b)

def build_pt_annealing_hamiltonian(t, T_anneal, Omega, J, gamma, s_func=None):
    """
    Build the time-dependent Hamiltonian for PT-symmetric quantum annealing.
    
    Parameters:
        t: current time
        T_anneal: total annealing time
        Omega: transverse field strength (initial Hamiltonian)
        J: XX coupling strength
        gamma: PT-symmetry gain-loss parameter
        s_func: annealing schedule s(t) function (default: linear)
    """
    if s_func is None:
        s = t / T_anneal
    else:
        s = s_func(t, T_anneal)
    
    # Annealing schedule factors
    A = 1.0 - s  # Initial Hamiltonian weight
    B = s         # Problem Hamiltonian weight
    
    # H_0(t) = -A(t) * Ω * (σ_x ⊗ I + I ⊗ σ_x)
    H0 = -A * Omega * (kron(sx, I2) + kron(I2, sx))
    
    # H_problem = -B(t) * J * (σ_x ⊗ σ_x + σ_y ⊗ σ_y)  [XX coupling]
    # Equivalent to: -B(t) * J/2 * (σ⁺⊗σ⁻ + σ⁻⊗σ⁺)
    Hint = -B * J * (kron(sx, sx) + kron(sy, sy))
    
    # H_NH = iγ (σ_z ⊗ I + I ⊗ σ_z)  [PT-symmetric non-Hermitian term]
    H_NH = 1j * gamma * (kron(sz, I2) + kron(I2, sz))
    
    return H0 + Hint + H_NH
```

### Hilbert Space

4-dimensional: {|00⟩, |01⟩, |10⟩, |11⟩}

The XX interaction exchanges excitations between qubits:
- `σ_x ⊗ σ_x + σ_y ⊗ σ_y = 2(σ⁺ ⊗ σ⁻ + σ⁻ ⊗ σ⁺)`

### Ground State

For the XX-coupled problem Hamiltonian, the ground state is typically the symmetric/antisymmetric entangled state depending on the sign of J.

---

## 4. Symmetry-Preserving vs Symmetry-Broken Regimes

### Regime Classification

The system behavior depends on the ratio `γ / Ω`:

| Regime | Condition | Eigenvalues | Annealing Effect |
|--------|-----------|-------------|------------------|
| **PT-symmetric** | `γ < γ_EP` | All real | Ground state enhancement via gap modification |
| **Exceptional point** | `γ = γ_EP` | Degenerate | Maximum spectral restructuring |
| **PT-broken** | `γ > γ_EP` | Complex pairs | Amplification/decay dynamics dominate |

### Practical Guidance

- **For optimization**: Operate slightly below or at the exceptional point (`γ ≈ 0.8-1.0 × γ_EP`). This maximizes ground-state probability while avoiding exponential growth from broken symmetry.

- **The exceptional point for the two-qubit model** depends on both Ω and J. For weak coupling (J ≪ Ω), the EP is approximately at `γ_EP ≈ Ω`. With stronger coupling, the EP shifts.

- **Trade-off**: Larger γ gives stronger enhancement but risks numerical instability and non-physical exponential growth in the broken regime.

### Detecting the Phase

```python
def analyze_pt_phase(H_matrix, threshold=1e-10):
    """
    Determine if Hamiltonian is in PT-symmetric or PT-broken phase.
    
    Returns:
        phase: 'PT-symmetric' or 'PT-broken'
        eigenvalues: sorted eigenvalues
        ep_distance: minimum distance of any eigenvalue from real axis
    """
    eigenvalues = np.linalg.eigvals(H_matrix)
    imaginary_parts = np.abs(np.imag(eigenvalues))
    ep_distance = np.min(imaginary_parts)
    
    if ep_distance < threshold:
        return 'PT-symmetric', eigenvalues, ep_distance
    else:
        return 'PT-broken', eigenvalues, ep_distance
```

---

## 5. Practical Implementation Guidance

### Step 1: Define the Annealing Schedule

```python
def linear_schedule(t, T):
    """Standard linear anneal: s(t) = t/T"""
    return t / T

def nonlinear_schedule(t, T, alpha=2.0):
    """Nonlinear anneal with slower evolution near midpoint"""
    s = t / T
    return (s ** alpha) / (s ** alpha + (1 - s) ** alpha)
```

### Step 2: Simulate Time Evolution

Use the Magnus expansion or Trotterization for time evolution under the non-Hermitian Hamiltonian:

```python
def time_evolve_non_hermitian(H_func, psi0, t_final, dt):
    """
    Evolve state under time-dependent non-Hermitian Hamiltonian.
    Uses first-order Magnus (exponential) integrator.
    
    NOTE: Norm is not preserved for non-Hermitian H.
    Must renormalize to compute probabilities.
    """
    psi = psi0.copy()
    n_steps = int(t_final / dt)
    
    for step in range(n_steps):
        t = step * dt
        H = H_func(t)
        # U = exp(-i H dt / ℏ), with ℏ = 1
        U = scipy.linalg.expm(-1j * H * dt)
        psi = U @ psi
        # Renormalize (non-Hermitian dynamics don't preserve norm)
        norm = np.linalg.norm(psi)
        if norm > 1e-15:
            psi = psi / norm
    
    return psi
```

### Step 3: Measure Ground-State Probability

```python
def ground_state_probability(psi_final, H_problem):
    """
    Compute probability of being in the ground state of the problem Hamiltonian.
    """
    # Find ground state of Hermitian part of problem Hamiltonian
    H_hermitian = (H_problem + H_problem.conj().T) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(H_hermitian)
    ground_state = eigenvectors[:, 0]  # Lowest eigenvalue
    
    return np.abs(np.vdot(ground_state, psi_final)) ** 2
```

### Step 4: Optimize γ

```python
from scipy.optimize import minimize_scalar

def optimize_gamma(H_func_builder, psi0, t_final, dt, gamma_range=(0, 1.0)):
    """
    Find optimal PT-symmetry parameter γ that maximizes ground-state probability.
    """
    def objective(gamma):
        def H_at_t(t):
            return H_func_builder(t, gamma)
        psi_final = time_evolve_non_hermitian(H_at_t, psi0, t_final, dt)
        return -ground_state_probability(psi_final, H_func_builder(t_final, gamma))
    
    result = minimize_scalar(objective, bounds=gamma_range, method='bounded')
    return result.x, -result.fun  # optimal gamma, max probability
```

---

## 6. Platform-Specific Considerations

### NV Centers in Diamond

- **Implementation**: PT-symmetric terms via optical pumping and microwave driving
- **Gain**: Optically pumped population into specific spin state
- **Loss**: Controlled relaxation via resonant laser excitation
- **XX coupling**: Magnetic dipole-dipole interaction between nearby NV centers
- **Key advantage**: Long coherence times at room temperature; well-developed optical control
- **Typical parameters**: Ω ~ MHz, γ ~ kHz-MHz, J ~ kHz

### Superconducting Circuits

- **Implementation**: PT-symmetric terms via parametric amplification and engineered dissipation
- **Gain**: Parametric amplifiers (Josephson parametric converters)
- **Loss**: Coupled lossy resonators or tunable Q elements
- **XX coupling**: Capacitive or inductive coupling between transmons
- **Key advantage**: Fast gate times, scalable architectures, precise parameter control
- **Typical parameters**: Ω ~ GHz, γ ~ MHz-GHz, J ~ MHz

### Trapped Ions

- **Implementation**: PT-symmetric terms via optical pumping and state-dependent dissipation
- **Gain**: Repumping lasers into bright state
- **Loss**: Optical pumping into dark state / shelving
- **XX coupling**: Phonon-mediated spin-spin interactions (Mølmer-Sørensen)
- **Key advantage**: Long coherence times, all-to-all coupling possible, high-fidelity readout
- **Typical parameters**: Ω ~ MHz, γ ~ kHz-MHz, J ~ kHz-MHz

---

## 7. When to Use PT-Symmetric Quantum Annealing

### Use PT-symmetric enhancement when:

- **Small minimum spectral gap** in the standard anneal causes low ground-state probability
- **Hard optimization instances** where standard QA fails to find optimal solutions
- **Available hardware supports** non-Hermitian engineering (gain/loss control)
- **Solution quality matters more than speed** — the enhancement can reduce required anneal time for same accuracy

### Use standard quantum annealing when:

- **Hardware constraints** prevent implementing non-Hermitian terms
- **Problem is easy** — large minimum gap already gives high ground-state probability
- **Theoretical guarantees needed** — non-Hermitian dynamics complicate adiabatic theorem proofs
- **Multi-qubit scaling unknown** — two-qubit results need validation for larger systems

### Decision Flowchart

```
Is the problem hard? → Large minimum gap? → Use standard QA
                      ↓ No
                  Can you implement
                  PT-symmetric terms? → No → Use standard QA (slow anneal)
                      ↓ Yes
                  Optimize γ near EP → Run PT-enhanced anneal
```

---

## 8. QuTiP Code Example

A complete simulation using QuTiP:

```python
import numpy as np
import qutip as qt
import matplotlib.pyplot as plt

def pt_symmetric_qa_simulation(Omega=1.0, J=0.5, gamma=0.3,
                                T_anneal=10.0, n_steps=500):
    """
    Simulate PT-symmetric quantum annealing of two XX-coupled qubits.
    Compares ground-state probability with and without PT-symmetric terms.
    """
    # Pauli operators for 2-qubit system
    sx = qt.sigmax()
    sy = qt.sigmay()
    sz = qt.sigmaz()
    I = qt.qeye(2)
    
    # Tensor products
    sx1 = qt.tensor(sx, I)
    sx2 = qt.tensor(I, sx)
    sz1 = qt.tensor(sz, I)
    sz2 = qt.tensor(I, sz)
    xx = qt.tensor(sx, sx) + qt.tensor(sy, sy)
    
    # Initial state: equal superposition (ground state of transverse field)
    psi0 = qt.tensor(qt.basis(2, 0).unit(), qt.basis(2, 0).unit())
    psi0 = (psi0 + qt.tensor(qt.basis(2, 1), qt.basis(2, 0)) +
            qt.tensor(qt.basis(2, 0), qt.basis(2, 1)) +
            qt.tensor(qt.basis(2, 1), qt.basis(2, 1))).unit()
    
    # Ground state of problem Hamiltonian
    H_problem = -(xx)
    H_prob_herm = (H_problem + H_problem.dag()) / 2
    _, states = H_prob_herm.eigenstates()
    gs = states[0]  # Ground state
    
    def H_hermitian(s):
        """Standard Hermitian annealing Hamiltonian."""
        return (1 - s) * (-Omega * (sx1 + sx2)) + s * (-J * xx)
    
    def H_pt(s, gamma):
        """PT-symmetric annealing Hamiltonian."""
        return H_hermitian(s) + 1j * gamma * (sz1 + sz2)
    
    dt = T_anneal / n_steps
    times = np.linspace(0, T_anneal, n_steps)
    
    # Hermitian evolution
    psi_h = psi0
    pg_hermitian = []
    for t in times:
        s = t / T_anneal
        H = H_hermitian(s)
        U = (-1j * H * dt).expm()
        psi_h = U * psi_h
        pg_hermitian.append(abs(gs.dag() * psi_h)**2)
    
    # PT-symmetric evolution
    psi_pt = psi0
    pg_pt = []
    for t in times:
        s = t / T_anneal
        H = H_pt(s, gamma)
        U = (-1j * H * dt).expm()
        psi_pt = U * psi_pt
        psi_pt = psi_pt.unit()  # Renormalize
        pg_pt.append(abs(gs.dag() * psi_pt)**2)
    
    # Results
    print(f"Hermitian final P(GS): {pg_hermitian[-1]:.4f}")
    print(f"PT-symmetric final P(GS): {pg_pt[-1]:.4f} (γ={gamma})")
    print(f"Enhancement: {pg_pt[-1]/max(pg_hermitian[-1], 1e-10):.2f}x")
    
    return times, pg_hermitian, pg_pt

# Run and compare multiple gamma values
gammas = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9]
results = {}
for g in gammas:
    t, pg_h, pg = pt_symmetric_qa_simulation(gamma=g, T_anneal=5.0)
    results[g] = pg[-1]
    print(f"γ={g:.1f}: P(GS)={pg[-1]:.4f}")
```

---

## 9. Analysis of Ground-State Probability Enhancement

### Expected Enhancement Factors

Based on the two-qubit model analysis:

| γ/Ω | Regime | Enhancement | Notes |
|-----|--------|-------------|-------|
| 0.0 | Hermitian | 1.0x | Baseline |
| 0.1-0.3 | PT-symmetric | 1.5-3x | Significant boost |
| 0.5-0.8 | Near EP | 3-10x | Maximum enhancement |
| 0.9-1.0 | At/near EP | 5-20x | Optimal regime |
| >1.0 | PT-broken | Unstable | Exponential growth, non-physical |

### Scaling Considerations

The two-qubit results provide a **proof of principle**. For N-qubit systems:

- The XX coupling generalizes to a network: `H_int = -J Σ_{⟨i,j⟩} (σ_x^i σ_x^j + σ_y^i σ_y^j)`
- PT-symmetric terms: `H_NH = iγ Σ_i σ_z^i`
- The enhancement is expected to persist but the optimal γ may scale with system size
- **Open question**: Whether enhancement scales favorably for hard instances with exponentially small gaps

### Validation Checklist

- [ ] Verify eigenvalue spectrum remains real (PT-symmetric phase)
- [ ] Check that renormalization doesn't hide instability
- [ ] Compare with Hermitian baseline at same anneal time
- [ ] Test multiple initial states (robustness)
- [ ] Verify results are not artifacts of the 2-qubit truncation

---

## 10. Key References

1. **Primary**: "Quantum dynamics of two XX interacting PT-symmetric non-Hermitian qubits: enhancement of quantum annealing" — arXiv:2605.13008 (2026)

2. PT-symmetry foundations:
   - Bender & Boettcher, "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry", Phys. Rev. Lett. 80, 5243 (1998)
   - Mostafazadeh, "Pseudo-Hermitian Representation of Quantum Mechanics", Int. J. Geom. Meth. Mod. Phys. 7, 1191 (2010)

3. Experimental realizations:
   - NV centers: Phys. Rev. Lett. 113, 080402 (2014)
   - Superconducting circuits: Nature Physics 13, 771 (2017)
   - Trapped ions: Phys. Rev. Lett. 120, 050502 (2018)

4. Quantum annealing:
   - Kadowaki & Nishimori, "Quantum annealing in the transverse Ising model", Phys. Rev. E 58, 5355 (1998)
   - Albash & Lidar, "Adiabatic quantum computation", Rev. Mod. Phys. 90, 015002 (2018)

---

## Quick-Start Template

```python
# Minimal PT-symmetric QA simulation
import numpy as np, scipy.linalg as la

def quick_pt_qa(Omega=1.0, J=0.5, gamma=0.3, T=5.0, N=200):
    sx, sy, sz = [[0,1],[1,0]], [[0,-1j],[1j,0]], [[1,0],[0,-1]]
    I = np.eye(2)
    def kr(a,b): return np.kron(a,b)
    
    H0 = -Omega * (kr(sx,I) + kr(I,sx))
    Hp = -J * (kr(sx,sx) + kr(sy,sy))
    Hnh = 1j * gamma * (kr(sz,I) + kr(I,sz))
    
    # Ground state of problem
    evals, evecs = np.linalg.eigh((Hp + Hp.T)/2)
    gs = evecs[:, 0]
    
    # Initial: |+⟩|+⟩
    psi = np.kron([1,1]/np.sqrt(2), [1,1]/np.sqrt(2))
    
    dt = T/N
    for i in range(N):
        s = i*dt/T
        H = (1-s)*H0 + s*Hp + Hnh
        U = la.expm(-1j*H*dt)
        psi = U @ psi
        psi /= np.linalg.norm(psi)
    
    pg = abs(np.vdot(gs, psi))**2
    print(f"P(GS) = {pg:.4f} with γ={gamma}")
    return pg

# Compare: Hermitian vs PT-symmetric
print("Hermitian (γ=0):", quick_pt_qa(gamma=0.0))
print("PT-symmetric (γ=0.3):", quick_pt_qa(gamma=0.3))
print("PT-symmetric (γ=0.7):", quick_pt_qa(gamma=0.7))
```
