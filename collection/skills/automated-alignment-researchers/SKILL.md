---
name: automated-alignment-researchers
description: Automated Alignment Researchers (AARs) methodology — using LLMs to autonomously discover alignment improvements. Multi-parallel agent setup for weak-to-strong supervision research: agents propose, test, and analyze alignment ideas independently, sharing findings on a shared forum. Use when: automating alignment research, weak-to-strong generalization, scalable oversight, multi-agent research systems, AI-assisted alignment, or designing autonomous research workflows.
---

# Automated Alignment Researchers (AARs)

Use LLMs as autonomous researchers to discover and test alignment improvements.

## Problem: Weak-to-Strong Supervision

- **Strong model** = potentially capable base model needing fine-tuning
- **Weak teacher** = much weaker model providing supervision signals
- **PGR (Performance Gap Recovered)**: 0 = no improvement over weak teacher, 1 = matches optimal strong model
- **Proxy for scalable oversight**: weak model stands in for humans, strong model for superhuman AI

## Architecture

Each AAR receives:
1. **Sandbox** — isolated environment to work and think
2. **Shared forum** — circulate findings with other AARs
3. **Storage system** — upload code and artifacts
4. **Scoring server** — receive PGR scores for experiments
5. **Background knowledge** — model training and inference concepts

## Key Design Patterns

### 1. Diverse Starting Points
- Give each AAR a different (intentionally ambiguous) starting direction
- Examples: one focuses on interpretability, another on data reweighting
- Without diversity, AARs converge on similar ideas, making less progress

### 2. Minimal Structure
- Too much structure ("propose → plan → code → test") hurts progress badly
- Let AARs autonomously decide their research workflow
- They should propose, experiment, analyze, and share findings independently

### 3. Cross-AAR Knowledge Sharing
- AARs share code and findings on the shared forum
- This enables building on each other's discoveries
- Prevents redundant exploration

## Results

- 9 parallel AARs achieved PGR of 0.97 after 800 cumulative hours (~$18,000)
- Human baseline: PGR of 0.23 after 7 days of work
- AAR methods generalized to held-out math (PGR 0.94) and coding (PGR 0.47) datasets
- **Cost**: ~$22 per AAR-hour

## Limitations

- AAR methods may capitalize on model/dataset-specific opportunities
- Production-scale testing showed limited success (may reflect trial limitations)
- Generalization isn't guaranteed — always test on held-out domains

## Recommendations

1. Allow AARs to test against multiple domains during research
2. Stress-test AAR discoveries on held-out datasets before claiming generalization
3. Avoid prescribing specific workflows — give direction but maintain autonomy
4. Start diverse, converge naturally
