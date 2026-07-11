# Graph Neural ODE Digital Twins for Control-Oriented Reactor Thermal-Hydraulic Forecasting

**arXiv ID**: 2604.07292v1
**Published**: 2026-04-08
**Authors**: Akzhol Almukhametov, Doyeong Lim, Rui Hu, Yang Liu
**PDF**: https://arxiv.org/pdf/2604.07292v1

## Summary

This paper presents a physics-informed GNN-ODE surrogate model for real-time forecasting of reactor thermal-hydraulic states at uninstrumented locations. The model achieves 105× faster inference than simulation while maintaining accuracy.

## Key Contributions

### 1. Directed Sensor Graph Representation

System represented as directed graph:
- Nodes: Sensors and components
- Edges: Hydraulic connectivity (flow/heat transfer)

### 2. Physics-Informed Message Passing

Edge encoding carries physical information:
- Flow rate
- Heat transfer coefficient
- Pressure differential

### 3. Neural ODE for Continuous Dynamics

Continuous-time state evolution:
```
dx/dt = f(x, t, u)  # u = control input
```

### 4. Topology-Guided Missing Node Initialization

Estimate uninstrumented node states from:
- Graph structure
- Neighbor observations
- Physical connectivity

## Performance Metrics

| Metric | Value |
|--------|-------|
| MAE @ 60s | 0.91 K |
| MAE @ 300s | 2.18 K |
| R² (reconstruction) | up to 0.995 |
| Speedup | 105× faster |
| Ensemble capability | 64-member rollouts |

## Architecture

```
┌────────────────────────────────────────┐
│  Input: Partial sensor observations    │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│  Missing Node Initializer              │
│  (Topology-guided estimation)          │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│  Physics-Informed GNN                  │
│  Message Passing on Hydraulic Graph    │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│  Neural ODE (Continuous Dynamics)      │
│  dx/dt = GNN(x, t, control)            │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│  Output: Full state forecast + UQ      │
└────────────────────────────────────────┘
```

## Applications

### Real-Time Control

- Forecast uninstrumented states
- Enable model predictive control
- Update every timestep (ms-scale)

### Uncertainty Quantification

- 64-member ensemble rollouts
- Probabilistic state estimates
- Confidence bounds on predictions

### Sim-to-Real Transfer

- Layerwise discriminative fine-tuning
- 30 training sequences sufficient
- Reynolds-number exponent matches correlations

## Code Resources

```python
# Core components
from torch_geometric.nn import MessagePassing
from torchdiffeq import odeint

# Physics-informed edge encoding
edge_features = [flow_rate, heat_transfer_coeff, pressure]

# Neural ODE forward pass
trajectory = odeint(ode_func, x0, t_span, method='dopri5')
```

## Citation

Almukhametov, A., Lim, D., Hu, R., & Liu, Y. (2026). Graph Neural ODE Digital Twins for Control-Oriented Reactor Thermal-Hydraulic Forecasting Under Partial Observability. arXiv:2604.07292v1.