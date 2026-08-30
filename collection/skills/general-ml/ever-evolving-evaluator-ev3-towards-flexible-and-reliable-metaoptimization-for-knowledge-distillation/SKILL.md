# Ever Evolving Evaluator (EV3): Towards Flexible and Reliable Meta-Optimization for Knowledge Distillation

**arXiv ID:** 2310.18893
**Authors:** Li Ding, Masrour Zoghi, Guy Tennenholtz, Maryam Karimzadehgan
**Published:** 2023-10-29T04:00:33Z
**Abstract:**
We introduce EV3, a novel meta-optimization framework designed to efficiently train scalable machine learning models through an intuitive explore-assess-adapt protocol. In each iteration of EV3, we explore various model parameter updates, assess them using pertinent evaluation methods, and then adapt the model based on the optimal updates and previous progress history. EV3 offers substantial flexibility without imposing stringent constraints like differentiability on the key objectives relevant to the tasks of interest, allowing for exploratory updates with intentionally-biased gradients and through a diversity of losses and optimizers. Additionally, the assessment phase provides reliable safety controls to ensure robust generalization, and can dynamically prioritize tasks in scenarios with multiple objectives. With inspiration drawn from evolutionary algorithms, meta-learning, and neural architecture search, we investigate an application of EV3 to knowledge distillation. Our experimental results illustrate EV3's capability to safely explore the modeling landscape, while hinting at its potential applicability across numerous domains due to its inherent flexibility and adaptability. Finally, we provide a JAX implementation of EV3, along with source code for experiments, available at: https://github.com/google-research/google-research/tree/master/ev3.

## Skill Description

This skill is generated from the arXiv paper: Ever Evolving Evaluator (EV3): Towards Flexible and Reliable Meta-Optimization for Knowledge Distillation (2310.18893).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2310.18893](http://arxiv.org/abs/2310.18893v2)
