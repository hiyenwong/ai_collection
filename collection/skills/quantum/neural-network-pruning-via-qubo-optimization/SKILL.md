# Neural Network Pruning via QUBO Optimization

**arXiv ID:** 2604.05856
**Authors:** Osama Orabi, Artur Zagitov, Hadi Salloum, Viktor A. Lobachev, Kasymkhan Khubiev, Yaroslav Kholodov
**Published:** 2026-04-07T13:16:40Z
**Abstract:**
Neural network pruning can be formulated as a combinatorial optimization problem, yet most existing approaches rely on greedy heuristics that ignore complex interactions between filters. Formal optimization methods such as Quadratic Unconstrained Binary Optimization (QUBO) provide a principled alternative but have so far underperformed due to oversimplified objective formulations based on metrics like the L1-norm. In this work, we propose a unified Hybrid QUBO framework that bridges heuristic importance estimation with global combinatorial optimization. Our formulation integrates gradient-aware sensitivity metrics - specifically first-order Taylor and second-order Fisher information - into the linear term, while utilizing data-driven activation similarity in the quadratic term. This allows the QUBO objective to jointly capture individual filter relevance and inter-filter functional redundancy. We further introduce a dynamic capacity-driven search to strictly enforce target sparsity without distorting the optimization landscape. Finally, we employ a two-stage pipeline featuring a Tensor-Train (TT) Refinement stage - a gradient-free optimizer that fine-tunes the QUBO-derived solution directly against the true evaluation metric. Experiments on the SIDD image denoising dataset demonstrate that the proposed Hybrid QUBO significantly outperforms both greedy Taylor pruning and traditional L1-based QUBO, with TT Refinement providing further consistent gains at appropriate combinatorial scales. This highlights the potential of hybrid combinatorial formulations for robust, scalable, and interpretable neural network compression.

## Skill Description

This skill is generated from the arXiv paper: Neural Network Pruning via QUBO Optimization (2604.05856).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.05856](http://arxiv.org/abs/2604.05856v1)
