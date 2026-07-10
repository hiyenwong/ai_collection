---
name: mteeg-multi-task-eeg-lora
description: "Multi-task EEG analysis framework using Low-Rank Adaptation (LoRA) for efficient adaptation of pre-trained models to multiple downstream tasks. Addresses EEG signal heterogeneity and task conflicts through task-specific low-rank decomposition. Activation: multi-task EEG, LoRA adaptation, MTEEG, parameter-efficient fine-tuning, cross-subject EEG, task conflict resolution."
---

# MTEEG: Multi-Task EEG Analysis with Low-Rank Adaptation

> Parameter-efficient framework for adapting pre-trained EEG models to multiple downstream tasks simultaneously using Low-Rank Adaptation to handle task conflicts.

## Metadata
- **Source**: arXiv:2604.25131
- **Authors**: Sicheng Dai, Kai Chen, Hongwang Xiao, Xiang Zhang, Bao-Liang Lu
- **Published**: 2026-04-28
- **Category**: EEG Analysis, Multi-Task Learning

## Core Methodology

### Key Innovation
Traditional EEG pre-training requires full fine-tuning for each downstream task, making multi-task deployment computationally expensive. MTEEG enables simultaneous adaptation to multiple tasks using Low-Rank Adaptation (LoRA), resolving task conflicts through task-specific low-rank decomposition.

### Problem: Task Conflicts in Multi-Task EEG
EEG signals exhibit heterogeneity due to:
- Different subjects with varying neural patterns
- Diverse recording devices and electrode placements
- Various experimental paradigms and tasks
- Domain shifts between pre-training and downstream tasks

These factors create optimization conflicts when jointly training on multiple tasks.

### Solution: LoRA-Based Task Adaptation

```
Pre-trained Model → Task-Specific LoRA Modules → Multi-Task Outputs
                          ↓
                    Low-Rank Decomposition: W = W₀ + BA
                    where B ∈ ℝ^(d×r), A ∈ ℝ^(r×k), r << min(d,k)
```

## Technical Framework

### Architecture Components

| Component | Purpose | Details |
|-----------|---------|---------|
| Shared Encoder | Universal feature extraction | Pre-trained EEG transformer |
| LoRA Modules | Task-specific adaptation | Low-rank matrices per task |
| Task Heads | Output prediction | Classification/regression heads |
| Conflict Resolver | Gradient alignment | Gradient surgery or PCGrad |

### LoRA Formulation for EEG

For each task t, the adapted weight matrix:

```
W_t = W_0 + ΔW_t = W_0 + B_t × A_t
```

Where:
- `W_0`: Frozen pre-trained weights
- `B_t`: Task-specific low-rank matrix (down-projection)
- `A_t`: Task-specific low-rank matrix (up-projection)
- `r`: Rank (typically 4-16 for EEG)

### Multi-Task Training Strategy

#### Gradient Surgery for Conflict Resolution
```python
def pcgrad(gradients):
    """Project Conflicting Gradients"""
    for i, g_i in enumerate(gradients):
        for j, g_j in enumerate(gradients):
            if i != j and dot(g_i, g_j) < 0:
                # Project g_i onto normal of g_j
                g_i = g_i - (dot(g_i, g_j) / norm(g_j)**2) * g_j
    return gradients
```

#### Task Balancing
```python
# Uncertainty-weighted task loss
loss_total = Σ_t (1 / (2 * σ_t²)) * loss_t + log(σ_t)
```

## Implementation Guide

### Prerequisites
- Pre-trained EEG foundation model (e.g., EEGNet, Conformer)
- Multiple downstream task datasets
- PyTorch with transformers library

### Step-by-Step Implementation

#### Step 1: Install Dependencies
```bash
pip install torch transformers peft
```

#### Step 2: LoRA Configuration
```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=8,  # Rank
    lora_alpha=16,  # Scaling
    target_modules=["query", "value"],  # Apply to attention layers
    lora_dropout=0.1,
    bias="none",
    task_type="classification"
)

# Apply to base model
model = get_peft_model(base_eeg_model, lora_config)
```

#### Step 3: Multi-Task Data Loading
```python
class MultiTaskEEGDataset(Dataset):
    def __init__(self, task_datasets):
        self.task_datasets = task_datasets
        self.task_indices = {
            task: idx for idx, task in enumerate(task_datasets.keys())
        }
    
    def __getitem__(self, idx):
        # Sample from random task
        task = random.choice(list(self.task_datasets.keys()))
        data = self.task_datasets[task][idx % len(self.task_datasets[task])]
        return {
            'eeg': data['eeg'],
            'label': data['label'],
            'task_id': self.task_indices[task]
        }
```

#### Step 4: Training Loop with Task Routing
```python
class MTEEGTrainer:
    def __init__(self, model, task_heads, num_tasks):
        self.model = model
        self.task_heads = task_heads
        self.num_tasks = num_tasks
        
    def forward(self, eeg_batch, task_ids):
        # Shared encoding
        features = self.model.encode(eeg_batch)
        
        # Task-specific prediction
        outputs = []
        for task_id in range(self.num_tasks):
            mask = task_ids == task_id
            if mask.any():
                task_features = features[mask]
                task_output = self.task_heads[task_id](task_features)
                outputs.append((task_id, task_output, mask))
        
        return outputs
    
    def compute_loss(self, outputs, labels, task_ids):
        total_loss = 0
        for task_id, preds, mask in outputs:
            task_labels = labels[mask]
            task_loss = F.cross_entropy(preds, task_labels)
            total_loss += task_loss
        return total_loss
```

### Complete Training Example
```python
def train_mteeg(model, train_loader, num_epochs=100):
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(num_epochs):
        for batch in train_loader:
            eeg = batch['eeg'].cuda()
            labels = batch['label'].cuda()
            task_ids = batch['task_id'].cuda()
            
            # Forward pass
            outputs = trainer.forward(eeg, task_ids)
            loss = trainer.compute_loss(outputs, labels, task_ids)
            
            # Backward with gradient surgery
            optimizer.zero_grad()
            loss.backward()
            
            # Apply PCGrad
            grads = [p.grad for p in model.parameters() if p.grad is not None]
            if len(grads) > 0:
                pcgrad(grads)
            
            optimizer.step()
```

## Applications

### 1. Multi-Domain BCI
- Motor imagery classification
- Emotion recognition
- Mental workload estimation
- All from single adapted model

### 2. Cross-Subject Generalization
- Subject-independent models
- Few-shot personalization
- Domain adaptation

### 3. Clinical EEG Analysis
- Seizure detection
- Sleep stage classification
- Cognitive state monitoring

## Performance Characteristics

| Metric | Full Fine-tuning | MTEEG (LoRA) | Improvement |
|--------|-----------------|--------------|-------------|
| Parameters | 100% | 0.5-2% | 50-200x reduction |
| Memory | High | Low | Suitable for edge |
| Training Time | Long | Short | 5-10x faster |
| Multi-task Accuracy | Task-specific | Joint | Comparable |

## Pitfalls

1. **Rank Selection**: Too low rank may lose task-specific information; too high increases parameters
2. **Task Similarity**: Highly dissimilar tasks may still conflict despite LoRA
3. **Data Imbalance**: Unequal dataset sizes across tasks can bias optimization
4. **Pre-training Quality**: Poor base model limits adaptation effectiveness

## Related Skills
- eeg-foundation-model-adapters
- meta-learning-in-context-brain-decoding
- tta-eeg-foundation-models
- pa-tcnet-cross-subject-eeg

## References
- Dai, S., Chen, K., Xiao, H., Zhang, X., & Lu, B. L. (2026). Towards Unified Multi-task EEG Analysis with Low-Rank Adaptation. arXiv:2604.25131.
- Hu, E., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685.
- Yu, T., et al. (2020). Gradient Surgery for Multi-Task Learning. NeurIPS 2020.
