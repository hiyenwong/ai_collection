---
name: conservative-adaptive-rank-quantum-kinetics
description: "Conservative adaptive rank methodology for quantum kinetic simulations — ACA SVD with Fermi-Dirac reconstruction preserving discrete macroscopic invariants near machine precision."
---

# Conservative Adaptive Rank Quantum Kinetics

## Description
Methodology for conservative adaptive rank simulation of quantum kinetic systems (Wigner-Poisson). Combines ACA SVD compression with Fermi-Dirac-type macroscopic reconstruction to preserve discrete total energy and other invariants near machine precision.

## Activation Keywords
- adaptive rank quantum simulation
- Wigner-Poisson system
- conservative kinetic simulation
- Fermi-Dirac reconstruction
- quantum kinetic method
- ACA SVD quantum
- 自适应秩量子模拟
- 维格纳-泊松系统
- 守恒量子动力学

## Core Concepts

### Key Finding (arXiv:2606.20234)
A conservative adaptive rank method for the 1D1V Wigner-Poisson system that reduces phase-space evolution cost while preserving macroscopic invariants needed for physical fidelity.

### Key Components
1. **Sampling-based adaptive rank Wigner-Poisson update** — adapts numerical rank to phase-space complexity
2. **Conservative density-momentum solve** — provides local macroscopic updates
3. **Fermi-Dirac-type reconstruction** — transfers macroscopic updates to kinetic solution (motivated by quantum-statistical structure)
4. **Global quadratic moment correction** — enforces discrete total energy constraint at kinetic level
5. **ACA SVD representation** — allows rank to adapt to nonlocal Wigner operator and self-consistent Poisson field

### Novelty vs Classical Methods
Unlike Maxwell-Boltzmann-type corrections used in classical kinetic settings, the reconstruction uses Fermi-Dirac-type form motivated by quantum-statistical structure.

## Methodology

### Step 1: Setup Adaptive Rank Framework
1. Initialize phase-space representation with ACA SVD
2. Set target accuracy for macroscopic invariants
3. Configure adaptive rank bounds

### Step 2: Wigner-Poisson Update
1. Apply sampling-based adaptive rank update
2. Nonlocal Wigner operator generates phase-space complexity
3. Self-consistent Poisson field coupling
4. Numerical rank adapts automatically to complexity

### Step 3: Conservative Macroscopic Correction
1. **Local density-momentum solve**: Compute macroscopic updates locally
2. **Fermi-Dirac reconstruction**: Transfer updates to kinetic solution
   - Uses Fermi-Dirac form (NOT Maxwell-Boltzmann)
   - Motivated by quantum-statistical structure of the model
3. **Global quadratic moment correction**: Enforce discrete total energy at kinetic level

### Step 4: Validation
- Conservation errors should be near machine precision
- Adaptive ranks should remain bounded
- Phase-space dynamics should capture benchmark behavior

### Step 5: Formulation Comparison
Two compatible correction strategies:
- **Local density-momentum + global energy**: Uses local correction plus global total energy
- **Globally conservative**: Mass, momentum, and energy all globally conserved
- Both produce nearly identical results for periodic benchmarks

## Usage Patterns

### Pattern 1: Quantum Kinetic Simulation
For simulating Wigner-Poisson dynamics:
1. Use adaptive rank compression for efficiency
2. Apply Fermi-Dirac reconstruction for quantum statistics
3. Verify conservation near machine precision

### Pattern 2: Benchmark Validation
Standard test cases:
- Two-stream instability
- Strong Landau damping
- Bump-on-tail instability
- Various quantum parameter H values

### Pattern 3: Classical-to-Quantum Extension
When extending classical kinetic methods to quantum:
- Replace Maxwell-Boltzmann correction with Fermi-Dirac
- Add global quadratic moment correction for energy
- Both correction strategies are compatible with adaptive rank compression

## Error Handling

### Unbounded Adaptive Rank
If rank grows without bound:
- Check quantum parameter H range
- Verify ACA SVD tolerance settings
- Ensure Fermi-Dirac reconstruction is properly applied

### Conservation Drift
If conservation errors exceed machine precision:
- Verify global quadratic moment correction is applied
- Check Fermi-Dirac reconstruction consistency
- Ensure density-momentum solve is converged

## Resources
- arXiv:2606.20234 "A conservative adaptive rank method for the Wigner-Poisson system"
- Related skills: quantum-statistical-estimation-framework

## Notes
- Validated for 1D1V periodic setting
- Both correction strategies (local+global vs fully global) produce nearly identical results
- Conservation errors near machine precision achieved
- Applicable to quantum semiconductor and plasma simulations