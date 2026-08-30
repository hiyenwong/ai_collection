# Parallel Training of Deep Networks with Local Updates

**arXiv ID:** 2012.03837
**Authors:** Michael Laskin, Luke Metz, Seth Nabarro, Mark Saroufim, Badreddine Noune, Carlo Luschi, Jascha Sohl-Dickstein, Pieter Abbeel
**Published:** 2020-12-07T16:38:45Z
**Abstract:**
Deep learning models trained on large data sets have been widely successful in both vision and language domains. As state-of-the-art deep learning architectures have continued to grow in parameter count so have the compute budgets and times required to train them, increasing the need for compute-efficient methods that parallelize training. Two common approaches to parallelize the training of deep networks have been data and model parallelism. While useful, data and model parallelism suffer from diminishing returns in terms of compute efficiency for large batch sizes. In this paper, we investigate how to continue scaling compute efficiently beyond the point of diminishing returns for large batches through local parallelism, a framework which parallelizes training of individual layers in deep networks by replacing global backpropagation with truncated layer-wise backpropagation. Local parallelism enables fully asynchronous layer-wise parallelism with a low memory footprint, and requires little communication overhead compared with model parallelism. We show results in both vision and language domains across a diverse set of architectures, and find that local parallelism is particularly effective in the high-compute regime.

## Skill Description

This skill is generated from the arXiv paper: Parallel Training of Deep Networks with Local Updates (2012.03837).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2012.03837](http://arxiv.org/abs/2012.03837v2)
