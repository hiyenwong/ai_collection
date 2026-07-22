---
name: who-grades-the-grader-co-evolving-evaluation-metri
description: "Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents - Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable..."
version: 1.0.0
author: Xing Zhang, Guanghui Wang, Yanwei Cui et al.
arxiv_id: 2607.12790
created: 2026-07-14
category: nlp-llm
tags: [cs.AI, cs.CL, cs.MA]
activation_keywords: [grades, grader, evolving, evaluation, metrics, skills, self, improving, agents, agent]
---

# Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents

## Overview

Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and audited against a held-out anchor it never reads, yielding a transparent, inspectable metric rather than an opaque judge. Second, since no metric exists to beat, the yardstick is recovering what an accurate metric would have enabled, and \emph{Double Ratchet}, our co-evolution of the metric with a lifecycle-managed skill loop, does so: across code generation (MBPP+), enterprise text-to-SQL (Spider~2.0-Snow), and reference-free report generation, it retains 88--110\% of the held-out lift achieved by the same skill loop driven by ground truth or the best available rubric. Third, safety comes from anchor discipline plus outer audits: removing anchor guards collapses the metric into a vacuous detector while removing the lifecycle does not; and when evolved skills gamed the report rubric, an independent judge caught it, one detector repaired it, and a task-aware judge then preferred the evolved outputs over the pre-evolution baseline in 77\% of decided pairs. We argue this failure-expecting architecture is the right default wherever no reliable automatic verifier exists.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

grades, grader, evolving, evaluation, metrics, skills, self, improving, agents, agent

---
