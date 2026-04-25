---
name: trajonco-multi-agent-framework-temporal-reasoning
description: "Accurate estimation of cancer risk from longitudinal electronic health records (EHRs) could support earlier detection and improved care, but modeling ... 触发词: 多智能体系统, 控制系统."
---

# TrajOnco: a multi-agent framework for temporal reasoning over longitudinal EHR for multi-cancer early detection

## Overview
Accurate estimation of cancer risk from longitudinal electronic health records (EHRs) could support earlier detection and improved care, but modeling such complex patient trajectories remains challenging. We present TrajOnco, a training-free, multi-agent large language model (LLM) framework designed for scalable multi-cancer early detection. Using a chain-of-agents architecture with long-term memory, TrajOnco performs temporal reasoning over sequential clinical events to generate patient-level summaries, evidence-linked rationales, and predicted risk scores. We evaluated TrajOnco on de-identified Truveta EHR data across 15 cancer types using matched case-control cohorts, predicting risk of cancer diagnosis at 1 year. In zero-shot evaluation, TrajOnco achieved AUROCs of 0.64-0.80, performing comparably to supervised machine learning in a lung cancer benchmark while demonstrating better temporal reasoning than single-agent LLMs. The multi-agent design also enabled effective temporal reasoning with smaller-capacity models such as GPT-4.1-mini. The fidelity of TrajOnco's output was validated through human evaluation. Furthermore, TrajOnco's interpretable reasoning outputs can be aggregated to reveal population-level risk patterns that align with established clinical knowledge. These findings highlight the potential of multi-agent LLMs to execute interpretable temporal reasoning over longitudinal EHRs, advancing both scalable multi-cancer early detection and clinical insight generation.

## Source Paper
- **Title:** TrajOnco: a multi-agent framework for temporal reasoning over longitudinal EHR for multi-cancer early detection
- **Authors:** Sihang Zeng, Young Won Kim, Wilson Lau et al.
- **arXiv:** 2604.10386v1
- **Published:** 2026-04-12

## Core Concepts

1. **多智能体系统**
2. **控制系统**
3. **方法论框架**

## Practical Applications

### 实现框架
```python
class Trajonco_Multi_Agent_Framework_Temporal_Reasoning:
    def __init__(self):
        self.framework = "trajonco-multi-agent-framework-temporal-reasoning"
        self.source = "arXiv:2604.10386v1"
    
    def apply(self, data):
        """
        应用论文中的方法论
        """
        pass
```

## 方法论要点

1. **理论基础**: 基于论文提出的新方法
2. **实现步骤**: 参考论文算法描述
3. **验证方法**: 与论文实验结果对比

## References
- Sihang Zeng et al. (2026). arXiv:2604.10386v1
- PDF: https://arxiv.org/pdf/2604.10386v1

## Activation Keywords
- 多智能体系统, 控制系统, 方法论框架
