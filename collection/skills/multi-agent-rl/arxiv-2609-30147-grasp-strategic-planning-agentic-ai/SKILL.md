---
name: arxiv-2609-30147-grasp-strategic-planning-agentic-ai
description: 'Research paper: GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI.'
metadata:
  openclaw:
    emoji: "🎯"
    tags: ["research", "arxiv", "multi-agent-rl", "planning", "agentic", "llm", "strategic-reasoning"]
---

# GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI

**arXiv ID:** 2609.30147
**Authors:** Arunabh Srivastava, Mohammad A. Khojastepour, Srimat Chakradhar, Sennur Ulukus
**Categories:** cs.AI, cs.CL, cs.LG, cs.MA
**Utility Score:** 0.92

## Abstract

Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing GRASP, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within isolated context windows (RevPlan), and independently evaluates trajectories using a multi-criteria discriminator (VerPlan). Empirical evaluations show that GRASP consistently establishes a new state-of-the-art frontier across diverse datasets, yielding substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling (~12.4%↑), ZebraLogic (~30.8%↑), and SciBench Math. Crucially, under multi-task scaling—where standard planners suffer immediate performance collapse—GRASP completely flattens the multi-task degradation penalty. In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7% over direct LLM planners. Furthermore, by isolating context and enforcing strict macro-regularization, GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5%.

## Key Contributions

1. **Multi-Stage Planning Framework**: GRASP decouples planning into three specialized modules (GenPlan, RevPlan, VerPlan) with context isolation
2. **Strategy Exploration**: RevPlan explores alternative localized strategies within isolated context windows before committing
3. **Multi-Criteria Discriminator**: VerPlan independently evaluates plan trajectories using multiple quality criteria
4. **Multi-Task Scaling**: GRASP completely flattens the multi-task degradation penalty that causes standard planners to collapse
5. **State-of-the-Art**: Achieves ~12.4% improvement on Calendar Scheduling, ~30.8% on ZebraLogic, outperforms GPT-5-mini by 14.5%

## Relevance to AI Systems

- **Agentic Planning**: Provides a robust framework for complex multi-step task planning in agentic systems
- **Context Isolation**: Demonstrates that isolating planning stages prevents context contamination
- **Scalability**: Addresses the critical challenge of performance degradation under multi-task scaling
- **Practical Impact**: Directly applicable to real-world agentic planning pipelines requiring strategic reasoning
