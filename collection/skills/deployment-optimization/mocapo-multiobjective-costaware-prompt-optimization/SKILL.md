# MO-CAPO: Multi-Objective Cost-Aware Prompt Optimization

**arXiv ID:** 2605.18869
**Authors:** Jan Büssing, Moritz Schlager, Timo Heiß, Tom Zehle, Matthias Feurer
**Published:** 2026-05-15T14:56:27Z
**Abstract:**
Large language models (LLMs) achieve strong performance across a wide range of tasks but are highly sensitive to prompt design, motivating the need for automatic prompt optimization. Existing methods predominantly focus on performance alone, ignoring competing objectives such as inference cost or latency. At the same time, existing work on multi-objective prompt optimization relies on off-the-shelf NSGA-II, ignoring optimization efficiency. As a remedy, we introduce MO-CAPO, a novel multi-objective prompt optimization algorithm that jointly optimizes performance and inference cost while leveraging budget allocation for cost-efficient optimization. We further propose a deployment-oriented cost objective that captures the full computational profile of LLM inference. We evaluate our approach across four tasks and three LLMs and compare it to an NSGA-II-based multi-objective method and state-of-the-art single-objective prompt optimizers. Results show that MO-CAPO consistently identifies strong, robust, and diverse Pareto front approximations while maintaining cost-efficiency. It outperforms the NSGA-II baseline on 8 out of 12 cases in terms of the noisy R2 metric and achieves competitive performances often already at a considerably lower budget. The discovered solution sets span diverse performance-cost trade-offs that are omitted by single-objective optimizers, yet the top-performance candidates remain competitive with single-objective solutions. Additionally, we conduct the first evaluation of multi-objective machine learning experiments that considers generalization and robustness through noisy R2 and approximation gap, enabling a more realistic assessment of solution quality. MO-CAPO enables practitioners to select from an efficiently discovered set of multiple prompts offering different trade-offs between performance and cost.

## Skill Description

This skill is generated from the arXiv paper: MO-CAPO: Multi-Objective Cost-Aware Prompt Optimization (2605.18869).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.18869](http://arxiv.org/abs/2605.18869v1)
