---
name: brain-state-transition-network-control
description: "脑状态转移动力学与网络控制方法论。基于网络控制理论计算平均可控性、模态可控性、最小控制能量等指标，研究脑网络状态转移的能量需求与动态特性。Activation: brain state transition, network control, controllability, control energy, brain dynamics, structural connectome, functional connectome, 控制理论, 状态转移, 脑网络控制."
---

# Brain State Transition Network Control

脑状态转移动力学与网络控制方法论，将控制理论应用于结构脑网络，量化状态转移的能量需求和动态可控性。

## 核心概念

### 1. 网络可控性

脑网络可控性分析基于线性时不变系统理论：

```
x(t+1) = Ax(t) + Bu(t)
```

其中：
- `x(t)`: 脑网络状态向量（各脑区活动）
- `A`: 结构连接矩阵（归一化的白质连接）
- `B`: 控制输入矩阵（驱动节点选择）
- `u(t)`: 外部控制输入

### 2. 可控性指标

#### 平均可控性 (Average Controllability)

量化网络从任意初始状态到达所有可能状态的平均能力：

```
C_avg = trace((A^T A)^{-1} W_c)
```

其中 `W_c` 是可控性 Gramian 矩阵。

**意义**：平均可控性高的节点可以驱动系统到达多种状态。

#### 模态可控性 (Modal Controllability)

量化特定节点对网络动态模式的控制能力：

```
C_modal = sum_j (1 - lambda_j^2) * v_j^i^2
```

其中：
- `lambda_j`: A 的第 j 个特征值
- `v_j^i`: 第 j 个特征向量的第 i 个元素

**意义**：模态可控性高的节点可以影响难以控制的动态模式。

### 3. 最小控制能量

从初始状态 `x_0` 到目标状态 `x_target` 的最小能量：

```
E_min = (x_target - x_0)^T W_c^{-1} (x_target - x_0)
```

**意义**：能量越低，状态转移更容易实现。

## 实现步骤

### Step 1: 准备结构连接矩阵

```python
import numpy as np
from scipy.linalg import eig, inv

# 加载结构连接矩阵（通常从 DTI 数据获取）
# SC: Structural Connectivity matrix
SC = np.load('structural_connectivity.npy')

# 形变归一化（确保系统稳定性）
def normalize_connectivity(SC):
    # 对称化
    SC_sym = (SC + SC.T) / 2
    
    # 归一化使谱半径 < 1（稳定性）
    eigenvalues = eig(SC_sym)[0]
    spectral_radius = np.max(np.abs(eigenvalues))
    
    if spectral_radius > 1:
        SC_norm = SC_sym / spectral_radius
    else:
        SC_norm = SC_sym
    
    return SC_norm

A = normalize_connectivity(SC)
```

### Step 2: 计算可控性指标

```python
def compute_average_controllability(A, B):
    """计算平均可控性"""
    n = A.shape[0]
    T = 100  # 时间步数
    
    # 计算可控性 Gramian
    W_c = np.zeros((n, n))
    for t in range(T):
        A_t = np.linalg.matrix_power(A, t)
        W_c += A_t @ B @ B.T @ A_t.T
    
    # 平均可控性 = trace(W_c)
    C_avg = np.trace(W_c)
    
    return C_avg

def compute_modal_controllability(A):
    """计算各节点的模态可控性"""
    eigenvalues, eigenvectors = eig(A)
    
    n = A.shape[0]
    C_modal = np.zeros(n)
    
    for i in range(n):  # 对每个节点
        for j in range(n):  # 对每个模式
            # 模态可控性公式
            phi_j = 1 - eigenvalues[j]**2  # 模式可控性权重
            v_j_i = eigenvectors[j, i]  # 特征向量分量
            C_modal[i] += np.real(phi_j * v_j_i**2)
    
    return C_modal

def compute_minimum_control_energy(A, B, x_0, x_target, T):
    """计算最小控制能量"""
    n = A.shape[0]
    
    # 计算 Gramian
    W_c = np.zeros((n, n))
    for t in range(T):
        A_t = np.linalg.matrix_power(A, t)
        W_c += A_t @ B @ B.T @ A_t.T
    
    # 目标状态差
    delta_x = x_target - x_0
    
    # 最小能量
    E_min = delta_x.T @ np.linalg.inv(W_c) @ delta_x
    
    return np.real(E_min)
```

### Step 3: 节点角色分类

```python
def classify_node_roles(C_avg_nodes, C_modal_nodes):
    """根据可控性指标分类节点角色"""
    
    # 合并指标
    roles = []
    
    for i in range(len(C_avg_nodes)):
        avg_high = C_avg_nodes[i] > np.percentile(C_avg_nodes, 75)
        modal_high = C_modal_nodes[i] > np.percentile(C_modal_nodes, 75)
        
        if avg_high and modal_high:
            role = "Integration Hub"
        elif avg_high and not modal_high:
            role = "Flexible Controller"
        elif not avg_high and modal_high:
            role = "Specific Controller"
        else:
            role = "Passive Node"
        
        roles.append(role)
    
    return roles

# 获取各节点的可控性（使用单一节点控制）
B_matrices = []
for i in range(n):
    B = np.zeros((n, 1))
    B[i, 0] = 1  # 单节点控制
    B_matrices.append(B)

C_avg_nodes = [compute_average_controllability(A, B) for B in B_matrices]
C_modal_nodes = compute_modal_controllability(A)

# 分类节点角色
node_roles = classify_node_roles(C_avg_nodes, C_modal_nodes)
```

### Step 4: 状态转移能量图谱

```python
def compute_transition_energy_map(A, states, T=50):
    """计算所有状态对之间的转移能量"""
    
    n_states = len(states)
    energy_map = np.zeros((n_states, n_states))
    
    # 使用全节点控制
    B = np.eye(A.shape[0])
    
    for i, state_from in enumerate(states):
        for j, state_to in enumerate(states):
            if i != j:
                E = compute_minimum_control_energy(A, B, state_from, state_to, T)
                energy_map[i, j] = E
    
    return energy_map

# 定义代表性状态（例如：静息态、任务态、睡眠态等）
states = [
    np.random.randn(n),  # 随机状态
    np.zeros(n),         # 静息态
    # 可以添加从实际数据提取的状态
]

energy_map = compute_transition_energy_map(A, states)
```

## 应用场景

### 1. 脑区功能角色分析

**输入**：DTI 结构连接数据

**输出**：
- 各脑区的可控性指标
- 节点角色分类（Integration Hub, Controller, Passive）

**应用**：
- 识别脑网络中的关键控制节点
- 理解不同脑区在网络动态中的作用

### 2. 任务切换能量预测

**输入**：静息态 → 任务态的转移

**输出**：
- 最小控制能量
- 最优驱动节点选择

**应用**：
- 预测认知任务切换的能量需求
- 优化刺激位点选择

### 3. 神经调控策略设计

**输入**：治疗目标状态（例如：抑制癫痫状态）

**输出**：
- 最小能量控制路径
- 最佳刺激节点和强度

**应用**：
- TMS/DBS 刺激位点优化
- 神经调控治疗规划

## 关键发现（文献总结）

### 1. 结构可控性 vs 功能灵活性

**发现**：高平均可控性节点通常是网络枢纽，可以驱动系统到达多种状态。

**意义**：结构连接决定了功能动态的可能性空间。

### 2. 模态可控性与认知灵活性

**发现**：模态可控性高的节点可以影响难以控制的动态模式，关联认知灵活性。

**意义**：某些脑区专门用于"解锁"特定的网络模式。

### 3. 能量不对称性

**发现**：状态转移能量具有方向不对称性（A→B ≠ B→A）。

**意义**：某些认知状态更容易到达，某些更难退出（例如：焦虑状态）。

### 4. 脑区角色分布

**发现**：
- Integration Hubs: 前额叶、顶叶
- Specific Controllers: 感觉运动区
- Passive Nodes: 小脑、边缘系统部分区域

## 进阶应用

### 1. 多时间尺度控制

```python
def compute_multi_scale_controllability(A, scales):
    """多时间尺度可控性分析"""
    
    results = {}
    
    for scale in scales:
        # 根据时间尺度调整系统矩阵
        A_scaled = A ** scale  # 符号运算
        
        C_avg = compute_average_controllability(A_scaled, B)
        C_modal = compute_modal_controllability(A_scaled)
        
        results[scale] = {
            'average': C_avg,
            'modal': C_modal
        }
    
    return results
```

### 2. 非线性扩展

对于非线性脑动力学（使用神经网络建模）：

```python
# 使用神经网络建模非线性动力学
import torch.nn as nn

class BrainDynamicsNet(nn.Module):
    def __init__(self, n_regions):
        super().__init__()
        self.linear = nn.Linear(n_regions, n_regions)  # 结构连接
        self.nonlinear = nn.Sequential(
            nn.Linear(n_regions, n_regions * 2),
            nn.ReLU(),
            nn.Linear(n_regions * 2, n_regions)
        )
    
    def forward(self, x):
        return self.linear(x) + self.nonlinear(x)

# 训练网络以拟合实际 fMRI 动态
# 然后使用最优控制理论设计控制策略
```

### 3. 结合功能连接

```python
def integrate_functional_connectivity(A_struct, FC_data):
    """整合结构和功能连接"""
    
    # 结构连接提供可控性基础
    # 功能连接反映实际动态模式
    
    # 使用 FC 作为状态可达性的验证
    reachable_states = extract_states_from_FC(FC_data)
    
    # 验证结构可控性预测
    predicted_energy = compute_transition_energy_map(A_struct, reachable_states)
    actual_transitions = compute_actual_transition_probs(FC_data)
    
    # 相关性分析
    correlation = np.corrcoef(predicted_energy.flatten(), 
                              actual_transitions.flatten())[0, 1]
    
    return correlation
```

## 工具与数据源

### 数据获取

- **结构连接**：DTI tractography（HCP, ADNI 数据集）
- **功能连接**：fMRI resting-state data
- **节点定义**：脑图谱（AAL, Schaefer, Glasser）

### 软件工具

- **Network Control Toolbox**: https://github.com/jbmedina/network_control
- **Brain Connectivity Toolbox**: https://sites.google.com/site/bctnet/
- **nctpy**: Python 实现的网络可控性库

### 关键参考文献

1. Gu et al. (2015) - "Controllability of structural brain networks"
2. Tang et al. (2017) - "Structural control theory of brain network dynamics"
3. Muldoon et al. (2016) - "Network control theory of functional brain dynamics"

## 验证与评估

### 1. 可控性预测验证

```python
def validate_controllability_prediction(A, FC_data, task_states):
    """验证可控性预测与实际动态"""
    
    # 计算预测的最优控制节点
    C_modal = compute_modal_controllability(A)
    optimal_nodes = np.argsort(C_modal)[-10:]  # 前10个节点
    
    # 实际任务切换中活跃的节点
    task_active_nodes = identify_task_active_regions(task_states)
    
    # 验证重叠
    overlap = len(set(optimal_nodes) & set(task_active_nodes))
    accuracy = overlap / len(optimal_nodes)
    
    return accuracy
```

### 2. 能量预测验证

```python
def validate_energy_prediction(A, state_transitions):
    """验证能量预测"""
    
    # 预测能量
    predicted_energies = [compute_minimum_control_energy(A, B, s1, s2, T) 
                         for s1, s2 in state_transitions]
    
    # 实际切换时间（能量越高→切换越慢）
    actual_times = [measure_transition_time(s1, s2) 
                   for s1, s2 in state_transitions]
    
    # 相关性检验
    correlation = np.corrcoef(predicted_energies, actual_times)[0, 1]
    
    return correlation
```

## 局限性与注意事项

### 1. 线性假设

- **局限**：实际脑动力学非线性
- **应对**：使用神经网络扩展或分段线性化

### 2. 结构连接不完整

- **局限**：DTI 只捕获部分白质连接
- **应对**：整合多模态数据（DTI + fMRI + EEG）

### 3. 状态定义困难

- **局限**：如何定义"脑状态"
- **应对**：使用聚类、PCA 或 ICA 从实际数据提取

### 4. 时间尺度问题

- **局限**：不同认知过程有不同时间尺度
- **应对**：多尺度可控性分析

## 与其他方法的关系

### vs Functional Connectivity Analysis

- FC 分析：描述相关关系
- 网络控制：描述因果能力和能量需求

### vs Effective Connectivity

- EC 分析：推断因果连接
- 网络控制：量化控制能力和最优策略

### vs Dynamic Causal Modeling

- DCM：参数化模型拟合
- 网络控制：基于结构连接的可控性理论

## 临床应用

### 1. 神经调控规划

**应用**：TMS/DBS 刺激位点选择

**方法**：
- 计算各节点的模态可控性
- 选择可控性高的节点作为刺激位点
- 预测刺激效果和能量需求

### 2. 脑损伤影响预测

**应用**：预测脑损伤对网络动态的影响

**方法**：
- 模拟节点删除（损伤）
- 计算可控性变化
- 预测功能恢复路径

### 3. 神经退行性疾病

**应用**：阿尔茨海默病网络退化分析

**方法**：
- 跟踪可控性指标随时间变化
- 识别关键节点退化
- 预测认知功能衰退

## 激活关键词

- brain state transition
- network control
- controllability
- control energy
- brain dynamics
- structural connectome
- functional connectome
- 控制理论
- 状态转移
- 脑网络控制
- 平均可控性
- 模态可控性
- integration hub
- cognitive flexibility
- TMS optimization
- DBS planning
- neurostimulation

## 相关 Skills

- [[brain-network-controllability]]: 脑网络可控性基础分析
- [[functional-connectome-fingerprint]]: 功能连接指纹分析
- [[brain-connectivity-analysis]]: 脑连接综合分析方法
- [[graph-laplacian-denoising]]: 图拉普拉斯去噪
- [[eeg-brain-connectivity-bci]]: EEG 连接 BCI 分析

## 推荐阅读

1. Gu S, et al. (2015). Controllability of structural brain networks. Nature Communications.
2. Tang E, et al. (2017). Structural control theory of brain network dynamics. PLoS Computational Biology.
3. Muldoon SF, et al. (2016). Network control theory of functional brain dynamics. Nature Communications.
4. Betzel RF, et al. (2016). Optimizing network control. Network Neuroscience.

## 代码仓库

- nctpy: https://github.com/jbmedina/nctpy
- Brain Network Control: https://github.com/jbmedina/network_control

---

## Instructions for Agents

使用此 skill 时：

1. 首先确认有结构连接数据（DTI 或图谱数据）
2. 计算平均可控性和模态可控性指标
3. 分类节点角色并可视化
4. 如果有目标状态，计算转移能量
5. 验证预测与实际动态的一致性

## Examples

### Example 1: 基础可控性分析

**User**: 分析脑网络的可控性指标

**Agent**: 
- 加载结构连接矩阵
- 计算平均可控性：识别 Integration Hubs
- 计算模态可控性：识别 Specific Controllers
- 生成节点角色分布图

### Example 2: 任务切换能量计算

**User**: 计算从静息态到任务态的控制能量

**Agent**:
- 定义静息态和任务态向量
- 计算最小控制能量
- 识别最优驱动节点
- 提供控制策略建议

### Example 3: TMS 刺激位点选择

**User**: 选择 TMS 刺激的最优位点

**Agent**:
- 计算各节点的模态可控性
- 排序并选择前 N 个节点
- 提供刺激参数建议（基于控制能量）
