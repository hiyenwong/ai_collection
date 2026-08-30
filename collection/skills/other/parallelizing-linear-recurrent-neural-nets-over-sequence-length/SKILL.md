# Parallelizing Linear Recurrent Neural Nets Over Sequence Length

**arXiv ID:** 1709.04057
**Authors:** Eric Martin, Chris Cundy
**Published:** 2017-09-12T20:52:22Z
**Abstract:**
Recurrent neural networks (RNNs) are widely used to model sequential data but their non-linear dependencies between sequence elements prevent parallelizing training over sequence length. We show the training of RNNs with only linear sequential dependencies can be parallelized over the sequence length using the parallel scan algorithm, leading to rapid training on long sequences even with small minibatch size. We develop a parallel linear recurrence CUDA kernel and show that it can be applied to immediately speed up training and inference of several state of the art RNN architectures by up to 9x. We abstract recent work on linear RNNs into a new framework of linear surrogate RNNs and develop a linear surrogate model for the long short-term memory unit, the GILR-LSTM, that utilizes parallel linear recurrence. We extend sequence learning to new extremely long sequence regimes that were previously out of reach by successfully training a GILR-LSTM on a synthetic sequence classification task with a one million timestep dependency.

## Skill Description

This skill is generated from the arXiv paper: Parallelizing Linear Recurrent Neural Nets Over Sequence Length (1709.04057).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1709.04057](http://arxiv.org/abs/1709.04057v2)
