---
name: "staged-hybridisation-visual-qrl"
description: "Knowledge distillation as staged hybridisation strategy for visual quantum reinforcement learning. Train classical visual teacher, freeze encoder as feature interface, distill teacher policy into compact downstream heads (classical or VQC-based)."
---

# Staged Hybridisation for Visual Quantum Reinforcement Learning

## Description
Knowledge distillation (KD) as a staged hybridisation strategy for visual quantum reinforcement learning (QRL). Instead of training a hybrid visual agent end-to-end from pixels, first train a classical visual teacher, freeze its encoder as a feature interface, and distill the teacher's policy behaviour into compact downstream heads. These heads can be classical or VQC-based, enabling small quantum-compatible students to be evaluated under the same frozen representation as compact classical controls.

## Activation Keywords
- staged hybridisation QRL
- visual quantum reinforcement learning knowledge distillation
- quantum student classical teacher
- VQC knowledge distillation
- hybrid QRL feature interface
- 分阶段混合视觉量子强化学习
- 量子强化学习知识蒸馏
- frozen encoder quantum student

## Core Concepts

### Staged Hybridisation Pipeline
1. **Stage 1 — Classical Teacher Training**: Train a full classical visual RL agent (e.g., PPO/A2C) on pixel observations. The encoder learns rich visual representations.
2. **Stage 2 — Feature Interface Freezing**: Freeze the teacher's encoder as a fixed feature extractor. This provides a stable, low-dimensional representation interface.
3. **Stage 3 — Student Distillation**: Train compact downstream heads (classical or VQC-based) on the frozen features by distilling the teacher's policy behaviour (action distributions, value estimates).
4. **Stage 4 — Evaluation**: Compare quantum-compatible students against classical controls under identical frozen representations.

### Key Advantages
- **Avoids joint optimisation conflicts**: Separates visual representation learning from quantum policy learning
- **Fair comparison**: Quantum and classical students share the same frozen feature interface
- **Scalable**: Teacher can be large/complex while students remain compact
- **Modular**: Different student architectures (classical/VQC) can be swapped without retraining teacher

## Usage Patterns

### Pattern 1: Visual QRL Research
Use when benchmarking quantum vs classical policies on visual RL tasks. The staged approach isolates the quantum circuit's contribution from representation learning.

### Pattern 2: Feature-Interface Quantum Policy
Use when you want to integrate a VQC as a drop-in replacement for a classical policy head on pre-trained features.

### Pattern 3: Resource-Constrained QRL
Use when quantum hardware constraints limit circuit size — freeze the heavy computation (encoder) classically, only the policy head runs quantum.

## Instructions for Agents

### Step 1: Train Classical Teacher
```python
# Train standard RL agent (e.g., PPO) on visual environment
# Save encoder weights and policy head separately
teacher_encoder = model.encoder  # Save this
teacher_policy = model.policy_head  # For distillation targets
```

### Step 2: Freeze Encoder as Feature Interface
```python
# Freeze encoder parameters
for param in teacher_encoder.parameters():
    param.requires_grad = False

# Define feature extraction function
def extract_features(obs):
    with torch.no_grad():
        return teacher_encoder(obs)
```

### Step 3: Build Student Heads
```python
# Classical student head
classical_head = nn.Sequential(
    nn.Linear(feature_dim, 64),
    nn.ReLU(),
    nn.Linear(64, num_actions)
)

# VQC student head
class VQCHead(nn.Module):
    def __init__(self, feature_dim, num_actions, n_qubits):
        super().__init__()
        self.feature_proj = nn.Linear(feature_dim, n_qubits)
        self.vqc = VariationalQuantumCircuit(n_qubits, n_layers=2)
        self.output = nn.Linear(n_qubits, num_actions)
```

### Step 4: Distillation Training
```python
# KL divergence between teacher and student action distributions
def distillation_loss(student_logits, teacher_probs, temperature=1.0):
    student_dist = Categorical(logits=student_logits / temperature)
    teacher_dist = Categorical(probs=teacher_probs)
    return F.kl_div(
        F.log_softmax(student_logits / temperature, dim=-1),
        teacher_probs,
        reduction='batchmean'
    ) * (temperature ** 2)
```

## Error Handling

### VQC Trainability Issues
- **Problem**: VQC heads may suffer from barren plateaus
- **Solution**: Use small number of qubits (4-8), shallow circuits (2-3 layers), and layer-wise initialization

### Feature Dimension Mismatch
- **Problem**: Teacher encoder output dimension may not match VQC input
- **Solution**: Use a linear projection layer between frozen encoder and VQC

### Distillation Temperature Sensitivity
- **Problem**: Temperature too high → loss of information; too low → hard labels only
- **Solution**: Start with temperature=1.0, sweep [0.5, 2.0] for optimal transfer

## Resources
- arXiv: 2606.30520 — "Staged Hybridisation for Visual Quantum Reinforcement Learning via Knowledge Distillation"
- Related skills: `quantum-ml-patterns`, `quantum-neural-hybrid`, `knowledge-distillation-patterns`
