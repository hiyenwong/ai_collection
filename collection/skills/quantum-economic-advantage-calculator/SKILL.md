---
name: quantum-economic-advantage-calculator
description: "Framework for calculating quantum economic advantage timing — determines when quantum systems outperform classical computers on cost-equivalent basis for specific algorithms, incorporating error correction overhead, gate speeds, connectivity, and hardware roadmaps."
---

# Quantum Economic Advantage Calculator

## Description
Methodology for systematically calculating when quantum computers will achieve economic advantage over classical systems for specific algorithmic problems. Economic advantage means outperforming on a cost-equivalent basis, not just raw speed. Framework incorporates error correction overhead, gate speeds, qubit connectivity, and hardware roadmap assumptions.

## Activation Keywords
- quantum economic advantage
- 量子经济优势
- quantum advantage timing
- advantage calculator
- when quantum advantage
- cost-equivalent quantum
- quantum vs classical timing
- 量子优势时间预测
- quantum hardware roadmap

## Tools Used
- exec: Run advantage calculation models, numerical simulations
- write_file: Create advantage assessment reports
- read_file: Read hardware roadmap specifications
- web_search: Find latest quantum hardware specifications

## Core Framework

### Economic Advantage vs Technical Advantage

| Aspect | Technical Advantage | Economic Advantage |
|--------|-------------------|-------------------|
| Definition | Quantum solves faster | Quantum solves cheaper |
| Metric | Time to solution | Cost per solution |
| Factors | Qubit count, depth | Error correction, cloud costs, electricity |
| Timing | Earlier | Later (more conservative) |

### Key Variables

1. **Algorithm Parameters**:
   - Logical qubits required
   - Circuit depth (T-gate count)
   - Error rate tolerance

2. **Hardware Parameters**:
   - Physical qubit count
   - Gate speed (ns)
   - Gate fidelity
   - Connectivity (all-to-all vs nearest neighbor)

3. **Error Correction Parameters**:
   - Code distance
   - Overhead ratio (physical:logical)
   - Decoding latency

4. **Economic Parameters**:
   - Quantum cloud cost ($/hour)
   - Classical compute cost
   - Time value of computation

## Usage Patterns

### Pattern 1: Advantage Timing Estimation
When evaluating whether to invest in quantum vs classical:
1. Specify the algorithm and its quantum resource requirements
2. Define hardware assumptions (gate speed, fidelity, connectivity)
3. Set economic parameters (compute costs)
4. Calculate break-even timeline under different hardware roadmaps
5. Identify sensitivity to each parameter

### Pattern 2: Robustness Analysis
When determining how reliable an advantage prediction is:
1. Vary each technical parameter independently
2. Classify timing as "robust" (insensitive to assumptions) or "contingent" (highly sensitive)
3. Shor's algorithm: typically robust timing
4. Grover's algorithm: typically contingent timing
5. Report parameter ranges for advantage window

### Pattern 3: Hardware Roadmap Comparison
When comparing quantum hardware platforms:
1. Define identical algorithmic problem
2. Apply each platform's specifications
3. Calculate advantage timeline for each
4. Identify which parameters most affect the result
5. Generate sensitivity tornado chart

## Instructions for Agents

### Step 1: Define the Problem
```
Problem: {algorithm_name}
Classical complexity: O(f(n))
Quantum complexity: O(g(n))
Input size: n = {value}
Classical baseline: {time/cost on best classical}
```

### Step 2: Gather Hardware Assumptions
```
Physical qubits: {current} → {projected_year}
Gate speed: {ns}
Gate fidelity: {1-error_rate}
Error correction overhead: {physical_per_logical}x
```

### Step 3: Calculate Advantage Timing
```
For each year Y:
  projected_qubits(Y) = f(roadmap)
  projected_fidelity(Y) = f(improvement_rate)
  logical_qubits_available(Y) = projected_qubits(Y) / overhead
  time_to_solve_quantum(Y) = quantum_complexity / gate_speed
  cost_quantum(Y) = time * cloud_rate
  if cost_quantum(Y) < cost_classical:
    advantage_year = Y
    break
```

### Step 4: Sensitivity Analysis
```
For each parameter P:
  P_low = P * 0.5
  P_high = P * 2.0
  advantage_year_low = calculate(P_low)
  advantage_year_high = calculate(P_high)
  sensitivity = advantage_year_high - advantage_year_low
```

## Error Handling

### Insufficient Hardware Data
If hardware specs are unknown:
- Use conservative estimates from published roadmaps
- Cite sources (IBM, Google, IonQ, etc.)
- Report ranges instead of point estimates

### Algorithm Complexity Unknown
If quantum algorithm complexity is debated:
- Report multiple estimates
- Use best-case and worst-case scenarios
- Flag as "contingent" prediction

## Resources
- arXiv: 2508.21031 — Introducing the Quantum Economic Advantage Online Calculator
- Choi, Moses, Thompson (2023) — Quantum advantage framework
- https://futuretech.mit.edu/quantum-economic-advantage-calculator

## Related Skills
- quantum-finance-stack-analysis — Financial computation evaluation
- qbalance-quantum-workflow-optimization — NISQ workflow optimization
- quantum-fault-tolerance-benchmark — FTQC code evaluation
