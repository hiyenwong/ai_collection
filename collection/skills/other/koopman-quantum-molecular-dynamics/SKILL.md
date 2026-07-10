---
name: koopman-quantum-molecular-dynamics
description: "Koopman-von Neumann (KvN) molecular dynamics methodology for computing Green-Kubo transport coefficients as quantum algorithm readout problems. Formulates classical NVE and NVT dynamics as unitary evolutions on Hilbert spaces, enabling quantum speedup for molecular property estimation with O(log(1/ε)) qubit scaling."
---

# Koopman-Quantum Molecular Dynamics

## Description
Methodology for computing Green-Kubo transport coefficients of classical molecular dynamics by formulating them as readout problems for quantum algorithms using the Koopman-von Neumann (KvN) representation. Both NVE (microcanonical) and Nose-Hoover NVT (canonical) dynamics are derived as unitary evolutions on Hilbert spaces associated with classical phase spaces. The discretization error in correlation functions decreases as a power law in the number of grid points N_z, or equivalently, exponentially in the register size n_z (where N_z = 2^{n_z}), so a target accuracy ε requires only n_z = O(log(1/ε)) qubits.

## Activation Keywords
- Koopman-von Neumann molecular dynamics
- Green-Kubo transport coefficients
- quantum molecular dynamics
- KvN quantum algorithm
- classical dynamics quantum readout
- transport coefficient quantum
- NVE NVT quantum simulation
- quantum phase estimation molecular
- 库普曼-冯诺依曼分子动力学
- 量子格林-久保系数

## Core Concepts

### Koopman-von Neumann (KvN) Representation
- Classical mechanics reformulated in Hilbert space language
- Phase space density ψ(q,p) evolves unitarily: i∂ψ/∂t = L̂ψ
- L̂ is the Liouvillian operator (classical analog of Hamiltonian)
- Bridges classical and quantum formalisms naturally

### Green-Kubo Formula
Transport coefficients expressed as time integrals of equilibrium correlation functions:
```
κ = (1/kT²V) ∫₀^∞ ⟨J(0)J(t)⟩ dt
```
where J is the relevant flux operator.

### Quantum Algorithm Pipeline
1. **KvN Encoding**: Map classical phase space to quantum register
2. **Unitary Evolution**: Implement Liouvillian evolution as quantum circuit
3. **Flux-Excited State Preparation**: Prepare initial state with flux perturbation
4. **Quantum Phase Estimation (QPE)**: Read out correlation function spectrum
5. **Transport Coefficient Extraction**: Compute probability P₀ to extract coefficient

### Qubit Scaling
- Discretization error ∝ N_z^{-α} (power law in grid points)
- Equivalently: error ∝ 2^{-α·n_z} (exponential in qubit count)
- Target accuracy ε requires n_z = O(log(1/ε)) qubits
- Exponential advantage over classical grid-based methods

### Dynamics Types
| Ensemble | Dynamics | Quantum Implementation |
|----------|----------|----------------------|
| NVE (microcanonical) | Hamiltonian flow | Direct Liouvillian unitary |
| NVT (Nose-Hoover) | Thermostatted flow | Extended phase space unitary |

## Usage Patterns

### Pattern 1: Thermal Conductivity Estimation
Use KvN + QPE to compute thermal conductivity from classical MD trajectories with logarithmic qubit scaling.

### Pattern 2: Viscosity Calculation
Apply the framework to shear stress autocorrelation functions for viscosity estimation.

### Pattern 3: Diffusion Coefficient
Formulate velocity autocorrelation as KvN readout problem.

## Instructions for Agents

### Step 1: System Setup
- Define the classical Hamiltonian and phase space
- Choose ensemble (NVE or NVT)
- Identify the relevant flux operator for the transport coefficient

### Step 2: KvN Encoding
- Discretize phase space on grid with N_z = 2^{n_z} points
- Map classical phase space density to quantum state vector
- Construct Liouvillian operator as sparse matrix

### Step 3: Quantum Circuit Design
- Implement Liouvillian evolution using Trotterization or other methods
- Design flux-excited state preparation circuit
- Integrate QPE module for spectral analysis

### Step 4: Readout and Post-processing
- Extract probability distribution from QPE
- Compute Green-Kubo integral from spectral data
- Estimate statistical and discretization errors

### Step 5: Resource Analysis
- Analyze qubit requirements: n_z = O(log(1/ε)) for target accuracy
- Count gate complexity for Liouvillian implementation
- Compare against classical MD scaling

## Error Handling

### Discretization Error
- Grid resolution N_z controls discretization accuracy
- Error decreases as power law: O(N_z^{-α})
- For high accuracy, increase n_z logarithmically

### Trotterization Error
- For time evolution, Trotter error accumulates
- Use higher-order Trotter formulas or qubitization
- Balance circuit depth against accuracy requirements

### Finite Sampling
- QPE requires multiple shots for probability estimation
- Use amplitude estimation for quadratic speedup
- Account for statistical uncertainty in final coefficient

## Resources
- arXiv:2605.30142 — Koopman-von Neumann Molecular Dynamics for Green-Kubo Transport Coefficients

## Related Skills
- quantum-computing-patterns
- quantum-algorithm-framework-designer
- quantum-mechanical-data-assimilation
