---
name: dementia-neurodynamics-eeg
description: 痴呆症脑网络神经动力学EEG分析方法论。通过频谱功率、Lyapunov指数、相位同步区分阿尔茨海默病（AD）和额颞叶痴呆（FTD）。适用于痴呆症诊断、脑网络分析。触发词：痴呆症、阿尔茨海默、FTD、EEG、脑网络、neurodynamics。
user-invocable: true
---

# Dementia Neurodynamics EEG - 痴呆症脑网络神经动力学EEG分析

## 核心思想

通过多维度 EEG 指标表征 AD 和 FTD 的差异化神经动力学。

**来源：** arXiv:2507.08728
**效用：** 1.0

---

## 疾病对比

| 特征 | AD | FTD |
|------|----|----|
| 协调性 | 低 | 较高 |
| 连接性 | 低 | 保留 |
| 随机性 | 高 | 低 |

---

## 分析指标

1. **频谱功率：** Delta-Theta-Alpha-Beta-Gamma
2. **Lyapunov 指数：** 混沌性量化
3. **相位同步：** PLV 相位锁定值
4. **功能网络：** 连接组织

---

## 实现

```python
import numpy as np
from scipy import signal

def compute_lyapunov(eeg, m=10, tau=10):
    """计算Lyapunov指数"""
    n = len(eeg)
    embedded = np.array([eeg[i:i+m] for i in range(0, n-m, tau)])
    lyap_sum, count = 0, 0
    for i in range(len(embedded)-1):
        d = np.linalg.norm(embedded - embedded[i], axis=1)
        d[i] = np.inf
        nearest = np.argmin(d)
        if i+1 < len(embedded) and nearest+1 < len(embedded):
            lyap_sum += np.log(d[nearest+1]/d[nearest]+1e-10)
            count += 1
    return lyap_sum/count if count > 0 else 0

def compute_plv(eeg1, eeg2):
    """相位锁定值"""
    p1 = np.angle(signal.hilbert(eeg1))
    p2 = np.angle(signal.hilbert(eeg2))
    return np.abs(np.mean(np.exp(1j*(p1-p2))))
```

---

## 关键发现

- AD：协调性低、连接性低、随机性高
- FTD：协调性保留、额叶慢活动异常
- 两者代表从正常相反方向的偏离

---

## 参考文献

- arXiv:2507.08728