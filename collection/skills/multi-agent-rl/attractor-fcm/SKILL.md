# Attractor FCM

**arXiv ID:** 2604.27947
**Authors:** Alexis Kafantaris
**Published:** 2026-04-30T14:44:47Z
**Abstract:**
In this paper an attractor FCM is created, tested, and analyzed. This FCM is neither a hebbian based nor agentic, nor a hybrid; it rather is a gradient descent based, physics constrained, Jacobian version of an FCM. Moreover, this model has several quirks; it uses residual memory, back propagation through time, and a fixed point anchor that is recursively implemented to update its weights. The residuals update the recursive part without losing the system memory. The model's anchor enables it to converge in a fixed point for which back propagation through time unrolls it and ensures that the error minimization is for an accurate gradient. Furthermore, a new learning algorithm is utilized. The Newton's method finds the system's fixed point attractor and then gradient descend is adaptively changing the landscape; an adaptive term is used to directly manipulate the weights through the attractor dynamics. As the adaptive term changes, the descent through the landscape is constantly adjusting according to sigmoid saturation, and that prevents premature convergence to a local minimum. Lastly, the updates are filtered by causal mask that informs the network about the physics, respecting the initial expert based opinions, for which model reduces the error to the target in an efficient way.

## Skill Description

This skill is generated from the arXiv paper: Attractor FCM (2604.27947).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.27947](http://arxiv.org/abs/2604.27947v2)
