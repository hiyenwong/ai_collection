---
name: quantum-subgroup-discovery
description: >
  Quantum-enhanced subgroup discovery for network security and explainable
  intrusion detection. Formulates subgroup discovery (SD) as QUBO optimization
  solved via QAOA on quantum hardware. Covers Weighted Relative Accuracy (WRAcc)
  landscape fitting, surrogate sampling for large QUBOs, NISQ hardware scaling
  boundaries, and quantum-classical SD comparison. Use when building explainable
  network intrusion detection systems, applying quantum optimization to feature
  subset selection, discovering interpretable security rules, or evaluating
  QAOA performance on NISQ hardware for combinatorial search problems.
  Trigger: quantum subgroup discovery, quantum intrusion detection, QAOA network
  security, explainable quantum ML, WRAcc optimization, NISQ scaling boundary.
---

# Quantum Subgroup Discovery for Network Security

Methodology from arXiv:2604.27153 "Formulating Subgroup Discovery as a Quantum Optimization Problem for Network Security" by Spell & Shyu.

## Core Insight

Subgroup Discovery (SD) builds interpretable rules characterizing feature interactions associated with attack traffic. Classical beam search struggles with exponential search spaces and prunes critical multi-feature interactions. Formulating SD as QUBO solved via QAOA discovers subgroups competitive with classical heuristics while finding multi-feature patterns that greedy search prunes.

## QUBO Formulation for Subgroup Discovery

### Objective

Maximize Weighted Relative Accuracy (WRAcc) over feature subsets:

```
WRAcc(S) = p(S) · (p(C|S) - p(C))
```

Where S = subgroup, C = target class (attack).

### QUBO Encoding

```
H = Σᵢ αᵢ·qᵢ + Σᵢ<ⱼ βᵢⱼ·qᵢ·qⱼ
```

- qᵢ ∈ {0,1}: whether feature i is included in subgroup
- αᵢ: single-feature WRAcc contribution
- βᵢⱼ: interaction WRAcc between features i and j

### Least-Squares Fitting

Fit Hamiltonian coefficients by sampling feature subsets and measuring WRAcc:

```
min ||A·θ - WRAcc||²
```

Where A encodes subset membership, θ contains Hamiltonian parameters.

### Surrogate Sampling for Large QUBOs

For QUBOs exceeding hardware qubit count:
1. Sample subset of features
2. Fit QUBO on sampled subset
3. Solve reduced QUBO
4. Aggregate results across samples

## NISQ Hardware Scaling Boundary

Empirical results on IBM quantum hardware (ibm_pittsburgh):

| Qubits | WRAcc Ratio | Interpretation |
|--------|-------------|----------------|
| 10 | 0.983 | Near-optimal |
| 15 | 0.971 | Excellent |
| 20 | 0.855 | Good |
| 25 | 0.624 | Degrading |
| 30 | 0.039 | Noise dominates |

**Boundary**: QAOA at depth p=1 effective up to ~20 qubits on current hardware. Beyond 25 qubits, circuit noise dominates signal.

## Quantum Advantages over Classical SD

1. **Multi-feature interactions**: QAOA discovers patterns pruned by greedy beam search
2. **QAOA-unique subgroups**: Achieve up to 99.6% test precision
3. **Global search**: Explores full feature space, not greedy local optima
4. **Explainability**: Output subgroups are interpretable rules

## Workflow for Quantum Subgroup Discovery

1. **Preprocess data**: Encode features as binary/categorical
2. **Sample feature subsets**: Generate training data for QUBO fitting
3. **Compute WRAcc**: Measure quality of each sampled subset
4. **Fit QUBO**: Solve least-squares for Hamiltonian coefficients
5. **Execute QAOA**: Run on quantum hardware at depth p=1
6. **Decode results**: Map qubit states to feature subsets
7. **Evaluate**: Compare WRAcc and precision against beam search baseline
8. **Scale**: Use surrogate sampling for feature spaces > hardware qubits

## Integration with Intrusion Detection Pipeline

```
[Network Traffic] → [Feature Extraction] → [Quantum SD] → [Interpretable Rules] → [Detection]
```

- Quantum SD produces human-readable rules (e.g., "IF protocol=TCP AND dst_bytes>500 AND flag=REJ THEN attack")
- Rules can be deployed in classical IDS for real-time detection
- Quantum component only needed for periodic rule discovery/retraining

## Common Pitfalls

- **QUBO fitting quality**: Poor sampling leads to inaccurate Hamiltonian
- **Hardware noise**: Beyond 25 qubits, noise overwhelms signal at p=1
- **Depth limitation**: p>1 QAOA infeasible on current hardware for SD problems
- **Feature encoding**: Must properly discretize continuous features for binary QUBO

## Activation Keywords

- quantum subgroup discovery
- quantum intrusion detection
- QAOA network security
- WRAcc optimization
- explainable quantum ML
- NISQ scaling boundary
- quantum feature selection
- quantum cybersecurity
