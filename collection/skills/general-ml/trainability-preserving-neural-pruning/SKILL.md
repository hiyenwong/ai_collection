# Trainability Preserving Neural Pruning

**arXiv ID:** 2207.12534
**Authors:** Huan Wang, Yun Fu
**Published:** 2022-07-25T21:15:47Z
**Abstract:**
Many recent works have shown trainability plays a central role in neural network pruning -- unattended broken trainability can lead to severe under-performance and unintentionally amplify the effect of retraining learning rate, resulting in biased (or even misinterpreted) benchmark results. This paper introduces trainability preserving pruning (TPP), a scalable method to preserve network trainability against pruning, aiming for improved pruning performance and being more robust to retraining hyper-parameters (e.g., learning rate). Specifically, we propose to penalize the gram matrix of convolutional filters to decorrelate the pruned filters from the retained filters. In addition to the convolutional layers, per the spirit of preserving the trainability of the whole network, we also propose to regularize the batch normalization parameters (scale and bias). Empirical studies on linear MLP networks show that TPP can perform on par with the oracle trainability recovery scheme. On nonlinear ConvNets (ResNet56/VGG19) on CIFAR10/100, TPP outperforms the other counterpart approaches by an obvious margin. Moreover, results on ImageNet-1K with ResNets suggest that TPP consistently performs more favorably against other top-performing structured pruning approaches. Code: https://github.com/MingSun-Tse/TPP.

## Skill Description

This skill is generated from the arXiv paper: Trainability Preserving Neural Pruning (2207.12534).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2207.12534](http://arxiv.org/abs/2207.12534v3)
