---
name: quantum-computing-patterns
description: >
  Reusable patterns from quantum computing and quantum machine learning research.
  Covers distributed quantum computing, variational quantum algorithms, QML architectures,
  and quantum advantage verification. Use when analyzing quantum computing papers,
  designing quantum-classical hybrid systems, or researching quantum advantage in ML.
  Triggers: quantum computing, QML, variational quantum algorithm, distributed quantum,
  quantum advantage, quantum circuit routing, NISQ.
---

# Quantum Computing Patterns

Reusable patterns extracted from arXiv/Nature/Science quantum computing research.

## Pattern 1: Distributed Quantum Computing (DQC)

**Core idea:** Partition quantum computation across multiple NISQ devices.

### Key Techniques
1. **Matrix partitioning** - Split large linear systems Ax=b across quantum nodes
2. **Variational distributed algorithms** - Each node optimizes local parameters
3. **Low-loss interconnects** - Microwave/photonic links between quantum modules

### When to Use
- Problem size exceeds single NISQ device capacity
- Need modular scalability for fault-tolerant QC
- Multi-parameter quantum metrology tasks

## Pattern 2: Quantum Circuit Routing via RL

**Core idea:** Frame qubit routing as reinforcement learning problem.

### Key Techniques
1. **State-dependent networking** - Qubit placement depends on current circuit state
2. **Action-space engineering** - Design RL actions for qubit swap/placement
3. **Cross-module coordination** - Route qubits between DQC modules

### When to Use
- Distributed quantum circuit compilation
- NISQ device with limited qubit connectivity
- Dynamic qubit allocation across modules

## Pattern 3: Quantum-Classical Hybrid Neural Networks

**Core idea:** Combine quantum circuits with classical neural network layers.

### Key Techniques
1. **Quantum feature extraction** - Use quantum circuits as trainable feature maps
2. **Hybrid loss landscapes** - Joint optimization of quantum and classical parameters
3. **Quantum kernel methods** - Train quantum kernels with quantum neural networks

### When to Use
- Small quantum advantage on classical ML tasks
- Quantum-enhanced feature spaces
- Quantum reservoir computing

## Pattern 4: Variational Quantum Algorithms (VQA)

**Core idea:** Parameterized quantum circuits optimized via classical feedback loop.

### Key Techniques
1. **Parameterized ansatz** - Design circuit templates with tunable parameters
2. **Classical optimizer loop** - Use gradient-free optimizers (COBYLA, SPSA)
3. **Error mitigation** - Zero-noise extrapolation, probabilistic error cancellation

### When to Use
- NISQ-era quantum applications
- Quantum chemistry/optimization problems
- Quantum machine learning model training

## Pattern 5: Quantum Advantage Verification

**Core idea:** Demonstrate and verify quantum advantage over classical methods.

### Key Techniques
1. **Verifiable protocols** - Interactive proofs for quantum computations
2. **Blind quantum computing** - Client verifies without revealing computation
3. **Benchmark comparisons** - Compare with best classical algorithms

### When to Use
- Quantum supremacy/advantage claims
- Algorithm comparison studies
- Quantum computing capability assessment

## Key References
- arXiv:2604.01426 - Distributed Variational Quantum Linear Solver
- arXiv:2605.02389 - Action-Space Engineering for Quantum Circuit Routing
- arXiv:2602.00048 - Quantum Circuit-Based Learning Models
- Nature s41467-026-68535-9 - Distributed Multi-Parameter Quantum Metrology
- Science adu6894 - Universal Distributed Blind Quantum Computing
- arXiv:2505.23860 - Quantum Computing and AI: Status and Perspectives

## Session Research Logs
- See [references/session-2026-05-05.md](references/session-2026-05-05.md) for 2026-05-05 research findings, KG PageRank results, and emerging trend analysis.

## Tools Integration
- **kg_tool**: Import quantum papers, search knowledge graph
- **arxiv-search**: Search for latest quantum computing papers
- **web_search**: Find news and breakthrough announcements

## Verification Steps
1. Check arXiv for latest papers in quant-ph, cs.LG, cs.DC
2. Search knowledge graph for related papers
3. Verify claimed quantum advantage against classical baselines
4. Check if NISQ constraints are realistically addressed
