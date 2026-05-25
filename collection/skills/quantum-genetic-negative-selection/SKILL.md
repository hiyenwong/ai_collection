---
name: quantum-genetic-negative-selection
description: >
  Quantum Genetic Negative Selection Algorithm (QGNSA) methodology. Integrates Quantum Genetic Algorithm (QGA) 
  into negative selection algorithms for anomaly detection. Uses quantum superposition (qubit representation) 
  and probabilistic amplitude adjustment (rotation gates) to enhance search space exploration and convergence 
  efficiency in detector generation. Use when optimizing anomaly detectors, implementing artificial immune systems 
  with quantum computing, applying QGA to combinatorial search problems, or hybrid quantum-classical optimization 
  for cybersecurity/finance anomaly detection. Triggers: quantum genetic algorithm, negative selection, anomaly 
  detection, artificial immune system quantum, quantum-inspired optimization, QGA, QGNSA, 量子遗传, 阴性选择算法.
---

# Quantum Genetic Negative Selection Algorithm (QGNSA)

Integrate Quantum Genetic Algorithm (QGA) into negative selection algorithms for improved anomaly detection via quantum superposition-based search.

## Core Methodology

### Qubit Encoding
Represent detector candidates as qubit chromosomes. Each gene is a qubit pair `[alpha, beta]` where `|alpha|^2 + |beta|^2 = 1`. Probability amplitudes encode superposition of 0/1 states.

### Quantum Rotation Gate Update
Update qubit states via rotation matrix:
```
[alpha_new]   [cos(dtheta)  -sin(dtheta)] [alpha_old]
[beta_new]  = [sin(dtheta)   cos(dtheta)] [beta_old]
```

`dtheta` is determined by comparing current fitness vs. best solution — rotate toward better states.

### Measurement-Collapse
Measure qubit chromosome to collapse to binary string (detector candidate). Multiple measurements give diverse candidates from same quantum state.

### Negative Selection Loop
1. Initialize qubit population with uniform superposition (alpha=beta=1/sqrt(2))
2. Measure to generate binary detector candidates
3. Evaluate: candidates must NOT match any "self" patterns
4. Score non-self detectors by anomaly detection accuracy
5. Apply quantum rotation gates guided by fitness
6. Repeat until convergence

## Usage Patterns

### Pattern 1: QGNSA for Anomaly Detection
Use QGA to optimize detector generation in negative selection algorithms. Replaces classical genetic algorithm in EvoSeedRNSA with quantum-enhanced search.

### Pattern 2: Quantum Superposition for Search Diversity
Leverage quantum superposition to maintain population diversity — single qubit chromosome encodes exponential candidate space.

### Pattern 3: Amplitude Adjustment for Convergence
Use rotation gate angle to control exploration vs. exploitation. Large angles = exploration, small angles = convergence.

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Population size | 40-100 | Qubit chromosomes |
| Rotation step | 0.01-0.05*pi | Max dtheta per iteration |
| Self tolerance | domain-specific | Detector non-self threshold |
| Measurement count | 1-2 per chromosome | Samples per iteration |

## Implementation Notes

- Qubit representation gives O(n) space for 2^n candidate states
- Rotation gate replaces classical crossover/mutation
- Works on NISQ hardware or classical simulation
- Evaluated on Metaverse Financial Transactions Dataset — superior to classical GA
- Future: deploy on real quantum hardware, hybrid quantum-classical approaches

## Related Skills

- `quantum-genetic-algorithm` (general QGA patterns)
- `quantum-negative-selection` (negative selection in quantum domain)
- `anomaly-detection` (classical anomaly detection methods)

## References

- arXiv:2605.22527 — "Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection"
