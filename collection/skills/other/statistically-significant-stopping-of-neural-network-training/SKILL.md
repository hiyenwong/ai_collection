# Statistically Significant Stopping of Neural Network Training

**arXiv ID:** 2103.01205
**Authors:** J. K. Terry, Mario Jayakumar, Kusal De Alwis
**Published:** 2021-03-01T18:51:16Z
**Abstract:**
The general approach taken when training deep learning classifiers is to save the parameters after every few iterations, train until either a human observer or a simple metric-based heuristic decides the network isn't learning anymore, and then backtrack and pick the saved parameters with the best validation accuracy. Simple methods are used to determine if a neural network isn't learning anymore because, as long as it's well after the optimal values are found, the condition doesn't impact the final accuracy of the model. However from a runtime perspective, this is of great significance to the many cases where numerous neural networks are trained simultaneously (e.g. hyper-parameter tuning). Motivated by this, we introduce a statistical significance test to determine if a neural network has stopped learning. This stopping criterion appears to represent a happy medium compared to other popular stopping criterions, achieving comparable accuracy to the criterions that achieve the highest final accuracies in 77% or fewer epochs, while the criterions which stop sooner do so with an appreciable loss to final accuracy. Additionally, we use this as the basis of a new learning rate scheduler, removing the need to manually choose learning rate schedules and acting as a quasi-line search, achieving superior or comparable empirical performance to existing methods.

## Skill Description

This skill is generated from the arXiv paper: Statistically Significant Stopping of Neural Network Training (2103.01205).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2103.01205](http://arxiv.org/abs/2103.01205v3)
