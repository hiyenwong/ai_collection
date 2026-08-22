---
name: arxiv-2608-20210-daedalus-150m-a-convolution-attention-hybrid-desig
description: 'Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference (arXiv: 2608.20210)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference

**Authors:** Christos Koutsiaris
**arXiv:** 2608.20210
**Utility:** 1.00
**Published:** 2026-08-20T16:09:43Z
**Link:** http://arxiv.org/abs/2608.20210

## Abstract

Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one user, one token at a time, 4-bit weights, ordinary CPU, and chose the architecture to suit it. The result keeps full attention in only 6 of its 18 blocks. The other 12 use short convolutions whose memory is two timesteps wide no matter how long the conversation gets, so two thirds of the network never re-reads a growing cache.
  Trained from scratch on 59.9B tokens, the model scores 47.31 on a five-task benchmark against a bar of 42.20 that was fixed before training began. It beats GPT-2 124M, Pythia-160M, OPT-125M and GPT-neo-125M, all trained on three to six times more data, and exceeds MobileLLM-125M's published score despite that model seeing a trillion tokens. Validation bits-per-byte is 0.8685.
  To check the architecture rather than the training recipe, we trained a conventional all-attention model of the same size on the same data, and wrote down the winning condition before scoring either. The hybrid won the chosen quality metric by 0.81%, matched it on downstream tasks, produced a 6.3% smaller 4-bit file, and decoded 1.76x faster at 2048 tokens of context, 2.08x against an external model of similar size. In every measurement the speed advantage is near zero at an empty context and grows with length, which is what the mechanism predicts and what a merely leaner model would not show. A simple bandwidth calculation predicts only 1.17x, so memory volume alone does not explain the gap.
  We also report what did not work: an unmitigated 4-bit quality cost, roughly half the convolution channels ending up inert and impossible to remove, and a vocabulary larger than this model size warrants.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20210
