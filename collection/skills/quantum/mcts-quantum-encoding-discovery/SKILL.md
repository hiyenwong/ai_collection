---
name: mcts-quantum-encoding-discovery
description: MCTS-based quantum data encoding discovery methodology. Uses Monte Carlo Tree Search to find optimal encoding circuits for quantum-classical neural networks, with effective rank as performance predictor. Trigger words: MCTS encoding, quantum encoding discovery, QML encoding optimization, 量子编码发现.
---

# MCTS Quantum Encoding Discovery

## Description

Monte Carlo Tree Search (MCTS) methodology for discovering optimal data encoding
strategies in quantum machine learning (QML). Evaluates encoding circuits by their
effective rank and uses tree search to efficiently navigate the encoding circuit
space. Validated on medical imaging datasets.

## Core Methodology

The key insight: **not all data encodings are equal**, and the choice of encoding
significantly impacts QML performance. Rather than using hand-designed encodings,
MCTS systematically discovers encoding circuits that outperform standard approaches.

### Framework Components

1. **Quantum-Classical CNN (QCCNN)**: Non-variational quantum block for feature
   extraction followed by a classical classifier
2. **MCTS Search**: Tree search over encoding circuit configurations
3. **Effective Rank Metric**: Key predictor of encoding quality — correlates with
   performance better than entanglement capability or Fourier decomposition
4. **Threshold Criterion**: Use effective rank to prune low-performing branches

## Mathematical Framework

### Effective Rank of Feature Maps

The effective rank measures the informativeness of quantum feature maps:

```
r_eff(Φ) = exp(H(λ)) / d
```

where λ are the eigenvalues of the feature covariance matrix, H is the Shannon
entropy, and d is the dimension. Higher effective rank indicates more uniformly
distributed information across feature dimensions.

### MCTS for Encoding Discovery

```
Selection → Expansion → Simulation → Backpropagation

- State: Partial encoding circuit configuration
- Action: Add/remove/modify a gate in the encoding
- Reward: Classification accuracy on validation set
- Rollout: Quick evaluation with limited epochs
```

## Usage Patterns

### Pattern 1: Discovering QML Encoding Circuits

When building a quantum-classical hybrid model:

1. Define the encoding search space (gate types, qubit connectivity)
2. Set up MCTS with effective rank as early stopping criterion
3. Run search: select → expand → simulate → backpropagate
4. Extract top-k encoding circuits for final evaluation
5. Compare against standard encodings (amplitude, angle, IQP)

### Pattern 2: Encoding Quality Prediction

Before full training, use effective rank to predict encoding performance:

1. Compute feature maps for each candidate encoding
2. Calculate effective rank of the feature covariance matrix
3. Rank encodings by effective rank (higher → better)
4. Use as threshold to prune search space early

### Pattern 3: Medical Imaging QML Pipeline

For medical image classification with quantum models:

1. Preprocess images to compatible quantum state format
2. Use MCTS-discovered encoding for quantum feature extraction
3. Non-variational quantum block: fixed circuit, no trainable parameters
4. Classical classifier on top: lightweight neural network or SVM
5. Evaluate with cross-validation on medical dataset

## Instructions for Agents

### Step 1: Identify the QML Problem

- Determine if quantum encoding is the bottleneck
- Check if classical baselines are competitive
- Assess dataset size and feature dimensionality

### Step 2: Set Up MCTS Search

- Define action space: available quantum gates (RY, RZ, CNOT, etc.)
- Set tree depth and breadth parameters
- Initialize with common encoding strategies as root

### Step 3: Run Evaluation

- Use effective rank for quick pre-screening
- Full evaluation: train QCCNN with discovered encoding
- Compare against: amplitude encoding, angle encoding, IQP encoding

### Step 4: Analyze Results

- Check if entanglement capability correlates with performance (spoiler: it doesn't)
- Check if Fourier decomposition provides insight (spoiler: minimal)
- Verify effective rank as the primary predictor

## Pitfalls

### Effective Rank vs Other Metrics

- **Entanglement capability**: Poor predictor of encoding performance
- **Fourier decomposition**: Minimal insight for practical encoding selection
- **Effective rank**: Best single predictor — use this

### QCCNN Design

- The quantum block should be **non-variational** (fixed parameters)
- Train only the classical classifier
- This avoids barren plateau issues while still gaining quantum advantage

### Dataset Requirements

- Works best on structured data (medical images, tabular)
- Need sufficient samples for effective rank computation
- Small datasets may not show clear encoding differences

### MCTS Configuration

- Too few iterations → poor exploration
- Too many → diminishing returns
- Start with 100-500 iterations, scale based on action space size

## Activation Keywords

- MCTS encoding discovery
- quantum encoding optimization
- QML data encoding
- quantum-classical neural network encoding
- effective rank encoding
- 量子编码发现
- 量子机器学习编码优化

## Related Skills

- `quantum-ml-patterns` — General QML research patterns
- `quantum-neural-architecture` — QNN architecture design
- `quantum-neural-network-designer` — QNN optimization
- `hybrid-quantum-classical-nn` — Hybrid model patterns

## Reference

- arXiv:2605.18540 — "Discovering Data Encoding Strategies for Quantum-Classical
  Neural Networks Using Monte Carlo Tree Search" (Tokuhiro et al., 2026)
