---
name: diffusing-blame-dale-principle-credit-assignment
version: 1.0.0
description: Error Diffusion (ED) methodology for biologically plausible credit assignment under Dale's principle — dual-stream E/I architecture achieving 96.7% MNIST without weight transport, extends to RL with PPO
tags: [biologically-plausible-learning, dale-principle, credit-assignment, error-diffusion, excitatory-inhibitory, dual-stream, reinforcement-learning, no-backprop]
source: arXiv:2606.31700v1
authors: Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, Sebastian Risi, David Ha, Robert Tjarko Lange
date: 2026-06-30
publication: ALIFE 2026
trigger_words: [error-diffusion, dale-principle, credit-assignment, dual-stream, excitatory-inhibitory, biologically-plausible, no-weight-transport, modulo-error-routing, ed-ppo]
---

# Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

## 核心创新

Error Diffusion (ED) 在严格 Dale's principle 约束下的双流 E/I 架构中实现生物合理的信用分配，无需权重传输或随机反馈矩阵。

## 方法论框架

### 1. Dale's Principle 约束
- 每个神经元的突触统一为兴奋性或抑制性
- 需要协调分离的兴奋性和抑制性群体
- 根本性改变学习过程中的信用分配方式

### 2. Error Diffusion 机制
- 全局误差信号路由到所有层
- **无需**: 转置前馈权重
- **无需**: 随机反馈矩阵
- **无需**: 权重传输

### 3. Modulo Error Routing（本文创新）
- 将 Error Diffusion 从二分类扩展到多分类
- 关键技术突破

### 4. 三项领域特定创新
1. **Layer-specific sigmoid widths**: 层级特定的 sigmoid 宽度
2. **Batch-centered class error signals**: 批量居中的类误差信号
3. **Asymmetric initialization**: 非对称初始化

## 实验结果

### 监督学习
| 数据集 | 性能 | 备注 |
|--------|------|------|
| MNIST  | 96.7% | Dale's principle 下 |
| CIFAR-10 | 61.7% | 建立基线 |

### 关键发现
- MNIST 和 CIFAR-10 上三项创新的重要性**反转**
- 揭示单基准评估不可见的任务依赖信用分配瓶颈

### 强化学习
- 与 PPO 集成 → ED-PPO
- 在 Google Brax 连续控制任务上测试
- 在 Craftax 开放式探索任务上测试
- 性能与 Direct Feedback Alignment（无反传基线）相当

## 数学框架

### 双流架构
```
Forward: x → E/I separation → hidden layers → output
Error:   error → routed to all layers via same E/I channels
Update:  local Hebbian-like updates using diffused error
```

### 核心约束
```
对于每个神经元 i:
  if i is excitatory: w_ij ≥ 0 for all j
  if i is inhibitory: w_ij ≤ 0 for all j
```

### 相比其他方法的生物合理性
| 方法 | 权重传输 | 对称连接 | 分离通道 | 减法/逆 |
|------|----------|----------|----------|---------|
| Backprop | ✗ | ✗ | ✗ | ✗ |
| Direct FA | ✓ | ✓ | ✓ | ✓ |
| Error Diffusion | ✓ | ✓ | ✓ | ✓ |

## 任务依赖瓶颈分析

### MNIST vs CIFAR-10
```
MNIST 关键因素:  → 非对称初始化 > sigmoid widths > batch-centered errors
CIFAR-10 关键因素: → batch-centered errors > sigmoid widths > 非对称初始化
```
**教训**: 单一 benchmark 评估会掩盖关键的信用分配机制

## 应用方向

1. **神经形态计算**: 在硬件上实现生物合理学习
2. **RL for Robotics**: 生物合理的强化学习
3. **脑启发AI**: 遵循 Dale's principle 的深度学习
4. **可解释AI**: 理解 E/I 平衡在计算中的角色

## 实现建议

```python
class DualStreamEDNetwork:
    def __init__(self, layers):
        # 分离兴奋性和抑制性群体
        self.exc_neurons = [...]  # all outgoing weights ≥ 0
        self.inh_neurons = [...]  # all outgoing weights ≤ 0
    
    def forward(self, x):
        # 前向传播通过 E/I 分离的层
        pass
    
    def modulo_error_route(self, error):
        # 通过相同活动通道反向路由误差
        # 使用 modulo 操作处理多分类
        pass
    
    def local_update(self):
        # 局部 Hebbian-like 更新
        pass
```

## 核心引用

```bibtex
@inproceedings{yamada2026diffusing,
  title={Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks},
  author={Yamada, Yutaro and Grillotti, Luca and Charakorn, Rujikorn and Risi, Sebastian and Ha, David and Lange, Robert Tjarko},
  booktitle={ALIFE 2026},
  year={2026}
}
```

## 相关技能
- [[chaos-freezing-without-plasticity]]
- [[self-caused-credit-spiking-agency]]
- [[feedback-hebbian-continual-learning]]
