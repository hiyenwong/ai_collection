---
name: arxiv-2610-01161-my-fault-self-diagnosis-as-credit-assignment
description: "Research paper: My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning. Proposes FAULT (Self-Diagnosis-guided Terminal Credit Redistribution) that turns diagnosed errors into explicit step-level credit anchored by terminal outcomes, solving credit assignment in long-horizon agentic RL tasks."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Multi-Agent, Reinforcement-Learning, Credit-Assignment, Agentic-RL, Self-Evolution]
    related_skills: [multi-agent-rl, reinforcement-learning]
---

# My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning

**arXiv ID:** 2610.01161  
**Categories:** cs.CL  
**Utility Score:** 0.85 (High)  
**PDF:** https://arxiv.org/pdf/2610.01161

## Abstract

Agentic reinforcement learning (RL) has emerged as a powerful approach for training large language model agents on multi-step tasks, yet reliance on terminal outcome rewards creates two credit-assignment problems, particularly in long-horizon tasks. First, same-outcome rollout groups provide no learning signal from terminal rewards. Second, terminal rewards provide only trajectory-wide feedback, making it difficult to identify which decisions caused a failure. Recent work supplements terminal rewards with finer-grained information from trajectory analysis, such as natural-language reflections on intermediate decisions and errors. However, natural-language diagnoses are difficult to use directly for credit assignment: their error claims may be unreliable, and they do not quantify how much each error should affect learning. We propose Self-Diagnosis-guided Terminal Credit Redistribution (FAULT), which turns diagnosed errors into explicit step-level credit anchored by terminal outcomes. FAULT checks diagnostic evidence and learns relative error costs from task outcomes. During training, the policy and self-diagnoser co-evolve, while error costs are updated online from recent outcomes. On ALFWorld, FAULT recovers learning signals from same-outcome groups, reaching 95% signal coverage versus 41% for GRPO and 72% for GiGPO, while better localizing credit to specific error steps. Across two model scales, FAULT delivers strong improvements on the long-horizon ALFWorld and WebShop tasks while remaining competitive on short-horizon Search-based QA.

## Key Contributions

1. **Self-Diagnosis-guided Credit Assignment**: Introduces FAULT framework that converts natural-language error diagnoses into quantifiable step-level credit signals
2. **Evidence-Based Diagnostic Verification**: Validates diagnostic claims against task outcomes to ensure reliability
3. **Online Error Cost Learning**: Dynamically learns relative error costs from recent task outcomes during training
4. **Co-Evolution Architecture**: Policy and self-diagnoser evolve together, improving both decision-making and error identification
5. **Same-Outcome Recovery**: Recovers learning signals from rollout groups where traditional methods (GRPO, GiGPO) fail

## Technical Approach

- **Problem**: Terminal rewards in agentic RL provide sparse, trajectory-wide feedback
- **Solution**: FAULT extracts step-level credit from self-diagnosed errors
- **Mechanism**: 
  - Self-diagnoser identifies errors in intermediate decisions
  - Evidence checker validates diagnostic claims against outcomes
  - Error cost learner quantifies impact of each error type
  - Credit redistributor assigns step-level rewards based on verified errors
- **Training**: Policy and diagnoser co-evolve; error costs update online

## Experimental Results

- **ALFWorld**: 95% signal coverage (vs 41% GRPO, 72% GiGPO)
- **WebShop**: Strong improvements on long-horizon tasks
- **Search-based QA**: Competitive on short-horizon tasks
- **Model Scales**: Consistent gains across two model sizes

## Implications for Agent Systems

- **Long-Horizon Tasks**: Critical for complex multi-step agent workflows where terminal rewards are sparse
- **Self-Evolving Agents**: Demonstrates co-evolution of policy and diagnostic capabilities
- **Credit Assignment**: Provides practical solution to one of RL's fundamental challenges in agentic settings
- **Sample Efficiency**: Recovers learning signals from otherwise uninformative rollout groups

## Related Work

- GRPO (Group Relative Policy Optimization)
- GiGPO (Group-in-Group Policy Optimization)
- Self-reflection in LLM agents
- Credit assignment in multi-step RL

## Code & Resources

- Paper: https://arxiv.org/abs/2610.01161
- PDF: https://arxiv.org/pdf/2610.01161
