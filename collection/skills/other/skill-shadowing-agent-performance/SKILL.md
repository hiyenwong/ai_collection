---
name: skill-shadowing-agent-performance
description: >
  Skill shadowing analysis for LLM agent performance degradation when scaling
  skill libraries. Use when: (1) diagnosing agent performance drops with large
  skill libraries, (2) designing skill selection mechanisms, (3) optimizing
  agent tool-use pipelines, (4) studying context overhead vs selection failure.
  Key finding: skill selection failure (shadowing) is the primary bottleneck,
  not context overhead. Trigger: skill shadowing, agent performance degradation,
  skill library scaling, 技能遮蔽, agent tool selection.
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.24050"
  published: "2026-05-26"
  authors: "Hongwen Song (Vinson)"
  tags: [LLM-agents, skill-libraries, skill-shadowing, context-overhead, agent-performance, library-scaling]
---

# Skill Shadowing and Agent Performance

## Core Finding

**Skill shadowing** is the primary bottleneck when expanding skill libraries:
- Performance degrades up to 21% when scaling from small set to 202-skill library
- Two effects decompose the degradation:
  1. **Skill shadowing**: agent selects wrong skills more often as library grows
  2. **Context overhead**: enlarged context degrades execution (small/indistinguishable)
- Skill shadowing grows with library size; context overhead does NOT

## Practical Implications

### For Skill Library Design
- **Focus on selection, not context**: Optimize skill retrieval/matching
- **Curate aggressively**: Remove overlapping/ambiguous skills
- **Hierarchical organization**: Group related skills to reduce selection space
- **Skill disambiguation**: Clear activation keywords prevent shadowing

### For Agent Architecture
- Two-stage retrieval: coarse filter → fine selection
- Skill embeddings for semantic matching (not keyword-only)
- Confidence thresholds: skip skill loading when no good match
- Skill composition: combine related skills into one

### Quantitative Bounds
- Upper bound on skill shadowing effect grows with library size
- Upper bound on context overhead effect ≈ 0
- Selection failure >> context effects

## Activation Keywords
- skill shadowing
- agent performance degradation
- skill library scaling
- context overhead
- agent tool selection
- 技能遮蔽
- agent 性能退化
