# OFA$^2$: A Multi-Objective Perspective for the Once-for-All Neural Architecture Search

**arXiv ID:** 2303.13683
**Authors:** Rafael C. Ito, Fernando J. Von Zuben
**Published:** 2023-03-23T21:30:29Z
**Abstract:**
Once-for-All (OFA) is a Neural Architecture Search (NAS) framework designed to address the problem of searching efficient architectures for devices with different resources constraints by decoupling the training and the searching stages. The computationally expensive process of training the OFA neural network is done only once, and then it is possible to perform multiple searches for subnetworks extracted from this trained network according to each deployment scenario. In this work we aim to give one step further in the search for efficiency by explicitly conceiving the search stage as a multi-objective optimization problem. A Pareto frontier is then populated with efficient, and already trained, neural architectures exhibiting distinct trade-offs among the conflicting objectives. This could be achieved by using any multi-objective evolutionary algorithm during the search stage, such as NSGA-II and SMS-EMOA. In other words, the neural network is trained once, the searching for subnetworks considering different hardware constraints is also done one single time, and then the user can choose a suitable neural network according to each deployment scenario. The conjugation of OFA and an explicit algorithm for multi-objective optimization opens the possibility of a posteriori decision-making in NAS, after sampling efficient subnetworks which are a very good approximation of the Pareto frontier, given that those subnetworks are already trained and ready to use. The source code and the final search algorithm will be released at https://github.com/ito-rafael/once-for-all-2

## Skill Description

This skill is generated from the arXiv paper: OFA$^2$: A Multi-Objective Perspective for the Once-for-All Neural Architecture Search (2303.13683).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2303.13683](http://arxiv.org/abs/2303.13683v1)
