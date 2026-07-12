# Tensor Network Methods for Quantum Systems

张量网络是多体量子系统的有效表示和计算方法。

## Core Concepts

### Tensor Network Basics

张量是多索引数组：
$$T_{i_1 i_2 \ldots i_n}$$

收缩操作：
$$\sum_k A_{i_1 \ldots i_k} B_{k \ldots j}$$

图形表示：
- 张量：节点（圆/方）
- 索引：线
- 收缩：连接线

### Matrix Product States (MPS)

一维系统的张量网络表示：
$$|\psi\rangle = \sum_{i_1 \ldots i_N} A^{[1]}_{i_1} A^{[2]}_{i_2} \ldots A^{[N]}_{i_N} |i_1 \ldots i_N\rangle$$

或带边界索引：
$$|\psi\rangle = \sum_{i_1 \ldots i_N} A^{[1]}_{\alpha_0 i_1 \alpha_1} A^{[2]}_{\alpha_1 i_2 \alpha_2} \ldots |i_1 \ldots i_N\rangle$$

关键性质：
- 素积维（bond dimension）控制精度
- 低纠缠态高效表示
- 面积定律态：$D \sim O(1)$

### Projected Entangled Pair States (PEPS)

二维系统的张量网络：
$$|\psi\rangle = \sum_{i_1 \ldots i_N} A^{[1]}_{i_1 \alpha\beta\gamma\delta} \ldots |i_1 \ldots i_N\rangle$$

每个张量有多个辅助索引（连接邻居）。

挑战：
- PEPS 收缩复杂度高
- 需要近似收缩方法
- Belief Propagation 是一种解法

## Belief Propagation Algorithm

### Classical BP

图上的消息传递算法：
- 消息：$m_{i \to j}(x_j)$（节点 $i$ 到 $j$ 的信念）
- 更新规则：
$$m_{i \to j}(x_j) = \sum_{x_i} \phi_i(x_i) \phi_{ij}(x_i, x_j) \prod_{k \in \text{neighbors}(i)\setminus j} m_{k \to i}(x_i)$$

收敛后计算信念：
$$b_i(x_i) \propto \phi_i(x_i) \prod_{j \in \text{neighbors}(i)} m_{j \to i}(x_i)$$

### Tensor Network BP

张量网络的 BP 变体：

1. **初始化**：
   - 张量作为节点
   - 辅助索引作为边
   - 物理索引不传递

2. **消息定义**：
$$M_{A \to B} = \sum_{\text{other indices}} A \prod_{C \neq B} M_{C \to A}$$

3. **迭代更新**：
   - 直到消息收敛
   - 或固定迭代次数

4. **收缩计算**：
$$Z = \text{Tr}(\prod_A A) \approx \text{BP estimate}$$

### BP Convergence

收敛条件：
- 树结构：精确且收敛
- 一般图：近似，可能不收敛
- 量子系统：需要改进（量子 BP）

改进方法：
- Gauge freedom 选择
- 正则化
- 层次 BP

## Advanced Methods

### Tree Tensor Network (TTN)

树状结构：
- 无环，BP 精确
- 多分叉张量
- 层次结构

计算高效，适合低纠缠系统。

### Multi-scale Entanglement Renormalization Ansatz (MERA)

含 disentangler 和 isometry：
- 重正化群结构
- 临界态高效表示
- 对数纠缠律

### Quantum BP Variants

**Simple Update**：
- 每步只更新局部环境
- 快速但不精确

**Full Update**：
- 使用 BP 计算完整环境
- 更精确但计算量大

**Gradient-based**：
- 基于能量梯度优化
- 结合自动微分

## Computational Implementations

### Basic MPS

```python
import numpy as np

class MPS:
    """Matrix Product State"""
    
    def __init__(self, N, d, D):
        """
        Args:
            N: 系统大小
            d: 物理维度
            D: 素积维
        """
        self.N = N
        self.d = d
        self.D = D
        self.tensors = [
            np.random.randn(D, d, D) / np.sqrt(D * d * D)
            for _ in range(N)
        ]
        # 边界调整
        self.tensors[0] = self.tensors[0][0:1, :, :]
        self.tensors[-1] = self.tensors[-1][:, :, -1:]
    
    def normalize(self):
        """归一化 MPS"""
        norm = self.norm()
        self.tensors[0] /= np.sqrt(norm)
    
    def norm(self):
        """计算 <ψ|ψ>"""
        # 收缩所有张量
        pass
    
    def overlap(self, other):
        """计算 <ψ|φ>"""
        pass
    
    def expectation(self, op):
        """计算 <ψ|O|ψ>"""
        pass
```

### Belief Propagation

```python
def tensor_bp(tensor_graph, max_iter=100, tol=1e-6):
    """
    张量网络上的 Belief Propagation
    
    Args:
        tensor_graph: 张量和连接的图结构
        max_iter: 最大迭代次数
        tol: 收敛容差
    
    Returns:
        messages: 收敛后的消息
        marginal: 边缘分布估计
    """
    messages = initialize_messages(tensor_graph)
    
    for iteration in range(max_iter):
        new_messages = {}
        max_change = 0
        
        for edge in tensor_graph.edges:
            # 提取张量和索引
            tensor_a, tensor_b, indices = edge
            
            # 计算新消息
            new_msg = compute_message(
                tensor_a, 
                indices, 
                incoming_messages(messages, tensor_a, exclude=tensor_b)
            )
            
            # 检查变化
            change = np.linalg.norm(new_msg - messages[edge])
            max_change = max(max_change, change)
            
            new_messages[edge] = new_msg
        
        messages = new_messages
        
        if max_change < tol:
            print(f"BP converged at iteration {iteration}")
            break
    
    # 计算边缘
    marginal = compute_marginals(tensor_graph, messages)
    
    return messages, marginal

def compute_message(tensor, indices, incoming):
    """
    计算单个消息
    
    M_{A→B} = Σ_{other indices} A × (incoming messages)
    """
    # 收缩张量和传入消息
    contracted = tensor
    for edge, msg in incoming.items():
        contracted = np.tensordot(contracted, msg, axes=...)
    
    return contracted
```

## Applications

### 1. Ground State Search

使用张量网络找基态：
- DMRG（MPS 的经典算法）
- PEPS 优化（更复杂）

### 2. Time Evolution

模拟量子动力学：
- TEBD（Time Evolving Block Decimation）
- TDVP（Time Dependent Variational Principle）

### 3. Thermal States

有限温度态：
- PEPO（Projected Entangled Pair Operator）
- Purification 方法

### 4. Measurement Simulation

测量过程的张量网络：
- 测量算符的张量表示
- 条件态更新

## Key References

- arXiv:2604.03228 "Belief Propagation and Tensor Network Expansions"
- Orús (2014) "A practical introduction to tensor networks"
- Verstraete, Murg, Cirac (2008) "Matrix product states, projected entangled pair states"

## Limitations

- 高维系统困难
- 大纠缠态代价高
- BP 可能不收敛
- 需要领域知识选择结构