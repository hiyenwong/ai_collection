# QGNSA Implementation Notes (arXiv:2605.22527)

## Paper Details
- **Title:** Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- **Authors:** Giancarlo P. Gamberi, Calebe P. Bianchini
- **Published:** 2026-05-22
- **Dataset:** Metaverse Financial Transactions Dataset

## QGA Core Algorithm

### Qubit Chromosome Representation
Each chromosome is a string of n qubits, where each qubit is:
```
|ψ⟩ = α|0⟩ + β|1⟩, where |α|² + |β|² = 1
```

Initialize with α = β = 1/√2 (uniform superposition — maximal exploration).

### Quantum Rotation Gate
```
[α']   [cos(Δθ)  -sin(Δθ)] [α]
[β'] = [sin(Δθ)   cos(Δθ)] [β]
```

Δθ lookup table (from fitness comparison):
| Current bit | Best bit | f(current) < f(best) | Δθ |
|------------|----------|----------------------|-----|
| 0 | 0 | No | 0 |
| 0 | 0 | Yes | 0.01π |
| 0 | 1 | No | 0.02π |
| 0 | 1 | Yes | 0.05π |
| 1 | 0 | No | 0.02π |
| 1 | 0 | Yes | 0.05π |
| 1 | 1 | No | 0 |
| 1 | 1 | Yes | 0.01π |

### Measurement
Collapse qubit chromosome to binary string by sampling: bit=0 with prob |α|², bit=1 with prob |β|².

### Negative Selection Integration
1. Generate detector candidates via measurement
2. Filter: remove detectors that match any "self" pattern
3. Score remaining detectors on anomaly detection accuracy
4. Best detector guides rotation gate updates
5. Repeat until convergence or max iterations

## Key Results
- Superior anomaly detection accuracy vs classical EvoSeedRNSA
- More robust under varying hyperparameter configurations
- O(n) space complexity for 2^n candidate states

## Implementation Tips
- Start with uniform superposition for maximum diversity
- Use small rotation steps (0.01-0.05π) for stable convergence
- Multiple measurements per chromosome improve diversity
- Can deploy on NISQ hardware or classical simulation
- Future work: hybrid quantum-classical approaches for computational efficiency
