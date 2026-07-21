---
name: local-rl-alignment-engineering
description: 本地基座模型强化学习对齐工程实践 - 涵盖 RLHF/DPO/GRPO 算法选型、显存优化、框架选择、数据工程与全流程实施指南
version: 1.0.0
author: 工程狮5号
license: MIT
metadata:
  hermes:
    tags: [RLHF, DPO, GRPO, PPO, 本地训练, 显存优化, LoRA, QLoRA, 对齐, 强化学习]
    category: ai_collection
---

# 本地基座模型强化学习对齐工程实践

## 何时使用

当需要：
- 在消费级 GPU 或 **Apple Silicon Mac**（M系列）上对齐 7B-14B 模型
- 保护核心数据隐私，避免上传到云端
- 构建垂直领域专用模型（金融、法律、医疗等）
- 探索 GRPO 等轻量化对齐算法

**不要使用**：
- 有充足云端算力且无隐私要求（直接用云端 RLHF 服务）
- 只需简单指令跟随（SFT 足够）
- 无高质量偏好数据集

---

## 核心算法对比

### RLHF (PPO)
- **四模型共存**：Actor + Reference + Reward + Critic
- **优势**：在线采样，能利用环境反馈
- **劣势**：显存爆炸，多卡通信开销大
- **适用**：有充足算力（2x A100 80GB+）

### DPO (直接偏好优化)
- **两模型**：Actor + Reference
- **数学本质**：将 RL 转化为二元分类问题
- **公式**：
  ```
  L_DPO = -E[log σ(β log(π_θ(y_w|x)/π_ref(y_w|x)) - β log(π_θ(y_l|x)/π_ref(y_l|x)))]
  ```
- **适用**：单卡 24GB 训练 7B-14B，有偏好对数据集
- **注意**：对数据分布敏感，噪声数据易过拟合

### GRPO (组相对策略优化)
- **无 Critic 模型**：通过组内比较计算相对奖励
- **优势**：消除 Critic，显存需求降低 25%
- **适用**：数学、代码等可验证任务，能激发 CoT
- **推荐**：本地强化学习的首选算法

---

## 显存占用量化

| 技术 | 7B 模型显存 | 硬件建议 | 场景 |
|------|------------|---------|------|
| 全量微调 | 100-120 GB | 2x A100 80GB | 极高性能要求 |
| LoRA | 16-24 GB | RTX 3090/4090 24GB | 快速实验，单卡 |
| QLoRA (4-bit) | 6-12 GB | RTX 3060 12GB | 显存受限，大模型 |

**关键公式**（7B BF16）：
- 权重：14GB
- AdamW 优化器状态：28GB（一阶+二阶动量）
- 梯度 + 激活值：~20GB
- 总计：>60GB（全量微调）

---

## 框架选型

### LLaMA-Factory
- **优势**：集成度高，支持 100+ 模型，有 LlamaBoard GUI
- **算法**：GaLore, BAdam, DPO 变体（IPO, KTO, ORPO）
- **推荐配置**：14B+ 用 QLoRA + FlashAttention-2

### OpenRLHF
- **优势**：基于 Ray + vLLM，生产级性能
- **核心**：Hybrid Engine Scheduling（组件共享 GPU，休眠机制）
- **能力**：小型集群上运行 70B 全量 RL

### Unsloth
- **优势**：手写 Triton 内核，速度 2x，显存 -70%
- **专长**：GRPO 优化，5-7GB 显存可复现 R1-Zero

---

## 数据工程

### 数据格式

| 类型 | 关键字段 | 用途 |
|------|---------|------|
| 指令数据 | instruction, input, output | SFT 基础能力 |
| 偏好数据 | chosen, rejected | DPO/RM/PPO 对齐 |
| KTO 数据 | response, kto_tag (true/false) | 二进制反馈对齐 |

### 标注陷阱
- **长度偏见**：标注者倾向选择更长回答 → 导致模型输出臃肿
- **防控**：引入多维度评价（Helpfulness, Safety, Conciseness）
- **工具**：Label Studio, Doccano

---

## 实施流程

### Phase 1: SFT 基线
- BF16 精度（稳定性）
- cutoff_len: 2048 或 4098
- **关键**：模型必须先理解对话格式，否则 RL 奖励信号是噪声

### Phase 2: 对齐训练
**PPO 超参数**：
- `pref_beta`: 0.1（KL 散度权重，输出怪异时调高）
- `ppo_buffer_size`: 控制采样/训练比例
- `ppo_epochs`: 过高会导致灾难性遗忘

**GRPO 超参数**（参考 grpo-rl-training skill）：
- `num_generations`: 8-16
- `learning_rate`: 5e-6 ~ 1e-5
- 组合 3-5 个奖励函数

### Phase 3: 评估
- Side-by-Side 对比（GPT-4 裁判）
- MT-Bench 基准测试
- **不要**仅依赖 Loss 下降

---

## 硬件注意事项

### Apple Silicon（MPS / MLX）

在 M 系列 Mac 上训练，优先 MLX 或 PyTorch MPS 后端：

| 框架 | 显存（7B BF16） | M5 Max 128GB 表现 | GRPO 支持 |
|------|----------------|------------------|----------|
| **MLX**（Apple 原生） | ~7 GB | 🔥 最快推理 (~2000 tok/s) | 需手写 REINFORCE | 
| **PyTorch MPS** | ~14 GB + overhead | ✅ 兼容 TRL GRPOTrainer | ✅ 直接支持 |
| **Unsloth**（MPS） | ~5 GB（4-bit） | ⚡ Triton 内核部分支持 | ⚡ 实验性 |
| **llama.cpp + 自定义** | ~4 GB（GGUF Q4） | 🔥 llama.cpp 原生 | 需手写 RL 循环 |

**M5 Max 128GB 推荐配置：**
- 7B 模型→全量 BF16，无需 LoRA，全程 128GB 毫无压力
- 14B 模型→BF16 全量 (~28GB) 也很轻松
- 30B+ 模型→4-bit / LoRA 可行
- **GRPO 首选**：PyTorch MPS + TRL（最快上手），后续可迁移到 MLX

### PCIe 通信瓶颈（仅 NVIDIA 多卡场景）
- 消费级主板无 NVLink → 多卡延迟显著
- DeepSpeed ZeRO-Offload/ZeRO-3 可用系统 RAM/NVMe
- **代价**：ZeRO-3 可能降低训练速度一个数量级

### 推荐配置

| 预算级别 | 硬件 | 可训练模型 | 推荐框架 |
|---------|------|-----------|---------|
| 入门 | RTX 3060 12GB | 7B (QLoRA) | Unsloth |
| 入门 | Mac Mini M4 24GB | 7B (MLX 4-bit) | MLX |
| 主流 | RTX 4090 24GB | 14B (LoRA) | LLaMA-Factory |
| 主流 | MacBook Pro M4 Max 48GB | 7B-14B (BF16) | PyTorch MPS |
| **推荐** | **Mac M5 Max 128GB** | **7B-30B (BF16/4-bit)** | **MLX / PyTorch MPS** |
| 进阶 | 2x 4090 | 30B (QLoRA) | OpenRLHF |

---

## 陷阱清单

1. **SFT 基线不足** → RL 奖励信号变噪声
2. **KL 散度过低** → 策略坍缩，输出怪异
3. **偏好数据噪声** → DPO 过拟合
4. **ZeRO-3 过度使用** → 通信瓶颈导致训练极慢
5. **仅看 Loss** → 忽略真实指令遵循能力
6. **长度偏见数据** → 模型输出臃肿

---

## 参考文献
- DeepSeek R1 技术报告
- OpenRLHF 文档
- Unsloth GRPO 优化指南
- TRL GRPO Trainer 文档
- [`references/hf-model-research.md`](references/hf-model-research.md) — HF API 模型搜索技巧
