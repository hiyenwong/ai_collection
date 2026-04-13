---
name: bleg-llm-functions-powerful-fmri
description: "Graph Neural Networks (GNNs) have been widely used in diverse brain network analysis tasks based on preprocessed functional magnetic resonance imaging (fMRI) data. However, their p... Activation: fMRI, graph, neural, network, brain"
---

# BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis

## Overview
Graph Neural Networks (GNNs) have been widely used in diverse brain network analysis tasks based on preprocessed functional magnetic resonance imaging (fMRI) data. However, their performances are constrained due to high feature sparsity and inherent limitations of domain knowledge within uni-modal neurographs. Meanwhile, large language models (LLMs) have demonstrated powerful representation capabilities. Combining LLMs with GNNs presents a promising direction for brain network analysis. While LLMs and MLLMs have emerged in neuroscience, integration of LLMs with graph-based data remains unexplored. In this work, we deal with these issues by incorporating LLM's powerful representation and generalization capabilities. Considering great cost for directly tuning LLMs, we instead function LLM as enhancer to boost GNN's performance on downstream tasks. Our method, namely BLEG, can be divided into three stages. We firstly prompt LLM to get augmented texts for fMRI graph data, then we design a LLM-LM instruction tuning method to get enhanced textual representations at a relatively lower cost. GNN is trained together for coarsened alignment. Finally we finetune an adapter after GNN for given downstream tasks. Alignment loss between LM and GNN logits is designed to further enhance GNN's representation. Extensive experiments on different datasets confirmed BLEG's superiority.

## Source Paper
- **Title:** BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis
- **Authors:** Rui Dong, Zitong Wang, Jiaxing Li, Weihuang Zheng et al.
- **arXiv:** 2604.07361v1
- **Published:** 2026-04-01
- **Categories:** cs.LG
- **PDF:** https://arxiv.org/pdf/2604.07361v1

## Core Concepts

### Key Contributions
- Meanwhile, large language models (LLMs) have demonstrated powerful representation capabilities

### Applications
- Neuroscience research
- Brain network analysis
- Neural signal processing

## Implementation Notes
- Python-based neuroimaging analysis
- Standard preprocessing pipelines

## References
- Rui Dong et al. (2026). "BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis." arXiv:2604.07361v1.

## Activation Keywords
- fMRI
- graph
- neural
- network
- brain
- neuroscience
- brain research


## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
