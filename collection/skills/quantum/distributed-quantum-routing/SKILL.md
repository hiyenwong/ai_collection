---
name: distributed-quantum-routing
description: "Routing and compilation methodology for distributed quantum computers (DQCs). Covers SABRE-style routing, teleportation-based scheduling, and EPR pair optimization across multi-core quantum processors."
category: quantum
---

# Distributed Quantum Computing Routing & Compilation

## Description
System-level methodologies for distributed quantum computing (DQC) including qubit routing, circuit scheduling, and EPR pair consumption optimization. Based on arXiv:2605.21960v1 (dSABRE) and arXiv:2605.21795v1 (ATHENA).

## Activation Keywords
- distributed quantum routing
- dSABRE router
- ATHENA compiler
- quantum circuit allocation
- EPR consumption optimization
- multi-core quantum computer
- 分布式量子路由
- 量子电路调度
- quantum interconnect routing

## Core Concepts

### Distributed Quantum Computing Architecture
- **Multi-core processors**: Connect smaller quantum chips via photonic interconnects
- **Teleportation-based gates**: Execute remote CNOTs using pre-shared EPR pairs
- **EPR pair management**: Minimize EPR consumption (dominant cost in DQC routing)
- **SWAP vs teleportation trade-off**: Local SWAPs vs remote entanglement

### dSABRE Routing (arXiv:2605.21960v1)
- **SABRE-style heuristic**: Greedy routing adapted for distributed architecture
- **Lookahead window**: Consider future gate dependencies for routing decisions
- **EPR minimization**: Primary objective is reducing entanglement resource usage
- **Multi-core topology**: Route across heterogeneous processor layouts

### ATHENA Scheduling (arXiv:2605.21795v1)
- **Compiler-optimized scheduling**: Co-ordinate qubit movement and gate execution
- **Teleportation-aware**: Account for latency and success probability of entanglement
- **Circuit partitioning**: Divide circuits for distributed execution
- **Resource allocation**: Balance EPR consumption, execution time, fidelity

## Usage Patterns

### Pattern 1: DQC Circuit Routing
Route a quantum circuit onto distributed hardware:
1. Parse circuit and hardware topology
2. Initialize qubit placement (heuristic or optimized)
3. For each gate:
   a. If local: execute directly
   b. If remote: evaluate SWAP vs teleportation cost
   c. Choose routing strategy minimizing total EPR consumption
4. Output: scheduled circuit with routing decisions

### Pattern 2: EPR Budget Optimization
Given limited EPR pairs, optimize circuit execution:
1. Analyze circuit's non-local gate requirements
2. Prioritize gates by critical path length
3. Schedule teleportations to minimize peak EPR usage
4. Insert SWAPs when EPR budget exceeded

### Pattern 3: RL-Based Allocation (SQARL - arXiv:2605.27027v1)
Use size-agnostic RL for circuit allocation:
1. Train policy on diverse circuit sizes
2. State: circuit structure + hardware topology
3. Action: qubit-to-processor assignment
4. Reward: minimize EPR consumption + execution time
5. Deploy for online allocation on new circuits

## Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| EPR consumption | Total entanglement pairs used | Minimize |
| Circuit depth | Number of sequential layers | Minimize |
| Fidelity | End-to-end gate fidelity | Maximize |
| Routing overhead | Extra operations from routing | < 2x original |

## Error Handling

### EPR Exhaustion
- Fall back to SWAP-based routing
- Split circuit into smaller sub-circuits
- Reduce parallelism to conserve EPR pairs

### Routing Failure
- If no valid path: relax constraints, allow lower-fidelity gates
- If timeout: use greedy heuristic instead of optimization
- If circuit too large: partition and execute sequentially

## Implementation Considerations

### Topology Abstraction
- Model DQC as graph: nodes = qubits, edges = connectivity + EPR links
- Weight edges by: SWAP cost, EPR cost, fidelity
- Use graph algorithms for initial placement

### Scheduling Constraints
- Respect gate dependencies (DAG ordering)
- Account for EPR generation latency
- Handle probabilistic entanglement (retry on failure)

## Resources
- arXiv:2605.21960v1 - dSABRE: SABRE-Style Router for Multi-Core DQCs
- arXiv:2605.21795v1 - ATHENA: Compiler For Optimized Scheduling in DQCs
- arXiv:2605.27027v1 - SQARL: Size-Agnostic RL for Circuit Allocation
