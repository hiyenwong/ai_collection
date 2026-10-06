---
name: learning-to-read-the-contextual-tokens
description: "Learning to Read the Contextual Tokens in Diffusio..."
tags: [cs.CV, cs.AI, cs.GR]
source: arxiv
arxiv_id: 2610.06844v1
utility: 0.9
published: 2026-10-05
---

# Learning to Read the Contextual Tokens in Diffusion Transformers

**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, Daniel Cohen-Or, Or Patashnik
**Published:** 2026-10-05
**arXiv:** [2610.06844v1](https://arxiv.org/abs/2610.06844v1)
**Categories:** cs.CV, cs.AI, cs.GR, cs.LG
**Utility Score:** 0.9

## Abstract

Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Large Language Model (LLM), allowing the LLM to answer questions about the emerging image directly from these hidden representations. Our reader reveals that contextual tokens encode a rich, global representation of the emerging scene: generation-specific semantics, including attributes left underspecified by the prompt, are accessible surprisingly early in denoising, while increasingly fine-grained details become readable over time. Remarkably, this information remains decodable even when the MM-DiT receives an empty prompt, showing that contextual tokens accumulate substantial image-specific information from the evolving visual representation itself. We further find that generations with more readable contextual representations tend to receive higher human-preference scores. Building on these observations, we introduce Contextual Alignment, a training technique that explicitly reinforces the visual-semantic information encoded in the contextual tokens, improving generation quality and d

## Key Contributions

- Novel research in cs.CV, cs.AI
- Published 2026-10-05

## Activation

learning, read, contextual, tokens, diffusion, transformers
