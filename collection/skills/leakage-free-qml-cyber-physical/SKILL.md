---
name: leakage-free-qml-cyber-physical
description: "Leakage-free evaluation methodology for quantum ML in cyber-physical systems. Temporal group-aware protocols and feature audits prevent inflated performance claims."
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
source: arXiv:2605.19233
metadata:
  hermes:
    tags: [Quantum-ML, Evaluation, Cyber-Physical, Anomaly-Detection, Benchmarking]
---

# Leakage-Free Quantum ML Evaluation for Cyber-Physical Systems

## Overview
Provides rigorous evaluation methodology for quantum ML applications in cyber-physical systems, preventing performance inflation from data leakage.

**Paper**: arXiv:2605.19233 (May 2026)

## Core Methodology

### B2 Temporal Protocol
- Partition dataset into contiguous time blocks
- Evaluate over multiple seeds
- Eliminate inflation from random stratified splits mixing neighboring samples

### Three-Mode Feature Audit
- **Full mode**: all features including contextual proxies
- **Loose mode**: partial feature restriction
- **Strict mode**: proxy-free evaluation (only instantaneous physical signals)
- Quantifies accuracy contribution from proxies vs genuine signals

### Hybrid Benchmarking
- Benchmark hybrid quantum-classical models against classical controls
- Use identical computational budgets
- Report per-seed variance alongside mean performance

**Activation**: leakage-free evaluation, quantum ML benchmark, cyber-physical anomaly, UAV detection, temporal protocol, feature audit, DRU classifier
