---
name: quantum-fourier-generative-models
description: "Quantum Fourier generative models trainable at large scale. Parallel Fourier feature maps + forrelation circuits for training quantum generative models on 1000+ qubits with classical train-on-deploy-on-quantum approach. arXiv: 2606.28483"
---

# Quantum Fourier Generative Models

Methodology from arXiv:2606.28483 — Quantum Fourier Generative Models Trainable at Large Scale.

## Core Innovation

A framework for building and training quantum generative models for multivariate probability distributions using parallel Fourier feature maps combined with forrelation-type quantum circuits. Enables training at 1000+ qubits on a single GPU.

## Key Technical Components

1. **Parallel Fourier Feature Maps**: Embed continuous-valued variables into quantum state space using parallel Fourier representations
2. **Forrelation-Type Quantum Circuits**: Tuning Fourier coefficients of the quantum model through specialized circuit structure
3. **Log-Likelihood Training Strategy**: Uses unbiased Monte Carlo estimator based on Parseval's identity — goes beyond matching low frequency moments (unlike MMD loss)
4. **Train-on-Classical, Deploy-on-Quantum**: Efficient classical training, then inverse QFT maps model to sampling circuit in computational basis
5. **Multi-Modal Preservation**: Avoids oversmoothing, preserves multi-modal structure of target distributions

## Training Pipeline

```
1. Encode continuous variables via parallel Fourier feature maps
2. Build forrelation-type quantum circuit for Fourier coefficient tuning
3. Train classically using log-likelihood loss (Parseval-based Monte Carlo estimator)
4. Apply inverse QFT to map to computational basis sampling circuit
5. Deploy on quantum hardware for fast sampling (~300μs per sample)
```

## Advantages Over Prior Work

- MMD-loss IQP models show poor performance on non-trivial structures
- Normalizing flow and diffusion baselines tend to oversmooth
- Fourier approach preserves multi-modal structure
- Scales to 1000+ qubits on single GPU

## Hardware Validation

Successfully deployed on superconducting quantum devices with per-sample execution times of approximately 300μs.

## When to Use

- Quantum generative modeling for continuous probability distributions
- Large-scale quantum circuits (100+ qubits)
- Multi-modal distribution modeling
- Train-on-classical deploy-on-quantum workflows

## Activation Keywords

quantum generative model, Fourier feature map, forrelation, quantum circuit, log-likelihood training, quantum sampling, amplitude amplification, quantum machine learning, quantum generative AI, continuous distribution

## Paper Reference

- **Title**: Quantum Fourier Generative Models Trainable at Large Scale
- **arXiv**: 2606.28483
- **Authors**: Cenk Tüysüz, Oleksandr Kyriienko, Michele Grossi
- **Date**: 2026-06-30
- **Category**: quant-ph
