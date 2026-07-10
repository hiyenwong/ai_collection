---
name: ontology-constrained-llm-hypothesis-scoring
description: 本体约束多 LLM 假设评分方法论。使用专家本体（36 个概念）约束本地多 LLM 理事会，对跨学科文献（如预测编码神经科学）进行假设支持评分，生成可审计的分歧测量和定量假设空间映射。
version: 1.0.0
category: neuroscience
authors:
  - Hamed Nejat
  - Alexander Maier
  - Jesse Spencer-Smith
  - André M. Bastos
arxiv_id: 2606.05206
created: 2026-06-09
activation_keywords:
  - multi-LLM
  - ontology constraint
  - hypothesis scoring
  - predictive coding
  - literature synthesis
  - disagreement measurement
related_skills:
  - kg-research-workflow
  - llm-decision-centric-design
---

# Ontology-Constrained Multi-LLM Hypothesis Scoring

## Overview

本体约束多 LLM 假设评分是一个本地多 LLM 管道，用于跨学科文献综合。通过专家本体约束提示词生成，验证输出，使用多 LLM 理事会评分假设支持，生成可审计的分歧测量和定量假设空间映射。

## Core Methodology

### 1. Predictive Coding Glossary Construction

专家定义的预测编码本体：
- 36 个概念分组为 3 个假设
- Hypothesis 1：Predictive suppression（预测性抑制）
- Hypothesis 2：Feedforward error propagation（前馈误差传播）
- Hypothesis 3：Ubiquity（普适性）

### 2. Multi-LLM Pipeline Architecture

四阶段管道：
```
Stage 1: Read papers → Extract evidence
Stage 2: Incorporate figure descriptions → Assemble prompts
Stage 3: Ontology validation → Glossary compliance check
Stage 4: Multi-LLM council scoring → Agreement/disagreement quantification
```

### 3. Local Multi-LLM Council

使用 10 个本地语言模型：
- 独立评分每个研究对本体概念的同意/不同意
- 分歧来源可追溯（模型偏见、证据解读差异）
- 可审计的评分过程

### 4. Hypothesis-Space Mapping

几何假设空间映射：
- Pairwise study-agreement analysis（成对研究一致性分析）
- Cross-model comparison（跨模型比较）
- Three-dimensional hypothesis space（三维假设空间）

## Key Innovation: Hypothesis-Space Temperature

**定义**：几何离散度度量，衡量研究在假设空间中的紧凑程度
```python
def compute_hypothesis_temperature(study_vectors):
    """计算假设空间温度"""
    # 离散度 = 向量间平均距离
    pairwise_distances = compute_all_distances(study_vectors)
    temperature = np.mean(pairwise_distances)
    return temperature
```

**发现**：
- Local oddball contexts：低温（紧凑聚集）
- Global oddball contexts：高温（分散分布）
- 意义：Global oddball 研究间分歧更大

## Implementation Workflow

### Step 1: Glossary Definition

```yaml
glossary:
  predictive_suppression:
    - error suppression
    - prediction error reduction
    - sensory suppression
  
  feedforward_error_propagation:
    - error signal transmission
    - hierarchical error propagation
    - forward error flow
  
  ubiquity:
    - predictive coding everywhere
    - universal prediction
    - across all brain regions
```

### Step 2: Paper Reading & Evidence Extraction

```python
def extract_evidence_from_paper(pdf_path, glossary):
    """从论文提取证据"""
    # 使用本地 LLM 提取
    evidence = local_llm.extract(
        prompt=f"Extract evidence for concepts: {glossary}",
        document=pdf_path
    )
    return evidence
```

### Step 3: Ontology-Constrained Prompt Assembly

```python
def assemble_constrained_prompt(evidence, figure_desc, glossary):
    """组装约束提示词"""
    prompt = f"""
    Evidence: {evidence}
    Figure Description: {figure_desc}
    
    Score agreement/disagreement with each glossary concept:
    - Use ONLY concepts from approved glossary
    - Score: -1 (disagree), 0 (neutral), +1 (agree)
    - Provide reasoning for each score
    
    Glossary: {glossary}
    """
    return prompt
```

### Step 4: Multi-LLM Council Scoring

```python
def multi_llm_council_score(prompt, n_models=10):
    """多 LLM 理事会评分"""
    scores = []
    for model_id in range(n_models):
        model_output = local_models[model_id].generate(prompt)
        validated_output = validate_against_glossary(
            model_output, glossary
        )
        scores.append(validated_output)
    
    # 计算分歧
    disagreement_matrix = compute_disagreement(scores)
    return scores, disagreement_matrix
```

### Step 5: Hypothesis-Space Mapping

```python
def map_hypothesis_space(all_study_scores):
    """映射假设空间"""
    # 每个研究 → 3D 向量（对应 3 个假设）
    study_vectors = []
    for study in all_study_scores:
        vector = [
            study.score_hypothesis_1,
            study.score_hypothesis_2,
            study.score_hypothesis_3
        ]
        study_vectors.append(vector)
    
    # 可视化
    plot_3d_hypothesis_space(study_vectors)
    return study_vectors
```

## Key Findings

### 1. Structured Disagreement

预测编码文献中的结构化分歧：
- Local oddball paradigms：高一致性
- Global oddball paradigms：显著分歧
- 原因：实验范式差异导致证据解读分歧

### 2. Hypothesis-Space Temperature

温度差异揭示：
- Local oddball：假设空间紧凑（共识高）
- Global oddball：假设空间分散（分歧大）
- 应用：识别需要进一步研究的分歧点

### 3. Cross-Model Comparison

10 个 LLM 模型间比较：
- 模型偏见可识别
- 部分模型倾向严格评分
- 部分模型倾向宽松解读

## Applications

1. 跨学科文献综合：解决碎片化问题
2. 假设验证：定量评估假设支持度
3. 研究缺口识别：高分歧区域指向研究缺口
4. 文献综述自动化：替代传统元分析

## Advantages Over Traditional Meta-Analysis

| Approach | Common Comparison Space | Disagreement Measurement | Interdisciplinary |
|----------|------------------------|-------------------------|-------------------|
| Traditional meta-analysis | Requires | Limited | Difficult |
| **Ontology-constrained multi-LLM** | **Creates** | **Quantitative** | **Facilitated** |

## Limitations

1. 本体依赖：专家本体质量影响结果
2. LLM 偏见：模型训练偏见影响评分
3. 计算成本：多 LLM 理事会计算昂贵
4. 证据遗漏：部分证据可能未提取

## Future Directions

1. 本体自动化：使用 NLP 自动构建本体
2. 模型校准：开发偏见校准方法
3. 扩展应用：应用于其他跨学科领域（量子物理、AI 安全）
4. 实时更新：动态更新假设空间

## Example Use Case: Predictive Coding Neuroscience

预测编码神经科学的碎片化问题：
- 方法：计算理论、电生理、成像、行为、建模
- 传统元分析：无法统一比较
- Ontology-constrained multi-LLM：创建统一假设空间

结果：
- 31 篇研究的假设空间映射
- Local vs Global oddball 的分歧结构
- 识别预测编码假设的关键分歧点

## References

- arXiv:2606.05206
- Friston K. The free-energy principle: a unified brain theory? Nat Rev Neurosci (2010)
- Bastos AM, et al. Canonical microcircuits for predictive coding. Neuron (2012)

## Related Work

- kg-research-workflow：知识图谱研究工作流
- llm-decision-centric-design：决策中心 LLM 设计
- autoresearch：自动化研究循环