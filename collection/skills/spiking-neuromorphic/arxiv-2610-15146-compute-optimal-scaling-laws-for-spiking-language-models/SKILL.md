---
name: arxiv-2610-15146-compute-optimal-scaling-laws-for-spiking-language-models
description: 'Compute-Optimal Scaling Laws for Spiking Language Models (arXiv: 2610.15146)'
metadata:
  {
    "arxiv_id": "2610.15146",
    "utility": 0.96,
    "title": "Compute-Optimal Scaling Laws for Spiking Language Models",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.15146"
  }
---

# Compute-Optimal Scaling Laws for Spiking Language Models

**arXiv ID:** 2610.15146
**URL:** https://arxiv.org/abs/2610.15146
**Utility Score:** 0.96

## Abstract

Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N_{opt} \propto C^{0.56}$, close to the 0.50 that Hoffmann et al. report for dense Transformers, so spiking does not change how parameters and data should be traded off under a compute budget. Second, against non-spiking RWKV and Transformer baselines trained the same way, the loss gap splits into a backbone cost of about 0.16 nats that does not change with compute and a spiking cost that falls from 0.34 to about 0.23 nats and then levels off. These results give the first compute-optimal recipe for spiking language models and quantify the accuracy cost of their sparsity.

## Key Topics

neural, spiking, scaling law, efficient

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.15146
