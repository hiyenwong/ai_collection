---
name: quantum-neural-network-testing
description: Mutation testing framework for Quantum Neural Networks (QNNs). Use when: (1) testing QNN/VQC reliability and robustness, (2) evaluating quantum circuit quality, (3) designing test suites for variational quantum circuits, (4) simulating quantum hardware errors for validation, (5) localizing vulnerable regions in quantum circuits. Covers statistical mutation killing, gate-level and parameter-level mutation operators, and noisy-device simulation. Activation: quantum testing, QNN testing, mutation testing quantum, circuit validation, quantum neural network testing, QNN robustness.
---

# Quantum Neural Network Testing (QuanForge)

Mutation testing methodology for Quantum Neural Networks based on QuanForge framework (arXiv:2604.20706).

## Core Methodology

QNNs face unique testing challenges due to stochastic measurement outcomes and complex quantum dynamics. Standard deterministic mutation killing does not apply.

### Statistical Mutation Killing

Quantum measurements are probabilistic — a mutant circuit may produce the "correct" output by chance. Use statistical hypothesis testing:

1. Run both original and mutant circuits N times (N >= 100 recommended)
2. Collect output distributions P_original and P_mutant
3. Apply statistical test (e.g., chi-squared, KL divergence with threshold)
4. Mutant is "killed" if distributions differ significantly (p < 0.05)

```python
import numpy as np
from scipy.stats import chisquare

def statistical_mutation_kill(original_counts, mutant_counts, alpha=0.05):
    """Test if mutant produces statistically different output."""
    total_orig = sum(original_counts.values())
    total_mut = sum(mutant_counts.values())
    # Normalize to same scale
    all_keys = set(original_counts) | set(mutant_counts)
    obs = [original_counts.get(k, 0.001) for k in all_keys]
    exp = [mutant_counts.get(k, 0.001) * total_orig / total_mut for k in all_keys]
    stat, p = chisquare(obs, exp)
    return p < alpha, p
```

### Mutation Operators (9 Types)

QuanForge defines operators at two levels:

**Gate-level mutations:**
- **Gate Insertion**: Add spurious single-qubit gates (X, Y, Z, H)
- **Gate Deletion**: Remove gates from the circuit
- **Gate Replacement**: Swap one gate type for another (e.g., H → X)
- **Gate Duplication**: Duplicate an existing gate

**Parameter-level mutations:**
- **Parameter Perturbation**: Add small noise θ' = θ + ε
- **Parameter Zeroing**: Set parameter to 0
- **Parameter Scaling**: Multiply parameter by factor k ≠ 1
- **Parameter Swap**: Exchange two rotation parameters
- **Parameter Negation**: θ → -θ

### Mutant Generation Algorithm

```python
def generate_mutants(circuit, operators, num_mutants=5):
    """Systematically generate mutants for QNN testing."""
    mutants = []
    for op in operators:
        for _ in range(num_mutants):
            mutant = circuit.copy()
            mutated = apply_operator(mutant, op)
            if mutated is not None:
                mutants.append((op, mutated))
    return mutants

def assess_vulnerability(mutation_results):
    """Identify circuit regions most prone to errors."""
    # Group by gate/parameter location
    region_kill_rates = {}
    for region, killed, total in mutation_results:
        if region not in region_kill_rates:
            region_kill_rates[region] = [0, 0]
        region_kill_rates[region][0] += killed
        region_kill_rates[region][1] += total
    
    return {r: k/t for r, (k, t) in region_kill_rates.items() if t > 0}
```

### Noisy Device Simulation

Evaluate testing framework under realistic noise:
- Apply depolarizing noise channels to gates
- Add measurement error (readout noise)
- Test if mutation operators remain distinguishable under noise
- Operators that survive noise simulation are most practically useful

## Workflow

1. **Prepare QNN**: Load trained quantum circuit
2. **Generate mutants**: Apply mutation operators
3. **Statistical testing**: Compare outputs with hypothesis testing
4. **Vulnerability localization**: Identify weak circuit regions
5. **Noise analysis**: Validate under simulated hardware noise

## Key Metrics

- **Mutation Score**: fraction of killed mutants / total mutants
- **Kill Rate by Operator**: effectiveness of each mutation type
- **Kill Rate by Region**: vulnerability map of circuit
- **Noise Resilience**: mutation score under different noise levels

## Application

Use this methodology to:
- Benchmark different QNN architectures for robustness
- Guide circuit simplification (remove redundant gates)
- Validate QNN implementations before hardware deployment
- Design targeted training data augmentation for weak regions

## Reference

- QuanForge: A Mutation Testing Framework for Quantum Neural Networks
  - Authors: Minqi Shao, Shangzhou Xia, Jianjun Zhao
  - arXiv: 2604.20706 (2026-04-22)
  - Categories: cs.SE, cs.AI
