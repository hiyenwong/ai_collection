---
name: qml-expressivity-trainability-paradox
description: Dynamical Lie Algebra framework for understanding and navigating the expressivity-trainability paradox in Quantum Machine Learning. Shows unstructured QML suffers quantum underfitting from barren plateaus. Symmetry-preserving structural regularization guarantees scalable gradient-rich landscapes. Trainability-by-Design approach.
version: 1.0.0
tags: [quantum, machine-learning, barren-plateau, dynamical-lie-algebra, trainability, expressivity]
source: arXiv:2606.31536
authors: [Kung-Ming Lan, Edward Huang]
published: 2026-06-30
trigger_words: [QML expressivity trainability paradox, barren plateau DLA, dynamical lie algebra quantum, trainability by design, quantum underfitting, symmetry-preserving QML]
---

# QML Expressivity-Trainability Paradox via DLA

## Core Insight

QML suffers from a **expressivity-trainability paradox**: the vast Hilbert space capacity of PQCs is the direct mathematical cause of Barren Plateaus. Unstructured QML architectures suffer from quantum underfitting, not overfitting.

## Key Findings

### 1. The Paradox
- Classical deep learning: increasing capacity risks overfitting
- Quantum ML: increasing capacity causes barren plateaus (quantum underfitting)
- The vast Hilbert space = the problem, not the solution

### 2. DLA Framework
- Links circuit generator algebraic dimension to optimization dynamics
- Exponential DLA growth = exponentially flat gradients
- Polynomial DLA growth = trainable landscapes

### 3. Trainability-by-Design
- Embed group-theoretic geometric priors as structural regularizers
- Restrict DLA growth to polynomial regime
- Sacrifice raw memorization capacity for scalable, gradient-rich landscapes

## Implementation Pattern

1. Analyze your PQC's DLA dimension
2. If DLA grows exponentially with qubit count, expect barren plateaus
3. Identify symmetries in your problem domain
4. Embed symmetry-preserving constraints into circuit architecture
5. Verify DLA growth is polynomial after constraint
6. Train with guaranteed gradient-rich landscape

## Practical Applications

### Financial QML
- Stock price prediction QNNs: embed market symmetry constraints
- Portfolio optimization: embed permutation symmetries
- Avoid barren plateaus by design, not by luck

### General QML
- Any QML task where circuit depth/qubit count scales
- Design circuits with built-in trainability guarantees
- Replace heuristic ansatz design with principled DLA analysis

## Activation

Use when:
- Designing QML architectures and worried about barren plateaus
- Analyzing why a QNN fails to train
- Need principled ansatz design methodology
- Building scalable quantum neural networks