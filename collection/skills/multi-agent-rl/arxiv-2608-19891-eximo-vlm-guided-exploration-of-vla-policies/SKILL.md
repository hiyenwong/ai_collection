---
name: arxiv-2608-19891-eximo-vlm-guided-exploration-of-vla-policies
description: 'EXIMO: VLM Guided Exploration of VLA Policies (arXiv: 2608.19891)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# EXIMO: VLM Guided Exploration of VLA Policies

**Authors:** Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch, Markus Wulfmeier, Abbas Abdolmaleki, Martin Riedmiller
**arXiv:** 2608.19891
**Utility:** 1.00
**Published:** 2026-08-20T10:58:45Z
**Link:** http://arxiv.org/abs/2608.19891

## Abstract

How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours of expensive human labour and the alternative, reinforcement learning (RL), can be notoriously sample-inefficient especially for long-horizon tasks. In addition, RL with VLAs imposes several challenges due to the model's size and architectural design. In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies. EXIMO operates in three stages: explore, imitate, and optimize. During the explore phase, EXIMO equips the VLA with a vision language model (VLM) that acts as a planner. The VLM thinks and breaks down challenging long-horizon problems into shorter ones for the VLA. The VLM, together with the VLA, is used to collect an orchestrated dataset on new tasks. During the imitate phase, the VLA is finetuned with the orchestrated data. Finally, during the optimize stage, we use residual off-policy RL to further finetune the policy. In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "EXIMO: VLM Guided Exploration of VLA Policies". 
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

- arXiv:2608.19891
