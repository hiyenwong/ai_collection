---
name: mzeqas-zero-shot-quantum-nas
description: "Zero-shot quantum neural architecture search methodology using QNTK convergence and MCTS for VQA circuit design. Eliminates repeated training costs. Activation: quantum NAS, neural architecture search, zero-shot, VQA, MCTS, 量子架构搜索."
---

# MZeQAS: Zero-Shot Quantum Neural Architecture Search

Zero-shot quantum neural architecture search (QNAS) methodology from arXiv:2605.27410 (May 2026). Uses Quantum Neural Tangent Kernel (QNTK) Gram matrix convergence to build surrogate models for estimating quantum circuit performance without full training, dramatically accelerating VQA architecture search on NISQ devices.

## Core Methodology

### Problem

Variational Quantum Algorithms (VQAs) require hand-designed circuit architectures balancing expressivity, trainability, and hardware constraints. Evolutionary-based QNAS methods repeatedly train each candidate circuit, making search computationally prohibitive.

### Key Insight

The Gram matrix of the Quantum Neural Tangent Kernel (QNTK) converges in certain settings, enabling a **zero-shot surrogate model** that estimates candidate circuit performance without training.

### MZeQAS Framework

1. **QNTK Convergence Analysis**: Identify conditions where QNTK Gram matrix converges for parameterized quantum circuits
2. **Zero-Shot Surrogate**: Build proxy model estimating candidate VQA performance from architecture features alone
3. **MCTS-Guided Search**: Monte Carlo Tree Search explores architecture space guided by surrogate predictions
4. **Efficient Discovery**: Discovers high-performing architectures with orders-of-magnitude fewer evaluations

## Numbered Steps

1. **Define architecture space**: Parameterize quantum circuit search space (gate types, connectivity, depth)
2. **Compute QNTK Gram matrix**: For each candidate architecture, compute the quantum neural tangent kernel Gram matrix
3. **Build zero-shot proxy**: Map architecture features → predicted performance using QNTK convergence properties
4. **Initialize MCTS**: Set up Monte Carlo Tree Search with surrogate as rollout policy
5. **Explore architectures**: MCTS balances exploration (unseen architectures) vs exploitation (high-scoring proxies)
6. **Validate top candidates**: Train only the best-discovered architectures to confirm surrogate predictions
7. **Deploy optimal circuit**: Use validated architecture for target VQA task

## Pitfalls

- **QNTK convergence conditions**: Not all circuit architectures satisfy convergence — must verify before building surrogate
- **NISQ hardware constraints**: Discovered architectures must respect qubit connectivity and gate fidelity limits
- **Surrogate accuracy**: Zero-shot estimates have error bars; always validate top candidates with actual training
- **Search space size**: Too large → MCTS explores poorly. Too small → misses optimal architectures. Calibrate carefully.

## Verification

- MZeQAS outperforms existing evolutionary QNAS in both search efficiency and solution quality
- Surrogate predictions correlate strongly with actual VQA performance (paper validates on benchmark tasks)
- Reduces training evaluations by eliminating full training of every candidate circuit

## When to Use

- Designing VQA circuits for NISQ devices
- Quantum architecture search where training cost is prohibitive
- Balancing expressivity vs trainability in quantum circuits
- Any VQAs task requiring automated circuit architecture selection
