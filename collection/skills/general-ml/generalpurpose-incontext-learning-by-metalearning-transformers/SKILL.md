# General-Purpose In-Context Learning by Meta-Learning Transformers

**arXiv ID:** 2212.04458
**Authors:** Louis Kirsch, James Harrison, Jascha Sohl-Dickstein, Luke Metz
**Published:** 2022-12-08T18:30:22Z
**Abstract:**
Modern machine learning requires system designers to specify aspects of the learning pipeline, such as losses, architectures, and optimizers. Meta-learning, or learning-to-learn, instead aims to learn those aspects, and promises to unlock greater capabilities with less manual effort. One particularly ambitious goal of meta-learning is to train general-purpose in-context learning algorithms from scratch, using only black-box models with minimal inductive bias. Such a model takes in training data, and produces test-set predictions across a wide range of problems, without any explicit definition of an inference model, training loss, or optimization algorithm. In this paper we show that Transformers and other black-box models can be meta-trained to act as general-purpose in-context learners. We characterize transitions between algorithms that generalize, algorithms that memorize, and algorithms that fail to meta-train at all, induced by changes in model size, number of tasks, and meta-optimization. We further show that the capabilities of meta-trained algorithms are bottlenecked by the accessible state size (memory) determining the next prediction, unlike standard models which are thought to be bottlenecked by parameter count. Finally, we propose practical interventions such as biasing the training distribution that improve the meta-training and meta-generalization of general-purpose in-context learning algorithms.

## Skill Description

This skill is generated from the arXiv paper: General-Purpose In-Context Learning by Meta-Learning Transformers (2212.04458).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2212.04458](http://arxiv.org/abs/2212.04458v2)
