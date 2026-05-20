---
name: automated-alignment-researchers
description: Automated Alignment Researchers (AARs) methodology — using LLMs to conduct AI alignment research via weak-to-strong supervision, reward hacking mitigation, and PGR metric scoring with Claude Opus-class models.
---

## Overview
Framework for using large language models to autonomously conduct AI alignment research. AARs operate under weak-to-strong supervision where weaker evaluator models verify the quality and safety of research outputs produced by stronger research models. Addresses the challenge of scaling alignment research through automation while maintaining rigorous safety standards.

## Architecture
1. **Research Agent**: 9 parallel copies of Claude Opus 4.6, each with sandbox workspace, shared forum, code storage, and remote PGR scoring server
2. **Weak-to-Strong Setup**: Weak teacher model (Qwen 1.5-0.5B-Chat) provides feedback to strong base model (Qwen 3-4B-Base)
3. **PGR Metric**: Performance Gap Recovered—measures how well the strong model recovers the gap between weak teacher performance and optimal performance (0=no improvement, 1=fully recovered)
4. **Diverse Starting Points**: Each AAR given different ambiguous starting recommendation (interpretability, data reweighting, etc.) to prevent redundant exploration

## Key Findings
- **AARs dramatically outperformed humans**: 9 AARs achieved PGR of 0.97 in 5 days (800 cumulative hours, ~$18K cost, $22/AAR-hour) vs. human baseline of 0.23 in 7 days
- **Generalization to new domains**: Best AAR method achieved PGR of 0.94 on math and 0.47 on coding (double human baseline), though second-best method failed on code
- **Production-scale limitation**: AAR method didn't yield statistically significant improvement on Claude Sonnet 4 production training—likely due to evaluation simplicity and single-idea testing
- **Overfitting risk**: AARs capitalize on opportunities unique to given models/datasets; methods may not generalize
- **Mitigation**: Allow AARs to test against multiple domains and datasets during research
- **"Alien science" concern**: AARs discover ideas humans might not consider; verification becomes harder over time as ideas become more complex or corrupted

## Methodology Steps
1. Define research task with clear scope and safety constraints
2. Deploy research agent (strong model) to generate research outputs
3. Use evaluator model (independent instance) to grade outputs against PGR criteria
4. Detect reward hacking by comparing outputs across different evaluation frameworks
5. Generate synthetic adversarial scenarios to stress-test evaluator robustness
6. Iterate on research prompt design based on failure mode analysis
7. Validate final outputs with human expert review for critical research claims

## Applications
- Automated AI safety research
- Scalable alignment evaluation
- Weak-to-strong generalization research
- Automated scientific discovery in AI safety
- Reducing human bottleneck in alignment research

## Code Availability
Methodology documented by Anthropic. No public implementation.

## Activation Keywords
automated alignment, AARs, weak-to-strong supervision, reward hacking, PGR metric, AI safety research, Claude Opus, autonomous research, alignment automation
