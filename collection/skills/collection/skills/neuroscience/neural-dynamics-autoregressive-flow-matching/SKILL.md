---
name: neural-dynamics-autoregressive-flow-matching
description: Autoregressive Flow Matching (AFM) framework for probabilistic prediction of neural dynamics. Use when working with neural activity forecasting, brain-computer interfaces, generative modeling of neural responses, or multi-step neural prediction with uncertainty quantification. Activation keywords - neural dynamics forecasting, autoregressive flow matching, brain activity prediction, neural response generation, AFM.
---

# Neural Dynamics Autoregressive Flow Matching (AFM)

Probabilistic prediction framework for neural dynamics using autoregressive flow matching. Based on the paper "Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching" (arXiv:2604.11178v1).

## Overview

Autoregressive Flow Matching (AFM) is a generative forecasting framework for modeling neural dynamics that:
- Leverages continuous normalizing flows to capture complex, non-Gaussian distributions of neural responses
- Uses autoregressive conditioning on past neural activity for multi-step forecasting
- Provides probabilistic predictions with uncertainty quantification
- Enables applications in brain-computer interfaces and closed-loop neurostimulation

## Core Methodology

### 1. Flow Matching Foundation

AFM builds on continuous normalizing flows:
- **Transport-based generative models**: Uses flow matching objectives to learn probability paths
- **Continuous-time dynamics**: Models data evolution through time-dependent vector fields
- **Non-Gaussian distributions**: Captures complex, multimodal neural response distributions

### 2. Autoregressive Conditioning

Key principle: Predict future neural activity conditioned on past observations

```
p(x_{t+1:t+k} | x_{1:t}) = AFM_θ(x_{t+1:t+k}; conditioning on history)

Where:
- x_t: Neural activity at time t
- k: Prediction horizon
- θ: Model parameters
```

### 3. Architecture Components

| Component | Description | Purpose |
|-----------|-------------|---------|
| Conditioning Network | Processes historical neural activity | Extract temporal features |
| Flow Matching Network | Learns conditional probability flow | Generate future distributions |
| Uncertainty Head | Quantifies prediction confidence | Estimate prediction intervals |

## Implementation Workflow

### Step 1: Data Preparation

```python
# Prepare neural recording data
# Input: Multi-channel neural recordings (spikes, LFP, fMRI, etc.)

def prepare_neural_data(recordings, window_size=100, prediction_horizon=10):
    """
    Args:
        recordings: Neural activity matrix (time x channels)
        window_size: History window length
        prediction_horizon: Future steps to predict
    
    Returns:
        X: Historical windows (samples x window_size x channels)
        y: Future activity (samples x prediction_horizon x channels)
    """
    X, y = [], []
    for i in range(len(recordings) - window_size - prediction_horizon):
        X.append(recordings[i:i+window_size])
        y.append(recordings[i+window_size:i+window_size+prediction_horizon])
    return np.array(X), np.array(y)
```

### Step 2: Model Training

```python
# Train AFM model
# Use flow matching objective with autoregressive structure

class AFMNeuralDynamics:
    def __init__(self, input_dim, hidden_dim=256, num_flow_steps=10):
        self.conditioning_net = TemporalEncoder(input_dim, hidden_dim)
        self.flow_model = ConditionalFlowMatching(hidden_dim, num_flow_steps)
        self.uncertainty_head = UncertaintyEstimator(hidden_dim)
    
    def forward(self, x_history, target_future=None, num_samples=1):
        # Encode history
        context = self.conditioning_net(x_history)
        
        # Generate future samples using flow matching
        if target_future is not None:
            # Training: compute flow matching loss
            loss = self.flow_model.compute_loss(context, target_future)
            return loss
        else:
            # Inference: sample future trajectories
            predictions = self.flow_model.sample(context, num_samples)
            uncertainties = self.uncertainty_head(context, predictions)
            return predictions, uncertainties
```

### Step 3: Multi-step Forecasting

```python
# Generate multi-step forecasts with uncertainty

def forecast_neural_activity(model, initial_history, num_steps=50, num_samples=100):
    """
    Generate probabilistic forecasts
    
    Args:
        model: Trained AFM model
        initial_history: Initial observation window
        num_steps: Number of future steps to predict
        num_samples: Number of Monte Carlo samples
    
    Returns:
        forecasts: Predicted trajectories (num_samples x num_steps x channels)
        mean_pred: Mean prediction
        std_pred: Prediction standard deviation (uncertainty)
    """
    forecasts = []
    current_history = initial_history.copy()
    
    for step in range(num_steps):
        # Predict next step
        pred, unc = model.forward(current_history, num_samples=num_samples)
        forecasts.append(pred)
        
        # Update history (autoregressive)
        current_history = update_history(current_history, pred)
    
    forecasts = np.array(forecasts)
    mean_pred = forecasts.mean(axis=0)
    std_pred = forecasts.std(axis=0)
    
    return forecasts, mean_pred, std_pred
```

## Key Applications

### 1. Brain-Computer Interfaces (BCIs)

```python
# Real-time neural decoding with AFM

def bci_decoding_pipeline(neural_signal, afm_model, decoder):
    """
    Decode intended actions from neural activity
    
    Process:
    1. Buffer recent neural activity
    2. Use AFM to predict future neural states
    3. Decode predicted states to actions/commands
    4. Quantify prediction confidence
    """
    # Predict future neural activity
    predicted_states, uncertainty = afm_model.forecast(neural_signal)
    
    # Decode to control signals
    control_signal = decoder.decode(predicted_states)
    
    # Confidence-based gating
    if uncertainty < threshold:
        return control_signal, confidence_high
    else:
        return None, confidence_low
```

### 2. Closed-loop Neurostimulation

```python
# Adaptive stimulation based on predicted neural states

def closed_loop_stimulation(neural_recording, target_pattern, afm_model, stimulator):
    """
    Optimize stimulation parameters based on predicted neural response
    
    Process:
    1. Predict neural response to different stimulation parameters
    2. Select parameters that drive activity toward target
    3. Apply stimulation and record actual response
    4. Update model with new observations
    """
    # Predict responses for candidate stimulations
    candidate_params = generate_candidate_parameters()
    predicted_responses = []
    
    for params in candidate_params:
        predicted = afm_model.predict_with_stimulation(neural_recording, params)
        predicted_responses.append(predicted)
    
    # Select optimal parameters
    optimal_params = select_optimal(predicted_responses, target_pattern)
    
    # Apply stimulation
    stimulator.deliver(optimal_params)
    
    return optimal_params
```

### 3. Neural Activity Synthesis

```python
# Generate synthetic neural responses for testing

def synthesize_neural_responses(afm_model, stimulus_conditions, num_trials=100):
    """
    Generate realistic neural activity for given stimulus conditions
    
    Use cases:
    - Data augmentation for training other models
    - Testing decoding algorithms
    - Simulating neural responses for experimental design
    """
    synthetic_data = []
    for condition in stimulus_conditions:
        # Condition neural activity generation
        initial_state = condition.get_initial_state()
        
        # Generate multiple trials
        trials = afm_model.sample_trajectories(
            initial_state, 
            num_trials=num_trials,
            condition_on=condition
        )
        synthetic_data.append(trials)
    
    return synthetic_data
```

## Technical Specifications

### Model Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `hidden_dim` | 256 | Dimension of conditioning network |
| `num_flow_steps` | 10 | Number of flow matching steps |
| `learning_rate` | 1e-4 | Training learning rate |
| `window_size` | 100 | Historical context window |
| `prediction_horizon` | 10 | Future steps to predict |

## Advantages Over Traditional Methods

| Aspect | Traditional | AFM |
|--------|-------------|-----|
| Distribution | Assumes Gaussian | Captures non-Gaussian |
| Uncertainty | Often ignored | Explicitly quantified |
| Multi-step | Accumulates error | Autoregressive conditioning |
| Flexibility | Fixed model | Generative, adaptable |

## Limitations

1. **Data requirements**: Needs substantial neural recording data for training
2. **Computational cost**: Flow matching more expensive than simple regression
3. **Stationarity assumption**: Assumes stable neural dynamics during training
4. **Interpretability**: Complex generative models may be less interpretable

## References

- Rogalla, N., Qin, Y., & Senden, M. (2026). Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching. arXiv:2604.11178v1.
- Lipman, Y., et al. (2023). Flow Matching for Generative Modeling.

## Activation Keywords

- neural dynamics forecasting
- autoregressive flow matching
- brain activity prediction
- neural response generation
- AFM neural dynamics
- probabilistic neural prediction
- brain-computer interface forecasting
- closed-loop neurostimulation
