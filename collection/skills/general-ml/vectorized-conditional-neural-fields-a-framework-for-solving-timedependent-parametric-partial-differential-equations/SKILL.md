# Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations

**arXiv ID:** 2406.03919
**Authors:** Jan Hagnberger, Marimuthu Kalimuthu, Daniel Musekamp, Mathias Niepert
**Published:** 2024-06-06T10:02:06Z
**Abstract:**
Transformer models are increasingly used for solving Partial Differential Equations (PDEs). Several adaptations have been proposed, all of which suffer from the typical problems of Transformers, such as quadratic memory and time complexity. Furthermore, all prevalent architectures for PDE solving lack at least one of several desirable properties of an ideal surrogate model, such as (i) generalization to PDE parameters not seen during training, (ii) spatial and temporal zero-shot super-resolution, (iii) continuous temporal extrapolation, (iv) support for 1D, 2D, and 3D PDEs, and (v) efficient inference for longer temporal rollouts. To address these limitations, we propose Vectorized Conditional Neural Fields (VCNeFs), which represent the solution of time-dependent PDEs as neural fields. Contrary to prior methods, however, VCNeFs compute, for a set of multiple spatio-temporal query points, their solutions in parallel and model their dependencies through attention mechanisms. Moreover, VCNeF can condition the neural field on both the initial conditions and the parameters of the PDEs. An extensive set of experiments demonstrates that VCNeFs are competitive with and often outperform existing ML-based surrogate models.

## Skill Description

This skill is generated from the arXiv paper: Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations (2406.03919).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2406.03919](http://arxiv.org/abs/2406.03919v2)
