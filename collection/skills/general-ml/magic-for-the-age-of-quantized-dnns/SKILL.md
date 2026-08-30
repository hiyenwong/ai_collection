# Magic for the Age of Quantized DNNs

**arXiv ID:** 2403.14999
**Authors:** Yoshihide Sawada, Ryuji Saiin, Kazuma Suetake
**Published:** 2024-03-22T07:21:09Z
**Abstract:**
Recently, the number of parameters in DNNs has explosively increased, as exemplified by LLMs (Large Language Models), making inference on small-scale computers more difficult. Model compression technology is, therefore, essential for integration into products. In this paper, we propose a method of quantization-aware training. We introduce a novel normalization (Layer-Batch Normalization) that is independent of the mini-batch size and does not require any additional computation cost during inference. Then, we quantize the weights by the scaled round-clip function with the weight standardization. We also quantize activation functions using the same function and apply surrogate gradients to train the model with both quantized weights and the quantized activation functions. We call this method Magic for the age of Quantised DNNs (MaQD). Experimental results show that our quantization method can be achieved with minimal accuracy degradation.

## Skill Description

This skill is generated from the arXiv paper: Magic for the Age of Quantized DNNs (2403.14999).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2403.14999](http://arxiv.org/abs/2403.14999v1)
