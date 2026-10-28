---
name: ablation-response-fidelity-behavioral-models
description: Use when validating input ablations of behavioral/cognitive models. Oracle-calibrated response fidelity.
category: ai_collection
metadata:
  arxiv_id: "2609.36097"
  published: "2026-09-28"
  authors: "Hanbo Xie (Georgia Tech)"
  source: "arXiv q-bio.NC"
---

# 消融忠实性：行为模型预测精度 ≠ 机制恢复（Ablation Response Fidelity）

**论文**: "Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice" (arXiv:2609.36097, Hanbo Xie, Georgia Tech)

## 核心发现

对拟合行为模型做输入消融（去掉/替换奖励信息）并解释性能变化为"该信息对行为生成的重要性"——这个推断**不成立**。在已知生成策略的合成序列 bandit 任务中验证：**预测更好的模型，消融响应可以远小于真实生成器；预测更差的简单模型响应反而更忠实**。预测精度与消融忠实性是两个独立成就。

## 三大发现（restless 4臂bandit, w=1 时）

1. **无奖励也能预测好**：choice-only 训练的 GRU/Transformer/LLaMA 全面击败 4 个简单行为基线（臂频率/stay概率/一阶转移矩阵/lag预测器）；LLaMA 无奖励 NLL 0.475 vs uniform 1.386
2. **准确预测器响应远小于生成器**：donor 奖励替换下 oracle 效应 2.067 nats，但 GRU 仅 0.458、Transformer 0.084、LLaMA 0.194——"模型对奖励不敏感"≠"生成行为不依赖奖励"
3. **预测与忠实性排序背离**：w=1 时 RW+softmax 预测最差（NLL 0.556 vs LLaMA 0.392）但响应误差最小（0.407 vs 0.501-0.592）——简单模型不更准，但其概率变化更接近 oracle

**关键反转**：spatial 任务（GP 空间奖励泛化+Manhattan 距离选择核）中 LLaMA 在所有非零权重上预测和响应忠实性**同时**优于 RW（响应误差 0.368 vs 0.487 @ w=1）→ 排序是任务×拟合管线的经验属性，**不存在**"灵活性 vs 忠实性"的必然权衡。

## 方法论框架（可复用的验证协议）

三种必须区分的操作：
- **G = NLL(choice-only) − NLL(full)**：重训练无输入的预测收益 ≠ 因果效应
- **ΔNLL donor replacement**：固定预测器+参与者间奖励序列 derangement 置换（保持奖励观测存在、破坏与本人历史对应；20个固定 donor 分配跨模型族共享；teacher-forced 一步前向评估，非闭环 rollout）
- **响应忠实度 E(p,o)** = E[½·Σₐ|v_p(a) − v_o(a)|]，v = 概率响应向量 p(·|D_πh) − p(·|h)；比较**带符号响应向量**而非聚合 NLL 差（不允许跨动作/试次抵消；非总变差距离，可>1）

**校准流程**（Discussion 给出的 constructive procedure）：
1. 明确区分"重训练无输入"与"扰动已训练预测器"
2. 报告 intact + perturbed 性能绝对值（公共目标），而非只报相对百分比
3. 有受控模拟器时：相同 histories+操作下对比概率响应，配 fitted same-family 参考与 pooled 简单基线
4. 人类生成器未知时合成校准不能证明机制，但能**在应用于人类数据前暴露推断失败**

## 诚实报告的边界（作者明示）

- oracle 定义的是**所选 assay 的可复现响应**，不是活体奖励改变的因果效应（选择序列固定、donor 破坏 action-reward 联合结构）
- RW 高权重响应忠实性可能部分源于其 value-update motif 与生成器结构对齐（结构对齐≠机制恢复）
- LLaMA 仅 1 个 fine-tune seed（4-bit base + rank-8 LoRA, Centaur-style 管线）；模型差异不能归因于架构（预训练/分词/精度/个体校准访问均不同）
- w=0 端点 tie 结构不同，本质更噪；两任务的 w 语义不同（utility 混合 vs 概率混合），不可跨任务比较绝对 NLL

## 应用场景

- 用 Centaur/LLaMA 等行为基础模型做"机制解释"前的**必要校验**
- 任何 input ablation 解释性声明（saliency、removal-based explanation）的行为建模场景
- 认知建模 vs 神经网络之争：本文提供的是评估协议，不站队任何模型类
- "模型不看 X 也预测得好 → 人也不依赖 X" 类推断的通用反例

## 相关 skill

- [[cot-prefix-scoring-pitfall]] — 类似的"评估指标≠机制"诊断框架
- [[llm-self-correction-confidence-signals]] — 模型内部信号验证方法论
- [[naturalistic-computational-cognitive-science]] — 认知模型评估背景
