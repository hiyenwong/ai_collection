---
name: quantum-fast-weight-memory-gates
description: Stable Self-Modulating Quantum Fast-Weight Programmers (QFWPs) with bounded memory gates for quantum sequence modeling. Prevents long-sequence divergence via sign-preserving tanh gates on recurrent memory branch. Based on arXiv:2607.02363.
trigger_words: quantum fast weight programmer, quantum sequence modeling, bounded memory gate, QFWP, self-modulating quantum, quantum dynamics forecasting, quantum RNN
---

# Quantum Fast-Weight Memory Gates

## Description

Stable Self-Modulating Quantum Fast-Weight Programmers (QFWPs) for quantum sequence modeling. QFWPs store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states. Introduces bounded old-state modulation via sign-preserving tanh gates to prevent long-sequence divergence. Based on arXiv:2607.02363 (Peng et al., 2026).

## Activation Keywords

- quantum fast weight programmer
- QFWP bounded memory
- self-modulating quantum programmer
- quantum sequence modeling
- quantum memory gate
- quantum dynamics forecasting
- quantum RNN stability

## Core Methodology

### 1. Standard QFWP Baseline

```python
import numpy as np
from typing import Tuple

class StandardQFWP:
    """Standard Quantum Fast-Weight Programmer."""
    
    def __init__(self, n_qubits: int, n_layers: int):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        # Fast weights stored as circuit parameters
        self.fast_weights = np.zeros(n_layers * n_qubits * 3)  # RX, RY, RZ per qubit per layer
    
    def update(self, input_state: np.ndarray, learning_rate: float = 0.01):
        """Update fast weights based on input.
        
        Standard QFWP: additive update
        new_weights = old_weights + lr * gradient(input)
        """
        gradient = self._compute_gradient(input_state)
        self.fast_weights += learning_rate * gradient
    
    def _compute_gradient(self, input_state: np.ndarray) -> np.ndarray:
        """Compute parameter-shift gradient (simplified)."""
        return np.random.randn(len(self.fast_weights)) * 0.1
    
    def predict(self, input_state: np.ndarray) -> np.ndarray:
        """Apply quantum circuit with current fast weights."""
        # Simplified: linear projection through parameterized unitary
        W = self.fast_weights.reshape(self.n_layers, self.n_qubits, 3)
        output = input_state.copy()
        for layer in W:
            for qubit, angles in enumerate(layer):
                # Apply rotation gates
                output[qubit] *= np.exp(1j * angles[0])  # RX
                output[qubit] *= np.exp(1j * angles[1])  # RY
                output[qubit] *= np.exp(1j * angles[2])  # RZ
        return np.abs(output)**2
```

### 2. Self-Modulating QFWP (Bounded Old-State)

```python
class BoundedSelfModulatingQFWP:
    """Self-Modulating QFWP with bounded old-state gate.
    
    Key innovation: apply sign-preserving tanh gate ONLY to recurrent
    memory branch, leaving additive update and new-update modulation unchanged.
    """
    
    def __init__(self, n_qubits: int, n_layers: int, bound_scale: float = 1.0):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.bound_scale = bound_scale
        self.fast_weights = np.zeros(n_layers * n_qubits * 3)
        # Gate parameters (learned)
        self.new_gate_params = np.zeros(n_layers * n_qubits * 3)
        self.old_gate_params = np.zeros(n_layers * n_qubits * 3)
    
    def _tanh_bound(self, weights: np.ndarray) -> np.ndarray:
        """Sign-preserving tanh gate on memory branch."""
        return self.bound_scale * np.tanh(weights / self.bound_scale)
    
    def _sigmoid_gate(self, params: np.ndarray) -> np.ndarray:
        """Sigmoid gating function."""
        return 1.0 / (1.0 + np.exp(-params))
    
    def update_bounded(self, input_state: np.ndarray, learning_rate: float = 0.01):
        """Bounded self-modulating update.
        
        Key difference from unbounded Self-Modulating QFWP:
        - old_state = tanh_bound(old_state)  # BOUND the recurrent branch
        - new_update = sigmoid(new_gate) * gradient(input)
        - fast_weights = old_state + new_update  # Additive update unchanged
        """
        # Step 1: Bound the accumulated memory (sign-preserving tanh)
        bounded_memory = self._tanh_bound(self.fast_weights)
        
        # Step 2: Compute new update with input-dependent gating
        gradient = self._compute_gradient(input_state)
        new_gate = self._sigmoid_gate(self.new_gate_params)
        new_update = new_gate * gradient * learning_rate
        
        # Step 3: Old-state modulation (bounded)
        old_gate = self._sigmoid_gate(self.old_gate_params)
        modulated_old = old_gate * bounded_memory
        
        # Step 4: Combine (additive — no multiplicative blowup)
        self.fast_weights = modulated_old + new_update
    
    def _compute_gradient(self, input_state: np.ndarray) -> np.ndarray:
        return np.random.randn(len(self.fast_weights)) * 0.1
    
    def predict(self, input_state: np.ndarray) -> np.ndarray:
        W = self.fast_weights.reshape(self.n_layers, self.n_qubits, 3)
        output = input_state.copy()
        for layer in W:
            for qubit, angles in enumerate(layer):
                output[qubit] *= np.exp(1j * angles[0])
                output[qubit] *= np.exp(1j * angles[1])
                output[qubit] *= np.exp(1j * angles[2])
        return np.abs(output)**2
```

### 3. Comparative Evaluation Framework

```python
def compare_qfwp_variants(sequences, task_fn, max_seq_len=100):
    """Compare QFWP variants on sequence forecasting tasks.
    
    Variants:
    - Standard QFWP (baseline)
    - Self-Modulating QFWP (unbounded — can diverge)
    - Only-New (only new-update modulation)
    - Only-Old (only old-state modulation)
    - Bounded Self-Modulating (proposed)
    """
    variants = {
        'standard': lambda: StandardQFWP(n_qubits=4, n_layers=2),
        'self_modulating_unbounded': lambda: UnboundedSelfModQFWP(n_qubits=4, n_layers=2),
        'only_new': lambda: OnlyNewModQFWP(n_qubits=4, n_layers=2),
        'only_old': lambda: OnlyOldModQFWP(n_qubits=4, n_layers=2),
        'bounded_self_modulating': lambda: BoundedSelfModulatingQFWP(n_qubits=4, n_layers=2),
    }
    
    results = {}
    for name, factory in variants.items():
        model = factory()
        errors = []
        
        for seq in sequences:
            for t in range(1, min(len(seq), max_seq_len)):
                # Predict next step
                pred = model.predict(seq[:t])
                actual = seq[t]
                error = np.mean((pred - actual)**2)
                errors.append(error)
                
                # Update model
                if hasattr(model, 'update_bounded'):
                    model.update_bounded(seq[t-1])
                else:
                    model.update(seq[t-1])
        
        results[name] = {
            'mean_error': np.mean(errors),
            'max_error': np.max(errors),
            'diverged': np.max(errors) > 10,  # Divergence threshold
            'stability_score': 1.0 / (1.0 + np.max(errors))
        }
    
    return results
```

### 4. Key Findings

**Bounded Old-State Gating**:
- Removes long-sequence divergence present in unbounded Self-Modulating QFWP
- Improves aggregate robustness across tasks
- Maintains the benefits of accumulated-memory modulation

**Only-Old Ablation**:
- Old-state modulation is the most consistent source of improvement over Standard QFWP
- Behavior similar to full Self-Modulating QFWP at longer input windows

**Only-New Ablation**:
- Less effective than old-state modulation
- New-update modulation alone doesn't capture temporal structure as well

## Workflow for Agents

### Step 1: Choose QFWP Variant

For production use → **Bounded Self-Modulating QFWP**
For research comparison → Test all variants

### Step 2: Configure Architecture

```python
model = BoundedSelfModulatingQFWP(
    n_qubits=4,       # Number of qubits
    n_layers=2,       # Circuit depth
    bound_scale=1.0   # Tanh bound scale
)
```

### Step 3: Train on Sequence Data

```python
for timestep, input_state in enumerate(sequence):
    if timestep > 0:
        # Predict
        pred = model.predict(sequence[timestep-1])
        # Update with bounded memory gate
        model.update_bounded(sequence[timestep-1], learning_rate=0.01)
```

### Step 4: Evaluate Stability

```python
# Check for divergence
max_error = compute_max_error(predictions, targets)
if max_error > threshold:
    # Model diverging — bounded variant should prevent this
    print("WARNING: Potential divergence detected")
```

## Error Handling

### Long-Sequence Divergence
```python
# If using unbounded Self-Modulating QFWP, switch to bounded variant
# The tanh gate prevents weight explosion:
# bounded_weights = bound_scale * tanh(weights / bound_scale)
```

### Vanishing Updates
```python
# If bound_scale is too small, increase it
model = BoundedSelfModulatingQFWP(n_qubits=4, n_layers=2, bound_scale=2.0)
```

## Related Skills

- `quantum-neural-dynamics` - quantum neural network dynamics
- `quantum-ml-data-loading` - quantum data loading
- `self-modulating-quantum-fast-weight` - variant reference

## References

- arXiv:2607.02363 - "Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates" (2026)
