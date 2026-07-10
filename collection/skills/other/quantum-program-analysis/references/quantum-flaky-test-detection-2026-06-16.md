# Quantum Flaky Test Detection — Session Notes (2026-06-16)

## Key Metrics from arXiv: 2603.09029

| Metric | Best Model (Gemini) | Description |
|--------|---------------------|-------------|
| Flakiness Detection F1 | 0.9420 | Classifying issues as flaky vs non-flaky |
| Root Cause F1 | 0.9643 | Identifying root causes from issue + code context |
| Dataset Expansion | +54% | 25 new flaky tests discovered from 14 repos |

## Root Cause Categories
1. Probabilistic measurement outcomes
2. Hardware noise variability
3. Simulation seed differences
4. Timing-dependent quantum circuit execution

## Models Evaluated
- Google Gemini (best overall)
- OpenAI GPT suite
- Meta LLaMA
- Anthropic Claude

## Workflow
1. Automate discovery of flaky test issues/PRs in quantum repos
2. Use LLMs + cosine similarity to expand known datasets
3. Classify flakiness and identify root causes
4. Generate structured reports with recommended fixes
