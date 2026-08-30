# Neural Pruning via Growing Regularization

**arXiv ID:** 2012.09243
**Authors:** Huan Wang, Can Qin, Yulun Zhang, Yun Fu
**Published:** 2020-12-16T20:16:28Z
**Abstract:**
Regularization has long been utilized to learn sparsity in deep neural network pruning. However, its role is mainly explored in the small penalty strength regime. In this work, we extend its application to a new scenario where the regularization grows large gradually to tackle two central problems of pruning: pruning schedule and weight importance scoring. (1) The former topic is newly brought up in this work, which we find critical to the pruning performance while receives little research attention. Specifically, we propose an L2 regularization variant with rising penalty factors and show it can bring significant accuracy gains compared with its one-shot counterpart, even when the same weights are removed. (2) The growing penalty scheme also brings us an approach to exploit the Hessian information for more accurate pruning without knowing their specific values, thus not bothered by the common Hessian approximation problems. Empirically, the proposed algorithms are easy to implement and scalable to large datasets and networks in both structured and unstructured pruning. Their effectiveness is demonstrated with modern deep neural networks on the CIFAR and ImageNet datasets, achieving competitive results compared to many state-of-the-art algorithms. Our code and trained models are publicly available at https://github.com/mingsuntse/regularization-pruning.

## Skill Description

This skill is generated from the arXiv paper: Neural Pruning via Growing Regularization (2012.09243).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2012.09243](http://arxiv.org/abs/2012.09243v2)
