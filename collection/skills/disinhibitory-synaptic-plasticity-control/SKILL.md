---
name: disinhibitory-synaptic-plasticity-control
description: 去抑制神经回路控制突触可塑性符号的框架。通过自顶向下去抑制突触输入编码误差信号，实现误差调制学习的自然涌现。弥合功能性需求与实验观察到的可塑性规则之间的差距。触发词：去抑制、突触可塑性、credit assignment、误差调制、disinhibition、synaptic plasticity、error-modulated learning。
user-invocable: true
---

# Dis-inhibitory Synaptic Plasticity Control - 去抑制突触塑性控制

## 核心思想

通过去抑制神经回路实现信用分配，弥合功能性误差调制与实验观察到的 Hebbian 可塑性规则之间的差距。

**来源：** arXiv:2310.19614v2 (NeurIPS 2023)
**效用：** 0.91

---

## 方法论

### 微电路模型

```python
import torch
import torch.nn as nn

class DisinhibitoryCircuit(nn.Module):
    """去抑制神经回路模型
    
    结构：
    - 兴奋性神经元 (E)
    - 抑制性神经元 (I)
    - VIP 抑制性神经元 (去抑制)
    """
    
    def __init__(self, n_excitatory, n_inhibitory, n_vip):
        super().__init__()
        self.E = nn.Linear(n_excitatory, n_excitatory)  # 兴奋性
        self.I = nn.Linear(n_inhibitory, n_excitatory)  # 抑制性
        self.VIP = nn.Linear(n_vip, n_inhibitory)       # 去抑制 (VIP)
        
    def forward(self, x, topdown_error):
        # 兴奋性活动
        e_activity = torch.relu(self.E(x))
        
        # 去抑制：VIP 抑制 I，从而解除对 E 的抑制
        vip_activity = torch.sigmoid(self.VIP(topdown_error))
        i_activity = torch.relu(self.I(x)) * (1 - vip_activity)
        
        # 净活动
        net_activity = e_activity - i_activity
        return net_activity, e_activity, i_activity
```

### 误差调制学习规则

```python
class ErrorModulatedPlasticity:
    """误差调制的 Hebbian 可塑性规则
    
    Δw = η * (pre * post) * error_sign
    
    关键洞察：
    - 误差编码在去抑制输入中
    - 符号由抑制水平控制
    """
    
    @staticmethod
    def compute_weight_update(
        pre_activity,      # 突触前活动
        post_activity,     # 突触后活动
        inhibition_level,  # 抑制水平
        learning_rate=0.01
    ):
        # 去抑制调制有效学习率
        effective_lr = learning_rate * (1 - inhibition_level)
        
        # Hebbian 乘积
        hebbian_product = pre_activity * post_activity
        
        # 误差调制（通过去抑制实现符号控制）
        error_sign = torch.sign(1 - inhibition_level - 0.5)
        
        # 权重更新
        delta_w = effective_lr * hebbian_product * error_sign
        return delta_w
```

---

## 关键发现

1. **信用分配** - 去抑制电路自然实现误差反向传播
2. **符号控制** - 抑制水平决定突触可塑性符号
3. **生物合理性** - 与实验观察到的可塑性规则一致
4. **性能** - 在非线性可分任务上与 BP 相当

---

## 应用场景

1. 类脑计算芯片设计
2. 神经网络生物合理性改进
3. 信用分配机制研究
4. 神经形态计算

---

## 实验验证

| 条件 | 可塑性 | 符号 |
|------|--------|------|
| 无抑制 | LTP/LTD | Hebbian |
| 强抑制 | 减弱 | 依赖抑制强度 |
| 去抑制 | 调制 | 误差信号控制 |

---

## Activation Keywords
- 去抑制
- 突触可塑性
- credit assignment
- 误差调制
- disinhibition

## Tools Used
- torch
- numpy

## Instructions for Agents
1. 构建去抑制微电路模型
2. 实现误差调制学习规则
3. 验证信用分配功能
4. 与 BP 算法对比性能

## Examples
在多层神经网络中实现去抑制误差调制学习。

## 参考文献
- arXiv:2310.19614v2 (NeurIPS 2023)