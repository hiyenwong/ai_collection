# PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers

**arXiv ID:** 2606.03257
**Authors:** Rachmad Vidya Wicaksana Putra, Achyuta Muthuvelan, Alberto Marchisio, Muhammad Shafique
**Published:** 2026-06-02T07:18:57Z
**Abstract:**
Spiking Vision Transformer (SViT) models are promising low-power ViT models for solving vision-based tasks with state-of-the-art performance. However, their large sizes limit their deployments for resource-constrained embedded platforms, underscoring the needs of model compression. One of prominent compression techniques is pruning, and the state-of-the-art works employ unstructured pruning techniques to compress SViT models. Such techniques require specialized hardware architectures tailored for the sparsity patterns to maximize their efficiency benefits, making this approach not scalable. To address this, we propose PSViT, a novel methodology to perform structured pruning on SViT models, hence making it possible to efficiently accelerate their inference using the existing and widely-used computing architectures. To do this, PSViT employs several key steps: uniform channel-wise filter pruning to structurally eliminate the non-significant weights, sensitivity analysis to evaluate the impact of channel-wise pruning of individual layer on accuracy and network size, as well as fine-grained channel-wise pruning based on the sensitivity analysis and the given network architecture. Experimental results show that PSViT effectively obtains 22.4% memory saving through single-shot pruning, while maintaining high accuracy within 3% (70.3% without fine-tuning and 72.8% with fine-tuning) from the original non-pruned SViT model (73.3%) on the ImageNet-1K. These results also show that the PSViT methodology advances the effort in enabling efficient SViT deployments on resource-constrained applications.

## Skill Description

This skill is generated from the arXiv paper: PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers (2606.03257).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2606.03257](http://arxiv.org/abs/2606.03257v1)
