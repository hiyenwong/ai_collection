---
name: spiking-computational-neuroscience-survey
version: v1.0.0
last_updated: 2026-04-19
description: Comprehensive survey of Spiking Neural Networks (SNNs) applied to computational neuroscience. Bridges the gap between artificial SNNs and biological neural computation, covering neuron models, learning rules, network architectures, and neuroscientific applications. Provides practical guide for using SNNs as computational models of brain function. Applicable to SNN neuroscience modeling, biologically plausible learning, neural simulation. Trigger: SNN computational neuroscience, biologically plausible networks, spiking neuron models neuroscience, neural simulation SNN, brain-inspired computation
---

# Spiking Neural Networks for Computational Neuroscience

## Description

A comprehensive survey of Spiking Neural Networks (SNNs) as tools for computational neuroscience. SNNs provide a bridge between artificial neural networks and biological neural systems, using discrete spikes (action potentials) as the fundamental unit of computation. This methodology covers neuron models, synaptic plasticity rules, network architectures, and practical applications to understanding brain function.

Based on: "Spiking Neural Networks for Computational Neuroscience" (arXiv:2511.24654, November 2025)

## Neuron Models Hierarchy

### From Simple to Complex

```python
# 1. Integrate-and-Fire (IF) - simplest
class IFNeuron:
    """Basic integrate-and-fire neuron."""
    def step(self, input_current):
        self.membrane += input_current
        if self.membrane >= self.threshold:
            self.membrane = 0
            return 1  # spike
        return 0

# 2. Leaky Integrate-and-Fire (LIF)
class LIFNeuron:
    """Leaky integrate-and-fire with membrane decay."""
    def step(self, input_current, dt=1.0):
        tau = 20.0  # membrane time constant
        self.membrane += dt/tau * (self.rest - self.membrane) + input_current
        if self.membrane >= self.threshold:
            self.membrane = self.reset
            return 1
        return 0

# 3. Adaptive Exponential (AdEx)
class AdExNeuron:
    """Adaptive exponential integrate-and-fire."""
    def step(self, input_current, dt=1.0):
        tau_m, tau_w = 20.0, 200.0
        a, b = 0.1, 0.5  # adaptation parameters
        
        # Membrane equation
        dv = (-(self.V - self.V_rest) + self.delta_T * torch.exp((self.V - self.V_T)/self.delta_T) + self.R*input_current - self.R*self.w) * dt/tau_m
        
        # Adaptation equation
        dw = (a * (self.V - self.V_rest) - self.w) * dt/tau_w
        
        self.V += dv
        self.w += dw
        
        if self.V >= self.threshold:
            self.V = self.V_reset
            self.w += b
            return 1
        return 0

# 4. Hodgkin-Huxley (HH) - most biologically realistic
class HHNeuron:
    """Full Hodgkin-Huxley model."""
    def step(self, input_current, dt=0.01):
        # Ion channel dynamics
        g_Na, g_K, g_L = 120.0, 36.0, 0.3
        E_Na, E_K, E_L = 50.0, -77.0, -54.4
        
        # Update gating variables
        self.m = self._update_m(self.V, self.m, dt)
        self.h = self._update_h(self.V, self.h, dt)
        self.n = self._update_n(self.V, self.n, dt)
        
        # Membrane potential
        I_Na = g_Na * self.m**3 * self.h * (self.V - E_Na)
        I_K = g_K * self.n**4 * (self.V - E_K)
        I_L = g_L * (self.V - E_L)
        
        self.V += dt * (input_current - I_Na - I_K - I_L) / self.C
        return 1 if self.V > 0 else 0
```

## Learning Rules for Biological Plausibility

### Spike-Timing-Dependent Plasticity (STDP)

```python
def stdp_update(pre_spike_times, post_spike_times, dt_max=50.0, A_plus=0.01, A_minus=0.012):
    """
    STDP weight update based on spike timing differences.
    
    Pre before post -> LTP (weight increase)
    Post before pre -> LTD (weight decrease)
    """
    dw = 0
    for t_pre in pre_spike_times:
        for t_post in post_spike_times:
            delta_t = t_post - t_pre
            if 0 < delta_t < dt_max:
                dw += A_plus * torch.exp(-delta_t / 20.0)
            elif -dt_max < delta_t < 0:
                dw -= A_minus * torch.exp(delta_t / 20.0)
    return dw
```

### Three-Factor Learning Rules

```python
def three_factor_learning(pre_spike, post_spike, neuromodulator, lr=0.01):
    """
    Three-factor learning: pre-spike * post-spike * neuromodulator.
    
    Captures dopamine-modulated plasticity for reinforcement learning.
    """
    eligibility_trace = pre_spike * post_spike
    dw = lr * neuromodulator * eligibility_trace
    return dw
```

## Network Architectures for Neuroscience

### Balanced Excitation-Inhibition

```python
class BalancedEINetwork:
    """
    Network with balanced excitation and inhibition.
    Exhibits irregular, asynchronous activity similar to cortex.
    """
    def __init__(self, n_excitatory, n_inhibitory):
        self.n_e = n_excitatory
        self.n_i = n_inhibitory
        
        # Sparse random connectivity
        self.W_ee = self._sparse_connect(n_excitatory, n_excitatory, p=0.1, J=0.1)
        self.W_ei = self._sparse_connect(n_excitatory, n_inhibitory, p=0.1, J=-0.4)
        self.W_ie = self._sparse_connect(n_inhibitory, n_excitatory, p=0.1, J=0.1)
        self.W_ii = self._sparse_connect(n_inhibitory, n_inhibitory, p=0.1, J=-0.2)
    
    def run(self, external_input, duration=1000):
        """Simulate network dynamics."""
        spike_train = []
        for t in range(duration):
            # Compute input to each population
            I_e = self.W_ee @ spikes_e + self.W_ei @ spikes_i + external_input
            I_i = self.W_ie @ spikes_e + self.W_ii @ spikes_i
            
            # Update neurons
            spikes_e = self.exc_neurons.step(I_e)
            spikes_i = self.inh_neurons.step(I_i)
            spike_train.append((spikes_e, spikes_i))
        
        return spike_train
```

## Applications in Computational Neuroscience

1. **Sensory processing models**: V1 orientation selectivity, auditory processing
2. **Motor control**: Cerebellar learning, basal ganglia function
3. **Memory and learning**: Hippocampal place cells, working memory
4. **Decision making**: Drift-diffusion models with spiking neurons
5. **Disease modeling**: Parkinson's tremor, epilepsy, schizophrenia
