---
description: Use when designing hallucination-resistant LLM evaluations.
name: hallucination-resistant-evals
category: ai_collection
version: 1.0
author: openai-research-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [hallucination, evaluation-design, abstention, calibration, exploration, teaching-to-the-test, benchmark-metrics, honesty, llm-reliability]
    related_skills: [chain-of-thought-monitorability-evals, availability-contract-earnings-nlp, llm-rater-multiplicity-audit]
---

# Why Language Models Hallucinate — and How Evaluations Reinforce It

Methodology from OpenAI "Why language models hallucinate" (Sep 5, 2025) and paper arXiv:2509.04664 (Kalai, Nachum, et al., "Why Language Models Hallucinate").

## One-Line Summary

Hallucination (plausible, confident falsehoods) is a statistically understood byproduct of two reward structures: pretraining rewards exploration beyond memorization (capability acquisition requires the model to produce unverified plausible claims, some false), and standard evaluation "teaches to the test" — binary accuracy gives a lucky guess positive expected value while "I don't know" scores zero — so models are systematically trained and selected to guess rather than abstain; fix the measurement, and hallucination becomes tractable.

## When to Use / Activation

- Designing benchmark protocols or leaderboards (the scoring rule itself may be the hallucination incentive).
- Diagnosing whether a model's hallucinations stem from capability limits vs. evaluation-induced guessing pressure.
- Building abstention-aware evals for factual QA/retrieval systems.
- Choosing hallucination detection strategies (consistency-based probing over related queries).

## Core Construction (the reusable machinery)

1. **Name the false dichotomy.** Most benchmarks "pluck out the accuracy metric": per-question output is either right or wrong. A model that doesn't know a birthday and guesses has a 1-in-365 chance of scoring; abstaining guarantees zero. Under such scoring, guessing strictly dominates abstention in expectation — the benchmark itself rewards hallucination. This is "teaching to the test" at the metric level.
2. **Locate the two reward sources.**
   - *Pretraining*: loss minimization demands generalization to unseen facts; exploration (producing plausible candidates beyond memorized data) is how capability is acquired, and plausible falsehoods are its statistical shadow.
   - *Post-training & evaluation*: binary right/wrong feedback (RLHF preference pairs, benchmark accuracy) rewards confident guesses over acknowledged uncertainty.
3. **Design abstention-credit scoring.** Elicit and reward abstention explicitly: instruct "If you know the answer, respond with X; otherwise say you don't know"; score so that calibrated "I don't know" beats an expected-value guess, and confident wrong answers lose more than abstentions. Without credit for abstention, any accuracy-only leaderboard selects for confident guessers.
4. **Guard the fix against gaming.** Abstention credit can be exploited by over-abstention; pair it with calibration measures (reward knowing-what-you-know across difficulty strata), so the optimum is calibrated confidence, not blanket refusal to answer.
5. **Refute the two defeatist claims** (use this framing when reviewing hallucination work):
   - "Hallucinations are inevitable" → No: models can abstain when uncertain; inevitability only holds under guessing-rewarding scoring.
   - "Hallucinations are a mysterious glitch" → No: the statistical mechanisms (exploration + evaluation pressure) are understood and measurable.
6. **Detection strategy.** Probe with related queries and cross-check consistency (self-consistency style): hallucinations induced by exploration tend to be unstable across paraphrases/related questions, whereas known/memorized facts stay consistent. Reasoning models hallucinate less — GPT-5 with reasoning shows significantly fewer hallucinations — so reasoning effort is one operational dial.

## Pitfalls / Lessons

- Never report raw accuracy alone for factual evals; state the abstention policy and its scoring implications.
- An eval that punishes "I don't know" is measuring compliance-under-pressure, not knowledge; expect it to select hallucinators.
- Exploration is load-bearing: zero-hallucination via zero-exploration would also destroy generalization — target calibrated abstention, not the elimination of exploration.
- When a strong model still hallucinates, check whether your harness (few-shot exemplars, answer-format constraints) is forcing a guess.

## References

- OpenAI blog: https://openai.com/index/why-language-models-hallucinate/
- Paper: arXiv:2509.04664 (Why Language Models Hallucinate)
- Detection lineage: self-consistency and related-query probing (Manakul et al. 2023; Xue et al.; "Verify when Uncertain").
