---
name: sex-by-age-brain-connectivity
arxiv_id: 1801.01577v1
utility: 0.88
tags: '[sex differences, brain connectivity, resting-state, age effects, PACE, hierarchical modularity, fMRI]'
created: 2026-03-31
description: "Sex-by-Age Brain Connectivity Analysis"
---

# Sex-by-Age Brain Connectivity Analysis

## Activation Keywords

- 脑连接性别差异
- resting-state sex differences
- 年龄相关脑网络变化
- PACE algorithm
- hierarchical modularity
- functional connectome sex analysis

## Problem Statement

脑连接研究中的性别差异问题：
- 传统研究忽视性别-年龄交互效应
- 负边（anti-correlations）处理不一致
- 缺乏全局概率性分析框架
- 临床症状与连接差异的关系不明

## Method Overview

Zhan et al. (2018) 提出 PACE 算法并研究性别-年龄差异：
1. 概率相关社区估计（PACE）
2. 正负边对偶公式化
3. 年龄分层的性别差异分析
4. 临床症状关联分析

## Tools Used

- `Component` - Analysis component
- `PACE Algorithm` - Analysis component
- `Dual Formulation` - Analysis component
- `F1000/HCP Data` - Analysis component
- `Statistical Testing` - Analysis component

## Key Findings

### Sex-by-Age Interaction

| Age Group | Sex Difference |
|-----------|---------------|
| 22-25 | Non-significant |
| 26-30 | Significant |
| 31-35 | Highly significant |

### Diverging Brain Regions

- Prefrontal cortex
- Temporal lobe
- Amygdala
- Hippocampus
- Inferior parietal lobule
- Posterior cingulate
- Precuneus

### Clinical Correlates

- Inattention symptoms
- Hyperactivity scores
- Anxiety problems
- Depression patterns

## Step-by-Step Instructions

### PACE 算法实现

1. **概率相关社区估计**
   ```python
   import numpy as np
   from scipy import stats
   
   def pace_algorithm(correlation_matrix, n_permutations=1000):
       """PACE: Probability Associated Community Estimation"""
       n = correlation_matrix.shape[0]
       
       # 计算边概率
       edge_probs = np.zeros((n, n))
       
       for _ in range(n_permutations):
           # 随机置换
           permuted = permute_correlations(correlation_matrix)
           
           # 社区检测
           communities = detect_communities(permuted)
           
           # 累积边出现概率
           for i in range(n):
               for j in range(n):
                   if communities[i] == communities[j]:
                       edge_probs[i, j] += 1
       
       return edge_probs / n_permutations
   ```

2. **对偶公式化（正负边）**
   ```python
   def dual_formulation(correlation_matrix):
       """PACE 对偶公式：正边和负边等价处理"""
       # 分离正负相关
       positive_edges = np.maximum(correlation_matrix, 0)
       negative_edges = np.maximum(-correlation_matrix, 0)
       
       # 对偶处理：负边转换为正边
       # 允许一致性的社区结构
       
       # 正边社区
       pos_communities = pace_algorithm(positive_edges)
       
       # 负边社区（转换为正边后等价）
       neg_communities = pace_algorithm(negative_edges)
       
       # 对偶一致性验证
       consistency = np.corrcoef(pos_communities.flatten(), 
                                 neg_communities.flatten())[0, 1]
       
       return pos_communities, neg_communities, consistency
   ```

3. **年龄分层分析**
   ```python
   def age_stratified_sex_analysis(connectivity_data, ages, sex):
       """年龄分层的性别差异分析"""
       age_groups = {
           '22-25': (22, 25),
           '26-30': (26, 30),
           '31-35': (31, 35)
       }
       
       results = {}
       
       for group_name, (age_min, age_max) in age_groups.items():
           mask = (ages >= age_min) & (ages <= age_max)
           group_data = connectivity_data[mask]
           group_sex = sex[mask]
           
           male_data = group_data[group_sex == 'M']
           female_data = group_data[group_sex == 'F']
           
           # t-test for each connection
           t_stats, p_values = stats.ttest_ind(male_data, female_data, axis=0)
           
           # FDR correction
           from statsmodels.stats.multitest import fdrcorrection
           _, p_corrected = fdrcorrection(p_values.flatten())
           
           results[group_name] = {
               't_stats': t_stats,
               'p_values': p_corrected.reshape(t_stats.shape),
               'n_male': len(male_data),
               'n_female': len(female_data)
           }
       
       return results
   ```

4. **临床症状关联**
   ```python
   def clinical_correlates(connectivity_measures, symptoms):
       """连接差异与临床症状的关联"""
       # 症状类型
       symptom_types = ['inattention', 'hyperactivity', 'anxiety']
       
       correlations = {}
       
       for symptom in symptom_types:
           symptom_scores = symptoms[symptom]
           
           # Pearson 相关
           r, p = stats.pearsonr(connectivity_measures, symptom_scores)
           
           correlations[symptom] = {
               'r': r,
               'p': p,
               'significant': p < 0.05
           }
       
       return correlations
   ```

## Example Usage

```python
import numpy as np

# 加载静息态 fMRI 连接数据
connectivity = load_fmri_connectivity()  # shape: (n_subjects, n_regions, n_regions)
ages = load_ages()  # shape: (n_subjects,)
sex = load_sex()  # shape: (n_subjects,)

# 1. PACE 分析
edge_probs = pace_algorithm(connectivity.mean(axis=0))
pos_comm, neg_comm, consistency = dual_formulation(connectivity.mean(axis=0))
print(f"Dual consistency: {consistency:.3f}")

# 2. 年龄分层性别差异
age_results = age_stratified_sex_analysis(connectivity, ages, sex)

for group, result in age_results.items():
    sig_edges = np.sum(result['p_values'] < 0.05)
    print(f"{group}: {sig_edges} significant edges")

# 3. 临床关联
symptoms = load_symptom_scores()
correlations = clinical_correlates(connectivity[:, :10, :10].mean(axis=(1,2)), symptoms)
```

## Paradigm Shift

| Traditional | Basal Configuration Framework |
|-------------|------------------------------|
| Static sex differences | Dynamic sex-by-age configuration |
| Simple concepts | Global probabilistic thinking |
| Ignored age interaction | Age-stratified analysis |
| Separate analysis | Integrated clinical correlates |

## Description

Sex-by-Age Brain Connectivity Analysis

**Key Concepts:**
- 脑连接研究中的性别差异问题：
- 传统研究忽视性别-年龄交互效应
- 负边（anti-correlations）处理不一致
- 缺乏全局概率性分析框架
- 临床症状与连接差异的关系不明

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 概率相关社区估计

### Step 2: 对偶公式化（正负边）

### Step 3: 年龄分层分析

### Step 4: 临床症状关联

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Sex-by-Age Brain Connectivity Analysis to my analysis.

**Agent:** I'll help you apply sex-by-age-brain-connectivity. First, let me understand your specific use case...

**Context:** 脑连接研究中的性别差异问题：
- 传统研究忽视性别-年龄交互效应
- 负边（anti-correlations）处理不一致
- 缺乏全局概率性分析框架
- 临床

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for sex-by-age-brain-connectivity?

**Agent:** Let me search for the latest research and best practices...

## References

- Zhan, L. et al. (2018). Sex-by-age differences in the resting-state brain connectivity. arXiv:1801.01577.

## Related Skills

- time-varying-brain-connectivity
- functional-connectome-fingerprint
- brain-higher-order-structures