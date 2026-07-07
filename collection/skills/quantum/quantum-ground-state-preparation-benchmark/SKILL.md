---
name: quantum-ground-state-preparation-benchmark
description: "Benchmark methodology for comparing quantum ground state preparation algorithms (cooling, adiabatic, QAOA) under realistic noise conditions. Provides phase-dependent performance analysis using quadratic fermionic Hamiltonians with depolarizing noise."
---

# Quantum Ground State Preparation Benchmark

## Description
Benchmark methodology for comparing quantum ground state preparation algorithms under realistic noise conditions. Based on arXiv:2606.20551 (Molpeceres et al., 2026), which derives scaling laws for achievable relative energy as a function of noise rate across cooling, adiabatic, and optimization algorithms. Key finding: algorithm performance depends critically on the quantum phase — adiabatic evolution dominates in the trivial phase while multi-frequency cooling is superior in the topological phase where gap-closing limits adiabatic protocols.

## Activation Keywords
- ground state preparation benchmark
- quantum algorithm benchmark noise
- 量子基态制备基准
- cooling vs adiabatic vs QAOA
- quantum phase transition benchmark
- noisy quantum state preparation
- multi-frequency cooling algorithm
- depolarizing noise benchmark

## Tools Used
- terminal: Run numerical simulations of quantum algorithms
- write_file: Create benchmark scripts and analysis code
- skill_view: Reference related quantum algorithm skills

## Core Framework

### 1. Algorithm Categories
| Algorithm | Best Phase | Noise Robustness | Key Advantage |
|-----------|-----------|-----------------|---------------|
| Adiabatic Evolution | Trivial | Moderate | Conceptual simplicity |
| Multi-Frequency Cooling | Topological | High | Gap-closing resilience |
| QAOA | Trivial | Low-Moderate | Competitive with cooling in trivial phase |

### 2. Benchmark Protocol

**Step 1: Define Hamiltonian Family**
- Use exactly solvable quadratic fermionic Hamiltonians
- Include a quantum phase transition (trivial vs topological phases)
- Parameterize by gap size and system size

**Step 2: Model Noise**
- Apply depolarizing noise at varying rates (p)
- Track noise rate as primary parameter
- Include parameter imperfections for robustness testing

**Step 3: Run Each Algorithm**
- Adiabatic: Vary evolution time, measure energy vs noise
- Cooling: Multi-frequency protocol, compare with single-frequency baseline
- QAOA: Optimize angles, compare with cooling performance

**Step 4: Evaluate Metrics**
- Achievable relative energy: (E_achieved - E_ground) / E_ground
- Scaling with noise rate: fit energy vs p curves
- Robustness to parameter imperfections
- Phase-dependent performance crossover points

### 3. Phase-Dependent Analysis
The critical insight: performance depends on the quantum phase:
- **Trivial phase**: Adiabatic evolution is favorable; QAOA competitive with cooling
- **Topological phase**: Multi-frequency cooling superior (gap-closing limits adiabatic)
- **Near phase transition**: All algorithms degrade; cooling shows most graceful degradation

### 4. Noise Scaling Laws
For quadratic fermionic models with depolarizing noise:
- Derive analytical scaling of achievable energy as function of noise rate
- Validate with numerical simulations
- Identify noise thresholds below which each algorithm is viable

### 5. Robustness to Parameter Imperfections
- Cooling protocol shows enhanced robustness to parameter imperfections
- This is critical for realistic NISQ-era implementations
- Test by varying Hamiltonian parameters ±10% and measuring energy degradation

## Usage Patterns

### Pattern 1: Benchmark New Ground State Algorithm
1. Implement the algorithm on the standard quadratic fermionic Hamiltonian family
2. Test across both trivial and topological phases
3. Compare against the three baselines (adiabatic, cooling, QAOA)
4. Report phase-dependent performance, not just average

### Pattern 2: Noise-Aware Algorithm Selection
1. Estimate the noise rate of your quantum hardware
2. Identify the phase of your target Hamiltonian
3. Select algorithm based on the phase-noise performance map:
   - Low noise + trivial phase → adiabatic
   - Any noise + topological phase → multi-frequency cooling
   - Moderate noise + trivial phase → QAOA or cooling

### Pattern 3: Extend to New Model Classes
1. Verify the model is exactly solvable (or has known ground state)
2. Identify phase transitions and their nature
3. Apply the same benchmark protocol
4. Compare scaling laws with the fermionic baseline

## Error Handling
### Algorithm Fails in Topological Phase
- This is expected for adiabatic protocols (gap-closing)
- Switch to multi-frequency cooling
- Report the phase-dependent performance honestly

### Noise Rate Too High
- All algorithms will fail to reach ground state
- Report the noise threshold for each algorithm
- Consider error mitigation strategies before benchmarking

## Resources
- arXiv:2606.20551: "Benchmark of quantum algorithms for ground state preparation in the presence of noise" (Molpeceres, Lu, Cirac, Kraus, 2026)
