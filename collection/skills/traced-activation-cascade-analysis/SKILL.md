# TRACED: Activation Cascade Root-Cause Analysis

**Source:** arXiv:2207.07965v1 (July 2022)
**Utility:** 0.90
**Authors:** Qihang Yao et al.
**Conference:** Brain Informatics 2022

---

## Description

TRACED (Topological Root-Cause Analysis of Cascade Differences) identifies
the smallest set of brain connectivity changes that explain observed
activation cascade differences between two groups (e.g., Controls vs MDD).

**Core Insight:** Activation cascade comparison is more insightful than
static network differences for understanding functional impact.

---

## Tools Used

- `numpy` - Graph operations and matrix computations
- `connectome_data` - Structural connectivity matrices (dMRI tractography)
- `linear_threshold_model` - Activation cascade simulation
- `graph_analysis` - Edge weight difference identification

---

## Instructions for Agents

1. **Compute activation cascades** for both groups using Linear Threshold model
2. **Identify cascade differences** - Compare activation patterns between groups
3. **Apply TRACED algorithm** - Find minimal edge weight changes explaining
   differences
4. **Validate root-cause set** - Confirm changes reproduce observed cascade
   differences
5. **Interpret clinical relevance** - Map edges to brain regions and
   functional implications

---

## Examples

### Example 1: MDD vs Healthy Controls

**User:** 如何分析抑郁症患者与健康对照组的脑网络差异？

**Agent:** 使用 TRACED 方法：

1. 对两组分别计算激活级联（刺激各脑区）
2. 识别级联差异（哪些区域激活模式不同）
3. TRACED 找出最小连接变化集合
4. 结果：特定边缘连接权重变化解释了大部分级联差异

**优势：** 比静态网络差异（如 centrality）更能反映功能性影响。

### Example 2: Comparing Treatment Groups

**User:** 治疗前后脑网络有什么功能性变化？

**Agent:** TRACED 分析：

1. 治疗前激活级联
2. 治疗后激活级联
3. 找出哪些连接变化导致了级联模式改变
4. 确定治疗作用的关键路径

---

## Activation Keywords

- 激活级联、activation cascade
- 根因分析、root-cause analysis
- 脑网络差异、connectome comparison
- TRACED、cascade differences
- Linear Threshold model

---

## Key Concepts

### 1. Activation Cascade

Simulated activity propagation after stimulating a source region:
- Uses Linear Threshold model on weighted graph
- Captures functional dynamics of connectome
- More informative than static connectivity measures

### 2. TRACED Algorithm

**Input:**
- Group A activation cascades
- Group B activation cascades
- Connectome graphs for both groups

**Output:**
- Minimal set of edge weight changes explaining cascade differences

**Steps:**
1. For each source region, compute cascade difference
2. Identify edges contributing to differences
3. Greedy selection of minimal explanatory set
4. Validate by simulating modified cascades

### 3. Clinical Application

Applied to Major Depressive Disorder (MDD) vs healthy controls:
- Identified specific connections causing cascade differences
- More insightful than static weight/centrality differences

---

## When to Use

1. **Clinical group comparison** - Disorders vs controls
2. **Treatment effect analysis** - Pre vs post intervention
3. **Functional impact assessment** - Beyond static connectivity
4. **Network perturbation studies** - What changes matter?

---

## Results (Paper)

| Finding | TRACED vs Static Methods |
|---------|--------------------------|
| Explanatory power | Higher (functional dynamics) |
| Minimal changes | Precise set of edges |
| Clinical insight | Better correlation with symptoms |

---

## Limitations

1. Requires accurate connectome data (dMRI tractography)
2. Linear Threshold model assumptions
3. Edge weight changes may not capture all differences
4. Clinical validation needed for each disorder

---

## Related Skills

- `brain-stimulation-dynamics-state` - Stimulation effects on dynamics
- `brain-network-controllability` - Control theory for brain networks
- `ccep-causal-brain-network` - Causal connectivity from stimulation