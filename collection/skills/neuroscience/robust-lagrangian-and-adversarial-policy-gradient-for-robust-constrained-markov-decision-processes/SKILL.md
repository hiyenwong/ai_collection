# Robust Lagrangian and Adversarial Policy Gradient for Robust Constrained Markov Decision Processes

**arXiv ID:** 2308.11267
**Authors:** David M. Bossens
**Published:** 2023-08-22T08:24:45Z
**Abstract:**
The robust constrained Markov decision process (RCMDP) is a recent task-modelling framework for reinforcement learning that incorporates behavioural constraints and that provides robustness to errors in the transition dynamics model through the use of an uncertainty set. Simulating RCMDPs requires computing the worst-case dynamics based on value estimates for each state, an approach which has previously been used in the Robust Constrained Policy Gradient (RCPG). Highlighting potential downsides of RCPG such as not robustifying the full constrained objective and the lack of incremental learning, this paper introduces two algorithms, called RCPG with Robust Lagrangian and Adversarial RCPG. RCPG with Robust Lagrangian modifies RCPG by taking the worst-case dynamics based on the Lagrangian rather than either the value or the constraint. Adversarial RCPG also formulates the worst-case dynamics based on the Lagrangian but learns this directly and incrementally as an adversarial policy through gradient descent rather than indirectly and abruptly through constrained optimisation on a sorted value list. A theoretical analysis first derives the Lagrangian policy gradient for the policy optimisation of both proposed algorithms and then the adversarial policy gradient to learn the adversary for Adversarial RCPG. Empirical experiments injecting perturbations in inventory management and safe navigation tasks demonstrate the competitive performance of both algorithms compared to traditional RCPG variants as well as non-robust and non-constrained ablations. In particular, Adversarial RCPG ranks among the top two performing algorithms on all tests.

## Skill Description

This skill is generated from the arXiv paper: Robust Lagrangian and Adversarial Policy Gradient for Robust Constrained Markov Decision Processes (2308.11267).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2308.11267](http://arxiv.org/abs/2308.11267v3)
