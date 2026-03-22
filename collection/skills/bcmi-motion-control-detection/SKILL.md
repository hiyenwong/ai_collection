---
name: bcmi-motion-control-detection
description: BCMI驱动的运动控制检测方法论。基于EEG的高阶脑网络机器学习，使用交互熵量化动态协调。触发词：脑机音乐接口、运动控制检测、EEG机器学习、高阶脑网络、交互熵、BCMI、motor control detection、higher-order network、cross-information entropy。
user-invocable: true
---

# BCMI-Driven Motion Control Detection

基于EEG的高阶脑网络机器学习方法，用于音乐辅助模拟驾驶中的认知运动控制检测。

## 核心方法论

### 1. 高阶网络构建

使用基于EEG的交叉信息熵构建动态高阶网络模型：

```python
import numpy as np
from scipy import signal
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score

class HigherOrderBrainNetwork:
    """高阶脑网络分析框架"""
    
    def __init__(self, n_channels=64, order=3):
        self.n_channels = n_channels
        self.order = order
        
    def compute_cross_information_entropy(self, signal1, signal2, n_bins=20):
        """计算两信号间的交叉信息熵"""
        # 联合直方图
        hist_2d, x_edges, y_edges = np.histogram2d(
            signal1, signal2, bins=n_bins
        )
        
        # 归一化为概率
        pxy = hist_2d / hist_2d.sum()
        
        # 边缘分布
        px = pxy.sum(axis=1)
        py = pxy.sum(axis=0)
        
        # 互信息
        mi = 0.0
        for i in range(n_bins):
            for j in range(n_bins):
                if pxy[i, j] > 0 and px[i] > 0 and py[j] > 0:
                    mi += pxy[i, j] * np.log2(pxy[i, j] / (px[i] * py[j]))
        
        return mi
    
    def build_higher_order_network(self, eeg_data):
        """构建高阶脑网络
        
        Args:
            eeg_data: shape (n_channels, n_samples)
        
        Returns:
            高阶网络连接矩阵
        """
        n_channels = eeg_data.shape[0]
        
        # 二阶连接（成对交互）
        second_order = np.zeros((n_channels, n_channels))
        for i in range(n_channels):
            for j in range(i+1, n_channels):
                entropy = self.compute_cross_information_entropy(
                    eeg_data[i], eeg_data[j]
                )
                second_order[i, j] = entropy
                second_order[j, i] = entropy
        
        # 三阶连接（三元组交互）
        third_order = self._compute_third_order_connectivity(eeg_data)
        
        return {
            'second_order': second_order,
            'third_order': third_order
        }
    
    def _compute_third_order_connectivity(self, eeg_data):
        """计算三阶连接性"""
        n_channels = eeg_data.shape[0]
        n_triplets = n_channels * (n_channels - 1) * (n_channels - 2) // 6
        third_order = np.zeros((n_channels, n_channels, n_channels))
        
        for i in range(n_channels):
            for j in range(i+1, n_channels):
                for k in range(j+1, n_channels):
                    # 三变量交互信息
                    mi_ij = self.compute_cross_information_entropy(
                        eeg_data[i], eeg_data[j]
                    )
                    mi_jk = self.compute_cross_information_entropy(
                        eeg_data[j], eeg_data[k]
                    )
                    mi_ik = self.compute_cross_information_entropy(
                        eeg_data[i], eeg_data[k]
                    )
                    
                    # 高阶交互（协同/冗余）
                    triple_interaction = (mi_ij + mi_jk + mi_ik) / 3
                    third_order[i, j, k] = triple_interaction
                    third_order[i, k, j] = triple_interaction
                    third_order[j, i, k] = triple_interaction
        
        return third_order

    def extract_features(self, network):
        """提取高阶网络特征"""
        features = []
        
        # 二阶特征
        second_order = network['second_order']
        features.append(np.mean(second_order))
        features.append(np.std(second_order))
        features.append(np.max(second_order))
        
        # 三阶特征
        third_order = network['third_order']
        features.append(np.mean(third_order[third_order > 0]))
        features.append(np.std(third_order[third_order > 0]))
        features.append(np.max(third_order))
        
        # Phi值（高阶信息熵）
        phi = self._compute_phi(third_order)
        features.append(phi)
        
        return np.array(features)
    
    def _compute_phi(self, third_order):
        """计算高阶信息熵Phi值"""
        # 提取非零三阶连接
        nonzero = third_order[third_order > 0]
        if len(nonzero) == 0:
            return 0.0
        
        # 计算信息熵
        p = nonzero / nonzero.sum()
        phi = -np.sum(p * np.log2(p + 1e-10))
        return phi


class MotionControlClassifier:
    """运动状态分类器"""
    
    def __init__(self):
        self.network_builder = HigherOrderBrainNetwork()
        self.classifier = SVC(kernel='rbf', probability=True)
        
    def fit(self, eeg_data_list, labels):
        """训练分类器
        
        Args:
            eeg_data_list: EEG数据列表 [(n_channels, n_samples), ...]
            labels: 标签列表 (0: 基线驾驶, 1: 音乐刺激驾驶)
        """
        features_list = []
        for eeg_data in eeg_data_list:
            network = self.network_builder.build_higher_order_network(eeg_data)
            features = self.network_builder.extract_features(network)
            features_list.append(features)
        
        X = np.array(features_list)
        self.classifier.fit(X, labels)
        
    def predict(self, eeg_data):
        """预测运动控制状态"""
        network = self.network_builder.build_higher_order_network(eeg_data)
        features = self.network_builder.extract_features(network)
        return self.classifier.predict([features])[0]
    
    def predict_proba(self, eeg_data):
        """预测概率"""
        network = self.network_builder.build_higher_order_network(eeg_data)
        features = self.network_builder.extract_features(network)
        return self.classifier.predict_proba([features])[0]
```

### 2. 时序动态分析

```python
class DynamicNetworkAnalysis:
    """动态网络时序分析"""
    
    def __init__(self, window_size=500, step_size=100):
        self.window_size = window_size
        self.step_size = step_size
        
    def sliding_window_analysis(self, eeg_data, sampling_rate=250):
        """滑动窗口分析动态网络变化"""
        n_samples = eeg_data.shape[1]
        network_builder = HigherOrderBrainNetwork()
        
        results = []
        for start in range(0, n_samples - self.window_size, self.step_size):
            window_data = eeg_data[:, start:start + self.window_size]
            network = network_builder.build_higher_order_network(window_data)
            features = network_builder.extract_features(network)
            results.append({
                'time': start / sampling_rate,
                'features': features,
                'network': network
            })
        
        return results
    
    def detect_state_changes(self, results, threshold=0.3):
        """检测状态变化点"""
        features = np.array([r['features'] for r in results])
        
        # 计算特征变化率
        diff = np.diff(features, axis=0)
        change_magnitude = np.linalg.norm(diff, axis=1)
        
        # 检测显著变化
        change_points = np.where(change_magnitude > threshold)[0]
        
        return change_points, change_magnitude
```

## 应用场景

### 1. 脑机音乐接口（BCMI）
- 音乐刺激下的认知状态监测
- 实时运动控制反馈
- 音乐治疗应用

### 2. 驾驶疲劳检测
- 长时间驾驶的认知状态评估
- 音乐辅助驾驶效果验证
- 实时预警系统

### 3. 认知神经科学研究
- 高阶脑网络动态分析
- 多任务认知协调研究
- 音乐认知与运动控制交互

## 使用示例

```python
# 生成模拟EEG数据
n_channels = 64
n_samples = 5000
eeg_baseline = np.random.randn(n_channels, n_samples)
eeg_music = np.random.randn(n_channels, n_samples) * 1.2  # 音乐刺激下振幅增加

# 构建分类器
classifier = MotionControlClassifier()

# 训练（使用模拟数据）
training_data = [eeg_baseline, eeg_music] * 5
training_labels = [0, 1] * 5
classifier.fit(training_data, training_labels)

# 预测新数据
test_eeg = np.random.randn(n_channels, n_samples) * 1.1
prediction = classifier.predict(test_eeg)
probability = classifier.predict_proba(test_eeg)

print(f"预测状态: {'音乐刺激驾驶' if prediction == 1 else '基线驾驶'}")
print(f"置信度: {max(probability):.2%}")
```

## 参考文献

- arXiv:2603.15208 - BCMI-Driven Motion Control Detection: EEG-Based Machine Learning and Interaction Entropy for High-Order Brain Networks