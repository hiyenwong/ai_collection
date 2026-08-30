# BR-NS: an Archive-less Approach to Novelty Search

**arXiv ID:** 2104.03936
**Authors:** Achkan Salehi, Alexandre Coninx, Stephane Doncieux
**Published:** 2021-04-08T17:31:34Z
**Abstract:**
As open-ended learning based on divergent search algorithms such as Novelty Search (NS) draws more and more attention from the research community, it is natural to expect that its application to increasingly complex real-world problems will require the exploration to operate in higher dimensional Behavior Spaces which will not necessarily be Euclidean. Novelty Search traditionally relies on k-nearest neighbours search and an archive of previously visited behavior descriptors which are assumed to live in a Euclidean space. This is problematic because of a number of issues. On one hand, Euclidean distance and Nearest-neighbour search are known to behave differently and become less meaningful in high dimensional spaces. On the other hand, the archive has to be bounded since, memory considerations aside, the computational complexity of finding nearest neighbours in that archive grows linearithmically with its size. A sub-optimal bound can result in "cycling" in the behavior space, which inhibits the progress of the exploration. Furthermore, the performance of NS depends on a number of algorithmic choices and hyperparameters, such as the strategies to add or remove elements to the archive and the number of neighbours to use in k-nn search. In this paper, we discuss an alternative approach to novelty estimation, dubbed Behavior Recognition based Novelty Search (BR-NS), which does not require an archive, makes no assumption on the metrics that can be defined in the behavior space and does not rely on nearest neighbours search. We conduct experiments to gain insight into its feasibility and dynamics as well as potential advantages over archive-based NS in terms of time complexity.

## Skill Description

This skill is generated from the arXiv paper: BR-NS: an Archive-less Approach to Novelty Search (2104.03936).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2104.03936](http://arxiv.org/abs/2104.03936v1)
