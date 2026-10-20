---
name: page-entrokv-gqa-kv-eviction
description: "GQA模型长上下文KV-cache驱逐策略设计时用。Page-EntroKV：按物理KV组(而非per-head)打分，sink隔离Rényi-2熵池化头权重+PagedAttention页对齐，预算保持与needle召回可证。Activation: KV cache eviction, grouped-query attention, GQA serving, PagedAttention, long context, token importance, retrieval head, sink head, cache budget"
metadata:
  arxiv_id: "2610.03135"
  published: "2026-10-02"
  authors: "Inbasekaran S"
  source: "arXiv cs.LG"
  tags: [kv-cache, gqa, inference-efficiency, long-context, attention]
---

# Page-EntroKV: GQA 对齐的熵加权 KV-Cache 驱逐

## 核心问题

GQA 下多个 query head 共享一个物理 KV buffer，per-head 独立驱逐策略失配：

1. **Union 开销**：各 head 独立选 token → serving 引擎被迫保留并集，cache 膨胀最高至组比率 r（形式化为 union overhead ratio, UOR）
2. **均值池化缺陷**：算术平均稀释了承载事实记忆的专化 retrieval head；sink head 会伪装成 retrieval head

## Page-EntroKV 方法

在 GQA 实际分配的粒度上驱逐——硬件元组 (layer, group, page)：

1. **组内池化**：组内 head 以 sink 隔离的 collision（Rényi-2）熵导出权重池化——每 head 一次内积，prefill 时算一次，无需校准
2. **Sink 隔离**：防止 sink head 被误判为 retrieval head
3. **页对齐**：池化分数投影到 PagedAttention page frame，驱逐按页执行

## 理论保证

- 两 head 组的 UOR 与组内分歧的精确恒等式 + 任意组比率的双侧界
- 严格预算保持 + 有限上下文 needle 保留界（算术均值池化可证违反）
- 精确的每层页核算

## 结果（Qwen2.5-1.5B-Instruct, r=6, 2240 组测量）

- head 独立重放 UOR 高达 4.75x（2% 预算）→ Page-EntroKV 恒为 1.000
- sink 伪装消除 13x；20% 预算下 needle 召回 100%（均值池化 0%）
- 20% 保留率下 QA 与代码任务仍可解
