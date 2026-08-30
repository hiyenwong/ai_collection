# AutoQD: Automatic Discovery of Diverse Behaviors with Quality-Diversity Optimization

**arXiv ID:** 2506.05634
**Authors:** Saeed Hedayatian, Stefanos Nikolaidis
**Published:** 2025-06-05T23:34:53Z
**Abstract:**
Quality-Diversity (QD) algorithms have shown remarkable success in discovering diverse, high-performing solutions, but rely heavily on hand-crafted behavioral descriptors that constrain exploration to predefined notions of diversity. Leveraging the equivalence between policies and occupancy measures, we present a theoretically grounded approach to automatically generate behavioral descriptors by embedding the occupancy measures of policies in Markov Decision Processes. Our method, AutoQD, leverages random Fourier features to approximate the Maximum Mean Discrepancy (MMD) between policy occupancy measures, creating embeddings whose distances reflect meaningful behavioral differences. A low-dimensional projection of these embeddings that captures the most behaviorally significant dimensions can then be used as behavioral descriptors for CMA-MAE, a state of the art blackbox QD method, to discover diverse policies. We prove that our embeddings converge to true MMD distances between occupancy measures as the number of sampled trajectories and embedding dimensions increase. Through experiments in multiple continuous control tasks we demonstrate AutoQD's ability in discovering diverse policies without predefined behavioral descriptors, presenting a well-motivated alternative to prior methods in unsupervised Reinforcement Learning and QD optimization. Our approach opens new possibilities for open-ended learning and automated behavior discovery in sequential decision making settings without requiring domain-specific knowledge. Source code is available at https://github.com/conflictednerd/autoqd-code.

## Skill Description

This skill is generated from the arXiv paper: AutoQD: Automatic Discovery of Diverse Behaviors with Quality-Diversity Optimization (2506.05634).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2506.05634](http://arxiv.org/abs/2506.05634v2)
