---
name: complex-valued-gnn-control
description: "Complex-Valued GNN Control - 复数值图神经网络用于分布式基不变控制系统。核心技术：复数域几何表示、相位等变激活、全局基不变性。适用于GPS拒绝环境分布式控制。激活词：complex GNN, 复数值 GNN, basis invariant, 基不变控制."
---

# Complex-Valued GNN Control Skill

复数值图神经网络实现分布式基不变控制系统。

## 核心来源

**论文**: "Complex-Valued GNNs for Distributed Basis-Invariant Control of Planar Systems"
- **arxiv**: 2604.02615
- **关键贡献**: 全局基不变的 GNN 参数化

## 核心问题

**传统分布式 GNN 控制问题**:
- 所有节点需在兼容基中收集几何观测
- GPS 拒绝环境 → 无全局坐标
- 指南针拒绝 → 无全局方向参考

**解决方案**: 
复数值表示 + 相位等变架构 → 全局基不变性

## 技术架构

### 1. 复数域几何表示

**2D 几何特征 → 复数**:
```python
# 平面位置/速度 → 复数
z = x + iy  # 位置
v = v_x + i*v_y  # 速度

# 基变换 → 相位旋转
z' = z * e^(iθ)  # 旋转角度θ
```

**关键洞察**:
- 不同基选择 = 不同相位旋转
- 相位等变 = 基变换不变

### 2. 复数值 GNN 层

**架构设计**:
```python
import torch
import torch.nn as nn

class ComplexLinear(nn.Module):
    """复数值线性层"""
    
    def __init__(self, in_features, out_features):
        super().__init__()
        # 复权重: W = W_real + i*W_imag
        self.W_real = nn.Parameter(torch.randn(out_features, in_features))
        self.W_imag = nn.Parameter(torch.randn(out_features, in_features))
    
    def forward(self, z):
        """
        输入: z (complex tensor)
        输出: W @ z (complex)
        
        数学: (W_r + i*W_i) @ (x + iy)
            = W_r @ x - W_i @ y + i(W_r @ y + W_i @ x)
        """
        x, y = z.real, z.imag
        
        out_real = torch.matmul(self.W_real, x) - torch.matmul(self.W_imag, y)
        out_imag = torch.matmul(self.W_real, y) + torch.matmul(self.W_imag, x)
        
        return torch.complex(out_real, out_imag)


class PhaseEquivariantActivation(nn.Module):
    """相位等变激活函数"""
    
    def __init__(self):
        super().__init__()
        # 激活作用于模，保持相位
        self.activation = nn.ReLU()
    
    def forward(self, z):
        """
        相位等变: f(z*e^(iθ)) = f(z)*e^(iθ)
        
        实现: 对模激活，保持相位不变
        """
        magnitude = torch.abs(z)
        phase = torch.angle(z)
        
        # 激活模
        activated_mag = self.activation(magnitude)
        
        # 重构复数
        return activated_mag * torch.exp(1j * phase)


class ComplexGNNLayer(nn.Module):
    """复数值 GNN 层"""
    
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.complex_linear = ComplexLinear(in_dim, out_dim)
        self.activation = PhaseEquivariantActivation()
    
    def forward(self, z, adjacency):
        """
        GNN 消息传递（复数值）
        
        z: 复数节点特征 (N, in_dim)
        adjacency: 邻接矩阵 (N, N)
        """
        # 消息聚合: Σ_j A_ij * z_j
        messages = torch.matmul(adjacency, z)
        
        # 复数线性变换
        transformed = self.complex_linear(messages)
        
        # 相位等变激活
        return self.activation(transformed)
```

### 3. 全局基不变性

**不变性保证**:

输入在基 B1: `z = x + iy`
输入在基 B2: `z' = z * e^(iθ)` (旋转θ)

GNN 输出:
```python
# 相位等变架构保证
GNN(z') = GNN(z) * e^(iθ)

# 控制决策基不变
control(z') = control(z) * e^(iθ)
```

**实际意义**:
- 每个节点可用本地基（无需全局坐标）
- 控制决策相对于本地基一致
- 分布式控制全局协调

### 4. 分布式控制决策

**架构流程**:
```python
class DistributedComplexGNNController(nn.Module):
    """分布式复数值 GNN 控制器"""
    
    def __init__(self, n_agents, state_dim, control_dim, n_layers=3):
        super().__init__()
        
        # GNN 层
        self.layers = nn.ModuleList([
            ComplexGNNLayer(state_dim, state_dim)
            for _ in range(n_layers)
        ])
        
        # 控制输出层
        self.control_head = ComplexLinear(state_dim, control_dim)
    
    def forward(self, states, adjacency):
        """
        分布式控制决策
        
        states: 复数状态 (N, state_dim)
        adjacency: 邻接矩阵
        """
        z = states
        
        # GNN 消息传递
        for layer in self.layers:
            z = layer(z, adjacency)
        
        # 每节点独立控制决策
        controls = self.control_head(z)
        
        return controls
    
    def distributed_execution(self, agent_id, local_state, neighbor_states):
        """
        单节点执行（无全局信息）
        
        agent_id: 本节点 ID
        local_state: 本节点状态（本地基）
        neighbor_states: 邻居状态（邻居基）
        """
        # 需处理基变换（邻居状态相位对齐）
        aligned_neighbors = self.align_bases(local_state, neighbor_states)
        
        # 本地消息聚合
        local_message = local_state + sum(aligned_neighbors)
        
        # 本地 GNN 处理
        z = local_message
        for layer in self.layers:
            z = layer.complex_linear(z.unsqueeze(0)).squeeze(0)
            z = layer.activation(z)
        
        # 本地控制决策
        control = self.control_head(z.unsqueeze(0)).squeeze(0)
        
        return control
    
    def align_bases(self, local_state, neighbor_states):
        """
        基对齐：邻居状态变换到本地基
        
        关键: 使用相对观测（相位差）
        """
        # 相对相位估计
        local_phase = torch.angle(local_state)
        aligned = []
        
        for neighbor in neighbor_states:
            neighbor_phase = torch.angle(neighbor)
            phase_diff = neighbor_phase - local_phase
            
            # 相位对齐
            aligned_neighbor = neighbor * torch.exp(-1j * phase_diff)
            aligned.append(aligned_neighbor)
        
        return aligned
```

## 应用场景

### 1. GPS 拒绝环境控制

```python
# 无 GPS、无指南针
# 每节点使用本地基（相对方向）

controller = DistributedComplexGNNController(
    n_agents=10,
    state_dim=4,  # 位置(x,y) + 速度(vx,vy) → 2 complex
    control_dim=2  # 力(Fx,Fy) → 1 complex
)

# 分布式控制决策
controls = controller(states, adjacency)
```

### 2. 多机器人协调

```python
# 机器人群体控制
# 无全局定位系统

# 每机器人：
# 1. 本地传感器（相对位置/方向）
# 2. 与邻居通信（相对观测）
# 3. 本地计算控制决策
```

### 3. 无人机集群

```python
# 无 GPS 信号环境
# 无人机集群分布式控制

# 应用：室内、地下、干扰环境
```

## 技术优势

### 1. 基不变性

- **传统方法**: 需全局坐标 → GPS 拒绝失效
- **复数值 GNN**: 本地基 → 无需全局坐标

### 2. 分布式执行

- **传统集中式**: 一个控制器 → 通信瓶颈
- **分布式 GNN**: 每节点独立 → 实时响应

### 3. 相位等变

数学保证：基变换 → 输出同步变换
```
f(z*e^(iθ)) = f(z)*e^(iθ)
```

## 与其他技能关联

- **distributed-control**: 分布式控制基础
- **gnn-transformer-fusion**: GNN 架构设计
- **geometry-aware-spiking-gnn**: 几何感知 GNN
- **quantum-eeg-foundation**: 复数域处理（量子态）

## 实现要点

### 1. 复数值激活函数

**选择**:
- ReLU(mod) + 保持相位 ✓
- sigmoid(mod) ✓
- tanh(mod) ✓

**避免**:
- 直接复数激活（破坏相位等变）

### 2. 基对齐策略

**相对观测**:
```python
# 相位差估计
phase_diff = angle(neighbor) - angle(local)

# 对齐变换
aligned = neighbor * e^(-i*phase_diff)
```

### 3. 训练策略

**数据增强**:
```python
# 随机基变换（训练不变性）
def augment_with_random_basis(states):
    random_phase = torch.rand(1) * 2 * np.pi
    return states * torch.exp(1j * random_phase)
```

**损失函数**:
```python
# 控制任务损失 + 不变性损失
L = L_task + λ * L_equivariance
```

## 关键洞察

**核心创新**:
1. 复数域表示 → 几何特征自然编码
2. 相位等变 → 基变换不变性
3. 分布式架构 → 实时控制

**应用价值**:
- GPS 拒绝环境控制
- 无全局定位系统场景
- 保密/隐私分布式控制

## 研究前沿

- 3D 系统扩展（复数 → 四元数）
- 非平面系统
- 动态拓扑网络
- 异构多智能体

## 工具依赖

```bash
pip install torch numpy
```

## 注意事项

1. 平面系统（2D）假设
2. 需邻居通信（相对观测）
3. 相位估计可能有噪声
4. 训练需要基变换数据增强

---

_复数之美，基不变之智，分布式之力。_