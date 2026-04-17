# Implementation Patterns: Heterogeneous Delay SNN Working Memory

## 1. Heterogeneous Delay Weight Tensor

```python
import torch
import torch.nn as nn

class HeterogeneousDelayLayer(nn.Module):
    """Recurrent layer with D heterogeneous delay channels per synapse.
    
    Weight tensor W ∈ R^{N×N×D} where D = number of delay channels.
    Each delay channel d represents a connection that fires d timesteps later.
    """
    def __init__(self, n_neurons: int, n_delays: int = 41):
        super().__init__()
        self.n = n_neurons
        self.d = n_delays
        # W[i, j, d] = weight from neuron j to neuron i with delay d
        self.weights = nn.Parameter(torch.randn(n_neurons, n_neurons, n_delays) * 0.1)
        # Delay line buffer: stores past spikes for each neuron
        self.delay_buffer: torch.Tensor | None = None
        
    def forward(self, spikes: torch.Tensor) -> torch.Tensor:
        """Compute delayed synaptic input from past spikes.
        
        Args:
            spikes: (N,) binary spike vector at current timestep
            
        Returns:
            (N,) synaptic current from all delayed connections
        """
        # Append current spikes to delay buffer
        # buffer shape: (D, N) — buffer[d] = spikes from d steps ago
        self.delay_buffer = torch.cat([spikes.unsqueeze(0), self.delay_buffer[:-1]], dim=0)
        
        # Contract: input[d] = sum_j W[i,j,d] * buffer[d, j]
        # result[i] = sum_{j,d} W[i,j,d] * buffer[d, j]
        synaptic_input = torch.einsum('ijd,dj->i', self.weights, self.delay_buffer)
        return synaptic_input
    
    def reset(self, batch_size: int = 1, device='cpu'):
        self.delay_buffer = torch.zeros(self.d, self.n, device=device)
```

## 2. LIF Neuron with Surrogate Gradient

```python
class SurrogateSpike(torch.autograd.Function):
    """Spike function with surrogate gradient for BPTT.
    
    Forward: Heaviside step (spike if V > threshold)
    Backward: Smooth approximation (e.g., sigmoid derivative)
    """
    @staticmethod
    def forward(ctx, v_mem, threshold=1.0, width=0.5):
        ctx.save_for_backward(v_mem)
        ctx.threshold = threshold
        ctx.width = width
        return (v_mem > threshold).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        v_mem, = ctx.saved_tensors
        # Surrogate: derivative of sigmoid with scaled width
        grad = grad_output * torch.exp(-ctx.width * (v_mem - ctx.threshold).abs())
        return grad

class LIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire neuron with surrogate gradient spiking."""
    def __init__(self, n_neurons: int, tau_mem: float = 20.0, threshold: float = 1.0, dt: float = 1.0):
        super().__init__()
        self.n = n_neurons
        self.tau_mem = tau_mem
        self.decay = torch.exp(-dt / tau_mem)
        self.threshold = threshold
        
    def forward(self, input_current: torch.Tensor, v_mem: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """One timestep of LIF dynamics.
        
        Args:
            input_current: (N,) synaptic input current
            v_mem: (N,) membrane potential from previous step
            
        Returns:
            spikes: (N,) binary output spikes
            v_mem: (N,) updated membrane potential
        """
        # Update membrane potential (leaky integration)
        v_mem = self.decay * v_mem + (1 - self.decay) * input_current
        
        # Spike with surrogate gradient
        spikes = SurrogateSpike.apply(v_mem, self.threshold)
        
        # Reset membrane potential after spike (soft reset)
        v_mem = v_mem - spikes * self.threshold
        return spikes, v_mem
    
    def reset(self, batch_size: int = 1, device='cpu'):
        return torch.zeros(self.n, device=device)
```

## 3. Full Recurrent SNN with Heterogeneous Delays

```python
class HeterogeneousDelaySNN(nn.Module):
    """Recurrent SNN with heterogeneous synaptic delays for working memory.
    
    Architecture:
    - N recurrent neurons with D delay channels each
    - Weight tensor W ∈ R^{N×N×D}
    - Trained with surrogate-gradient BPTT
    
    Usage:
        model = HeterogeneousDelaySNN(n_neurons=512, n_delays=41)
        loss = train_on_patterns(model, target_patterns, T=1000)
    """
    def __init__(self, n_neurons: int = 512, n_delays: int = 41, tau_mem: float = 20.0):
        super().__init__()
        self.n = n_neurons
        self.d = n_delays
        self.delay_layer = HeterogeneousDelayLayer(n_neurons, n_delays)
        self.neuron = LIFNeuron(n_neurons, tau_mem=tau_mem)
        
    def forward(self, input_current: torch.Tensor, n_steps: int) -> torch.Tensor:
        """Run the network for n_steps and return all spike traces.
        
        Args:
            input_current: (T, N) external input over time
            n_steps: number of timesteps to simulate
            
        Returns:
            spike_trace: (T, N) binary spike tensor
        """
        device = input_current.device
        v_mem = self.neuron.reset(device=device)
        self.delay_layer.reset(device=device)
        
        spike_trace = []
        for t in range(n_steps):
            # Recurrent input from heterogeneous delays
            rec_input = self.delay_layer.forward(torch.zeros(self.n, device=device))
            
            # Total input = external + recurrent
            total_input = input_current[t] + rec_input
            
            # LIF step
            spikes, v_mem = self.neuron(total_input, v_mem)
            
            # Feed spikes back into delay buffer
            self.delay_layer(spikes)  # updates buffer internally
            
            spike_trace.append(spikes)
        
        return torch.stack(spike_trace)  # (T, N)
    
    def clamp_and_recall(self, init_pattern: torch.Tensor, n_clamp: int, n_free: int) -> torch.Tensor:
        """Clamp initial window then let network freely recall.
        
        Args:
            init_pattern: (n_clamp, N) initial spike pattern to clamp
            n_clamp: number of clamped timesteps
            n_free: number of free-running recall timesteps
            
        Returns:
            full_trace: (n_clamp + n_free, N) complete spike trace
        """
        device = init_pattern.device
        v_mem = self.neuron.reset(device=device)
        self.delay_layer.reset(device=device)
        
        spike_trace = []
        
        # Clamped phase: force specific spike patterns
        for t in range(n_clamp):
            spikes = init_pattern[t]
            rec_input = self.delay_layer(spikes)
            total_input = rec_input  # no external input
            _, v_mem = self.neuron(total_input, v_mem)
            spike_trace.append(spikes)
        
        # Free-running phase: network self-sustains
        for t in range(n_free):
            rec_input = self.delay_layer(spikes)
            spikes, v_mem = self.neuron(rec_input, v_mem)
            spike_trace.append(spikes)
        
        return torch.stack(spike_trace)
```

## 4. Training with Surrogate-Gradient BPTT

```python
def train_on_patterns(model: HeterogeneousDelaySNN,
                      target_patterns: torch.Tensor,
                      n_epochs: int = 1000,
                      lr: float = 1e-3,
                      motif_length: int = 41) -> list[float]:
    """Train the SNN to store and recall M target spike patterns.
    
    Each target pattern is a (T, N) binary tensor. Training decomposes
    patterns into overlapping motifs of length D and uses BPTT.
    
    Args:
        model: HeterogeneousDelaySNN
        target_patterns: (M, T, N) binary target spike patterns
        n_epochs: training epochs
        lr: learning rate
        motif_length: length of spiking motif window (should match n_delays)
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    losses = []
    
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        total_loss = 0.0
        
        for pattern_idx in range(target_patterns.shape[0]):
            target = target_patterns[pattern_idx]  # (T, N)
            T, N = target.shape
            
            # Forward pass: clamp initial window, then free recall
            n_clamp = motif_length
            init_pattern = target[:n_clamp]
            output = model.clamp_and_recall(init_pattern, n_clamp, T - n_clamp)
            
            # Compute loss on free-running portion
            # Use smoothed BCE or F1-based loss for spike precision
            output_free = output[n_clamp:]
            target_free = target[n_clamp:]
            
            # Temporal precision loss: penalize wrong spikes at wrong times
            loss = F.binary_cross_entropy_with_logits(
                output_free, target_free, reduction='mean'
            )
            total_loss += loss
        
        total_loss /= target_patterns.shape[0]
        total_loss.backward()
        optimizer.step()
        losses.append(total_loss.item())
        
    return losses
```

## 5. Spiking Motif Extraction and Evaluation

```python
def extract_motifs(spike_trace: torch.Tensor, motif_length: int = 41) -> list[torch.Tensor]:
    """Decompose spike trace into overlapping spiking motifs.
    
    Each motif is a contiguous window of length D that captures
    the local spike pattern structure.
    """
    T, N = spike_trace.shape
    motifs = []
    for t in range(T - motif_length + 1):
        motif = spike_trace[t:t + motif_length]  # (D, N)
        motifs.append(motif)
    return motifs

def compute_f1_score(predicted: torch.Tensor, target: torch.Tensor, 
                     tolerance: int = 1) -> float:
    """Compute F1 score for spike pattern matching with timing tolerance.
    
    A predicted spike within `tolerance` timesteps of a target spike
    counts as a true positive.
    """
    # Dilate target spikes by tolerance window
    dilated_target = torch.nn.functional.max_pool1d(
        target.T.unsqueeze(0), kernel_size=2 * tolerance + 1, stride=1, padding=tolerance
    ).squeeze(0).T
    
    tp = (predicted & dilated_target).sum().item()
    fp = (predicted & ~dilated_target).sum().item()
    fn = (~predicted & dilated_target).sum().item()
    
    precision = tp / max(tp + fp, 1)
    recall = tp / max(tp + fn, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-8)
    return f1

def evaluate_working_memory(model: HeterogeneousDelaySNN, 
                            test_patterns: torch.Tensor,
                            motif_length: int = 41) -> dict:
    """Evaluate working memory recall on test patterns.
    
    Returns dict with per-pattern F1 scores and overall mean F1.
    """
    f1_scores = []
    for i in range(test_patterns.shape[0]):
        target = test_patterns[i]
        T = target.shape[0]
        
        # Clamp initial motif, recall the rest
        output = model.clamp_and_recall(target[:motif_length], motif_length, T - motif_length)
        
        # Evaluate recall portion
        f1 = compute_f1_score(output[motif_length:], target[motif_length:])
        f1_scores.append(f1)
    
    return {
        'f1_scores': f1_scores,
        'mean_f1': sum(f1_scores) / len(f1_scores),
        'perfect_recall': all(f == 1.0 for f in f1_scores)
    }
```

## 6. Memory Propagation Analysis

```python
def analyze_recall_propagation(spike_trace: torch.Tensor, 
                               target: torch.Tensor,
                               motif_length: int = 41,
                               window_size: int = 50) -> list[float]:
    """Analyze how recall accuracy propagates forward in time.
    
    Measures F1 in sliding windows to observe recall emerging from
    the clamped initialization window and propagating forward.
    """
    T = spike_trace.shape[0]
    window_f1s = []
    
    for t_start in range(motif_length, T - window_size, window_size):
        window_pred = spike_trace[t_start:t_start + window_size]
        window_target = target[t_start:t_start + window_size]
        f1 = compute_f1_score(window_pred, window_target)
        window_f1s.append(f1)
    
    return window_f1s
```
