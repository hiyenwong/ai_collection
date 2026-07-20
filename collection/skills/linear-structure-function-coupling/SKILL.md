---
name: linear-structure-function-coupling
description: 脑结构-功能耦合线性生成框架。从扩散加权成像(DWI)结构连接预测静息态fMRI功能连接，揭示整合枢纽和中介枢纽的机制，支持虚拟损伤实验。适用于脑连接组学、神经影像分析、结构-功能关系研究。触发词：结构功能耦合、脑连接组、结构连接、功能连接、整合枢纽、structure-function coupling、structural connectivity、functional connectivity、integrator hub、mediator hub。
user-invocable: true
---

# 脑结构-功能耦合线性生成框架

**来源论文：** arXiv:2507.06136 - A Linear Generative Framework for Structure-Function Coupling in the Human Brain

## 核心方法论

### 1. 结构-功能耦合问题

**结构连接 (SC)：** 白质通路网络（DWI 测量）

**功能连接 (FC)：** 脑区神经活动相关性（rs-fMRI 测量）

**核心问题：** 结构架构如何塑造功能模式？

### 2. 线性生成模型

**核心方程：**

\[
FC = \sum_{k} \alpha_k \cdot M_k(SC)
\]

其中：
- \(M_k\) - 结构动机（motif）变换
- \(\alpha_k\) - 权重系数
- 通过直接/间接通路预测 FC

### 3. 枢纽分类

| 类型 | 功能 | 作用 |
|------|------|------|
| **整合枢纽** | 结构支点 | 促进同步 |
| **中介枢纽** | 结构杠杆 | 协调竞争动力学 |

### 4. 虚拟损伤实验

预测连接破坏如何级联影响功能网络

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict
from scipy import stats
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


@dataclass
class StructureFunctionConfig:
    """结构-功能耦合配置"""
    n_regions: int = 100           # 脑区数量
    n_motifs: int = 5              # 结构动机数量
    
    # 模型参数
    regularization: float = 1.0    # 正则化参数
    
    # 枢纽识别
    hub_threshold: float = 0.8     # 枢纽阈值（百分位）


class StructuralMotifExtractor:
    """结构动机提取器"""
    
    def __init__(self, config: StructureFunctionConfig):
        self.config = config
        
    def extract_direct_connections(self, SC: np.ndarray) -> np.ndarray:
        """提取直接连接动机
        
        Args:
            SC: 结构连接矩阵
            
        Returns:
            direct: 直接连接动机
        """
        return SC.copy()
    
    def extract_indirect_connections(self, 
                                      SC: np.ndarray,
                                      max_path_length: int = 3) -> List[np.ndarray]:
        """提取间接连接动机
        
        Args:
            SC: 结构连接矩阵
            max_path_length: 最大路径长度
            
        Returns:
            indirect_motifs: 间接连接动机列表
        """
        motifs = []
        
        # 2步路径
        path_2 = SC @ SC
        motifs.append(path_2 / (path_2.max() + 1e-10))
        
        # 3步路径
        if max_path_length >= 3:
            path_3 = SC @ path_2
            motifs.append(path_3 / (path_3.max() + 1e-10))
            
        return motifs
    
    def extract_triadic_motifs(self, SC: np.ndarray) -> np.ndarray:
        """提取三元动机
        
        Args:
            SC: 结构连接矩阵
            
        Returns:
            triadic: 三元动机
        """
        n = SC.shape[0]
        triadic = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                # 计算 i→j 的三元动机强度
                for k in range(n):
                    if k != i and k != j:
                        triadic[i, j] += SC[i, k] * SC[k, j]
                        
        return triadic / (triadic.max() + 1e-10)
    
    def extract_all_motifs(self, SC: np.ndarray) -> np.ndarray:
        """提取所有结构动机
        
        Args:
            SC: 结构连接矩阵
            
        Returns:
            motifs: 动机矩阵 (n_motifs, n_regions, n_regions)
        """
        motifs = []
        
        # 直接连接
        motifs.append(self.extract_direct_connections(SC))
        
        # 间接连接
        indirect = self.extract_indirect_connections(SC)
        motifs.extend(indirect)
        
        # 三元动机
        motifs.append(self.extract_triadic_motifs(SC))
        
        return np.array(motifs)


class LinearGenerativeModel:
    """线性生成模型"""
    
    def __init__(self, config: StructureFunctionConfig):
        self.config = config
        self.motif_extractor = StructuralMotifExtractor(config)
        
        # 模型权重
        self.weights = None
        self.motifs = None
        
    def fit(self, SC: np.ndarray, FC: np.ndarray) -> Dict:
        """拟合模型
        
        Args:
            SC: 结构连接矩阵 (n_regions, n_regions)
            FC: 功能连接矩阵 (n_regions, n_regions)
            
        Returns:
            training_info: 训练信息
        """
        # 提取动机
        self.motifs = self.motif_extractor.extract_all_motifs(SC)
        n_motifs = len(self.motifs)
        
        # 准备训练数据
        n_regions = SC.shape[0]
        
        # 展平动机
        X = self.motifs.reshape(n_motifs, -1).T  # (n_regions^2, n_motifs)
        y = FC.flatten()  # (n_regions^2,)
        
        # 岭回归
        model = Ridge(alpha=self.config.regularization)
        model.fit(X, y)
        
        self.weights = model.coef_
        
        # 交叉验证
        cv_scores = cross_val_score(model, X, y, cv=5)
        
        return {
            'weights': self.weights,
            'cv_score_mean': cv_scores.mean(),
            'cv_score_std': cv_scores.std(),
            'n_motifs': n_motifs
        }
    
    def predict(self, SC: np.ndarray) -> np.ndarray:
        """预测功能连接
        
        Args:
            SC: 结构连接矩阵
            
        Returns:
            FC_pred: 预测的功能连接
        """
        if self.weights is None:
            raise ValueError("Model not fitted. Call fit() first.")
            
        # 提取动机
        motifs = self.motif_extractor.extract_all_motifs(SC)
        
        # 加权组合
        FC_pred = np.zeros((SC.shape[0], SC.shape[0]))
        
        for i, w in enumerate(self.weights):
            if i < len(motifs):
                FC_pred += w * motifs[i]
                
        # 对称化
        FC_pred = (FC_pred + FC_pred.T) / 2
        
        return FC_pred
    
    def compute_prediction_accuracy(self,
                                     FC_true: np.ndarray,
                                     FC_pred: np.ndarray) -> Dict:
        """计算预测准确度
        
        Args:
            FC_true: 真实 FC
            FC_pred: 预测 FC
            
        Returns:
            accuracy: 准确度指标
        """
        # 展平
        true = FC_true.flatten()
        pred = FC_pred.flatten()
        
        # 移除对角线
        n = FC_true.shape[0]
        mask = ~np.eye(n, dtype=bool)
        
        true_masked = true[mask.flatten()]
        pred_masked = pred[mask.flatten()]
        
        # 相关系数
        correlation = np.corrcoef(true_masked, pred_masked)[0, 1]
        
        # R²
        r2 = 1 - np.sum((true_masked - pred_masked)**2) / np.sum((true_masked - true_masked.mean())**2)
        
        return {
            'correlation': correlation,
            'r2': r2,
            'rmse': np.sqrt(np.mean((true_masked - pred_masked)**2))
        }


class HubClassifier:
    """枢纽分类器"""
    
    def __init__(self, config: StructureFunctionConfig):
        self.config = config
        
    def classify_hubs(self, 
                      SC: np.ndarray,
                      FC: np.ndarray) -> Dict:
        """分类枢纽
        
        Args:
            SC: 结构连接矩阵
            FC: 功能连接矩阵
            
        Returns:
            classification: 分类结果
        """
        n = SC.shape[0]
        
        # 计算节点强度
        sc_strength = SC.sum(axis=1) + SC.sum(axis=0)
        fc_strength = FC.sum(axis=1) + FC.sum(axis=0)
        
        # 计算参与系数
        participation = self._compute_participation_coefficient(SC)
        
        # 识别枢纽
        sc_threshold = np.percentile(sc_strength, self.config.hub_threshold * 100)
        hub_mask = sc_strength >= sc_threshold
        
        # 分类
        integrator_hubs = []
        mediator_hubs = []
        
        for i in range(n):
            if hub_mask[i]:
                # 高参与系数 → 整合枢纽
                # 低参与系数但高强度 → 中介枢纽
                if participation[i] > np.median(participation[hub_mask]):
                    integrator_hubs.append(i)
                else:
                    mediator_hubs.append(i)
                    
        return {
            'integrator_hubs': integrator_hubs,
            'mediator_hubs': mediator_hubs,
            'sc_strength': sc_strength,
            'fc_strength': fc_strength,
            'participation': participation
        }
    
    def _compute_participation_coefficient(self, SC: np.ndarray) -> np.ndarray:
        """计算参与系数
        
        Args:
            SC: 结构连接矩阵
            
        Returns:
            participation: 参与系数
        """
        n = SC.shape[0]
        
        # 简化的社区检测（使用模块度优化）
        # 这里用度排序作为代理
        degree = SC.sum(axis=1)
        
        # 分成两个社区
        sorted_indices = np.argsort(degree)
        community = np.zeros(n, dtype=int)
        community[sorted_indices[n//2:]] = 1
        
        # 计算参与系数
        participation = np.zeros(n)
        
        for i in range(n):
            s = SC[i, :].sum()
            if s == 0:
                continue
                
            # 每个社区的连接比例
            for c in [0, 1]:
                s_c = SC[i, community == c].sum()
                p_c = s_c / s
                participation[i] += p_c**2
                
            participation[i] = 1 - participation[i]
            
        return participation


class VirtualLesionExperiment:
    """虚拟损伤实验"""
    
    def __init__(self, model: LinearGenerativeModel):
        self.model = model
        
    def simulate_lesion(self,
                        SC: np.ndarray,
                        lesion_region: int) -> np.ndarray:
        """模拟损伤
        
        Args:
            SC: 结构连接矩阵
            lesion_region: 损伤脑区
            
        Returns:
            SC_lesioned: 损伤后的结构连接
        """
        SC_lesioned = SC.copy()
        
        # 移除该区域的所有连接
        SC_lesioned[lesion_region, :] = 0
        SC_lesioned[:, lesion_region] = 0
        
        return SC_lesioned
    
    def analyze_cascade_effect(self,
                                SC: np.ndarray,
                                FC_original: np.ndarray,
                                lesion_regions: List[int]) -> Dict:
        """分析级联效应
        
        Args:
            SC: 结构连接矩阵
            FC_original: 原始功能连接
            lesion_regions: 损伤脑区列表
            
        Returns:
            cascade: 级联效应分析
        """
        results = []
        
        for region in lesion_regions:
            # 模拟损伤
            SC_lesioned = self.simulate_lesion(SC, region)
            
            # 预测新的 FC
            FC_pred = self.model.predict(SC_lesioned)
            
            # 计算变化
            fc_change = FC_pred - FC_original
            global_change = np.mean(np.abs(fc_change))
            
            # 局部变化
            local_change = np.mean(np.abs(fc_change[region, :]))
            
            results.append({
                'lesion_region': region,
                'global_fc_change': global_change,
                'local_fc_change': local_change,
                'fc_predicted': FC_pred
            })
            
        return {
            'lesion_results': results,
            'most_disruptive_region': max(results, 
                                         key=lambda x: x['global_fc_change'])['lesion_region']
        }


def visualize_structure_function_coupling(SC: np.ndarray,
                                           FC: np.ndarray,
                                           FC_pred: np.ndarray):
    """可视化结构-功能耦合"""
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 结构连接
    ax = axes[0, 0]
    im = ax.imshow(SC, cmap='hot')
    ax.set_title('Structural Connectivity (SC)')
    ax.set_xlabel('Brain Region')
    ax.set_ylabel('Brain Region')
    plt.colorbar(im, ax=ax)
    
    # 2. 真实功能连接
    ax = axes[0, 1]
    im = ax.imshow(FC, cmap='coolwarm', vmin=-1, vmax=1)
    ax.set_title('Functional Connectivity (FC) - True')
    ax.set_xlabel('Brain Region')
    ax.set_ylabel('Brain Region')
    plt.colorbar(im, ax=ax)
    
    # 3. 预测功能连接
    ax = axes[1, 0]
    im = ax.imshow(FC_pred, cmap='coolwarm', vmin=-1, vmax=1)
    ax.set_title('FC - Predicted')
    ax.set_xlabel('Brain Region')
    ax.set_ylabel('Brain Region')
    plt.colorbar(im, ax=ax)
    
    # 4. 预测 vs 真实
    ax = axes[1, 1]
    n = SC.shape[0]
    mask = ~np.eye(n, dtype=bool)
    ax.scatter(FC[mask], FC_pred[mask], alpha=0.3, s=10)
    ax.plot([-1, 1], [-1, 1], 'r--', label='Identity')
    ax.set_xlabel('True FC')
    ax.set_ylabel('Predicted FC')
    ax.set_title(f'Prediction Accuracy: r={np.corrcoef(FC[mask], FC_pred[mask])[0,1]:.3f}')
    ax.legend()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('structure_function_coupling.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'structure_function_coupling.png'


# 使用示例
def example_structure_function_coupling():
    """示例：结构-功能耦合分析"""
    print("="*60)
    print("脑结构-功能耦合线性生成框架")
    print("="*60)
    
    config = StructureFunctionConfig(n_regions=100)
    
    # 生成模拟数据
    n = config.n_regions
    
    # 结构连接（稀疏）
    SC = np.random.rand(n, n) * 0.3
    SC = (SC + SC.T) / 2
    SC[np.random.rand(n, n) > 0.1] = 0  # 稀疏化
    np.fill_diagonal(SC, 0)
    
    # 功能连接（基于 SC 加噪声）
    FC = SC @ SC + np.random.randn(n, n) * 0.1
    FC = (FC + FC.T) / 2
    np.fill_diagonal(FC, 0)
    FC = FC / (np.abs(FC).max() + 1e-10)
    
    # 创建模型
    model = LinearGenerativeModel(config)
    
    # 拟合
    print("\n拟合模型...")
    training_info = model.fit(SC, FC)
    print(f"  动机数量: {training_info['n_motifs']}")
    print(f"  CV 分数: {training_info['cv_score_mean']:.3f} ± {training_info['cv_score_std']:.3f}")
    
    # 预测
    print("\n预测功能连接...")
    FC_pred = model.predict(SC)
    
    # 评估
    accuracy = model.compute_prediction_accuracy(FC, FC_pred)
    print(f"  相关系数: {accuracy['correlation']:.3f}")
    print(f"  R²: {accuracy['r2']:.3f}")
    print(f"  RMSE: {accuracy['rmse']:.3f}")
    
    # 枢纽分类
    print("\n枢纽分类...")
    classifier = HubClassifier(config)
    classification = classifier.classify_hubs(SC, FC)
    print(f"  整合枢纽: {len(classification['integrator_hubs'])} 个")
    print(f"  中介枢纽: {len(classification['mediator_hubs'])} 个")
    
    # 虚拟损伤
    print("\n虚拟损伤实验...")
    lesion_exp = VirtualLesionExperiment(model)
    cascade = lesion_exp.analyze_cascade_effect(
        SC, FC,
        classification['integrator_hubs'][:3]
    )
    print(f"  最具破坏性区域: {cascade['most_disruptive_region']}")
    
    print(f"\n关键发现:")
    print(f"  ✅ 线性模型预测 FC")
    print(f"  ✅ 识别整合/中介枢纽")
    print(f"  ✅ 虚拟损伤预测级联效应")
    
    return model


## Activation Keywords
- 结构功能耦合
- 脑连接组
- 结构连接
- 功能连接
- 整合枢纽
- structure-function coupling
- structural connectivity
- functional connectivity
- integrator hub
- mediator hub

## Tools Used
- numpy
- scipy
- sklearn

## Instructions for Agents
1. 从 DWI 提取结构连接矩阵
2. 从 rs-fMRI 提取功能连接矩阵
3. 提取结构动机（直接/间接/三元）
4. 拟合线性生成模型
5. 识别整合枢纽和中介枢纽
6. 进行虚拟损伤实验预测级联效应

## Examples
```python
# 结构-功能耦合分析示例
from linear_structure_function_coupling import (
    LinearGenerativeModel, HubClassifier,
    VirtualLesionExperiment, StructureFunctionConfig
)

# 1. 配置
config = StructureFunctionConfig(n_regions=100)

# 2. 创建模型
model = LinearGenerativeModel(config)

# 3. 拟合
training_info = model.fit(SC, FC)

# 4. 预测
FC_pred = model.predict(SC)

# 5. 评估
accuracy = model.compute_prediction_accuracy(FC, FC_pred)
print(f"相关系数: {accuracy['correlation']:.3f}")

# 6. 枢纽分类
classifier = HubClassifier(config)
hubs = classifier.classify_hubs(SC, FC)

# 7. 虚拟损伤
lesion_exp = VirtualLesionExperiment(model)
cascade = lesion_exp.analyze_cascade_effect(SC, FC, hubs['integrator_hubs'])
```

if __name__ == "__main__":
    example_structure_function_coupling()
```

## Related Skills

- `brain-network-controllability` - 脑网络可控性
- `generative-brain-dynamics-models` - 脑动力学生成模型
- `time-varying-brain-connectivity` - 时变脑连接

## References

- arXiv:2507.06136 - A Linear Generative Framework for Structure-Function Coupling in the Human Brain
- Topics: Neurons and Cognition (q-bio.NC), Quantitative Methods (q-bio.QM)