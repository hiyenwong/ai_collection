# mlx-snn: Spiking Neural Networks on Apple Silicon via MLX

**arXiv ID:** 2603.03529
**Authors:** Jiahao Qin
**Published:** 2026-03-03T21:25:36Z
**Abstract:**
We introduce mlx-snn, the first spiking neural network (SNN) library built natively on Apple's MLX framework. As SNN research grows rapidly, all major libraries -- snnTorch, Norse, SpikingJelly, Lava -- target PyTorch or custom backends, leaving Apple Silicon users without a native option. mlx-snn provides six neuron models (LIF, IF, Izhikevich, Adaptive LIF, Synaptic, Alpha), four surrogate gradient functions, four spike encoding methods (including an EEG-specific encoder), and a complete backpropagation-through-time training pipeline. The library leverages MLX's unified memory architecture, lazy evaluation, and composable function transforms (mx.grad, mx.compile) to enable efficient SNN research on Apple Silicon hardware. We validate mlx-snn on MNIST digit classification across five hyperparameter configurations and three backends, achieving up to 97.28% accuracy with 2.0--2.5 times faster training and 3--10 times lower GPU memory than snnTorch on the same M3 Max hardware. mlx-snn is open-source under the MIT license and available on PyPI. https://github.com/D-ST-Sword/mlx-snn

## Skill Description

This skill is generated from the arXiv paper: mlx-snn: Spiking Neural Networks on Apple Silicon via MLX (2603.03529).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2603.03529](http://arxiv.org/abs/2603.03529v1)
