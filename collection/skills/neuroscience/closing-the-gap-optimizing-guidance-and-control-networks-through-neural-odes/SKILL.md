# Closing the gap: Optimizing Guidance and Control Networks through Neural ODEs

**arXiv ID:** 2404.16908
**Authors:** Sebastien Origer, Dario Izzo
**Published:** 2024-04-25T13:14:32Z
**Abstract:**
We improve the accuracy of Guidance & Control Networks (G&CNETs), trained to represent the optimal control policies of a time-optimal transfer and a mass-optimal landing, respectively. In both cases we leverage the dynamics of the spacecraft, described by Ordinary Differential Equations which incorporate a neural network on their right-hand side (Neural ODEs). Since the neural dynamics is differentiable, the ODEs sensitivities to the network parameters can be computed using the variational equations, thereby allowing to update the G&CNET parameters based on the observed dynamics. We start with a straightforward regression task, training the G&CNETs on datasets of optimal trajectories using behavioural cloning. These networks are then refined using the Neural ODE sensitivities by minimizing the error between the final states and the target states. We demonstrate that for the orbital transfer, the final error to the target can be reduced by 99% on a single trajectory and by 70% on a batch of 500 trajectories. For the landing problem the reduction in error is around 98-99% (position) and 40-44% (velocity). This step significantly enhances the accuracy of G&CNETs, which instills greater confidence in their reliability for operational use. We also compare our results to the popular Dataset Aggregation method (DaGGER) and allude to the strengths and weaknesses of both methods.

## Skill Description

This skill is generated from the arXiv paper: Closing the gap: Optimizing Guidance and Control Networks through Neural ODEs (2404.16908).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2404.16908](http://arxiv.org/abs/2404.16908v1)
