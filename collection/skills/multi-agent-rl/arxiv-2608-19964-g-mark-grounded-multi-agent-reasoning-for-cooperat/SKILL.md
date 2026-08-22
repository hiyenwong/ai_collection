---
name: arxiv-2608-19964-g-mark-grounded-multi-agent-reasoning-for-cooperat
description: 'G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs (arXiv: 2608.19964)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs

**Authors:** Bhavya Gupta, Onat Gungor, Tajana Rosing
**arXiv:** 2608.19964
**Utility:** 1.00
**Published:** 2026-08-20T12:35:12Z
**Link:** http://arxiv.org/abs/2608.19964

## Abstract

Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects downstream decisions. We propose G-MARK, a grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs (KGs). The resulting KGs preserve object hypotheses together with their source attribution, ego-versus-partner visibility, uncertainty, conflicts, spatial relations, and planning-relevant context. G-MARK then derives a shared feature representation from these KGs, enabling lightweight task heads to support object reasoning, motion prediction, control selection, and trajectory forecasting. Compared with the state-of-the-art baseline, GMARK improves occlusion reasoning accuracy by 42.2%, reduces control-selection error by 13.1%, and achieves comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload. Our code is available at https://github.com/bhavyagupta98/g-mark.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19964
