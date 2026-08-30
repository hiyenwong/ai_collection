# Paradoxical noise preference in RNNs

**arXiv ID:** 2601.04539
**Authors:** Noah Eckstein, Manoj Srinivasan
**Published:** 2026-01-08T03:11:51Z
**Abstract:**
In recurrent neural networks (RNNs) used to model biological neural networks, noise is typically introduced during training to emulate biological variability and regularize learning. The expectation is that removing the noise at test time should preserve or improve performance. Contrary to this intuition, we find that continuous-time RNNs (CTRNNs) often perform best at or near the training noise level. This noise preference typically arises when noise is injected inside the neural activation function; networks trained with noise injected outside the activation function perform best with zero noise. The phenomenon arises robustly in diverse tasks for large enough training noise; we also show the phenomenon arising in feedforward neural networks, not just in RNNs. Our analyses show that the phenomenon stems from noise-induced shifts of fixed points (stationary distributions) in the underlying stochastic dynamics of the RNNs. These fixed point shifts are noise-level dependent and bias the network outputs when the noise is removed, degrading performance. Analytical and numerical results show that the bias arises when neural states operate near activation-function nonlinearities, where noise is asymmetrically attenuated, and that performance optimization incentivizes operation near these nonlinearities; such performance incentives exist for networks with noise inside, but not outside, the activation function, explaining why only noise-in networks show the preference. Thus, networks can overfit to the training noise itself rather than just to the input-output data. The phenomenon is distinct from stochastic resonance, wherein nonzero noise enhances signal processing. Our findings reveal that training noise can become an integral part of the computation learned by neural networks, with implications for understanding neural population dynamics and for the design of robust artificial RNNs.

## Skill Description

This skill is generated from the arXiv paper: Paradoxical noise preference in RNNs (2601.04539).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2601.04539](http://arxiv.org/abs/2601.04539v2)
