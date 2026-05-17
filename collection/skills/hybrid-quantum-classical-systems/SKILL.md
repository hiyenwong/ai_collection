---
name: hybrid-quantum-classical-systems
description: "Hybrid quantum-classical systems engineering skill for designing distributed quantum computing architectures, quantum error correction, and optimization workflows. Activates when discussing quantum-classical hybrid algorithms, distributed quantum systems, quantum error correction, or quantum system optimization."
---

# Hybrid Quantum-Classical Systems Engineering

Design and analysis of hybrid quantum-classical computing systems, combining quantum algorithms with classical distributed architectures.

## Activation Keywords

- hybrid quantum-classical
- distributed quantum computing
- quantum system design
- quantum error correction architecture
- 量子经典混合系统
- 分布式量子计算
- 量子系统架构
- 量子纠错设计

## Tools Used

- `exec`: Run simulations, scripts, quantum tools
- `read`: Load quantum research papers, reference materials
- `write`: Generate architecture diagrams, specifications
- `sqlite3`: Query knowledge graph for related papers

## Key Concepts

### Hybrid Architecture Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Dataflow** | Graph-based quantum-classical workflows | Long-running hybrid algorithms |
| **Remote Execution** | Cloud/distributed quantum access | Resource-constrained environments |
| **Error Mitigation** | Classical post-processing for quantum errors | NISQ-era devices |
| **Optimization Loops** | Classical optimizer + quantum evaluator | VQE, QAOA |

### Quantum Error Correction

| Code Type | Description | Threshold |
|-----------|-------------|-----------|
| Surface codes | 2D topological codes | ~1% |
| Color codes | 3D topological codes | ~0.1% |
| Bacon-Shor | Subsystem codes | ~0.5% |

### System Design Checklist

1. **Quantum Resource Estimation**
   - Qubit count requirements
   - Gate depth analysis
   - Coherence time constraints

2. **Classical Infrastructure**
   - Control system latency
   - Data bandwidth needs
   - Error correction processing

3. **Hybrid Integration**
   - Communication protocols
   - Synchronization requirements
   - Fault tolerance mechanisms

## Usage Patterns

### Pattern 1: Architecture Design

```
设计一个混合量子-经典系统用于 [应用场景]
```

Agent workflow:
1. Analyze problem requirements
2. Estimate quantum resource needs
3. Design classical control architecture
4. Specify integration protocols
5. Evaluate fault tolerance requirements

### Pattern 2: Error Correction Planning

```
为 [量子算法] 设计纠错架构
```

Agent workflow:
1. Identify error sources
2. Select appropriate QEC code
3. Calculate resource overhead
4. Design classical decoder
5. Estimate fault-tolerant threshold

### Pattern 3: Distributed System Analysis

```
分析分布式量子计算系统的 [指标]
```

Agent workflow:
1. Query kg.db for relevant papers
2. Analyze communication costs
3. Evaluate latency constraints
4. Compare architecture alternatives

## Instructions for Agents

### Step 1: Problem Analysis

Understand the quantum-classical hybrid requirements:
- Application domain (chemistry, optimization, ML)
- Quantum backend constraints (qubit count, connectivity)
- Classical infrastructure capabilities
- Performance targets

### Step 2: Architecture Selection

Choose appropriate hybrid pattern based on:
- Algorithm type (variational, measurement-based, etc.)
- Quantum resource availability
- Communication bandwidth and latency
- Error mitigation/correction needs

### Step 3: Resource Estimation

Calculate quantum resources:
- Logical qubit requirements
- Physical qubit overhead (with QEC)
- Gate depth and circuit width
- Coherence time requirements

### Step 4: Classical Integration Design

Specify classical components:
- Control systems and feedback loops
- Error correction decoders
- Data processing pipelines
- Communication protocols

### Step 5: Validation

Verify design feasibility:
- Resource constraints check
- Latency analysis
- Fault tolerance assessment
- Cost estimation

## Knowledge Graph Queries

Use kg.db to find related research:

```bash
# Find quantum computing papers
kg_tool search kg.db "quantum computing"

# Find distributed systems papers
kg_tool search kg.db "distributed systems"

# Find quantum error correction papers
kg_tool search kg.db "quantum error correction"

# Find similar entities
kg_tool similar kg.db [entity_id] 5
```

## Key Research Papers

From PageRank analysis of kg.db:

| Paper | Focus | Relevance |
|-------|-------|-----------|
| Tierkreis: Dataflow Framework | Hybrid workflows | High |
| Quantum error correction beyond qubits | QEC architecture | High |
| On the Limits of Distributed Quantum | Distributed limits | Medium |
| MMC Topology Optimization | System optimization | Medium |

## References

- Nielsen & Chuang: Quantum Computation and Quantum Information
- Preskill: Quantum Computing in the NISQ era
- Fowler et al.: Surface codes: Towards practical large-scale quantum computation

## Related Skills

- `quantum-algorithms`: Quantum algorithm design
- `distributed-systems`: Classical distributed systems
- `system-optimization`: General optimization techniques

## Notes

- Focus on practical NISQ-era constraints
- Consider both error mitigation and correction
- Balance quantum and classical resource allocation
- Account for communication overhead in distributed settings

## Examples

### Example 1: Using this skill
```
User: [Request related to this skill's domain]
Agent: [Applies skill knowledge to help user]
```
