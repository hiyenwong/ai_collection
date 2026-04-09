# SKILL.md - Spiking Generative Networks with Short-Term Plasticity

## Activation Keywords

- spiking generative networks, short-term plasticity, STP
- spike-based inference, probabilistic spiking networks
- energy-based models, spiking Boltzmann machines
- synaptic depression, facilitation, generative SNN

## What It Does

Demonstrates that spiking neural networks with short-term synaptic plasticity (STP) can outperform classical neural networks in generative tasks. Shows how local, spike-triggered synaptic dynamics achieve diverse energy landscapes without tempering.

## When To Use

**Use this skill when:**
- Building spiking generative models
- Implementing spike-based probabilistic inference
- Designing energy-based spiking networks
- Need computational advantages over classical networks
- Training on imbalanced datasets

**Do NOT use for:**
- Rate-based generative models (no spikes)
- Static synaptic weights (no plasticity)
- Simple classification tasks (no generative requirement)

## How To Use

### Step-by-Step Workflow

1. **Define Spiking Network with STP**
   - Use LIF or similar spiking neuron model
   - Add short-term plasticity (Tsodyks-Markram model)
   - Depression: U, facilitation: F parameters

2. **Configure STP Dynamics**
   - Synaptic efficacy: E(t) = E₀ · R(t) · u(t)
   - Recovery: dR/dt = (1-R)/τᵣ - u·R·δ(t-spike)
   - Facilitation: du/dt = (U-u)/ᵤ + U(1-u)·δ(t-spike)

3. **Energy-Based Learning**
   - Define energy function: E(v) = -½ v^T W v
   - STP creates dynamic energy landscape
   - Spike-triggered plasticity modifies landscape locally

4. **Training Procedure**
   - Present training samples
   - Run network dynamics to equilibrium
   - Update weights via contrastive learning
   - STP dynamics run continuously

5. **Sampling/Generation**
   - Initialize with random state or partial pattern
   - Let network settle with STP dynamics
   - Sample from equilibrium distribution

### Key Parameters

| Parameter | Role | Typical Value |
|-----------|------|---------------|
| U (depression) | Resource consumption | 0.2-0.5 |
| F (facilitation) | Utilization increase | 0.1-0.3 |
| τᵣ (recovery) | Depression timescale | 100-500 ms |
| ᵤ (facilitation) | Facilitation timescale | 50-200 ms |

### STP-Enhanced Generative Advantage

**Without STP:**
- Single fixed energy landscape
- Requires tempering for diverse modes
- Computationally expensive

**With STP:**
- Dynamic, time-varying energy landscape
- Automatic mode exploration
- Efficient sampling

## Example Usage

### Spiking Generative Network with STP

**Problem:** Build generative model for imbalanced data

**Implementation:**
```python
import numpy as np

class SpikingGenerativeNetwork:
    def __init__(self, N, U=0.3, F=0.2, tau_r=200, tau_f=100):
        self.N = N
        self.weights = np.random.randn(N, N) * 0.1
        
        # Short-term plasticity parameters
        self.U = U  # Depression
        self.F = F  # Facilitation
        self.tau_r = tau_r
        self.tau_f = tau_f
        
        # STP state
        self.R = np.ones((N, N))  # Resource availability
        self.u = np.full((N, N), U)  # Utilization
    
    def stp_update(self, pre_spike, post_spike, dt):
        """
        Update STP state based on spikes
        Tsodyks-Markram model
        """
        # Recovery (no spike)
        dR = (1 - self.R) / self.tau_r * dt
        du = (self.U - self.u) / self.tau_f * dt
        
        # Spike-triggered updates
        if pre_spike is not None:
            for j in np.where(pre_spike)[0]:
                dR[:, j] -= self.u[:, j] * self.R[:, j]
                du[:, j] += self.F * (1 - self.u[:, j])
        
        self.R += dR
        self.u += du
        
        # Effective synaptic weight
        W_eff = self.weights * self.R * self.u
        return W_eff
    
    def generate(self, steps=1000, dt=1.0):
        """
        Generate samples from network equilibrium
        """
        spikes = np.zeros(self.N)
        membrane = np.random.randn(self.N)
        
        samples = []
        for t in range(steps):
            # Update STP
            W_eff = self.stp_update(spikes, None, dt)
            
            # Membrane dynamics
            input_current = W_eff @ spikes
            membrane += dt * (-membrane + input_current)
            
            # Spike generation
            spikes = (membrane > 1.0).astype(float)
            membrane[spikes > 0] = 0  # Reset
            
            # Sample
            samples.append(spikes.copy())
        
        return np.array(samples)
```

### Training on Imbalanced Data

**Analysis:**
```python
def train_on_imbalanced_data(network, data, labels, epochs=100):
    """
    Train generative model on imbalanced dataset
    STP helps explore rare modes
    """
    for epoch in range(epochs):
        for sample in data:
            # Clamp to data
            initial_spikes = sample
            
            # Run dynamics with STP
            generated = network.generate(steps=100)
            
            # Contrastive update
            # Positive phase: data
            # Negative phase: generated
            
            # Weight update (simplified)
            network.weights += 0.01 * (
                np.outer(sample, sample) - 
                np.mean([np.outer(g, g) for g in generated[-10:]], axis=0)
            )
    
    return network
```

**Result:** STP enables better coverage of rare modes in imbalanced data

## Key Advantages

| Advantage | Mechanism |
|-----------|-----------|
| Diverse energy landscape | Dynamic STP modification |
| No tempering needed | Automatic mode exploration |
| Imbalanced data handling | Better rare mode coverage |
| Biological plausibility | Spike-triggered local updates |

## Related Skills

- **tsodyks-markram-chaotic-dynamics** - STP and chaos
- **spiking-mode-neural-networks** - Spiking network architectures
- **noisy-snn-learning** - Learning in noisy SNNs

## Source

- arXiv:1709.08166v3
- Title: Spiking neurons with short-term synaptic plasticity form superior generative networks
- Utility: 0.87
- Authors: (from arxiv)

## Notes

- Key insight: STP provides computational advantage for generative tasks
- Outperforms classical networks on imbalanced data
- No need for tempering techniques
- Local, spike-triggered dynamics
- Applications: generative modeling, probabilistic inference, SNNs
- Evidence for spike-based computation superiority

---

_Created: 2026-04-01_