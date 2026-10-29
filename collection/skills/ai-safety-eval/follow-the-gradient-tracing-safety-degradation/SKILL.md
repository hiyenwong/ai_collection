---
name: follow-the-gradient-tracing-safety-degradation
description: "Research paper: Follow the Gradient: Tracing Safety Degradation Back to Training Data"
tags: [arxiv, paper, cs.LG, cs.AI, cs.CL]
arxiv_id: "2610.37481"
utility: 0.9
---

# Follow the Gradient: Tracing Safety Degradation Back to Training Data

**arXiv:** [2610.37481](https://arxiv.org/abs/2610.37481)
**Authors:** Saket Reddy, Amro Abbas, Anshuman Suri, Ari Morcos, David Schwab...
**Published:** 2026-10-27
**Categories:** cs.LG, cs.AI, cs.CL
**Utility Score:** 0.9

## Abstract

Fine-tuning Large Language Models (LLMs) on instruction data can quietly erode their safety, even when no training example looks harmful. Because this safety-degrading data looks benign, standard content filters struggle to catch it. We tackle this problem by developing SimpleLoRIF, a scalable gradient embedding method that identifies fine-tuning examples whose gradients align with unsafe behavior. By simplifying a low-rank attribution method and restricting backpropagation to the final four transformer blocks, SimpleLoRIF can embed datasets on the order of a million examples, boosting gradient attribution from a small-scale analysis tool into a practical filter for full post-training datasets. We first validate it on emergent misalignment, where we find that gradients can connect insecure-code training data to the broadly harmful behaviors that appear after fine-tuning, with AUC as high as 0.865 in the gradient space of misaligned models. We then use SimpleLoRIF to build SafeTulu, a version of Tulu 3 with the 20% of examples most gradient-aligned with unsafe responses removed. Training on SafeTulu reduces GCG attack success rate by up to 22% across Qwen, Llama, and Olmo, outperforming both LLM-as-a-judge and prior gradient-based filtering, while largely preserving or even improving capability. Finally, we analyzed the removed data and identify possibly under-studied sources of safety degradation, such as tool-execution failures and narrative arithmetic. We release SafeTulu a

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG, cs.AI, cs.CL

## Potential Applications

- Research reference for ai safety eval domain
- Building block for future work in this area
