# Empirical Comparison Framework: Quantum Simulation vs Learning

## Core Thesis

Classical simulation and sample-based learning both aim to reproduce Born-rule statistics, but **simulability ≠ learnability**. This was empirically demonstrated in arXiv:2605.28986.

## Complexity Classes Observed

### Hard-to-Simulate but Learnable
- Random quantum circuits beyond classical simulation threshold
- Yet efficiently learnable from O(poly(n)) measurement samples
- Implication: quantum advantage claims based solely on simulation hardness are incomplete

### Simulable but Hard-to-Learn
- Structured quantum systems with known classical descriptions
- Sample complexity may be exponential despite efficient simulability
- Example: certain Clifford + T circuits

### Both Easy
- Clifford circuits: efficiently simulable (Gottesman-Knill) AND learnable
- Stabilizer states: both approaches polynomial

### Both Hard
- Generic quantum systems: both simulation and learning are intractable

## Empirical Methodology

### Metrics to Track
1. **Wall-clock time** for simulation vs learning
2. **Sample complexity** for learning approach
3. **Memory requirements** for both approaches
4. **Accuracy** (KL divergence from true distribution)
5. **Scaling behavior** with system size

### Typical Experimental Setup
- System sizes: n = 4, 8, 16, 32 qubits
- Circuit depths: d = 10, 50, 100, 500
- Noise levels: 0%, 0.1%, 1%, 10%
- Number of samples: 10², 10³, 10⁴, 10⁵

## Related Work

- arXiv:2605.28986 (2026-05-27): First empirical comparison
- Quantum supremacy experiments (Google Sycamore, 2019)
- Classical simulation benchmarks (tensor network methods)
- Shadow tomography (Huang, Kueng, Preskill, 2020)

## Activation

- quantum simulation vs learning comparison
- simulability learnability gap
- Born-rule statistics benchmark
- quantum advantage verification methodology
