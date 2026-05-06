---
name: quantum-neuroscience-patterns
description: Reusable patterns for quantum-inspired neuroscience research. Extracts methodologies from papers combining quantum computing/mechanics with neuroscience, brain-inspired AI, and cognitive modeling. Use when researching quantum neural networks, quantum-like cognition models, brain-inspired quantum architectures, or neuro-quantum interfaces.
---

# Quantum-Neuroscience Research Patterns

## Overview

This skill captures reusable methodological patterns from research at the intersection of quantum computing and neuroscience, based on analysis of recent arXiv papers (2024-2026).

## Key Research Patterns

### Pattern 1: Quantum-Like Cognition Modeling (QL)

**Core idea**: Apply quantum probability theory (not quantum physics) to model cognitive phenomena that classical probability cannot explain.

**When to use**: Research shows order effects, conjunction fallacies, decision interference, or response replicability in human cognition.

**Methodology**:
- Use Generalized Probability Theory (GPT) with ordered linear state spaces instead of complex Hilbert spaces
- Model neuronal networks as weighted directed graphs
- Encode weight matrices within GPT framework
- Incorporate effect observables and state updates via measurement instruments
- Key effects reproduced: order effects, non-repeatability, disjunction effects (decision interference)

**Papers**: Khrennikov et al. (2411.00036, 2506.00040)

### Pattern 2: Stochastic Quantum Neural Networks (SQNN)

**Core idea**: Combine stochastic differential equations (biological neuronal processes) with quantum evolution (superposition, entanglement, unitary evolution).

**When to use**: Building neuro-quantum models of the brain that go beyond von Neumann architecture limitations.

**Methodology**:
- Qubits evolve via stochastic differential equations inspired by biological neurons
- Incorporate random fluctuations of neuronal processing within quantum framework
- Address decoherence and qubit stability as key challenges
- Mathematical formalization of QNNS with biological grounding

**Paper**: Filardo & Heckmann (2511.11609)

### Pattern 3: Quantum Neural Network Robustness Framework

**Core idea**: Integrated approach to QNN efficiency, security, and privacy in the NISQ era.

**When to use**: Developing reliable quantum neural networks for real-world applications.

**Methodology**:
- Efficient parameter initialization to mitigate barren plateaus
- Residual quantum circuit connections for error propagation control
- Systematic quantum architecture exploration
- Defensive mechanisms against adversarial attacks
- Quantum Federated Learning (QFL) for privacy-preserving distributed training

**Paper**: Innan et al. (2507.20537)

### Pattern 4: Higher-Order Brain Network Analysis via Combinatorial Complexes

**Core idea**: Move beyond pairwise graph representations to capture higher-order neural interactions (3+ node dependencies).

**When to use**: Analyzing fMRI or neural data where pairwise connectivity misses critical group interactions.

**Methodology**:
- Construct combinatorial complexes (CCs) from fMRI time series
- Use information-theoretic measures for higher-order dependencies
- Bridge topological deep learning with network neuroscience
- Key insight: graph-based representations systematically miss higher-order dependencies

**Paper**: Shankar et al. (2511.20692)

### Pattern 5: Neural Brain Framework for Embodied Agents

**Core idea**: Biologically-inspired architecture for autonomous agents integrating perception, cognition, and action.

**When to use**: Building embodied AI systems that need human-like adaptability in unstructured environments.

**Components**:
1. Multimodal active sensing
2. Perception-cognition-action function
3. Neuroplasticity-based memory storage and updating
4. Neuromorphic hardware/software optimization

**Key challenges**:
- Integrating spiking dynamics with foundation models
- Maintaining lifelong plasticity without catastrophic forgetting
- Unifying language with sensorimotor learning
- Ethical safeguards in autonomous systems

**Paper**: Liu et al. (2505.07634)

## Skill Extraction Templates

### For New Paper Analysis

When analyzing a new quantum-neuroscience paper:

1. **Identify the intersection type**:
   - Quantum computing applied to brain data analysis
   - Quantum-like mathematical models for cognition
   - Brain-inspired quantum algorithms
   - Physical quantum-neural interfaces

2. **Extract methodology**:
   - What quantum concepts are borrowed? (superposition, entanglement, interference, measurement)
   - What neuroscience concepts are modeled? (neural oscillations, synaptic plasticity, memory)
   - How are they coupled? (mathematical formalism, hardware implementation, simulation)

3. **Identify reusable patterns**:
   - Can the mathematical framework be generalized?
   - Are there implementation challenges common across papers?
   - What validation methods are used?

### For Skill Creation from Papers

When creating a new skill from a quantum-neuroscience paper:

1. **Skill name**: `<domain>-<technique>-<application>` (e.g., `quantum-neural-decoding`)
2. **Trigger keywords**: Include both quantum terms and neuroscience terms
3. **Core workflow**: Paper's main methodology as numbered steps
4. **Validation**: How to verify the approach works (benchmarks, datasets, metrics)

## Research Clusters (from KG Analysis)

Based on knowledge graph analysis (2026-05-04):

| Cluster | Papers | Key Topics |
|---------|--------|------------|
| quant-ph | 13 | Quantum algorithms, QEC, QNN, quantum advantage |
| cs.AI | 4 | Brain-inspired AI, neuroscience foundations |
| q-bio.NC | 2 | Computational neuroscience, neurocybernetics |
| cs.CV | 4 | Quantum vision, brain-computer vision |

## Important Papers (by PageRank)

From the knowledge graph PageRank analysis:
- [16] Mapping the Mind of a Large Language Model (Anthropic)
- [59] Stochastic Quantum Neural Network Model for AI
- [1] Architecting Early Fault Tolerant Neutral Atoms Systems
- [28] Brain-Inspired Paradigm for Scalable Quantum Vision
- [25] Brain-Inspired Quantum Neural Architectures

## Research Workflow

When conducting neuro-quantum research:

1. **Search arXiv** via proxy (http://127.0.0.1:7890) — direct connections timeout from sandbox
   - Categories: `quant-ph` + `q-bio.NC`, `quant-ph` + `cs.LG`, `q-bio.NC` + `cs.AI`
   - Use `httpx.Proxy` with 5+ second delays between requests
2. **Import to kg.db** using `scripts/import_to_kg.py` or `scripts/import_new_papers.py`
   - Check duplicates against existing URLs before inserting
   - Generate 128-dim deterministic hash-based vectors
   - Create category-based relationships (weight = overlap/max)
3. **Analyze** with `scripts/kg_analysis.py` (Python fallback — kg_tool has limited commands)
   - Vector similarity search, PageRank, category-based community detection
4. **Extract patterns** using this skill's pattern templates above
5. **Record** in `memory/YYYY-MM-DD.md`

### Common Pitfalls
- kg_tool binary commands: `import-paper`, `generate-embeddings`, `search`, `pagerank`, `communities`, `stats`. Commands like `vector`, `embed`, `import`, `community`, `louvain`, `analyze` are NOT supported. Always fall back to Python scripts for full analysis.
- kg_vectors stores vectors as BLOB (binary), not JSON. When reading vectors in Python, use `bytes` handling, not `json.loads()` directly. New vectors should be stored as JSON-encoded bytes.
- kg_entities has UNIQUE constraint on `url` column — check existing URLs before inserting.
- execute_code sandbox cannot reach arxiv.org directly — must use terminal tool with proxy (`http://127.0.0.1:7890`).
- arXiv API requires HTTPS (`https://export.arxiv.org/api/query`), not HTTP. HTTP returns 301 redirect.
- Weekly topic schedule: Mon=Neuroscience, Tue=CS, Wed=Medicine, Thu=Systems Engineering, Fri=Math/Stats/Number Theory, Sat=Economics/Investing, Sun=Informatics. Daily quantum mechanics always included.

## Resources

- kg.db: Knowledge graph with 67 entities (vectors, relations, PageRank)
- scripts/kg_analysis.py: Vector similarity search and community detection
- scripts/weekly_topics.py: Daily/weekly research topic management
