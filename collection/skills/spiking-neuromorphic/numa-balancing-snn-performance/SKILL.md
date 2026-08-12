---
name: numa-balancing-snn-performance
title: NUMA Balancing Performance Optimization for Spiking Neural Networks
version: 1.0.0
description: Methodology for optimizing spiking neural network simulation performance by managing NUMA balancing settings on HPC systems.
tags:
  - neuroscience
  - spiking-neural-networks
  - hpc
  - performance-optimization
  - numa
trigger: When running spiking neural network simulations on NUMA-enabled HPC systems and experiencing performance fluctuations or suboptimal energy efficiency.
---

# NUMA Balancing Performance Optimization for Spiking Neural Networks

## Overview

This skill addresses a critical but often overlooked performance issue in spiking neural network (SNN) simulations on modern NUMA (Non-Uniform Memory Access) enabled HPC systems. The research shows that automatic NUMA balancing can significantly hamper SNN simulation performance and increase energy consumption by up to 30%.

## Key Findings

- **Performance Impact**: Automatic NUMA balancing can reduce energy efficiency by 30% in SNN simulations
- **Memory Access Pattern**: SNN simulation code has dynamic memory access patterns that interact poorly with automatic NUMA balancing
- **Detection Method**: Time- and compute-node resolved performance displays can expose fine-grained temporal variability
- **Root Cause**: Automatic NUMA balancing affects the jemalloc library for thread-aware memory allocation in a transient manner
- **Solution**: Turning off automatic NUMA balancing on a per-job basis provides optimal performance

## Implementation Steps

### 1. Detect NUMA Balancing Issues

Monitor performance metrics during SNN simulations:
- Look for fluctuating time measurements
- Check for inconsistent energy consumption across runs
- Use performance profiling tools that show node-level metrics

### 2. Configure NUMA Settings

For Linux systems, control NUMA balancing via:
```bash
# Check current NUMA balancing status
cat /proc/sys/kernel/numa_balancing

# Disable NUMA balancing (requires root)
echo 0 | sudo tee /proc/sys/kernel/numa_balancing

# Enable NUMA balancing
echo 1 | sudo tee /proc/sys/kernel/numa_balancing
```

### 3. Per-Job NUMA Control

For HPC environments with job schedulers:
```bash
# SLURM example - disable NUMA balancing for specific job
srun --ntasks=64 --cpus-per-task=1 bash -c 'echo 0 > /proc/sys/kernel/numa_balancing && your_snn_simulation_command'
```

### 4. Memory Allocation Optimization

Ensure proper memory allocation strategy:
- Use jemalloc or similar thread-aware allocators
- Pre-allocate memory where possible
- Consider memory binding policies using `numactl`

### 5. Performance Validation

After disabling NUMA balancing:
- Run benchmark simulations
- Measure energy consumption reduction
- Verify simulation correctness remains intact

## Best Practices

1. **Always Test**: Compare performance with and without NUMA balancing for your specific SNN workload
2. **Job-Level Control**: Implement per-job NUMA balancing control rather than system-wide changes
3. **Monitor System Perturbations**: Use the time-resolved performance display method to detect other HPC system issues
4. **Documentation**: Document NUMA settings used for reproducible research
5. **Energy Awareness**: Consider energy consumption as a key metric alongside runtime

## Verification

The optimization is successful when:
- Runtime decreases by 10-30%
- Energy consumption shows consistent reduction
- Performance measurements become more stable across runs
- Simulation results remain numerically identical

## References

- Lober, M., Inangu, A., Coppola, G. P., Terhorst, D., Gillessen, S., Vogelsang, J., ... & Diesmann, M. (2026). NUMA balancing hampering performance of spiking network simulations. arXiv:2607.22275v1
- Related work on NUMA effects in scientific computing

## Activation Keywords

- numa balancing
- spiking network performance
- HPC energy efficiency
- jemalloc NUMA
- distributed SNN simulation