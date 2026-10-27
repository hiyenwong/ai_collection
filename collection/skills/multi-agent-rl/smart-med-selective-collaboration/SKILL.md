---
name: smart-med-selective-collaboration
description: "SMART-Med: Selective multi-agent medical reasoning via uncertainty-aware routing. Use when building efficient multi-agent medical AI that collaborates only when needed."
version: 1.0.0
author: Hermes Agent
date: 2026-10-27
source: arXiv:2610.33544
tags: [multi-agent-systems, medical-ai, selective-collaboration, uncertainty-routing, privacy, efficient-inference]
category: multi-agent-rl
---

# SMART-Med: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing

## Core Contribution

SMART-Med challenges two assumptions in multi-agent medical AI: (1) always-active dense collaboration, and (2) dependence on large cloud models. Instead, it proposes selective collaboration activated only when needed, with uncertainty-aware routing and privacy-preserving local models.

## Key Insights

- **Assumption 1 Challenged**: Always-on collaboration is inefficient; agents should collaborate selectively
- **Assumption 2 Challenged**: Large cloud models raise privacy/efficiency concerns; smaller local models can work
- **Solution**: Uncertainty-aware routing determines when to activate multi-agent collaboration
- **Benefit**: Maintains performance while improving privacy and efficiency

## Technical Approach

1. **Uncertainty-Aware Routing**: Route cases to single-agent or multi-agent processing based on uncertainty
2. **Selective Collaboration**: Activate multi-agent reasoning only for difficult cases
3. **Local Models**: Use smaller, privacy-preserving models instead of large cloud models
4. **Multimodal Medical Reasoning**: Handle diverse medical data types (images, text, signals)

## Benefits

- **Privacy**: Reduced reliance on cloud models keeps data local
- **Efficiency**: Only use expensive multi-agent collaboration when needed
- **Performance**: Maintains accuracy through intelligent routing
- **Practical Deployment**: More suitable for real clinical environments

## Applications

- Medical AI systems with privacy requirements
- Efficient multi-agent healthcare applications
- Uncertainty-based routing in clinical decision support
- Resource-constrained medical AI deployment

## Activation Triggers

Use this skill when:
- Building multi-agent medical AI systems
- Need privacy-preserving healthcare AI
- Want to optimize collaboration costs in agent systems
- Designing uncertainty-aware routing for multi-agent pipelines

## Related Concepts

- Multi-agent systems
- Medical AI
- Uncertainty quantification
- Privacy-preserving ML
- Selective collaboration

## References

- arXiv:2610.33544
- Categories: cs.AI
