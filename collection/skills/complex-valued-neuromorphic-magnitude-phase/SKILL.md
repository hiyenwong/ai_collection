---
id: complex-valued-neuromorphic-magnitude-phase
name: complex-valued-neuromorphic-magnitude-phase
description: Complex-valued neural network with magnitude-phase decomposition for event-driven neuromorphic learning, enabling efficient spiking computation with rich representational capacity
tags: [neuromorphic-computing, complex-valued-networks, spiking-neural-networks, event-driven-learning, magnitude-phase]
created: 2026-07-01
source: arxiv:2606.29099
authors: ["Reza Ahmadvand", "Sarah Safura Sharif", "Yaser Mike Banad"]
---

# Complex-Valued Neuromorphic Learning via Magnitude-Phase Decomposition

## Core Framework

### Problem Setting
Design efficient event-driven neural networks for neuromorphic hardware using:
- **Complex-valued neurons**: Encode information in both magnitude and phase
- **Magnitude-phase decomposition**: Separate amplitude and timing information
- **Event-driven processing**: Spike-based computation for energy efficiency

### Mathematical Formulation

#### Complex Neuron Model
Each neuron state z ∈ ℂ is represented as:
```
z = r · exp(iφ)
```
Where:
- r: magnitude (firing rate / amplitude)
- φ: phase (timing information)
- i: imaginary unit

#### Network Dynamics
```
dz_j/dt = -z_j + Σ_k W_jk · σ(z_k) + I_j
```
Where W ∈ ℂ^{N×N} are complex synaptic weights.

#### Magnitude-Phase Split
Decouple dynamics into two real equations:
```
dr/dt = -r + |Σ W·σ(z)| · cos(θ) + Re(I)
dφ/dt = arg(Σ W·σ(z)) + Im(I)
```
Where θ is the phase difference between pre and post synaptic terms.

## Key Insights

### 1. Dual Information Channels
- **Magnitude channel**: Encodes rate-based information (traditional)
- **Phase channel**: Encodes temporal/relative timing information
- **Multiplexing**: Both channels operate simultaneously on same hardware

### 2. Event-Driven Efficiency
- **Sparse updates**: Phase changes trigger selective updates
- **Phase-only spikes**: Some events carry only phase information
- **Energy reduction**: Magnitude updates are more expensive → reduce frequency

### 3. Representational Advantages
- **Rotation invariance**: Phase naturally encodes rotation/translation
- **Interference patterns**: Complex multiplication enables binding operations
- **Frequency multiplexing**: Different oscillation frequencies for different features

## Learning Rules

### Complex Hebbian Learning
```
ΔW_jk = η · (z_j · z_k* - λW_jk)
```
Where z_k* is complex conjugate, λ is weight decay.

### Phase-Gradient Learning
```
∂L/∂φ_j = ∂L/∂r_j · ∂r_j/∂φ_j + ∂L/∂φ_j|direct
```
Separate gradients for magnitude and phase enable independent optimization.

## Implementation

### Neuromorphic Mapping
```python
class ComplexSpikingNeuron:
    def __init__(self, N, tau=20.0):
        self.r = np.zeros(N)      # magnitude (membrane potential)
        self.phi = np.zeros(N)    # phase (oscillator phase)
        self.W_re = np.random.randn(N, N) / np.sqrt(N)
        self.W_im = np.random.randn(N, N) / np.sqrt(N)
    
    def forward(self, spikes_re, spikes_im):
        # Complex multiplication via real arithmetic
        h_re = self.W_re @ spikes_re - self.W_im @ spikes_im
        h_im = self.W_re @ spikes_im + self.W_im @ spikes_re
        
        # Magnitude-phase update
        self.r = 0.95 * self.r + np.sqrt(h_re**2 + h_im**2)
        self.phi = np.angle(h_re + 1j * h_im)
        
        # Spike generation (event-driven)
        spikes = (self.r > threshold).astype(float)
        self.r[spikes > 0] = 0  # reset
        return spikes, self.phi
```

### Hardware Considerations
- **Memristor crossbars**: Real/imaginary parts on separate crossbar arrays
- **Phase detection**: Time-to-digital converters for phase measurement
- **Event routing**: Address-event representation (AER) with phase tags

## Applications

### 1. Signal Processing
- **Beamforming**: Phase differences encode spatial information
- **Frequency analysis**: Natural FFT-like computation
- **Coherent detection**: Phase-sensitive pattern matching

### 2. Associative Memory
- **Complex Hopfield networks**: Higher capacity via phase coding
- **Sequence memory**: Phase progression encodes temporal order
- **Pattern binding**: Complex multiplication binds features

### 3. Sensory Processing
- **Auditory**: Phase encodes frequency/ITD cues
- **Visual**: Phase encodes edge orientation/position
- **Olfactory**: Phase synchrony encodes odor identity

## Comparison with Prior Work

| Method | Capacity | Energy | Biological Plausibility |
|--------|----------|--------|------------------------|
| Real-valued SNN | Baseline | Low | High |
| Rate-coded ANN | High | High | Low |
| **Complex SNN** | **2× real** | **Medium** | **Medium** |
| Phase-only coding | Limited | Very Low | Medium |

## Open Questions

1. **Optimal phase coding**: What phase schemes maximize information?
2. **Learning stability**: How to prevent phase drift during training?
3. **Hardware primitives**: What neuromorphic devices best support complex operations?
4. **Biological evidence**: Do real neurons use complex-valued computation?

## References

- Original paper: arXiv:2606.29099
- Complex-valued networks: Hirose (2012)
- Event-driven learning: Tavanaei et al. (2019)
- Phase coding in neuroscience: Buzsáki (2006)
