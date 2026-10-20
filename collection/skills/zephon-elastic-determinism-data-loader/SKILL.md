---
name: zephon-elastic-determinism-data-loader
description: "基础模型训练数据管线（在线tokenize/pack/mix、GPU拓扑变化、checkpoint-resume）需要可复现性时用。Zephon弹性确定性：拓扑无关lane划分+排序/计算分离+有界in-flight状态checkpoint，任意GPU数下全局batch序列确定。Activation: deterministic data loading, foundation model training, data pipeline, checkpoint resume, GPU topology, sample packing, online tokenization, shuffle reproducibility, training ablation"
metadata:
  arxiv_id: "2610.03087"
  published: "2026-10-02"
  authors: "Maximilian Böther, Josh Wills, Ties Robroek, Sonnet Xu, Paul Burstein et al. (17 authors)"
  source: "arXiv cs.LG/cs.AI/cs.DB"
  tags: [data-loading, determinism, training-infrastructure, foundation-model]
---

# Zephon: 在线有状态数据管线的弹性确定性

## 核心问题

基础模型 ablation 需要**确定性数据序列**——观测差异必须归因于改动的参数而非数据顺序噪声。但现代管线在线 tokenize/pack/mix 引入有状态 n-to-m 变换，破坏样本索引；GPU 稀缺导致跨 run 拓扑不同；频繁 checkpoint-resume。现有 loader 假设 1-to-1 可索引管线；离线物化昂贵且视频等模态不可行。

## 弹性确定性 (Elastic Determinism)

**定义**：尽管 GPU 拓扑跨 run 改变、频繁 resume、后端不同，全局训练 batch 序列仍确定。

## Zephon 设计

1. **拓扑无关 lane**：全局流划分为 lane，lane→worker 映射随拓扑伸缩但全局顺序不变
2. **排序/计算分离**：顺序决策串行化（便宜、确定），无状态计算在可互换后端并行
3. **有界 in-flight 状态 checkpoint**：只保存有界的在途状态，恢复成本不随训练进度增长

## 结果

文本与视觉-语言负载吞吐量具竞争力，同时提供现有 loader 均不具备的在线有状态管线组合保证。
