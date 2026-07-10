---
name: parameter-efficient-quantum-mtl
description: "Parameter-efficient Quantum Multi-task Learning (QMTL) methodology. Replaces conventional task-specific linear heads with fully quantum prediction heads in hybrid architectures. Quantum head parameters scale linearly with task count vs quadratic for classical heads. Use when designing multi-task learning systems for medical imaging, NLP, or multimodal tasks with constrained parameter budgets."
---

# Parameter-Efficient Quantum Multi-task Learning

## Description
Framework for parameter-efficient quantum multi-task learning (QMTL) that replaces conventional task-specific linear heads with fully quantum prediction heads in a hybrid architecture. Demonstrates that quantum head parameter cost scales linearly with task count, while classical head cost scales quadratically. Evaluated on medical imaging, NLP, and multimodal benchmarks (arXiv:2604.13560).

## Activation Keywords
- quantum multi-task learning
- 量子多任务学习
- parameter-efficient quantum
- QMTL
- quantum prediction head
- quantum MTL
- variational quantum multi-task

## Core Concepts

### The Problem: Parameter Explosion in Multi-task Learning
In standard hard-parameter-sharing MTL:
- Shared backbone: processes input → shared representation
- Task-specific heads: map shared representation → task predictions
- **Problem**: Task-specific parameters grow quadratically O(d × T) with tasks T and representation dimension d

### The QMTL Solution
Replace task-specific linear heads with a hybrid quantum-classical architecture:
1. **Shared VQC encoding**: maps classical data to Hilbert space (task-independent)
2. **Task-specific ansatz blocks**: lightweight quantum blocks for localized adaptation
3. **Linear scaling**: quantum head parameters scale as O(T), not O(d × T)

### Architecture
```
Input → Classical/Shared Backbone → Shared VQC Encoding
                                        ├── Task 1 Ansatz Block → Prediction 1
                                        ├── Task 2 Ansatz Block → Prediction 2
                                        └── Task T Ansatz Block → Prediction T
```

## Implementation Workflow

### Step 1: Shared Representation
```
- Classical backbone (e.g., ResNet for images, Transformer for text)
- OR shared VQC encoding stage for quantum-native representation
- Output: shared feature vector of dimension d
```

### Step 2: Task-Specific Quantum Heads
```
For each task t:
  - Lightweight ansatz block (2-3 parameterized gates)
  - Maps shared representation → task-specific output
  - Parameters per task: O(1), not O(d)
```

### Step 3: Training
```
- Joint loss: L = Σ_t L_t(prediction_t, label_t)
- Backprop through shared backbone + task ansatz blocks
- Quantum simulation or real hardware execution
```

## Usage Patterns

### Pattern 1: Medical Multi-task Diagnosis
```
Input: Medical image (e.g., fundus photo)
Tasks: 
  - Disease classification (diabetic retinopathy grade)
  - Severity assessment
  - Risk prediction
Architecture: Shared CNN → Shared VQC → 3 task-specific ansatz blocks
```

### Pattern 2: NLP Multi-task
```
Input: Text sequence
Tasks:
  - Sentiment analysis
  - Named entity recognition
  - Text classification
Architecture: Shared Transformer → Shared VQC → task ansatz blocks
```

### Pattern 3: Parameter-Constrained Edge Deployment
```
When classical MTL exceeds memory/compute budget:
  - Replace heavy task heads with lightweight quantum heads
  - Maintain shared representation quality
  - Quantum simulation provides compact parameterization
```

## Parameter Scaling Analysis
| Architecture | Parameters vs Tasks | Space Complexity |
|-------------|-------------------|-----------------|
| Classical MTL head | O(d × T) | Quadratic |
| QMTL (proposed) | O(T) | Linear |
| Hybrid quantum MTL (prior) | O(d × T) | Quadratic |

## Error Handling

### Quantum Simulation Bottleneck
- Limit qubit count to 4-8 for practical simulation
- Use statevector simulator for training, shot-based for evaluation
- Consider hardware execution for final deployment

### Task Interference
- If tasks conflict, increase ansatz block expressibility
- Monitor per-task loss curves for negative transfer
- Consider task grouping before quantum head assignment

### Gradient Flow Through Quantum Layers
- Use parameter-shift rule for gradient computation
- Monitor barren plateau indicators
- Shallow circuits (2-3 layers) recommended for NISQ era

## Resources
- arXiv:2604.13560 — Parameter-efficient Quantum Multi-task Learning
- PennyLane for VQC implementation
- Medical imaging benchmarks (e.g., BreastMNIST, PathMNIST)
- NLP benchmarks for multi-task evaluation
