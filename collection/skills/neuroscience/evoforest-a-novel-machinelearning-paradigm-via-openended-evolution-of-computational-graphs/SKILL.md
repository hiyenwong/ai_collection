# EvoForest: A Novel Machine-Learning Paradigm via Open-Ended Evolution of Computational Graphs

**arXiv ID:** 2604.19761
**Authors:** Kamer Ali Yuksel, Hassan Sawaf
**Published:** 2026-03-26T00:07:45Z
**Abstract:**
Modern machine learning is still largely organized around a single recipe: choose a parameterized model family and optimize its weights. Although highly successful, this paradigm is too narrow for many structured prediction problems, where the main bottleneck is not parameter fitting but discovering what should be computed from the data. Success often depends on identifying the right transformations, statistics, invariances, interaction structures, temporal summaries, gates, or nonlinear compositions, especially when objectives are non-differentiable, evaluation is cross-validation-based, interpretability matters, or continual adaptation is required. We present EvoForest, a hybrid neuro-symbolic system for end-to-end open-ended evolution of computation. Rather than merely generating features, EvoForest jointly evolves reusable computational structure, callable function families, and trainable low-dimensional continuous components inside a shared directed acyclic graph. Intermediate nodes store alternative implementations, callable nodes encode reusable transformation families such as projections, gates, and activations, output nodes define candidate predictive computations, and persistent global parameters can be refined by gradient descent. For each graph configuration, EvoForest evaluates the discovered computation and uses a lightweight Ridge-based readout to score the resulting representation against a non-differentiable cross-validation target. The evaluator also produces structured feedback that guides future LLM-driven mutations. In the 2025 ADIA Lab Structural Break Challenge, EvoForest reached 94.13% ROC-AUC after 600 evolution steps, exceeding the publicly reported winning score of 90.14% under the same evaluation protocol.

## Skill Description

This skill is generated from the arXiv paper: EvoForest: A Novel Machine-Learning Paradigm via Open-Ended Evolution of Computational Graphs (2604.19761).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.19761](http://arxiv.org/abs/2604.19761v1)
