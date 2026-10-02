---
name: arxiv-2609-39143-refcon-iterative-refinement-contrastive-memory
description: "Research paper: RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent. Proposes RefCon combining sequential self-refinement with parallel self-contrast to extract higher-quality memories without gold labels. Achieves 21.6% gain on ACE and 16.6% on ReMe, generalizes across model scales and software engineering tasks."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Memory-Extraction, Context-Evolving, Self-Refinement, Contrastive-Learning, Agent-Systems]
    related_skills: [multi-agent-rl, memory]
---

# RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent

**arXiv ID:** 2609.39143  
**Categories:** cs.AI, cs.LG, cs.MA  
**Utility Score:** 0.75 → Promoted (High)  
**PDF:** https://arxiv.org/pdf/2609.39143

## Abstract

Long-horizon agent interactions generate useful but noisy experience, and retraining models to absorb it is expensive. Context-evolving agents therefore need memory extraction methods that improve with more test-time compute without relying on gold labels. We propose RefCon, which combines sequential self-refinement with parallel self-contrast to extract higher-quality memories without gold labels. Evaluated on AppWorld and BFCL-V3 across multiple context-evolving agent frameworks, RefCon delivers strong and consistent gains, including relative improvements of 21.6% on ACE and 16.6% on ReMe over no-scaling baselines, while a diversity-focused variant (DivCon) achieves a 35.5% gain on ReasoningBank. RefCon consistently outperforms existing baselines without ground-truth labels, and generalizes across model scales and to software engineering tasks, where it surpasses even ground-truth baselines. We further analyze the accuracy-token trade-off and scaling behavior, showing RefCon maintains favorable efficiency and continues to improve as more trajectories are used, unlike diversity-only scaling which saturates earlier.

## Key Contributions

1. **RefCon Framework**: Combines sequential self-refinement with parallel self-contrast for memory extraction
2. **No Gold Labels Required**: Extracts high-quality memories without ground-truth annotations
3. **Diversity Variant (DivCon)**: Achieves 35.5% gain on ReasoningBank through diversity-focused scaling
4. **Cross-Domain Generalization**: Works across model scales and software engineering tasks
5. **Scaling Behavior**: Continues improving with more trajectories (unlike diversity-only methods that saturate)

## Technical Approach

### Problem Statement
- **Challenge**: Long-horizon agent interactions generate noisy experience
- **Cost**: Retraining models to absorb experience is expensive
- **Need**: Memory extraction that improves with test-time compute, no gold labels

### RefCon Architecture

#### Sequential Self-Refinement
- Iteratively refines extracted memories
- Each iteration improves quality
- Builds on previous refinements

#### Parallel Self-Contrast
- Generates multiple memory candidates in parallel
- Contrasts candidates to identify high-quality extractions
- Selects best memories based on internal consistency

### DivCon Variant (Diversity-Focused)
- Emphasizes diversity in memory extraction
- Achieves higher gains on reasoning-heavy benchmarks
- Complementary to RefCon's quality focus

## Experimental Results

### Benchmarks
- **AppWorld**: Complex multi-step reasoning environment
- **BFCL-V3**: Berkeley Function Calling Leaderboard v3
- **ACE**: Agent Context Evolution benchmark
- **ReMe**: Reasoning Memory benchmark
- **ReasoningBank**: Reasoning-focused memory retrieval

### Performance Gains
- **ACE**: +21.6% relative improvement over no-scaling baseline
- **ReMe**: +16.6% relative improvement
- **ReasoningBank (DivCon)**: +35.5% gain
- **Software Engineering**: Surpasses even ground-truth baselines

### Generalization
- **Model Scales**: Consistent gains across different model sizes
- **Domains**: Generalizes to software engineering tasks
- **Frameworks**: Works across multiple context-evolving agent frameworks

### Scaling Behavior
- **Accuracy-Token Trade-off**: Maintains favorable efficiency
- **Trajectory Scaling**: Continues improving with more trajectories
- **Saturation**: Unlike diversity-only scaling, RefCon doesn't saturate early

## Implications for Agent Systems

- **Context-Evolving Agents**: Critical for agents that accumulate experience over time
- **Test-Time Compute**: Demonstrates value of investing compute at inference time
- **Memory Quality**: Shows how to extract high-quality memories without labels
- **Scalability**: Method scales effectively with more data and compute
- **Practical Deployment**: No retraining required, works with existing agents

## Comparison with Baselines

### vs. No-Scaling Baselines
- RefCon: +21.6% (ACE), +16.6% (ReMe)
- DivCon: +35.5% (ReasoningBank)

### vs. Ground-Truth Baselines
- Surpasses ground-truth methods on software engineering tasks
- Competitive or better across all benchmarks

### vs. Diversity-Only Scaling
- RefCon continues improving with more trajectories
- Diversity-only methods saturate earlier
- RefCon maintains better accuracy-token efficiency

## Related Work

- Memory-augmented neural networks
- Self-refinement in LLMs
- Contrastive learning methods
- Context-evolving agent architectures
- Test-time compute scaling

## Code & Resources

- Paper: https://arxiv.org/abs/2609.39143
- PDF: https://arxiv.org/pdf/2609.39143
