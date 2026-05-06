---
name: lattice-field-theory-neurons
description: 晶格场论在神经网络中的应用方法论。将神经元建模为晶格格点上的场变量，利用重整化群分析网络粗粒化、临界性和尺度不变性。适用于理解神经网络的可解释性、泛化能力和架构设计。触发词：lattice field theory, 晶格场论, renormalization group, 重整化群, neural networks as field theory, 神经网络场论, 粗粒化, coarse-graining, neural criticality, 神经临界性, discrete-to-continuous, 离散连续桥梁。
user-invocable: true
---

# Lattice Field Theory for Neural Networks

将晶格场论(Lattice Field Theory, LFT)框架应用于神经网络，把神经元视为离散晶格格点上的场变量，连接视为晶格链路上的耦合。通过重整化群(Renormalization Group, RG)方法分析网络的尺度行为、临界现象和连续极限。

**核心洞察：** 神经网络的层间信息流动与晶格场论中的关联传播具有深刻的数学同构性——重整化群粗粒化操作自然对应池化和下采样，场论的临界行为对应网络的最佳泛化点。

---

## 1. Lattice Field Theory Basics Applied to Neurons

### 1.1 核心映射：从物理晶格到神经晶格

| LFT概念 | 神经网络对应 | 说明 |
|---------|-------------|------|
| 晶格格点(site) | 神经元/特征单元 | 离散空间中的基本自由度 |
| 场变量 φ(x) | 神经元激活值 | 格点上的实/复数值 |
| 链路(link) | 突触权重 W_ij | 格点间的耦合强度 |
| 配分函数 Z | 网络边缘分布 | 所有配置的加权和 |
| 作用量 S[φ] | 损失函数 + 正则项 | 决定构型概率 |
| 关联函数 ⟨φ(x)φ(y)⟩ | 神经元互相关 | 信息传播度量 |
| 质量隙 m | 有效感受野衰减 | 关联衰减的特征尺度 |

### 1.2 神经场论作用量

将神经网络建模为标量场论，作用量为：

```
S[h] = Σ_x [ ½(∇h)² + ½m²h² + V(h) ] + S_int[h, W]
```

其中：
- `h(x)` 为格点 x 处的神经元激活
- `(∇h)²` 为离散梯度项，对应相邻神经元的差异
- `m²` 为质量项，控制激活的衰减速率
- `V(h)` 为非线性势函数（对应激活函数）
- `S_int` 为权重耦合项

```python
import numpy as np
from scipy import sparse

class NeuralLatticeField:
    """
    将神经网络建模为晶格场
    
    神经元 = 晶格格点上的标量场
    权重 = 晶格链路上的耦合
    """
    
    def __init__(self, lattice_shape, coupling_type='nearest'):
        """
        参数:
            lattice_shape: 晶格形状，如 (32, 32) 或 (8, 8, 8)
            coupling_type: 耦合类型 ('nearest', 'next_nearest', 'all')
        """
        self.shape = lattice_shape
        self.ndims = len(lattice_shape)
        self.n_sites = int(np.prod(lattice_shape))
        
        # 构建晶格拉普拉斯算子 (离散二阶导数)
        self.laplacian = self._build_laplacian(coupling_type)
        
        # 场变量 (神经元激活)
        self.field = np.zeros(self.n_sites)
        
        # 质量参数
        self.mass = 1.0
        
    def _build_laplacian(self, coupling_type):
        """
        构建晶格离散拉普拉斯算子
        
        一维情况：L = tridiag(-1, 2, -1)
        高维：各维拉普拉斯之和
        """
        n = self.n_sites
        
        # 从晶格坐标到一维索引的映射
        def to_index(coords):
            idx = 0
            stride = 1
            for i, c in enumerate(coords):
                idx += c * stride
                stride *= self.shape[i]
            return idx
        
        def to_coords(idx):
            coords = []
            for s in self.shape:
                coords.append(idx % s)
                idx //= s
            return coords
        
        rows, cols, vals = [], [], []
        
        for idx in range(n):
            coords = to_coords(idx)
            
            # 对角元
            rows.append(idx)
            cols.append(idx)
            vals.append(2 * self.ndims)
            
            # 最近邻耦合
            for dim in range(self.ndims):
                for delta in [-1, 1]:
                    neighbor = list(coords)
                    neighbor[dim] += delta
                    # 周期性边界条件
                    neighbor[dim] %= self.shape[dim]
                    
                    nidx = to_index(neighbor)
                    rows.append(idx)
                    cols.append(nidx)
                    vals.append(-1)
        
        L = sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))
        return L
    
    def action(self, field=None):
        """
        计算场构型的作用量
        
        S = ½ φ^T (-∇² + m²) φ + V(φ)
        """
        if field is None:
            field = self.field
        
        # 动能项 (梯度项)
        kinetic = 0.5 * field @ self.laplacian @ field
        
        # 质量项
        mass_term = 0.5 * self.mass**2 * np.sum(field**2)
        
        # 非线性势 (φ⁴ 理论，对应ReLU类激活)
        potential = 0.1 * np.sum(np.maximum(field, 0)**4)
        
        return kinetic + mass_term + potential
    
    def correlation_function(self, field=None, max_dist=10):
        """
        计算两点关联函数 ⟨φ(x)φ(y)⟩
        
        关联函数揭示信息的传播范围和特征尺度
        """
        if field is None:
            field = self.field
        
        n = len(field)
        correlations = np.zeros(max_dist)
        counts = np.zeros(max_dist)
        
        for i in range(n):
            coords_i = self._to_coords(i)
            for j in range(i+1, n):
                coords_j = self._to_coords(j)
                
                # 计算曼哈顿距离（考虑周期性）
                dist = 0
                for dim in range(self.ndims):
                    d = abs(coords_i[dim] - coords_j[dim])
                    d = min(d, self.shape[dim] - d)
                    dist += d
                
                if dist < max_dist:
                    correlations[dist] += field[i] * field[j]
                    counts[dist] += 1
        
        # 归一化
        nonzero = counts > 0
        correlations[nonzero] /= counts[nonzero]
        
        return correlations[:np.max(np.where(nonzero)[0])+1]
    
    def _to_coords(self, idx):
        """一维索引转为晶格坐标"""
        coords = []
        for s in self.shape:
            coords.append(idx % s)
            idx //= s
        return coords
```

### 1.3 激活函数的场论解释

不同激活函数对应不同的场论势函数：

| 激活函数 | 场论势 V(φ) | 物理意义 |
|---------|-------------|---------|
| ReLU | V(φ) = λ·φ⁴·Θ(φ) | 单向φ⁴理论 |
| Tanh/Sigmoid | V(φ) = λ·φ⁴ + ½m²φ² | 经典φ⁴理论 |
| GELU | V(φ) = φ·Φ(φ) - ½φ² | 自相互作用场 |
| Linear | V(φ) = 0 | 自由场理论 |
| Softplus | V(φ) = ln(1+e^φ) - φ | 平滑截断场 |

```python
class ActivationPotential:
    """激活函数的场论势函数"""
    
    @staticmethod
    def relu_potential(phi, lam=0.1):
        """ReLU 对应单向 φ⁴ 势"""
        return lam * np.maximum(phi, 0)**4
    
    @staticmethod
    def tanh_potential(phi, m2=1.0, lam=0.1):
        """Tanh 对应经典 φ⁴ 势"""
        return 0.5 * m2 * phi**2 + lam * phi**4
    
    @staticmethod
    def softplus_potential(phi):
        """Softplus 势"""
        return np.log(1 + np.exp(phi)) - phi
    
    @staticmethod
    def effective_mass(activation_type, operating_point):
        """
        计算激活函数的有效质量（二阶导数）
        
        有效质量决定了信号传播的衰减特性
        """
        if activation_type == 'relu':
            return 0 if operating_point > 0 else np.inf
        elif activation_type == 'tanh':
            # tanh'(x) = 1 - tanh²(x), tanh''(x) = -2·tanh(x)·(1-tanh²(x))
            t = np.tanh(operating_point)
            return 2 * t * (1 - t**2)
        elif activation_type == 'sigmoid':
            s = 1 / (1 + np.exp(-operating_point))
            return s * (1 - s) * (1 - 2*s)
        elif activation_type == 'gelu':
            # GELU近似二阶导
            return 1 - 0.044715 * 3 * operating_point**2
        return 0
```

---

## 2. Renormalization Group for Neural Networks

### 2.1 RG思想在神经网络中的核心应用

重整化群的核心操作：
1. **粗粒化 (Coarse-graining)**：整合局部自由度 → 对应池化/下采样
2. **重标度 (Rescaling)**：调整尺度 → 对应特征归一化
3. **重归一化 (Renormalization)**：调整耦合常数 → 对应权重更新

神经网络中的RG流：
- 浅层 → 深层 = UV → IR (紫外到红外)
- 逐层变换构成RG轨迹
- 不动点对应尺度不变的特征表示

```python
class NeuralRGFlow:
    """
    神经网络的重整化群分析
    
    将网络逐层变换视为RG流
    """
    
    def __init__(self, n_layers):
        self.n_layers = n_layers
        self.beta_functions = []  # β函数：耦合常数随尺度的变化
        self.coupling_constants = []
        
    def block_spin_transform(self, weights, block_size=2):
        """
        块自旋变换：将 block_size×block_size 的神经元块
        粗粒化为单个有效神经元
        
        对应池化操作的RG解释
        """
        shape = weights.shape
        if len(shape) == 2:
            # 权重矩阵的块粗粒化
            n_rows, n_cols = shape
            new_rows = n_rows // block_size
            new_cols = n_cols // block_size
            
            coarse_weights = np.zeros((new_rows, new_cols))
            
            for i in range(new_rows):
                for j in range(new_cols):
                    row_start = i * block_size
                    col_start = j * block_size
                    
                    # 块内权重平均（或最大，取决于池化类型）
                    block = weights[row_start:row_start+block_size,
                                  col_start:col_start+block_size]
                    coarse_weights[i, j] = np.mean(block)
            
            return coarse_weights
        else:
            # 卷积核的块粗粒化
            out_ch, in_ch, kh, kw = shape
            new_kh = kh // block_size
            new_kw = kw // block_size
            
            coarse = np.zeros((out_ch, in_ch, new_kh, new_kw))
            for oc in range(out_ch):
                for ic in range(in_ch):
                    for i in range(new_kh):
                        for j in range(new_kw):
                            block = weights[oc, ic, 
                                           i*block_size:(i+1)*block_size,
                                           j*block_size:(j+1)*block_size]
                            coarse[oc, ic, i, j] = np.mean(block)
            return coarse
    
    def compute_beta_function(self, coupling, scale_factors):
        """
        计算β函数：dg/d ln(b)
        
        β(g) 描述耦合常数随尺度变换的变化率
        β(g) = 0 的点为RG不动点（临界点）
        """
        beta = np.gradient(coupling, np.log(scale_factors))
        return beta
    
    def find_fixed_points(self, coupling_trajectory):
        """
        寻找RG不动点
        
        不动点对应：
        - 高斯不动点：自由场理论（线性网络）
        - Wilson-Fisher不动点：临界现象（最优泛化）
        """
        # β(g*) = 0 的点
        for i in range(1, len(coupling_trajectory)-1):
            g_prev = coupling_trajectory[i-1]
            g_curr = coupling_trajectory[i]
            g_next = coupling_trajectory[i+1]
            
            # 检查是否接近不动点
            if abs(g_next - g_prev) < 1e-3:
                yield i, g_curr
    
    def critical_exponent(self, observable, length_scales):
        """
        计算临界指数
        
        在临界点附近，可观测量按幂律缩放：
        O ~ L^(-η)
        """
        log_L = np.log(length_scales)
        log_O = np.log(np.abs(observable) + 1e-10)
        
        # 线性拟合得到临界指数
        coeffs = np.polyfit(log_L, log_O, 1)
        eta = -coeffs[0]
        
        return eta
    
    def analyze_layer_wise_rg(self, layer_weights):
        """
        逐层RG分析
        
        将每层权重视为不同尺度下的有效耦合
        """
        results = {
            'spectral_ratios': [],
            'effective_couplings': [],
            'correlation_lengths': []
        }
        
        for W in layer_weights:
            # 谱比：最大特征值/次大特征值
            eigenvalues = np.linalg.svd(W, compute_uv=False)
            if len(eigenvalues) > 1 and eigenvalues[1] > 0:
                ratio = eigenvalues[0] / eigenvalues[1]
            else:
                ratio = eigenvalues[0]
            
            results['spectral_ratios'].append(ratio)
            results['effective_couplings'].append(np.mean(np.abs(W)))
            
            # 关联长度估计（从谱衰减）
            if len(eigenvalues) > 2:
                corr_len = -1 / np.log(eigenvalues[1] / eigenvalues[0])
            else:
                corr_len = float('inf')
            results['correlation_lengths'].append(corr_len)
        
        return results
```

### 2.2 RG与泛化能力

网络在临界点附近（RG不动点）训练时，泛化能力最优：

```python
class RGGeneralizationAnalyzer:
    """
    基于RG的网络泛化分析
    
    假设：网络在RG流中接近临界不动点时泛化最优
    """
    
    def __init__(self, model):
        self.model = model
    
    def measure_distance_to_criticality(self):
        """
        测量网络当前状态到临界点的距离
        
        距离越小 → 泛化潜力越高
        """
        layers = self._extract_weight_matrices()
        
        # 计算每层的序参量（类似磁化强度）
        order_parameters = []
        for W in layers:
            # 用权重的平均绝对值作为序参量
            m = np.mean(np.abs(W))
            order_parameters.append(m)
        
        # 临界点附近序参量应满足幂律
        # |m - m_c| ~ |T - T_c|^β
        
        # 估计与临界点的距离
        m_mean = np.mean(order_parameters)
        m_std = np.std(order_parameters)
        
        # 距离度量：层间一致性
        distance_to_critical = m_std / (m_mean + 1e-10)
        
        return {
            'distance': distance_to_critical,
            'order_parameters': order_parameters,
            'is_near_critical': distance_to_critical < 0.3
        }
    
    def _extract_weight_matrices(self):
        """从模型提取权重矩阵列表"""
        weights = []
        for param in self.model.parameters():
            if param.dim() == 2:
                weights.append(param.detach().cpu().numpy())
        return weights
    
    def rg_informed_regularization(self, lambda_base=0.01):
        """
        基于RG的自适应正则化
        
        在远离临界点的层施加更强正则化
        """
        layers = self._extract_weight_matrices()
        reg_weights = []
        
        for W in layers:
            # 计算该层的有效耦合强度
            g_eff = np.sqrt(np.mean(W**2))
            
            # 远离临界点 → 更强正则化
            # 理想耦合强度 g* ≈ 1
            deviation = abs(g_eff - 1.0)
            reg_w = lambda_base * (1 + deviation)
            reg_weights.append(reg_w)
        
        return reg_weights
```

---

## 3. Discrete-to-Continuous Bridge

### 3.1 离散神经网络的连续极限

当神经元数量 N → ∞ 且连接间距 a → 0 时，离散神经网络趋向连续场论：

```python
class DiscreteToContinuous:
    """
    离散到连续的桥接分析
    
    研究有限尺寸网络如何逼近连续场论极限
    """
    
    def __init__(self, discrete_network, lattice_spacing=1.0):
        self.network = discrete_network
        self.a = lattice_spacing  # 晶格间距
        
    def continuum_limit(self, field_values, coordinates):
        """
        从离散场值构造连续场
        
        φ_continuous(x) = Σ_i φ_i · K_a(x - x_i)
        
        K_a 为核函数（插值核）
        """
        def interpolate(x, field_vals, coords, kernel='gaussian'):
            result = 0.0
            for i, (phi_i, x_i) in enumerate(zip(field_vals, coords)):
                dist = np.linalg.norm(x - x_i)
                
                if kernel == 'gaussian':
                    # 高斯核
                    weight = np.exp(-dist**2 / (2 * self.a**2))
                elif kernel == 'sinc':
                    # 理想带限插值（Whittaker-Shannon）
                    if dist == 0:
                        weight = 1.0
                    else:
                        weight = np.sin(np.pi * dist / self.a) / (np.pi * dist / self.a)
                else:
                    # 线性插值
                    weight = max(0, 1 - dist / self.a)
                
                result += phi_i * weight
            return result
        
        return interpolate
    
    def finite_size_scaling(self, observables, system_sizes):
        """
        有限尺寸标度分析
        
        O(L) = L^(-x/ν) · f(L/ξ)
        
        用于从有限网络推断无限网络的性质
        """
        # 不同尺寸下的观测量
        log_L = np.log(system_sizes)
        
        results = {}
        for obs_name, obs_values in observables.items():
            log_O = np.log(np.abs(obs_values) + 1e-10)
            
            # 幂律拟合
            coeffs = np.polyfit(log_L, log_O, 1)
            exponent = -coeffs[0]
            
            results[obs_name] = {
                'scaling_exponent': exponent,
                'infinite_limit': obs_values[-1] if exponent > 0 else 0
            }
        
        return results
    
    def lattice_artifacts(self, discrete_result, continuous_prediction):
        """
        量化离散晶格的人工效应
        
        晶格人工效应 ~ O(a²) 对于二阶精度的离散化
        """
        error = np.abs(discrete_result - continuous_prediction)
        
        # 检查误差是否按 a² 缩放
        return {
            'absolute_error': error,
            'relative_error': error / (np.abs(continuous_prediction) + 1e-10),
            'is_O_a_squared': error < 2 * (self.a**2)
        }
```

### 3.2 神经正切核(NTK)与连续场论的联系

```python
class NTKContinuumLimit:
    """
    神经正切核的连续极限
    
    当网络宽度→∞时，NTK趋向确定性的连续核
    """
    
    @staticmethod
    def compute_ntk_discrete(inputs, params, model_fn):
        """
        计算离散网络的NTK
        
        K(x, x') = Σ_p ∂f(x)/∂θ_p · ∂f(x')/∂θ_p
        """
        import jax
        from jax import vmap, jacrev
        
        # 雅可比矩阵
        jacobian = vmap(jacrev(model_fn))(params, inputs)
        
        # NTK = J @ J^T
        ntk = jacobian @ jacobian.T
        return ntk
    
    @staticmethod
    def continuum_kernel(ntk_discrete, grid_spacing):
        """
        将离散NTK转换为连续核函数
        
        K_cont(x, x') = lim_{a→0} K_disc(x, x') / a^d
        """
        n = ntk_discrete.shape[0]
        
        # 重标度
        ntk_continuum = ntk_discrete / (grid_spacing ** 2)
        
        return ntk_continuum
    
    @staticmethod
    def spectral_analysis(ntk, n_modes=50):
        """
        NTK的谱分析
        
        特征值衰减率决定了学习不同频率信号的能力
        """
        eigenvalues = np.linalg.eigvalsh(ntk)
        eigenvalues = np.sort(eigenvalues)[::-1]
        
        # 幂律拟合
        nonzero = eigenvalues > 0
        log_idx = np.log(np.arange(1, np.sum(nonzero)+1))
        log_eval = np.log(eigenvalues[nonzero])
        
        if len(log_idx) > 2:
            slope = np.polyfit(log_idx, log_eval, 1)[0]
        else:
            slope = 0
        
        return {
            'eigenvalues': eigenvalues[:n_modes],
            'spectral_slope': slope,
            'condition_number': eigenvalues[0] / (eigenvalues[-1] + 1e-10),
            'effective_rank': np.sum(eigenvalues > eigenvalues[0] * 0.01)
        }
```

---

## 4. Implementation Patterns

### 4.1 晶格正则化神经网络 (Lattice-Regularized Neural Network)

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LatticeRegularizedLayer(nn.Module):
    """
    带有晶格场论正则化的神经网络层
    
    正则化项来自离散场论的作用量：
    L_reg = ½ Σ_<ij> (h_i - h_j)² + ½m² Σ_i h_i²
    """
    
    def __init__(self, in_features, out_features, 
                 lattice_shape=(8, 8), mass=0.1, 
                 gradient_weight=0.01):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.lattice_shape = lattice_shape
        self.mass = mass
        self.gradient_weight = gradient_weight
        
        # 预计算晶格梯度算子
        self._build_gradient_operators()
    
    def _build_gradient_operators(self):
        """构建离散梯度算子"""
        h, w = self.lattice_shape
        n = h * w
        
        # 一维差分算子（x方向）
        Dx = torch.zeros(n, n)
        for i in range(h):
            for j in range(w):
                idx = i * w + j
                Dx[idx, idx] = 1
                if j < w - 1:
                    Dx[idx, idx + 1] = -1
        
        # 一维差分算子（y方向）
        Dy = torch.zeros(n, n)
        for i in range(h):
            for j in range(w):
                idx = i * w + j
                Dy[idx, idx] = 1
                if i < h - 1:
                    Dy[idx, idx + w] = -1
        
        self.register_buffer('Dx', Dx)
        self.register_buffer('Dy', Dy)
    
    def lattice_regularization(self, activations):
        """
        计算晶格正则化项
        
        L_reg = ||∇h||² + m²||h||²
        """
        batch_size = activations.shape[0]
        h = activations.view(batch_size, -1)
        
        # 梯度项
        grad_x = h @ self.Dx.T
        grad_y = h @ self.Dy.T
        gradient_term = (grad_x**2 + grad_y**2).sum()
        
        # 质量项
        mass_term = self.mass**2 * (h**2).sum()
        
        return self.gradient_weight * (gradient_term + mass_term)
    
    def forward(self, x):
        out = self.linear(x)
        reg = self.lattice_regularization(out)
        self.lattice_reg = reg  # 保存用于损失计算
        return out


class LatticeFieldNetwork(nn.Module):
    """
    完整的晶格场论正则化网络
    
    将场论作用量作为训练目标的一部分
    """
    
    def __init__(self, input_dim, hidden_dims, output_dim,
                 lattice_shape=(16, 16), mass=0.05,
                 interaction_lambda=0.01):
        super().__init__()
        
        layers = []
        prev_dim = input_dim
        
        for dim in hidden_dims:
            layers.append(
                LatticeRegularizedLayer(prev_dim, dim,
                                       lattice_shape=lattice_shape,
                                       mass=mass)
            )
            layers.append(nn.ReLU())
            prev_dim = dim
        
        layers.append(nn.Linear(prev_dim, output_dim))
        self.network = nn.Sequential(*layers)
        
        self.interaction_lambda = interaction_lambda
    
    def forward(self, x):
        return self.network(x)
    
    def total_loss(self, predictions, targets):
        """
        总损失 = 任务损失 + 晶格场论正则化
        
        L = L_task + Σ_layers λ_reg · S_lattice[h]
        """
        task_loss = F.mse_loss(predictions, targets)
        
        reg_loss = 0
        for module in self.modules():
            if isinstance(module, LatticeRegularizedLayer):
                if hasattr(module, 'lattice_reg'):
                    reg_loss += module.lattice_reg
        
        return task_loss + self.interaction_lambda * reg_loss
```

### 4.2 RG-Inspired Coarse-Graining Pooling

```python
class RGPooling(nn.Module):
    """
    受重整化群启发的粗粒化池化
    
    与标准池化的区别：
    1. 池化权重可学习（由RG流决定）
    2. 多尺度信息保留
    3. 关联函数保持
    """
    
    def __init__(self, in_channels, block_size=2, 
                 n_scales=3, trainable=True):
        super().__init__()
        self.block_size = block_size
        self.n_scales = n_scales
        self.trainable = trainable
        
        # 每个尺度的RG耦合参数
        if trainable:
            self.rg_couplings = nn.Parameter(
                torch.ones(n_scales, block_size, block_size)
            )
        else:
            self.rg_couplings = torch.ones(n_scales, block_size, block_size)
    
    def forward(self, x):
        """
        多尺度RG池化
        
        输出：[coarse_1, coarse_2, ..., coarse_n] 的拼接
        """
        batch_size, channels, height, width = x.shape
        
        outputs = []
        
        for scale in range(self.n_scales):
            # 当前尺度的块大小
            bs = self.block_size ** (scale + 1)
            
            # 适配尺寸
            h_adapt = (height // bs) * bs
            w_adapt = (width // bs) * bs
            
            x_scaled = x[:, :, :h_adapt, :w_adapt]
            
            # RG加权池化
            pooled = self._rg_pool(x_scaled, bs, scale)
            outputs.append(pooled)
        
        # 多尺度特征拼接
        return torch.cat(outputs, dim=1)
    
    def _rg_pool(self, x, block_size, scale_idx):
        """RG加权池化操作"""
        batch_size, channels, height, width = x.shape
        
        # 重塑为块
        x_blocks = x.view(batch_size, channels,
                         height // block_size, block_size,
                         width // block_size, block_size)
        
        # 获取当前尺度的RG权重
        if self.trainable:
            weights = torch.softmax(
                self.rg_couplings[scale_idx], dim=0
            )
        else:
            weights = self.rg_couplings[scale_idx] / \
                     self.rg_couplings[scale_idx].sum()
        
        # 加权平均
        weights = weights.view(1, 1, 1, block_size, 1, block_size)
        pooled = (x_blocks * weights).sum(dim=(3, 5))
        
        return pooled
```

### 4.3 场论启发的初始化 (Field-Theoretic Initialization)

```python
def field_theoretic_init(module, lattice_dim=2, field_type='free'):
    """
    场论启发的权重初始化
    
    基于自由场理论的关联函数设定初始权重
    """
    if isinstance(module, nn.Conv2d):
        kh, kw = module.kernel_size
        in_ch = module.in_channels
        out_ch = module.out_channels
        
        for oc in range(out_ch):
            for ic in range(in_ch):
                weight = module.weight.data[oc, ic]
                
                if field_type == 'free':
                    # 自由场：指数衰减关联
                    # ⟨φ(x)φ(y)⟩ ~ exp(-m|x-y|) / |x-y|^(d-2)
                    m = 0.5  # 质量参数
                    for i in range(kh):
                        for j in range(kw):
                            r = np.sqrt((i - kh//2)**2 + (j - kw//2)**2)
                            if lattice_dim == 2 and r > 0:
                                weight[i, j] = np.exp(-m * r) / r
                            elif r > 0:
                                weight[i, j] = np.exp(-m * r) / (r ** (lattice_dim - 2))
                            else:
                                weight[i, j] = 1.0
                
                elif field_type == 'critical':
                    # 临界场：幂律衰减关联
                    # ⟨φ(x)φ(y)⟩ ~ 1/|x-y|^(d-2+η)
                    eta = 0.25  # 异常维度
                    for i in range(kh):
                        for j in range(kw):
                            r = np.sqrt((i - kh//2)**2 + (j - kw//2)**2)
                            if r > 0:
                                weight[i, j] = 1.0 / (r ** (lattice_dim - 2 + eta))
                            else:
                                weight[i, j] = 1.0
                
                # 归一化
                weight /= torch.sqrt((weight**2).sum() + 1e-10)
    
    elif isinstance(module, nn.Linear):
        if field_type == 'free':
            # 正交初始化对应自由场的对角关联
            nn.init.orthogonal_(module.weight)
        elif field_type == 'critical':
            # 重尾初始化对应临界场的长程关联
            nn.init.kaiming_normal_(module.weight, 
                                   nonlinearity='relu',
                                   mode='fan_out')


# 应用到场论网络
def apply_field_init(model, field_type='free'):
    """递归应用场论初始化到整个网络"""
    for module in model.modules():
        if isinstance(module, (nn.Conv2d, nn.Linear)):
            field_theoretic_init(module, field_type=field_type)
```

### 4.4 Wilsonian RG for Weight Pruning

```python
class WilcoianWeightPruning:
    """
    威尔逊RG启发的权重剪枝
    
    思想：在RG粗粒化过程中，
     irrelevant operators（无关算子）可以被安全积分掉
    
    对应：小权重（低RG特征值）可以被安全剪枝
    """
    
    def __init__(self, model, relevance_threshold=0.1):
        self.model = model
        self.threshold = relevance_threshold
    
    def compute_relevance(self):
        """
        计算每个权重的RG相关性
        
        relevant: β(g) > 0 （随尺度增长）
        irrelevant: β(g) < 0 （随尺度衰减）
        marginal: β(g) = 0
        """
        relevance_map = {}
        
        for name, param in self.model.named_parameters():
            if param.dim() == 2:
                W = param.detach().cpu().numpy()
                
                # 奇异值分解
                U, S, Vt = np.linalg.svd(W)
                
                # 奇异值对应RG本征值
                # 大奇异值 = relevant方向
                # 小奇异值 = irrelevant方向
                relevance = S / (S.max() + 1e-10)
                
                relevance_map[name] = {
                    'singular_values': S,
                    'relevance_spectrum': relevance,
                    'n_relevant': np.sum(relevance > self.threshold),
                    'n_irrelevant': np.sum(relevance <= self.threshold)
                }
        
        return relevance_map
    
    def prune_irrelevant(self):
        """
        剪枝irrelevant方向的权重
        
        保留relevant方向，剪掉irrelevant方向
        """
        with torch.no_grad():
            for name, param in self.model.named_parameters():
                if param.dim() == 2 and name in self.compute_relevance():
                    W = param.data
                    
                    # SVD
                    U, S, Vt = torch.svd(W)
                    
                    # 保留relevant方向
                    mask = S > (S.max() * self.threshold)
                    S_pruned = S * mask.float()
                    
                    # 重构权重
                    W_pruned = U @ torch.diag(S_pruned) @ Vt.T
                    param.data.copy_(W_pruned)
        
        return self.model
```

---

## 5. Pitfalls & Best Practices

### 5.1 常见陷阱

| 陷阱 | 说明 | 解决方案 |
|------|------|---------|
| **晶格对称性破坏** | 全连接层破坏空间对称性 | 使用卷积或图结构保持局部性 |
| **质量项过强** | 过大质量参数抑制信号传播 | 质量参数应与网络深度适配 |
| **RG流发散** | 远离临界点时耦合常数发散 | 加入自适应正则化 |
| **有限尺寸效应** | 小网络无法逼近连续极限 | 使用有限尺寸标度修正 |
| **边界条件不当** | 固定边界引入人工反射 | 使用周期性或开放边界 |
| **激活函数不兼容** | 某些激活破坏场论对称性 | 选择与目标场论对称性匹配的激活 |

### 5.2 最佳实践

```python
# ✓ 推荐：质量参数与层深适配
def adaptive_mass(layer_depth, total_depth, m_base=0.1):
    """质量参数随深度自适应调整"""
    return m_base * (1 + layer_depth / total_depth)

# ✓ 推荐：使用临界初始化
model = LatticeFieldNetwork(784, [256, 128, 64], 10)
apply_field_init(model, field_type='critical')

# ✓ 推荐：RG监控
def monitor_rg_flow(model, data_loader, n_steps=100):
    """监控训练过程中的RG流"""
    trajectory = []
    for step, (x, y) in enumerate(data_loader):
        if step >= n_steps:
            break
        
        # 提取有效耦合
        couplings = [np.mean(np.abs(p.detach().cpu().numpy())) 
                    for p in model.parameters() if p.dim() == 2]
        trajectory.append(couplings)
    
    return np.array(trajectory)

# ✗ 避免：在全连接层使用空间晶格正则化
# 全连接层没有空间结构，晶格正则化无意义

# ✗ 避免：对已剪枝网络应用RG分析
# RG分析需要完整的谱信息
```

### 5.3 验证清单

- [ ] 确认网络结构具有空间/拓扑结构（CNN, GNN, RNN）
- [ ] 检查晶格尺寸是否足够大以避免有限尺寸效应
- [ ] 验证激活函数与目标场论势的对应关系
- [ ] 监控训练中的RG流轨迹是否收敛到不动点
- [ ] 检查关联函数是否呈现预期的衰减行为
- [ ] 使用有限尺寸标度验证连续极限外推

---

## 6. Activation Keywords

### English
- lattice field theory
- renormalization group neural networks
- RG flow in deep learning
- neural criticality
- coarse-graining networks
- field theory machine learning
- Wilsonian RG pruning
- lattice regularization
- neural field theory
- continuum limit neural networks
- correlation length neural networks
- scaling exponents deep learning
- block spin transformation
- beta function neural networks
- RG-inspired pooling

### 中文
- 晶格场论神经网络
- 重整化群深度学习
- 神经临界性
- 粗粒化网络
- 场论机器学习
- 威尔逊剪枝
- 晶格正则化
- 神经场论
- 连续极限网络
- 关联长度
- 标度指数
- 块自旋变换
- β函数
- RG池化
- 离散连续桥梁
- 有限尺寸标度

---

## 7. Related Skills

- `lattice-rnn-pruning` — 基于偏序集的RNN格剪枝方法
- `energy-based-neurocomputation` — 能量基神经计算框架
- `attractor-metadynamics-neural` — 吸引子元动力学与慢适应过程
- `physics-guided-neural-networks` — 物理信息神经网络
- `quantum-neural-dynamics` — 量子神经动力学
- `neural-cellular-automata-attractors` — 神经细胞自动机吸引子
- `thermodynamic-brain-connectivity` — 热力学脑连接分析
- `brain-inspired-neural-cellular-automata` — 脑启发神经细胞自动机
- `snns-working-memory-heterogeneous-delays` — 异质延迟SNN工作记忆
- `quantum-ml-data-loading` — 量子机器学习数据加载

---

## References

1. Mehta, P. & Schwab, D.J. (2014). "An exact mapping between the Variational Renormalization Group and Deep Learning." arXiv:1410.3831
2. Lin, H.W., Tegmark, M. & Rolnick, D. (2017). "Why does deep and cheap learning work so well?" J. Stat. Phys. 168:1223–1247.
3. Koch-Janusz, M. & Ringel, Z. (2021). "Mutual-information relevant and irrelevant features and the renormalization group." arXiv:2103.09664
4. Gordon, J. et al. (2020). "On the scale-invariance and the renormalization group flow of neural networks." arXiv:2006.10473
5. Roberts, D.A., et al. (2021). "Teaching the neural network to renormalize." arXiv:2104.00991
6. Montvay, I. & Münster, G. (1994). "Quantum Fields on a Lattice." Cambridge University Press.
7. Jacquier, A. & Wiese, K.J. (2021). "Field theory of deep neural networks." arXiv:2103.04536
