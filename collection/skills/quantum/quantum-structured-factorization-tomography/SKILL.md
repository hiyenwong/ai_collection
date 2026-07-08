---
name: quantum-structured-factorization-tomography
description: Unified structured factorization framework for quantum state tomography using Burer-Monteiro-type factorization parametrizing density matrix as FF†, guaranteeing physical validity while incorporating structural priors.
category: quantum
created: 2026-07-06
source: arXiv:2607.01608
---

# Structured Factorization Approaches for Quantum State Tomography

## Source

arXiv:2607.01608 - "Structured Factorization Approaches for Quantum State Tomography" by Zhen Qin, Joseph M. Lukens, Brian T. Kirby, Zhihui Zhu (2026-07-02)

## Overview

Since quantum state tomography (QST) complexity scales exponentially with system size, exploiting priors such as low-rankness, tensor-network structures, and neural-network representations is essential for scalable QST.

## Core Methodology

1. **Burer-Monteory Factorization**: Parametrize the density matrix as FF† where factor F is constrained to belong to a structured model class.

2. **Physical Validity by Construction**: This factorization guarantees physical validity by construction while allowing broad range of structural priors.

3. **Structured Model Classes**: Range from generic Cholesky decomposition to low-rank matrices, matrix product states, tensor train formats, and neural network representations.

4. **Unified Framework**: Provides single framework encompassing multiple approaches to scalable QST.

## Key Findings

- Exponential complexity of QST → need for structural priors
- FF† factorization guarantees positive semidefinite density matrices
- Framework unifies low-rank, tensor network, and neural network approaches
- Enables scalable tomography in terms of both sample and parameter complexity

## Applications

- Quantum state characterization in experiments
- Quantum device benchmarking
- Quantum error correction syndrome analysis
- Quantum sensing and metrology
- Quantum machine learning state preparation

## Trigger Words

quantum state tomography, structured factorization, Burer-Monteiro, density matrix, low-rank, tensor network, neural network representation, sample complexity

## Activation

When:
- Performing quantum state tomography
- Designing scalable quantum characterization protocols
- Working with low-rank quantum state estimation
- Using tensor network representations for quantum states
- Optimizing measurement settings for quantum state reconstruction