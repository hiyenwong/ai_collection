---
name: recast-reconstruction-of-chain-of-thought-via-auditable
description: "RECAST: REconstruction of Chain-of-Thought via Aud..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.41813v1
utility: 0.88
published: 2026-10-30
---

# RECAST: REconstruction of Chain-of-Thought via Auditable Structured Traces

**Authors:** Qi Wang, Kang Xu, Chengcheng Wan, Jiangtao Wang
**Published:** 2026-10-30
**arXiv:** [2610.41813v1](https://arxiv.org/abs/2610.41813v1)
**Categories:** cs.AI
**Utility Score:** 0.88

## Abstract

Large closed-source reasoning models expose only their final answers. The intermediate reasoning that produces those answers is hidden behind API surfaces, tool-call policies, and safety filters. Existing chain-of-thought (CoT) extraction methods assume a side channel: a visible reasoning field, a scratchpad carried through tool calls, or a signed/encrypted reasoning block. We reproduce three representative state-of-the-art extraction methods and find that, on Claude-Sonnet-5.5 accessed through the standard chat-completions interface, all three return zero CoT tokens. The failure is structural rather than a bug: the reasoning field is absent, named tool selection is rejected, free-text scratchpad arguments are filtered, and no replayable reasoning block is exposed. We therefore take a different route. We present RECAST, a reconstruction-based framework that conditions a decoder on the question and the target model's final answer, reconstructs a first-person structured rationale, cleans it, and builds SFT-ready data. To the best of our knowledge, RECAST is the first system to reconstruct CoT from frontier closed models such as Claude-Sonnet-5.5, GPT-6.1, and Gemini 3 without using hidden reasoning channels. We instantiate RECAST on Claude-Sonnet-5.5 and additionally obtain successful qualitative reconstructions on GPT-6.1 and Gemini 3 with the same answer-only protocol. The system is open-source and packaged as an agent skill: one prompt deploys it and runs the complete pipeli

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-30

## Activation

recast, reconstruction, chainofthought, auditable, structured, traces
