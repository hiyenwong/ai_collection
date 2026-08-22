---
name: arxiv-2608-20087-towards-professional-tennis-styles-for-humanoid-ro
description: 'Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking (arXiv: 2608.20087)'
category: vision-generative
version: "1.0"
date: 2026-08-22
---

# Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking

**Authors:** Tao Huang, Ruofei Liu, Xuchen Tang, Xinyin Zhang, Junli Ren, Huayi Wang, Feiyu Jia, Yukai Qi, Kangning Yin, Weishuai Zeng, Lipeng Chen, Xi Li, Ting Wu, Kailin Li, Ruoli Dai, Jingbo Wang, Lei Han, Jiangmiao Pang
**arXiv:** 2608.20087
**Utility:** 1.00
**Published:** 2026-08-20T14:19:36Z
**Link:** http://arxiv.org/abs/2608.20087

## Abstract

Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast videos. This hierarchical design is motivated by the key insight that the planner generates stylistic kinematic motions, while the tracker executes them with minimal interference with planning. Despite its effectiveness in simulation, a substantial sim-to-real gap emerges: tracking performance inevitably degrades on real robots, and this degradation is partially overlooked by autoregressive planning and further compounded by noisy perception. To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors. Real-world experiments on the Unitree G1 demonstrate the effectiveness of our adaptation mechanism in bridging the sim-to-real gap. We further deploy AdaPT policies on the full-size Dobot Atom humanoid robot (1.7m) and demonstrate in-the-wild serving without motion capture. Beyond these results, our real-world experiments reveal both algorithmic and engineering insights for future humanoid ball-sports systems. Videos and code are available on our \href{https://humanoidtennis.github.io/AdaPT/}{project website}.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking". 
The paper presents novel ideas in vision-generative that can be applied to agent systems.

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

- arXiv:2608.20087
