---
name: llm-binary-deobfuscation
description: "Deobfuscating binary code remains a fundamental challenge in reverse engineering, as obfuscation is widely used to hinder analysis and conceal program logic. Although large language models (LLMs) have... Activation: LLM, reverse engineering"
---

# Can LLMs Deobfuscate Binary Code? A Systematic Analysis of Large Language Models into Pseudocode Deobfuscation

## Overview

Deobfuscating binary code remains a fundamental challenge in reverse engineering, as obfuscation is widely used to hinder analysis and conceal program logic. Although large language models (LLMs) have shown promise in recovering semantics from obfuscated binaries, a systematic evaluation of their effectiveness is still lacking. In this work, we present BinDeObfBench, the first comprehensive benchmark for assessing LLM-based binary deobfuscation across diverse transformations spanning pre-compilation, compile-time, and post-compilation stages. Our evaluation shows that deobfuscation performance depends more on reasoning capability and domain expertise than on model scale, and that task-specific supervised fine-tuning consistently outperforms broad domain pre-training. Reasoning models can maintain robustness under severe obfuscation, generalize across different instruction set architectures (ISAs) and optimization levels. In-context learning benefits standard models but yields limited gains for reasoning models. Overall, our study highlights the importance of task-specific fine-tuning and reasoning-driven strategies, and positions BinDeObfBench as a basis for future work in binary deobfuscation.

## Source Paper

- **Title:** Can LLMs Deobfuscate Binary Code? A Systematic Analysis of Large Language Models into Pseudocode Deobfuscation
- **Authors:** Li Hu, Xiuwei Shang, Jieke Shi, Shaoyin Cheng, Junqi Zhang, Gangyang Li, Zhou Yang, Weiming Zhang, David Lo
- **arXiv:** 2604.08083v1
- **Categories:** cs.SE
- **Published:** 2026-04-09
- **PDF:** https://arxiv.org/pdf/2604.08083v1

## Core Concepts

- Robust control

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

- Li Hu et al. (2026). "Can LLMs Deobfuscate Binary Code? A Systematic Analysis of Large Language Models into Pseudocode Deobfuscation." arXiv:2604.08083v1.

## Activation Keywords

- LLM, reverse engineering
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
