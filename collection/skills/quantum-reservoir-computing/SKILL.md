---
name: quantum-reservoir-computing
description: "Quantum Reservoir Computing (QRC) framework covering chaotic dynamics prediction, thermodynamic limits, symmetry exploitation, amplitude encoding protocols, hybrid architectures, operating band localization, and Kerr feedback superiority. Use for designing energy-efficient QRC systems, aligning symmetries across QRC interfaces, and selecting optimal operating regimes."
---

# Quantum Reservoir Computing for Chaotic Dynamics

This skill implements the Quantum Reservoir Computing (QRC) framework for time-series prediction on chaotic systems, benchmarking against variational Quantum Physics-Informed Neural Networks (QPINN).

## Overview

Deploying quantum machine learning on NISQ devices requires architectures where training overhead does not negate computational advantages. This methodology systematically compares QRC (fixed-reservoir) vs QPINN (variational) approaches for chaotic time-series prediction.

## Key Findings

### Performance Comparison (4-5 qubits, 2-3 layers)
- **QRC MSE**: ~10^-3 (significantly lower)
- **QPINN MSE**: Higher error
- **Training Speed**: QRC trains ~10,000x faster (0.2s vs hours per seed)
- **Root Cause**: QPINN instability stems from capacity limitations and competing loss terms, NOT barren plateaus

## Activation Keywords
- quantum reservoir computing
- QRC
- QPINN
- quantum physics-informed neural network
- chaotic dynamics
- Lorenz system
- fixed-reservoir quantum
- variational quantum architecture

## Tools Used
- exec: Run quantum simulations and benchmarks
- python: Implement QRC and QPINN architectures

## Core Methodology

### 1. Quantum Reservoir Computing (QRC)

#### Architecture
```
Input State → Quantum Reservoir (Fixed Hamiltonian) → Measurement → Classical Readout
```

#### Fixed Hamiltonian
- Transverse-field Ising model
- Fixed parameters (no variational optimization)
- Natural quantum dynamics as reservoir states

#### Temporal Windowing Technique
Based on classical delay-embedding principle:
```python
def temporal_window(input_history, window_size):
    """
    Provide bounded, structured input history
    Improves attractor reconstruction
    """
    return input_history[-window_size:]
```

### 1.5 Hybrid Quantum-Classical Reservoir Computing (HRC)

**Key insight**: Standalone QRC produces fundamentally linear outputs for single input states, preventing computation of nonlinear functionals (purity, entropy). The hybrid architecture overcomes this by combining a qubit quantum reservoir with a classical Echo State Network.

**Architecture**:
```
Quantum Input States → Quantum Reservoir (qubits) → Measurement → Classical ESN → Output
```

**Usage**: Nonlinear quantum functional approximation, temporal processing of quantum state sequences, experimental assessment with measurement back-action. Particularly advantageous in partial information regime (single-axis measurements). See `hybrid-quantum-classical-reservoir-computing` skill (arXiv:2606.21327).

### 1.6 Amplitude-Encoded Online QRC Protocol

**Key insight**: Amplitude encoding on quantum hardware is achievable via mid-circuit measurement and reset operations that implement partial-trace dynamics, without interrupting temporal processing.

**Protocol**:
```
Input qubits → Mid-circuit measurement + reset → Partial-trace dynamics → Indirect measurement of memory qubits
```

**Benefits**:
- Preserves online operation (no input buffering)
- Runtime stays linear in number of time steps
- Dual monitoring: direct (input qubits) + indirect (memory qubits) measurement channels
- Enables full system observation while isolating internal reservoir evolution

**Design Principle**: Use mid-circuit measurement+reset instead of full circuit execution for amplitude encoding. Keep runtime linear by avoiding input buffering. See `amplitude-encoded-quantum-reservoir-protocol` skill (arXiv:2606.18991).

### 1.7 Symmetry Exploitation in QRC

**Key insight**: A symmetric Hamiltonian alone is NOT sufficient for symmetry-aligned QRC. The relevant symmetry must be visible in the measured feature map — optimization cannot recover channels that were never measured.

**Problem**: For cyclic forecasting tasks (sensors around turbine, weather stations along latitude), rotating the input by one site should rotate (not change) the predicted field. A symmetric Hamiltonian with mismatched measurement channels fails even with large Pauli measurement sets.

**Solution: Observable-Orbit Completion**
1. Measure all symmetry-related observable channels
2. Align encoding, dynamics, measurement, and readout interfaces simultaneously
3. The strongest gains come from aligning ALL four interfaces together

**Design Principle**: Don't just make the Hamiltonian symmetric — ensure measurement captures the symmetry. Validate on matched hardware (spin-ring, weather data, IBM) for consistent mechanism. See `qrc-symmetry-exploitation` skill (arXiv:2607.01187).

### 1.8 Locating the Transferable Operating Band

**Key insight**: Good QRC performance concentrates in a single, well-defined operating region of control space (input drive strength, qubit coupling, dissipation rate). This region transfers across tasks and reservoir initializations.

**How to find it**: Use a simple memory diagnostic before running any task to locate the operating region cheaply.

**Design Principle**: The operating region is mechanistically grounded — it disappears whenever any of the mechanisms that create it is removed. Can be located cheaply before any task runs. See arXiv:2606.13284.

### 1.9 Non-Markovian Kerr Feedback Superiority

**Key insight**: A single Kerr (nonlinear) mode with time-delayed feedback outperforms any N-mode Gaussian (linear) reservoir. Feedback turns time into space: D passes through one nonlinear mode replace D parallel linear modes.

**Resource separation**: N-mode Gaussian reservoir reaches cross-time nonlinear rank at most 2N (hardware ceiling); single Kerr mode reaches rank equal to feedback depth D (achievable D = 30–230 on integrated platforms). Loss is the counterintuitive ingredient — each round-trip dims light differently, giving every echo its own fingerprint.

**Design Principle**: One nonlinear mode + feedback replaces up to ~100 linear modes, at the price of measurement time. See arXiv:2606.06689.

### 2. Quantum Physics-Informed Neural Network (QPINN)

#### Architecture
```
Input → Variational Quantum Circuit (Trainable) → Measurement → Physics-Informed Loss
```

#### Loss Components
1. **Data Loss**: MSE between predictions and ground truth
2. **Physics Loss**: Residuals of governing equations
3. **Regularization**: Parameter norm constraints

#### Failure Mode Analysis
- **NOT Barren Plateaus**: Gradient norms remain large (~10^-1)
- **Capacity Limitation**: Limited expressivity for complex dynamics
- **Competing Objectives**: Data fidelity vs physics constraints

## Implementation

### QRC Implementation
```python
import pennylane as qml
import numpy as np

class QuantumReservoir:
    def __init__(self, n_qubits, hamiltonian_params):
        self.n_qubits = n_qubits
        self.params = hamiltonian_params  # Fixed!
        self.dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode
    def reservoir_dynamics(self, input_state, time_steps):
        # Initialize state
        qml.MottonenStatePreparation(input_state, wires=range(self.n_qubits))
        
        # Apply fixed Hamiltonian evolution
        for t in range(time_steps):
            self._ising_step()
        
        # Return expectation values
        return [qml.expval(qml.PauliZ(i)) for i in range(self.n_qubits)]
    
    def _ising_step(self):
        # Transverse-field Ising model
        for i in range(self.n_qubits):
            qml.RX(self.params['h'], wires=i)
        for i in range(self.n_qubits - 1):
            qml.IsingXX(self.params['J'], wires=[i, i+1])
```

### Temporal Windowing
```python
class TemporalWindowEncoder:
    def __init__(self, window_size, stride=1):
        self.window_size = window_size
        self.stride = stride
    
    def encode(self, time_series):
        """
        Create delay-embedded windows for reservoir input
        """
        windows = []
        for i in range(0, len(time_series) - self.window_size, self.stride):
            window = time_series[i:i + self.window_size]
            windows.append(window)
        return np.array(windows)
```

### Benchmarking Framework
```python
class QuantumChaosBenchmark:
    def __init__(self, system='lorenz'):
        self.system = system
        self.systems = {
            'lorenz': LorenzSystem(),
            'rossler': RosslerSystem(),
            'lorenz96': Lorenz96System()
        }
    
    def benchmark(self, model, n_seeds=10):
        results = []
        for seed in range(n_seeds):
            # Generate data
            train_data, test_data = self.systems[self.system].generate(seed)
            
            # Train and evaluate
            model.train(train_data)
            mse = model.evaluate(test_data)
            train_time = model.training_time
            
            results.append({
                'seed': seed,
                'mse': mse,
                'train_time': train_time
            })
        
        return self._aggregate(results)
```

## Test Systems

### 1. Lorenz System
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```
Parameters: σ=10, ρ=28, β=8/3

### 2. Rössler System
```
dx/dt = -y - z
dy/dt = x + ay
dz/dt = b + z(x - c)
```
Parameters: a=0.2, b=0.2, c=5.7

### 3. Lorenz-96 System
N-dimensional chaotic system with forcing F:
```
dx_i/dt = (x_{i+1} - x_{i-2})x_{i-1} - x_i + F
```

## Results Summary

| System | QRC MSE | QPINN MSE | QRC Training | QPINN Training |
|--------|---------|-----------|--------------|----------------|
| Lorenz | ~10^-3 | Higher | 0.2s | Hours |
| Rössler | ~10^-3 | Higher | 0.2s | Hours |
| Lorenz-96 | ~10^-3 | Higher | 0.2s | Hours |

## Key Insights

1. **Fixed-Reservoir Advantage**: Non-variational approach avoids optimization instabilities
2. **No Barren Plateaus**: Gradients remain tractable at tested scales
3. **Temporal Structure**: Delay embedding crucial for attractor reconstruction
4. **NISQ Compatibility**: Minimal quantum circuit depth required

## Advanced Technique: Split-Ensemble Training

From "Reorganizing Quantum Measurement Records Improves Time-Series Prediction" (arXiv:2604.28160v1, 2026-04-30).

### Problem
Standard approach averages all shots from one labeled time step into a single feature vector. This reduces finite-shot noise but gives the readout only one training example per time step — too few for effective learning.

### Solution: Split-Ensemble Training
Split the same measurement shots into groups, and use each group average as a separate, partially denoised feature vector for the same target:

```python
def split_ensemble(shots, n_groups):
    """
    Split measurement records into n_groups.
    Each group average becomes a separate training example.
    No additional quantum circuit executions required.
    """
    group_size = len(shots) // n_groups
    groups = [shots[i*group_size:(i+1)*group_size] for i in range(n_groups)]
    feature_vectors = [np.mean(g, axis=0) for g in groups]
    return feature_vectors  # n_groups examples for same target
```

### Benefits
- **More training data** without additional quantum hardware cost
- **Partial denoising** from group averaging (trade-off between noise reduction and data quantity)
- **Strongest gains on real hardware** where shot noise is significant
- **Broadly applicable** across quantum reservoir computing tasks

### Integration with QRC
```python
class EnhancedQRC(QuantumReservoir):
    def extract_features_split(self, input_history, window_size, n_groups=4):
        """
        Split-ensemble feature extraction for QRC.
        Instead of averaging all shots, split into groups.
        """
        all_shots = self.run_circuit(input_history, n_shots=1024)
        # Split into groups, each gives a training example
        feature_groups = split_ensemble(all_shots, n_groups)
        # Each group is a partially-denoised feature vector
        return feature_groups
```

## References

- Paper: "Fixed-Reservoir vs Variational Quantum Architectures for Chaotic Dynamics: Benchmarking QRC and QPINN on the Lorenz System" (arXiv:2604.23743)
- Paper: "Reorganizing Quantum Measurement Records Improves Time-Series Prediction" (arXiv:2604.28160v1, 2026-04-30) - Split-Ensemble Training
- Author: Tushar Pandey (QRC); Markus Baumann et al. (Split-Ensemble)
- Categories: Quantum Physics (quant-ph), Machine Learning (cs.LG)

## Best Practices

1. **Use Temporal Windowing**: Essential for capturing dynamics
2. **Apply Split-Ensemble**: When readout has too few training examples, split shots into groups (n_groups=4-8 recommended)
3. **Start Small**: Test on 4-5 qubits before scaling
4. **Monitor Gradients**: Verify non-vanishing gradients in QPINN
5. **Multiple Seeds**: Average over random initializations
6. **Physics Validation**: Compare reconstructed attractors visually

## Medical Dataset Applications

### Hardware-Induced Regularization on Small Medical Data

When applying QRC to small, complex medical datasets (biomarker prediction, < 1000 samples),
hardware execution on neutral-atom Rydberg processors produces a **beneficial regularization effect**:

- **Mean compression** — feature values shift toward mean, reducing extreme values
- **Mutual information decay** — progressive MI reduction between features
- **Reduced variance** across data splits vs noiseless emulation

This is NOT simple noise degradation — it acts as implicit regularization (analogous to dropout
in classical DL). See [[quantum-reservoir-medical-regularization]] skill (arXiv: 2602.14641)
for full methodology.

### When to Use QRC for Medical Prediction

- Dataset < 1000 samples with nonlinear, correlated biomarkers
- Classical ML overfits on emulation; hardware noise provides regularization
- Use SHAP for feature subset selection before quantum encoding
- Always compare emulation vs hardware execution

## Limitations

- Tested on small qubit counts (4-5)
- Quantum advantage not yet demonstrated
- Requires classical optimization of readout layer
- Hardware noise not fully characterized
- Split-ensemble: optimal group size depends on total shot budget and noise level

## Related Skills
- quantum-machine-learning
- physics-informed-neural-networks
- chaotic-systems-modeling
- quantum-reservoir-medical-regularization — QRC for small medical datasets; hardware-induced regularization effect on neutral-atom processors
