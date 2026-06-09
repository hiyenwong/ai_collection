---
name: qaoa-zne-portfolio
description: "QAOA + Zero Noise Extrapolation (ZNE) workflow for multi-objective portfolio optimization on real IBM Quantum hardware. Demonstrates QAOA with error mitigation outperforming classical greedy baselines on 88-variable problems with carbon sequestration, biodiversity, and social impact objectives. Use when: (1) running QAOA on real quantum hardware, (2) applying ZNE for error mitigation, (3) multi-objective portfolio optimization, (4) ESG/green finance quantum applications, (5) NISQ-era quantum advantage demonstration."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2602.09047"
  published: "2026-02-13"
  authors: "Hugo José Ribeiro"
  tags: [QAOA, ZNE, portfolio-optimization, IBM-Quantum, error-mitigation, ESG, multi-objective]
---

# QAOA + ZNE for Multi-Objective Portfolio Optimization

## Core Concept

Applies the Quantum Approximate Optimization Algorithm (QAOA) combined with Zero Noise Extrapolation (ZNE) error mitigation to solve multi-objective portfolio optimization problems on real IBM Quantum hardware. Demonstrates that QAOA+ZNE consistently outperforms classical greedy baselines on 88-variable problems.

## QAOA+ZNE Workflow

### Step 1: Problem Formulation

Encode portfolio optimization as QUBO:
- **Variables**: Binary selection of assets/projects (88 variables in the study)
- **Objectives**: Carbon sequestration, biodiversity connectivity, social impact metrics
- **Constraints**: Cardinality constraints (fixed number of selections), budget limits
- **Objective function**: Weighted sum of objectives converted to Ising Hamiltonian

### Step 2: QAOA Circuit Construction

```
|0⟩^n → H^{⊗n} → [U_C(γ) · U_M(β)]^p → Measure
```

- **Cost unitary** U_C(γ): e^{-iγH_C} encodes the portfolio objective
- **Mixer unitary** U_M(β): e^{-iβH_M} explores solution space (typically X-mixer)
- **Depth p**: Number of QAOA layers (higher p → better approximation, deeper circuit)

### Step 3: Zero Noise Extrapolation (ZNE)

Error mitigation to counteract NISQ hardware noise:

1. **Noise scaling**: Intentionally amplify noise by stretching gate durations or inserting identity gates
2. **Measure at multiple noise levels**: Run circuit at noise factors λ = {1, 2, 3, ...}
3. **Extrapolate to zero noise**: Fit polynomial (Richardson or exponential) to noisy results and extrapolate to λ=0

**ZNE variants**:
- **Gate folding**: Replace gate G → G·G†·G to triple effective noise
- **Unitary folding**: Replace G → G·G†·G^n for arbitrary noise scaling
- **Richardson extrapolation**: Linear polynomial fit, most common

### Step 4: Classical Optimization Loop

```python
for iteration in range(max_iters):
    # Quantum: run QAOA+ZNE circuit
    expectation = run_qaoa_zne(parameters, backend=ibm_hardware)
    
    # Classical: optimize parameters
    parameters = optimizer.step(expectation, parameters)
    
    # Check convergence
    if converged(expectation):
        break
```

## Key Results

- QAOA+ZNE on IBM Quantum hardware outperforms classical greedy baseline
- 88-variable problem with 3 objectives (carbon, biodiversity, social impact)
- Error mitigation (ZNE) is essential — raw QAOA results degraded by hardware noise
- Demonstrates practical quantum advantage for ESG portfolio optimization

## Implementation Tips

- Use Qiskit Runtime for efficient ZNE execution on IBM hardware
- Start with low QAOA depth (p=1,2) on real hardware due to coherence limits
- ZNE shot budget: multiply shots by number of noise levels (typically 3-5×)
- Constrained optimization: use constraint-native encoding or penalty terms
- Compare against classical baselines: greedy, simulated annealing, Gurobi

## Applications

- Carbon credit portfolio optimization
- ESG investment allocation
- Multi-objective territorial planning
- Any QUBO problem benefiting from error-mitigated quantum optimization

## Activation Keywords

- QAOA ZNE
- zero noise extrapolation
- error mitigation QAOA
- quantum portfolio optimization
- IBM Quantum hardware
- multi-objective QUBO
- ESG quantum
- carbon credit portfolio
- QAOA error mitigation
- NISQ optimization
- Richardson extrapolation
- gate folding
