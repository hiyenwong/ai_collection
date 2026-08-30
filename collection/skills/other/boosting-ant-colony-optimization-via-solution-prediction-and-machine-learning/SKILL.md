# Boosting Ant Colony Optimization via Solution Prediction and Machine Learning

**arXiv ID:** 2008.04213
**Authors:** Yuan Sun, Sheng Wang, Yunzhuang Shen, Xiaodong Li, Andreas T. Ernst, Michael Kirley
**Published:** 2020-07-29T13:03:37Z
**Abstract:**
This paper introduces an enhanced meta-heuristic (ML-ACO) that combines machine learning (ML) and ant colony optimization (ACO) to solve combinatorial optimization problems. To illustrate the underlying mechanism of our ML-ACO algorithm, we start by describing a test problem, the orienteering problem. In this problem, the objective is to find a route that visits a subset of vertices in a graph within a time budget to maximize the collected score. In the first phase of our ML-ACO algorithm, an ML model is trained using a set of small problem instances where the optimal solution is known. Specifically, classification models are used to classify an edge as being part of the optimal route, or not, using problem-specific features and statistical measures. The trained model is then used to predict the probability that an edge in the graph of a test problem instance belongs to the corresponding optimal route. In the second phase, we incorporate the predicted probabilities into the ACO component of our algorithm, i.e., using the probability values as heuristic weights or to warm start the pheromone matrix. Here, the probability values bias sampling towards favoring those predicted high-quality edges when constructing feasible routes. We have tested multiple classification models including graph neural networks, logistic regression and support vector machines, and the experimental results show that our solution prediction approach consistently boosts the performance of ACO. Further, we empirically show that our ML model trained on small synthetic instances generalizes well to large synthetic and real-world instances. Our approach integrating ML with a meta-heuristic is generic and can be applied to a wide range of optimization problems.

## Skill Description

This skill is generated from the arXiv paper: Boosting Ant Colony Optimization via Solution Prediction and Machine Learning (2008.04213).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2008.04213](http://arxiv.org/abs/2008.04213v2)
