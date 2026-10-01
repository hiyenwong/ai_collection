---
name: frontier-training-safety-cases
category: ai-safety
description: "Use when writing safety cases for frontier RL training runs."
---

# Safety Cases for Frontier AI Training

Methodology from OpenAI (Sep 29, 2026): "Towards safety cases for frontier AI training" (https://openai.com/index/towards-safety-cases-for-frontier-ai-training/). Argument-based safety documentation (as in aviation/nuclear) required *before continuing any frontier RL training run*.

## Core Concept

A **safety case** = comprehensive, structured, evidence-based argument about risk, required before continuing a frontier RL training run. Borrowed from safety-critical industries (aviation, nuclear). Treated as aspirational north star; acknowledged harder for AI due to emergent complexity at each capability level.

## Three Pillars of Technical Safeguards

A safety case must cover the full technical stack with defense in depth:

1. **Alignment** (model shouldn't WANT to take misaligned actions)
2. **Containment** (if it did, breaking out is hard)
3. **Monitoring** (catch it before harm)

### 1. Alignment Training Safeguards
- **Automated dataset reviews**: agents find/fix broken RL environments that could let misaligned trajectories get high reward via exploits (reward hacking prevention at the source)
- **Manual dataset reviews**: human quality checks over datasets to find flawed tasks that reinforce misaligned behavior
- **Grader tuning**: penalize attempts to exploit/hack RL environments during training
- **Prior run analysis**: classifiers over traces from prior experiments to verify graders work as intended
- **Alignment measurement**: evaluations tracking misalignment propensities (measure the effect of interventions)

### 2. Containment
- Restrict what a training run can touch (sandboxing, tool restrictions, network isolation)

### 3. Monitoring
- Runtime detection of misaligned behavior in traces/actions
- Classifier checks for unauthorized behavior + automatic stop

## Governance & Oversight
- Structured documentation must be reviewed *before* the run continues (gate, not afterthought)
- Codify practices into a framework; iterate as internal processes mature
- Focus: frontier RL training specifically — deployment safety requires broader alignment properties

## Why Argument-Based (not Checklist-Based)
- A safety case is an *argument* backed by evidence, not a compliance checkbox list
- Each claim must trace to measurable evidence (evals, analyses, red-team results)
- Emergent complexity at each new capability level means cases must be re-argued per run — past safety doesn't automatically transfer

## Implementation Checklist

- [ ] Enumerate risk claims for the specific run
- [ ] For each claim, attach evidence: alignment evals, containment tests, monitoring coverage
- [ ] Automated RL environment integrity review (reward-hack surface)
- [ ] Manual dataset review pass
- [ ] Grader adversarial-tuning + prior-run trace analysis
- [ ] Governance gate: review before continuing run
- [ ] Independent oversight access

## Related
- `gpt-red-self-play-red-teaming` (alignment/robustness data source)
- `how-we-monitor-internal-coding-agents-misalignment`
- `ai-safety-assessment-framework`
- `requirement-bound-verified-commissioning` (LLM safety-critical commissioning)

**Activation**: safety case, frontier training safety, RL training governance, pre-training safety review, alignment containment monitoring, evidence-based safety argument
