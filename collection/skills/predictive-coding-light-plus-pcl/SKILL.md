---
name: predictive-coding-light-plus-pcl
description: "Predictive Coding Light+ (PCL+) methodology for unsupervised sequence learning in spiking neural networks using STDP and heterogeneous synaptic delays. Combines energy-efficient predictive coding with working memory via delayed recurrent excitation. ArXiv 2605.12732."
tags: [snn, predictive-coding, stdp, synaptic-delays, sequence-learning, working-memory, event-camera]
arxiv_id: "2605.12732"
date: "2026-05-12"
---

# Predictive Coding Light+ (PCL+) Methodology

## Paper Reference

**Title:** Predictive Coding Light+: learning to predict visual sequences with spike timing-dependent plasticity and synaptic delays  
**Authors:** Antony W. N'dri, Thomas Barbier, Céline Teulière, Jochen Triesch  
**arXiv:** 2605.12732 (May 12, 2026)  
**Categories:** q-bio.NC  
**Affiliations:** Université Clermont Auvergne, Orange Labs, Frankfurt Institute for Advanced Studies, Goethe University Frankfurt

## Abstract Summary

PCL+ is a spiking neural network architecture for unsupervised sequence processing that learns recurrent excitatory connections with delays to enable short-term retention of information. It reproduces classic findings on sequence learning in visual cortex and learns to "fill in" missing input in a challenging gesture recognition task. Combines energy-efficient predictive coding with working memory without spending extra spikes.

## Core Architecture

### PCL+ Network Components

The PCL+ network extends the original PCL (Predictive Coding Light) model with **delayed recurrent excitation**:

```
┌─────────────────────────────────────────────────────────┐
│                    PCL+ Architecture                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Complex Cells (Layer 2)                                 │
│  ┌──────────────┐                                        │
│  │  Top-down    │                                        │
│  │  Inhibition ─┼──────► Simple Cells                    │
│  │  + Delayed   │         (Layer 1)                     │
│  │  Excitation ─┤                                        │
│  └──────────────┘                                        │
│       ▲                                                  │
│       │ Feedforward                                      │
│       │ Excitation                                       │
│       │                                                  │
│  ┌────┴─────────────────────────────────┐                │
│  │    Simple Cells                      │                │
│  │    ┌───────────────────────────┐     │                │
│  │    │  Local Lateral Inhibition │     │                │
│  │    │  Distant Lateral Inhib.   │     │                │
│  │    │  Distant Lateral EXCITATION│    │  ◄── NEW IN PCL+│
│  │    │  (with delays Δt)         │     │                │
│  │    └───────────────────────────┘     │                │
│  └──────────────────────────────────────┘                │
│       ▲                                                  │
│       │ Event Camera Input (ON/OFF events)              │
└─────────────────────────────────────────────────────────┘
```

### Synaptic Connection Types

| Type | Direction | Plasticity | Delay | Purpose |
|------|-----------|------------|-------|---------|
| Feedforward excitation | Input→Simple | STDP | None | Sensory drive |
| Local lateral inhibition | Simple↔Simple (nearby) | STDP | None | WTA competition |
| Distant lateral inhibition | Simple→Simple (far) | STDP | None | Suppress predictable |
| Top-down inhibition | Complex→Simple | STDP | None | Suppress predictable |
| **Distant lateral excitation** | Simple→Simple (far) | STDP | **Heterogeneous (100-500ms)** | **Working memory (NEW)** |
| **Top-down excitation** | Complex→Simple | STDP | **Heterogeneous (100-500ms)** | **Working memory (NEW)** |

### Key Innovation: Delayed Recurrent Excitation

PCL+ introduces **two new connection types** with heterogeneous synaptic delays:

1. **Delayed distant lateral excitation** between simple cells
2. **Delayed top-down excitation** from complex cells to simple cells

These connections:
- Learn via standard STDP rules
- Use heterogeneous delays drawn from uniform distribution [100ms, 500ms]
- Maintain a record of the recent past through delayed spike propagation
- Decay over time due to recurrent inhibition (fading memory)

## Neuron Model

### Leaky Integrate-and-Fire (LIF)

```python
def update_membrane_potential(V, dt, tau_m, V_reset, V_thresh, 
                               V_min, eta_RP, tau_RP, t_since_spike,
                               synaptic_inputs):
    """Event-based LIF update."""
    V_tilde = max(V_min, V * exp(-dt / tau_m) + 
                  sum(synaptic_inputs) - 
                  eta_RP * exp(-(t_since_spike) / tau_RP))
    
    if V_tilde >= V_thresh:
        return V_reset, True  # Spike!
    return V_tilde, False
```

### Key Parameters

| Parameter | Simple Cells | Complex Cells |
|-----------|-------------|---------------|
| V_reset | -10 mV | -10 mV |
| V_thresh | 30 mV | 3 mV |
| τ_m | 18 ms | 50 ms |
| τ_RP | 5 ms | 5 ms |
| V_min | -20 mV | -20 mV |

## STDP Learning Rules

### Causal STDP

PCL+ uses causal spike timing-dependent plasticity:

```python
def causal_stdp(pre_spike_time, post_spike_time, 
                tau_LTP, tau_LTD, eta_plus, eta_minus,
                w_current, w_min, w_max):
    dt = post_spike_time - pre_spike_time
    
    if dt > 0:  # Pre before post → LTP
        delta_w = eta_plus * exp(-dt / tau_LTP)
        w_new = min(w_max, w_current + delta_w)
    elif dt < 0:  # Post before pre → LTD
        delta_w = eta_minus * exp(dt / tau_LTD)
        w_new = max(w_min, w_current + delta_w)
    else:
        w_new = w_current
    
    return w_new
```

### Weight-Dependent STDP

For stability, PCL+ uses weight-dependent scaling:

```python
def weight_dependent_stdp(delta_w, w_current, w_max, w_min, lambda_param):
    # Soft bound: scaling depends on distance from bounds
    if delta_w > 0:  # Potentiation
        scale = ((w_max - w_current) / (w_max - w_min)) ** lambda_param
    else:  # Depression
        scale = ((w_current - w_min) / (w_max - w_min)) ** lambda_param
    return delta_w * scale
```

## Network Training Workflow

### Step 1: Event Camera Preprocessing

```python
def event_camera_to_spikes(events, simple_cell_receptive_fields):
    """Convert event camera ON/OFF events to simple cell input spikes."""
    # Events: (x, y, polarity, timestamp)
    # Polarity: +1 (ON/brightness increase), -1 (OFF/brightness decrease)
    spikes = []
    for event in events:
        x, y, polarity, t = event
        # Map to simple cell receptive fields
        for rc in simple_cell_receptive_fields:
            if rc.covers(x, y, polarity):
                spikes.append((rc.neuron_id, t))
    return spikes
```

### Step 2: Feedforward Excitatory Learning

Simple cells learn receptive fields from event camera input via STDP:

```python
def learn_feedforward_weights(input_spikes, simple_cell_spikes,
                               w_feedforward, tau_LTP, tau_LTD):
    for inp_time in input_spikes:
        for sc_time in simple_cell_spikes:
            dt = sc_time - inp_time
            w_feedforward = causal_stdp(inp_time, sc_time, 
                                         tau_LTP, tau_LTD, 
                                         w_feedforward)
    return w_feedforward
```

### Step 3: Lateral Connection Learning

Both inhibitory and excitatory lateral connections learn via STDP:

```python
def learn_lateral_connections(simple_cell_spikes, 
                               w_lateral_inhib, w_lateral_excit,
                               delays_uniform=(100, 500)):
    """Learn lateral connections with heterogeneous delays."""
    for i, spikes_i in enumerate(simple_cell_spikes):
        for j, spikes_j in enumerate(simple_cell_spikes):
            if i == j:
                continue
            # Inhibition: instantaneous
            w_lateral_inhib[i, j] = learn_from_pairs(spikes_i, spikes_j)
            # Excitation: with delay (NEW in PCL+)
            delay = random.uniform(*delays_uniform)
            w_lateral_excit[i, j] = learn_from_pairs_with_delay(
                spikes_i, spikes_j, delay)
    return w_lateral_inhib, w_lateral_excit
```

### Step 4: Complex Cell Learning

Complex cells learn to pool over simple cells and provide top-down feedback:

```python
def learn_topdown_connections(simple_spikes, complex_spikes,
                               w_topdown_inhib, w_topdown_excit):
    """Learn top-down inhibitory and excitatory connections."""
    # Inhibition: suppress predictable simple cell spikes
    w_topdown_inhib = learn_from_pairs(complex_spikes, simple_spikes)
    # Excitation with delay: maintain memory (NEW in PCL+)
    delay = random.uniform(100, 500)
    w_topdown_excit = learn_from_pairs_with_delay(
        complex_spikes, simple_spikes, delay)
    return w_topdown_inhib, w_topdown_excit
```

## Sequence Learning Mechanism

### Temporal Association via Delayed Excitation

```
Time:     t₁        t₂        t₃        t₄        t₅
          │         │         │         │         │
Input:    [Stim A]  [Stim B]  [Stim C]  [—]       [—]
          │         │         │
Simple:   [spike]──►[spike]──►[spike]
           │  │       │  │       │
Delayed   └──┼───────┼──┼───────┘  (recurrent excitation)
Excitation  └────────┼───────────►  activates at t₃
                     └───────────►  activates at t₄
                                    
Memory:   [Stim A]  [A+B]     [A+B+C]   [A+B+C]   [fading...]
```

The delayed excitatory connections create **temporal associations**:
- A spike at t₁ arrives at target cell at t₁ + delay
- Multiple connections with different delays create a distributed memory trace
- Recurrent inhibition ensures the memory fades over time

### "Filling In" Missing Input

When trained on sequences, PCL+ can predict and fill in missing sensory input:

```
Test:     [Stim A]  [Stim B]  [—]       [—]       [—]
                   │         │
Memory via ────────┼─────────┘
Delayed Excit.     │         
                   └────────► Predicts Stim C pattern
                            (without actual input)
```

## Implementation Considerations

### Event-Based Simulation

PCL+ uses event-based simulation (no fixed time steps):

```python
class EventBasedSNN:
    def __init__(self, neurons, connections):
        self.event_queue = PriorityQueue()  # Sorted by time
    
    def step(self):
        """Process next event in queue."""
        event = self.event_queue.pop()
        self.process_event(event)
    
    def process_event(self, event):
        if event.type == "SPIKE":
            self.propagate_spike(event.neuron, event.time)
        elif event.type == "INPUT":
            self.process_input(event)
```

### Energy Efficiency

PCL+ achieves energy efficiency through:

1. **Event-based processing**: Only compute when spikes arrive
2. **Predictive spike suppression**: Redundant spikes are removed by inhibition
3. **Delayed excitation for memory**: No persistent activity needed
4. **Sparse coding**: Only unpredictable events generate spikes

### Working Memory Trade-off

| Memory Mechanism | Energy Cost | Capacity | Decay |
|-----------------|-------------|----------|-------|
| Persistent activity (traditional SNN) | High (continuous spiking) | Limited by runaway excitation | N/A |
| PCL+ delayed excitation | Low (propagating spikes only) | Set by delay distribution | Natural decay via inhibition |

## Experimental Results Summary

1. **Grating sequences**: PCL+ reproduces visual sequence learning findings in mouse V1
2. **Gesture recognition**: Successfully fills in missing input in event-camera gesture videos
3. **Control experiments**: Shuffled connections and random connectivity fail to fill in, confirming learned structure is necessary

## When to Use PCL+

- **Unsupervised sequence learning**: Learning temporal patterns from event-based data
- **Working memory in SNNs**: Short-term retention without persistent activity
- **Energy-efficient temporal processing**: Neuromorphic hardware deployment
- **Predictive sensory processing**: Systems that need to predict future inputs
- **Event camera applications**: Processing asynchronous event-based vision data

## Activation Keywords

predictive coding light plus, PCL+, STDP sequence learning, synaptic delay memory, event camera SNN, working memory spiking network, unsupervised visual sequence, energy-efficient temporal processing

## Related Skills

- predictive-coding-light: Original PCL methodology
- spiking-neural-network-analysis: General SNN paper analysis
- spikingjelly-framework: SNN implementation framework
- snn-learning-survey: Comprehensive SNN learning rules
