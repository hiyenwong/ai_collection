---
name: snn-learning-neuromorphic
description: "Spiking Neural Network learning methods for neuromorphic computing — covering surrogate gradient, STDP, three-factor learning, DECOLLE, and sharpness-aware training. Use when training SNNs on neuromorphic hardware, implementing event-based learning, optimizing sparsity in spiking networks, or deploying energy-efficient AI. Trigger words: spiking neural network, SNN training, surrogate gradient, STDP, three-factor learning, DECOLLE, neuromorphic learning, event-based learning, temporal credit assignment"
---

# Spiking Neural Network Learning Methods

## Core Learning Paradigms

### 1. Surrogate Gradient Learning

Backpropagation through spikes using differentiable approximations:

```python
import torch
import torch.nn as nn

class SurrogateSpike(torch.autograd.Function):
    """Surrogate gradient for spiking function."""
    
    @staticmethod
    def forward(ctx, x, thresh=1.0):
        ctx.save_for_backward(x)
        ctx.thresh = thresh
        return (x > thresh).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        # Multi-Gaussian surrogate gradient
        sigma = 0.5
        grad = torch.exp(-((x - ctx.thresh) ** 2) / (2 * sigma**2))
        return grad_output * grad

# Usage
spike_fn = SurrogateSpike.apply
membrane_potential = torch.randn(10, 100)
spikes = spike_fn(membrane_potential)
```

### 2. Spike-Timing-Dependent Plasticity (STDP)

```python
def stdp_update(weights, pre_spikes, post_spikes, dt=1.0):
    """STDP weight update rule.
    
    Args:
        weights: Synaptic weight matrix (pre x post)
        pre_spikes: Presynaptic spike times
        post_spikes: Postsynaptic spike times
        dt: Time resolution
    """
    # Calculate timing differences
    delta_t = post_spikes[:, None] - pre_spikes[None, :]
    
    # LTP (pre before post)
    ltp = np.where(delta_t > 0, 
                   np.exp(-delta_t / 20.0),  # tau_plus = 20ms
                   0)
    
    # LTD (post before pre)
    ltd = np.where(delta_t < 0, 
                   -np.exp(delta_t / 20.0),  # tau_minus = 20ms
                   0)
    
    # Weight update
    dw = ltp + ltd
    return weights + dw * 0.01  # learning rate
```

### 3. Three-Factor Learning

```python
def three_factor_learning(weights, pre_spikes, post_spikes, modulatory_signal):
    """Three-factor learning rule with modulatory signal.
    
    Combines pre/post activity with global modulatory signal
    (e.g., dopamine, reward prediction error).
    """
    # Hebbian term (pre-post correlation)
    hebbian = pre_spikes[:, None] * post_spikes[None, :]
    
    # Modulated update
    dw = modulatory_signal * hebbian
    
    return weights + dw * learning_rate
```

### 4. DECOLLE (Deep Continuous Local Learning)

```python
class DECOLLELayer(nn.Module):
    """DECOLLE layer with local learning rule."""
    
    def __init__(self, n_in, n_out, n_classes):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(n_out, n_in))
        self.readout = nn.Parameter(torch.randn(n_classes, n_out))
        
    def forward(self, x):
        # Local loss for immediate feedback
        local_pred = self.readout @ x
        local_loss = F.cross_entropy(local_pred, target)
        
        # Synaptic update using local gradient
        with torch.no_grad():
            grad = torch.autograd.grad(local_loss, self.weight, retain_graph=True)[0]
            self.weight -= lr * grad
        
        return x @ self.weight.T
```

## Sharpness-Aware Surrogate Training (SAST)

For on-sensor SNN training with hardware-aware optimization:

```python
def sast_optimizer(model, data, rho=0.05, lr=0.01):
    """Sharpness-Aware Surrogate Training.
    
    Minimizes both loss and loss sharpness for robust training.
    """
    # First forward-backward pass
    loss = compute_loss(model, data)
    loss.backward()
    
    # Compute perturbation for sharpness
    with torch.no_grad():
        perturbations = {}
        for name, param in model.named_parameters():
            if param.grad is not None:
                perturbations[name] = rho * param.grad / (param.grad.norm() + 1e-8)
                param.data += perturbations[name]
    
    # Second forward pass with perturbed weights
    loss_sharp = compute_loss(model, data)
    
    # Restore weights and update
    with torch.no_grad():
        for name, param in model.named_parameters():
            param.data -= perturbations.get(name, 0)
        
        # Combined update
        for name, param in model.named_parameters():
            if param.grad is not None:
                param.data -= lr * (param.grad + loss_sharp.grad)
```

## Key Design Patterns

### Temporal Credit Assignment

1. **Event-based backpropagation**: Only propagate through spike events
2. **Memory-efficient replay**: Store only spike times, not full membrane trajectories
3. **Local approximations**: Use eligibility traces for online learning

### Energy-Efficient Training

1. **Sparse connectivity**: Prune weak synapses during training
2. **Low-precision weights**: Quantize to 4-8 bit for neuromorphic deployment
3. **Event-driven computation**: Skip computations for silent neurons

## Deployment Pipeline

```python
# Training pipeline
def train_snn(model, train_loader, epochs=100):
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    surrogate = SurrogateSpike.apply
    
    for epoch in range(epochs):
        for data, target in train_loader:
            optimizer.zero_grad()
            
            # Forward pass with surrogate gradients
            output = model(data, surrogate_fn=surrogate)
            loss = F.cross_entropy(output, target)
            
            loss.backward()
            optimizer.step()
            
        # Optional: Apply STDP for biological plausibility
        if epoch % 10 == 0:
            apply_stdp_regularization(model)

# Export to neuromorphic format
def export_to_neuromorphic(model, format='loihi'):
    """Export trained SNN to neuromorphic hardware format."""
    if format == 'loihi':
        return export_to_loihi(model)
    elif format == 'speck':
        return export_to_speck(model)
    elif format == 'dynap':
        return export_to_dynapcnns(model)
```

## Performance Optimization

1. **Sparsity analysis**: Monitor firing rates and synaptic sparsity
2. **Temporal compression**: Reduce time steps without accuracy loss
3. **Hardware-aware quantization**: Match precision to target hardware

## Activation Keywords

- spiking neural network, SNN training, surrogate gradient
- STDP, three-factor learning, DECOLLE, neuromorphic learning
- event-based learning, temporal credit assignment
- sharpness-aware training, on-sensor training

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify the user's specific question or task related to Snn Learning Neuromorphic
2. Gather relevant context from files or user input
3. Apply Snn Learning Neuromorphic methodology to address the request
4. Provide clear results with actionable insights

## Examples

### Basic usage
```
User: "Help me with snn learning neuromorphic"
→ Understand requirements → Apply methodology → Provide results
```

### Advanced usage
```
User: "I need detailed Snn Learning Neuromorphic assistance"
→ Clarify scope → Execute analysis → Present findings
```
