# Optimising Communication Overhead in Federated Learning Using NSGA-II

**arXiv ID:** 2204.02183
**Authors:** José Ángel Morell, Zakaria Abdelmoiz Dahi, Francisco Chicano, Gabriel Luque, Enrique Alba
**Published:** 2022-04-01T18:06:20Z
**Abstract:**
Federated learning is a training paradigm according to which a server-based model is cooperatively trained using local models running on edge devices and ensuring data privacy. These devices exchange information that induces a substantial communication load, which jeopardises the functioning efficiency. The difficulty of reducing this overhead stands in achieving this without decreasing the model's efficiency (contradictory relation). To do so, many works investigated the compression of the pre/mid/post-trained models and the communication rounds, separately, although they jointly contribute to the communication overload. Our work aims at optimising communication overhead in federated learning by (I) modelling it as a multi-objective problem and (II) applying a multi-objective optimization algorithm (NSGA-II) to solve it. To the best of the author's knowledge, this is the first work that \texttt{(I)} explores the add-in that evolutionary computation could bring for solving such a problem, and \texttt{(II)} considers both the neuron and devices features together. We perform the experimentation by simulating a server/client architecture with 4 slaves. We investigate both convolutional and fully-connected neural networks with 12 and 3 layers, 887,530 and 33,400 weights, respectively. We conducted the validation on the \texttt{MNIST} dataset containing 70,000 images. The experiments have shown that our proposal could reduce communication by 99% and maintain an accuracy equal to the one obtained by the FedAvg Algorithm that uses 100% of communications.

## Skill Description

This skill is generated from the arXiv paper: Optimising Communication Overhead in Federated Learning Using NSGA-II (2204.02183).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2204.02183](http://arxiv.org/abs/2204.02183v1)
