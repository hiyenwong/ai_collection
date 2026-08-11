---
name: dual-node-dgx-spark-distributed-llm-training
title: Dual-Node NVIDIA DGX Spark Distributed LLM Training
version: 1.0
description: Dual-node DGX Spark LLM training over Tailscale.
---

# Dual-Node NVIDIA DGX Spark Distributed LLM Training

## Overview
This skill provides a methodology for deploying distributed LLM training across two NVIDIA DGX Spark systems, each with GB10 Grace Blackwell SoC and 128GB unified memory, administered remotely over Tailscale mesh VPN with dedicated 200 Gb/s QSFP56 direct fiber link.

## Core Methodology

### Hardware Setup
- **Systems**: Two NVIDIA DGX Spark systems
- **GPU**: GB10 Grace Blackwell SoC per node
- **Memory**: 128 GB unified memory per node
- **Network**: 
  - Tailscale mesh VPN for remote administration
  - Dedicated 200 Gb/s QSFP56 direct fiber link for training communication

### Software Configuration
- **Framework**: PyTorch with torchrun, DDP, and NCCL
- **Process Configuration**: One process per node
- **Model**: Depth-20 NanoChat model
- **Batch Configuration**:
  - Local batch size: 32 per node
  - Context length: 2,048 tokens
  - Global batch: 131,072 tokens per step

### Performance Metrics
- **Step time**: ~69.4 seconds
- **Throughput**: ~1,890 tokens/second
- **Total processed**: ~653 million tokens over 4 days

### Key Implementation Steps

1. **Link Configuration**: Set up dedicated 200 Gb/s QSFP56 direct fiber link
2. **Container Setup**: Configure Docker containers with appropriate CUDA drivers
3. **Interface Binding**: Bind NCCL to the correct network interfaces
4. **Troubleshooting**: Address step-zero evaluation bugs that trigger NCCL timeouts
5. **Checkpointing**: Implement proper checkpointing for fault tolerance

### Cybersecurity Fine-Tuning Extension
- **Dataset**: 77 CISA advisories (338 training, 37 validation conversations)
- **Evaluation**: 17-question held-out evaluation with Ollama-hosted LLM judge
- **Results**: CTI-specific categories improved while general-knowledge categories regressed (2.06 → 2.29 on 0-10 scale)

## Pitfalls and Solutions

### Common Issues
- **NCCL Timeouts**: Caused by step-zero evaluation bugs; resolve by proper interface binding
- **Network Configuration**: Ensure Tailscale doesn't interfere with direct fiber link
- **Memory Management**: Monitor unified memory usage across both CPU and GPU

### Best Practices
- **Reproducibility**: Document all configuration steps in a runbook
- **Educational Use**: Same cluster can support AI courses and cybersecurity query engines
- **Feasibility Focus**: Establish feasibility rather than scaling-efficiency claims

## Verification Steps

1. Verify network connectivity between nodes via direct fiber link
2. Test single-node throughput as baseline (estimated, not measured under matched conditions)
3. Validate NCCL communication with simple distributed tensor operations
4. Run small-scale training job to verify checkpointing functionality
5. Execute cybersecurity fine-tuning evaluation pipeline

## Resources
- **Code Availability**: Deployment runbook and scripts available at GitHub repository
- **Paper**: arXiv:2608.07226 [cs.AR]
- **DOI**: https://doi.org/10.48550/arXiv.2608.07226

## Activation Keywords
distributed systems, DGX Spark, LLM training, Tailscale, NCCL, multi-node training, cybersecurity fine-tuning