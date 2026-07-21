---
name: neuro-quantum-research
description: >
  Research methodology for the intersection of neuroscience and quantum physics/computing.
  Use when analyzing papers or research at the boundary of brain science and quantum mechanics,
  including quantum neural networks, quantum memory models of cognition, quantum-inspired
  brain simulation, quantum computing for neuroscience, and quantum effects in biological systems.
  Triggers: quantum neuroscience, quantum brain, quantum neural network, quantum memory,
  quantum cognition, neuromorphic quantum, quantum machine learning brain.
---

# Neuro-Quantum Research

## Overview

Analyze and extract patterns from research at the intersection of neuroscience and quantum
physics/computing. This field spans quantum neural networks, quantum-inspired models of
consciousness, quantum memory as a model for biological memory, and quantum computing
applied to brain simulation.

## Key Research Directions

### 1. Organic-Quantum Brain Hypothesis (q-bio.NC + quant-ph)
- **3-Layer Quantum Brain Hypothesis** extended to engineered organic materials
- **Magnetic-field-free quantum computing** via SVILC qubits in organic materials
- Four paths: (P1) flavin-nitroxide radical-pair reservoir, (P2) PTM radical arrays in COFs, (P3) SVILC on κ-(BEDT-TTF) salts, (P4) SSH soliton on trans-polyacetylene
- **Key insight**: If organic materials support quantum computing without external fields, quantum brain effects become experimentally testable

### 2. Information Geometric Quantum Dynamics (quant-ph + statistical physics)
- Classical and quantum dynamics in information geometric spaces (Bernoulli random variables)
- Direct connection to **Friston's free energy principle** (Bayesian brain hypothesis)
- Provides rigorous mathematical bridge between quantum formalism and neural prediction

### 3. Quantum Spectroscopy for Biomolecular Sensing (quant-ph)
- Quantum spectroscopy with undetected photons for mid-infrared protein detection
- Double-pass quantum interferometer for non-destructive biomolecular analysis
- Applications to brain-relevant peptides (NT-proBNP, BSA)

### 4. Quantum Memory and Scrambling (quant-ph)
- Quantum memory protocols (error correction, entanglement distribution)
- Scrambling as a model for information processing in neural networks
- Classical neural networks as perspectives on quantum memory dynamics
- Key metric: entanglement fidelity, erasure error rates

### 2. Quantum Neural Networks (q-bio.NC + quant-ph)
- Stochastic quantum neural network models
- Quantum-inspired architectures for brain simulation
- Brain-inspired quantum vision models
- Superposition and entanglement as computational primitives for cognition

### 3. Multisensory Learning and Memory Engrams
- How sensory modalities recruit neurons across brain regions
- Memory engram formation and consolidation
- Cross-modal neural recruitment patterns
- Connection to quantum-like superposition in memory states

### 4. Neural Decoding and Brain-Computer Interfaces
- Saliency-aware multi-view neural decoding
- Functional connectivity-guided band selection
- Intrinsic brain network analysis
- Object-centric neural representations

## Analysis Workflow

### Step 1: Paper Classification
Classify papers by primary domain:
- **quant-ph dominant**: Quantum physics paper with neuroscience applications
- **q-bio.NC dominant**: Neuroscience paper using quantum-inspired methods
- **cs.AI/cs.LG**: Machine learning at the intersection
- **Cross-disciplinary**: Equal contribution from both fields

### Step 2: Extract Technical Patterns
For each paper, identify:
- Core methodology (quantum algorithm, neural architecture, hybrid model)
- Mathematical framework (Hilbert space, Hamiltonian dynamics, graph theory)
- Experimental validation (simulation, biological data, quantum hardware)
- Performance metrics (accuracy, fidelity, computational efficiency)

### Step 3: Map to Knowledge Graph
- Add entities to kg.db with full metadata
- Create relationships based on shared categories, authors, methodologies
- Generate vector embeddings for similarity search
- Run PageRank to identify influential papers

### Step 4: Identify Skill Patterns
Extract reusable methodologies:
- Quantum error correction patterns applicable to neural noise
- Neural network architectures inspired by quantum principles
- Brain simulation techniques using quantum computing
- Memory models bridging quantum and biological frameworks

## Common Pitfalls

- Confusing quantum-inspired classical algorithms with actual quantum computing
- Over-interpreting quantum effects in biological systems without experimental evidence
- Missing the distinction between quantum neural networks (quantum hardware) and
  quantum-inspired neural networks (classical hardware with quantum math)
- Not checking arxiv rate limits (429 errors) - use 5+ second delays between requests

## Resources

### Key Categories to Search arXiv
- `quant-ph` + `q-bio.NC`: Direct neuroscience-quantum intersection
- `quant-ph` + `cs.LG`: Quantum machine learning
- `q-bio.NC` + `cs.AI`: AI-brain modeling
- `cs.NE`: Neural and Evolutionary Computing (often includes quantum-inspired methods)
- `physics.soc-ph`: Quantum cognition for social science (decision making, game theory)
- `math.LO`: Logic-based quantum cognition (psychoanalysis, formal reasoning)
- `cs.AI` + `quant-ph`: Quantum reasoning, quantum abduction, strategic reasoning

### Proven Search Queries (2026-06)
- `all:"quantum neuroscience" OR all:"quantum brain" OR all:"quantum cognition"` → 104 results, highest recall
- `cat:q-bio.NC AND cat:quant-ph` → cross-category exact matches only

### Domain Saturation Tracking
Neuro-quantum domain is ~96% saturated (2,745 entities in kg.db). For heavily-covered domains:
- Cross-reference arXiv search results against existing skill directories using `search_files`
- Check kg.db `arxiv_papers` table: `SELECT id FROM arxiv_papers WHERE id LIKE '%{arxiv_id}%'`
- Papers in kg.db without corresponding SKILL.md files are the most valuable targets
- Focus on older papers (2025) that may have been missed by earlier searches

### Resources
- `scripts/kg_analysis.py`: Vector similarity search, PageRank, community detection
- `kg.db`: SQLite knowledge graph with entities (129+), vectors (BLOB), relationships (1136+)
- `scripts/kg_tool/target/release/kg_tool`: Compiled KG binary — supports: `import-paper`, `generate-embeddings`, `search`, `pagerank`, `communities`, `stats`. Commands `vector`, `embed`, `import`, `community`, `louvain`, `analyze` are NOT supported.

### Import Workflow
1. Search arXiv via proxy (`http://127.0.0.1:7890`) using HTTPS endpoint: `https://export.arxiv.org/api/query`
2. Parse XML response for paper metadata
3. Filter duplicates against existing kg.db entries (UNIQUE constraint on `url` column)
4. Insert into kg_entities with proper schema
5. Generate vector embeddings for similarity search (store as JSON-encoded bytes in BLOB column)
6. Create category-based relationships
7. Run analysis (PageRank, community detection)

## Examples

### Example: Analyzing a New Paper
User: "分析这篇量子神经网络论文: arxiv 2604.25663"

Agent should:
1. Fetch paper details from arXiv API
2. Import into kg.db
3. Run vector similarity search for related papers
4. Check PageRank to see if it connects to influential work
5. Extract any reusable skill patterns
