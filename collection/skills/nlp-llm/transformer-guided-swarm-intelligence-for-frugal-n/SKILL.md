---
name: transformer-guided-swarm-intelligence-for-frugal-n
description: Skill derived from arXiv paper 2607.11826: Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search
category: nlp-llm
created: 2026-07-23
arxiv_id: 2607.11826
utility: 0.87
---
# transformer-guided-swarm-intelligence-for-frugal-n

Derived from arXiv paper [2607.11826]: Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search

## Abstract
Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller, trained via Reinforcement Learning (RL), with the local micro-exploitation of an Artificial Bee Colony (ABC) algorithm. To prevent premature convergence during the RL phase, we introduce a dynamic entropy mechanism that forces topological exploration upon detection of performance stagnation. Evaluated on a standard GPU (NVIDIA RTX 3060), our hybrid method effectively resolves the "cold-start" problem inherent in metaheuristics. By algorithmically penalizing network depth, our framework actively mitigates model bloat: on the CIFAR-10 dataset, it discovers an efficient architecture reaching 84.85% accuracy with only $\sim$174,000 parameters (significantly smaller than standard baselines like ResNet-20) in 3 hours of search time. Furthermore, we demonstrate the framework's flexibility by applying it to credit card fraud detection, directly optimizing the F1-Score on highly imbalanced tabular data to reach a F1-Score of 0.71 with a compact network of $\sim$4,600 parameters. These results suggest that our approach can yield tailored, accessible, and highly parameter-efficient deep learning models suitable for edge deployment.

## Authors
Romain Amigon

## Published
2026-07-13

## Categories
cs.LG, cs.AI, cs.NE

## Utility
0.87

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
