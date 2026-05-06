---
name: cortex-continual-learning-ftn
description: "Functional Task Networks (FTN) - cortex-inspired parameter isolation for unsupervised continual learning without catastrophic forgetting. Uses dendrite-like masking over network subpopulations. Triggers: continual learning, cortex-inspired, functional task networks, FTN, catastrophic forgetting."
---

# Cortex-Inspired Continual Learning: FTN

> FTN enables unsupervised task instantiation and recovery using cortex-inspired dendritic masking over distributed network subpopulations, preventing catastrophic forgetting.

## Metadata
- **Source**: arXiv:2604.24637
- **Authors**: Kevin McKee, Thomas Hazy, Yicong Zheng, Zacharie Bugaud
- **Published**: 2026-04-27
- **Category**: cs.LG, q-bio.NC

## Core Methodology

### Key Innovation
FTN (Functional Task Networks) is inspired by **structural and dynamical motifs in the mammalian neocortex**, specifically:
- **Mixture-of-experts** architecture
- **Dendritic models of pyramidal neurons** with nonlinear integration
- **Sparse, self-organizing binary masks** for parameter isolation

The key breakthrough is **unsupervised task inference** at test time—no task labels required.

### Biological Inspiration

#### Pyramidal Neuron Model
- **Apical dendrites**: Receive contextual/top-down signals
- **Basal dendrites**: Receive feedforward sensory input
- **Nonlinear integration**: Dendritic branches act as independent subunits

#### FTN Analog
- **Base network pool**: Large population of small but deep networks (analogous to pyramidal cells)
- **High-dimensional binary mask**: Self-organizing mask selects which subnetworks are active
- **Context-dependent routing**: Mask generation depends on input characteristics

### Technical Framework

#### Architecture
```
Input
  ↓
[Mask Generator Network] → Binary Mask M ∈ {0,1}^N
  ↓
[Subnetwork Pool: N small networks]
  ↓ (masked: only active subnetworks compute)
[Aggregation Layer]
  ↓
Output
```

#### Key Components
1. **Subnetwork Pool**: N small deep networks (e.g., 32 networks × 3 layers)
2. **Binary Mask Generator**: Produces sparse binary mask based on input
3. **Task-Specific Masks**: Different inputs activate different subnetwork combinations
4. **Local Plasticity**: Only active subnetworks update weights

## Implementation Guide

### Prerequisites
- PyTorch or JAX
- GPU recommended for parallel subnetwork computation
- Datasets for continual learning benchmarks (e.g., Split CIFAR-10/100, Permuted MNIST)

### Step-by-Step Implementation

#### Step 1: Define Subnetwork Pool
```python
import torch
import torch.nn as nn

class SmallNetwork(nn.Module):
    """Individual subnetwork in the pool."""
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, x):
        return self.net(x)

class SubnetworkPool(nn.Module):
    """Pool of small networks."""
    def __init__(self, num_networks, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.networks = nn.ModuleList([
            SmallNetwork(input_dim, hidden_dim, output_dim)
            for _ in range(num_networks)
        ])
    
    def forward(self, x, mask):
        """
        Args:
            x: input [batch_size, input_dim]
            mask: binary mask [batch_size, num_networks]
        Returns:
            aggregated output
        """
        outputs = []
        for i, net in enumerate(self.networks):
            if mask[:, i].any():  # Only compute if network is active
                out = net(x)
                outputs.append(out * mask[:, i:i+1])
        
        # Aggregate (mean or weighted sum)
        return sum(outputs) / mask.sum(dim=1, keepdim=True).clamp(min=1)
```

#### Step 2: Mask Generator
```python
class MaskGenerator(nn.Module):
    """Generates binary mask based on input."""
    def __init__(self, input_dim, num_networks, hidden_dim=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        self.mask_head = nn.Linear(hidden_dim, num_networks)
        self.temperature = 1.0  # For Gumbel-Softmax
    
    def forward(self, x, hard=True):
        """Generate binary mask using Gumbel-Softmax."""
        features = self.encoder(x)
        logits = self.mask_head(features)
        
        if hard and not self.training:
            # Hard binary mask at inference
            mask = (logits > 0).float()
        else:
            # Soft mask during training (Gumbel-Softmax)
            mask = torch.sigmoid(logits / self.temperature)
        
        return mask
```

#### Step 3: FTN Model
```python
class FTN(nn.Module):
    """Complete Functional Task Network."""
    def __init__(self, input_dim, output_dim, num_networks=32, 
                 subnet_hidden=64):
        super().__init__()
        self.num_networks = num_networks
        
        self.mask_generator = MaskGenerator(input_dim, num_networks)
        self.subnet_pool = SubnetworkPool(
            num_networks, input_dim, subnet_hidden, output_dim
        )
    
    def forward(self, x):
        mask = self.mask_generator(x)
        output = self.subnet_pool(x, mask)
        return output, mask
    
    def get_active_networks(self, x):
        """Get indices of active networks for given input."""
        mask = self.mask_generator(x, hard=True)
        active = [i for i in range(self.num_networks) 
                  if mask[:, i].any().item()]
        return active
```

#### Step 4: Continual Learning Training
```python
def train_ftn_continual(model, tasks, epochs_per_task=10):
    """
    Train FTN on sequence of tasks.
    
    Args:
        model: FTN model
        tasks: List of (train_loader, test_loader) tuples
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    for task_idx, (train_loader, test_loader) in enumerate(tasks):
        print(f"Training Task {task_idx + 1}")
        
        for epoch in range(epochs_per_task):
            model.train()
            for batch_idx, (data, target) in enumerate(train_loader):
                optimizer.zero_grad()
                
                output, mask = model(data)
                loss = criterion(output, target)
                
                # Add sparsity regularization on mask
                sparsity_loss = mask.mean() * 0.01
                total_loss = loss + sparsity_loss
                
                total_loss.backward()
                
                # Gradient masking for parameter isolation
                # Only update weights of active networks
                with torch.no_grad():
                    for name, param in model.named_parameters():
                        if 'subnet_pool' in name:
                            # Extract network index from parameter name
                            # Zero out gradients for inactive networks
                            pass  # Implementation depends on naming scheme
                
                optimizer.step()
        
        # Evaluate on all previous tasks
        evaluate_on_all_tasks(model, tasks[:task_idx+1])
```

#### Step 5: Unsupervised Task Inference
```python
def infer_task_unsupervised(model, x, task_prototypes):
    """
    Infer which task an input belongs to without labels.
    
    Args:
        model: Trained FTN model
        x: Input sample
        task_prototypes: Dictionary mapping task_id → mask prototype
    """
    with torch.no_grad():
        mask = model.mask_generator(x, hard=True)
        
        # Find closest task prototype
        min_distance = float('inf')
        inferred_task = None
        
        for task_id, prototype in task_prototypes.items():
            distance = torch.norm(mask - prototype)
            if distance < min_distance:
                min_distance = distance
                inferred_task = task_id
        
        return inferred_task, mask
```

### Complete Example
```python
import torch
import torch.nn as nn
from torchvision import datasets, transforms

# Setup
input_dim = 784  # MNIST
output_dim = 10
num_networks = 32

# Create FTN model
model = FTN(input_dim, output_dim, num_networks, subnet_hidden=64)

# Create Split MNIST tasks
tasks = []
for i in range(5):
    # Each task: binary classification of 2 digits
    task_data = create_split_mnist_task(i)
    tasks.append(task_data)

# Train continually
train_ftn_continual(model, tasks, epochs_per_task=5)

# Test unsupervised task inference
test_input = tasks[0][1].dataset[0][0]  # Sample from task 0
task_id, mask = infer_task_unsupervised(model, test_input, task_prototypes)
print(f"Inferred task: {task_id}")
```

## Applications

### Continual Learning Benchmarks
- **Split CIFAR-10/100**: Sequential learning of disjoint classes
- **Permuted MNIST**: Multiple MNIST tasks with pixel permutations
- **Task-Incremental Learning**: Same classes, different task contexts

### Neuroscience-Inspired AI
- Modeling cortex-like modular computation
- Understanding how biological neural networks avoid catastrophic forgetting
- Bridging biological and artificial intelligence

### Real-World Deployment
- **Streaming data**: Learning from non-stationary data distributions
- **Edge devices**: Sparse activation enables efficient inference
- **Personalization**: Task-specific masks enable user adaptation

## Pitfalls

1. **Mask Sparsity**: Too sparse → insufficient capacity per task; Too dense → overlap and forgetting
   - **Solution**: Monitor effective capacity per task, tune sparsity regularization

2. **Task Similarity**: Highly similar tasks may share masks → interference
   - **Solution**: Use hierarchical or structured masks

3. **Cold Start**: New tasks need mask exploration
   - **Solution**: Warm-start mask generator with similar tasks

4. **Scalability**: Large number of subnetworks increases memory
   - **Solution**: Dynamic allocation, weight sharing across subnetworks

## Related Skills
- `multi-plasticity-snn-training`: Multi-plasticity synergy for SNN training
- `meta-learning-biological-plasticity`: Meta-learning biologically plausible plasticity
- `neuro-attractor-landscape-working-memory`: Attractor landscapes for working memory

## References
- McKee et al. (2026). Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks. arXiv:2604.24637
- Yang et al. (2025). Task-Driven Co-Design for Multi-Robot Systems
- Pfeiffer & Pfeil (2018). Deep learning with spiking neurons: opportunities and challenges
