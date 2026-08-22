---
name: arxiv-2608-20123-discrete-diffusion-inference-time-control-with-nes
description: 'Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo (arXiv: 2608.20123)'
category: signal-control-systems
version: "1.0"
date: 2026-08-22
---

# Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo

**Authors:** Lohithsai Yadala Chanchu, Hany Abdulsamad, Christian A. Naesseth
**arXiv:** 2608.20123
**Utility:** 1.00
**Published:** 2026-08-20T14:52:17Z
**Link:** http://arxiv.org/abs/2608.20123

## Abstract

We study inference-time control for text generation in discrete diffusion language models, where the goal is to steer sampling toward sequence-level rewards without retraining. Prior work in this domain has focused on particle-based methods such as best-of-$n$ sampling and bootstrap sequential Monte Carlo, which may suffer from overoptimism and weight degeneracy, respectively. We address these limitations using \emph{nested} sequential Monte Carlo methods. We formulate nested SMC (NSMC) and fully-adapted nested SMC (FA-NSMC) for Feynman--Kac steering, identifying and correcting errors in prior formulations that lead to biased final estimates. We evaluate these methods on toxicity and fluency steering tasks, showing that NSMC and FA-NSMC consistently outperform best-of-$n$ and bootstrap SMC.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo". 
The paper presents novel ideas in signal-control-systems that can be applied to agent systems.

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

- arXiv:2608.20123
