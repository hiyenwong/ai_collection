---
name: mcts-encoding-discovery-qml
description: "Monte Carlo Tree Search (MCTS) methodology for discovering optimal data encoding circuits in quantum-classical neural networks (QML). Use when: (1) designing data encoding strategies for quantum machine learning models, (2) optimizing variational quantum circuit encoding layers, (3) evaluating encoding performance predictors (effective rank vs entanglement capability vs Fourier decomposition), (4) building hybrid quantum-classical CNNs for medical imaging or other domains. Based on arXiv:2605.18540."
license: Complete terms in LICENSE.txt
---

# MCTS Encoding Discovery for QML

Discover optimal data encoding circuits for quantum-classical neural networks using Monte Carlo Tree Search (MCTS), as introduced in arXiv:2605.18540.

## Core Problem

Data encoding is the most impactful design choice in QML performance, yet why certain encodings outperform others is poorly understood. Manual encoding design is suboptimal and doesn't scale.

## MCTS Encoding Discovery Methodology

### Step 1: Define the QCCNN Architecture

Build a Quantum-Classical Convolutional Neural Network with:
- Non-variational quantum block for feature extraction
- Classical classifier head
- Encodings searched in the quantum block

### Step 2: Run MCTS Over Encoding Circuit Space

- State: Current partial encoding circuit
- Actions: Add gate/rotation from available set (RY, RZ, CNOT, etc.)
- Reward: Validation accuracy of the QCCNN with that encoding
- Use standard MCTS (selection → expansion → simulation → backpropagation)
- Evaluate each candidate on a short training budget before full retraining

### Step 3: Evaluate with Effective Rank Threshold

Key insight from the paper: **effective rank** of feature maps is a strong predictor of encoding performance, while entanglement capability and Fourier decomposition provide minimal insight.

- Compute effective rank of feature maps for discovered encodings
- Use effective rank as a threshold criterion to accelerate search
- Prune low-effective-rank candidates early to save computation

### Step 4: Validate on Target Dataset

- Train the best-discovered encoding with full budget
- Compare against standard encoding strategies (amplitude, angle, IQP)
- Compare against purely classical baselines

## Key Findings

1. MCTS-discovered encodings outperform commonly used strategies on medical imaging datasets
2. **Effective rank** is the most useful predictor — use it to accelerate future searches
3. Entanglement capability and Fourier decomposition are poor predictors
4. Discovered circuits remain competitive with classical counterparts

## Implementation Notes

- Use Qiskit or equivalent for quantum circuit simulation
- MCTS can be implemented with standard libraries (e.g., `mcts` package)
- Start with small circuit depths (3-5 layers) for tractable search
- For production, use effective rank as an early stopping criterion

## Activation

Keywords: MCTS encoding discovery, quantum data encoding, QCCNN, effective rank encoding predictor, Monte Carlo Tree Search quantum machine learning, encoding circuit optimization
