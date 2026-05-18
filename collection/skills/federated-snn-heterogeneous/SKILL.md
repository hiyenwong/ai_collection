---
name: federated-snn-heterogeneous-temporal
category: research
created: "2026-05-19"
source: "arXiv:2605.15355v1"
description: Federated learning framework for SNNs that addresses temporal resolution mismatch across edge devices. Enables clients to train at local temporal resolution while remaining compatible with global model aggregation.
tags: [snn, federated-learning, temporal-heterogeneity, edge-computing, stateful-neurons]
---

# Federated Learning of SNNs under Heterogeneous Temporal Resolutions

**Source**: arXiv:2605.15355v1 - "Federated Learning of Spiking Neural Networks under Heterogeneous Temporal Resolutions"

## Summary

Addresses the fundamental challenge of temporal resolution mismatch in federated SNN learning. When edge devices collect data at different time resolutions (due to hardware/energy constraints), naive federated averaging fails because parameters learned at one resolution don't transfer directly to another. Proposes adaptation methods that recover accuracy lost due to temporal mismatch.

## Core Methodology

### Key Problem
- Edge devices in federated learning collect time-series data at different temporal resolutions
- SNNs and deep networks with stateful neurons are sensitive to temporal resolution
- Naive FedAvg is ineffective when clients have different sampling rates
- Parameters at one resolution don't directly transfer to another

### Solution
- Framework for integrating neuron parameters learned from different temporal resolutions
- Adaptation methods for model aggregation across resolution mismatches
- Each client trains at local temporal resolution while remaining compatible with global model

### Evaluation
- SNN-native benchmarks: SHD (Spiking Heidelberg Datasets) and DVS-Gesture
- Range of resolution heterogeneity scenarios
- Substantial accuracy recovery compared to naive federated averaging

## When to Use
- Federated learning of SNNs across heterogeneous edge devices
- Time-series applications with varying sampling rates across clients
- IoT sensor networks with different hardware capabilities
- Any federated learning with stateful neurons and temporal data

## Implementation Considerations
- Requires temporal resolution adaptation layer during aggregation
- Works with SNNs and broader class of stateful-neuron networks
- Clients maintain independent temporal resolution settings
- Global model must support parameter mapping across resolutions

## Activation
federated SNN, temporal resolution mismatch, heterogeneous edge, stateful neuron FL, federated averaging SNN
