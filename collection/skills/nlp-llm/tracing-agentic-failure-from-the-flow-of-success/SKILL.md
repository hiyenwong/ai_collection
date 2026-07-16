---
name: tracing-agentic-failure-from-the-flow-of-success
description: "Tracing Agentic Failure from the Flow of Success - Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debu..."
version: 1.0.0
author: Samuel Yeh, Yiwen Zhu, Shaleen Deep et al.
arxiv_id: 2607.12747
created: 2026-07-14
category: nlp-llm
tags: [cs.AI, cs.CL]
activation_keywords: [tracing, agentic, failure, flow, success, attribution, based, systems, identifying, which]
---

# Tracing Agentic Failure from the Flow of Success

## Overview

Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and trainable without step-level supervision on failure data. To this end, we address unsupervised failure attribution, i.e., training exclusively on successful trajectories and identifying error steps at inference time given a failure trajectory. We propose OAT, which casts this problem as one-class learning with neural controlled differential equations, modeling the dynamical pattern of successful trajectories in latent space. At inference time, each step in a failure trajectory is assigned an anomaly score based on its deviation from the dynamics learned on successful trajectories, which is then used to form a set of error steps. With training on only 100 successful trajectories, experiments show that OAT is 200--5000 $\times$ faster than prompting-based baselines, and, at the same time, consistently outperforms them in both in-domain and out-of-distribution datasets with +20% and +7% F1 scores, respectively, demonstrating that OAT is a promising and efficient direction for diagnosing agentic system failures.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

tracing, agentic, failure, flow, success, attribution, based, systems, identifying, which

---
