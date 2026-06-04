---
name: quantum-classical-hybrid-nn
description: "Design and implement quantum-classical hybrid neural networks that combine quantum computing with classical deep learning. Use when working with quantum machine learning (QML), quantum neural networks (QNN), hybrid quantum-classical architectures, or when needing to balance quantum expressivity with trainability. Keywords: quantum ML, quantum neural network, hybrid quantum-classical, QEEGNet, LieTrunc-QNN, quantum computing for AI, quantum-classical normalizing flows."
---

# Quantum-Classical Hybrid Neural Networks

Design patterns and best practices for building neural networks that integrate quantum computing with classical deep learning.

## Core Concepts

### 1. Quantum Expressivity vs Trainability Balance

**Key Principle:** Increasing quantum circuit expressivity leads to exponential gradient suppression (barren plateaus). Solution: Restrict to structured Lie subalgebras.

**LieTrunc-QNN Framework:**
- Model parameterized quantum circuits as Lie subalgebras of u(2^n)
- Expressivity = intrinsic manifold dimension and geometry
- Structured Lie subalgebras prevent concentration of measure
- Compact Lie subalgebras provide inherent robustness to perturbations

**Design Rule:**
```
expressivity ~ manifold dimension
gradient variance ~ exp(-dimension)  # barren plateaus
solution: Lie algebra truncation -> polynomial gradient decay
```

### 2. Quantum Layer Integration Patterns

**Pattern 1: Quantum Feature Encoding**
```
Classical Input -> Quantum Encoding Layer -> Classical Processing
Examples: QEEGNet (quantum encoding for EEG signals)
```

**Pattern 2: Quantum Processing Unit**
```
Classical Preprocessing -> Quantum Circuit -> Classical Postprocessing
Examples: Quantum-Classical Normalizing Flows
```

**Pattern 3: Hybrid Parallel Architecture**
```
Classical Branch || Quantum Branch -> Fusion Layer -> Output
Examples: Multi-split quantum-classical architectures
```

### 3. Architecture Design Guidelines

**For EEG/Signal Processing (QEEGNet pattern):**
- Use quantum encoding for high-dimensional temporal signals
- Quantum layers for feature extraction and pattern recognition
- Classical layers for final classification/interpretation
- Hybrid architecture improves encoding efficiency

**For Generative Models (Quantum Normalizing Flows):**
- Quantum circuits for analytically invertible transforms
- Split architecture: quantum for transformation, classical for density estimation
- Multi-split design for expressivity control

**For Trainable QNN (LieTrunc pattern):**
- Identify Lie algebra generators from circuit structure
- Restrict to compact subalgebras (SO(n), SU(n))
- Monitor Fubini-Study metric rank for expressivity
- Use algebraic span of generators to bound expressivity

## Implementation Checklist

### Step 1: Define Quantum Component
1. Choose quantum circuit type (variational, encoding, processing)
2. Identify Lie algebra generators
3. Determine expressivity requirements vs trainability constraints

### Step 2: Design Classical Integration
1. Select classical preprocessing/postprocessing layers
2. Define quantum-classical interface (encoding/decoding)
3. Choose fusion strategy (serial, parallel, hybrid)

### Step 3: Optimize for Trainability
1. Apply LieTrunc if barren plateaus detected
2. Monitor gradient variance during training
3. Validate Fubini-Study metric rank stability

### Step 4: Hardware Considerations
1. Determine quantum hardware requirements (qubits, gates)
2. Estimate quantum circuit depth vs coherence time
3. Plan for noise resilience and error correction

## Example Architectures

### Example 1: QEEGNet for EEG Analysis

```
Architecture:
  Input: EEG signals (high-dimensional temporal data)
  
  Classical Preprocessing: Signal normalization, temporal segmentation
  
  Quantum Encoding Layer:
    - Encode temporal features into quantum states
    - Use parameterized quantum circuits for feature extraction
    - Lie algebra: SU(4) truncated to preserve gradients
  
  Classical Processing:
    - Convolutional layers for spatial patterns
    - Attention layers for temporal dependencies
    - Dense layers for classification
  
  Output: EEG classification (cognitive states, neural markers)

Benefits:
  - Quantum encoding improves high-dimensional data compression
  - Hybrid architecture balances quantum expressivity with classical flexibility
  - Trainability maintained via Lie algebra truncation
```

### Example 2: Quantum-Classical Normalizing Flows

```
Architecture:
  Input: Data distribution
  
  Classical Split: 
    - Data preprocessing
    - Density estimation preparation
  
  Quantum Transform:
    - Analytically invertible quantum circuits
    - Multi-split design for controlled expressivity
    - Each split: different Lie subalgebra
  
  Classical Postprocessing:
    - Density computation from quantum samples
    - Log-likelihood estimation
  
  Output: Generative model with quantum-enhanced expressivity

Benefits:
  - Quantum circuits provide invertible transformations
  - Multi-split architecture prevents barren plateaus
  - Hybrid approach enables efficient sampling and training
```

### Example 3: LieTrunc-QNN for General QML

```
Architecture:
  Input: Classical data
  
  Quantum Circuit:
    - Parameterized gates forming Lie subalgebra
    - Compact subalgebra selection (SO(n), SU(n))
    - Expressivity controlled via algebraic span
  
  Classical Readout:
    - Measurement-based feature extraction
    - Classical neural network for final prediction
  
  Training:
    - Monitor Fubini-Study metric rank
    - Gradient variance tracking
    - Algebraic structure preservation

Benefits:
  - Provable polynomial trainability regime
  - Inherent noise resilience from compact algebra
  - Unified geometric framework for QNN design
```

## Common Patterns from Literature

### Pattern: Expressivity Control
**From:** LieTrunc-QNN (2604.02697)
**Key Insight:** Expressivity is governed by Lie algebra structure, not parameter count
**Application:** Use compact Lie subalgebras to prevent barren plateaus

### Pattern: Quantum Feature Encoding
**From:** QEEGNet (2407.19214)
**Key Insight:** Quantum encoding improves high-dimensional signal processing
**Application:** Use quantum layers for temporal/spatial feature extraction

### Pattern: Hybrid Invertible Transformations
**From:** Quantum-Classical Normalizing Flows (IJCNN 2026)
**Key Insight:** Quantum circuits provide analytically invertible transformations
**Application:** Use for generative models and density estimation

### Pattern: Quantum-Holographic Reinforcement Learning
**From:** AlphaChip Quantum-Holographic RL (2604.06)
**Key Insight:** Quantum circuits with holographic memory for self-optimizing systems
**Application:** Reinforcement learning with quantum state encoding

## Key Papers Reference

- **LieTrunc-QNN** (2604.02697): Algebraic-geometric framework for trainable QNN
- **QEEGNet** (2407.19214): Quantum ML for EEG encoding
- **Quantum-Classical Normalizing Flows** (IJCNN 2026): Multi-split architecture
- **Quantum Circuit-Based Learning Models** (2602.00048): QC-ML integration overview
- **Quantum-Holographic RL for AlphaChip** (2604.06): Quantum RL architecture

## Tools Used

- `exec`: Run quantum circuit simulations (Qiskit, PennyLane, Cirq)
- `read`: Load research papers and quantum computing frameworks
- `write`: Document quantum-classical hybrid architectures
- `edit`: Modify architecture configurations

## Error Handling

### Barren Plateau Detection
**Symptom:** Exponentially vanishing gradients during QNN training
**Solution:** Apply Lie algebra truncation to restrict expressivity

### Expressivity Collapse
**Symptom:** Fubini-Study metric rank collapse during training
**Solution:** Use structured Lie subalgebras (SO(n), SU(n))

### Quantum Noise Sensitivity
**Symptom:** Performance degradation under quantum hardware noise
**Solution:** Use compact Lie subalgebras for inherent noise resilience

## Related Skills

- **spikingjelly-framework**: For classical SNN implementations
- **neural-dynamics-universal-translator**: For neural dynamics modeling
- **quantum-computing-basics**: For quantum computing fundamentals
- **neural-architecture-search**: For optimizing classical components

## Notes

- Always balance expressivity with trainability in quantum circuits
- Use Lie algebra framework for theoretical grounding
- Test gradient variance early in development
- Consider hardware constraints when designing quantum circuits
- Hybrid architectures often outperform pure quantum or classical approaches