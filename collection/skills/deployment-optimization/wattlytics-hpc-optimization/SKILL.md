---
name: wattlytics-hpc-optimization
description: "Wattlytics: Co-Optimizing Performance, Energy, and TCO in HPC Clusters. Use for holistic what-if analysis across hardware-software stack for HPC planning and operation. Activation: HPC optimization, performance energy trade-off, TCO analysis, cluster configuration optimization."
---

# Wattlytics: HPC Cluster Optimization

Interactive decision-support system for co-optimizing performance, energy, and total cost of ownership (TCO) in GPU-accelerated HPC clusters.

## Overview

This skill implements the Wattlytics methodology from arXiv:2604.08182v1 for holistic HPC cluster optimization.

**Key Benefits:**
- Holistic what-if analysis across hardware-software stack
- Trade-off exploration between performance, energy, and TCO
- Actionable insights for HPC center planning and operation

## Core Framework

### Optimization Objectives

```python
objectives = {
    "performance": {
        "metrics": ["throughput", "latency", "job_completion_time"],
        "weight": 0.4
    },
    "energy": {
        "metrics": ["power_consumption", "energy_efficiency", "PUE"],
        "weight": 0.3
    },
    "tco": {
        "metrics": ["capex", "opex", "lifetime_cost"],
        "weight": 0.3
    }
}
```

### Model Components

1. **Performance Models**: Analytical models for workload performance
2. **Power Models**: Power consumption based on utilization
3. **Cost Models**: CAPEX and OPEX calculations

## Workflow

### Step 1: Define Cluster Configuration

```python
cluster_config = {
    "compute_nodes": {
        "count": 100,
        "gpu_per_node": 8,
        "gpu_type": "NVIDIA H100",
        "cpu": "AMD EPYC 9654",
        "memory_gb": 2048
    },
    "interconnect": {
        "type": "InfiniBand NDR",
        "topology": "fat-tree"
    },
    "cooling": {
        "type": "liquid_cooled",
        "pue_target": 1.1
    }
}
```

### Step 2: Define Workload Characteristics

```python
workload_profile = {
    "job_types": [
        {"name": "AI_training", "percentage": 60, "gpu_hours_per_job": 100},
        {"name": "simulation", "percentage": 30, "gpu_hours_per_job": 50},
        {"name": "inference", "percentage": 10, "gpu_hours_per_job": 10}
    ],
    "arrival_rate": "poisson",  # jobs per hour
    "utilization_target": 0.85
}
```

### Step 3: Run What-If Analysis

```python
# Scenario 1: Increase GPU count
scenario_1 = modify_config(cluster_config, {"compute_nodes.gpu_per_node": 16})
results_1 = analyze(scenario_1, workload_profile)

# Scenario 2: Change cooling type
scenario_2 = modify_config(cluster_config, {"cooling.type": "air_cooled", "cooling.pue_target": 1.3})
results_2 = analyze(scenario_2, workload_profile)

# Compare scenarios
comparison = compare_results([results_1, results_2])
```

## Analysis Functions

### Performance Analysis

```python
def analyze_performance(config, workload):
    """
    Estimate job completion times and throughput.
    """
    # Use analytical performance models
    # Consider network topology, GPU interconnect, etc.
    return {
        "throughput_jobs_per_hour": ...,
        "avg_job_completion_time_hours": ...,
        "bottleneck": ...
    }
```

### Energy Analysis

```python
def analyze_energy(config, workload):
    """
    Estimate power consumption and energy efficiency.
    """
    # Calculate based on component power curves
    # Include cooling overhead
    return {
        "peak_power_kw": ...,
        "avg_power_kw": ...,
        "annual_energy_mwh": ...,
        "pue": ...,
        "energy_efficiency_gflops_per_watt": ...
    }
```

### TCO Analysis

```python
def analyze_tco(config, workload, energy_results, years=5):
    """
    Calculate total cost of ownership.
    """
    capex = calculate_capex(config)
    opex = calculate_opex(energy_results, years)
    
    return {
        "capex_usd": capex,
        "opex_5yr_usd": opex,
        "tco_5yr_usd": capex + opex,
        "cost_per_gpu_hour": (capex + opex) / total_gpu_hours
    }
```

## Decision Matrix

| Configuration | Performance | Energy | TCO | Recommendation |
|---------------|-------------|--------|-----|----------------|
| Baseline | 100% | 100% | 100% | Current |
| +GPU/node | +30% | +25% | +20% | High ROI |
| Air cooling | -5% | +40% | +15% | Not recommended |

## References

- Paper: Wattlytics: A Web Platform for Co-Optimizing Performance, Energy, and TCO in HPC Clusters (arXiv:2604.08182v1)
- Authors: Ayesha Afzal, Georg Hager, Gerhard Wellein
- Platform: https://wattlytics.netlify.app
