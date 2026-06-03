---
name: probe-trajectory-reasoning-monitoring
description: Probe trajectory methodology for monitoring Large Reasoning Model (LRM) internal dynamics. Tracks concept probability evolution across Chain of Thought tokens using signal-processing features (volatility, trend, steady-state) to predict future model behavior.
category: ai_collection
---

# Probe Trajectory Reasoning Monitoring

## Overview

Probe trajectories provide a continuous monitoring framework for Large Reasoning Models (LRMs) by evaluating concept probability at each generated token during Chain of Thought (CoT) reasoning. Rather than relying on a single static probe prediction, the full temporal evolution encodes task-specific dynamics that improve outcome separability.

## Core Methodology

### 1. Per-Token Probe Evaluation
- Evaluate a linear probe at **every generated token** during CoT reasoning
- Construct a probe trajectory: continuous evolution of concept probability across reasoning process
- Future behavior is more distinguishable when examined over the full trajectory vs. single static prediction

### 2. Signal-Processing Feature Extraction
Extract temporal dynamics from probe trajectories:
- **Volatility**: Variance/rate of change in probe confidence
- **Trend**: Directional movement (increasing/decreasing confidence)
- **Steady-state**: Final convergence behavior

### 3. Critical Design Choices
- **Pooling matters**: 
  - Max-pooling: achieves up to 95% AUROC, yields stable trajectories
  - Average-pooling and last-token: collapse to near-random performance
- **Training data**: Template-based training achieves near-parity with dynamically generated responses, eliminating costly inference and labeling

## Implementation

```python
# Per-token probe evaluation during generation
def build_probe_trajectory(model, tokenizer, prompt, probe):
    trajectory = []
    # Generate token by token, evaluating probe at each step
    for token_position in range(max_length):
        hidden_states = get_hidden_states(model, current_input)
        probe_score = probe(hidden_states)  # concept probability
        trajectory.append(probe_score)
    return trajectory

# Signal-processing features
def extract_trajectory_features(trajectory):
    features = {
        'volatility': np.std(np.diff(trajectory)),
        'trend': np.polyfit(range(len(trajectory)), trajectory, 1)[0],
        'steady_state': np.mean(trajectory[-10:]) if len(trajectory) > 10 else trajectory[-1],
        'max_confidence': np.max(trajectory),
    }
    return features
```

## Key Findings

1. **Trajectory > Static**: Full trajectory analysis significantly outperforms single-point probes
2. **Max-pooling is essential**: Other pooling strategies collapse performance
3. **Templates suffice**: Template-based training data is nearly as good as model-generated responses
4. **Cross-domain applicability**: Works for both safety monitoring and mathematical reasoning

## Activation

probe trajectory, reasoning monitoring, LRM safety, CoT faithfulness, internal monologue, reasoning dynamics, outcome prediction

## Reference

- arXiv: 2605.18549
- "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"
