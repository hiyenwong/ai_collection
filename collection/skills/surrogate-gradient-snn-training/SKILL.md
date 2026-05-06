---
name: surrogate-gradient-snn-training
description: "Surrogate Gradient Learning for Spiking Neural Networks - comprehensive training framework using differentiable surrogate functions to overcome the non-differentiability of spike functions. Includes multiple surrogate gradient types (fast-sigmoid, exponential, arctan, erf), temporal batch normalization, neuron normalization, and advanced training strategies for deep SNNs. Activation: surrogate gradient SNN, differentiable spike, spiking neural network training, SNN backpropagation, time surrogate gradient."
tags: ["spiking-neural-networks", "surrogate-gradient", "SNN-training", "backpropagation-through-time", "differentiable-spike", "temporal-credit-assignment", "neuromorphic-deep-learning"]
---

# Surrogate Gradient Learning for Spiking Neural Networks

## Overview

Surrogate gradient learning is the dominant training method for Spiking Neural Networks (SNNs), overcoming the non-differentiability of the spike function by using smooth approximations during backpropagation while maintaining discrete spikes during forward passes.

## The Problem: Non-Differentiable Spike Functions

```
Spike Function (Heaviside Step):
    s[t] = Θ(v[t] - v_th)
    
    where Θ(x) = {1 if x >= 0, 0 if x < 0}
    
Derivative:
    dΘ/dx = 0 (almost everywhere) or undefined (at x=0)
    
This prevents gradient flow during backpropagation!
```

## The Solution: Surrogate Gradients

```
Forward Pass: Use discrete spikes (non-differentiable)
Backward Pass: Use smooth surrogate gradient (differentiable)

Surrogate Function σ(x) ≈ Θ(x) but with well-defined derivatives
```

## Surrogate Gradient Functions

### 1. Fast Sigmoid (Most Common)

```python
import torch
import torch.nn as nn

def fast_sigmoid_surrogate(x, alpha=1.0):
    """
    Fast sigmoid surrogate gradient.
    
    σ(x) = x / (1 + |x|)
    dσ/dx = 1 / (1 + |x|)²
    
    Args:
        x: Membrane potential - threshold (v - v_th)
        alpha: Steepness parameter (higher = steeper)
    """
    return x / (1.0 + torch.abs(x * alpha))

class FastSigmoidSurrogate(torch.autograd.Function):
    """
    Fast sigmoid surrogate with custom forward/backward.
    """
    
    @staticmethod
    def forward(ctx, x, alpha=1.0):
        ctx.save_for_backward(x)
        ctx.alpha = alpha
        # Forward: Heaviside step function
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        alpha = ctx.alpha
        
        # Backward: Fast sigmoid derivative
        grad_input = grad_output * alpha / (1.0 + torch.abs(x * alpha))**2
        return grad_input, None
```

### 2. Exponential Surrogate

```python
class ExponentialSurrogate(torch.autograd.Function):
    """
    Exponential surrogate gradient.
    
    σ(x) = exp(-|x|)
    dσ/dx = -sign(x) * exp(-|x|)
    
    Properties:
    - Maximum gradient at threshold
    - Smooth everywhere
    - Bounded derivative
    """
    
    @staticmethod
    def forward(ctx, x, alpha=1.0):
        ctx.save_for_backward(x)
        ctx.alpha = alpha
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        alpha = ctx.alpha
        
        # Exponential derivative
        abs_x = torch.abs(x * alpha)
        grad_input = grad_output * alpha * torch.exp(-abs_x)
        return grad_input, None
```

### 3. Arctangent Surrogate

```python
class ArctanSurrogate(torch.autograd.Function):
    """
    Arctangent surrogate gradient.
    
    σ(x) = arctan(αx) / π + 0.5
    dσ/dx = α / (π(1 + (αx)²))
    
    Properties:
    - Normalized to [0, 1]
    - Smooth transitions
    - Used in some implementations
    """
    
    @staticmethod
    def forward(ctx, x, alpha=1.0):
        ctx.save_for_backward(x)
        ctx.alpha = alpha
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        alpha = ctx.alpha
        
        # Arctangent derivative
        grad_input = grad_output * alpha / (torch.pi * (1 + (x * alpha)**2))
        return grad_input, None
```

### 4. Super (SuperSpike) Surrogate

```python
class SuperSurrogate(torch.autograd.Function):
    """
    SuperSpike surrogate with adaptive width.
    
    σ(x) = 1 / (1 + |x|)²
    
    Based on: Zenke & Vogels (2021) "The Remarkable Robustness of Surrogate Gradient Learning"
    """
    
    @staticmethod
    def forward(ctx, x, beta=0.3):
        ctx.save_for_backward(x)
        ctx.beta = beta
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        beta = ctx.beta
        
        # SuperSpike derivative
        abs_x = torch.abs(x)
        grad_input = grad_output / (beta * (1.0 + abs_x / beta)**2)
        return grad_input, None
```

### 5. Sigmoid Surrogate

```python
class SigmoidSurrogate(torch.autograd.Function):
    """
    Standard sigmoid surrogate.
    
    σ(x) = 1 / (1 + exp(-αx))
    dσ/dx = α * σ(x) * (1 - σ(x))
    """
    
    @staticmethod
    def forward(ctx, x, alpha=10.0):
        ctx.save_for_backward(x)
        ctx.alpha = alpha
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        alpha = ctx.alpha
        
        sigmoid = torch.sigmoid(x * alpha)
        grad_input = grad_output * alpha * sigmoid * (1 - sigmoid)
        return grad_input, None
```

### 6. Gaussian (Spike-Response Model) Surrogate

```python
class GaussianSurrogate(torch.autograd.Function):
    """
    Gaussian/error function surrogate.
    
    σ(x) = exp(-x² / 2σ²) / √(2πσ²)
    
    Matches the derivative of the error function,
    often used with probabilistic neuron models.
    """
    
    @staticmethod
    def forward(ctx, x, sigma=0.5):
        ctx.save_for_backward(x)
        ctx.sigma = sigma
        return (x >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        sigma = ctx.sigma
        
        # Gaussian derivative
        grad_input = grad_output * torch.exp(-x**2 / (2 * sigma**2)) / (sigma * torch.sqrt(torch.tensor(2 * torch.pi)))
        return grad_input, None
```

## Complete Surrogate Neuron Implementation

```python
import torch
import torch.nn as nn

class SurrogateGradientNeuron(nn.Module):
    """
    Spiking neuron with configurable surrogate gradient.
    
    Supports multiple neuron models:
    - LIF: Leaky Integrate-and-Fire
    - ALIF: Adaptive LIF
    - PLIF: Parametric LIF
    """
    
    SURROGATE_FUNCTIONS = {
        'fast_sigmoid': FastSigmoidSurrogate,
        'exponential': ExponentialSurrogate,
        'arctan': ArctanSurrogate,
        'super': SuperSurrogate,
        'sigmoid': SigmoidSurrogate,
        'gaussian': GaussianSurrogate,
    }
    
    def __init__(
        self,
        neuron_type='LIF',
        surrogate_type='fast_sigmoid',
        surrogate_params=None,
        tau_mem=20.0,
        tau_adapt=None,
        v_th=1.0,
        v_reset=0.0,
        spike_fn=None
    ):
        super().__init__()
        
        self.neuron_type = neuron_type
        self.surrogate_type = surrogate_type
        self.surrogate_params = surrogate_params or {}
        
        # Neuron parameters
        self.tau_mem = tau_mem
        self.v_th = v_th
        self.v_reset = v_reset
        
        # Adaptive threshold parameters (for ALIF)
        if neuron_type == 'ALIF':
            self.tau_adapt = tau_adapt or 100.0
            self.beta_adapt = 1.8  # Adaptation strength
        
        # Get surrogate function
        if spike_fn is None:
            self.spike_fn = self.SURROGATE_FUNCTIONS[surrogate_type]
        else:
            self.spike_fn = spike_fn
    
    def forward(self, x, state=None):
        """
        Forward pass through spiking neuron.
        
        Args:
            x: Input current (batch_size,)
            state: Dictionary with 'v' (membrane potential) and optionally 'v_th_adapt'
        
        Returns:
            spike: Output spike (0 or 1)
            new_state: Updated state dictionary
        """
        batch_size = x.shape[0]
        
        # Initialize state if needed
        if state is None:
            state = self.reset_state(batch_size, x.device)
        
        v = state['v']
        
        # Adaptive threshold (for ALIF)
        if self.neuron_type == 'ALIF':
            v_th = state.get('v_th_adapt', self.v_th)
        else:
            v_th = self.v_th
        
        # Membrane potential update
        alpha = torch.exp(-1.0 / self.tau_mem)
        v = alpha * v + (1 - alpha) * x
        
        # Spike generation with surrogate gradient
        spike = self.spike_fn.apply(v - v_th, **self.surrogate_params)
        
        # Reset membrane potential after spike
        v = v * (1 - spike) + self.v_reset * spike
        
        # Update adaptive threshold
        if self.neuron_type == 'ALIF':
            alpha_adapt = torch.exp(-1.0 / self.tau_adapt)
            v_th = alpha_adapt * v_th + spike * self.beta_adapt
            new_state = {'v': v, 'v_th_adapt': v_th}
        else:
            new_state = {'v': v}
        
        return spike, new_state
    
    def reset_state(self, batch_size, device):
        """Initialize neuron state."""
        state = {'v': torch.zeros(batch_size, device=device)}
        if self.neuron_type == 'ALIF':
            state['v_th_adapt'] = torch.full((batch_size,), self.v_th, device=device)
        return state
```

## SNN Layer with Temporal Processing

```python
class SpikingLayer(nn.Module):
    """
    Spiking neural network layer with temporal dynamics.
    
    Processes input over time steps and maintains state.
    """
    
    def __init__(
        self,
        in_features,
        out_features,
        neuron_type='LIF',
        surrogate_type='fast_sigmoid',
        surrogate_alpha=1.0,
        tau_mem=20.0,
        time_steps=100,
        dropout=0.0,
        use_recurrent=False,
        recurrent_tau=5.0
    ):
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        self.time_steps = time_steps
        self.use_recurrent = use_recurrent
        
        # Feedforward weights
        self.linear = nn.Linear(in_features, out_features)
        
        # Recurrent weights (optional)
        if use_recurrent:
            self.recurrent = nn.Linear(out_features, out_features, bias=False)
            self.recurrent_tau = recurrent_tau
        
        # Neuron model
        self.neuron = SurrogateGradientNeuron(
            neuron_type=neuron_type,
            surrogate_type=surrogate_type,
            surrogate_params={'alpha': surrogate_alpha},
            tau_mem=tau_mem,
            v_th=1.0
        )
        
        # Dropout for regularization
        self.dropout = nn.Dropout(dropout) if dropout > 0 else None
    
    def forward(self, x, states=None):
        """
        Forward pass over time.
        
        Args:
            x: Input spikes (batch, time, features) or (batch*time, features)
            states: Initial states for neurons (optional)
        
        Returns:
            spikes: Output spike train (batch, time, out_features)
            membrane_trace: Membrane potential over time
            final_states: Final neuron states
        """
        batch_size = x.shape[0]
        
        # Handle different input shapes
        if x.dim() == 2:
            # Assume (batch*time, features) - reshape
            x = x.view(batch_size // self.time_steps, self.time_steps, -1)
        
        # Initialize states
        if states is None:
            states = self.reset_states(batch_size, x.device)
        
        # Collect outputs over time
        spike_list = []
        membrane_list = []
        
        for t in range(self.time_steps):
            # Current input
            x_t = x[:, t, :]  # (batch, in_features)
            
            # Linear transformation
            current = self.linear(x_t)  # (batch, out_features)
            
            # Add recurrent input
            if self.use_recurrent:
                rec_current = self.recurrent(states['spike'])
                # Filter with exponential decay
                alpha_rec = torch.exp(-1.0 / self.recurrent_tau)
                states['recurrent_mem'] = alpha_rec * states['recurrent_mem'] + (1 - alpha_rec) * rec_current
                current = current + states['recurrent_mem']
            
            # Apply dropout
            if self.dropout is not None:
                current = self.dropout(current)
            
            # Neuron dynamics
            spike, new_neuron_state = self.neuron(current, states['neuron'])
            
            # Update states
            states['neuron'] = new_neuron_state
            if self.use_recurrent:
                states['spike'] = spike
            
            # Store outputs
            spike_list.append(spike)
            membrane_list.append(new_neuron_state['v'])
        
        # Stack over time
        spikes = torch.stack(spike_list, dim=1)  # (batch, time, out_features)
        membrane_trace = torch.stack(membrane_list, dim=1)
        
        return spikes, membrane_trace, states
    
    def reset_states(self, batch_size, device):
        """Reset all states."""
        states = {
            'neuron': self.neuron.reset_state(batch_size, device),
        }
        if self.use_recurrent:
            states['spike'] = torch.zeros(batch_size, self.out_features, device=device)
            states['recurrent_mem'] = torch.zeros(batch_size, self.out_features, device=device)
        return states
```

## Temporal Batch Normalization

```python
class TemporalBatchNorm(nn.Module):
    """
    Batch normalization adapted for temporal sequences.
    
    Normalizes across batch and time dimensions while
    maintaining temporal statistics separately.
    """
    
    def __init__(self, num_features, eps=1e-5, momentum=0.1):
        super().__init__()
        
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum
        
        # Learnable parameters
        self.weight = nn.Parameter(torch.ones(num_features))
        self.bias = nn.Parameter(torch.zeros(num_features))
        
        # Running statistics
        self.register_buffer('running_mean', torch.zeros(num_features))
        self.register_buffer('running_var', torch.ones(num_features))
    
    def forward(self, x):
        """
        Args:
            x: (batch, time, features) or (batch, features)
        """
        if self.training:
            # Compute statistics across batch and time
            if x.dim() == 3:
                mean = x.mean(dim=[0, 1])
                var = x.var(dim=[0, 1], unbiased=False)
            else:
                mean = x.mean(dim=0)
                var = x.var(dim=0, unbiased=False)
            
            # Update running statistics
            self.running_mean = (1 - self.momentum) * self.running_mean + self.momentum * mean
            self.running_var = (1 - self.momentum) * self.running_var + self.momentum * var
        else:
            mean = self.running_mean
            var = self.running_var
        
        # Normalize
        x_normalized = (x - mean) / torch.sqrt(var + self.eps)
        
        # Scale and shift
        return x_normalized * self.weight + self.bias


class NeuronNorm(nn.Module):
    """
    Neuron-wise normalization for SNNs.
    
    Normalizes each neuron's activity separately,
    helps with training stability.
    """
    
    def __init__(self, num_neurons, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.scale = nn.Parameter(torch.ones(num_neurons))
    
    def forward(self, x):
        """Normalize per neuron."""
        mean = x.mean(dim=-1, keepdim=True)
        std = x.std(dim=-1, keepdim=True)
        return self.scale * (x - mean) / (std + self.eps)
```

## Deep SNN Architecture

```python
class DeepSNN(nn.Module):
    """
    Deep Spiking Neural Network with surrogate gradient training.
    
    Architecture: Input -> [Conv/ReLU] -> SNN Layers -> Output
    """
    
    def __init__(
        self,
        input_size,
        hidden_sizes=[512, 256],
        output_size=10,
        time_steps=100,
        neuron_type='LIF',
        surrogate_type='fast_sigmoid',
        surrogate_alpha=1.0,
        tau_mem=20.0,
        use_readout='mean',  # 'mean', 'last', 'max', 'spike_count'
        dropout=0.2
    ):
        super().__init__()
        
        self.input_size = input_size
        self.output_size = output_size
        self.time_steps = time_steps
        self.use_readout = use_readout
        
        # Build layers
        layers = []
        prev_size = input_size
        
        for i, hidden_size in enumerate(hidden_sizes):
            layers.append(
                SpikingLayer(
                    in_features=prev_size,
                    out_features=hidden_size,
                    neuron_type=neuron_type,
                    surrogate_type=surrogate_type,
                    surrogate_alpha=surrogate_alpha,
                    tau_mem=tau_mem,
                    time_steps=time_steps,
                    dropout=dropout if i < len(hidden_sizes) - 1 else 0.0,
                    use_recurrent=(i == 0)  # Recurrent in first layer
                )
            )
            layers.append(TemporalBatchNorm(hidden_size))
            prev_size = hidden_size
        
        self.snn_layers = nn.ModuleList(layers)
        
        # Readout layer (non-spiking)
        self.readout = nn.Linear(prev_size, output_size)
    
    def forward(self, x):
        """
        Forward pass.
        
        Args:
            x: Input (batch, time, input_features) or (batch, input_features)
        
        Returns:
            output: (batch, output_size)
            spike_counts: Spike counts per layer for regularization
        """
        # Encode input to spikes if needed
        if x.dim() == 2:
            x = x.unsqueeze(1).repeat(1, self.time_steps, 1)
        
        batch_size = x.shape[0]
        
        # Pass through SNN layers
        current = x
        spike_counts = []
        states = None
        
        for i, layer in enumerate(self.snn_layers):
            if isinstance(layer, SpikingLayer):
                current, membrane, states = layer(current, states)
                spike_counts.append(current.sum())
            else:  # BatchNorm
                # Reshape for batch norm: (batch*time, features)
                original_shape = current.shape
                current = layer(current.view(-1, current.shape[-1]))
                current = current.view(original_shape)
        
        # Readout
        if self.use_readout == 'mean':
            # Average over time
            readout_input = current.mean(dim=1)
        elif self.use_readout == 'last':
            # Use last time step
            readout_input = current[:, -1, :]
        elif self.use_readout == 'spike_count':
            # Total spike count
            readout_input = current.sum(dim=1)
        elif self.use_readout == 'max':
            # Max membrane potential
            readout_input = current.max(dim=1)[0]
        
        output = self.readout(readout_input)
        
        return output, spike_counts
    
    def reset_states(self):
        """Reset all layer states."""
        for layer in self.snn_layers:
            if isinstance(layer, SpikingLayer):
                layer.reset_states()
```

## Training Pipeline

```python
class SNNTrainer:
    """
    Training pipeline for Spiking Neural Networks.
    
    Handles:
    - Surrogate gradient backpropagation
    - Temporal credit assignment
    - Activity regularization
    - Spike rate monitoring
    """
    
    def __init__(
        self,
        model,
        optimizer,
        criterion,
        device='cuda',
        reg_lambda=1e-5,  # Spike rate regularization
        target_spike_rate=0.1
    ):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.reg_lambda = reg_lambda
        self.target_spike_rate = target_spike_rate
    
    def train_step(self, x, y):
        """Single training step."""
        self.model.train()
        
        x = x.to(self.device)
        y = y.to(self.device)
        
        # Forward pass
        output, spike_counts = self.model(x)
        
        # Classification loss
        loss = self.criterion(output, y)
        
        # Spike rate regularization
        total_spikes = sum(spike_counts)
        avg_spike_rate = total_spikes / (x.shape[0] * self.model.time_steps)
        rate_loss = self.reg_lambda * (avg_spike_rate - self.target_spike_rate)**2
        
        total_loss = loss + rate_loss
        
        # Backward pass
        self.optimizer.zero_grad()
        total_loss.backward()
        
        # Gradient clipping for stability
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
        
        self.optimizer.step()
        
        return {
            'loss': loss.item(),
            'rate_loss': rate_loss.item(),
            'total_loss': total_loss.item(),
            'accuracy': (output.argmax(dim=1) == y).float().mean().item(),
            'avg_spike_rate': avg_spike_rate.item()
        }
    
    def validate(self, dataloader):
        """Validation loop."""
        self.model.eval()
        total_loss = 0.0
        total_acc = 0.0
        total_spikes = 0
        
        with torch.no_grad():
            for x, y in dataloader:
                x = x.to(self.device)
                y = y.to(self.device)
                
                output, spike_counts = self.model(x)
                loss = self.criterion(output, y)
                
                total_loss += loss.item() * x.shape[0]
                total_acc += (output.argmax(dim=1) == y).sum().item()
                total_spikes += sum(s.item() for s in spike_counts)
        
        n_samples = len(dataloader.dataset)
        return {
            'loss': total_loss / n_samples,
            'accuracy': total_acc / n_samples,
            'avg_spike_rate': total_spikes / (n_samples * self.model.time_steps)
        }
    
    def train_epoch(self, train_loader, val_loader=None):
        """Train for one epoch."""
        train_metrics = []
        
        for x, y in train_loader:
            metrics = self.train_step(x, y)
            train_metrics.append(metrics)
        
        # Average training metrics
        avg_train = {
            k: sum(m[k] for m in train_metrics) / len(train_metrics)
            for k in train_metrics[0].keys()
        }
        
        # Validation
        if val_loader is not None:
            val_metrics = self.validate(val_loader)
            return avg_train, val_metrics
        
        return avg_train, None


# Example training loop
def train_snn(
    model,
    train_loader,
    val_loader,
    epochs=100,
    lr=0.001,
    device='cuda'
):
    """Complete training function."""
    
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    criterion = nn.CrossEntropyLoss()
    
    trainer = SNNTrainer(
        model=model,
        optimizer=optimizer,
        criterion=criterion,
        device=device
    )
    
    best_acc = 0.0
    history = []
    
    for epoch in range(epochs):
        train_metrics, val_metrics = trainer.train_epoch(train_loader, val_loader)
        scheduler.step()
        
        history.append({
            'epoch': epoch,
            'train': train_metrics,
            'val': val_metrics
        })
        
        if val_metrics and val_metrics['accuracy'] > best_acc:
            best_acc = val_metrics['accuracy']
            torch.save(model.state_dict(), 'best_snn_model.pt')
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Train Acc={train_metrics['accuracy']:.4f}, "
                  f"Val Acc={val_metrics['accuracy']:.4f}, "
                  f"Spike Rate={train_metrics['avg_spike_rate']:.4f}")
    
    return history
```

## Advanced Techniques

### 1. Adaptive Surrogate Gradients

```python
class AdaptiveSurrogate(nn.Module):
    """
    Adaptive surrogate gradient that adjusts steepness during training.
    """
    
    def __init__(self, initial_alpha=1.0, min_alpha=0.5, max_alpha=10.0):
        super().__init__()
        self.alpha = nn.Parameter(torch.tensor(initial_alpha))
        self.min_alpha = min_alpha
        self.max_alpha = max_alpha
    
    def forward(self, x):
        # Clamp alpha to valid range
        alpha = torch.clamp(self.alpha, self.min_alpha, self.max_alpha)
        
        # Forward: Heaviside
        spike = (x >= 0).float()
        
        # Backward: Fast sigmoid with adaptive alpha
        if self.training:
            spike.register_hook(
                lambda grad: grad * alpha / (1.0 + torch.abs(x * alpha))**2
            )
        
        return spike
```

### 2. Population Coding Loss

```python
class PopulationCodeLoss(nn.Module):
    """
    Loss function for population-coded outputs in SNNs.
    
    Uses spike timing or rates to encode continuous values.
    """
    
    def __init__(self, coding_scheme='rate', tau_readout=20.0):
        super().__init__()
        self.coding_scheme = coding_scheme
        self.tau_readout = tau_readout
    
    def forward(self, spike_trains, target):
        """
        Args:
            spike_trains: (batch, time, neurons) spike trains
            target: (batch, output_dim) target values
        """
        if self.coding_scheme == 'rate':
            # Population rate coding
            rates = spike_trains.sum(dim=1)  # Spike counts
            decoded = self._decode_population(rates)
            loss = F.mse_loss(decoded, target)
            
        elif self.coding_scheme == 'time_to_first_spike':
            # Time-to-first-spike coding
            spike_times = self._get_first_spike_times(spike_trains)
            decoded = self._decode_temporal(spike_times)
            loss = F.mse_loss(decoded, target)
            
        elif self.coding_scheme == 'rank_order':
            # Rank-order coding
            spike_order = self._get_spike_order(spike_trains)
            loss = self._rank_order_loss(spike_order, target)
        
        return loss
    
    def _decode_population(self, rates):
        """Decode from population rates."""
        # Weighted average of preferred values
        return rates / (rates.sum(dim=-1, keepdim=True) + 1e-8)
    
    def _get_first_spike_times(self, spike_trains):
        """Extract time of first spike for each neuron."""
        # Find first spike time
        spike_times = (spike_trains > 0).float().argmax(dim=1)
        # If no spike, return large value
        no_spike = (spike_trains.sum(dim=1) == 0)
        spike_times = spike_times.float() + no_spike.float() * 1e6
        return spike_times
```

### 3. Multi-Timescale Learning

```python
class MultiTimescaleSNN(nn.Module):
    """
    SNN with multiple timescales for different neurons.
    
    Mimics biological heterogeneity in membrane time constants.
    """
    
    def __init__(self, sizes, tau_range=(10, 100)):
        super().__init__()
        
        # Assign different time constants to different neurons
        self.tau_mem = nn.ParameterList()
        for size in sizes:
            # Log-uniform distribution of time constants
            log_tau_min, log_tau_max = np.log(tau_range[0]), np.log(tau_range[1])
            log_taus = torch.linspace(log_tau_min, log_tau_max, size)
            self.tau_mem.append(nn.Parameter(torch.exp(log_taus)))
    
    def get_decay_constants(self, layer_idx):
        """Get decay constants for a layer."""
        return torch.exp(-1.0 / self.tau_mem[layer_idx])
```

## Performance Comparison

```python
def compare_surrogate_gradients():
    """
    Compare different surrogate gradient functions on benchmark task.
    """
    surrogates = [
        ('fast_sigmoid', {'alpha': 1.0}),
        ('exponential', {'alpha': 1.0}),
        ('super', {'beta': 0.3}),
        ('arctan', {'alpha': 2.0}),
    ]
    
    results = {}
    
    for name, params in surrogates:
        model = DeepSNN(
            input_size=784,
            hidden_sizes=[512, 256],
            output_size=10,
            surrogate_type=name,
            surrogate_alpha=params.get('alpha', 1.0)
        )
        
        # Train and evaluate
        history = train_snn(model, train_loader, val_loader, epochs=50)
        results[name] = history
    
    return results
```

## References

1. Neftci, E. O., Mostafa, H., & Zenke, F. (2019). Surrogate gradient learning in spiking neural networks. IEEE Signal Processing Magazine.
2. Zenke, F., & Vogels, T. P. (2021). The remarkable robustness of surrogate gradient learning for instilling complex function in spiking neural networks. Neural Computation.
3. Kaiser, J., Mostafa, H., & Neftci, E. (2020). Synaptic plasticity dynamics for deep continuous local learning. Frontiers in Neuroscience.
4. Fang, W., et al. (2021). Incorporating learnable membrane time constant to enhance learning of spiking neural networks. IEEE/CVF ICCV.
5. Zenke, F., & Ganguli, S. (2018). Superspike: Supervised learning in multi-layer spiking neural networks. Neural Computation.

## Activation Keywords

- surrogate gradient SNN
- differentiable spike
- spiking neural network training
- SNN backpropagation
- surrogate gradient function
- temporal credit assignment
- surrogate gradient descent
- spike function derivative
- SNN optimization
- neuromorphic deep learning
- spiking neuron backpropagation
