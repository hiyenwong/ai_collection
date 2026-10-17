---
name: memory-weights-internalizing-long-term-history
description: "Memory as Weights: Internalizing Long-Term History for Streaming Videos"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22070"
utility: 0.86
date: "2026-10-17"
---

# Memory as Weights: Internalizing Long-Term History for Streaming Videos

**arXiv:** [2610.22070](https://arxiv.org/abs/2610.22070)
**Authors:** Zhuoming Liu, Jinhong Lin, Lin Zhang, Yiwu Zhong, Yin Li
**Published:** 2026-10-15
**Categories:** cs.CV, cs.AI, cs.LG
**Utility Score:** 0.86

## Abstract

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries. Existing memory mechanisms typically compress, retrieve, or cache historical observations and reintroduce them into the input context, forcing historical memory and current observations to compete for limited context. We propose MaLoW, a streaming memory framework that instead internalizes historical context into evolving lightweight parameter updates. MaLoW uses a recurrent HyperNetwork to incrementally consolidate incoming video observations into fixed-size LoRA weights, allowing historical information to be carried forward without revisiting the full video stream. In doing so, MaLoW represents history as weights, while keeping the current observation as input. To support training, we further construct MaLoW-Instruct, a large-scale streaming video dataset containing 381K question-answer pairs over 56K videos. We conduct extensive experiments to demonstrate that MaLoW achieves strong performance on OVO-Bench, StreamingBench, and StreamArena. On the backward split of OVO-Bench, MaLoW outperforms prior memory approaches by 3.9% to 11.8% across different video backbones while incurring only modest latency overhead. Beyond streaming video understanding, MaLoW also generalizes to vision-language-action models, improving the action success rate on Simpler WidowX by 9.3%.

## Key Contributions

- Novel research in cs.CV, cs.AI
- High utility score (0.86) indicating significant research value

## Activation

memory, weights, internalizing, longterm, history, streaming, videos

## Notes

Added by arXiv cron job on 2026-10-17.
