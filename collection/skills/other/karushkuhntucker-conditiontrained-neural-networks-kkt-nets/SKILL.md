# Karush-Kuhn-Tucker Condition-Trained Neural Networks (KKT Nets)

**arXiv ID:** 2410.15973
**Authors:** Shreya Arvind, Rishabh Pomaje, Rajshekhar V Bhat
**Published:** 2024-10-21T12:59:58Z
**Abstract:**
This paper presents a novel approach to solving convex optimization problems by leveraging the fact that, under certain regularity conditions, any set of primal or dual variables satisfying the Karush-Kuhn-Tucker (KKT) conditions is necessary and sufficient for optimality. Similar to Theory-Trained Neural Networks (TTNNs), the parameters of the convex optimization problem are input to the neural network, and the expected outputs are the optimal primal and dual variables. A choice for the loss function in this case is a loss, which we refer to as the KKT Loss, that measures how well the network's outputs satisfy the KKT conditions. We demonstrate the effectiveness of this approach using a linear program as an example. For this problem, we observe that minimizing the KKT Loss alone outperforms training the network with a weighted sum of the KKT Loss and a Data Loss (the mean-squared error between the ground truth optimal solutions and the network's output). Moreover, minimizing only the Data Loss yields inferior results compared to those obtained by minimizing the KKT Loss. While the approach is promising, the obtained primal and dual solutions are not sufficiently close to the ground truth optimal solutions. In the future, we aim to develop improved models to obtain solutions closer to the ground truth and extend the approach to other problem classes.

## Skill Description

This skill is generated from the arXiv paper: Karush-Kuhn-Tucker Condition-Trained Neural Networks (KKT Nets) (2410.15973).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2410.15973](http://arxiv.org/abs/2410.15973v1)
