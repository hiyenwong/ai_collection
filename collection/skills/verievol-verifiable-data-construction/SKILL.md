---
name: verievol-verifiable-data-construction
description: Verifiable Evol-Instruct framework for scaling multimodal mathematical reasoning. Type-aware evolution + HTV-Agent verifier with offline hypothesis-test falsification ensures reliable reward labels at scale.
trigger_words:
  - verifiable data
  - evol-instruct
  - hypothesis testing
  - multimodal reasoning
  - data verification
version: 1.0
arxiv: 2606.23543v1
authors: Haoling Li, Kai Zheng, Jie Wu, et al.
date: 2026-06-22
categories: cs.AI, cs.CL, cs.CV, cs.LG
---

# VeriEvol: Verifiable Evol-Instruct for Mathematical Reasoning

**Core Insight:** Scaling RL requires verifiable data construction. Decouple prompt difficulty (evolution) from answer reliability (falsification) before policy updates.

## Problem Addressed
- **Reward label reliability decay** as data volume grows
- **Supervision scaling** trusts labeller without verification
- **Policy-side methods** assume answers already correct

## Key Methodology

### Two-Axis Decoupling

1. **Prompt Difficulty Axis**:
   - Type-aware evolution operators
   - Rewrite low-difficulty seeds into harder, image-grounded prompts
   - Route-specific evolution strategies

2. **Answer Reliability Axis**:
   - **HTV-Agent verifier**: Offline hypothesis-test falsification
   - Accept answer only after multi-source counter-evidence fails to refute
   - Never trust labeller blindly

### HTV-Agent Verification Process

```python
def htv_agent_verify(question, proposed_answer, image):
    # Generate counter-evidence from multiple sources
    counter_evidence = []
    
    # Source 1: Mathematical consistency check
    consistency = check_mathematical_consistency(proposed_answer)
    counter_evidence.append(consistency)
    
    # Source 2: Visual grounding verification
    visual_grounding = verify_image_grounding(proposed_answer, image)
    counter_evidence.append(visual_grounding)
    
    # Source 3: Alternative solution derivation
    alternative = derive_alternative_solution(question)
    counter_evidence.append(alternative)
    
    # Hypothesis-test falsification
    if all_falsification_attempts_failed(counter_evidence):
        return ACCEPT_VERIFIED
    else:
        return REJECT_UNVERIFIED
```

## Performance Gains
- Scaling 10K → 250K samples: **35.42 → 54.73** mean accuracy
- Evolved prompts: **+1.82** gain
- HTV-Agent verifier: **+2.06** gain
- Cumulative: **+3.88** over un-evolved RL baseline

## When to Use
- Scaling reinforcement learning datasets
- Multimodal mathematical reasoning
- Visual math benchmarks
- Verifiable reward label construction
- Auditable data pipelines

## Key Insight
**Decouple difficulty from reliability** - evolution expands difficulty, falsification ensures reliability. Both must scale independently.

---

## References
- arXiv: [2606.23543v1](https://arxiv.org/abs/2606.23543v1)
- Authors: Haoling Li, Kai Zheng, et al. (7 authors)
- Categories: cs.AI, cs.CL, cs.CV, cs.LG
- Project: https://flow6d.github.io/
- Release: Full prompts, data, models, code, verifier traces