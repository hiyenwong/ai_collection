# Implicit variance regularization in non-contrastive SSL

**arXiv ID:** 2212.04858
**Authors:** Manu Srinath Halvagal, Axel Laborieux, Friedemann Zenke
**Published:** 2022-12-09T13:56:42Z
**Abstract:**
Non-contrastive SSL methods like BYOL and SimSiam rely on asymmetric predictor networks to avoid representational collapse without negative samples. Yet, how predictor networks facilitate stable learning is not fully understood. While previous theoretical analyses assumed Euclidean losses, most practical implementations rely on cosine similarity. To gain further theoretical insight into non-contrastive SSL, we analytically study learning dynamics in conjunction with Euclidean and cosine similarity in the eigenspace of closed-form linear predictor networks. We show that both avoid collapse through implicit variance regularization albeit through different dynamical mechanisms. Moreover, we find that the eigenvalues act as effective learning rate multipliers and propose a family of isotropic loss functions (IsoLoss) that equalize convergence rates across eigenmodes. Empirically, IsoLoss speeds up the initial learning dynamics and increases robustness, thereby allowing us to dispense with the EMA target network typically used with non-contrastive methods. Our analysis sheds light on the variance regularization mechanisms of non-contrastive SSL and lays the theoretical grounds for crafting novel loss functions that shape the learning dynamics of the predictor's spectrum.

## Skill Description

This skill is generated from the arXiv paper: Implicit variance regularization in non-contrastive SSL (2212.04858).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2212.04858](http://arxiv.org/abs/2212.04858v2)
