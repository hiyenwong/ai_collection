---
name: spike-sparsity-deployment-cost
description: >-
  Analyzing deployment cost of spiking neural networks on edge hardware.
  Demonstrates that algorithmic spike sparsity may not translate to actual
  deployed cost reduction on commodity edge GPUs. Covers VS-WNO (Variable-Spiking
  Wavelet Neural Operator), WNO comparison, Jetson Orin Nano profiling.
  Activation: spike sparsity deployment, edge GPU SNN, neuromorphic deployment cost,
  VS-WNO, wavelet neural operator, SNN hardware, Jetson profiling.
version: 1.0.0
metadata:
  hermes:
    tags: [snn, deployment, edge-computing, neuromorphic, hardware, spiking, performance]
    source_paper: "When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano (arXiv:2604.17040)"
    citations: 0
---

# Spike Sparsity vs Deployment Cost Analysis

## Overview

Spiking neural networks achieve algorithmic sparsity through event-driven computation,
but this does not always translate to reduced deployed cost on commodity hardware.
This skill covers methodology for profiling and analyzing the gap between algorithmic
sparsity and actual hardware performance for SNN deployment.

## Key Insight

On Jetson Orin Nano 8GB, VS-WNO shows substantial algorithmic sparsity (mean spike rates
54.26% → 18.15% across layers), but deployment-style request paths show no cost reduction
vs dense WNO. Sparsity only helps under specific hardware/software stack conditions.

## Critical Parameters

| Parameter | Description | Impact |
|-----------|-------------|--------|
| Spike rate | Mean activity per layer | Lower ≠ always faster |
| Request path | Deployment vs reference-aligned | Critical distinction |
| Batch size | Workload batching | Affects sparsity utilization |
| Memory bandwidth | GPU memory bottleneck | Often dominates over compute |

## Analysis Methodology

1. Profile both reference-aligned and deployment-style request paths
2. Measure per-layer spike rates and correlate with wall-clock time
3. Compare against matched dense model baselines
4. Profile memory bandwidth utilization vs compute utilization

## Pitfalls

- Do not assume algorithmic sparsity → hardware efficiency
- Edge GPU software stacks may not exploit sparsity
- Memory bandwidth often dominates compute in sparse workloads
- Batch size significantly affects sparsity utilization

## References

- Original: Yoo et al., arXiv:2604.17040 (April 2026)
