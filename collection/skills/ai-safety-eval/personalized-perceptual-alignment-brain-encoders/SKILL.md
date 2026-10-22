---
name: personalized-perceptual-alignment-brain-encoders
description: Use when aligning brain encoders to human perception.
category: ai_collection
metadata:
  arxiv_id: "2610.22569"
  published: "2026-10-15"
  authors: "Daniel Chong, Haomiao Chen, Keith W. Jamison, Raja Marjieh, Ilia Sucholutsky, Nori Jacoby, Amy Kuceyeski (Cornell / Harvard / Purdue)"
  source: "arXiv q-bio.NC"
---

# 个性化知觉对齐的视觉脑编码模型（两级自举框架）

**论文**: "Alignment of visual brain encoding models with individual perceptual similarity judgments" (arXiv:2610.22569; NSD, DreamSim, NRF)

## 核心主张

- **脑准确 ≠ 知觉对齐**：NSD 8 被试上，基线 NRF 编码器对个体知觉相似度的 within-subject 对齐**优于实测 fMRI 本身**（ρ=0.198 vs 0.146, W=0, p=0.008；归因于编码模型的 SNR 增益），且强保留 fMRI 的被试间结构（ρ=0.819）——但**完全不反映知觉判断的被试间结构**（ρ=−0.028, p=0.89）。用 fMRI 精度优化继承的是脑响应的个体差异几何，不是知觉的个体差异几何
- **两级自举**：100 张图的稀疏行为判断（NSD-Meadows 多重排列任务，45 min/人）→ 个性化 DreamSim（冻结骨干 + 每被试特征重加权）→ 为 9K 训练图生成个体相似度监督 → RSA 微调编码器
- 微调阶梯（within-subject 知觉对齐）：基线 0.192 < 群体 DreamSim 微调 0.287 < **个性化 DreamSim 微调 0.377**（两两 Wilcoxon 均显著）；且个性化微调的编码器是唯一恢复**知觉判断被试间结构**的脑编码器（ρ=0.508, p=0.002；10 次 CV 重复 0.38–0.57），代价是失去与 fMRI 被试间结构的对应（群体微调仍保留 fMRI 结构 ρ=0.77）
- 代价-收益：体素预测精度 −9.2%（个性化）/ −7.1%（群体）vs 知觉对齐 +190% / +119%；图像对层面：6.2% 分歧→一致 vs 仅 3.5% 一致→分歧

## 方法骨架

1. **个性化知觉模型**：冻结 DreamSim（1792 维嵌入）；每被试 k 学重加权向量 wk：Sk(i,j) = cos(wk⊙ei, wk⊙ej)。损失 = z-score 归一化后模型/观测相似度的均方差 + λ‖wk−1‖²（λ=1，锚定原群体模型）；全批 Adam lr=0.05 × 100 步；5 折 CV × 10 重复（80 图 3,160 对训练 / 20 图 190 held-out 对评估，无图泄漏）
2. **编码器 RSA 微调**：student 从该被试基线 NRF 编码器初始化 + **冻结 teacher**（同基线）；损失 = λ_teacher·MSE(teacher 体素预测, student 体素预测) + λ_RSA·(1 − r(S_student, S_DreamSim))，λ_teacher=10 ≫ λ_RSA=2；Adam lr=1e-4，≤15 epochs，5 折 × 10
3. **评估**：RSM（体素模式 Pearson / DreamSim cosine / 人判断=取负距离）；within-subject 对齐 = RSM 与人判断 RSM 的 Spearman；被试间结构 = 8×8 被试对相似度矩阵，跨模态比较用 Mantel 式 subject-label 置换检验（10,000 次，处理 28 个被试对的依赖性）

## 实操规则

1. 解码导向的编码模型评估必须报告**知觉对齐**，不能只报体素精度——两者可解离且存在被试依赖的 tradeoff
2. 稀疏行为数据（100 项/人）足以个性化群体相似模型：**特征重加权 + 单位向量正则**；相似度比较前先 z-score 归一化
3. 个体化只能来自个体数据：群体级对齐提升平均对齐，但**永远无法恢复个体特异的被试间结构**（群体微调后仍 ρ=−0.099）
4. teacher 约束权重（10）≫ RSA 项（2）：在保留脑预测的同时重塑表征几何；纯 RSA 微调会丢掉太多体素精度
5. 下游假设：与个体知觉相似度对齐的编码器 → 图像解码/重建更符合**该人**的感知（对齐的意义在解码保真度而非编码精度）
6. 局限：受 DreamSim 代理质量上限约束；更强 VLM 知觉骨干（如更新的人类相似度模型）可直接替换骨干；fMRI 对齐下降是已知 tradeoff 而非缺陷

## 相关

- `lpact-brain-lm-alignment-evaluation` - 锁定式预测-对齐跨模态测试
- `platonic-representations-brain-universal-geometry` - 跨个体普适几何与正交旋转翻译
- `brain-llm-alignment-training-data` - 训练语言主导的脑对齐
- `target-space-recovery-profiles-brain-alignment` - 超越预测精度的目标空间恢复剖面
- `correspondence-score-audit-alignment` - 对应分数三查审计
- `mlm-brain-alignment-task-probing` - 任务条件化对齐探测
