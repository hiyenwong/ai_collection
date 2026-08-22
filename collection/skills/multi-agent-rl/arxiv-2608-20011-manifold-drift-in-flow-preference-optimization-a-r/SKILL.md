---
name: arxiv-2608-20011-manifold-drift-in-flow-preference-optimization-a-r
description: 'Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking (arXiv: 2608.20011)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

**Authors:** Yansen Han, Shengyi Liao, Yuanxing Zhang, Pengfei Wan, Tao Lin
**arXiv:** 2608.20011
**Utility:** 1.00
**Published:** 2026-08-20T13:25:24Z
**Link:** http://arxiv.org/abs/2608.20011

## Abstract

Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the pretrained support. We formalize this failure mode as manifold drift. Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a preference update leaves the pretrained manifold whenever its induced terminal displacement has a nonzero normal component. As a remedy, we propose ThermoDPO, a temperature-controlled objective that anchors pairwise preference optimization on preferred samples. Across temperature regimes, this objective connects rejection sampling fine-tuning and FlowDPO and controls a pointwise reconstruction-based surrogate for manifold distance. To counteract diminished signals at low temperatures, we further introduce a weighted variant, ThermoDPO-weighted. On the main toy benchmark, ThermoDPO-weighted attains a StrictScore of 0.899, compared with 0.629 for FlowDPO and 0.857 for FlowDPO+RFT. On SD3.5-M at CFG = 4.5, it improves OCR by 47.5% and the average of four metrics by 16.0%.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking". 
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

- arXiv:2608.20011
