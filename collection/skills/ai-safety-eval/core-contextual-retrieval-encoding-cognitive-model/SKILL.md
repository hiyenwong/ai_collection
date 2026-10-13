---
name: core-contextual-retrieval-encoding-cognitive-model
description: CORE认知核心模型：层级情景记忆+预测误差+上下文遗忘，45万参数拟合703万选择击败Transformer。Use when建模人类跨范式行为、构建认知架构或心理学统一理论。
category: ai_collection
---

# CORE: Contextual Retrieval and Encoding — 小型认知核心解释大规模人类行为

**论文**: "A small cognitive core explains human behavior at scale" — Marcel Binz, Eric Schulz (Helmholtz Munich / MPI Tübingen), arXiv:2610.13603, cs.LG, 2026-10-09

## 核心洞察

心理学的许多认知原理各自孤立发展，从未检验其**联合解释力**。CORE 把少量成熟原理组装成单一模型，在 137 个实验、7,036,442 个人类选择上联合拟合（MAP 估计），结果：
- 预测 held-out 选择优于同配置 Transformer（PNLL 262,572 vs 329,043），**62/62 研究全胜**
- 优于认知基础模型 Centaur（262,572 vs 389,151），47/62 研究胜
- 模拟行为再现 **75%（50/67）** 原论文报告的行为学效应
- 总参数仅 **452,608**（Centaur 小 5 个数量级）

## 模型架构（全部组件均有认知科学出处）

输入为实验转写的自然语言 transcript（指令、刺激、反馈、被试自己的反应），经 eSpeak 音素化 → 128 维嵌入。核心是 **6 层情景记忆**（每层 4 头独立记忆矩阵 H_t ∈ R^d×d，会话开始时 H_0 = 0）：

**1. 编码（Hebbian 外积 + 上下文学习率）**：
```
H_t = H_{t-1} diag(α_t) + diag(β_t) v_t k_t^T        (Eq.1)
```

**2. 上下文门控**（所有量由当前输入计算）：
```
k_t = φ(W_k x_t)          # key：SiLU + 单位归一化
α_t = σ(W_α x_t)           # 遗忘因子：exp(-a·softplus(z+b))，每特征学习 a>0,b
β_t = σ(W_β x_t)           # 学习率：logistic
q_t = φ(W_q x_t)           # query
```

**3. 检索（经典记忆检索的相似度加权）**：
```
y_t = H_t q_t = Σ_i diag(β_i) v_i (k̄_i^T q_t)      (Eq.3)
k̄_i = diag(α_t)···diag(α_{i+1}) k_i   # 写入后被逐步衰减的 key
```

**4. 预测误差写入（非原始输入）**：
```
v_t = x_t − H_{t-1} diag(α_t) k_t                    (Eq.4)
```
只写"记忆尚未学会的内容"（associative learning theory），释放容量。

**5. 层级堆叠**：x^(l+1) = x^(l) + y^(l)（残差），最终层线性读出 + softmax → 按键概率。模型**除记忆读写外无任何其他计算**。

## 关键设计决策与消融

| 组件 | ΔNLML（去掉的代价） | 认知依据 |
|------|---------------------|----------|
| 层级（6层 vs 1层） | 859,990（最大） | 层级表征 / 新皮层重复局部回路 |
| 遗忘 α_t | 131,706 | 情景记忆衰减 |
| 音素编码（vs BPE） | 110,303 | 言语知觉的音素表征；嵌入参数 11,136 vs 1,750,016，BPE 训练拟合更好但泛化更差 |
| 预测误差（vs Hebbian 写原始输入） | 68,874 | Rescorla-Wagner / predictive coding |

## 潜变量自发涌现经典现象

- **贝叶斯学习特征**：学习率随证据累积而下降（Kalman filter 预言），15/17 实验中成立，89/128 维度平均下降
- **事件分割特征**：记忆时间尺度 τ = −1/log α_t 在一局游戏内增长，在局边界坍塌 80%（17/17 实验），94/128 维度一致 → 事件分段理论（event segmentation）
- 低层学习率中位数 0.44 → 高层 0.17；记忆时间尺度第 1 层 8 token → 第 4 层 43 token：从快局部处理到慢整合处理的层级
- 低层 τ 分布窄而单峰（领域通用），高层宽而多峰（上下文特异）

## 训练要点（可复现路径）

- 数据：Psych-201 的 agentic 重转写版（DeepSeek-V4-Flash 转写 + Claude Fable 5.1 校验），HuggingFace: `marcelbinz/Psych-201-discrete-agentic`
- MAP 拟合：schedule-free AdamW，lr 1e-3，weight decay 0.5（解耦），100 epochs，batch 304,500 tokens，单 H100 24h
- 记忆更新为 chunked Triton kernel（扩展 flash-linear-attention 库），训练时间从 10 天降到 24h
- 评估：NLML 用 Laplace 近似（对角经验 Fisher），PNLL 为 held-out 选择对数概率和
- 行为效应再现：agentic pipeline 为每个实验生成模拟器 + 原文主效应分析脚本；效应计数标准：模拟数据中显著且方向一致
- 探索器：https://core-cognition.github.io/core-model/results/

## 失败模式（诚实边界）

- 语言/社会判断域最弱（7/12）：任务依赖实验室外的世界知识，CORE 只见过实验转写
- 无显式 planning 机制 → model-based planning 特征缺失（two-step task）
- 无长时记忆：实验普遍短于 1 小时，纵向数据才能支撑长期记忆/巩固建模
- 原理可解释 ≠ 计算可解释：key/学习率/遗忘如何计算仍是学习到的变换，未来需替换为独立动机的计算原理

## 何时使用本方法论

- 构建跨范式认知架构、统一行为模型、"小而完整"替代黑箱行为基础模型
- 为 linear attention / fast-weight / Gated Delta Networks 变体寻找认知科学动机（CORE 是其极简认知化版本——只保留记忆读写）
- 设计"联合拟合全部实验记录"的心理学理论检验范式
- 需要可解释潜变量（学习率、记忆时间尺度）做认知神经科学对照分析
