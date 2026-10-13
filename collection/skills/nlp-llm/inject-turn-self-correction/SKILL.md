---
name: inject-turn-self-correction
description: 'Learning where to intervene in failed LLM reasoning rollouts for self-correction. Use when training LLMs to identify and correct their own reasoning errors mid-generation.'
arxiv_id: '2610.13672'
utility: 0.86
authors: Jiwon Jeon, Myungsik Cho, Jeonghye Kim, Youngchul Sung
categories: [cs.CL, cs.AI]
tags: [self-correction, llm-reasoning, intervention, error-detection, training]
---

# Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning

## Key Innovation

Instead of fine-tuning LLMs to generate revisions or feedback, learns WHERE to intervene in failed rollouts and HOW to redirect them. Trains a 130K-parameter MLP head on frozen encoder using only final-answer correctness.

## Method

- Intervention point selection via lightweight MLP head (130K params)
- Frozen encoder backbone — minimal training overhead
- Uses only final-answer correctness signal (no intermediate labels)
- Redirects reasoning by injecting new turns, not tokens

## Key Finding

Inline token injections fail to reliably correct reasoning under fixed generation budgets — turn-level intervention is more effective.

## Results

- Improved self-correction rates on reasoning tasks
- Lightweight intervention model (130K parameters)
- Works with frozen base model

## Practical Use

- Improving LLM reasoning reliability
- Building self-correcting agent systems
- Efficient training of reasoning correction capabilities

## URL

https://arxiv.org/abs/2610.13672
