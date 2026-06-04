---
name: quantum-neuroscience-fusion
description: "Quantum neuroscience research skill - explores the intersection of quantum computing and neuroscience, including quantum neural networks, quantum spiking neural networks, quantum brain-inspired computing, covariant quantum error correction in biological systems, quantum photonic neural networks, and quantum cognitive modeling. Use when searching quantum neuroscience papers, analyzing quantum-ML architectures, designing quantum neuromorphic systems, or studying biological quantum coherence."
---

# Quantum Neuroscience Fusion

Research skill for exploring the intersection of quantum computing and neuroscience. Covers quantum neural networks, quantum spiking neural networks, quantum brain-inspired computing, and quantum cognitive modeling.

## Activation Keywords

- quantum neuroscience
- 量子神经科学
- quantum neural network
- quantum spiking neural network
- quantum brain
- quantum cognition
- quantum neuromorphic
- quantum SNN
- 量子脉冲神经网络
- CQEC quantum error correction biological
- quantum photonic neural network
- quantum cognitive modeling
- radical-pair mechanism

## Tools Used

- `web_search`: Search quantum neuroscience papers
- `browser_navigate` + `browser_snapshot`: Extract arXiv results (API is rate-limited)
- `exec`: Run kg_tool for knowledge graph queries
- `read`: Load paper abstracts, skill references
- `write`: Create research summaries, notes

## Core Concepts

### Quantum Neural Networks (QNN)

Variational quantum circuits for learning tasks:
- Parameterized quantum circuits
- Quantum variational classifiers
- Quantum autoencoders
- Hybrid classical-quantum networks

### Quantum Spiking Neural Networks

Brain-inspired quantum computing:
- Quantum neurons with spiking dynamics
- Quantum synapses with entanglement
- Quantum reservoir computing
- Quantum oscillator-based associative memory

### Quantum Cognitive Modeling

Quantum models of cognition:
- Quantum probability for decision making
- Quantum contextuality in perception
- Quantum entanglement in neural assemblies
- Quantum coherence in brain dynamics
- **Two paradigms**: (1) quantum-like (informational, Khrennikov) — uses quantum formalism without claiming physical quantum brain; (2) physical quantum brain (Wakaura 2604.08587) — tests actual coherence in biological substrates

### CQEC in Biological Systems (Key Finding, 2026)

Covariant Quantum Error Correction (Wakaura, arXiv:2604.08587):
- Three-layer architecture: nuclear spin memory → electron spin interface → electrochemistry
- CRY: T2=52ms, T1=0.53ns; MAO-A: T2=3.2ms, T1=1.1ns
- CQEC maintains coherence 0.83 over 200ms behavioral window (6.9x improvement at decoherence rate 0.19)
- Layer-protein tradeoff: no single protein optimizes both T1 and T2
- Coherence collapses at rate 3.08 even with CQEC
- Classical Markov baseline produces only monotonic relaxation

### Time-Encoded QPNN (Key Finding, 2026)

Boras Vazquez et al. (arXiv:2603.23798):
- Time-bin QPNN uses constant photonic elements regardless of network size/depth
- Bell-state analyzer: 0.96 fidelity (realistic nonlinearity), 0.99+ with time gating, efficiency >0.9
- Solves scaling problem: O(1) hardware per time bin vs O(N×D) for spatial encoding
- Quantum dot + waveguide scattering provides realistic two-photon nonlinearity

## Research Workflow

### Step 1: Search Papers

**Use browser search, NOT the arXiv API.** The API is aggressively rate-limited (429 on repeat calls).

```
Navigate to: https://arxiv.org/search/?query=<keywords>&searchtype=all&order=-announced_date_first
Use browser_snapshot to extract results with abstracts.
```

### Step 2: Analyze Architecture

Key architecture patterns:
- **Circuit depth**: Shallow circuits for NISQ devices
- **Encoding**: Amplitude encoding, basis encoding, angle encoding, SPATE spike-phase encoding
- **Decoding**: Measurement-based readout, quantum state tomography
- **Hybrid**: Classical preprocessing + quantum processing

### Step 3: Extract Patterns

From knowledge graph:
```bash
kg_tool pagerank kg.db  # Find important papers
kg_tool louvain kg.db   # Find research clusters
kg_tool similar kg.db <entity_id>  # Find related work
```

### Step 4: Synthesize Insights

Key research directions:
1. Quantum advantage in neural network training
2. Quantum error mitigation in spiking dynamics
3. Quantum coherence for memory capacity
4. Quantum entanglement for distributed computation
5. CQEC for biological quantum systems
6. Scalable QPNN via time-encoding

## Key Papers (from kg.db)

### Top Quantum Neuroscience Papers

1. **Covariant Quantum Error Correction in Three-Layer Quantum Brain** (arXiv:2604.08587)
   - CQEC maintains coherence 0.83 over 200ms behavioral window (6.9x improvement)
   - Layer-protein tradeoff: CRY longer T2/shorter T1, MAO-A opposite
   - Defines next research targets

2. **Quantum Photonic Neural Networks in Time** (arXiv:2603.23798)
   - Time-bin QPNN: constant photonic elements regardless of size/depth
   - Bell-state analyzer: 0.96 fidelity, >0.99 time-gated, efficiency >0.9

3. **Contextuality of Mental Markers** (arXiv:2603.03358)
   - Quantum-informational cognitive contextuality (Khrennikov-style)
   - Incompatible measurements from context-dependent representations

4. **Quantum-Tunnelling Oscillators for Cognitive Modelling**
   - Quantum oscillators for neural computation
   - Machine-vision applications

5. **Simulation of memristive synapses on quantum computer**
   - Quantum memristor implementation
   - Neuromorphic quantum computing

6. **Circuit Harmonic Matrices: Quantum ML Framework**
   - Spectral framework for QML
   - Harmonic analysis approach

## Research Questions

- Can quantum entanglement improve associative memory capacity?
- Does quantum coherence enhance learning dynamics?
- How to implement quantum STDP (spike-timing-dependent plasticity)?
- What quantum advantages exist for brain-inspired computing?
- How does covariant QEC maintain coherence in multi-layer quantum brain models?
- Are time-encoded QPNN architectures more scalable than spatial ones?
- Can quantum-like models (without physical quantum brain) explain cognitive biases?

## Implementation Notes

### Quantum SNN Architecture

```
Quantum Neuron Model:
  Input: Classical spikes → Quantum state preparation
  Processing: Quantum circuit evolution
  Output: Quantum measurement → Classical spikes

Quantum Synapse:
  Entanglement between neurons
  Quantum gate-based plasticity
  Measurement-induced weight update
```

### Hybrid Quantum-Classical Pipeline

```
1. Classical preprocessing: Feature extraction
2. Quantum encoding: State preparation
3. Quantum processing: Circuit execution
4. Quantum decoding: Measurement
5. Classical postprocessing: Output interpretation
```

## Related Skills

- **spikingjelly-framework**: Spiking neural network implementation
- **quantum-machine-learning**: Quantum ML general
- **brain-network-analysis**: Brain connectivity analysis
- **quantum-cognition**: Quantum probability models for cognitive processes (CHSH testing, interference effects, QPNN implementation scripts)

> **Note**: `quantum-cognition` and `quantum-neuroscience-fusion` overlap on QPNN and CQEC topics. 
> `quantum-cognition` is the implementation methodology (scripts, math, patterns); 
> `quantum-neuroscience-fusion` is the research workflow (search, KG analysis, synthesis).
- **quantum-cognition**: Quantum probability models for cognitive processes

## Knowledge Graph Integration

Use kg.db for:
- Paper similarity search via vectors
- PageRank for importance ranking
- Louvain for community detection
- BFS for paper relationships

## Limitations

- NISQ era constraints (noise, limited qubits)
- Quantum error correction overhead
- Classical-quantum interface complexity
- Lack of established benchmarks
- arXiv API rate limits — always use browser search

## Future Directions

- Quantum error mitigation for SNNs
- Quantum hardware for neuromorphic systems
- Quantum advantage demonstrations
- Standard benchmarks for quantum neuroscience
- Layer-specific quantum error correction in biological systems