---
name: expert-rubric-computer-use-training
description: "Use when training or evaluating computer-use/agents on specialized professional software. Turns real business workflows into RL training tasks via expert-defined fine-grained rubrics, hosted practice environments, and synthetic task generation."
category: ai_collection
license: MIT
source: "OpenAI Research: Advancing computer use with Ironclad (2026-10-06)"
url: https://openai.com/index/advancing-computer-use-with-ironclad/
---

# Expert-Rubric Computer-Use Agent Training

OpenAI × Ironclad methodology for making agents reliably operate specialized business software (contracting, procurement, legal ops). Core loop: **domain experts define tasks + fine-grained success criteria → hosted sandbox for practice → synthetic task generation around representative workflows → RL from rubric-scored feedback**.

## When to use
- Training/evaluating agents that operate real SaaS workflows (multi-step UI work, not single API calls)
- You have (or can recruit) people who know the workflow deeply and can define success
- Partial credit matters: binary pass/fail hides where an agent fails

## Methodology

### 1. Task elicitation with workflow owners
- Partner with people who operate the software daily (Ironclad employees + internal users).
- Identify high-value, multi-step tasks: e.g., configure NDA intake, build procurement approval chains, update a reusable legal clause to reflect a selected jurisdiction.
- Calibrate task difficulty to human time: target tasks an experienced user takes ~30–40 min; these are long enough to require requirement-tracking across screens.

### 2. Fine-grained rubric scoring (the key trick)
- For each task, experts write **8–50 binary criteria** (complexity-scaled) covering every requirement the finished artifact must satisfy — not just endpoint success.
  - Example: "Finance approval configured above threshold" AND "requests below threshold follow the no-approval path" — the second is invisible to endpoint-only scoring.
- Score = fraction of criteria met. This gives partial credit, failure localization, and a dense RL reward signal.

### 3. Hosted practice environments
- The software vendor provides hosted sandbox instances of their product where models can attempt tasks repeatedly without touching real customer data.
- Without a practice environment, RL is impossible; scrape/record-replay harnesses are a fallback when no vendor sandbox exists.

### 4. Synthetic task generation + RL
- Researchers generate **synthetic variations around representative workflows** (different thresholds, jurisdictions, term types) so the model can't memorize one golden path.
- Train with RL where reward = rubric score on synthetic tasks; feedback comes from practice attempts in the sandbox.
- Report both score and estimated time-per-attempt: a model can meet criteria faster (GPT-6 Astra: 55.0% score, 19.2 min vs GPT-5.6 Sol: 41.6%, 37.0 min on 11 Ironclad tasks).

### 5. Failure analysis discipline
- Treat each unmet criterion as a diagnosable failure, not a lost episode.
- Manually review what "meeting the criteria" misses: agents that pass individual steps can still produce a process that fails across the situations it was designed for — evaluate the finished artifact end-to-end.

## Requirements checklist for partners (reusable template)
1. A concrete task example + evidence of where current agents fail
2. Domain experts who can define success criteria and review outputs
3. A secure/hosted environment for practice attempts
4. Data that can be safely used for research and synthetic generation

## Results (reference)
- GPT-6 Astra first frontier model trained on Ironclad tasks: +32% avg score, −48% time/attempt vs GPT-5.6 Sol; internal dev model 63.7%.
- Side-by-side: Astra 94% criteria in ~20 min vs Sol 85% in ~32 min on the same task.

## Pitfalls
- Endpoint-only scoring overestimates agent readiness (misses rule violations mid-workflow)
- Tasks without human-time calibration are either trivial or out of distribution
- Human oversight remains essential: an agent losing track of one business rule halfway through limits what you can delegate; the full platform (controls, review steps) stays in the loop
- Rubric criteria must be written per-situation; a single global checklist doesn't capture jurisdiction-dependent requirements
