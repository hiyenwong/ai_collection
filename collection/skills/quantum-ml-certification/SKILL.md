---
name: quantum-ml-certification
description: >
  Methodology for certified and robust quantum machine learning. Combines
  Interval Bound Propagation (IBP) for certified robustness training of QNNs,
  conformal prediction for distribution-free uncertainty quantification, and
  Lindblad dynamics learning for quantum noise characterization.
  Use when: building quantum neural networks with robustness guarantees,
  quantifying uncertainty in quantum ML predictions, characterizing quantum
  processor noise via ML, or implementing certified quantum training pipelines.
  Trigger: quantum ML certification, certified QNN, quantum robustness,
  conformal quantum learning, Lindblad dynamics, quantum uncertainty quantification.
---

# Quantum ML Certification & Robustness

Certified training and uncertainty quantification for quantum machine learning models.

## Core Concepts

### 1. Quantum Interval Bound Propagation (IBP)
Extends classical IBP to Quantum Neural Networks (QNNs) to provide
certified robustness guarantees against input perturbations.

**Key idea**: Propagate input bounds through quantum circuit layers
using interval arithmetic on rotation angles and measurement outcomes.

### 2. Conformalized Quantum DeepONet Ensembles
Combines quantum-enhanced operator learning with conformal prediction
to provide statistically valid prediction intervals without distributional assumptions.

**Key idea**: Use quantum neural networks as base predictors, then
apply conformal calibration on held-out data to produce valid
prediction intervals with guaranteed coverage.

### 3. Lindblad Dynamics Learning
Uses ML to infer Lindblad master equation parameters from
experimental quantum processor data for accurate noise modeling.

**Key idea**: Parameterize the Lindblad superoperator and optimize
against experimental trajectory data to characterize open quantum system dynamics.

## Workflow

### Step 1: Define Quantum Model Architecture

```python
import pennylane as qml
import numpy as np

def qnn_circuit(params, x, n_qubits=4):
    """Parametrized quantum circuit for classification."""
    for i in range(n_qubits):
        qml.RY(x[i], wires=i)
    for layer in range(2):
        for i in range(n_qubits):
            qml.Rot(*params[layer, i], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i+1])
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Step 2: Interval Bound Propagation for QNNs

```python
def propagate_bounds(params, x_lower, x_upper, n_qubits=4):
    """Propagate input bounds through quantum circuit.
    
    Returns output bounds for each measurement expectation value.
    """
    # Lower/upper bounds on rotation angles
    for layer in range(2):
        # Interval arithmetic for rotation gates
        angle_lower = np.minimum(x_lower, x_upper)
        angle_upper = np.maximum(x_lower, x_upper)
        
        # Propagate through parametrized rotations
        # For RY: output range depends on input range and parameter
        param_lower = params[layer] - epsilon  # parameter uncertainty
        param_upper = params[layer] + epsilon
        
        # Update bounds using monotonicity properties
        x_lower = angle_lower + param_lower
        x_upper = angle_upper + param_upper
    
    # Compute measurement bounds
    output_lower = np.tanh(x_lower)  # bounded activation
    output_upper = np.tanh(x_upper)
    
    return output_lower, output_upper
```

### Step 3: Conformal Prediction for Quantum ML

```python
def conformal_calibration(model, cal_data, cal_labels, alpha=0.1):
    """Calibrate conformal prediction scores on held-out data.
    
    Args:
        model: Trained quantum neural network
        cal_data: Calibration dataset inputs
        cal_labels: Calibration dataset labels
        alpha: Desired miscoverage rate (e.g., 0.1 for 90% coverage)
    
    Returns:
        quantile: Conformal quantile for prediction sets
    """
    # Compute nonconformity scores on calibration set
    scores = []
    for x, y in zip(cal_data, cal_labels):
        pred = model.predict(x)
        scores.append(nonconformity_score(pred, y))
    
    # Compute quantile for desired coverage
    n = len(scores)
    quantile = np.quantile(scores, np.ceil((n + 1) * (1 - alpha)) / n)
    return quantile

def conformal_predict(model, x_new, quantile):
    """Generate conformal prediction set for new input."""
    pred = model.predict(x_new)
    # Include all labels whose nonconformity score <= quantile
    prediction_set = [y for y in all_labels 
                      if nonconformity_score(pred, y) <= quantile]
    return prediction_set
```

### Step 4: Lindblad Dynamics Learning

```python
def learn_lindblad_dynamics(data_trajectories, n_qubits, dt=0.01):
    """Learn Lindblad superoperator from experimental data.
    
    Fits the generator of quantum dynamics:
    dρ/dt = -i[H, ρ] + Σ_k (L_k ρ L_k† - ½{L_k†L_k, ρ})
    """
    # Parameterize Hamiltonian H and jump operators L_k
    H_params = initialize_hermitian(n_qubits)
    L_params = initialize_operators(n_qubits, n_jump=3)
    
    # Optimize against trajectory data
    for epoch in range(100):
        loss = 0
        for traj in data_trajectories:
            # Simulate dynamics with current parameters
            simulated = simulate_lindblad(H_params, L_params, traj.t, dt)
            loss += mse(simulated, traj.rho_observed)
        
        # Gradient update
        H_params -= lr * gradient_H(loss, H_params)
        L_params -= lr * gradient_L(loss, L_params)
    
    return H_params, L_params
```

## Verification Steps

1. **IBP Certification**: Verify that output bounds are valid certificates
   by checking inclusion: true_output ∈ [output_lower, output_upper]

2. **Conformal Coverage**: Verify empirical coverage ≥ 1 - α on test set

3. **Lindblad Accuracy**: Validate learned dynamics reproduce held-out
   experimental trajectories within measurement noise

## Common Pitfalls

- **IBP looseness**: Bounds may be loose for deep circuits; consider
  using linear relaxation or symbolic interval propagation for tighter bounds
- **Conformal exchangeability**: Requires i.i.d. calibration data; use
  conformal adaptive methods for distribution shift
- **Lindblad identifiability**: Not all parameters may be identifiable
  from available measurements; use regularization or physical constraints

## References

- Andrews et al. (2026): Quantum Interval Bound Propagation for Certified Training of QNNs
- Matlia et al. (2026): Conformalized Quantum DeepONet Ensembles for Scalable Operator Learning
- Severin et al. (2026): Learning Lindblad Dynamics of a Superconducting Quantum Processor
