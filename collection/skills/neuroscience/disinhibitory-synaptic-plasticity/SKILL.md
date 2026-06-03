---
name: disinhibitory-synaptic-plasticity
description: 'Model dis-inhibitory neuronal circuits that control synaptic plasticity sign. Bridge functional error-modulated learning with Hebbian plasticity through adaptive control theory. Predict inhibitory modulation effects on excitatory plasticity.'
---

# Dis-inhibitory Synaptic Plasticity Control

## Description

A microcircuit model showing how dis-inhibitory synaptic afferents encode errors, enabling error-modulated learning to emerge naturally at circuit level when recurrent inhibition influences Hebbian plasticity. Bridges functional error back-propagation with experimentally observed Hebbian plasticity rules.

**Source:** arXiv:2310.19614v2 (NeurIPS 2023)
**Utility:** 0.91

## Activation Keywords

- disinhibitory circuit
- synaptic plasticity sign
- error-modulated learning
- hebbian plasticity inhibition
- credit assignment neuronal
- adaptive control plasticity
- inhibitory modulation plasticity
- top-down disinhibition

## Core Concepts

### 1. Credit Assignment Problem

**Central Question in Systems Neuroscience:**
- How neuronal circuits achieve credit assignment?
- How error signals propagate through multi-layer networks?
- How local errors determine synaptic plasticity sign?

**Traditional Solutions:**
- Back-propagation (BP) - functional but biologically implausible
- Distinct neuronal compartments for local error signals
- Explicit error modulation - inconsistent with Hebbian plasticity

### 2. Dis-inhibitory Circuit Model

**Key Innovation:**
- Errors encoded in **top-down dis-inhibitory synaptic afferents**
- Recurrent inhibition explicitly influences Hebbian plasticity
- Error-modulated learning emerges naturally at circuit level

**Microcircuit Structure:**
```
Top-down input → Interneuron (INH) ↓
                          ↓ (disinhibition)
Excitatory neuron (EXC) ← Local input
                          ↓ (Hebbian plasticity)
Output neuron
```

### 3. Adaptive Control Theory Framework

**Learning Rule:**
```
Δw = η * (pre * post - λ * inh * post)

where:
- pre: presynaptic activity
- post: postsynaptic activity
- inh: inhibitory input
- λ: inhibition influence factor
- η: learning rate
```

**Key Insight:**
- Inhibition modifies the effective postsynaptic term
- Sign of plasticity depends on inhibition balance
- Natural emergence of error-modulated learning

### 4. Bridging Functional and Phenomenological Models

| Model Type | Plasticity Sign Determination |
|------------|------------------------------|
| Functional (BP) | Error signal explicit |
| Phenomenological (Hebbian) | Postsynaptic activity |
| Dis-inhibitory | Postsynaptic + Inhibition |

**Resolution:**
- Hebbian rule remains valid
- Inhibition provides error encoding
- No need for distinct error compartments

## Step-by-Step Instructions

### 1. Dis-inhibitory Microcircuit Model

```python
import numpy as np
from typing import Tuple, Optional

class DisinhibitoryMicrocircuit:
    """
    Dis-inhibitory neuronal circuit for error-modulated learning.
    
    Architecture:
    - Top-down input disinhibits excitatory neurons
    - Recurrent inhibition modulates Hebbian plasticity
    - Error signals encoded in disinhibition
    
    Args:
        n_exc: Number of excitatory neurons
        n_inh: Number of inhibitory neurons
        learning_rate: Plasticity learning rate
        inhibition_factor: Influence of inhibition on plasticity
    """
    def __init__(
        self,
        n_exc: int = 10,
        n_inh: int = 5,
        learning_rate: float = 0.01,
        inhibition_factor: float = 0.5
    ):
        self.n_exc = n_exc
        self.n_inh = n_inh
        self.eta = learning_rate
        self.lambda_inh = inhibition_factor
        
        # Initialize weights
        self.w_exc = np.random.randn(n_exc, n_exc) * 0.1  # Excitatory weights
        self.w_inh = np.random.randn(n_inh, n_exc) * 0.1  # Inhibitory weights
        self.w_topdown = np.random.randn(n_inh) * 0.1     # Top-down to inhibitory
        
        # Activity variables
        self.exc_activity = np.zeros(n_exc)
        self.inh_activity = np.zeros(n_inh)
        
    def compute_activity(
        self,
        local_input: np.ndarray,
        topdown_input: float
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute excitatory and inhibitory activity.
        
        Args:
            local_input: Local input to excitatory neurons
            topdown_input: Top-down disinhibitory input
        
        Returns:
            exc_activity: Excitatory neuron activity
            inh_activity: Inhibitory neuron activity
        """
        # Inhibitory neurons receive top-down input
        self.inh_activity = np.tanh(self.w_topdown * topdown_input)
        
        # Excitatory neurons receive local input minus inhibition
        inhibition = np.dot(self.w_inh.T, self.inh_activity)
        total_input = local_input - inhibition
        self.exc_activity = np.tanh(total_input)
        
        return self.exc_activity, self.inh_activity
    
    def hebbian_plasticity_with_inhibition(
        self,
        pre_activity: np.ndarray,
        post_activity: np.ndarray,
        inh_activity: np.ndarray
    ) -> np.ndarray:
        """
        Hebbian plasticity rule with inhibition modulation.
        
        Δw = η * (pre * post - λ * inh * post)
        
        Args:
            pre_activity: Presynaptic activity
            post_activity: Postsynaptic activity
            inh_activity: Inhibitory activity
        
        Returns:
            weight_change: Weight update
        """
        # Standard Hebbian term
        hebbian = np.outer(pre_activity, post_activity)
        
        # Inhibition modulation term
        inh_modulation = self.lambda_inh * np.outer(inh_activity, post_activity)
        
        # Combined plasticity
        weight_change = self.eta * (hebbian - inh_modulation)
        
        return weight_change
    
    def update_weights(
        self,
        pre_activity: np.ndarray,
        post_activity: np.ndarray,
        inh_activity: np.ndarray
    ):
        """
        Update excitatory weights with dis-inhibitory plasticity.
        
        Args:
            pre_activity: Presynaptic activity
            post_activity: Postsynaptic activity
            inh_activity: Inhibitory activity
        """
        weight_change = self.hebbian_plasticity_with_inhibition(
            pre_activity, post_activity, inh_activity
        )
        
        self.w_exc += weight_change
        
        # Clip weights to prevent explosion
        self.w_exc = np.clip(self.w_exc, -1.0, 1.0)
```

### 2. Error Encoding in Disinhibition

```python
class ErrorEncodingDisinhibition:
    """
    Encode errors in top-down disinhibitory signals.
    
    Key insight:
    - Positive error → increased disinhibition → enhanced plasticity
    - Negative error → reduced disinhibition → suppressed plasticity
    """
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
        
    def encode_error(self, error: float) -> float:
        """
        Encode error signal as disinhibitory input.
        
        Args:
            error: Error signal (positive = too low, negative = too high)
        
        Returns:
            disinhibitory_signal: Top-down disinhibitory input
        """
        # Disinhibition proportional to positive error
        if error > 0:
            disinhibitory_signal = error * self.threshold
        else:
            disinhibitory_signal = 0.0
        
        return disinhibitory_signal
    
    def compute_plasticity_sign(
        self,
        post_activity: float,
        inh_activity: float,
        error: float
    ) -> str:
        """
        Determine sign of synaptic plasticity.
        
        Args:
            post_activity: Postsynaptic activity
            inh_activity: Inhibitory activity
            error: Error signal
        
        Returns:
            sign: 'LTP' (long-term potentiation) or 'LTD' (long-term depression)
        """
        effective_post = post_activity - self.lambda_inh * inh_activity
        
        if effective_post > 0:
            return 'LTP'
        else:
            return 'LTD'
```

### 3. Comparison with Back-Propagation

```python
class PlasticityComparison:
    """
    Compare dis-inhibitory plasticity with back-propagation.
    
    Benchmarks:
    - XOR problem
    - Circle classification
    - Spiral classification
    """
    def __init__(self, n_hidden: int = 10):
        self.n_hidden = n_hidden
        
    def generate_xor_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate XOR problem data.
        
        Returns:
            X: Input patterns
            y: Target outputs
        """
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([[0], [1], [1], [0]])
        return X, y
    
    def train_disinhibitory(
        self,
        X: np.ndarray,
        y: np.ndarray,
        epochs: int = 100
    ) -> list:
        """
        Train dis-inhibitory circuit on XOR.
        
        Args:
            X: Input patterns
            y: Target outputs
            epochs: Training epochs
        
        Returns:
            losses: Training loss history
        """
        circuit = DisinhibitoryMicrocircuit(
            n_exc=self.n_hidden,
            n_inh=5,
            learning_rate=0.1
        )
        
        losses = []
        
        for epoch in range(epochs):
            epoch_loss = 0.0
            
            for i in range(len(X)):
                # Forward pass
                exc_act, inh_act = circuit.compute_activity(X[i], 0.5)
                
                # Compute error
                output = np.mean(exc_act)
                error = y[i, 0] - output
                epoch_loss += error**2
                
                # Update with dis-inhibitory plasticity
                circuit.update_weights(X[i], exc_act, inh_act)
            
            losses.append(epoch_loss / len(X))
        
        return losses
    
    def train_backprop(
        self,
        X: np.ndarray,
        y: np.ndarray,
        epochs: int = 100
    ) -> list:
        """
        Train standard back-propagation on XOR.
        
        Args:
            X: Input patterns
            y: Target outputs
            epochs: Training epochs
        
        Returns:
            losses: Training loss history
        """
        # Simple MLP with back-prop
        W1 = np.random.randn(2, self.n_hidden) * 0.1
        W2 = np.random.randn(self.n_hidden, 1) * 0.1
        
        losses = []
        
        for epoch in range(epochs):
            epoch_loss = 0.0
            
            for i in range(len(X)):
                # Forward pass
                h = np.tanh(np.dot(X[i], W1))
                output = np.tanh(np.dot(h, W2))
                
                # Compute error
                error = y[i, 0] - output
                epoch_loss += error**2
                
                # Back-prop
                d_output = error * (1 - output**2)
                d_hidden = np.dot(W2, d_output) * (1 - h**2)
                
                # Update weights
                W2 += 0.1 * np.outer(h, d_output)
                W1 += 0.1 * np.outer(X[i], d_hidden)
            
            losses.append(epoch_loss / len(X))
        
        return losses
    
    def compare_performance(self) -> dict:
        """
        Compare dis-inhibitory vs back-prop performance.
        
        Returns:
            comparison: Performance comparison results
        """
        X, y = self.generate_xor_data()
        
        # Train both models
        losses_disinh = self.train_disinhibitory(X, y, epochs=100)
        losses_bp = self.train_backprop(X, y, epochs=100)
        
        comparison = {
            'disinhibitory': {
                'final_loss': losses_disinh[-1],
                'convergence': len([l for l in losses_disinh if l > 0.1])
            },
            'backprop': {
                'final_loss': losses_bp[-1],
                'convergence': len([l for l in losses_bp if l > 0.1])
            }
        }
        
        return comparison
```

### 4. Experimental Predictions

```python
class InhibitoryModulationPredictions:
    """
    Experimental predictions from dis-inhibitory plasticity model.
    
    Predictions:
    1. Blocking inhibition enhances LTP
    2. Enhancing inhibition suppresses LTP or induces LTD
    3. Top-down inputs modulate plasticity through interneurons
    """
    def __init__(self):
        self.predictions = {
            'prediction_1': 'Blocking inhibition should enhance excitatory plasticity',
            'prediction_2': 'Enhancing inhibition should suppress or reverse plasticity',
            'prediction_3': 'Top-down disinhibitory inputs control plasticity sign'
        }
        
    def simulate_inhibition_blocking(self) -> dict:
        """
        Simulate effect of blocking inhibition.
        
        Returns:
            results: Simulation results showing enhanced LTP
        """
        circuit = DisinhibitoryMicrocircuit(n_exc=10, n_inh=5)
        
        # Normal condition
        exc_normal, inh_normal = circuit.compute_activity(
            np.random.randn(10), 0.5
        )
        delta_w_normal = circuit.hebbian_plasticity_with_inhibition(
            exc_normal, exc_normal, inh_normal
        )
        
        # Blocked inhibition (set inh to 0)
        delta_w_blocked = circuit.hebbian_plasticity_with_inhibition(
            exc_normal, exc_normal, np.zeros(5)
        )
        
        results = {
            'normal_plasticity': np.mean(delta_w_normal),
            'blocked_plasticity': np.mean(delta_w_blocked),
            'enhancement_factor': np.mean(delta_w_blocked) / np.mean(delta_w_normal)
        }
        
        return results
    
    def simulate_inhibition_enhancement(self) -> dict:
        """
        Simulate effect of enhancing inhibition.
        
        Returns:
            results: Simulation results showing suppressed/reversed plasticity
        """
        circuit = DisinhibitoryMicrocircuit(n_exc=10, n_inh=5)
        
        # Normal condition
        exc_normal, inh_normal = circuit.compute_activity(
            np.random.randn(10), 0.5
        )
        delta_w_normal = circuit.hebbian_plasticity_with_inhibition(
            exc_normal, exc_normal, inh_normal
        )
        
        # Enhanced inhibition
        inh_enhanced = inh_normal * 2.0
        delta_w_enhanced = circuit.hebbian_plasticity_with_inhibition(
            exc_normal, exc_normal, inh_enhanced
        )
        
        results = {
            'normal_plasticity': np.mean(delta_w_normal),
            'enhanced_plasticity': np.mean(delta_w_enhanced),
            'suppression_factor': np.mean(delta_w_enhanced) / np.mean(delta_w_normal)
        }
        
        return results
    
    def test_predictions(self) -> dict:
        """
        Test all experimental predictions.
        
        Returns:
            test_results: Validation of predictions
        """
        blocking_results = self.simulate_inhibition_blocking()
        enhancement_results = self.simulate_inhibition_enhancement()
        
        test_results = {
            'blocking_enhances_LTP': blocking_results['enhancement_factor'] > 1.0,
            'enhancement_suppresses_LTP': enhancement_results['suppression_factor'] < 1.0,
            'predictions_validated': all([
                blocking_results['enhancement_factor'] > 1.0,
                enhancement_results['suppression_factor'] < 1.0
            ])
        }
        
        return test_results
```

### 5. Complete Workflow

```python
def disinhibitory_plasticity_workflow(
    input_data: np.ndarray,
    target_data: np.ndarray,
    epochs: int = 100
) -> dict:
    """
    Complete dis-inhibitory plasticity learning workflow.
    
    Args:
        input_data: Training inputs
        target_data: Training targets
        epochs: Training epochs
    
    Returns:
        results: Training results and predictions
    """
    # Initialize circuit
    circuit = DisinhibitoryMicrocircuit(
        n_exc=len(input_data[0]),
        n_inh=5,
        learning_rate=0.1
    )
    
    # Training
    losses = []
    for epoch in range(epochs):
        epoch_loss = 0.0
        
        for i in range(len(input_data)):
            # Compute activity
            exc_act, inh_act = circuit.compute_activity(input_data[i], 0.5)
            
            # Compute error
            output = np.mean(exc_act)
            error = target_data[i] - output
            epoch_loss += error**2
            
            # Update weights
            circuit.update_weights(input_data[i], exc_act, inh_act)
        
        losses.append(epoch_loss / len(input_data))
    
    # Test predictions
    predictor = InhibitoryModulationPredictions()
    predictions = predictor.test_predictions()
    
    results = {
        'training_loss': losses[-1],
        'loss_history': losses,
        'predictions': predictions,
        'final_weights': circuit.w_exc
    }
    
    return results
```

## Tools Used

- `numpy` - Numerical computations
- `typing` - Type annotations
- `matplotlib` - Visualization (optional)
- `exec` - Run simulation scripts

## Example Use Cases

### 1. XOR Learning

```python
# Train on XOR problem
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

results = disinhibitory_plasticity_workflow(X, y, epochs=100)
print(f"Final loss: {results['training_loss']}")
```

### 2. Plasticity Sign Control

```python
# Demonstrate plasticity sign control
circuit = DisinhibitoryMicrocircuit(n_exc=10, n_inh=5)

# With inhibition
exc, inh = circuit.compute_activity(np.ones(10), 0.5)
sign_with_inh = circuit.hebbian_plasticity_with_inhibition(exc, exc, inh)

# Without inhibition
sign_without_inh = circuit.hebbian_plasticity_with_inhibition(exc, exc, np.zeros(5))

print(f"With inhibition: {np.mean(sign_with_inh)}")
print(f"Without inhibition: {np.mean(sign_without_inh)}")
```

### 3. Experimental Validation

```python
# Test experimental predictions
predictor = InhibitoryModulationPredictions()
results = predictor.test_predictions()

print(f"Blocking enhances LTP: {results['blocking_enhances_LTP']}")
print(f"Enhancement suppresses LTP: {results['enhancement_suppresses_LTP']}")
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Dis-inhibitory Microcircuit Model

## Examples

### Example 1: Basic Application

**User:** I need to apply Dis-inhibitory Synaptic Plasticity Control to my analysis.

**Agent:** I'll help you apply disinhibitory-synaptic-plasticity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for disinhibitory-synaptic-plasticity?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `stdp-bernoulli-message-passing` - STDP plasticity
- `neuromodulated-synaptic-plasticity` - Neuromodulated learning
- `multi-plasticity-synergy-snn` - Multi-plasticity in SNN

## References

- Rossbroich, J. et al. (2023). "Dis-inhibitory neuronal circuits can control the sign of synaptic plasticity" arXiv:2310.19614v2 [q-bio.NC] (NeurIPS 2023)

---

**Created:** 2026-03-29 23:05
**Author:** Aerial (from arXiv:2310.19614v2)