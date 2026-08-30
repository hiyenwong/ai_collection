# Self-Distillation Learning Based on Temporal-Spatial Consistency for Spiking Neural Networks

**arXiv ID:** 2406.07862
**Authors:** Lin Zuo, Yongqi Ding, Mengmeng Jing, Kunshan Yang, Yunqian Yu
**Published:** 2024-06-12T04:30:40Z
**Abstract:**
Spiking neural networks (SNNs) have attracted considerable attention for their event-driven, low-power characteristics and high biological interpretability. Inspired by knowledge distillation (KD), recent research has improved the performance of the SNN model with a pre-trained teacher model. However, additional teacher models require significant computational resources, and it is tedious to manually define the appropriate teacher network architecture. In this paper, we explore cost-effective self-distillation learning of SNNs to circumvent these concerns. Without an explicit defined teacher, the SNN generates pseudo-labels and learns consistency during training. On the one hand, we extend the timestep of the SNN during training to create an implicit temporal ``teacher" that guides the learning of the original ``student", i.e., the temporal self-distillation. On the other hand, we guide the output of the weak classifier at the intermediate stage by the final output of the SNN, i.e., the spatial self-distillation. Our temporal-spatial self-distillation (TSSD) learning method does not introduce any inference overhead and has excellent generalization ability. Extensive experiments on the static image datasets CIFAR10/100 and ImageNet as well as the neuromorphic datasets CIFAR10-DVS and DVS-Gesture validate the superior performance of the TSSD method. This paper presents a novel manner of fusing SNNs with KD, providing insights into high-performance SNN learning methods.

## Skill Description

This skill is generated from the arXiv paper: Self-Distillation Learning Based on Temporal-Spatial Consistency for Spiking Neural Networks (2406.07862).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2406.07862](http://arxiv.org/abs/2406.07862v1)
