---
name: structural-plasticity-growth-stability
description: "Analysis methodology for structural plasticity in neural networks — evaluating growth vs pruning operators, newborn unit integration stability, and time-sensitive optimization dynamics. Covers forward-active backward-starved phenomenon, insertion stability, and continual learning plasticity."
---

# Structural Plasticity Growth Stability Analysis

Methodology for analyzing and implementing structural plasticity — specifically the growth operator for dynamically expanding neural network architectures during training. Reveals that growth is not simply the inverse of pruning, and identifies the critical "forward-active, backward-starved" phenomenon that limits newborn unit integration.

Based on: *On the Stability of Growth in Structural Plasticity* (arXiv: 2605.15435)
Authors: Lillo & Cheney, 2026

## Activation

- structural plasticity growth
- dynamic network growth
- newborn unit integration
- forward-active backward-starved
- neural network growth pruning
- insertion stability
- adaptive network architecture
- continual learning plasticity
- 结构可塑性生长
- 新生单元集成

## Core Findings

### Growth is NOT the Inverse of Pruning

- **Pruning** selects among units that have participated in training from the start
- **Growth** inserts new units into an already specialized optimization trajectory
- Newborn units face a fundamentally different optimization landscape than pruned units

### Forward-Active, Backward-Starved Phenomenon

Newborn units exhibit a critical asymmetry:
- **Forward-active**: They participate in the forward computation immediately after insertion
- **Backward-starved**: They receive much weaker gradient signals than incumbent units
- This disadvantage is minor in small MLP benchmarks but becomes severe in harder settings (convolutional trunks, image classification)

### Three Evaluation Regimes

1. **Final accuracy**: Growth can achieve high final accuracy during structural editing
2. **Trajectory-averaged performance**: Pruning is stronger when performance is averaged over the full training trajectory
3. **Retrained sparse networks**: Pruning produces better subnetworks when retrained from scratch

## Methodology

### Step 1: Growth Operator Implementation

```python
import torch
import torch.nn as nn

class GrowPruneNetwork(nn.Module):
    """Network supporting dynamic growth and pruning."""
    
    def __init__(self, layer_sizes, growth_rate=0.1):
        super().__init__()
        self.layer_sizes = list(layer_sizes)
        self.growth_rate = growth_rate
        self.layers = nn.ModuleList()
        
        for i in range(len(layer_sizes) - 1):
            layer = nn.Linear(layer_sizes[i], layer_sizes[i + 1])
            self.layers.append(layer)
    
    def grow_layer(self, layer_idx: int, n_new: int, optimizer):
        """Add new neurons to a specific layer."""
        layer = self.layers[layer_idx]
        prev_layer = self.layers[layer_idx - 1] if layer_idx > 0 else None
        next_layer = self.layers[layer_idx + 1] if layer_idx < len(self.layers) - 1 else None
        
        old_in, old_out = layer.weight.shape
        
        # Create new weights with small random initialization
        new_in = old_in
        new_out = old_out + n_new
        
        # Extend the current layer
        new_weight = torch.randn(new_out, new_in) * 0.01  # Small init for newborn
        new_weight[:old_out] = layer.weight.data.clone()
        layer.weight = nn.Parameter(new_weight)
        
        new_bias = torch.zeros(new_out)
        new_bias[:old_out] = layer.bias.data.clone()
        layer.bias = nn.Parameter(new_bias)
        
        # Adjust next layer input dimension
        if next_layer is not None:
            new_next_weight = torch.randn(next_layer.out_features, new_out) * 0.01
            new_next_weight[:, :old_out] = next_layer.weight.data.clone()
            next_layer.weight = nn.Parameter(new_next_weight)
        
        # Adjust optimizer state for the modified parameters
        self._update_optimizer_state(optimizer, layer, n_new, old_out)
    
    def _update_optimizer_state(self, optimizer, layer, n_new, old_size):
        """Reset or initialize optimizer state for new parameters."""
        for group in optimizer.param_groups:
            for p in group['params']:
                if p is layer.weight or p is layer.bias:
                    state = optimizer.state[p]
                    state.clear()  # Fresh start for modified parameters
```

### Step 2: Gradient Signal Analysis

```python
def analyze_gradient_signals(model, data_loader, device='cpu'):
    """Measure gradient magnitudes for newborn vs incumbent units."""
    model.train()
    gradient_stats = {'newborn': [], 'incumbent': []}
    
    # Track which units are newborn (need external tracking)
    newborn_mask = getattr(model, 'newborn_mask', None)
    
    for batch_x, batch_y in data_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        
        # Forward pass
        output = model(batch_x)
        loss = torch.nn.functional.cross_entropy(output, batch_y)
        
        # Backward pass
        loss.backward()
        
        # Collect gradient statistics per layer
        for name, param in model.named_parameters():
            if param.grad is not None and 'weight' in name:
                grad = param.grad.data
                if newborn_mask is not None:
                    newborn_grads = grad[newborn_mask[name]].abs().mean()
                    incumbent_grads = grad[~newborn_mask[name]].abs().mean()
                    gradient_stats['newborn'].append(newborn_grads.item())
                    gradient_stats['incumbent'].append(incumbent_grads.item())
    
    return {
        'newborn_mean': torch.tensor(gradient_stats['newborn']).mean().item(),
        'incumbent_mean': torch.tensor(gradient_stats['incumbent']).mean().item(),
        'ratio': (torch.tensor(gradient_stats['newborn']).mean() / 
                  (torch.tensor(gradient_stats['incumbent']).mean() + 1e-8)).item(),
    }
```

### Step 3: Insertion Stability Interventions

```python
class InsertionInterventions:
    """Interventions to improve newborn unit integration."""
    
    @staticmethod
    def scaled_initialization(layer, n_new, method='gradient-matched'):
        """Initialize newborn units to match incumbent gradient scale."""
        if method == 'gradient-matched':
            # Initialize with variance scaled to match existing units
            existing_std = layer.weight[:layer.weight.shape[0] - n_new].std()
            new_weights = torch.randn(n_new, layer.weight.shape[1]) * existing_std
            layer.weight.data[-n_new:] = new_weights
        
        elif method == 'copy-perturb':
            # Copy an existing unit and add small perturbation
            idx = torch.randint(0, layer.weight.shape[0] - n_new, (1,)).item()
            for i in range(n_new):
                layer.weight.data[-(i+1)] = layer.weight.data[idx] + torch.randn_like(layer.weight.data[idx]) * 0.01
        
        elif method == 'zero-start':
            # Start with near-zero weights (baseline)
            layer.weight.data[-n_new:] = torch.randn(n_new, layer.weight.shape[1]) * 0.001
    
    @staticmethod
    def warm_optimizer_state(optimizer, layer, n_new, old_size, warmup_steps=10):
        """Warm up optimizer state for new parameters."""
        for group in optimizer.param_groups:
            for p in group['params']:
                if p is layer.weight or p is layer.bias:
                    # Initialize momentum/state with scaled-down values
                    state = optimizer.state[p]
                    if 'momentum_buffer' in state:
                        buf = state['momentum_buffer']
                        # Scale momentum for new units
                        if buf.shape[0] > old_size:
                            buf[old_size:] *= 0.1  # Dampened momentum for newborns
    
    @staticmethod
    def selective_lr(layer, base_lr, newborn_lr_multiplier=5.0, newborn_mask=None):
        """Apply higher learning rate to newborn units."""
        if newborn_mask is not None:
            per_param_lr = torch.ones_like(layer.weight) * base_lr
            per_param_lr[newborn_mask] *= newborn_lr_multiplier
            return per_param_lr
        return base_lr
```

### Step 4: Evaluation Protocol

```python
def evaluate_growth_vs_pruning(model, train_data, test_data, 
                               growth_schedule, prune_schedule,
                               max_epochs, device='cpu'):
    """Comprehensive evaluation of growth vs pruning."""
    
    results = {
        'growth': {'final_acc': [], 'trajectory_acc': [], 'per_epoch': []},
        'prune': {'final_acc': [], 'trajectory_acc': [], 'per_epoch': []},
    }
    
    for strategy in ['growth', 'prune']:
        model_copy = copy.deepcopy(model)
        optimizer = torch.optim.Adam(model_copy.parameters(), lr=1e-3)
        
        per_epoch_accs = []
        for epoch in range(max_epochs):
            # Apply structural edit if scheduled
            if strategy == 'growth' and epoch in growth_schedule:
                for layer_idx, n_new in growth_schedule[epoch]:
                    model_copy.grow_layer(layer_idx, n_new, optimizer)
            
            if strategy == 'prune' and epoch in prune_schedule:
                for layer_idx, n_prune in prune_schedule[epoch]:
                    model_copy.prune_layer(layer_idx, n_prune, optimizer)
            
            # Train for one epoch
            train_acc = train_one_epoch(model_copy, train_data, optimizer, device)
            per_epoch_accs.append(train_acc)
        
        # Final accuracy
        final_acc = evaluate(model_copy, test_data, device)
        
        # Retrain sparse network from scratch (for pruning comparison)
        retrained_acc = retrain_from_scratch(model_copy, train_data, test_data, device)
        
        results[strategy] = {
            'final_acc': final_acc,
            'trajectory_acc': sum(per_epoch_accs) / len(per_epoch_accs),
            'retrained_acc': retrained_acc,
            'per_epoch': per_epoch_accs,
        }
    
    return results
```

### Step 5: Continual Learning Plasticity Test

```python
def continual_learning_plasticity_test(model, task_sequence, 
                                       use_growth=True, device='cpu'):
    """Test growth in continual learning with plasticity loss."""
    
    accuracies = []
    for task_idx, (train_data, test_data) in enumerate(task_sequence):
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
        
        # Grow if using structural plasticity
        if use_growth:
            for layer in model.layers:
                n_new = max(1, layer.out_features // 10)  # 10% growth per task
                model.grow_layer(model.layers.index(layer), n_new, optimizer)
        
        # Train on current task
        for epoch in range(50):
            train_one_epoch(model, train_data, optimizer, device)
        
        # Evaluate on all seen tasks
        task_accs = []
        for prev_train, prev_test in task_sequence[:task_idx + 1]:
            acc = evaluate(model, prev_test, device)
            task_accs.append(acc)
        accuracies.append(task_accs)
    
    return {
        'average_accuracy': sum(sum(a) for a in accuracies) / sum(len(a) for a in accuracies),
        'backward_transfer': accuracies[-1][0] - accuracies[0][0],  # Forgetting measure
        'per_task': accuracies,
    }
```

## Key Insights

### When Growth Works

1. **Sufficient integration time**: Newborn units need enough epochs to integrate into the optimization trajectory
2. **Appropriate initialization**: Gradient-matched or copy-perturb initialization outperforms random small init
3. **Continual learning**: Growth is competitive when new tasks require genuinely new capacity
4. **Warm optimizer state**: Fresh optimizer state or warmed momentum improves newborn integration

### When Pruning is Better

1. **Architecture search**: If goal is finding optimal sparse architecture, prune + retrain wins
2. **Trajectory-averaged performance**: Pruning maintains consistent performance throughout training
3. **Final subnetwork quality**: Pruned networks retrained from scratch outperform grown networks

### Pitfalls

1. **Backward starvation**: Newborn units receive weaker gradients — always verify gradient flow
2. **Insufficient evaluation**: Don't only measure final accuracy; evaluate trajectory and retrained performance
3. **MLP bias**: Growth performance in small MLP benchmarks does not transfer to harder convolutional settings
4. **Optimizer state mismatch**: Failing to update optimizer state after growth causes inconsistent updates
5. **Premature growth**: Growing too early or too frequently wastes capacity and destabilizes training

## Dependencies

```bash
pip install torch numpy
```

## Related Skills

- **snn-learning-survey**: Comprehensive SNN learning algorithms
- **neurotrain-local-learning-snn-benchmarking**: SNN training benchmarking
- **continual-learning-spiking-transformer**: Continual learning in spiking models
- **multi-plasticity-snn-training**: Multi-plasticity synergy in SNNs

## References

- Lillo, L., & Cheney, N. "On the Stability of Growth in Structural Plasticity." arXiv:2605.15435, 2026.
- Moczulski et al. "DCG: Deep Complex-valued Growth." 2024.
- Bellec et al. "A solution to the learning dilemma for recurrent networks of spiking neurons." 2020.
