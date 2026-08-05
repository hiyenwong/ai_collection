---
name: numa-balancing-spiking-network-hpc
description: "NUMA balancing performance optimization for spiking network simulations on HPC systems. Identifies that automatic NUMA balancing can reduce energy efficiency by 30% in spiking network simulations and provides methodology for per-job NUMA balancing control to optimize performance and energy consumption."
metadata:
  arxiv_id: "2607.22275"
  published: "2026-07-24"
  authors: "Melissa Lober, Alp Inangu, Gorka Peraza Coppola, Dennis Terhorst, Sebastian Gillessen, Jan Vogelsang, Hans Ekkehard Plesser, Brian Wylie, Benedikt Steinbusch, Guido Trensch, Susanne Kunkel, Markus Diesmann"
  tags: [spiking-neural-networks, hpc, numa, performance-optimization, energy-efficiency, distributed-computing]
license: Complete terms in LICENSE.txt
---

# NUMA Balancing Performance Optimization for Spiking Network Simulations

## Overview

This skill addresses a critical performance issue in spiking network simulations on conventional HPC systems: automatic NUMA (Non-Uniform Memory Access) balancing can significantly hamper performance and energy efficiency. The research shows that turning off automatic NUMA balancing may reduce energy consumption by up to 30%, which dwarfs other energy efficiency optimization attempts in terms of cost effectiveness.

## Key Findings

### Problem Identification
- **Memory access pattern interaction**: Spiking network simulation code dynamically interacts with automatic NUMA balancing
- **Performance fluctuations**: Time measurements fluctuate, obstructing optimization efforts
- **Hidden impact**: Does not affect correctness of results, so goes unnoticed in day-to-day neuroscience research
- **Library interference**: Affects jemalloc library for thread-aware memory allocation in a transient manner

### Solution Methodology
- **Per-job NUMA control**: Equip supercomputers with option to turn on/off automatic NUMA balancing on a per-job basis
- **Performance monitoring**: Use time- and compute-node resolved performance display to expose fine-grained temporal variability
- **System perturbation detection**: Method allows developers to detect HPC system perturbations and target specific improvements

## Practical Implementation

### For Researchers
1. **Evaluate NUMA settings**: Test both NUMA balancing ON and OFF for your specific spiking network simulation
2. **Measure performance**: Use fine-grained temporal performance monitoring to identify optimal settings
3. **Document findings**: Record NUMA configuration that provides best performance/energy trade-off for your application

### For System Administrators
1. **Enable per-job control**: Implement user-level options to control NUMA balancing per job submission
2. **Monitor system performance**: Use the proposed performance display methodology to detect system perturbations
3. **Educate users**: Make researchers aware of this phenomenon as it may not be common knowledge in scientific computing

### Performance Analysis Workflow
1. **Baseline measurement**: Run simulation with default NUMA settings
2. **NUMA OFF measurement**: Run identical simulation with automatic NUMA balancing disabled
3. **Compare metrics**: Analyze runtime, energy consumption, and memory access patterns
4. **Fine-grained analysis**: Use time- and node-resolved performance displays to identify temporal variability
5. **Optimize configuration**: Select NUMA setting that provides optimal performance for the specific application

## Technical Details

### NUMA Balancing Impact
- **Energy reduction**: Up to 30% energy consumption reduction when NUMA balancing is disabled
- **Runtime improvement**: Corresponding decrease in application runtime
- **Memory allocation**: Transient effects on jemalloc thread-aware memory allocation
- **Correctness preservation**: Simulation results remain correct regardless of NUMA setting

### Applicability
- **HPC systems**: Conventional CPU- and GPU-based supercomputing centers
- **Spiking network simulations**: Large-scale neural network simulation codes
- **Scientific computing**: Potentially applicable to other scientific codes with similar memory access patterns
- **Neuromorphic reference**: Relevant as conventional systems serve as reference for neuromorphic computing energy efficiency claims

## Activation Keywords

- numa balancing spiking networks
- hpc performance optimization neuroscience
- energy efficiency spiking simulations
- memory access pattern neuroscience
- jemalloc numa interference
- distributed spiking network performance
- supercomputer numa configuration

## References

- arXiv:2607.22275 - NUMA balancing hampering performance of spiking network simulations
- DOI: https://doi.org/10.48550/arXiv.2607.22275

## Pitfalls and Considerations

### Common Misconceptions
- **Assumption of universal benefit**: Automatic NUMA balancing is not universally beneficial for all workloads
- **Overlooked impact**: Performance impact may go unnoticed due to preserved result correctness
- **Limited awareness**: Phenomenon may not be common knowledge in scientific computing communities

### Implementation Challenges
- **System-specific behavior**: NUMA behavior may vary across different HPC architectures
- **Workload dependency**: Optimal NUMA settings depend on specific simulation characteristics
- **Monitoring overhead**: Fine-grained performance monitoring may introduce additional overhead

### Broader Implications
- **Energy efficiency claims**: Neuromorphic computing energy efficiency comparisons should account for optimized conventional system performance
- **Scientific reproducibility**: NUMA settings should be documented in computational neuroscience publications
- **HPC best practices**: This finding suggests need for workload-specific NUMA optimization strategies in scientific computing