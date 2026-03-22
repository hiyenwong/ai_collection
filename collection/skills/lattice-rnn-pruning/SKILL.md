---
name: lattice-rnn-pruning
description: 基于格论的RNN剪枝方法论。将RNN建模为偏序集，构建依赖格，识别不可约元进行选择性剪枝。相比传统幅度剪枝更好地保留功能连接性。触发词：RNN剪枝、格剪枝、偏序集、依赖格、不可约元、网络压缩、lattice pruning、poset、meet irreducible。
user-invocable: true
---

# 基于格论的RNN剪枝

基于 arXiv:2502.16525 - "Lattice-Based Pruning in Recurrent Neural Networks via Poset Modeling"

## 核心方法论

### 1. 偏序集建模

将RNN建模为偏序集(Partially Ordered Set, Poset)：
- 神经元作为元素
- 连接关系定义偏序
- 保留结构依赖关系

```python
import numpy as np
from collections import defaultdict
from itertools import combinations

class PosetRNN:
    """
    将RNN建模为偏序集
    """
    
    def __init__(self, n_hidden, n_input=1, n_output=1):
        """
        参数:
            n_hidden: 隐藏层神经元数量
            n_input: 输入维度
            n_output: 输出维度
        """
        self.n_hidden = n_hidden
        self.n_input = n_input
        self.n_output = n_output
        
        # 权重矩阵
        self.W_hh = np.random.randn(n_hidden, n_hidden) * 0.1  # 隐藏-隐藏
        self.W_ih = np.random.randn(n_hidden, n_input) * 0.1    # 输入-隐藏
        self.W_ho = np.random.randn(n_output, n_hidden) * 0.1  # 隐藏-输出
        
        # 偏序关系 (依赖关系)
        self.dependency = defaultdict(set)
        
    def build_dependency_relation(self):
        """
        构建依赖关系
        
        节点i依赖于节点j，如果存在从j到i的非零连接
        """
        # 隐藏层内部依赖
        for i in range(self.n_hidden):
            for j in range(self.n_hidden):
                if np.abs(self.W_hh[i, j]) > 1e-6:
                    self.dependency[i].add(j)
        
        return self.dependency
    
    def partial_order(self, a, b):
        """
        偏序比较: a ≤ b if b depends on a (directly or indirectly)
        
        返回:
            -1: a < b
            0: a || b (不可比较)
            1: a > b
        """
        if a == b:
            return 0
        
        # 检查传递依赖
        def depends_on(x, y, visited=None):
            if visited is None:
                visited = set()
            if x == y:
                return True
            if x in visited:
                return False
            visited.add(x)
            return any(depends_on(z, y, visited) for z in self.dependency.get(x, set()))
        
        if depends_on(b, a):
            return -1  # a < b
        elif depends_on(a, b):
            return 1   # a > b
        else:
            return 0   # 不可比较


class DependencyLattice:
    """
    依赖格构建器
    """
    
    def __init__(self, poset):
        """
        参数:
            poset: PosetRNN实例
        """
        self.poset = poset
        self.n_hidden = poset.n_hidden
        self.lattice = {}
        
    def build_lattice(self):
        """
        从偏序集构建格
        
        格元素 = 神经元子集，满足特定的依赖闭包性质
        """
        # 识别所有下集(downsets)
        downsets = self._compute_all_downsets()
        
        # 格的元素 = 所有下集
        self.lattice = {frozenset(s): s for s in downsets}
        
        return self.lattice
    
    def _compute_all_downsets(self):
        """
        计算所有下集
        
        下集S：如果x ∈ S且y ≤ x，则y ∈ S
        """
        all_elements = set(range(self.n_hidden))
        downsets = [set()]  # 空集是最小的下集
        
        # BFS构造下集
        for element in all_elements:
            # 找到该元素的下闭包
            down_closure = self._down_closure(element)
            downsets.append(down_closure)
            
            # 组合现有下集
            for existing in list(downsets):
                combined = existing | down_closure
                # 验证是否为有效下集
                if self._is_downset(combined):
                    if combined not in downsets:
                        downsets.append(combined)
        
        return downsets
    
    def _down_closure(self, element):
        """计算元素的向下闭包"""
        closure = {element}
        stack = [element]
        
        while stack:
            current = stack.pop()
            for dep in self.poset.dependency.get(current, set()):
                if dep not in closure:
                    closure.add(dep)
                    stack.append(dep)
        
        return closure
    
    def _is_downset(self, subset):
        """验证是否为下集"""
        for x in subset:
            for dep in self.poset.dependency.get(x, set()):
                if dep not in subset:
                    return False
        return True
    
    def meet(self, s1, s2):
        """
        格的meet运算（最大下界）
        
        s1 ∧ s2 = s1 ∩ s2
        """
        return s1 & s2
    
    def join(self, s1, s2):
        """
        格的join运算（最小上界）
        
        s1 ∨ s2 = s1 ∪ s2 的下闭包
        """
        union = s1 | s2
        return self._compute_downset(union)
    
    def _compute_downset(self, subset):
        """计算子集的下闭包"""
        downset = set(subset)
        for x in list(subset):
            downset |= self._down_closure(x)
        return downset


class MeetIrreduciblePruner:
    """
    基于不可约元的剪枝器
    """
    
    def __init__(self, rnn):
        """
        参数:
            rnn: 训练好的RNN模型
        """
        self.rnn = rnn
        self.poset = PosetRNN(rnn.hidden_size if hasattr(rnn, 'hidden_size') else rnn.n_hidden)
        self.poset.W_hh = rnn.W_hh if hasattr(rnn, 'W_hh') else rnn.weight_hh_l0.detach().numpy()
        self.poset.build_dependency_relation()
        
    def identify_meet_irreducibles(self):
        """
        识别meet不可约元
        
        定义：格元素a是meet不可约的，如果a ≠ 1（最大元），
        且对于所有b, c，a = b ∧ c 蕴含 a = b 或 a = c
        
        简化：在神经元格中，meet不可约元对应于"关键神经元"
        """
        lattice = DependencyLattice(self.poset)
        lattice.build_lattice()
        
        meet_irreducibles = []
        
        # 对每个神经元计算其重要性
        importance = self._compute_importance()
        
        for neuron in range(self.poset.n_hidden):
            # 计算该神经元的"不可替代性"
            irreplaceability = self._compute_irreplaceability(neuron, importance)
            
            if irreplaceability > 0.5:  # 阈值
                meet_irreducibles.append(neuron)
        
        return meet_irreducibles, importance
    
    def _compute_importance(self):
        """
        计算神经元重要性
        
        基于：
        1. 权重幅度
        2. 激活频率
        3. 连接度
        """
        W = self.poset.W_hh
        
        # 权重幅度
        weight_importance = np.sum(np.abs(W), axis=1) + np.sum(np.abs(W), axis=0)
        
        # 连接度
        out_degree = np.sum(np.abs(W) > 1e-6, axis=1)
        in_degree = np.sum(np.abs(W) > 1e-6, axis=0)
        connectivity = out_degree + in_degree
        
        # 综合重要性
        importance = weight_importance / np.max(weight_importance) + \
                     connectivity / np.max(connectivity)
        
        return importance / np.max(importance)
    
    def _compute_irreplaceability(self, neuron, importance):
        """
        计算神经元的不可替代性
        
        高不可替代性 = meet不可约元候选
        """
        # 检查该神经元是否是某些依赖路径的唯一桥梁
        W = self.poset.W_hh
        
        # 出边和入边强度
        out_strength = np.sum(np.abs(W[neuron, :]))
        in_strength = np.sum(np.abs(W[:, neuron]))
        
        # 检查是否连接不连通的组件
        dependents = self.poset.dependency.get(neuron, set())
        providers = set()
        for i in range(self.poset.n_hidden):
            if neuron in self.poset.dependency.get(i, set()):
                providers.add(i)
        
        # 独特性分数
        uniqueness = 1 - len(dependents & providers) / max(len(dependents | providers), 1)
        
        # 综合不可替代性
        irreplaceability = importance[neuron] * (0.5 + 0.5 * uniqueness)
        
        return irreplaceability
    
    def prune(self, target_sparsity=0.5):
        """
        执行剪枝
        
        参数:
            target_sparsity: 目标稀疏度 (保留神经元比例)
        
        返回:
            pruned_weights: 剪枝后的权重矩阵
            kept_neurons: 保留的神经元索引
        """
        meet_irreducibles, importance = self.identify_meet_irreducibles()
        
        n_keep = int(self.poset.n_hidden * target_sparsity)
        
        # 确保meet不可约元被保留
        candidates = list(range(self.poset.n_hidden))
        
        # 按重要性排序，但meet不可约元优先
        sorted_neurons = sorted(candidates, 
                               key=lambda x: (x in meet_irreducibles, importance[x]),
                               reverse=True)
        
        kept_neurons = sorted(sorted_neurons[:n_keep])
        
        # 创建剪枝后的权重矩阵
        W_pruned = np.zeros((n_keep, n_keep))
        
        for i, ni in enumerate(kept_neurons):
            for j, nj in enumerate(kept_neurons):
                W_pruned[i, j] = self.poset.W_hh[ni, nj]
        
        return W_pruned, kept_neurons, meet_irreducibles
```

### 2. 多层网络剪枝

```python
class MultiLayerLatticePruner:
    """
    多层RNN格剪枝器
    
    支持自顶向下反馈的多层网络
    """
    
    def __init__(self, layers):
        """
        参数:
            layers: RNN层列表 [(n_hidden, W_hh, W_ih), ...]
        """
        self.layers = layers
        self.n_layers = len(layers)
        self.pruners = []
        
        for layer in layers:
            n_hidden, W_hh, W_ih = layer
            # 创建临时RNN对象
            class TempRNN:
                def __init__(self, n, W, W_in):
                    self.n_hidden = n
                    self.W_hh = W
                    self.W_ih = W_in
            
            rnn = TempRNN(n_hidden, W_hh, W_ih)
            self.pruners.append(MeetIrreduciblePruner(rnn))
    
    def hierarchical_prune(self, target_sparsities):
        """
        分层剪枝
        
        考虑层间依赖关系
        """
        pruned_layers = []
        kept_indices = []
        
        for i, (pruner, sparsity) in enumerate(zip(self.pruners, target_sparsities)):
            W_pruned, kept, irreducibles = pruner.prune(sparsity)
            pruned_layers.append({
                'weights': W_pruned,
                'kept_neurons': kept,
                'irreducibles': irreducibles
            })
            kept_indices.append(kept)
            
            # 更新下一层的输入连接
            if i < self.n_layers - 1:
                self._update_next_layer_input(i, kept)
        
        return pruned_layers, kept_indices
    
    def _update_next_layer_input(self, layer_idx, kept_neurons):
        """更新下一层的输入权重矩阵"""
        if layer_idx >= self.n_layers - 1:
            return
        
        # 创建映射：原始索引 -> 剪枝后索引
        n_hidden, W_hh, W_ih = self.layers[layer_idx + 1]
        
        # 剪枝输入连接
        if layer_idx == 0:
            # 第一层的输入维度不变
            pass
        else:
            # 后续层需要调整输入
            kept_prev = kept_neurons
            new_W_ih = W_ih[:, kept_prev]
            self.layers[layer_idx + 1] = (n_hidden, W_hh, new_W_ih)


def evaluate_pruning_performance(original_rnn, pruned_weights, kept_neurons, 
                                  test_data, test_labels):
    """
    评估剪枝后性能
    
    返回准确率和稀疏度
    """
    # 在测试数据上评估
    # 这里需要根据具体的RNN实现进行适配
    
    sparsity = 1 - len(kept_neurons) / original_rnn.n_hidden
    
    # 简化评估：计算权重重构误差
    reconstruction_error = 0
    total_elements = 0
    
    for i, ni in enumerate(kept_neurons):
        for j, nj in enumerate(kept_neurons):
            original = original_rnn.W_hh[ni, nj]
            pruned = pruned_weights[i, j]
            reconstruction_error += (original - pruned) ** 2
            total_elements += 1
    
    mse = reconstruction_error / max(total_elements, 1)
    
    return {
        'sparsity': sparsity,
        'mse': mse,
        'kept_neurons': len(kept_neurons),
        'total_neurons': original_rnn.n_hidden
    }
```

### 3. 连续值邻接矩阵

```python
class ContinuousLatticePruner:
    """
    连续值邻接矩阵的格剪枝
    
    使用软阈值而非硬删除
    """
    
    def __init__(self, W_hh):
        self.W = W_hh
        self.n = W_hh.shape[0]
    
    def compute_laplacian(self):
        """计算图拉普拉斯矩阵"""
        D = np.diag(np.sum(np.abs(self.W), axis=1))
        L = D - np.abs(self.W)
        return L
    
    def spectral_importance(self, k=10):
        """
        谱重要性
        
        基于特征向量计算神经元重要性
        """
        L = self.compute_laplacian()
        eigenvalues, eigenvectors = np.linalg.eigh(L)
        
        # 使用前k个最小非零特征值对应的特征向量
        importance = np.zeros(self.n)
        
        for i in range(min(k, self.n)):
            if eigenvalues[i] > 1e-10:
                importance += np.abs(eigenvectors[:, i]) / eigenvalues[i]
        
        return importance / np.max(importance)
    
    def soft_prune(self, threshold=0.1):
        """
        软剪枝：将弱连接缩小而非删除
        """
        importance = self.spectral_importance()
        
        # 创建缩放矩阵
        scale = np.outer(importance, importance)
        
        # 应用软剪枝
        W_pruned = self.W * scale
        
        # 小于阈值的连接置零
        W_pruned[np.abs(W_pruned) < threshold * np.max(np.abs(self.W))] = 0
        
        return W_pruned, importance
```

## 应用场景

### 1. 模型压缩
- RNN模型压缩与加速
- 边缘设备部署优化

### 2. 神经网络分析
- 理解网络结构重要性
- 识别关键神经元

### 3. 神经科学建模
- 生物神经网络简化
- 突触修剪机制研究

## Activation Keywords
- RNN剪枝
- 格剪枝
- 偏序集
- 依赖格
- 不可约元
- 网络压缩
- lattice pruning
- poset
- meet irreducible
- 模型压缩
- 结构剪枝

## Tools Used
- numpy
- pytorch

## Instructions for Agents
1. 理解偏序集建模：神经元作为元素，连接定义偏序
2. 构建依赖格：从偏序集计算下集
3. 识别meet不可约元：关键神经元，剪枝时必须保留
4. 计算神经元重要性：基于权重幅度和连接度
5. 注意保留功能连接性，而非仅基于幅度剪枝

## Examples
```python
# 使用示例
from lattice_rnn_pruning import PosetRNN, MeetIrreduciblePruner

# 1. 创建RNN和偏序集
rnn = PosetRNN(n_hidden=100)
rnn.build_dependency_relation()

# 2. 创建剪枝器
pruner = MeetIrreduciblePruner(trained_rnn)

# 3. 识别关键神经元
irreducibles, importance = pruner.identify_meet_irreducibles()
print(f"关键神经元数量: {len(irreducibles)}")

# 4. 执行剪枝
W_pruned, kept_neurons, irreducibles = pruner.prune(target_sparsity=0.5)
print(f"保留神经元: {len(kept_neurons)}/{100}")
```

## 参考文献

- Sengupta, R. et al. (2025). "Lattice-Based Pruning in Recurrent Neural Networks via Poset Modeling" arXiv:2502.16525