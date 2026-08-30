# Hybrid activation functions for deep neural networks: S3 and S4 -- a novel approach to gradient flow optimization

**arXiv ID:** 2507.22090
**Authors:** Sergii Kavun
**Published:** 2025-07-29T09:21:57Z
**Abstract:**
Activation functions are critical components in deep neural networks, directly influencing gradient flow, training stability, and model performance. Traditional functions like ReLU suffer from dead neuron problems, while sigmoid and tanh exhibit vanishing gradient issues. We introduce two novel hybrid activation functions: S3 (Sigmoid-Softsign) and its improved version S4 (smoothed S3). S3 combines sigmoid for negative inputs with softsign for positive inputs, while S4 employs a smooth transition mechanism controlled by a steepness parameter k. We conducted comprehensive experiments across binary classification, multi-class classification, and regression tasks using three different neural network architectures. S4 demonstrated superior performance compared to nine baseline activation functions, achieving 97.4% accuracy on MNIST, 96.0% on Iris classification, and 18.7 MSE on Boston Housing regression. The function exhibited faster convergence (-19 for ReLU) and maintained stable gradient flow across network depths. Comparative analysis revealed S4's gradient range of [0.24, 0.59] compared to ReLU's 18% dead neurons in deep networks. The S4 activation function addresses key limitations of existing functions through its hybrid design and smooth transition mechanism. The tunable parameter k allows adaptation to different tasks and network depths, making S4 a versatile choice for deep learning applications. These findings suggest that hybrid activation functions represent a promising direction for improving neural network training dynamics.

## Skill Description

This skill is generated from the arXiv paper: Hybrid activation functions for deep neural networks: S3 and S4 -- a novel approach to gradient flow optimization (2507.22090).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2507.22090](http://arxiv.org/abs/2507.22090v1)
