---
name: nonstabilizerness-diffusive-dynamics
description: "Nonstabilizerness diffusion dynamics methodology for analyzing magic resource generation in many-body quantum systems using stabilizer Renyi entropy and tensor network methods."
---

# Nonstabilizerness Diffusive Dynamics

## Description

Methodology for analyzing nonstabilizerness (magic) generation and dynamics in many-body quantum systems. Computes stabilizer Renyi entropy using four-replica tensor networks evaluated by S4-adapted iTEBD in the thermodynamic limit. Identifies diffusive universality class with 1/t gap closing for late-time approach to random-state value.

## Activation Keywords
- nonstabilizerness dynamics
- stabilizer Renyi entropy
- magic state generation
- tensor network quantum dynamics
- hydrodynamic quantum information
- diffusive magic dynamics
- iTEBD quantum circuits
- 非稳定化性动力学
- 稳定化Renyi熵

## Tools Used
- exec: Run tensor network simulations
- write: Save entropy calculations
- terminal: Execute iTEBD computations

## Usage Patterns

### Pattern 1: Stabilizer Renyi Entropy Computation
For U(1)-symmetric random circuits:
1. Construct four-replica tensor network representation
2. Apply S4-symmetric iTEBD in thermodynamic limit
3. Compute stabilizer Renyi entropy M2 = -log(E[sum p_i^2])
4. Track convergence to random-state value

### Pattern 2: Hydrodynamic Analysis
For identifying universality class:
1. Map nonstabilizerness dynamics to hydrodynamic equation
2. Identify diffusive scaling: gap ~ 1/t
3. Verify scaling across different circuit families
4. Connect to random-state ensemble predictions

### Pattern 3: Energy-Conserving System Verification
For nonintegrable Ising chains:
1. Simulate time evolution under energy-conserving Hamiltonian
2. Compute stabilizer Renyi entropy at multiple times
3. Verify 1/t scaling matches random circuit prediction
4. Establish universality across model classes

## Instructions for Agents

### Step 1: System Setup
- Define the quantum circuit/Hamiltonian
- Identify symmetries (U(1), Z2, etc.)
- Choose initial state (product state, GHZ, etc.)

### Step 2: Tensor Network Construction
```python
def build_four_replica_tn(circuit, symmetries):
    """Build four-replica tensor network for stabilizer Renyi entropy."""
    # Each physical site has 4 replica indices
    # S4 symmetry permutes replicas
    tn = TensorNetwork(replicas=4, symmetry='S4')
    for gate in circuit:
        tn.apply_gate(gate, replica_structure='diagonal')
    return tn
```

### Step 3: iTEBD Evaluation
```python
def compute_stabilizer_renyi(tn, max_bond_dim=128):
    """Compute M2 via iTEBD."""
    state = tn.initialize_infinite_mps(bond_dim=max_bond_dim)
    for step in range(max_steps):
        state = iTEBD_step(state, tn, symmetrize='S4')
        if converged(state):
            break
    return stabilizer_renyi_entropy(state)
```

### Step 4: Scaling Analysis
- Plot M2(t) vs time
- Fit to 1/t + const form
- Extract diffusion coefficient
- Compare across system sizes

## Error Handling

### Bond Dimension Truncation
If convergence issues:
- Increase max_bond_dim
- Check truncation error threshold
- Use extrapolation in bond dimension

### Symmetry Enforcement
If S4 symmetry violated:
- Project onto symmetric subspace
- Use symmetry-adapted tensor format
- Verify symmetry at each iTEBD step

## Mathematical Framework

### Stabilizer Renyi Entropy
M2(rho) = -log( sum_{P in P_n} |tr(P * rho)|^2 / 2^n )
where P_n is the n-qubit Pauli group

### Diffusive Scaling
M2(infinity) - M2(t) ~ c/t  (late-time approach)
where c depends on circuit details and dimension

### Hydrodynamic Description
dm/dt = D * nabla^2 m + noise
where m is nonstabilizerness density, D is diffusion constant

## Resources
- arXiv: 2606.13606 (Xiao & Ryu, 2026)
- Related: Stabilizer formalism (Gottesman 1998)
- iTEBD: Infinite Time-Evolving Block Decimation

## Related Skills
- tensor-network-quantum-electromechanics
- quantum-statistical-mechanics-gauge
- statistical-mechanics-quantum-decoding
