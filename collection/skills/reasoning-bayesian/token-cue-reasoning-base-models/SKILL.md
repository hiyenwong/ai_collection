---
name: token-cue-reasoning-base-models
description: Use when prompting or evaluating base (non-RL-trained) LLMs, analyzing reasoning behavior, or studying how training data shapes output associations. Token cues at response start (e.g. ".\n\nOkay", "Alright,") unlock base-model reasoning to RL-level accuracy; causal data interventions can create/remove cues.
trigger: base model reasoning, token cues, reasoning elicitation, RL training data attribution, prompt prefix engineering, refusal behavior analysis, Olmo Qwen base models
category: ai_collection
---

# Token Cues: Base Models Can Reason By Taking a Cue From Training Data

**Source**: arXiv:2610.06851v1 (2026-10-05) — Wang, Dravid, Shao, Farhat, Min, Efros (6 authors). Code: github.com/sophicle/cues

## Core Finding

Training data creates associations between the **first tokens of a response** and the reasoning behavior that follows. Fixing particular starting token cues makes a base model competitive with its RL-trained counterpart — no RL needed.

| Cue | Model | Benchmark | Base → Cued |
|---|---|---|---|
| `".\n\nOkay"` | Olmo-3-7B | MATH-500 pass@1 | 42% → **78%** |
| `"Alright,"` | Qwen3-14B | MATH-500 pass@1 | 72% → **87%** |

## Three Mechanistic Results

1. **RL works largely by making cues more likely.** RL-trained models emit these cue tokens more often; forcing base models to emit them recovers much of the RL gain.
2. **Cues are causal, traceable to training data.** Data interventions can turn an arbitrary word (e.g. "chicken") into an effective reasoning cue, or erase an existing cue's effect. "Think duck duck goose" can be made as effective as "Think step by step".
3. **Cues correspond to document types.** Hidden-state representations induced by different cues correlate with distinct document genres in the training set (e.g. reasoning-heavy vs dialogue corpora). Safety behaviors (refusal/compliance) also cue-specific.

## Reusable Patterns

### Pattern 1: Cue-Conditioned Evaluation
When evaluating base models on math/code/reasoning, **fix the starting token** across samples instead of relying on the model's own first-token distribution. This isolates capability from the model's propensity to emit reasoning cues. Report both uncued and cued scores.

### Pattern 2: Cue Search
Enumerate candidate first-token strings (from RL model response openers, training-data genre markers, discourse markers), fix each via constrained decoding, and measure downstream accuracy. High-variance cues reveal latent capability masked by first-token sampling.

### Pattern 3: Causal Cue Attribution
To test whether a training-data patch causes a behavior: edit documents containing the cue-word (add/remove the word in similar contexts), retrain or fine-tune, and measure whether the cue's behavioral effect appears/disappears. Extends to safety: different cues elicit different refusal/compliance patterns tied to different data sources.

## Caveats

- Effect sizes are model- and benchmark-specific; always re-validate cues per model.
- Cuing does not add capability beyond the base model's latent knowledge — it elicits existing reasoning circuits conditioned on training-data associations.

## Related Skills

- `cot-prefix-scoring-pitfall` — CoT prefix scoring methodology
- `reasoning-core-procedural-data-design` — designing reasoning training data
