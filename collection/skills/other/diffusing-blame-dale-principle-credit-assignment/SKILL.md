---
name: diffusing-blame-dale-principle-credit-assignment
description: Error Diffusion (ED) methodology for biologically plausible credit assignment under Dale's principle. Dual-stream excitatory/inhibitory architecture with modulo error routing. Achieves 96.7% MNIST and 61.7% CIFAR-10 under strict Dale's constraint. Integrates with PPO for RL. Trigger words: Dale's principle, error diffusion, excitatory-inhibitory, biologically plausible learning, credit assignment, dual-stream network.
---

# Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**arXiv**: 2606.31700v1 | **Date**: 2026-06-30 | **Venue**: ALIFE2026  
**Authors**: Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, Sebastian Risi, David Ha, Robert Tjarko Lange

## Core Methodology

### Problem Statement
Biological neural circuits obey **Dale's principle**: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks respecting this constraint must coordinate separate E/I populations, fundamentally changing credit assignment. Previous biologically plausible rules struggle to scale beyond MNIST under strict Dale's constraint.

### Error Diffusion (ED) Framework
- **Dual-stream architecture**: Separate excitatory and inhibitory populations
- **Global error routing**: Error signals routed to all layers without:
  - Transporting transposed forward weights (no weight transport)
  - Random feedback matrices
- **Modulo error routing**: Extension enabling multi-class classification (beyond binary)

### Three Domain-Specific Innovations
1. **Layer-specific sigmoid widths** — adaptive gain per layer
2. **Batch-centered class error signals** — normalized error propagation
3. **Asymmetric initialization** — E/I balance-aware weight init

## Key Results

| Benchmark | Accuracy | Notes |
|-----------|----------|-------|
| MNIST | 96.7% | State-of-the-art under strict Dale's principle |
| CIFAR-10 | 61.7% | First strong baseline under Dale's constraint |
| Brax (RL) | Competitive | ED-PPO vs Direct Feedback Alignment |
| Craftax | Competitive | Open-ended exploration task |

## Critical Findings

### Task-Dependent Credit Assignment
- Ablation analysis reveals **reversal of innovation importance** between MNIST and CIFAR-10
- Exposes **task-dependent bottlenecks** invisible to single-benchmark evaluation
- Implication: Multi-benchmark evaluation essential for biologically plausible learning research

### RL Integration
- ED + PPO achieves competitive performance
- Demonstrates scalability to continuous control
- Benchmark: Direct Feedback Alignment (backprop-free baseline)

## Pitfalls & Considerations

1. **CIFAR-10 gap**: 61.7% is baseline, not SOTA — representation learning possible but limited
2. **Dale's constraint cost**: Significant performance drop vs unconstrained networks
3. **Innovation interaction effects**: Layer-specific gains + asymmetric init interact non-trivially
4. **RL scaling**: Craftax results preliminary; full RL benchmark suite needed

## Related Work
- Direct Feedback Alignment (Lillicrap et al.)
- Target Propagation
- Feedback Alignment family
- Predictive Coding networks

## Activation Keywords
Dale's principle, error diffusion, excitatory-inhibitory, dual-stream, biologically plausible learning, credit assignment, modulo error routing, PPO integration
