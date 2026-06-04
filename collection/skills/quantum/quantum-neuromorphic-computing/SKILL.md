---
name: quantum-neuromorphic-computing
description: "Quantum neuromorphic computing framework combining quantum gates, memristive synapses, and quantum cognition for decision making. Use when: (1) analyzing quantum brain models, (2) implementing quantum neural networks, (3) studying quantum cognition mechanisms, (4) exploring memristive quantum synapses, (5) simulating quantum neuromorphic systems."
---

# Quantum Neuromorphic Computing

Framework for quantum-enhanced neuromorphic computing, combining insights from quantum cognition theory, quantum brain models, and memristive quantum synapses.

## Activation Keywords
- quantum neuromorphic
- 量子神经形态
- quantum brain model
- quantum cognition
- memristive quantum
- quantum synapse
- quantum reservoir computing
- quantum extreme learning

## Tools Used
- `exec`: Run kg_tool for knowledge graph operations, Python scripts for simulation
- `read`: Load skill references, paper abstracts, configuration files
- `write`: Save analysis results, simulation outputs, configuration files

## Core Concepts

### Quantum Cognition
Decision-making framework using quantum probability to model cognitive processes. Key features:
- **Non-commutative measurements**: Order-dependent outcomes (contextuality)
- **Superposition states**: Multiple cognitive states simultaneously
- **Entanglement**: Correlated cognitive subsystems
- **Interference effects**: Probability interference in decision outcomes

### Quantum Brain Models
Theoretical models treating neural dynamics as quantum processes:
- **Lipkin-Meshkov-Glick (LMG) model**: Collective spin dynamics with synaptic feedback
- **Phase transitions**: Paramagnetic/ferromagnetic states modulated by synaptic plasticity
- **Husimi distribution**: Phase-space representation of quantum states
- **Wehrl entropy**: Measure of localization and phase-space deformation

### Memristive Quantum Synapses
Quantum gates exhibiting memristive behavior:
- **Pinched hysteresis loop**: Memory-dependent conductance
- **Long-term plasticity**: Quantum state-encoded synaptic weights
- **Ohm's law**: Quantum conductance behavior
- **Universal quantum computing**: Three-layer memristive quantum neural networks

## Workflow

### Phase 1: Knowledge Retrieval

1. **Search knowledge graph**:
```bash
kg_tool search kg.db "quantum neural"
kg_tool search kg.db "quantum cognition"
kg_tool search kg.db "memristive quantum"
```

2. **Find related papers**:
```bash
kg_tool similar kg.db <entity_id> 10
```

3. **Get PageRank important papers**:
```bash
kg_tool pagerank kg.db
```

### Phase 2: Analysis

Run quantum cognition analysis script:
```bash
python3 ~/.openclaw/skills/quantum-neuromorphic-computing/scripts/quantum_cognition_analysis.py --input <paper_id> --kg kg.db
```

### Phase 3: Simulation

For quantum brain model simulations:
```bash
python3 ~/.openclaw/skills/quantum-neuromorphic-computing/scripts/quantum_brain_simulation.py --model lmg --feedback synaptic
```

## Key Research Papers

From knowledge graph analysis (kg.db):

1. **Extreme Quantum Cognition Machines (2603.05430)**: Quantum learning architectures for deliberative decision making with dynamical attention mechanism

2. **Quantum Brain Model with Synaptic Feedback (2603.03345)**: LMG model showing how synaptic plasticity modulates phase transitions

3. **Memristive Synapses on Quantum Computer (2007.09574)**: Quantum gates with memristive behavior for neuromorphic computing

### Hybrid Spiking-Quantum Architectures (2026)

4. **SPATE (2604.11022, IJCNN 2026)**: Spiking-Phase Adaptive Temporal Encoding — converts real-valued features into LIF spike trains, maps spike statistics to quantum rotations with temporal qubits. CKTA 0.966 vs 0.632 (angle encoding). See `references/spiking-quantum-encoding.md` for methodology details.

5. **SQDR-CNN (2512.03895, PeerJ CS 2026)**: Spiking-Quantum Data Re-upload CNN — end-to-end joint training of convolutional SNNs + quantum circuits via surrogate gradients + data re-uploading. 86% SOTA accuracy at 0.5% parameters. See `references/spiking-quantum-cnn.md`.

6. **Q-SpiRL (2605.20801)**: Quantum Spiking Reinforcement Learning for robot navigation — QSNN achieves 99% success rate on 40x40 grid worlds, deployed on IBM quantum hardware.

7. **Stochastic QNN (2511.11609)**: Stochastic quantum neural networks with qubits evolving via stochastic differential equations inspired by biological neuronal processes.

## Spiking-Quantum Hybrid Methodologies

### SPATE: Spike-to-Phase Encoding

**Core pipeline**: Features → LIF spike trains → spike statistics → quantum rotation angles + temporal qubits

**Steps**:
1. Normalize features to [0,1]
2. Convert to LIF spike trains: τ·dV/dt = -(V - V_rest) + R·I(t), spike when V > V_threshold
3. Extract statistics: firing rate, mean ISI, coefficient of variation
4. Map to R_z(θ) rotation gates with controlled phase operations on temporal qubits
5. Feed into variational quantum circuit

**Evaluation protocol**: CKTA, Fisher separability, silhouette score, normalized entropy, TVpair collapse — assess encoding quality independently of classifier.

**Pitfalls**:
- Spike train length trade-off: too short loses temporal info, too long → decoherence
- Each temporal qubit doubles circuit depth — use sparingly
- LIF τ and V_threshold must be calibrated per dataset

### SQDR-CNN: Joint SNN-Quantum Training

**Core innovation**: Surrogate gradient + quantum data-reupload enables end-to-end backprop without pretrained SNN encoders.

**Architecture**: Input → ConvSNN → Flatten spikes → Data Re-upload Layers → Measurement

**Key principles**:
- Surrogate gradient: smooth approximation of Heaviside for spike backprop
- Quantum data-reupload: N re-uploads ≈ N-qubit expressivity on single qubit
- Hybrid optimizer: Adam for classical, parameter-shift for quantum

**Pitfalls**:
- Surrogate gradient choice (sigmoid/arctan/triangle) critically affects stability
- Temporal steps: too few → poor SNN dynamics; too many → slow training
- Feature-to-qubit mismatch requires dimensionality reduction

## References

For detailed theoretical background:
- **Quantum cognition**: See `references/quantum_cognition.md`
- **Quantum brain models**: See `references/quantum_brain_models.md`
- **Memristive quantum**: See `references/memristive_quantum.md`
- **Quantum-classical bridging patterns**: See `references/quantum-classical-bridging.md` — DBM-NQS for spin glasses, thermodynamic networks, Born-rule DQPT analysis, Leggett-Garg neural tests

## Error Handling

### kg_tool not found
```bash
# Build kg_tool if missing
cd /path/to/sqlite-knowledge-graph
cargo build --release
```

### Embedding generation fails
- Ensure `sentence-transformers` installed: `pip install sentence-transformers`
- Check kg_vectors table exists: `sqlite3 kg.db "SELECT COUNT(*) FROM kg_vectors"`

### Simulation convergence issues
- Reduce model complexity (fewer spins)
- Increase simulation time steps
- Adjust feedback coupling strength

## Applications

1. **Decision making**: Quantum cognition models for deliberative inference
2. **Sequence analysis**: Quantum reservoir computing for temporal patterns
3. **Anomaly detection**: Quantum extreme learning for classification
4. **Brain modeling**: Understanding synaptic plasticity through quantum dynamics
5. **Hardware implementation**: Memristive quantum gates for neuromorphic hardware

## Notes

- This skill bridges neuroscience and quantum computing
- Focuses on theoretical models with potential hardware implementations
- Uses knowledge graph (kg.db) for paper retrieval and analysis
- Supports both analysis and simulation workflows