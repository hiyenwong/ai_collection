---
name: clockless-neuromorphic-chip
description: "Scalable neuromorphic computing from autonomous spiking dynamics in clockless (asynchronous) reconfigurable FPGA chips. Boolean spiking neurons with configurable E/I weights, spike-encoded data pipeline, and competitive audio classification at significantly lower power."
---

# Clockless Neuromorphic Chip

## Description

Scalable neuromorphic architecture based on autonomous time-continuous evolution of clockless (asynchronous) digital circuits. Implements networks of interacting Boolean spiking neurons with configurable excitatory/inhibitory synaptic weights on commercial FPGAs. Complete spike-encoded data processing pipeline for ML tasks with significantly lower power than traditional digital implementations.

Based on: "Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip" (arXiv: 2605.16114) by Oliveira Gomes & Rontani, May 2026.

## Activation Keywords

- clockless neuromorphic
- asynchronous spiking chip
- autonomous spiking dynamics
- FPGA neuromorphic
- Boolean spiking neurons
- spike-encoded pipeline
- 时钟less神经形态
- 异步脉冲芯片
- 无时钟神经形态计算
- neuromorphic FPGA audio

## Core Architecture

### Boolean Spiking Neurons

The system uses Boolean neurons where spiking dynamics emerge from autonomous time-continuous evolution of asynchronous digital circuits:

```python
class BooleanSpikingNeuron:
    """Boolean spiking neuron with configurable E/I weights."""
    
    def __init__(self, neuron_id, threshold=1):
        self.neuron_id = neuron_id
        self.threshold = threshold
        self.membrane = 0  # Boolean state
        self.spike_history = []
        
    def update(self, inputs, weights):
        """Asynchronous update: excitatory (+1) and inhibitory (-1) inputs."""
        # Sum weighted inputs
        excitation = sum(w for inp, w in zip(inputs, weights) if inp and w > 0)
        inhibition = sum(abs(w) for inp, w in zip(inputs, weights) if inp and w < 0)
        
        # Boolean threshold dynamics
        net_input = excitation - inhibition
        if net_input >= self.threshold:
            self.membrane = 1
            self.spike_history.append(1)
            return True  # Spike fired
        else:
            self.membrane = 0
            self.spike_history.append(0)
            return False
```

### Key Design Principles

1. **Clockless (Asynchronous)**: No global clock — neurons evolve autonomously based on local state changes
2. **Boolean Dynamics**: Spiking emerges from discrete Boolean logic, not analog membrane equations
3. **Configurable E/I Weights**: Each synapse can be excitatory or inhibitory
4. **Spike-Encoded I/O**: Complete pipeline handles spike-encoded input data and produces spike-encoded output

## Implementation Patterns

### Pattern 1: FPGA Neuromorphic Network

```python
class NeuromorphicNetwork:
    """Network of Boolean spiking neurons on FPGA."""
    
    def __init__(self, n_neurons, connectivity_matrix):
        self.neurons = [BooleanSpikingNeuron(i) for i in range(n_neurons)]
        self.weights = connectivity_matrix  # Configurable E/I weights
        self.time_step = 0
        
    def propagate(self, input_spikes):
        """Asynchronous propagation of spike activity."""
        spiked = []
        for i, neuron in enumerate(self.neurons):
            inputs = input_spikes if i in self.input_layer else [n.membrane for n in self._get_presynaptic(i)]
            weights = self.weights[i]
            if neuron.update(inputs, weights):
                spiked.append(i)
        self.time_step += 1
        return spiked
```

### Pattern 2: Spike-Encoded Audio Processing Pipeline

```python
class SpikeAudioEncoder:
    """Convert audio to spike-encoded representation."""
    
    def __init__(self, n_channels, threshold=0.5):
        self.n_channels = n_channels
        self.threshold = threshold
        
    def encode(self, audio_signal):
        """Convert audio frames to spike trains."""
        # Frame the audio signal
        frames = self.frame_audio(audio_signal)
        spike_trains = []
        for frame in frames:
            # Each frequency band becomes a spike channel
            spikes = [1 if amplitude > self.threshold else 0 
                     for amplitude in frame]
            spike_trains.append(spikes)
        return spike_trains
```

## Key Findings

| Metric | Result |
|--------|--------|
| **Audio Classification** | Competitive performance on spike-encoded audio tasks |
| **Power Consumption** | Significantly lower than traditional digital implementations |
| **Processing Speed** | High-speed processing via autonomous evolution |
| **Scalability** | Commercial FPGA implementation, inherently scalable |

## Transfer to Traditional ML

The paper demonstrates that neuromorphic modules (ns_TIN, superficial_TIN) can be transferred to ResNet18:
- **ns_TIN module**: Improves budget-reduced performance preservation
- **superficial_TIN module**: Improves Gaussian noise robustness

## Pitfalls

1. **Clockless ≠ Slow**: Asynchronous circuits can be faster than clocked ones because they don't wait for clock edges
2. **Boolean ≠ Simple**: Boolean spiking neurons can exhibit rich dynamics through network-level interactions
3. **E/I Balance is Critical**: Proper balance of excitatory and inhibitory weights is essential for stable dynamics
4. **FPGA vs ASIC**: While demonstrated on FPGA, true power advantages are realized on custom neuromorphic ASICs

## Applications

- Low-power edge AI inference
- Real-time audio/signal processing
- Neuromorphic sensor data processing
- Energy-constrained autonomous systems
- Spike-based machine learning on FPGA

## Related Skills

- `neuromorphic-continual-nuclear-ics` - Neuromorphic continual learning
- `snn-learning-survey` - SNN learning rules
- `edgespike-edge-iot-snn` - SNN for edge IoT sensing

## Resources

- Paper: https://arxiv.org/abs/2605.16114
- Key: Autonomous time-continuous Boolean spiking dynamics on FPGA
