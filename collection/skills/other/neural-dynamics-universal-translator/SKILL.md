---
name: neural-dynamics-universal-translator
description: 神经动力学通用翻译器方法论。在单细胞、单脉冲分辨率下翻译不同神经模型的动力学，实现跨模型动力学对齐。适用于神经元模型转换、动力学分析、计算神经科学。触发词：神经动力学、模型翻译、脉冲分辨率、神经元模型、neural dynamics、universal translator、single-spike。
user-invocable: true
---

# Neural Dynamics Universal Translator - 神经动力学通用翻译器

## 核心思想

构建"通用翻译器"，在单细胞、单脉冲分辨率下对齐不同神经模型的动力学行为。

**来源：** arXiv:2407.14668
**效用：** 0.93

---

## 方法论

### 核心问题

- 神经模型多样性（HH, LIF, Izhikevich等）
- 动力学行为难以跨模型比较
- 缺乏统一的语言描述神经活动

### 翻译框架

```python
import numpy as np
from scipy.optimize import minimize

class NeuralDynamicsTranslator:
    """神经动力学通用翻译器"""
    
    def __init__(self):
        # 支持的模型类型
        self.models = {
            'LIF': self.lif_dynamics,
            'Izhikevich': self.izhikevich_dynamics,
            'HH': self.hh_dynamics
        }
    
    def lif_dynamics(self, params, I):
        """LIF 模型动力学"""
        tau_m, v_thresh, v_reset = params
        v = -65.0
        spikes = []
        dt = 0.1
        
        for t, current in enumerate(I):
            dv = (-(v + 65) + current) / tau_m
            v += dv * dt
            
            if v > v_thresh:
                spikes.append(t * dt)
                v = v_reset
        
        return np.array(spikes)
    
    def izhikevich_dynamics(self, params, I):
        """Izhikevich 模型动力学"""
        a, b, c, d = params
        v = -65.0
        u = b * v
        spikes = []
        dt = 0.1
        
        for t, current in enumerate(I):
            dv = 0.04*v**2 + 5*v + 140 - u + current
            du = a * (b * v - u)
            
            v += dv * dt
            u += du * dt
            
            if v >= 30:
                spikes.append(t * dt)
                v = c
                u += d
        
        return np.array(spikes)
    
    def hh_dynamics(self, params, I):
        """简化 Hodgkin-Huxley 模型"""
        gNa, gK, gL = params
        # 简化实现...
        v = -65.0
        spikes = []
        dt = 0.1
        
        for t, current in enumerate(I):
            # HH 方程简化
            dv = current - 0.1 * (v + 65)
            v += dv * dt
            
            if v > 0:
                spikes.append(t * dt)
                v = -65.0
        
        return np.array(spikes)
    
    def translate(self, source_model, target_model, source_params, input_current):
        """
        翻译动力学：找到目标模型参数使其产生相似的脉冲模式
        
        Parameters:
        -----------
        source_model : str
            源模型名称
        target_model : str
            目标模型名称
        source_params : tuple
            源模型参数
        input_current : np.ndarray
            输入电流
            
        Returns:
        --------
        target_params : tuple
            翻译后的目标模型参数
        """
        # 生成源模型的脉冲模式
        source_spikes = self.models[source_model](source_params, input_current)
        
        # 定义目标函数：最小化脉冲模式差异
        def objective(target_params):
            target_spikes = self.models[target_model](target_params, input_current)
            return self.spike_distance(source_spikes, target_spikes)
        
        # 优化寻找最佳参数
        initial_params = self.get_default_params(target_model)
        result = minimize(objective, initial_params, method='Nelder-Mead')
        
        return result.x
    
    def spike_distance(self, spikes1, spikes2):
        """计算两个脉冲序列的距离"""
        if len(spikes1) == 0 and len(spikes2) == 0:
            return 0.0
        
        # 使用 Victor-Purpura 距离
        # 简化实现
        return abs(len(spikes1) - len(spikes2)) + np.mean(np.abs(np.diff(spikes1) - np.diff(spikes2))) if len(spikes1) > 1 and len(spikes2) > 1 else 100.0
    
    def get_default_params(self, model):
        """获取模型默认参数"""
        defaults = {
            'LIF': (20.0, -50.0, -65.0),
            'Izhikevich': (0.02, 0.2, -65.0, 8.0),
            'HH': (120.0, 36.0, 0.3)
        }
        return defaults.get(model, (1.0,))
```

---

## 应用场景

1. **模型转换：** 将一种神经模型的参数转换为另一种
2. **动力学比较：** 跨模型的动力学行为分析
3. **计算神经科学：** 统一的神经动力学描述

---

## Activation Keywords
- 神经动力学
- 模型翻译
- 单脉冲分辨率
- 神经元模型

## Tools Used
- numpy
- scipy

## Instructions for Agents
1. 理解不同神经模型的动力学
2. 构建脉冲距离度量
3. 通过优化翻译参数

## Examples
将 LIF 模型参数翻译为 Izhikevich 等效参数。

## 参考文献
- arXiv:2407.14668