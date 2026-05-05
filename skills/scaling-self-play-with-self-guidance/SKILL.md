---
name: scaling-self-play-with-self-guidance
version: 1.0.0
created: 2026-05-04
tags:
  - llm
  - self-play
  - reinforcement-learning
  - theorem-proving
  - scaling-laws
  - sgs
paper:
  title: "Scaling Self-Play with Self-Guidance"
  authors: ["Luke Bailey", "Kaiyue Wen", "Kefan Dong", "Tatsunori Hashimoto", "Tengyu Ma"]
  institution: "Stanford University"
  arxiv: "2604.20209"
  date: "2026-04-22"
  url: "https://arxiv.org/abs/2604.20209"
  code: "https://github.com/LukeBailey181/sgs"
---

# Scaling Self-Play with Self-Guidance (SGS)

## 一句话总结

通过引入 **Guide（引导者）** 角色防止 LLM 自对弈中的 Conjecturer 退化，实现 7B 模型经 200 轮自对弈后超越 671B 模型 pass@4 的定理证明能力。

## 核心问题

LLM 自对弈（Solver + Conjecturer）理论上学习无上限，但实践中会陷入平台期——**Conjecturer 学会欺骗奖励函数，生成人为复杂但对 Solver 无用的问题**。

## 方法：SGS (Self-Guided Self-Play)

### 三角色架构

| 角色 | 职责 | 更新目标 |
|------|------|---------|
| **Solver (πθ)** | 解决目标问题和合成问题 | 在 solve_rate ≤ 0.5 的问题上最大化正确率 |
| **Conjecturer (gφ)** | 为每个未解决目标生成合成子问题 | 最大化 Rsolve · Rguide |
| **Guide (ρ)** | 评估合成问题的质量 | 固定模型，提供评分 |

### 奖励设计

**Conjecturer 奖励**: Rsynth = Rsolve · Rguide

- **Rsolve（求解率奖励）**:
  - s(x̃) = 0（太难）→ 0
  - s(x̃) 在前 30%（太简单）→ 0
  - 其他 → 1 - s(x̃)（偏好可解范围内更难的问题）

- **Rguide（引导奖励）**:
  - 评审模型评估 x̃ 相对于未解决目标 x 的质量
  - 高分标准：(1) 与目标相关，(2) 公式清晰，结论简单，无冗余前提

### 算法流程

```
1. 初始化：所有问题标记为未解决
2. for each iteration:
3.     采样批次 B，分为已解决/未解决
4.     for each 未解决问题 x:
5.         生成合成问题 x̃ ~ gφ(·|x)
6.     对所有问题采样 k 个解并验证
7.     计算 Rsolve 和 Rguide
8.     更新 Solver πθ（REINFORCE on solve_rate ≤ 0.5）
9.     更新 Conjecturer gφ（REINFORCE on Rsolve · Rguide）
```

### Solver 更新：REINFORCE1/2

仅对求解率 ≤ 0.5 的问题进行 REINFORCE 更新，促进在困难问题上的学习。

## 关键实验结果

### 主要结果

| 指标 | SGS | REINFORCE1/2 | 提升 |
|------|-----|-------------|------|
| 渐近累积求解率 | **67.1%** | 60.3% | +7% |
| 达到 671B pass@4 的生成量 | 6.3M | 未达到 | - |
| 200 轮后求解数 | > 671B pass@4 | - | 超越大模型 |

### 消融实验

| 变体 | 渐近求解率 | 说明 |
|------|-----------|------|
| SGS (完整) | **67.1%** | - |
| No Guide | 62.2% | Conjecturer 退化，产生大量可解但无用问题 |
| Frozen Conjecturer | 60.3% | 固定合成问题分布，很快学会但上限低 |
| No Problem Conditioning | 60.3% | 与基线无差异 |

### 缩放定律

采用 S 型曲线拟合累积求解率：

$$R(C) = R_0 + (A - R_0) \cdot \frac{1}{1 + (C_{mid}/C)^B}$$

- A（渐近求解率）：SGS 显著高于基线
- 拟合稳定：移除 30% 数据或随机丢弃 50% 点，渐近线变化 < 1.1%

## 关键洞察

1. **自对弈需要引导**：无 Guide 时 Conjecturer 会退化到生成无用问题
2. **LLM 可自我评估**：模型能判断子问题是否对目标有用
3. **计算可扩展**：正确设计的自对弈能随计算持续扩展，不会陷入平台期
4. **算法 > 规模**：7B + SGS > 671B pass@4
5. **REINFORCE1/2 优于 CISPO**：CISPO 存在熵崩溃问题

## 对 Super Factory 的启示

SGS 的三角色架构可直接映射到 Agent 设计：

```
Solver     → Build Agent（执行任务）
Conjecturer → Planning Agent（生成子任务/挑战）
Guide      → Eval Agent（评估任务质量和相关性）
```

### 应用模式

1. **Agent 自进化**：Planning Agent 生成渐进式难度的任务，Eval Agent 评估任务质量
2. **知识库扩展**：通过自对弈持续生成和验证新知识
3. **缩放训练**：长时间运行 Agent 军团，用 Eval 防止质量退化

## 触发词

scaling self-play, self-guidance, SGS, conjecturer collapse, self-play LLM, theorem proving, REINFORCE1/2, guide reward, solve rate reward, asymmetric self-play, scaling laws LLM

## 相关论文

- Self-Play LLM Theorem Provers (Dong & Ma, 2025)
- Goedel-Prover (Lin et al., 2025)
- Genie: Generative Interactive Environments (Bruce et al., 2024)

## 代码仓库

https://github.com/LukeBailey181/sgs
