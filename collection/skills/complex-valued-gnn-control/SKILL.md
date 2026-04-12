---
name: complex-valued-gnn-control
description: Complex-Valued GNNs for distributed basis-invariant control of planar systems in GPS-denied environments
category: robotics
paper: "Complex-Valued GNNs for Distributed Basis-Invariant Control of Planar Systems"
arxiv: 2604.02615
---

# Complex-Valued GNN Control

## Description

复数值图神经网络实现分布式基不变控制，适用于GPS拒绝环境。提供：
- 复数域几何表示
- 相位等变激活
- 全局基不变性保证
- 分布式无人机/多机器人控制

核心优势：基不变性使得本地基无需全局坐标，每个节点独立计算控制，通过相位等变数学保证基变换不变。

## Activation Keywords

- complex GNN
- phase equivariant
- basis invariant
- distributed control
- GPS-denied
- 复数值GNN
- 相位等变
- 无GPS控制

## Tools Used

- read: Read reference implementation code
- write: Save implementation code
- exec: Run Python implementation tests

## Instructions for Agents

When a user asks about complex-valued GNN for distributed control:

1. **Identify the problem**: Determine if the user is working on GPS-denied multi-robot control
2. **Explain the core concepts**: Complex number representation, phase equivariance, basis invariance
3. **Provide code templates**: Use the included Python snippets for implementation
4. **Help with architecture**: Guide on how to integrate into GNN-based control pipelines
5. **Reference the paper**: Cite the arXiv source for deeper understanding

## Examples

### Example: User asks about GPS-denied drone control

```
User: How do I implement distributed control for drones without GPS?
Agent: I'll help you using the Complex-Valued GNN Control skill. This approach uses phase equivariant complex GNNs to achieve basis-invariant distributed control...
```

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
magnitude = abs(z)
phase = angle(z)
output = activation(magnitude) * np.exp(1j * phase)
```

## 核心优势

1. **基不变**: 本地基无需全局坐标
2. **分布式**: 每节点独立计算控制
3. **相位等变**: 数学保证基变换不变

## 应用场景

- GPS 拒绝环境多机器人控制
- 无人机集群（无 GPS）
- 室内/地下分布式控制

## References

Lee, K. (2026). Complex-Valued GNNs for Distributed Basis-Invariant Control of Planar Systems. arXiv:2604.02615 [cs.RO].
