---
name: spike-htr-spiking-neural-transformer
description: "Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition - hybrid spiking recognizer that controls both spiking steps and sequence positions processed by deep sequence mixer. Use when working with handwritten text recognition, spiking neural networks for computer vision, or computational efficiency in SNNs."
metadata:
  arxiv_id: "2608.01646"
  authors: "Xiubo Liang, Jinxing Han, Yuke Li, Haoqi Zhu, Yu Zhao, Hongzhi Wang"
  published: "2026-08-03"
  tags: [spiking-neural-network, handwritten-text-recognition, transformer, computational-efficiency, inkcoder, ctc-guided-length-reducer]
license: Complete terms in LICENSE.txt
---

# Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition

## Overview
Spike-HTR addresses the computational imbalance in Handwritten Text Recognition (HTR) by creating a hybrid spiking recognizer that controls both the number of spiking steps and the number of width positions processed by the deep sequence mixer. This approach makes static images suitable for short-horizon spiking inference while reducing sequence computation.

## Core Components

### 1. InkCoder
- Converts static handwritten images into coarse-to-fine input streams
- Early timesteps cover broad stroke regions
- Later timesteps emphasize sharper stroke details
- Makes static images suitable for short-horizon spiking inference

### 2. CTC-Guided Length Reducer
- Keeps likely character or uncertain positions
- Compresses long blank-dominated stretches before deep mixing
- Reduces sequence computation requirements
- Works without language models or lexicons

## Key Features
- **Computational efficiency**: Addresses the mismatch between static images and temporal spiking computation
- **No external dependencies**: Trains only on target data, decodes without language models or lexicons
- **State-of-the-art performance**: Achieves CERs of 3.5/5.4, 2.3/2.5, and 4.2/3.9 on IAM, LAM, and READ2016 datasets
- **Hybrid architecture**: Combines spiking neural networks with transformer-based sequence mixing

## Datasets and Performance
- **IAM**: 3.5% validation CER, 5.4% test CER
- **LAM**: 2.3% validation CER, 2.5% test CER  
- **READ2016**: 4.2% validation CER, 3.9% test CER
- Code available at the provided repository URL

## When to Use This Skill
- Building spiking neural networks for handwritten text recognition
- Addressing computational imbalance in SNN computer vision tasks
- Converting static images to temporal spiking inputs
- Reducing sequence computation in spiking transformers
- Research on hybrid spiking-classical architectures

## Implementation Considerations
- Requires careful tuning of spiking timestep duration
- InkCoder parameters should be optimized for stroke complexity
- CTC-guided length reduction threshold affects accuracy vs. efficiency trade-off
- Can be adapted for other sequential recognition tasks beyond HTR

## Activation Keywords
- spike-htr
- spiking neural transformer
- handwritten text recognition
- inkcoder
- ctc-guided length reducer
- spiking computer vision
- computational efficiency SNN
- hybrid spiking architecture

## References
- Original paper: https://arxiv.org/abs/2608.01646
- Code repository: Available at the URL provided in the paper
- Related work on spiking neural networks and handwritten text recognition