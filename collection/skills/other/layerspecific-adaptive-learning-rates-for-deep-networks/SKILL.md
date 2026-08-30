# Layer-Specific Adaptive Learning Rates for Deep Networks

**arXiv ID:** 1510.04609
**Authors:** Bharat Singh, Soham De, Yangmuzi Zhang, Thomas Goldstein, Gavin Taylor
**Published:** 2015-10-15T16:31:46Z
**Abstract:**
The increasing complexity of deep learning architectures is resulting in training time requiring weeks or even months. This slow training is due in part to vanishing gradients, in which the gradients used by back-propagation are extremely large for weights connecting deep layers (layers near the output layer), and extremely small for shallow layers (near the input layer); this results in slow learning in the shallow layers. Additionally, it has also been shown that in highly non-convex problems, such as deep neural networks, there is a proliferation of high-error low curvature saddle points, which slows down learning dramatically. In this paper, we attempt to overcome the two above problems by proposing an optimization method for training deep neural networks which uses learning rates which are both specific to each layer in the network and adaptive to the curvature of the function, increasing the learning rate at low curvature points. This enables us to speed up learning in the shallow layers of the network and quickly escape high-error low curvature saddle points. We test our method on standard image classification datasets such as MNIST, CIFAR10 and ImageNet, and demonstrate that our method increases accuracy as well as reduces the required training time over standard algorithms.

## Skill Description

This skill is generated from the arXiv paper: Layer-Specific Adaptive Learning Rates for Deep Networks (1510.04609).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1510.04609](http://arxiv.org/abs/1510.04609v1)
