---
name: quantum-ai-patterns
description: >
  Reusable research patterns at the intersection of quantum computing and artificial intelligence.
  Use when analyzing quantum machine learning papers, designing hybrid quantum-classical systems,
  or extracting architectural patterns from quantum-AI research. Covers QNN design, distributed
  quantum computing, AI-assisted error correction, and continuous-time quantum models.
  Triggers: quantum machine learning, QNN, quantum neural network, hybrid quantum-classical,
  quantum AI patterns, distributed quantum computing, quantum error correction AI.
---

# Quantum-AI Research Patterns

Reusable patterns extracted from analyzing quantum computing + AI research papers.

## Pattern 1: Quantum-Classical Hybrid Architecture

Hybrid systems where quantum processors handle specific subroutines while classical systems manage orchestration.

**When to use**: Problems with separable quantum-suitable and classical-suitable subproblems.

**Architecture**:
```
Classical Controller → Quantum Subroutine → Classical Post-processing
     ↓                      ↓                      ↓
  Control flow          Linear algebra          I/O, display
  Optimization loop     Sampling/estimation     Decision logic
```

**Key principle**: Decompose problems into:
- **Quantum-suitable**: Linear algebra, optimization, sampling, Fourier transforms
- **Classical-suitable**: Control flow, I/O, preprocessing, decision logic

**Examples**: VQE (Variational Quantum Eigensolver), QAOA, quantum kernel methods

## Pattern 2: Distributed Quantum Resource Management

Managing limited qubit resources across multiple quantum processing nodes.

**When to use**: Computation exceeds single-device qubit capacity.

**Key techniques**:
- Circuit cutting: partition quantum circuits across devices
- Quantum teleportation: inter-node quantum state transfer
- Classical communication: coordinate distributed quantum operations
- Error-aware scheduling: account for varying noise profiles across nodes

**Key principle**: When resources are constrained, distribute computation with explicit communication protocols.

## Pattern 3: Error-Corrected Learning

Using machine learning to optimize quantum error correction and vice versa.

**When to use**: Quantum systems with noisy operations requiring adaptive error management.

**Bidirectional benefits**:
- **AI → QEC**: Neural decoders for syndrome measurement, adaptive threshold optimization
- **QEC → AI**: Quantum-enhanced feature spaces, noise-robust training

**Key principle**: Use ML to optimize system-level parameters traditionally hand-tuned (error correction thresholds, scheduling, gate calibration).

## Pattern 4: Continuous-Time Quantum Models

Continuous-time formulations bridging differential equations and quantum computing.

**When to use**: Modeling dynamical systems, time-series analysis, recurrent architectures.

**Key models**:
- CTRQNets (Continuous-Time Recurrent Quantum Networks)
- LQNets (Liquid Quantum Networks)
- Quantum neural ODEs

**Key principle**: Continuous-time models provide more natural representations for dynamical systems than discrete-time approximations.

## Search Queries for Paper Discovery

Effective arXiv search patterns:
- `cat:quant-ph AND cat:cs.LG` — Quantum ML papers
- `all:"quantum neural network"` — QNN papers
- `all:"distributed quantum"` — Distributed QC papers
- `all:"variational quantum"` — VQA/VQE papers
- `all:"quantum error correction" AND all:"machine learning"` — AI-assisted QEC

## Knowledge Graph Integration

When importing papers into kg.db:
1. Categorize by primary domain: `quant-ph`, `cs.LG`, `cs.AI`, `cs.CV`
2. Tag cross-domain papers with multiple categories (e.g., `quant-ph, cs.LG`)
3. Use PageRank to identify foundational papers in the intersection field
4. Community detection reveals research clusters (typically: QML, QEC, QNN, Distributed QC)
