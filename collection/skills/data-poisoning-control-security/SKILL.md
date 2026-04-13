---
name: data-poisoning-control-security
description: "Data-driven control has emerged as a powerful paradigm for synthesizing controllers directly from data, bypassing explicit model identification. However, this reliance on data introduces new and large... Activation: control systems, security, edge computing"
---

# Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis

## Overview

Data-driven control has emerged as a powerful paradigm for synthesizing controllers directly from data, bypassing explicit model identification. However, this reliance on data introduces new and largely unexplored vulnerabilities. In this paper, we show that an attacker can systematically poison the data used for control synthesis, causing any linear state-feedback controller synthesized by the planner to destabilize the physical system. Concerningly, we show that the attacker can achieve this objective without knowledge of the system model or the controller synthesis procedure. To this end, we develop a recursive data-poisoning mechanism that generates falsified state trajectories, inducing a precise geometric shift in the apparent system dynamics. More broadly, our results establish that data-driven control pipelines can be deterministically destabilized by model-agnostic attacks operating solely at the data level. Numerical simulations corroborate these findings for both noise-free and noisy data.

## Source Paper

- **Title:** Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis
- **Authors:** Vijayanand Digge, Martina Vanelli, Ahmad W. Al-Dabbagh, Julien M. Hendrickx, Gianluca Bianchin
- **arXiv:** 2604.08392v1
- **Categories:** math.OC
- **Published:** 2026-04-09
- **PDF:** https://arxiv.org/pdf/2604.08392v1

## Core Concepts

- Data-driven methods

## Key Contributions

1. Novel theoretical framework
2. Practical implementation guidelines
3. Experimental validation

## Practical Applications

### Application 1: Research Implementation
```python
# Example implementation based on paper methodology
# See original paper for complete details
def apply_methodology():
    """
    Apply the methodology from the paper.
    """
    # TODO: Implement based on paper specifications
    pass
```

## References

- Vijayanand Digge et al. (2026). "Data Poisoning Attacks Can Systematically Destabilize Data-Driven Control Synthesis." arXiv:2604.08392v1.

## Activation Keywords

- control systems, security, edge computing
- systems engineering
- research paper


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`
