---
name: classical-shadow-unitary-channel-estimation
description: "Classical Shadow Estimation of Unitary Channels (CSEU) methodology for efficient quantum process learning with Heisenberg-limited query complexity."
---

# Classical Shadow Estimation of Unitary Channels (CSEU)

## Description

Classical Shadow Estimation of Unitary Channels (CSEU) is a methodology for predicting properties of unknown quantum evolutions without full tomography. Uses parallel non-adaptive queries achieving O(d/eps) query complexity (Heisenberg scaling) with a matching Omega(d/eps) lower bound. Enables efficient learning of unitary channel properties, Hamiltonian parameters, and shallow circuit behavior.

## Activation Keywords
- classical shadow estimation
- unitary channel tomography
- CSEU protocol
- quantum process learning
- Heisenberg limit tomography
- parallel quantum queries
- quantum channel characterization
- Hamiltonian learning
- 经典影子估计
- 量子信道学习

## Tools Used
- exec: Run quantum simulation (Qiskit/PennyLane)
- write: Save experimental results
- terminal: Execute quantum circuit simulations

## Usage Patterns

### Pattern 1: Parallel Non-adaptive CSEU Protocol
Given unknown unitary U and target precision eps:
1. Prepare entangled input states (or use constant-rank states)
2. Apply U in parallel across multiple queries
3. Measure in randomized bases (Clifford/Pauli)
4. Store classical snapshots (shadows)
5. Predict expectation values tr[O * U*rho*U^dagger] from shadows

### Pattern 2: Hamiltonian Learning via Channel Shadows
When learning Hamiltonian H from time evolution U = exp(-iHt):
1. Use CSEU to obtain classical shadow of U
2. Extract Pauli transfer matrix elements
3. Reconstruct Hamiltonian coefficients from shadow data
4. Achieves Heisenberg scaling in precision eps

### Pattern 3: Pure State Property Estimation
For learning properties of unknown pure states:
1. Treat state preparation as unitary channel |0> -> |psi>
2. Apply CSEU protocol to the preparation channel
3. Predict arbitrary observables on |psi> from shadows

## Instructions for Agents

### Step 1: Problem Formulation
- Identify the quantum process to learn (unitary U)
- Determine target precision eps
- Check if input states/observables have constant rank

### Step 2: Protocol Selection
- Use parallel non-adaptive CSEU when:
  - Sequential queries are expensive/impossible
  - High precision is required (Heisenberg scaling matters)
  - Multiple properties need prediction from same data
- Query complexity: O(d/eps) for d-dimensional system

### Step 3: Implementation
```python
import numpy as np

def cseu_protocol(unitary, num_queries, eps, dim):
    """Parallel non-adaptive CSEU protocol."""
    # Prepare entangled input states
    shadows = []
    for _ in range(num_queries):
        # Randomized measurement basis
        basis = random_clifford(dim)
        # Apply unitary and measure
        outcome = measure(unitary, basis)
        shadows.append(classical_snapshot(outcome, basis))
    return shadows

def predict_expectation(shadows, observable):
    """Predict expectation value from classical shadows."""
    return np.mean([shadow_predict(s, observable) for s in shadows])
```

### Step 4: Verification
- Verify O(d/eps) query scaling empirically
- Compare against sequential protocol baselines
- Check prediction accuracy against ground truth

## Error Handling

### Insufficient Queries
If prediction error > eps:
- Increase queries to O(d/eps)
- Check if Omega(d/eps) lower bound applies

### High-Dimensional Systems
For large d where O(d/eps) is prohibitive:
- Exploit structure (locality, symmetry)
- Use approximate shadows with reduced dimension

## Mathematical Framework

### Query Complexity
- Upper bound: O(d * eps^{-1}) queries for constant-rank states/observables
- Lower bound: Omega(d * eps^{-1}) — query optimal
- Achieves Heisenberg scaling: eps^{-1} (not eps^{-2} like standard methods)

### Shadow Construction
For unitary U, input rho, observable O:
- Snapshot: M(U, rho) = inverse_channel(measurement_outcome)
- Prediction: E[tr(O * M(U, rho))] = tr(O * U * rho * U^dagger)

## Resources
- arXiv: 2606.13638 (He et al., 2026)
- Related: Classical shadows for states (Huang, Kueng, Preskill 2020)
- Applications: Hamiltonian learning, process tomography, circuit verification

## Related Skills
- quantum-ml-data-loading
- quantum-statistical-estimation
- quantum-state-fidelity-neural-networks
