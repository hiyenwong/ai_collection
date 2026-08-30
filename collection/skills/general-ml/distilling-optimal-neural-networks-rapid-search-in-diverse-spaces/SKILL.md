# Distilling Optimal Neural Networks: Rapid Search in Diverse Spaces

**arXiv ID:** 2012.08859
**Authors:** Bert Moons, Parham Noorzad, Andrii Skliar, Giovanni Mariani, Dushyant Mehta, Chris Lott, Tijmen Blankevoort
**Published:** 2020-12-16T11:00:19Z
**Abstract:**
Current state-of-the-art Neural Architecture Search (NAS) methods neither efficiently scale to multiple hardware platforms, nor handle diverse architectural search-spaces. To remedy this, we present DONNA (Distilling Optimal Neural Network Architectures), a novel pipeline for rapid, scalable and diverse NAS, that scales to many user scenarios. DONNA consists of three phases. First, an accuracy predictor is built using blockwise knowledge distillation from a reference model. This predictor enables searching across diverse networks with varying macro-architectural parameters such as layer types and attention mechanisms, as well as across micro-architectural parameters such as block repeats and expansion rates. Second, a rapid evolutionary search finds a set of pareto-optimal architectures for any scenario using the accuracy predictor and on-device measurements. Third, optimal models are quickly finetuned to training-from-scratch accuracy. DONNA is up to 100x faster than MNasNet in finding state-of-the-art architectures on-device. Classifying ImageNet, DONNA architectures are 20% faster than EfficientNet-B0 and MobileNetV2 on a Nvidia V100 GPU and 10% faster with 0.5% higher accuracy than MobileNetV2-1.4x on a Samsung S20 smartphone. In addition to NAS, DONNA is used for search-space extension and exploration, as well as hardware-aware model compression.

## Skill Description

This skill is generated from the arXiv paper: Distilling Optimal Neural Networks: Rapid Search in Diverse Spaces (2012.08859).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2012.08859](http://arxiv.org/abs/2012.08859v3)
