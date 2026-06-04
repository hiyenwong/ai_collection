---
name: quantum-neuroscience-patterns
description: >
  Research methodology bridging quantum computing and neuroscience. Covers quantum
  hyperdimensional computing (QHDC), quantum generative models for neuronal data,
  quantum-enhanced EEG encoding (QEEGNet), Leggett-Garg tests in neural dynamics,
  and quantum neuromorphic architectures. Use when: researching quantum brain models,
  quantum neural networks, quantum-EEG hybrid systems, quantum generative models
  for biological data, neuromorphic quantum architectures, or testing quantum effects
  in neural dynamics. Triggers: quantum neuroscience, quantum brain, QEEGNet, quantum
  hyperdimensional computing, quantum neuromorphic, Leggett-Garg neural, quantum EEG,
  biological quantum correlations.
---

# Quantum Neuroscience Patterns

Methodology for bridging quantum computing with neuroscience research, derived from
recent arXiv papers (2024-2026).

## Core Patterns

### Pattern 1: Quantum Hyperdimensional Computing (QHDC)

Maps brain-inspired Hyperdimensional Computing onto native quantum operations.

| HDC Operation | Quantum Equivalent |
|---------------|-------------------|
| Hypervectors  | Quantum states (amplitude/phase encoding) |
| Bundling      | Linear Combination of Unitaries (LCU) + Oblivious Amplitude Amplification (OAA) |
| Binding       | Quantum phase oracles |
| Permutation   | Quantum Fourier Transform (QFT) |
| Similarity    | Hadamard Test |

Validated on 156-qubit IBM Heron r3.

### Pattern 2: Quantum Generative Models for Neuronal Data

Generate synthetic neuronal data with fewer parameters than classical methods:

1. Encode spatial/temporal correlations of biological neurons
2. Use quantum circuits as generative models (VQC or QGAN)
3. Train with hybrid quantum-classical optimization
4. Advantage: captures complex correlations with fewer trainable parameters

### Pattern 3: QEEGNet - Quantum-Enhanced EEG Encoding

Hybrid quantum-classical architecture for EEG:
- Base: EEGNet (convolutional architecture for EEG)
- Extension: Insert quantum variational layers
- Key challenge: generalization across tasks and datasets
- Finding: hybrid architectures need further optimization to leverage full quantum advantage

### Pattern 4: Leggett-Garg Tests in Neural Dynamics

Testing non-diffusive stochastic structure in single neurons:
- Distinguish diffusive (Wiener/cable-equation) models from non-diffusive alternatives
- Use Leggett-Garg temporal correlation inequalities
- Experimental program for probing quantum-like temporal structure in neurons

### Pattern 5: Covariant Quantum Error Correction (CQEC) in Quantum Brain Models

Evaluating quantum coherence in biological radical-pair proteins using covariant QEC:
- Three-layer architecture: nuclear spin memory → electron spin interface → classical electrochemistry
- Tested on MAO-A (T2 = 3.2 ms) and Cryptochrome/CRY (T2 = 52 ms)
- CQEC achieves 6.9x coherence improvement (0.83 vs 0.12 without correction) at favorable decoherence rates
- Key insight: layer-protein tradeoff — no single protein optimizes both layers
- Eastin-Knill theorem constrains CQEC to approximate (not exact) purification
- Also extended to organic qubit platforms (SVILC qubits, PTM radical arrays) for magnetic-field-free quantum computing
- Reference: arXiv 2604.08587, arXiv 2605.00026

### Pattern 6: Metabolic Quantum Limits in Brain Imaging

Deriving fundamental information-theoretic bounds on noninvasive brain imaging:
- Combines quantum sensor energy resolution + neural metabolism + Planck's constant
- Maximum information rate: 2.2 Mbit/s for human brain (technology-independent)
- Higher multipole magnetic field components geometrically suppressed below quantum noise floor
- Spatio-temporal trade-off: temporal vs spatial bandwidths compete
- Reference: arXiv 2511.06401

### Pattern 7: ORCHID — Bio-Inspired Kuramoto Quantum Consensus

Maps the neuroscientific binding problem onto distributed Byzantine consensus:
- Neural oscillators → consensus nodes with quantum-noisy Kuramoto phase oscillators
- Gamma-band binding event → consensus trigger when order parameter r(t) > binding threshold θ_b
- Coherence-weighted Quantum Secret Sharing (QSS) layer provides post-quantum security
- Sharp QSS fidelity phase transition at coherence c* ≈ 0.82
- Performance: r_max = 0.988 at K=3.0, 100% consensus at 0-40% Byzantine faults, O(n·k) message complexity (vs PBFT O(n²) at n ≥ 150)
- Reference: arXiv 2605.12126 (Weinberg)

## Workflow for Research

1. **Identify the intersection**: quantum operation + neuroscience problem
2. **Choose encoding strategy**: amplitude, phase, or basis encoding
3. **Design hybrid architecture**: classical pre-processing + quantum layer + classical post-processing
4. **Benchmark against classical baseline**: prove quantum advantage, not just parity
5. **Validate on real hardware**: simulate first, then test on actual quantum devices

## Key Papers

- QHDC: arXiv 2511.12664 - Maps HDC operations to quantum primitives
- Quantum Generative Models for Neurons: arXiv 2409.09125
- QEEGNet: arXiv 2503.00080 - Hybrid quantum-classical EEG encoding
- Leggett-Garg Neural Tests: arXiv 2605.12126 (Ghose)
- Covariant QEC in Quantum Brain: arXiv 2604.08587 (Wakaura)
- Organic SVILC Qubits: arXiv 2605.00026 (Wakaura)
- GKSL Quantum Cognition: arXiv 2604.18643 (Asano & Khrennikov) — open-systems dynamics for decision-making
- Metabolic Quantum Limit MEG: arXiv 2511.06401 (Gkoudinakis et al.)
- Stochastic QNN Model: arXiv 2511.11609 (Filardo, Heckmann)
- ORCHID Kuramoto Consensus: arXiv 2605.12126 (Weinberg)

## Pitfalls

- Quantum advantage must be proven against classical baselines, not shown in isolation
- Hybrid architectures require careful optimization to avoid vanishing gradients
- Cross-dataset generalization remains a major challenge for quantum-EEG models
- Entanglement structure matters: some Bell states enable coordination, others harm it
