---
name: vqa-dynamic-portfolio-optimization
description: "VQA methodology for dynamic portfolio optimization — sampling strategies (adaptive CVaR scheduling), optimizer scheduling (PSO+NFT hybrid), and hardware-aware ansatz design (data-guided colored layout, heavy-hex deep-chain layout). Activation: vqa portfolio, dynamic portfolio optimization, CVaR scheduling, hardware-aware ansatz, heavy-hex layout, PSO optimizer, quantum portfolio, 动态投资组合优化"
metadata:
  arxiv_id: "2606.10098"
  published: "2026-06-08"
  categories: "cs.CE, quant-ph"
---

# VQA Dynamic Portfolio Optimization

## Description

Hardware-aware Variational Quantum Algorithm (VQA) methodology for multi-period dynamic portfolio optimization, covering sampling strategy selection, optimizer scheduling, and qubit layout design for NISQ processors.

## Core Methodology

### Adaptive CVaR Scheduling
Gradually tighten the sampled tail used for optimization: start with broader CVaR percentile (exploration), progressively focus on tail risk (exploitation). Prevents premature convergence to suboptimal portfolios.

### Two-Stage Optimizer
- **Stage 1**: Particle Swarm Optimization (PSO) for global exploration across parameter landscape
- **Stage 2**: Nakanishi-Fujii-Todo (NFT) optimizer for local refinement with gradient-free precision

### Hardware-Aware Ansatz Layout

**Data-Guided Colored Layout**:
- Map correlated asset variables to qubits connected by native entangling gates
- Use asset correlation matrix to inform qubit assignment
- Reduces SWAP gate overhead during transpilation

**Heavy-Hex Deep-Chain Layout**:
- Designed specifically for IBM heavy-hex topology
- Increases native two-qubit interaction depth without additional routing
- Best final objective value and CVaR-tail performance among tested layouts on ibm_quebec QPU

## Key Findings

- Sampling strategy, optimizer scheduling, and hardware-aware layout design **materially affect** VQA performance
- No quantum advantage observed over state-of-the-art classical solver on tested instances
- Heavy-hex-native deep-chain layout outperforms standard layouts on real QPU
- Tested on 150-qubit dynamic portfolio instance balancing return, risk, transaction costs, and cash-interest effects

## Implementation Steps

1. **Formulate QUBO**: Encode multi-period portfolio optimization (return, risk, transaction costs, cash-interest, constraints)
2. **Design Ansatz**: Choose hardware-aware layout (colored or heavy-hex deep-chain)
3. **Set CVaR Schedule**: Adaptive tightening from ~50th to ~10th percentile
4. **Train Stage 1**: PSO with broad parameter ranges
5. **Train Stage 2**: NFT optimizer with refined starting point
6. **Evaluate**: Compare on QPU vs classical solver baseline

## Pitfalls

- **No quantum advantage yet**: Classical exact solvers still outperform on tested instances
- **150-qubit scale**: Results may not extrapolate to larger portfolios
- **Heavy-hex topology specific**: Layout optimization is processor-specific
- **Simulator → QPU gap**: Simulator-selected configurations may not transfer directly to hardware

## Activation Keywords
- vqa portfolio optimization
- dynamic portfolio quantum
- CVaR adaptive scheduling
- hardware-aware ansatz
- heavy-hex layout
- PSO NFT optimizer
- quantum portfolio multi-period
- VQA动态投资组合
- 量子CVaR优化
