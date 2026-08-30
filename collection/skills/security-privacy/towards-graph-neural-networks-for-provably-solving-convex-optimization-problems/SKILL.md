# Towards graph neural networks for provably solving convex optimization problems

**arXiv ID:** 2502.02446
**Authors:** Chendi Qian, Christopher Morris
**Published:** 2025-02-04T16:11:41Z
**Abstract:**
Recently, message-passing graph neural networks (MPNNs) have shown potential for solving combinatorial and continuous optimization problems due to their ability to capture variable-constraint interactions. While existing approaches leverage MPNNs to approximate solutions or warm-start traditional solvers, they often lack guarantees for feasibility, particularly in convex optimization settings. Here, we propose an iterative MPNN framework to solve convex optimization problems with provable feasibility guarantees. First, we demonstrate that MPNNs can provably simulate standard interior-point methods for solving quadratic problems with linear constraints, covering relevant problems such as SVMs. Secondly, to ensure feasibility, we introduce a variant that starts from a feasible point and iteratively restricts the search within the feasible region. Experimental results show that our approach outperforms existing neural baselines in solution quality and feasibility, generalizes well to unseen problem sizes, and, in some cases, achieves faster solution times than state-of-the-art solvers such as Gurobi.

## Skill Description

This skill is generated from the arXiv paper: Towards graph neural networks for provably solving convex optimization problems (2502.02446).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2502.02446](http://arxiv.org/abs/2502.02446v1)
