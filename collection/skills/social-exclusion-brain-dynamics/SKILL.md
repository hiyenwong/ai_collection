---
name: social-exclusion-brain-dynamics
description: 社会排斥中的全局脑动力学分析方法。使用功能连接预测社会行为一致性，结合心智化网络和社会疼痛网络分析。触发词：社会排斥、social exclusion、脑动力学、社会行为预测、心智化网络、mentalizing network、社会疼痛。
user-invocable: true
---

# Global Brain Dynamics During Social Exclusion

## 核心方法论

研究社会排斥期间的全局脑动力学，预测后续社会行为一致性（conformity）：

1. **Cyberball 范式** - 使用虚拟抛球任务操纵社会排斥体验
2. **网络连接差异** - 计算排斥与包容状态的功能连接差异
3. **关键脑网络** - 心智化网络（mPFC, TPJ, Precuneus, TP）和社会疼痛网络（ACC, AI）
4. **机器学习预测** - 使用全局网络连接预测个体行为一致性

### 核心发现

- 社会排斥期间的全局功能连接可预测后续从众行为
- 心智化网络和社会疼痛网络的连接模式是关键预测因子
- 个体差异在神经层面的体现

## Python 代码示例

### 1. Cyberball 任务设计

```python
import numpy as np

class CyberballTask:
    """
    Cyberball 社会排斥任务设计
    
    阶段设计:
    - Inclusion: 玩家参与抛球
    - Exclusion: 玩家被排斥，观察他人抛球
    """
    
    def __init__(self, n_players=3, n_throws_inclusion=30, n_throws_exclusion=30):
        self.n_players = n_players
        self.n_throws_inclusion = n_throws_inclusion
        self.n_throws_exclusion = n_throws_exclusion
        
        # 玩家角色: 0=被试, 1=虚拟玩家1, 2=虚拟玩家2
        self.player_roles = ['subject', 'virtual_1', 'virtual_2']
    
    def generate_inclusion_sequence(self):
        """生成包容阶段的抛球序列"""
        throws = []
        current_holder = np.random.randint(0, self.n_players)
        
        for _ in range(self.n_throws_inclusion):
            # 随机选择接收者（不能是当前持球者）
            possible_receivers = [i for i in range(self.n_players) if i != current_holder]
            receiver = np.random.choice(possible_receivers)
            throws.append({
                'thrower': current_holder,
                'receiver': receiver,
                'phase': 'inclusion'
            })
            current_holder = receiver
        
        return throws
    
    def generate_exclusion_sequence(self):
        """生成排斥阶段的抛球序列（玩家被排除）"""
        throws = []
        # 开始时给被试一次，然后不再传球给被试
        current_holder = 0  # 被试开始持球
        throws.append({
            'thrower': 0,
            'receiver': 1,
            'phase': 'exclusion'
        })
        
        for _ in range(self.n_throws_exclusion - 1):
            # 虚拟玩家之间互传
            current_holder = np.random.choice([1, 2])
            receiver = 1 if current_holder == 2 else 2
            throws.append({
                'thrower': current_holder,
                'receiver': receiver,
                'phase': 'exclusion'
            })
        
        return throws
    
    def get_task_timing(self, tr=2.0):
        """获取任务时间点（用于 fMRI 分析）"""
        inclusion = self.generate_inclusion_sequence()
        exclusion = self.generate_exclusion_sequence()
        
        timing = {
            'inclusion_onset': 0,
            'inclusion_duration': len(inclusion) * 2.0,  # 假设每次抛球 2 秒
            'exclusion_onset': len(inclusion) * 2.0 + 10,  # 10 秒休息
            'exclusion_duration': len(exclusion) * 2.0
        }
        
        return timing, inclusion, exclusion
```

### 2. 功能连接差异分析

```python
import numpy as np
from scipy import stats
from nilearn import connectome

def compute_exclusion_inclusion_diff(fc_exclusion, fc_inclusion, 
                                      mentalizing_rois, social_pain_rois):
    """
    计算社会排斥与包容期间的功能连接差异
    
    Args:
        fc_exclusion: 排斥期的功能连接矩阵
        fc_inclusion: 包容期的功能连接矩阵
        mentalizing_rois: 心智化网络 ROI 索引列表
        social_pain_rois: 社会疼痛网络 ROI 索引列表
    
    Returns:
        diff_matrix: 连接差异矩阵
        significant_connections: 显著差异的连接
    """
    # 连接差异
    diff_matrix = fc_exclusion - fc_inclusion
    
    # 统计检验（组水平）
    significant_connections = {}
    
    key_rois = mentalizing_rois + social_pain_rois
    
    for i in key_rois:
        for j in key_rois:
            if i < j:
                diff = diff_matrix[i, j]
                # 这里应该使用组水平的统计检验
                significant_connections[(i, j)] = diff
    
    return diff_matrix, significant_connections

def extract_global_connectivity(fmri_data, mentalizing_network, social_pain_network):
    """
    提取全局网络连接特征
    
    Args:
        fmri_data: (n_timepoints, n_voxels) fMRI 数据
        mentalizing_network: 心智化网络 ROI 掩码
        social_pain_network: 社会疼痛网络 ROI 掩码
    
    Returns:
        connectivity_features: 全局连接特征向量
    """
    # 提取 ROI 时间序列
    mentalizing_ts = fmri_data[:, mentalizing_network].mean(axis=1)
    social_pain_ts = fmri_data[:, social_pain_network].mean(axis=1)
    
    # 计算功能连接
    correlation = np.corrcoef(mentalizing_ts.T, social_pain_ts.T)
    
    # 提取网络间连接
    n_m = len(mentalizing_network)
    n_s = len(social_pain_network)
    
    # 心智化网络内部连接
    mentalizing_internal = correlation[:n_m, :n_m][np.triu_indices(n_m, k=1)]
    
    # 社会疼痛网络内部连接
    social_pain_internal = correlation[n_m:, n_m:][np.triu_indices(n_s, k=1)]
    
    # 网络间连接
    between_network = correlation[:n_m, n_m:].flatten()
    
    # 合并特征
    connectivity_features = np.concatenate([
        mentalizing_internal,
        social_pain_internal,
        between_network
    ])
    
    return connectivity_features
```

### 3. 行为预测模型

```python
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class SocialConformityPredictor:
    """
    预测社会行为一致性的机器学习模型
    """
    
    def __init__(self, n_folds=10):
        self.n_folds = n_folds
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
    
    def fit_predict(self, X, y):
        """
        使用交叉验证预测行为一致性
        
        Args:
            X: 全局功能连接特征 (n_subjects, n_features)
            y: 行为一致性得分
        
        Returns:
            predictions: 预测值
            correlation: 预测与实际的相关
        """
        cv = KFold(n_splits=self.n_folds, shuffle=True, random_state=42)
        predictions = cross_val_predict(self.model, X, y, cv=cv)
        
        # 计算预测相关性
        correlation = np.corrcoef(predictions, y)[0, 1]
        
        return predictions, correlation
    
    def get_feature_importance(self, X, y, feature_names=None):
        """获取特征重要性"""
        self.model.fit(X, y)
        coefficients = self.model.named_steps['ridge'].coef_
        
        if feature_names is None:
            feature_names = [f'feature_{i}' for i in range(len(coefficients))]
        
        importance = dict(zip(feature_names, np.abs(coefficients)))
        importance = dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))
        
        return importance

# 使用示例
def predict_conformity_from_exclusion(fmri_exclusion, fmri_inclusion, 
                                       conformity_scores,
                                       mentalizing_rois, social_pain_rois):
    """
    完整预测流程
    
    Args:
        fmri_exclusion: 排斥期 fMRI 数据列表 [(n_tp, n_voxels), ...]
        fmri_inclusion: 包容期 fMRI 数据列表
        conformity_scores: 行为一致性得分
        mentalizing_rois: 心智化网络 ROI
        social_pain_rois: 社会疼痛网络 ROI
    
    Returns:
        predictions: 预测的一致性得分
        r: 预测相关系数
    """
    n_subjects = len(fmri_exclusion)
    features = []
    
    for i in range(n_subjects):
        # 计算功能连接
        fc_exclusion = compute_connectivity(fmri_exclusion[i], 
                                            mentalizing_rois + social_pain_rois)
        fc_inclusion = compute_connectivity(fmri_inclusion[i],
                                            mentalizing_rois + social_pain_rois)
        
        # 连接差异
        fc_diff = fc_exclusion - fc_inclusion
        
        # 提取特征
        features.append(fc_diff[np.triu_indices_from(fc_diff, k=1)])
    
    X = np.array(features)
    y = np.array(conformity_scores)
    
    # 预测
    predictor = SocialConformityPredictor()
    predictions, r = predictor.fit_predict(X, y)
    
    return predictions, r
```

### 4. ROI 定义（基于论文）

```python
# 心智化网络 (Mentalizing Network)
MENTALIZING_ROIS = {
    'mPFC': {'name': 'medial prefrontal cortex', 'MNI': [0, 52, -6]},
    'TPJ_L': {'name': 'left temporoparietal junction', 'MNI': [-54, -54, 24]},
    'TPJ_R': {'name': 'right temporoparietal junction', 'MNI': [54, -54, 24]},
    'Precuneus': {'name': 'precuneus', 'MNI': [0, -56, 40]},
    'TP_L': {'name': 'left temporal pole', 'MNI': [-48, 12, -32]},
    'TP_R': {'name': 'right temporal pole', 'MNI': [48, 12, -32]}
}

# 社会疼痛网络 (Social Pain Network)
SOCIAL_PAIN_ROIS = {
    'ACC': {'name': 'anterior cingulate cortex', 'MNI': [0, 20, 28]},
    'AI_L': {'name': 'left anterior insula', 'MNI': [-34, 20, -4]},
    'AI_R': {'name': 'right anterior insula', 'MNI': [34, 20, -4]}
}

def create_roi_masks(fmri_img, roi_definitions, radius=8):
    """
    创建球形 ROI 掩码
    
    Args:
        fmri_img: fMRI 图像
        roi_definitions: ROI 定义字典
        radius: 球形半径 (mm)
    
    Returns:
        masks: ROI 掩码字典
    """
    from nilearn import masking
    
    masks = {}
    for roi_name, roi_info in roi_definitions.items():
        mask = masking.create_sphere(
            roi_info['MNI'],
            radius=radius,
            img=fmri_img
        )
        masks[roi_name] = mask
    
    return masks
```

## 应用场景

1. **社会神经科学研究** - 研究社会排斥的神经机制
2. **个体差异预测** - 预测个体对社会影响的敏感性
3. **青少年行为研究** - 理解青少年从众行为的神经基础
4. **临床应用** - 社交焦虑、孤独感相关研究
5. **社会心理学实验设计** - fMRI 社会认知实验范式

## 方法要点

1. **全脑连接分析** - 不仅关注局部激活，更关注网络连接
2. **状态差异** - 关键在于排斥与包容的差异，而非单一状态
3. **交叉验证** - 预测模型需要严格的交叉验证
4. **行为关联** - 神经测量必须与实际行为相关联

## 参考文献

- Paper: arXiv:1710.00869
- Wasylyshyn et al., "Global Brain Dynamics During Social Exclusion Predict Subsequent Behavioral Conformity"