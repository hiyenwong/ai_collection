---
name: temporal-poisoning-clean-label-backdoors-snn
description: Skill for understanding and applying clean-label backdoor attacks via event redistribution in Spiking Neural Networks (SNNs) from arXiv paper 2607.28075
trigger_words: neuroscience, spiking neural network, SNN, backdoor attack, temporal poisoning, neuromorphic
---

# Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs

**arXiv ID**: 2607.28075v1
**Date**: 2026-07-30
**Authors**: Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta

## Overview
This skill encapsulates the methodology for clean-label temporal poisoning attacks on Spiking Neural Networks (SNNs), where a fixed timestamp transformation is applied only to target-class training streams while preserving per-pixel, per-polarity event counts exactly.

## Core Contributions
- First clean-label backdoor attack evaluated on SNNs and neuromorphic event data
- Temporal poisoning that preserves event counts but alters sequence processing by SNNs
- Achieves Attack Success Rate (ASR) of 1.00 in strongest configurations across three neuromorphic datasets
- Works on both convolutional and transformer-based SNN architectures
- Demonstrates limitations of rate-collapsed defenses against temporal attacks

## Methodology
### Attack Design
- **Clean-label approach**: Target-class training samples retain original labels
- **Temporal transformation**: Fixed timestamp transformation applied only to target class
- **Event preservation**: Per-pixel, per-polarity event count preserved exactly
- **Stealth mechanism**: Clean and triggered samples identical after temporal aggregation

### Evaluation Framework
- **Datasets**: Three neuromorphic datasets (NMNIST, SHD, IBM DVS Gesture)
- **Victim models**: Both convolutional and transformer-based SNNs
- **Metrics**: Attack Success Rate (ASR), poison budget analysis, trigger shape ablations
- **Defenses tested**: Rate-collapsed defenses, feature-space methods, model-free detection

### Detection Methods
- **Rate-collapsed defenses**: Blind by construction to temporal transformations
- **Feature-space methods**: Detect poison only in selected settings
- **Model-free detector**: Based on per-step event mass, effectively detects temporal transformations

## Applications
### Security Research
- Understanding vulnerabilities in SNN deployment scenarios
- Developing robust defenses against temporal poisoning attacks
- Evaluating security of neuromorphic hardware systems

### Defense Development
- Implementing temporal-aware inspection mechanisms
- Designing SNN architectures resistant to clean-label backdoors
- Creating monitoring systems for event-based anomaly detection

## Implementation Guidelines
1. **Data preparation**: Extract neuromorphic event streams from target datasets
2. **Temporal transformation**: Apply fixed timestamp shifts to target-class events
3. **Training**: Train SNN with poisoned clean-label data
4. **Evaluation**: Test ASR on triggered samples while maintaining accuracy on clean samples
5. **Defense testing**: Evaluate against rate-collapsed and feature-space defenses

## Key Insights
- Temporal information in SNNs creates unique attack surface not present in traditional ANNs
- Clean-label attacks are more stealthy and realistic than dirty-label approaches
- Event-based systems require temporal-aware security measures
- Model-free detection based on event mass provides effective defense

## References
- [Original Paper](https://arxiv.org/abs/2607.28075v1)
- [arXiv:2607.28075 [cs.CR]](https://arxiv.org/abs/2607.28075)
- Related work on SNN security and neuromorphic computing