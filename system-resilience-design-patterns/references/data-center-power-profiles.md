# Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning

**arXiv ID**: 2604.07345v1
**Published**: 2026-04-08
**Authors**: Roberto Vercellino, Jared Willard, Gustavo Campos, Weslley da Silva Pereira, Olivia Hull
**PDF**: https://arxiv.org/pdf/2604.07345v1

## Summary

This paper presents a methodology linking high-resolution workload power measurements (0.1-second resolution) to whole-facility energy demand for data center infrastructure planning using bottom-up event-driven modeling.

## Key Contributions

### 1. High-Resolution Power Profiling

- 0.1-second sampling (10 Hz)
- NVIDIA H100 GPU measurements
- Training, fine-tuning, and inference profiles

### 2. Standardized Benchmarks

- MLCommons benchmarks for training/fine-tuning
- vLLM benchmarks for inference
- Reproducible workload characterization

### 3. Bottom-Up Facility Model

Event-driven simulation:
- GPU power aggregation
- Cooling system dynamics
- Power distribution losses
- User behavior patterns

### 4. Infrastructure Planning Outputs

- Grid connection capacity
- On-site generation sizing
- Battery storage requirements
- PUE optimization targets

## Measurement Setup

| Component | Specification |
|-----------|---------------|
| GPU | NVIDIA H100 |
| Sampling | 0.1s resolution |
| Workloads | Training, Fine-tuning, Inference |
| Benchmarks | MLCommons, vLLM |

## Modeling Pipeline

```
┌─────────────────────────────────────────────┐
│  Workload Execution                         │
│  ┌───────────────────────────────────────┐ │
│  │ MLCommons Training Benchmarks         │ │
│  │ vLLM Inference Benchmarks             │ │
│  └───────────────────────────────────────┘ │
│              ↓                               │
│  ┌───────────────────────────────────────┐ │
│  │ High-Resolution Power Measurement     │ │
│  │ 10 Hz sampling, per-GPU               │ │
│  └───────────────────────────────────────┘ │
│              ↓                               │
│  ┌───────────────────────────────────────┐ │
│  │ Event-Driven Facility Model           │ │
│  │ • Cooling overhead (PUE)              │ │
│  │ • PDU losses                          │ │
│  │ • User arrival simulation             │ │
│  └───────────────────────────────────────┘ │
│              ↓                               │
│  ┌───────────────────────────────────────┐ │
│  │ Whole-Facility Energy Profile         │ │
│  │ Temporal fluctuations captured        │ │
│  └───────────────────────────────────────┘ │
│              ↓                               │
│  Infrastructure Planning Recommendations    │
└─────────────────────────────────────────────┘
```

## Facility Model Components

### 1. GPU Aggregation

```python
# Single GPU power profile
gpu_power = measure_gpu_power(workload, resolution=0.1)

# Multi-GPU aggregation based on user arrivals
active_gpus = simulate_user_arrivals(n_users, arrival_pattern)
total_gpu_power = gpu_power * active_gpus
```

### 2. Cooling Overhead

```python
# PUE (Power Usage Effectiveness)
pue = 1.4  # Typical data center
cooling_power = gpu_power * (pue - 1)
```

### 3. PDU Losses

```python
# Power distribution unit efficiency
pdu_efficiency = 0.95  # 5% loss in distribution
pdu_loss = total_power * (1 - pdu_efficiency)
```

## Infrastructure Planning Outputs

| Output | Calculation | Purpose |
|--------|-------------|---------|
| Grid capacity | peak_power × margin | Connection sizing |
| Generation capacity | mean_power | Solar/generator sizing |
| Battery storage | (peak - mean) × hours | Peak shaving |
| PUE target | cooling_efficiency | Efficiency goal |

## Key Results

- Public dataset of power profiles released
- Realistic temporal fluctuations captured
- Enables grid/microgrid integration planning
- Supports sustainable infrastructure design

## Applications to System Design

### Data Center Planning

- Size electrical infrastructure
- Plan cooling systems
- Design power distribution

### Grid Integration

- Connection capacity requirements
- Peak demand management
- Load forecasting

### Microgrid Design

- On-site generation sizing
- Battery storage optimization
- Renewable integration

### Sustainability

- Energy efficiency optimization
- Carbon footprint estimation
- Green infrastructure planning

## Citation

Vercellino, R., Willard, J., Campos, G., Pereira, W. S., & Hull, O. (2026). Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning. arXiv:2604.07345v1.