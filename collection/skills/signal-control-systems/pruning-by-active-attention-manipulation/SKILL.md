# Pruning by Active Attention Manipulation

**arXiv ID:** 2210.11114
**Authors:** Zahra Babaiee, Lucas Liebenwein, Ramin Hasani, Daniela Rus, Radu Grosu
**Published:** 2022-10-20T09:17:02Z
**Abstract:**
Filter pruning of a CNN is typically achieved by applying discrete masks on the CNN's filter weights or activation maps, post-training. Here, we present a new filter-importance-scoring concept named pruning by active attention manipulation (PAAM), that sparsifies the CNN's set of filters through a particular attention mechanism, during-training. PAAM learns analog filter scores from the filter weights by optimizing a cost function regularized by an additive term in the scores. As the filters are not independent, we use attention to dynamically learn their correlations. Moreover, by training the pruning scores of all layers simultaneously, PAAM can account for layer inter-dependencies, which is essential to finding a performant sparse sub-network. PAAM can also train and generate a pruned network from scratch in a straightforward, one-stage training process without requiring a pre-trained network. Finally, PAAM does not need layer-specific hyperparameters and pre-defined layer budgets, since it can implicitly determine the appropriate number of filters in each layer. Our experimental results on different network architectures suggest that PAAM outperforms state-of-the-art structured-pruning methods (SOTA). On CIFAR-10 dataset, without requiring a pre-trained baseline network, we obtain 1.02% and 1.19% accuracy gain and 52.3% and 54% parameters reduction, on ResNet56 and ResNet110, respectively. Similarly, on the ImageNet dataset, PAAM achieves 1.06% accuracy gain while pruning 51.1% of the parameters on ResNet50. For Cifar-10, this is better than the SOTA with a margin of 9.5% and 6.6%, respectively, and on ImageNet with a margin of 11%.

## Skill Description

This skill is generated from the arXiv paper: Pruning by Active Attention Manipulation (2210.11114).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2210.11114](http://arxiv.org/abs/2210.11114v1)
