# LLM-Guided Evolutionary Program Synthesis for Quasi-Monte Carlo Design

**arXiv ID:** 2510.03650
**Authors:** Amir Sadikov
**Published:** 2025-10-04T03:32:41Z
**Abstract:**
Low-discrepancy point sets and digital sequences underpin quasi-Monte Carlo (QMC) methods for high-dimensional integration. We cast two long-standing QMC design problems as program synthesis and solve them with an LLM-guided evolutionary loop that mutates and selects code under task-specific fitness: (i) constructing finite 2D/3D point sets with low star discrepancy, and (ii) choosing Sobol' direction numbers that minimize randomized QMC error on downstream integrands. Our two-phase procedure combines constructive code proposals with iterative numerical refinement. On finite sets, we rediscover known optima in small 2D cases and set new best-known 2D benchmarks for N >= 40, while matching most known 3D optima up to the proven frontier (N <= 8) and reporting improved 3D benchmarks beyond. On digital sequences, evolving Sobol' parameters yields consistent reductions in randomized quasi-Monte Carlo (rQMC) mean-squared error for several 32-dimensional option-pricing tasks relative to widely used Joe--Kuo parameters, while preserving extensibility to any sample size and compatibility with standard randomizations. Taken together, the results demonstrate that LLM-driven evolutionary program synthesis can automate the discovery of high-quality QMC constructions, recovering classical designs where they are optimal and improving them where finite-N structure matters. Data and code are available at https://github.com/hockeyguy123/openevolve-star-discrepancy.git.

## Skill Description

This skill is generated from the arXiv paper: LLM-Guided Evolutionary Program Synthesis for Quasi-Monte Carlo Design (2510.03650).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2510.03650](http://arxiv.org/abs/2510.03650v1)
