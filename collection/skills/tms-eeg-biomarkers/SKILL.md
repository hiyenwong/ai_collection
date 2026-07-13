---
name: tms-eeg-biomarkers
description: TMS-EEG生物标志物信效度评估方法论。系统评估TMS-EEG标志物的内部可靠性、外部可靠性和有效性，提供评估框架和最佳实践。触发词：TMS-EEG、生物标志物、可靠性、有效性、信效度、TMS biomarkers、reliability、validity、TMS-EEG analysis。
user-invocable: true
---

# TMS-EEG生物标志物信效度评估

基于 arXiv:2207.08456 - "Reliability and validity of TMS-EEG biomarkers"

## 核心方法论

### 1. 可靠性评估框架

```python
import numpy as np
from scipy import stats
from scipy.signal import welch, coherence
import warnings

class TMSEEGReliability:
    """
    TMS-EEG生物标志物可靠性评估
    
    包括内部可靠性（重复测量一致性）和外部可靠性（跨实验室/设备一致性）
    """
    
    def __init__(self):
        self.metrics = {}
    
    # ==================== 内部可靠性 ====================
    
    def intraclass_correlation(self, data, sessions=None):
        """
        计算组内相关系数(ICC)
        
        评估同一被试在不同测量间的一致性
        
        参数:
            data: (n_subjects, n_sessions, n_features) 或 (n_subjects, n_features)
            sessions: 会话标签（如果data是展平的）
        
        返回:
            ICC(2,1): 单一测量ICC
            ICC(2,k): 多测量平均ICC
        """
        if len(data.shape) == 2:
            # 假设每个被试有多个测量
            n_subjects = data.shape[0]
            n_measures = data.shape[1]
            
            # 单因素方差分析
            subject_means = np.mean(data, axis=1)
            grand_mean = np.mean(data)
            
            # 平方和
            SS_total = np.sum((data - grand_mean) ** 2)
            SS_between = np.sum((subject_means - grand_mean) ** 2) * n_measures
            SS_within = SS_total - SS_between
            
            # 均方
            MS_between = SS_between / (n_subjects - 1)
            MS_within = SS_within / (n_subjects * (n_measures - 1))
            
            # ICC
            ICC_single = (MS_between - MS_within) / (MS_between + (n_measures - 1) * MS_within)
            ICC_average = (MS_between - MS_within) / MS_between
            
            return {
                'ICC(2,1)': ICC_single,  # 单次测量
                'ICC(2,k)': ICC_average,  # 多次测量平均
                'interpretation': self._interpret_icc(ICC_single)
            }
        
        elif len(data.shape) == 3:
            # 多特征情况
            n_subjects, n_sessions, n_features = data.shape
            results = []
            
            for f in range(n_features):
                icc = self.intraclass_correlation(data[:, :, f])
                results.append(icc)
            
            return results
    
    def _interpret_icc(self, icc):
        """解释ICC值"""
        if icc < 0.5:
            return "poor reliability (ICC < 0.5)"
        elif icc < 0.75:
            return "moderate reliability (0.5 ≤ ICC < 0.75)"
        elif icc < 0.9:
            return "good reliability (0.75 ≤ ICC < 0.9)"
        else:
            return "excellent reliability (ICC ≥ 0.9)"
    
    def test_retest_reliability(self, session1, session2, method='pearson'):
        """
        测试-重测可靠性
        
        评估同一测量在不同时间点的一致性
        
        参数:
            session1, session2: 两次测量的数据 (n_subjects, n_features)
            method: 相关方法 ('pearson', 'spearman', 'concordance')
        """
        if method == 'pearson':
            r, p = stats.pearsonr(session1.flatten(), session2.flatten())
        elif method == 'spearman':
            r, p = stats.spearmanr(session1.flatten(), session2.flatten())
        elif method == 'concordance':
            r = self._concordance_correlation(session1.flatten(), session2.flatten())
            p = None
        
        return {
            'correlation': r,
            'p_value': p,
            'method': method
        }
    
    def _concordance_correlation(self, x, y):
        """计算一致性相关系数"""
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        var_x = np.var(x)
        var_y = np.var(y)
        cov = np.mean((x - mean_x) * (y - mean_y))
        
        r = 2 * cov / (var_x + var_y + (mean_x - mean_y)**2)
        return r
    
    def coefficient_of_variation(self, data):
        """
        变异系数
        
        衡量测量稳定性
        """
        cv = np.std(data) / np.mean(np.abs(data)) * 100
        return cv
    
    # ==================== 外部可靠性 ====================
    
    def cross_site_reliability(self, data_sites, site_labels):
        """
        跨站点可靠性
        
        评估不同实验室/设备间的一致性
        """
        n_sites = len(data_sites)
        n_subjects = data_sites[0].shape[0]
        
        # 计算所有站点对之间的相关性
        correlations = []
        for i in range(n_sites):
            for j in range(i+1, n_sites):
                r, _ = stats.pearsonr(data_sites[i].flatten(), data_sites[j].flatten())
                correlations.append(r)
        
        # 计算总体一致性
        mean_r = np.mean(correlations)
        
        return {
            'pairwise_correlations': correlations,
            'mean_cross_site_correlation': mean_r,
            'interpretation': 'good' if mean_r > 0.7 else 'moderate' if mean_r > 0.5 else 'poor'
        }
    
    def equipment_variance(self, data, equipment_types):
        """
        设备方差分析
        
        分解变异来源：被试、设备、交互
        """
        import pandas as pd
        from scipy.stats import f_oneway
        
        # 按设备类型分组
        groups = [data[np.array(equipment_types) == et] for et in set(equipment_types)]
        
        # 单因素方差分析
        F, p = f_oneway(*groups)
        
        # 计算效应量
        overall_mean = np.mean(data)
        SS_between = sum(len(g) * (np.mean(g) - overall_mean)**2 for g in groups)
        SS_within = sum(np.sum((g - np.mean(g))**2) for g in groups)
        SS_total = SS_between + SS_within
        
        eta_squared = SS_between / SS_total
        
        return {
            'F': F,
            'p_value': p,
            'eta_squared': eta_squared,
            'interpretation': f"{'significant' if p < 0.05 else 'non-significant'} equipment effect"
        }
```

### 2. 有效性评估

```python
class TMSEEGValidity:
    """
    TMS-EEG生物标志物有效性评估
    
    评估标志物是否真正测量了预期的神经信号
    """
    
    def __init__(self):
        self.validation_results = {}
    
    # ==================== 内容有效性 ====================
    
    def content_validity(self, biomarker_definition, expert_ratings):
        """
        内容有效性
        
        评估标志物是否涵盖了预期测量的所有方面
        """
        # 专家评分：每个专家对标志物相关性的评分
        # scale: 1-4 (1=不相关, 2=弱相关, 3=相关, 4=非常相关)
        
        CVR = (n_e - n/2) / (n/2)  # 内容效度比
        # 其中n_e是评为3或4的专家数，n是总专家数
        
        n_e = sum(1 for r in expert_ratings if r >= 3)
        n = len(expert_ratings)
        
        CVR = (n_e - n/2) / (n/2)
        CVI = np.mean([r >= 3 for r in expert_ratings])  # 内容效度指数
        
        return {
            'CVR': CVR,
            'CVI': CVI,
            'expert_agreement': n_e / n,
            'interpretation': 'adequate content validity' if CVI > 0.8 else 'insufficient'
        }
    
    # ==================== 标准有效性 ====================
    
    def criterion_validity_concurrent(self, tms_eeg_data, gold_standard):
        """
        同时标准有效性
        
        评估TMS-EEG标志物与已知金标准的相关性
        """
        # 皮尔逊相关
        r, p = stats.pearsonr(tms_eeg_data, gold_standard)
        
        # 决定系数
        r_squared = r ** 2
        
        # Bland-Altman分析
        mean_diff = np.mean(tms_eeg_data - gold_standard)
        std_diff = np.std(tms_eeg_data - gold_standard)
        limits_of_agreement = (mean_diff - 1.96*std_diff, mean_diff + 1.96*std_diff)
        
        return {
            'correlation': r,
            'p_value': p,
            'r_squared': r_squared,
            'bland_altman': {
                'mean_difference': mean_diff,
                'limits_of_agreement': limits_of_agreement
            },
            'interpretation': 'strong criterion validity' if abs(r) > 0.7 else 'moderate' if abs(r) > 0.4 else 'weak'
        }
    
    def criterion_validity_predictive(self, baseline_data, outcome_data, outcome_time):
        """
        预测标准有效性
        
        评估TMS-EEG标志物预测未来结果的能力
        """
        # 简单回归
        slope, intercept, r, p, se = stats.linregress(baseline_data, outcome_data)
        
        # ROC分析（如果是二分类结果）
        if len(np.unique(outcome_data)) == 2:
            from sklearn.metrics import roc_auc_score, roc_curve
            auc = roc_auc_score(outcome_data, baseline_data)
            fpr, tpr, thresholds = roc_curve(outcome_data, baseline_data)
            
            # 最佳阈值
            youden_index = tpr - fpr
            best_threshold = thresholds[np.argmax(youden_index)]
            
            return {
                'AUC': auc,
                'best_threshold': best_threshold,
                'sensitivity': tpr[np.argmax(youden_index)],
                'specificity': 1 - fpr[np.argmax(youden_index)],
                'interpretation': 'good predictive validity' if auc > 0.8 else 'moderate' if auc > 0.7 else 'poor'
            }
        
        return {
            'slope': slope,
            'intercept': intercept,
            'r': r,
            'p_value': p,
            'r_squared': r ** 2,
            'interpretation': 'significant predictor' if p < 0.05 else 'non-significant'
        }
    
    # ==================== 结构有效性 ====================
    
    def construct_validity_convergent(self, biomarker_data, related_measures):
        """
        收敛有效性
        
        评估与理论上相关的其他测量的一致性
        """
        correlations = {}
        for name, measure in related_measures.items():
            r, p = stats.pearsonr(biomarker_data, measure)
            correlations[name] = {'r': r, 'p': p}
        
        # 平均收敛相关性
        avg_r = np.mean([c['r'] for c in correlations.values()])
        
        return {
            'correlations': correlations,
            'average_convergence': avg_r,
            'interpretation': 'adequate convergence' if avg_r > 0.5 else 'poor convergence'
        }
    
    def construct_validity_discriminant(self, biomarker_data, unrelated_measures):
        """
        区分有效性
        
        评估与理论上不相关的测量的区分程度
        """
        correlations = {}
        for name, measure in unrelated_measures.items():
            r, p = stats.pearsonr(biomarker_data, measure)
            correlations[name] = {'r': r, 'p': p}
        
        # 区分相关性的平方根应大于收敛相关性
        avg_r = np.mean([abs(c['r']) for c in correlations.values()])
        
        return {
            'correlations': correlations,
            'average_discrimination': avg_r,
            'interpretation': 'good discriminant validity' if avg_r < 0.3 else 'concerning discrimination'
        }
    
    # ==================== 外部验证 ====================
    
    def invasive_validation(self, tms_eeg_response, invasive_recording):
        """
        使用侵入性记录验证TMS-EEG响应
        """
        # 时间对齐
        # 比较TMS-EEG响应与直接皮层记录
        
        correlation = np.corrcoef(tms_eeg_response, invasive_recording)[0, 1]
        
        # 计算延迟差异
        tms_peak = np.argmax(np.abs(tms_eeg_response))
        invasive_peak = np.argmax(np.abs(invasive_recording))
        delay_diff = tms_peak - invasive_peak
        
        return {
            'correlation_with_invasive': correlation,
            'peak_delay_difference_samples': delay_diff,
            'validation_strength': 'strong' if correlation > 0.8 else 'moderate' if correlation > 0.6 else 'weak'
        }
    
    def treatment_response_validation(self, baseline_biomarker, treatment_response):
        """
        使用治疗反应验证生物标志物
        """
        # 相关性分析
        r, p = stats.pearsonr(baseline_biomarker, treatment_response)
        
        # 分组分析（响应者 vs 非响应者）
        responders = treatment_response > np.median(treatment_response)
        biomarker_responders = baseline_biomarker[responders]
        biomarker_non_responders = baseline_biomarker[~responders]
        
        # t检验
        t, p_group = stats.ttest_ind(biomarker_responders, biomarker_non_responders)
        
        # 效应量
        cohens_d = (np.mean(biomarker_responders) - np.mean(biomarker_non_responders)) / \
                   np.sqrt((np.var(biomarker_responders) + np.var(biomarker_non_responders)) / 2)
        
        return {
            'correlation_with_response': r,
            'p_value': p,
            'group_difference_p': p_group,
            'cohens_d': cohens_d,
            'interpretation': 'validated by treatment response' if p_group < 0.05 else 'not validated'
        }
```

### 3. TMS-EEG特定标志物分析

```python
class TMSEEGBiomarkers:
    """
    TMS-EEG特定生物标志物提取和分析
    """
    
    def __init__(self, fs=1000):
        """
        参数:
            fs: 采样率 (Hz)
        """
        self.fs = fs
    
    def extract_tms_evoked_potential(self, eeg_data, tms_onset, window=(-10, 300)):
        """
        提取TMS诱发电位(TEP)
        
        参数:
            eeg_data: EEG数据 (n_channels, n_samples)
            tms_onset: TMS脉冲时间点索引
            window: 分析窗口 (ms)
        """
        window_samples = (int(window[0] * self.fs / 1000), 
                         int(window[1] * self.fs / 1000))
        
        n_channels = eeg_data.shape[0]
        n_tms = len(tms_onset)
        
        # 提取每个TMS脉冲周围的信号
        teps = np.zeros((n_channels, window_samples[1] - window_samples[0], n_tms))
        
        for i, onset in enumerate(tms_onset):
            start = onset + window_samples[0]
            end = onset + window_samples[1]
            teps[:, :, i] = eeg_data[:, start:end]
        
        # 平均TEP
        avg_tep = np.mean(teps, axis=2)
        
        return {
            'average_tep': avg_tep,
            'single_trials': teps,
            'time_axis': np.linspace(window[0], window[1], window_samples[1] - window_samples[0])
        }
    
    def compute_tep_amplitude(self, tep_data, component='P30', time_range=None):
        """
        计算TEP成分振幅
        
        常见成分: N15, P30, N45, P60, N100, P180
        """
        if time_range is None:
            component_times = {
                'N15': (10, 20),
                'P30': (25, 35),
                'N45': (40, 55),
                'P60': (55, 70),
                'N100': (90, 130),
                'P180': (150, 200)
            }
            time_range = component_times.get(component, (0, 300))
        
        # 找到时间范围内的峰值
        time_axis = tep_data['time_axis']
        mask = (time_axis >= time_range[0]) & (time_axis <= time_range[1])
        
        tep = tep_data['average_tep']
        
        if component.startswith('N'):
            # 负成分：找最小值
            amplitude = np.min(tep[:, mask], axis=1)
            latency = time_axis[mask][np.argmin(tep[:, mask], axis=1)]
        else:
            # 正成分：找最大值
            amplitude = np.max(tep[:, mask], axis=1)
            latency = time_axis[mask][np.argmax(tep[:, mask], axis=1)]
        
        return {
            'amplitude': amplitude,
            'latency': latency,
            'component': component
        }
    
    def compute_gamma_power(self, tep_data, freq_range=(30, 80)):
        """
        计算Gamma频段功率
        
        TMS后的Gamma振荡是重要的生物标志物
        """
        tep = tep_data['average_tep']
        time_axis = tep_data['time_axis']
        
        # 使用Welch方法计算功率谱
        freqs, psd = welch(tep, fs=self.fs, nperseg=min(256, tep.shape[1]))
        
        # Gamma频段
        gamma_mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
        gamma_power = np.mean(psd[:, gamma_mask], axis=1)
        
        return gamma_power
    
    def compute_connectivity(self, tep_data, method='coherence'):
        """
        计算TMS诱发的功能连接
        """
        tep = tep_data['average_tep']
        n_channels = tep.shape[0]
        
        connectivity_matrix = np.zeros((n_channels, n_channels))
        
        for i in range(n_channels):
            for j in range(i+1, n_channels):
                if method == 'coherence':
                    f, Cxy = coherence(tep[i], tep[j], fs=self.fs)
                    connectivity_matrix[i, j] = np.mean(Cxy)
                elif method == 'correlation':
                    connectivity_matrix[i, j] = np.corrcoef(tep[i], tep[j])[0, 1]
                
                connectivity_matrix[j, i] = connectivity_matrix[i, j]
        
        return connectivity_matrix
    
    def global_mean_field_power(self, tep_data):
        """
        计算全局平均场功率(GMFP)
        
        反映大脑整体激活水平
        """
        tep = tep_data['average_tep']
        gmfp = np.std(tep, axis=0)
        return gmfp
    
    def tms_intensity_response_curve(self, eeg_data_list, intensities, tms_onset_list):
        """
        计算TMS强度-响应曲线
        
        评估不同TMS强度下的响应
        """
        responses = []
        
        for eeg_data, intensity, tms_onset in zip(eeg_data_list, intensities, tms_onset_list):
            tep = self.extract_tms_evoked_potential(eeg_data, tms_onset)
            gmfp = self.global_mean_field_power(tep)
            peak_gmfp = np.max(gmfp)
            responses.append(peak_gmfp)
        
        # 拟合sigmoid函数
        from scipy.optimize import curve_fit
        
        def sigmoid(x, L, x0, k, b):
            return L / (1 + np.exp(-k * (x - x0))) + b
        
        try:
            popt, _ = curve_fit(sigmoid, intensities, responses, 
                               p0=[max(responses), np.median(intensities), 0.1, 0])
            fitted_curve = sigmoid(intensities, *popt)
            threshold = popt[1]  # 半最大响应的强度
        except:
            fitted_curve = None
            threshold = None
        
        return {
            'intensities': intensities,
            'responses': responses,
            'fitted_curve': fitted_curve,
            'estimated_threshold': threshold
        }
```

### 4. 质量控制与最佳实践

```python
class TMSEEGQualityControl:
    """
    TMS-EEG数据质量控制
    """
    
    def __init__(self):
        self.quality_metrics = {}
    
    def detect_artifacts(self, eeg_data, tms_onset, window=(-5, 50)):
        """
        检测TMS伪迹
        """
        # TMS脉冲伪迹检测
        pulse_window = (int(window[0] * self.fs / 1000), int(window[1] * self.fs / 1000))
        
        artifacts = []
        for onset in tms_onset:
            segment = eeg_data[:, onset + pulse_window[0]:onset + pulse_window[1]]
            # 高幅度瞬态检测
            if np.max(np.abs(segment)) > 100e-6:  # 100 µV阈值
                artifacts.append(onset)
        
        return artifacts
    
    def signal_to_noise_ratio(self, tep_data, baseline_window=(-10, 0)):
        """
        计算信噪比
        """
        tep = tep_data['average_tep']
        time_axis = tep_data['time_axis']
        
        baseline_mask = (time_axis >= baseline_window[0]) & (time_axis <= baseline_window[1])
        response_mask = ~baseline_mask
        
        noise = np.std(tep[:, baseline_mask])
        signal = np.std(tep[:, response_mask])
        
        snr = signal / noise if noise > 0 else np.inf
        
        return snr
    
    def recommend_quality_thresholds(self):
        """
        推荐质量阈值
        """
        return {
            'ICC_threshold': 0.75,  # 可靠性
            'SNR_threshold': 3.0,   # 信噪比
            'artifact_rejection': 'auto or manual',
            'min_trials': 50,        # 最小试次数
            'recommended_reporting': [
                'ICC with 95% CI',
                'CV for each biomarker',
                'Bland-Altman plots',
                'test-retest interval'
            ]
        }
```

## 应用场景

### 1. 临床研究
- TMS治疗反应预测
- 神经精神疾病诊断标志物

### 2. 方法学研究
- 评估新TMS-EEG标志物的可靠性
- 跨实验室数据整合

### 3. 设备验证
- 新TMS设备验证
- EEG系统比较

## Activation Keywords
- TMS-EEG
- 生物标志物
- 可靠性
- 有效性
- 信效度
- TMS biomarkers
- reliability
- validity
- TMS-EEG analysis
- ICC
- TEP
- 临床研究

## Tools Used
- numpy
- scipy
- sklearn

## Instructions for Agents
1. 理解三类可靠性：内部（重复测量）、外部（跨实验室）、测试-重测
2. 计算ICC（组内相关系数）：评估测量一致性
3. 提取TEP成分：N15、P30、N45、P60、N100、P180
4. 计算Gamma功率：TMS后的Gamma振荡是重要标志物
5. 注意质量阈值：ICC > 0.75、SNR > 3.0、最小50试次

## Examples
```python
# 使用示例
from tms_eeg_biomarkers import TMSEEGReliability, TMSEEGBiomarkers

# 1. 可靠性评估
reliability = TMSEEGReliability()
icc = reliability.intraclass_correlation(data)  # data: (n_subjects, n_sessions)
print(f"ICC(2,1): {icc['ICC(2,1)']:.4f}")
print(f"解释: {icc['interpretation']}")

# 2. 提取TEP
biomarkers = TMSEEGBiomarkers(fs=1000)
tep = biomarkers.extract_tms_evoked_potential(eeg_data, tms_onset)
amplitude = biomarkers.compute_tep_amplitude(tep, component='N100')

# 3. 计算Gamma功率
gamma_power = biomarkers.compute_gamma_power(tep)
```

## 参考文献

- Parmigiani, S. et al. (2022). "Reliability and validity of TMS-EEG biomarkers" arXiv:2207.08456