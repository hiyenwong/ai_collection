---
name: entropy-brain-connectivity-paths
description: 使用熵测度识别脑连接路径的方法论。通过信息论工具（熵密度、有效测度复杂度、Lempel-Ziv距离）检测线性与非线性动态，无需预设参数或模型假设。适用于任务态fMRI分析、脑区连接发现、探索性研究。触发词：脑连接、熵测度、信息流、fMRI分析、非线性动态、brain connectivity、entropy、information flow、Lempel-Ziv。
user-invocable: true
---

# Entropy Measures for Brain Connectivity Paths

基于信息论的脑连接路径分析方法

## 核心方法论

**来源：** arXiv:2507.04442
**效用：** 0.91

### 问题背景

研究大脑在不同刺激下各脑区间的信息流动：
- 传统方法依赖预建立的参数、模型或先验假设
- 难以捕获非线性动态
- 脑在多个功能层面表现出显著的非线性交互

### 熵测度工具箱

| 工具 | 用途 | 优势 |
|------|------|------|
| **熵密度** | 评估信息创造 | 无模型、无参数 |
| **有效测度复杂度** | 检测模式涌现 | 捕获线性和非线性动态 |
| **Lempel-Ziv 距离** | 比较序列相似性 | 无需先验知识 |

### 实现框架

```python
import numpy as np
from typing import Dict, List, Tuple
from itertools import combinations
from collections import defaultdict

class EntropyBrainConnectivity:
    """
    基于熵测度的脑连接路径分析
    
    无需模型假设，检测线性和非线性动态
    """
    
    def __init__(self):
        self.results = {}
    
    def compute_entropy_density(
        self, 
        time_series: np.ndarray,
        bins: int = 10
    ) -> float:
        """
        计算熵密度
        
        熵密度 = -Σ p(x) log(p(x))
        
        参数:
            time_series: 时间序列数据
            bins: 直方图箱数
            
        返回:
            熵密度值
        """
        # 计算概率分布
        hist, _ = np.histogram(time_series, bins=bins, density=True)
        hist = hist[hist > 0]  # 移除零概率
        
        # 计算熵
        entropy = -np.sum(hist * np.log2(hist + 1e-10))
        
        return entropy
    
    def compute_effective_measure_complexity(
        self,
        time_series: np.ndarray,
        L_max: int = 20
    ) -> float:
        """
        计算有效测度复杂度 (EMC)
        
        EMC = Σ L × (h_L - h_{L+1})
        
        衡量序列的结构复杂程度
        
        参数:
            time_series: 时间序列
            L_max: 最大块长度
            
        返回:
            有效测度复杂度
        """
        # 符号化
        symbols = self._symbolize(time_series, n_symbols=4)
        
        emc = 0.0
        for L in range(1, min(L_max, len(symbols) - 1)):
            # 计算块熵
            h_L = self._block_entropy(symbols, L)
            h_L1 = self._block_entropy(symbols, L + 1)
            
            emc += L * (h_L - h_L1)
        
        return emc
    
    def lempel_ziv_distance(
        self,
        series1: np.ndarray,
        series2: np.ndarray,
        threshold: float = None
    ) -> float:
        """
        计算 Lempel-Ziv 距离
        
        衡量两个时间序列的复杂度差异
        用于检测不同脑区活动模式的相似性
        
        参数:
            series1: 时间序列1
            series2: 时间序列2
            threshold: 二值化阈值
            
        返回:
            LZ 距离
        """
        # 二值化
        if threshold is None:
            threshold = np.median(np.concatenate([series1, series2]))
        
        binary1 = (series1 > threshold).astype(int)
        binary2 = (series2 > threshold).astype(int)
        
        # 计算复杂度
        c1 = self._lz_complexity(binary1)
        c2 = self._lz_complexity(binary2)
        c12 = self._lz_complexity(np.concatenate([binary1, binary2]))
        
        # 归一化距离
        n1, n2 = len(series1), len(series2)
        distance = (c12 - min(c1, c2)) / max(c1, c2)
        
        return distance
    
    def _lz_complexity(self, binary_sequence: np.ndarray) -> int:
        """
        计算 Lempel-Ziv 复杂度
        
        计算序列中不同子串的数量
        """
        n = len(binary_sequence)
        if n == 0:
            return 0
        
        complexity = 1
        i = 0
        
        while i < n:
            # 寻找最长新子串
            j = i + 1
            while j < n:
                # 检查子串是否出现过
                substring = binary_sequence[i:j+1]
                found = False
                for k in range(i):
                    if np.array_equal(binary_sequence[k:k+len(substring)], substring):
                        found = True
                        break
                
                if not found:
                    break
                j += 1
            
            complexity += 1
            i = j
        
        return complexity
    
    def _symbolize(
        self, 
        time_series: np.ndarray, 
        n_symbols: int = 4
    ) -> np.ndarray:
        """
        将连续时间序列符号化
        """
        percentiles = np.linspace(0, 100, n_symbols + 1)[1:-1]
        thresholds = np.percentile(time_series, percentiles)
        
        symbols = np.zeros(len(time_series), dtype=int)
        for i, threshold in enumerate(thresholds):
            symbols[time_series > threshold] = i + 1
        
        return symbols
    
    def _block_entropy(self, symbols: np.ndarray, L: int) -> float:
        """
        计算块熵
        """
        if len(symbols) < L:
            return 0.0
        
        # 统计块频率
        blocks = defaultdict(int)
        n_blocks = len(symbols) - L + 1
        
        for i in range(n_blocks):
            block = tuple(symbols[i:i+L])
            blocks[block] += 1
        
        # 计算熵
        entropy = 0.0
        for count in blocks.values():
            p = count / n_blocks
            entropy -= p * np.log2(p)
        
        return entropy
    
    def analyze_connectivity_paths(
        self,
        fmri_data: np.ndarray,
        region_labels: List[str],
        threshold_distance: float = 0.5
    ) -> Dict:
        """
        分析脑区间的连接路径
        
        参数:
            fmri_data: fMRI 数据 (n_timepoints, n_regions)
            region_labels: 脑区标签
            threshold_distance: 连接阈值
            
        返回:
            连接路径分析结果
        """
        n_regions = fmri_data.shape[1]
        
        results = {
            'entropy_density': {},
            'emc': {},
            'connectivity_matrix': np.zeros((n_regions, n_regions)),
            'paths': []
        }
        
        # 计算每个脑区的熵测度
        for i, label in enumerate(region_labels):
            results['entropy_density'][label] = self.compute_entropy_density(
                fmri_data[:, i]
            )
            results['emc'][label] = self.compute_effective_measure_complexity(
                fmri_data[:, i]
            )
        
        # 计算脑区间连接（LZ距离）
        for i, j in combinations(range(n_regions), 2):
            distance = self.lempel_ziv_distance(
                fmri_data[:, i], fmri_data[:, j]
            )
            
            # 距离越小，连接越强
            similarity = 1.0 - distance
            results['connectivity_matrix'][i, j] = similarity
            results['connectivity_matrix'][j, i] = similarity
            
            # 记录显著连接
            if similarity > threshold_distance:
                results['paths'].append({
                    'from': region_labels[i],
                    'to': region_labels[j],
                    'strength': similarity
                })
        
        return results
    
    def detect_nonlinear_dynamics(
        self,
        time_series: np.ndarray,
        surrogate_n: int = 100
    ) -> Dict:
        """
        检测非线性动态
        
        通过与打乱 surrogate 对比，判断是否存在显著非线性
        
        参数:
            time_series: 时间序列
            surrogate_n: surrogate 数量
            
        返回:
            非线性检测结果
        """
        # 原始 EMC
        original_emc = self.compute_effective_measure_complexity(time_series)
        
        # 打乱 surrogate
        surrogate_emcs = []
        for _ in range(surrogate_n):
            shuffled = np.random.permutation(time_series)
            surrogate_emcs.append(
                self.compute_effective_measure_complexity(shuffled)
            )
        
        # 统计检验
        mean_surrogate = np.mean(surrogate_emcs)
        std_surrogate = np.std(surrogate_emcs)
        
        z_score = (original_emc - mean_surrogate) / (std_surrogate + 1e-10)
        
        return {
            'original_emc': original_emc,
            'surrogate_mean': mean_surrogate,
            'z_score': z_score,
            'has_nonlinear': abs(z_score) > 2.0
        }


class TaskBasedConnectivityAnalyzer:
    """
    任务态 fMRI 连接分析器
    
    针对不同认知任务（运动、工作记忆、情绪识别、语言）
    """
    
    def __init__(self):
        self.entropy_analyzer = EntropyBrainConnectivity()
    
    def analyze_task(
        self,
        fmri_data: np.ndarray,
        region_labels: List[str],
        task_name: str
    ) -> Dict:
        """
        分析特定任务下的脑连接
        """
        connectivity = self.entropy_analyzer.analyze_connectivity_paths(
            fmri_data, region_labels
        )
        
        # 任务特定的分析
        connectivity['task'] = task_name
        connectivity['summary'] = self._summarize_task(
            connectivity, task_name
        )
        
        return connectivity
    
    def compare_tasks(
        self,
        task_results: Dict[str, Dict]
    ) -> Dict:
        """
        比较不同任务下的连接模式
        """
        tasks = list(task_results.keys())
        comparison = {
            'entropy_changes': {},
            'path_differences': {}
        }
        
        for task1, task2 in combinations(tasks, 2):
            # 比较熵密度变化
            ed1 = task_results[task1]['entropy_density']
            ed2 = task_results[task2]['entropy_density']
            
            for region in ed1.keys():
                change = ed2[region] - ed1[region]
                comparison['entropy_changes'][(task1, task2, region)] = change
        
        return comparison
    
    def _summarize_task(self, connectivity: Dict, task: str) -> str:
        """
        生成任务摘要
        """
        n_paths = len(connectivity['paths'])
        avg_entropy = np.mean(list(connectivity['entropy_density'].values()))
        avg_emc = np.mean(list(connectivity['emc'].values()))
        
        summary = f"""
        任务: {task}
        检测到连接路径: {n_paths}
        平均熵密度: {avg_entropy:.4f}
        平均有效测度复杂度: {avg_emc:.4f}
        
        主要发现:
        - 高熵密度脑区: {self._top_regions(connectivity['entropy_density'], 3)}
        - 高复杂度脑区: {self._top_regions(connectivity['emc'], 3)}
        """
        
        return summary
    
    def _top_regions(self, metric: Dict, n: int) -> List[str]:
        """
        获取指标最高的脑区
        """
        sorted_regions = sorted(
            metric.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        return [r[0] for r in sorted_regions[:n]]
```

## 应用场景

### 1. 任务态 fMRI 分析
- 运动任务
- 工作记忆任务
- 情绪识别任务
- 语言任务

### 2. 探索性研究
- 发现新连接模式
- 无需先验假设
- 适合假设生成

### 3. 非线性动态检测
- 识别非线性脑交互
- surrogate 检验

## 方法优势

| 优势 | 说明 |
|------|------|
| **无模型** | 不依赖预设模型 |
| **无参数** | 无需调整参数 |
| **非线性** | 捕获非线性动态 |
| **探索性** | 适合发现新模式 |

## Activation Keywords
- 脑连接
- 熵测度
- 信息流
- fMRI分析
- 非线性动态
- brain connectivity
- entropy
- information flow
- Lempel-Ziv
- effective measure complexity

## Tools Used
- numpy
- scipy
- nibabel (fMRI 数据读取)

## Instructions for Agents
1. 理解信息论工具：熵、复杂度、LZ距离
2. 掌握符号化方法：将连续信号转换为离散符号
3. 计算块熵：衡量序列结构
4. 注意非线性检测：使用 surrogate 检验
5. 应用场景：任务态 fMRI、探索性研究

## Examples
```python
# 使用示例
from entropy_brain_connectivity import EntropyBrainConnectivity, TaskBasedConnectivityAnalyzer

# 1. 创建分析器
analyzer = EntropyBrainConnectivity()

# 2. 计算熵密度
entropy = analyzer.compute_entropy_density(time_series)

# 3. 计算有效测度复杂度
emc = analyzer.compute_effective_measure_complexity(time_series)

# 4. 分析连接路径
results = analyzer.analyze_connectivity_paths(fmri_data, region_labels)

# 5. 检测非线性动态
nonlinear = analyzer.detect_nonlinear_dynamics(time_series)

# 6. 任务分析
task_analyzer = TaskBasedConnectivityAnalyzer()
motor_results = task_analyzer.analyze_task(fmri_motor, regions, "motor")
memory_results = task_analyzer.analyze_task(fmri_memory, regions, "working_memory")

# 7. 比较任务
comparison = task_analyzer.compare_tasks({
    "motor": motor_results,
    "memory": memory_results
})
```

## 参考文献
- Estévez-Rams, E., et al. (2025). "Entropy measures as indicators of connectivity paths in the human brain" arXiv:2507.04442
- Lempel, A., & Ziv, J. (1976). "On the complexity of finite sequences" IEEE Transactions on Information Theory