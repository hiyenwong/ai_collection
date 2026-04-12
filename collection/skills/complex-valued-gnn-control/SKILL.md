---
paper: "Complex-Valued GNNs for Distributed Basis-Invariant Control of Planar Systems"
arxiv: 2604.02615
keywords: [complex GNN, phase equivariant, basis invariant, distributed control, GPS-denied]
---

# Complex-Valued GNN Control Skill

## 核心贡献

复数值图神经网络实现分布式基不变控制：
- 复数域几何表示
- 相位等变激活
- 全局基不变性
- GPS 拒绝环境适用

## 技术架构

### 1. 复数表示

```python
z = x + iy  # 位置/速度
z' = z * e^(iθ)  # 基变换（旋转）
```

### 2. 复数值 GNN 层

```python
class ComplexLinear(nn.Module):
    # W = W_real + i*W_imag
    # 输出: (W_r @ x - W_i @ y) + i(W_r @ y + W_i @ x)
```

### 3. 相位等变激活

```python
# f(z*e^(iθ)) = f(z)*e^(iθ)
magnitude = |z|
phase = angle(z)
output = activation(magnitude) * e^(i*phase)
```

## 核心优势

1. **基不变**: 本地基无需全局坐标
2. **分布式**: 每节点独立计算控制
3. **相位等变**: 数学保证基变换不变

## 应用场景

- GPS 拒绝环境多机器人控制
- 无人机集群（无 GPS）
- 室内/地下分布式控制

---

Skill 文件位置: ~/.openclaw/skills/complex-valued-gnn-control/SKILL.md