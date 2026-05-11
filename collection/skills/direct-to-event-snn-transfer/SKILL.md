---
name: direct-to-event-snn-transfer
description: "Direct-to-event Spiking Neural Network transfer methodology for energy-efficient neuromorphic deployment. Addresses the energy gap between direct-coded SNNs and event-based counterparts by enabling transfer of pretrained direct-coded SNNs to event-driven execution. Use when: (1) deploying SNNs on neuromorphic hardware, (2) optimizing SNN energy efficiency, (3) converting between SNN coding schemes, (4) reusing pretrained SNN databases, (5) event-based inference. Activation: SNN energy efficiency, direct-to-event transfer, event-based SNN, neuromorphic deployment, SNN coding conversion, pretrained SNN reuse."
---

# Direct-to-Event SNN Transfer

Methodology for transferring pretrained direct-coded SNNs to energy-efficient event-driven execution. arXiv:2605.07207 (Luu et al., 2026).

## Problem Statement

Direct-coded SNNs (using surrogate gradient backpropagation) are easier to train but **substantially less energy-efficient** than event-based counterparts. This limits practical deployment in energy-sensitive scenarios.

## Key Insight

Pretrained direct-coded SNNs contain learned weights that can be **transferred** to event-based execution without retraining, enabling reuse of existing SNN databases.

## Transfer Pipeline

### Step 1: Identify Compatible Components

```
Direct-Coded SNN          →    Event-Based SNN
──────────────────────────     ──────────────────
Surrogate activation      →    Real spike generation
Continuous-time simulation →   Event-driven stepping
Frame-based input         →    Sparse event stream
Batch processing          →   Asynchronous processing
```

### Step 2: Weight Transfer

```python
def transfer_weights(direct_snn, event_snn):
    """Transfer weights from direct-coded to event-based SNN."""
    for layer_name in direct_snn.state_dict():
        if 'weight' in layer_name:
            event_snn.state_dict()[layer_name].copy_(
                direct_snn.state_dict()[layer_name]
            )
    return event_snn
```

### Step 3: Threshold Calibration

```python
def calibrate_thresholds(event_snn, calibration_data, target_accuracy=0.95):
    """Calibrate spiking thresholds for event-based execution."""
    best_thresholds = {}
    
    for layer in event_snn.spiking_layers:
        # Find threshold that preserves firing rate distribution
        activations = []
        for batch in calibration_data:
            out = layer(batch)
            activations.append(out.abs().mean().item())
        
        # Set threshold at percentile of activation distribution
        threshold = np.percentile(activations, 95)
        layer.threshold = threshold
        best_thresholds[layer.name] = threshold
    
    return best_thresholds
```

### Step 4: Event-Driven Simulation

```python
def event_driven_inference(event_snn, event_stream):
    """Run inference using event-driven stepping."""
    output_spikes = []
    
    for event in event_stream:
        # Only process active neurons
        active_neurons = event.active_indices
        if len(active_neurons) == 0:
            continue
        
        # Sparse forward pass
        output = event_snn.forward_sparse(active_neurons, event.values)
        output_spikes.append(output)
    
    return output_spikes
```

## Energy Efficiency Comparison

| Metric | Direct-Coded | Event-Based (after transfer) |
|--------|-------------|------------------------------|
| Operations/sample | Dense (all neurons each timestep) | Sparse (only active neurons) |
| Memory access | Full weight matrix per step | Sparse weight access |
| Latency | Fixed (T timesteps) | Variable (event-driven) |
| Power | High (continuous computation) | Low (idle between events) |

## Practical Considerations

1. **Accuracy trade-off**: Expect 1-5% accuracy drop after transfer
2. **Threshold tuning**: Critical for preserving performance
3. **Temporal resolution**: Match event timestamp resolution to training timestep
4. **Batch normalization**: May need recalibration for event-based execution
5. **Hardware support**: Best on true event-driven chips (Loihi, SpiNNaker, DYNAP-SE)

## When to Use

- Deploying existing SNN models to edge/neuromorphic hardware
- Energy-constrained applications (IoT, wearable BCI)
- Reusing large pretrained SNN databases
- Real-time event-based vision/audio processing
