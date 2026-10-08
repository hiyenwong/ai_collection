---
name: arxiv-2610-10411-training-parallel-speculative-draft-models-by-directly-minimizing-expected-decod
description: 'Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds (arXiv: 2610.10411)'
metadata:
  {
    "arxiv_id": "2610.10411",
    "utility": 1.0,
    "title": "Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds",
    "authors": "Yunxiao Zhao, Changxiao Cai",
    "url": "https://arxiv.org/abs/2610.10411v1",
    "categories": ["cs.LG", "cs.AI", "cs.CL", "stat.ML"],
    "published": "2026-10-07"
  }
---

# Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds

**arXiv ID:** 2610.10411
**Authors:** Yunxiao Zhao, Changxiao Cai
**URL:** https://arxiv.org/abs/2610.10411v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.LG, cs.AI, cs.CL, stat.ML

## Summary

Speculative decoding accelerates large language model inference by using a low-cost draft model to propose tokens that the full-size target model verifies in parallel. Parallel and semi-autoregressive (semi- AR) drafters improve drafting efficiency by proposing an entire block in a single forward pass, but training them raises a new difficulty: the draft distribution for a given position depends on where the decoding round starts, and where rounds start depends on how many tokens earlier rounds accepted. Existing training objectives typically rely on block-local surrogates that ignore this cross-round coupling, and therefore do not directly optimize the global decoding efficiency. In this work, we develop a theoretical framework for training and evaluating these drafters by representing speculative decoding as a Markov reward process. This formulation yields the Expected Decoding Rounds (EDR) objective, which weights local rejection costs by state occupancies and exactly equals the expected number of decoding rounds. Unlike prior surrogate objectives, EDR introduces no auxiliary hyperparameters. We then derive an exact temporal-difference gradient that supports unbiased stochastic optimization from target-model rollouts. The same framework also yields an exact offline evaluator for round counts, enabling paired drafter comparisons on shared target rollouts without running speculative decoding. Finetuning two state-of-the- art drafters, DSpark and DFly, with EDR consistently improves mean accepted length and outperforms existing training objectives across nine benchmarks spanning math reasoning, code generation, and chat.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10411v1
