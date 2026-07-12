---
name: quantum-neuromorphic-computing
description: "Quantum neuromorphic computing framework combining quantum gates, memristive synapses, quantum cognition, optical quantum neurons, and neuromorphic quantum kernels. Use when: (1) analyzing quantum brain models, (2) implementing quantum neural networks, (3) studying quantum cognition mechanisms, (4) exploring memristive quantum synapses, (5) simulating quantum neuromorphic systems, (6) building HOM interference-based optical quantum neurons, (7) comparing neuromorphic vs parameterized quantum kernels for clustering."
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

7. **Q-SpiRL (2605.20801)**: Quantum Spiking Reinforcement Learning for robot navigation — QSNN achieves 99% success rate on 40x40 grid worlds, deployed on IBM quantum hardware.

8. **Quantum-Attention Hebbian (2606.02098)**: Derives softmax-weighted Hebbian learning rules from quantum probability flow in associative memory. Imaginary-time dynamics → log-sum-exp free energy gradient → attention-like updates. Validated on D-Wave annealers — softmax rule outperforms Lorentzian power law. Gradient-free, local updates only. See `references/quantum-attention-hebbian.md`.

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

### Hardware-Level Quantum Optical Neurons (2026)

9. **Quantum Optical Neuron** (2603.28879) — Camera-free image classification via Hong-Ou-Mandel interference of spatially programmable single photons. Two-photon coincidences directly measure image-template overlap, replacing pixel-resolved acquisition with a single global measurement. Performance is resolution-independent under fixed measurement budget. Strong noise robustness from quantum interference. See `references/quantum-optical-neuron-2603.28879.md`.

10. **Neuromorphic Quantum Kernels** (2507.07018) — Comparing parameterized quantum kernels (pQK, angle-encoding + grid-search alignment) with QLIF neuromorphic kernels (population coding → spike trains → Victor-Purpura/van Rossum temporal metrics) for spectral clustering. Trade-off: QLIF wins on low-dim data (Iris, synthetic), pQK wins on high-dim (SDSS).

11. **Neuromorphic Quantum-Cognitive Transform** (2503.07681) — Tutorial for transforming feedforward NN, RNN, ESN reservoir, Bayesian NN into quantum-inspired neuromorphic models using standard laptop quantum simulators. Enables context-dependent processing, interference-based decisions, and non-commutative operations.

## Hardware: Quantum Optical Neurons

### Hong-Ou-Mandel Interference as Physical-Layer Inner Product

**Core insight**: Two-photon coincidence rate at a beam splitter directly computes |⟨ψ_in|ψ_template⟩|² — the squared overlap between an input image mode and a learned template. This replaces pixel-by-pixel acquisition with a single global measurement.

**Architecture**:
1. **Image encoding**: Spatial light modulator (SLM) programs photon spatial mode
2. **Template preparation**: Programmable beam splitter with learned weights
3. **HOM interference**: Two photons interfere; coincidence rate = similarity score
4. **Classification**: Maximum coincidence rate across templates → predicted class

**Key advantages over classical**:
- Resolution independence: fixed measurement budget works at any input resolution
- Photon efficiency: operates in photon-starved regimes where classical cameras fail
- Hardware simplicity: single beam splitter + SPADs vs. full pixel array + ADC

**Scaling to networks**: Cascade multiple HOM interferometers with tunable beam splitters as synaptic weights for shallow quantum neural networks.

### Neuromorphic Quantum Kernel Selection

**Decision rule for spectral clustering**:
- Feature dim < 10: use QLIF (Victor-Purpura or van Rossum kernel on spike trains)
- Feature dim > 50: use pQK (angle-encoding with grid-search-optimized rotations)
- Intermediate: test both, select via kernel-target alignment score

**QLIF pipeline**: tabular data → population coding → spike trains → temporal distance metric → kernel matrix → spectral clustering
**pQK pipeline**: tabular data → angle encoding → parametric circuit → kernel matrix → spectral clustering

### Cognitive Transform Recipes

See `references/neuromorphic-quantum-cognitive-transform.md` for detailed transformation recipes from classical to quantum-inspired architectures.

## References

### Recent Paradigms
- **Quantum Hyperdimensional Computing (QHDC)** (arXiv:2511.12664) — brain-inspired HDC maps natively to quantum primitives: LCU+OAA bundling, phase oracle binding, QFT permutation, Hadamard similarity. Validated on 156-qubit IBM Heron r3. See `references/quantum-hyperdimensional-computing-2511.12664.md`
- **Stochastic Quantum Spiking Neural Networks (SQSNN)** (arXiv:2506.21324) — multi-qubit quantum memory neurons with single-shot inference and local learning rules (no backprop). See `references/stochastic-quantum-spiking-2506.21324.md`
- **Thermocoherent Cognitive Dynamics** (arXiv:2604.04069) — physical basis of information flow in neural matter via thermocoherent effect

For detailed theoretical background:

- Quantum-SNN fusion methodology: see `quantum-snn-fusion` skill (arXiv: 2606.07657, 2606.03517, 2606.09734)
- QDS-SNN: Quantum deeply-supervised spiking networks with TSA-LIF neurons and QACM
- Butterfly architecture: O(n log n) scalable QNN training
- QUIVER: Forward gradient estimation for parameterized quantum circuits
- June 2026 papers detail: see `references/quantum-snn-papers-2026-06.md`
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

### Pitfall: NISQ Gradient Bottleneck
Parameter-shift gradient estimation scales quadratically with parameters, making hardware QNN training impractical beyond ~20 qubits. Use QUIVER forward gradient estimators (O(1) per direction) or Butterfly architecture (O(log n) per step) to scale to 60+ qubits.

### Pitfall: SNN Vanishing Gradients
Standard SNNs with LIF neurons suffer from vanishing gradients during backprop through time. Use TSA-LIF (Temporally and Spatially Adaptive LIF) neurons or deep supervision via quantum-assisted modules (QACM) to maintain gradient flow with as few as 6 time steps.
- Focuses on theoretical models with potential hardware implementations
- Uses knowledge graph (kg.db) for paper retrieval and analysis
- Supports both analysis and simulation workflows