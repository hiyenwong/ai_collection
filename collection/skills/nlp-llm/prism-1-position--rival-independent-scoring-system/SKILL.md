---
name: prism-1-position--rival-independent-scoring-system
description: "Prism-1: Position- and Rival-Independent Scoring for System One Models"
tags: [arxiv, paper, nlp-llm]
arxiv_id: "2610.22066"
utility: 0.96
date: "2026-10-17"
---

# Prism-1: Position- and Rival-Independent Scoring for System One Models

**arXiv:** [2610.22066](https://arxiv.org/abs/2610.22066)
**Authors:** Yao Long Teng, Jianguo Huang, Yanchen Deng, Jiayi Cai, Bo An
**Published:** 2026-10-15
**Categories:** cs.AI
**Utility Score:** 0.96

## Abstract

Given a state and a set of options, such as intents, tools or interface elements, System One decision models return a distribution over the options in one forward pass, without generated reasoning. Web systems increasingly build them by reading decisions from language models. Two axioms of rational choice are natural requirements for such decisions, because in web systems the listing and the option set are determined by other components and can change or be manipulated: the order in which the options are listed should not matter, and adding an option should not change the relative odds of the others (Luce's choice axiom). We test the standard reads, namely single-choice question (SCQ) prompting, with shuffled-order training, order averaging or sorted options, and invariant set architectures, and find that each violates at least one axiom: one shuffle changes 12-20% of SCQ answers, sorting only freezes an arbitrary convention, and a well-chosen added option steers 4-34% of decisions. By Luce's theorem, a read satisfies both axioms only if it is a softmax over scores that each depend on one option alone, so in a transformer they hold by construction only if no token that scores an option sees another. We implement this as Prism-1 (Position- and Rival-Independent Scoring for System One Models): every option is read in its own block at shared positions, with the model's usual left-to-right attention, in one forward pass. On five benchmark sets with Qwen3-8B and Gemma 4 12B, SCQ prompting trained on the same data still changes 7% of its answers under one shuffle, and an added irrelevant option steers 12% of its decisions. Prism-1 stays within one point of that baseline's accuracy and is 2-4 points more accurate once only answers that survive a reordering are counted, while no shuffle changes any of its answers and no added irrelevant option moves its choice among the others.

## Key Contributions

- Novel research in cs.AI
- High utility score (0.96) indicating significant research value

## Activation

prism, position, rivalindependent, scoring, system, models

## Notes

Added by arXiv cron job on 2026-10-17.
