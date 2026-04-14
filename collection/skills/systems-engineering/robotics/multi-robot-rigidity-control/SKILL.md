---
name: multi-robot-rigidity-control
description: Angle-based localization and rigidity maintenance control for multi-robot networks under sensing constraints. Establishes equivalence between angle rigidity and bearing rigidity.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [multi-robot systems, rigidity control, angle-based localization, formation control, sensing constraints]
    source_paper: "Angle-based Localization and Rigidity Maintenance Control for Multi-Robot Networks (arXiv:2604.11754)"
    citations: 0
    category: robotics
---

# 多机器人网络角度刚性控制 (Multi-Robot Rigidity Control)

## 概述
本文研究了在感知约束下的多机器人网络的角度定位与刚性维持控制问题。首次建立了角度刚性与方位刚性之间的等价关系，为基于纯角度测量的机器人编队控制提供了理论基础。

## 核心创新

### 1. 角度-方位刚性等价定理
在2D和3D空间中，当所有机器人的位置不在一条直线上时：
- 角度刚性 ⟺ 方位刚性

这意味着仅使用角度测量即可实现完整的刚性图控制。

### 2. 控制架构
```python
class RigidityController:
    def __init__(self, graph, desired_angles):
        self.G = graph  # 通信图
        self.theta_d = desired_angles  # 期望角度
        
    def compute_control(self, measurements):
        # 计算角度误差
        angle_errors = []
        for (i, j, k) in self.angle_triplets:
            theta_ijk = measurements.get_angle(i, j, k)
            error = theta_ijk - self.theta_d[(i, j, k)]
            angle_errors.append(error)
        
        # 刚性梯度控制律
        control = -self.K_r @ self.rigidity_jacobian().T @ angle_errors
        return control
    
    def check_rigidity(self):
        # 检查图的角度刚性
        return rank(self.angle_rigidity_matrix()) == 2*n - 3
```

### 3. 感知约束处理
- 处理有限视场(FOV)约束
- 处理遮挡和通信中断
- 最小传感器配置要求

## 应用场景
- **无人机编队**: GPS拒止环境下的纯视觉编队
- **水下机器人**: 声学定位受限场景
- **室内移动机器人**: 无全局定位的协作导航

## 数学框架

### 角度刚性矩阵
R_a(θ) ∈ ℝ^{|E_a| × 2n}
其中 E_a 是角度约束集合

### 稳定性条件
系统稳定当且仅当：
```
rank(R_a(θ*)) = 2n - 3
```

## 激活关键词
- 多机器人刚性控制
- 角度定位
- 编队控制
- multi-robot rigidity
- angle-based formation control

## 参考文献
- Presenza, J. F., Colombo, L. J., Giribet, J. I., & Mas, I. (2026). Angle-based Localization and Rigidity Maintenance Control for Multi-Robot Networks. arXiv:2604.11754.
