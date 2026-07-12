# Quantum Fisher Information Geometry

量子 Fisher 信息几何是量子态空间的几何化方法。

## Mathematical Foundation

### Classical Fisher Information

经典 Fisher 信息矩阵：
$$F_{ij} = \int p(x|\theta) \frac{\partial \log p(x|\theta)}{\partial \theta_i} \frac{\partial \log p(x|\theta)}{\partial \theta_j} dx$$

等价形式：
$$F_{ij} = \int \frac{1}{p(x|\theta)} \frac{\partial p(x|\theta)}{\partial \theta_i} \frac{\partial p(x|\theta)}{\partial \theta_j} dx$$

### Quantum Fisher Information

量子 Fisher 信息矩阵（SLD 定义）：
$$F_{ij} = \frac{1}{2} \text{Tr}[\rho(\{L_i, L_j\})]$$

其中 $L_i$ 是对称对数导数：
$$\frac{\partial \rho}{\partial \theta_i} = \frac{1}{2}(L_i \rho + \rho L_i)$$

纯态简化形式：
$$F_{ij} = \text{Re}(\langle \partial_i \psi | \partial_j \psi \rangle) - \langle \partial_i \psi | \psi \rangle \langle \psi | \partial_j \psi \rangle$$

### Bloch Sphere Geometry

对于单量子比特纯态：
$$|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$$

Fisher 信息矩阵：
$$F = \begin{pmatrix} 1 & 0 \\ 0 & \sin^2\theta \end{pmatrix}$$

这是球面度量（对应 Bloch 球的几何）。

## Applications

### 1. Quantum Metrology

Fisher 信息决定测量精度：
$$\Delta \theta \geq \frac{1}{\sqrt{F}}$$

Heisenberg 极限：$\Delta \theta \sim 1/N$（使用纠缠态）

### 2. Quantum State Distance

Fisher 信息定义状态距离：
$$d(\theta, \theta') = \sqrt{\int F(\theta) d\theta}$$

Bures 距离：
$$D_B(\rho_1, \rho_2) = \sqrt{2(1 - \sqrt{F(\rho_1, \rho_2)})}$$

其中 $F(\rho_1, \rho_2)$ 是保真度。

### 3. Quantum Phase Transitions

Fisher 信息在临界点行为：
- 连续相变：发散（奇异性）
- 拓扑相变：不连续跳变

用于识别量子相变点。

### 4. Quantum Geodesics

沿 Fisher 几何的最短路径：
- 参数空间中的最优演化
- 量子门的最优实现

## Key References

- arXiv:2601.09556 "Geometry- and Topology-Informed Quantum Computing"
- Braunstein & Caves (1994) "Statistical distance and the geometry of quantum states"
- Amari & Nagaoka (2000) "Methods of Information Geometry"

## Computational Methods

### Pure State Fisher Matrix

```python
import numpy as np

def pure_state_fisher(psi, params):
    """
    计算纯态的 Fisher 信息矩阵
    
    Args:
        psi: 量子态（参数化）
        params: 参数列表 [θ₁, θ₂, ...]
    
    Returns:
        F: Fisher 信息矩阵
    """
    n_params = len(params)
    F = np.zeros((n_params, n_params))
    
    # 计算偏导数
    for i in range(n_params):
        partial_i = np.gradient(psi, params[i])
        for j in range(n_params):
            partial_j = np.gradient(psi, params[j])
            
            # F_ij = Re(∂_iψ*∂_jψ) - Re(∂_iψ*ψ)(∂_jψ*ψ)
            F[i,j] = np.real(
                np.vdot(partial_i, partial_j) - 
                np.vdot(partial_i, psi) * np.vdot(psi, partial_j)
            )
    
    return F
```

### Mixed State Fisher Matrix

```python
def mixed_state_fisher_sld(rho, params):
    """
    混合态的 Fisher 信息矩阵（SLD 方法）
    
    Args:
        rho: 密度矩阵
        params: 参数列表
    
    Returns:
        F: Fisher 信息矩阵
        L: SLD 矩阵列表
    """
    n_params = len(params)
    F = np.zeros((n_params, n_params))
    L = []
    
    for i in range(n_params):
        # 计算 SLD: ∂ρ/∂θ = (Lρ + ρL)/2
        drho = np.gradient(rho, params[i])
        L_i = 2 * drho  # 简化，实际需要解方程
        
        for j in range(n_params):
            drho_j = np.gradient(rho, params[j])
            L_j = 2 * drho_j
            
            # F_ij = Tr(ρ{L_i, L_j})/2
            F[i,j] = 0.5 * np.trace(rho @ (L_i @ L_j + L_j @ L_i))
        
        L.append(L_i)
    
    return F, L
```

## Related Concepts

- **Quantum Metric Tensor**: Fisher 信息的几何解释
- **Berry Curvature**: 与 Fisher 信息的关系
- **Chern Number**: 拓扑不变量的几何意义
- **Quantum Speed Limit**: 由 Fisher 信息决定

## Advanced Topics

### Quantum Geometric Tensor

统一 Fisher 信息和 Berry 曲率：
$$Q_{ij} = \langle \partial_i \psi | (1 - |\psi\rangle\langle\psi|) | \partial_j \psi \rangle$$

实部：Fisher 信息 $g_{ij} = \text{Re}(Q_{ij})$
虚部：Berry 曲率 $F_{ij} = -2\text{Im}(Q_{ij})$

### Multiparameter Estimation

多参数估计的挑战：
- 参数不兼容性（非对易 SLD）
- 量子 Cramér-Rao bound 的修正
- Holevo bound

### Fisher Information Scaling

纠缠态的 Fisher 信息：
- $N$ 个独立粒子：$F \propto N$（标准量子极限）
- GHZ 纠缠态：$F \propto N^2$（Heisenberg 极限）
- 部分纠缠：介于两者之间