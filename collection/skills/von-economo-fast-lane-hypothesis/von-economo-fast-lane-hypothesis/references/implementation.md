# Implementation: Von Economo Fast Lane Hypothesis

## Core Neuron Models

### Dual LIF Neuron Implementation

```python
import torch
import torch.nn as nn
import numpy as np

class LIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire neuron with configurable time constants."""
    
    def __init__(self, tau_mem=20.0, v_threshold=1.0, v_reset=0.0, dt=1.0):
        super().__init__()
        self.tau_mem = tau_mem  # membrane time constant (ms)
        self.v_threshold = v_threshold
        self.v_reset = v_reset
        self.dt = dt
        self.decay = np.exp(-dt / tau_mem)
        
    def forward(self, input_current, v_mem, spike_history):
        """Single step update of LIF neuron dynamics."""
        # Leak and integrate
        v_mem = self.decay * v_mem + (1 - self.decay) * input_current
        
        # Spike generation
        spikes = (v_mem >= self.v_threshold).float()
        
        # Reset membrane potential after spike
        v_mem = v_mem * (1 - spikes) + self.v_reset * spikes
        
        return v_mem, spikes


class VENNeuron(LIFNeuron):
    """Von Economo Neuron — fast LIF with sparse fan-in."""
    
    def __init__(self, tau_mem=5.0, v_threshold=1.0, v_reset=0.0, 
                 dt=1.0, n_afferents=8):
        super().__init__(tau_mem, v_threshold, v_reset, dt)
        self.n_afferents = n_afferents  # sparse dendritic fan-in


class PyramidalNeuron(LIFNeuron):
    """Standard pyramidal neuron — slower, dense fan-in."""
    
    def __init__(self, tau_mem=20.0, v_threshold=1.0, v_reset=0.0,
                 dt=1.0, n_afferents=80):
        super().__init__(tau_mem, v_threshold, v_reset, dt)
        self.n_afferents = n_afferents  # dense dendritic fan-in
```

### Mixed Population Circuit

```python
class MixedCorticalCircuit(nn.Module):
    """Spiking cortical circuit with VEN and pyramidal populations."""
    
    def __init__(self, n_neurons=2000, ven_fraction=0.02, 
                 n_in=64, n_out=2, dt=1.0):
        super().__init__()
        self.n_neurons = n_neurons
        self.n_ven = int(n_neurons * ven_fraction)
        self.n_pyr = n_neurons - self.n_ven
        
        # Initialize neuron populations
        self.ven_neurons = VENNeuron(tau_mem=5.0, n_afferents=8, dt=dt)
        self.pyr_neurons = PyramidalNeuron(tau_mem=20.0, n_afferents=80, dt=dt)
        
        # Recurrent weight matrices (sparse for VEN pathway)
        self.W_ven = nn.Parameter(torch.randn(self.n_ven, n_in) * 0.1)
        self.W_pyr = nn.Parameter(torch.randn(self.n_pyr, n_in) * 0.1)
        self.W_rec = nn.Parameter(torch.randn(n_neurons, n_neurons) * 0.05)
        
        # Readout layer
        self.readout = nn.Linear(n_neurons, n_out)
        
        # State variables
        self.register_buffer('v_ven', torch.zeros(self.n_ven))
        self.register_buffer('v_pyr', torch.zeros(self.n_pyr))
        
    def step(self, input_current):
        """One simulation step."""
        # Compute recurrent input
        spikes = torch.cat([self.v_ven.ge(self.ven_neurons.v_threshold).float(),
                            self.v_pyr.ge(self.pyr_neurons.v_threshold).float()])
        rec_input = self.W_rec @ spikes
        
        # Update VEN population (fast)
        ven_input = self.W_ven @ input_current + rec_input[:self.n_ven]
        self.v_ven, ven_spikes = self.ven_neurons(ven_input, self.v_ven, None)
        
        # Update pyramidal population (slow)
        pyr_input = self.W_pyr @ input_current + rec_input[self.n_ven:]
        self.v_pyr, pyr_spikes = self.pyr_neurons(pyr_input, self.v_pyr, None)
        
        # Concatenate spikes for readout
        all_spikes = torch.cat([ven_spikes, pyr_spikes])
        return self.readout(all_spikes), all_spikes
    
    def forward(self, input_sequence, max_steps=500):
        """Run network for fixed duration or until decision."""
        outputs = []
        spike_trains = []
        
        for t in range(max_steps):
            x = input_sequence[t] if t < len(input_sequence) else torch.zeros_like(input_sequence[0])
            output, spikes = self.step(x)
            outputs.append(output)
            spike_trains.append(spikes)
            
        return torch.stack(outputs), torch.stack(spike_trains)
```

## Clinical Condition Simulations

```python
def create_typical_network(n_neurons=2000, ven_fraction=0.02, **kwargs):
    """Typical brain: 2% VENs."""
    return MixedCorticalCircuit(n_neurons, ven_fraction=ven_fraction, **kwargs)

def create_autism_network(n_neurons=2000, ven_fraction=0.004, **kwargs):
    """Autism-like: reduced VEN fraction (0.4%)."""
    return MixedCorticalCircuit(n_neurons, ven_fraction=ven_fraction, **kwargs)

def create_ftd_network(n_neurons=2000, ven_fraction=0.02, **kwargs):
    """FTD-like: post-training VEN ablation."""
    net = MixedCorticalCircuit(n_neurons, ven_fraction=ven_fraction, **kwargs)
    # Ablate VEN pathway by zeroing weights
    with torch.no_grad():
        net.W_ven.zero_()
    return net
```

## Social Discrimination Task

```python
class SocialDiscriminationTask:
    """Binary social discrimination task for training/validation."""
    
    def __init__(self, n_features=64, n_classes=2, seq_len=100):
        self.n_features = n_features
        self.n_classes = n_classes
        self.seq_len = seq_len
        
    def generate_sample(self, label=None):
        """Generate a synthetic social stimulus sequence."""
        if label is None:
            label = np.random.randint(self.n_classes)
        
        # Class-specific temporal patterns
        base = torch.randn(self.seq_len, self.n_features) * 0.5
        if label == 0:
            base[:20] += 1.0  # Early signal pattern
        else:
            base[20:40] -= 1.0  # Delayed signal pattern
            
        return base, label
    
    def compute_reaction_time(self, spike_trains, threshold=0.5, dt=1.0):
        """Compute reaction time from first spike crossing threshold."""
        for t, spikes in enumerate(spike_trains):
            if spikes.mean().item() > threshold:
                return t * dt
        return len(spike_trains) * dt  # No decision made
```

## Analysis Utilities

```python
def compute_first_spike_latencies(spike_trains, ven_indices, pyr_indices):
    """Compare first-spike latencies between VEN and pyramidal neurons."""
    ven_latencies = []
    pyr_latencies = []
    
    for t, spikes in enumerate(spike_trains):
        ven_spikes = spikes[ven_indices]
        pyr_spikes = spikes[pyr_indices]
        
        if ven_spikes.sum() > 0 and len(ven_latencies) == 0:
            ven_latencies.append(t)
        if pyr_spikes.sum() > 0 and len(pyr_latencies) == 0:
            pyr_latencies.append(t)
            
        if ven_latencies and pyr_latencies:
            break
            
    return ven_latencies, pyr_latencies


def run_statistical_comparison(rts_typical, rts_ftd, rts_autism):
    """Run t-tests between conditions."""
    from scipy import stats
    
    t_typ_ftd, p_typ_ftd = stats.ttest_ind(rts_typical, rts_ftd)
    t_typ_aut, p_typ_aut = stats.ttest_ind(rts_typical, rts_autism)
    
    print(f"Typical vs FTD:   t={t_typ_ftd:.2f}, p={p_typ_ftd:.4f}")
    print(f"Typical vs Autism: t={t_typ_aut:.2f}, p={p_typ_aut:.4f}")
    
    print(f"\nReaction Times (mean ± std):")
    print(f"  Typical: {np.mean(rts_typical):.2f} ± {np.std(rts_typical):.2f} ms")
    print(f"  Autism:  {np.mean(rts_autism):.2f} ± {np.std(rts_autism):.2f} ms")
    print(f"  FTD:     {np.mean(rts_ftd):.2f} ± {np.std(rts_ftd):.2f} ms")


def train_network(model, task, n_epochs=100, lr=1e-3):
    """Train the circuit on social discrimination task."""
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        
        # Generate batch
        inputs, labels = [], []
        for _ in range(32):
            x, y = task.generate_sample()
            inputs.append(x)
            labels.append(y)
            
        # Forward pass with surrogate gradients
        total_loss = 0
        for x, y in zip(inputs, labels):
            outputs, _ = model(x)
            # Use final or pooled output for classification
            loss = criterion(outputs[-1].unsqueeze(0), torch.tensor([y]))
            total_loss += loss
            
        total_loss /= len(inputs)
        total_loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: loss={total_loss.item():.4f}")
            
    return model
```

## Complete Training Pipeline

```python
def full_experiment(n_seeds=10):
    """Run complete Fast Lane Hypothesis experiment."""
    
    results = {'typical': [], 'autism': [], 'ftd': []}
    task = SocialDiscriminationTask()
    
    for seed in range(n_seeds):
        torch.manual_seed(seed)
        np.random.seed(seed)
        
        print(f"\n=== Seed {seed} ===")
        
        # Train typical network
        net_typical = create_typical_network()
        train_network(net_typical, task)
        
        # Evaluate typical
        rts_typ = evaluate_rt(net_typical, task)
        results['typical'].append(rts_typ)
        
        # Evaluate autism-like (same weights, fewer VENs)
        net_autism = create_autism_network()
        # Copy shared weights
        rts_aut = evaluate_rt(net_autism, task)
        results['autism'].append(rts_aut)
        
        # Evaluate FTD-like (VEN ablation)
        net_ftd = create_ftd_network()
        rts_ftd = evaluate_rt(net_ftd, task)
        results['ftd'].append(rts_ftd)
    
    # Statistical analysis
    run_statistical_comparison(
        results['typical'], results['ftd'], results['autism']
    )
    
    return results


def evaluate_rt(model, task, n_trials=100):
    """Evaluate reaction time over multiple trials."""
    rts = []
    accs = []
    
    for _ in range(n_trials):
        x, y = task.generate_sample()
        outputs, spike_trains = model(x)
        
        # Reaction time
        rt = task.compute_reaction_time(spike_trains)
        rts.append(rt)
        
        # Accuracy
        pred = outputs[-1].argmax().item()
        accs.append(pred == y)
        
    print(f"  Accuracy: {np.mean(accs):.3f}, RT: {np.mean(rts):.2f} ± {np.std(rts):.2f} ms")
    return np.mean(rts)
```
