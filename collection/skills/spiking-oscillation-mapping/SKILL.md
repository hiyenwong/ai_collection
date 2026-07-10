---
name: spiking-oscillation-mapping
description: "Analyze and map oscillatory states in balanced spiking neural networks (SNN). Identify regime transitions (silent, asynchronous-irregular, oscillatory) based on synaptic and temporal time scales. Activation: spiking oscillation, SNN regime mapping, balanced network dynamics, oscillatory state analysis."
---

# Spiking Oscillation Mapping

Map oscillatory regimes in balanced spiking neural networks based on time scale interactions.

## Background

Balanced spiking networks exhibit three regimes:
1. **Silent** - No sustained activity
2. **Asynchronous-Irregular (AI)** - Poisson-like spiking
3. **Oscillatory** - Periodic population activity

Regime depends on **interacting time scales**:
- Postsynaptic decay (τ_s)
- Membrane potential decay (τ_m)
- Refractory period (τ_ref)

## Core Concepts

### 1. Time Scale Interactions

Network dynamics governed by relative time scales:

```python
# Time scale ratios determine regime
alpha = tau_s / tau_m      # Synaptic vs membrane
beta = tau_ref / tau_m     # Refractory vs membrane
gamma = tau_s / tau_ref    # Synaptic vs refractory

# Regime boundaries
def get_regime(alpha, beta, gamma):
    if gamma > threshold_high:
        return "oscillatory"
    elif gamma < threshold_low and alpha < threshold:
        return "silent"
    else:
        return "asynchronous_irregular"
```

### 2. Oscillatory State Detection

Detect oscillation from spike train statistics:

```python
def detect_oscillation(spike_counts, time_window):
    # Compute population rate
    rate = spike_counts / time_window
    
    # Autocorrelation reveals oscillation
    autocorr = compute_autocorrelation(rate)
    
    # Peaks in autocorr indicate periodicity
    peaks = find_peaks(autocorr)
    
    if len(peaks) > 1:
        oscillation_freq = extract_frequency(autocorr, peaks)
        return "oscillatory", oscillation_freq
    else:
        return "asynchronous_irregular", None
```

### 3. Regime Mapping

Systematically explore parameter space:

```python
def map_regime_space(tau_s_range, tau_m_range, tau_ref_range):
    regimes = {}
    
    for tau_s in tau_s_range:
        for tau_m in tau_m_range:
            for tau_ref in tau_ref_range:
                # Run simulation
                spikes = run_simulation(tau_s, tau_m, tau_ref)
                
                # Classify regime
                regime, freq = detect_oscillation(spikes)
                
                # Store result
                key = (tau_s, tau_m, tau_ref)
                regimes[key] = {"regime": regime, "freq": freq}
    
    return regimes
```

### 4. Balanced Network Model

Base network structure:

```python
class BalancedSpikingNetwork:
    def __init__(self, N_exc, N_inh, tau_s, tau_m, tau_ref):
        self.exc_neurons = ExcitatoryPopulation(N_exc, tau_m, tau_ref)
        self.inh_neurons = InhibitoryPopulation(N_inh, tau_m, tau_ref)
        self.synapses = Synapses(tau_s)
        
        # Balance: EI ratio ~4:1 for stability
        self.EI_ratio = 4
    
    def simulate(self, duration, input_rate):
        # External drive
        exc_input = PoissonInput(input_rate)
        
        # Recurrent dynamics
        for t in range(duration):
            exc_spikes = self.exc_neurons.update(exc_input, self.inh_neurons)
            inh_spikes = self.inh_neurons.update(exc_spikes)
            
            # Balanced inhibition prevents runaway excitation
            self.synapses.update(exc_spikes, inh_spikes)
```

## Implementation Guidelines

### When to Use

1. **SNN stability analysis** - Understanding network dynamics
2. **Parameter tuning** - Finding optimal time scales for target regime
3. **Oscillation control** - Designing networks for rhythmic computation
4. **Regime transitions** - Studying state switching

### Key Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| τ_s | 5-100 ms | Synaptic integration window |
| τ_m | 10-50 ms | Membrane leakage |
| τ_ref | 2-10 ms | Spike refractory period |
| EI_ratio | 3-5 | Excitatory/inhibitory balance |

### Regime Characteristics

| Regime | Rate | Autocorrelation | Spike Pattern |
|--------|------|-----------------|---------------|
| Silent | ~0 | Flat | No sustained activity |
| AI | Irregular | Exponential decay | Poisson-like |
| Oscillatory | Periodic | Periodic peaks | Synchronized bursts |

## Analysis Tools

### Visualization

```python
# Plot regime map
def plot_regime_map(regimes):
    import matplotlib.pyplot as plt
    
    # Create 2D slice of parameter space
    tau_s_vals = sorted(set(k[0] for k in regimes.keys()))
    tau_ref_vals = sorted(set(k[2] for k in regimes.keys()))
    
    # Color-coded regime plot
    colors = {"oscillatory": "red", "AI": "green", "silent": "blue"}
    
    for key, data in regimes.items():
        color = colors[data["regime"]]
        plt.scatter(key[0], key[2], c=color)
    
    plt.xlabel("τ_s (ms)")
    plt.ylabel("τ_ref (ms)")
    plt.title("Regime Map")
```

### Transition Detection

```python
# Find regime boundaries
def find_transitions(regimes):
    transitions = []
    
    # Scan parameter space
    for param1 in regimes:
        for param2 in get_neighbors(param1):
            if regimes[param1]["regime"] != regimes[param2]["regime"]:
                # Boundary between regimes
                transition_point = (param1, param2)
                transitions.append(transition_point)
    
    return transitions
```

## Related Concepts

- **Balanced Networks**: Excitatory-inhibitory equilibrium
- **Asynchronous Irregular State**: Poisson-like spiking regime
- **Neural Oscillations**: Population-level rhythmic activity
- **Time Scale Separation**: Multiple temporal dynamics

## Resources

- Paper: "Regime Mapping of Oscillatory States in Balanced Spiking Networks" (2604.04770v1)
- SNN simulation frameworks: Brian2, NEST, BindsNET

## Usage Examples

### Example: Parameter Optimization

```python
# Find parameters for desired regime
def optimize_for_regime(target_regime="oscillatory", target_freq=40):
    best_params = None
    
    for tau_s in range(10, 100, 5):
        for tau_ref in range(2, 10):
            regime, freq = simulate_and_classify(tau_s, tau_ref)
            
            if regime == target_regime and abs(freq - target_freq) < 5:
                best_params = (tau_s, tau_ref)
                break
    
    return best_params
```

### Example: Regime Analysis

```python
# Analyze network dynamics
def analyze_snn_dynamics(network):
    spikes = network.simulate(duration=5000)
    
    regime, freq = detect_oscillation(spikes)
    
    report = {
        "regime": regime,
        "frequency": freq,
        "mean_rate": compute_mean_rate(spikes),
        "fano_factor": compute_fano(spikes),
        "cv ISI": compute_cv(spikes)
    }
    
    return report
```

---

**Source**: arxiv paper 2604.04770v1 - "Regime Mapping of Oscillatory States in Balanced Spiking Networks"
**Created**: 2026-04-07 by research-skill-creation-hourly cron job