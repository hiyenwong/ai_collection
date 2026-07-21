---
name: self-evolving-memory
description: >
  Self-evolving memory architecture for AI agents that learn across interactions without training.
  Use when building agents that need to: (1) accumulate experience across cases, (2) correct
  recurrent reasoning mistakes via reflection, (3) adapt tool-use behavior dynamically. Applicable
  to medical diagnosis, code debugging, customer support, research analysis, and any domain where
  agents solve repeated similar tasks. Trigger: self-evolving memory, inter-case learning,
  agent memory, episodic memory, adaptive heuristics, tool reliability tracking, agent reflection.
---

# Self-Evolving Memory Architecture

Pattern from Evo-MedAgent (arXiv:2604.14475) — a test-time memory module that equips any frozen
LLM agent with inter-case learning capacity, requiring no training.

## Core Architecture

Three complementary memory stores:

### 1. Retrospective Clinical Episodes (RCE)
- Store problem-solving experiences from past cases as structured episodes
- Each episode: {problem_description, solution_path, outcome, key_insights}
- At test time: retrieve top-k similar episodes for the current case
- Similarity: semantic embedding matching on problem description

### 2. Adaptive Procedural Heuristics (APH)
- Priority-tagged diagnostic/decision rules that evolve via reflection
- Format: {rule, priority, confidence, last_updated, source_case}
- After each case: reflect on what worked/didn't, update heuristics
- Rules are sorted by priority; higher confidence = higher priority

### 3. Tool Reliability Controller (TRC)
- Track per-tool trustworthiness scores over time
- Format: {tool_name, success_rate, avg_quality, last_used}
- Dynamically adjust tool selection based on reliability scores
- Decay old scores to adapt to tool updates/changes

## Workflow

### Step 1: Case Processing
```
Input: new problem/case
1. Query RCE for similar past episodes (embedding similarity)
2. Query APH for relevant heuristics (keyword/category match)
3. Query TRC for tool reliability scores
4. Combine retrieved context into augmented prompt
5. Execute agent reasoning with augmented context
```

### Step 2: Post-Case Reflection
```
After case completion:
1. Evaluate outcome (correct/incorrect/partial)
2. If incorrect: analyze failure mode, create new heuristic
3. If correct: reinforce existing heuristics, store episode in RCE
4. Update TRC scores for tools used
5. Prune low-confidence heuristics periodically
```

### Step 3: Memory Maintenance
```
Periodically (every N cases):
1. Cluster similar RCE episodes, merge duplicates
2. Recalculate APH priorities based on aggregate outcomes
3. Decay TRC scores for unused tools
4. Remove heuristics with confidence < threshold
```

## Implementation Notes

- **No training required**: works on top of any frozen model
- **Per-case overhead**: bounded by one retrieval pass + one reflection call
- **Scalability**: use vector database for RCE retrieval at scale
- **Safety**: reflection should validate new heuristics before adding

## Performance Gains (from paper)

| Base Model | Without Memory | With Memory | Improvement |
|-----------|---------------|-------------|-------------|
| GPT-5-mini | 0.68 MCQ acc | 0.79 MCQ acc | +11 points |
| Gemini-3 Flash | 0.76 MCQ acc | 0.87 MCQ acc | +11 points |

## Related Papers

- DeepMedix-R1 (arXiv:2509.03906): RL with grounded rewards for explainable medical reasoning
- Rational QM (arXiv:2510.02877): Finite qubit capacity limits in discretized Hilbert space
