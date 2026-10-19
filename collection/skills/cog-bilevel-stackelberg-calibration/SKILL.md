---
name: cog-bilevel-stackelberg-calibration
description: 把post-hoc校准重构为bilevel Stackelberg联训，零额外参数端到端校准.
category: ai_collection
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks

**arXiv**: 2610.13693 (Oct 2026) | Nektarios Kalampalikis, Pablo M. Olmos, Isabel Valera (Saarland + UC3M)

## When to Use
- 需要训练准确且校准良好的分类器，但不想单独划出校准集/不想加后处理阶段时
- 多任务学习（MTL）需要跨异构任务统一校准，传统 per-task 校准器太繁琐时
- 需要在标准训练循环内用最小改动（只加一个学习率）获得可靠预测概率时
- 对比/替换 temperature scaling、label smoothing、TST 等校准方法时

## 核心发现

**COG（Calibration in One Go）**把 post-hoc 校准重构为 **bilevel Stackelberg 优化**问题，让校准器作为 leader 与主干网络（follower）在同一个训练步内联合更新：
- 不需要单独校准集
- 不需要专门的校准损失（直接用交叉熵）
- 只引入 **1 个额外超参：校准器学习率 λc**（要求 λc < λf）
- 同一 minibatch、单次 forward + 单次 backward——训练开销与标准训练几乎相同

## 方法

### 1. Bilevel 形式化
```
min_{θcal}  E[L_train(c_{θcal}(f_{θtrain}(x)), y)]        (Leader: 校准器)
s.t. θtrain* = argmin_{θtrain} E[L_train(f_{θtrain}(x), y)]  (Follower: 主干)
```
- Post-hoc 校准 = 该问题的解耦近似：先解 follower 再固定它解 leader
- 解耦只在 follower 解唯一时最优；NN 训练有大量等价局部最优，解耦一般不合理——让校准器参与选择学到哪个解

### 2. 高效求解（GDA 风格）
```
θcal^{t+1}   = θcal^t   − λc · ∇_{θcal}  L_train(c(f(x_i)), y_i)
θtrain^{t+1} = θtrain^t − λf · ∇_{θtrain} L_train(c(f(x_i)), y_i)
s.t. λc < λf
```
- 两个目标用**同一损失（CE）、同一 minibatch**——一次前向+一次反向
- λc < λf 保持 Stackelberg 层级（follower 时间尺度快于 leader），保证渐近收敛到局部 Stackelberg 解
- 典型配置：λf=1e-3/5e-4, λc=5e-5~1e-4（比 λf 慢 ~10-100×）

### 3. 变体家族
| 变体 | 额外参数 | 对应 post-hoc 方法 |
------|--------|------------------|
| COG-FC | **0**（最后分类层即校准器） | —— |
| COG-TS | 1 个标量 | Temperature Scaling |
| COG-MS | K×K+K | Matrix Scaling |
| COG-TST | 多个 NN 层 | Two-Stage Training |
| COG+LS | 0 | Label Smoothing 目标替换两级损失 |

**推荐默认 COG-FC**：最后分类层本身充当校准器（依据：内部表征与最后分类层同样有效），零额外参数、开箱即用。

## 实验结果
- ResNet-101 @ SVHN/CIFAR-10/CIFAR-100：COG 变体整体匹配或超越对应 post-hoc 版本；各 COG 变体间差异小→额外校准器复杂度收益有限
- post-hoc Matrix Scaling 在 CIFAR-100 上不收敛，COG-MS 在联训下稳定
- CIFAR-100 top-ranked = COG-FC；OOD/协变量偏移下也稳健，有利于 OOD 检测
- **MTL（CelebA 40 二元属性）**：COG-FC 在 40 任务中的 32 个上胜 Temp. Scaling（80%），全部 40 个上胜 Label Smoothing（100%）；无需 40 个独立校准器
- MTL NLL：COG-FC 0.21 vs Label Smoothing 0.35——LS 在多任务下 NLL 明显变差
- 检查点选择用验证 Brier 分数（比 accuracy 更利于校准）

## 实现要点
```python
# PyTorch 骨架：只需两个参数组
optimizer = torch.optim.AdamW([
    {"params": backbone_params, "lr": 1e-3},   # follower λf
    {"params": fc_layer_params, "lr": 1e-5},   # leader  λc < λf
])
loss = F.cross_entropy(model(x), y)  # 标准循环，无额外损失项
```
- 关键约束只有 λc < λf；两参数组用同一 batch 同一损失
- 兼容任意架构（FC 替换为 TS/MS/TST 校准头即可）

## 可复用模式

1. **两时间尺度 GDA 模式**：任何“后处理/精调阶段”都可尝试改写为 λ_leader < λ_follower 的联训——分离式 pipeline 的耦合替代
2. **解耦损失识别**：凡“先训 A 再固定 A 训 B”的流程，且 A 的解不唯一，都是 bilevel 问题的解耦近似，联训可能更优
3. **零参数校准默认值**：新项目直接用 COG-FC（分类层慢学习率），几乎无成本消除“训完再校准”的 pipeline 复杂度
4. **MTL 免配置校准**：多任务无需 per-task 校准器/正则项，同一机制覆盖异构任务

## 相关技能
- [[confidence-ordering-reversal-contextual-priors]] — 神经解码中的置信度校准
- [[caliber-confidence-calibration]] — 状态依赖的置信度校准

## 标签
calibration, bilevel optimization, Stackelberg game, temperature scaling, label smoothing, multi-task learning, ECE, Brier score, post-hoc calibration
