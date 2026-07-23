---
name: do-you-remember-toward-memory-centric-multimodal-a
description: Skill derived from arXiv paper 2607.11919: Do You Remember? Toward Memory-Centric Multimodal AI
category: other
created: 2026-07-23
arxiv_id: 2607.11919
utility: 1.0
---
# do-you-remember-toward-memory-centric-multimodal-a

Derived from arXiv paper [2607.11919]: Do You Remember? Toward Memory-Centric Multimodal AI

## Abstract
Human memory is reconstructive, not a faithful recording. Current multimodal LLMs (MLLMs) lack this capability: they process images through a frozen visual encoder, produce a one-shot text output, and discard internal representations. We present DoYouRemember, a three-stage architecture introducing reconstructive memory into MLLMs: (1) a VQ-VAE compresses images into discrete visual tokens, (2) a LoRA-fine-tuned LLM jointly attends to visual and text tokens, and (3) a Diffusion Decoder reconstructs images from the LLM's hidden states. On 1,000 3D facial skin texture maps and 99,000 unlabeled facial images, we find that LLM hidden states contain approximately zero recoverable visual information -- the same Decoder producing clear reconstructions from VQ-VAE tokens (pre-LLM) produces pure noise from LLM hidden states (post-LLM), demonstrating that the LLM understands images but does not remember them. Training a shared memory matrix M under backpropagation systematically fails due to gradient cancellation (O(1/sqrt(N)) attenuation). We identify three root causes and show that local EMA updating resolves all three: each image updates only its top-8 slots out of 64, preserving inter-slot diversity. The resulting M (229K parameters, 16x compressed) approaches the VQ upper bound on unseen test images. Scaling to 1,024 slots surpasses it (LPIPS 0.056 vs. 0.071), as M's continuous representation avoids VQ quantization error. We unify these findings under an information-theoretic framework: memory is lossy compression, recall is decompression, and hallucination is an inherent property of lossy decompression rather than a defect.

## Authors
Xuguang Yu, Weigang Zheng, Minyue Yu

## Published
2026-07-07

## Categories
cs.NE, cs.AI, cs.CV, cs.LG

## Utility
1.0

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
