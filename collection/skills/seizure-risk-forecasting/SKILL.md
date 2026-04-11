---
name: seizure-risk-forecasting
description: '癫痫发作风险预测方法论。将iEEG功能脑网络嵌入低维欧氏空间，定义无量纲生物标志物区分发作间期和发作前期。适用于癫痫发作预测、iEEG分析。触发词：癫痫预测、seizure forecasting、preictal。'
user-invocable: true
---

# Seizure Risk Forecasting - 癫痫发作风险预测

## 核心思想

将 iEEG 功能连接网络嵌入低维欧氏空间，预测发作前状态（24小时内发作风险）。

**来源：** arXiv:2505.00856
**效用：** 1.0

---

## 实现

```python
import numpy as np
from sklearn.manifold import MDS

class SeizureRiskForecaster:
    def __init__(self, n_components=3):
        self.embedder = MDS(n_components=n_components)
    
    def compute_fc(self, iEEG):
        fc = np.corrcoef(iEEG)
        return 1 - np.abs(fc)
    
    def embed(self, dist):
        return self.embedder.fit_transform(dist)
    
    def compute_biomarker(self, curr, ref):
        c = np.mean(curr, axis=0)
        r = np.mean(ref, axis=0)
        return np.linalg.norm(c-r) / (np.std(ref)+1e-10)
    
    def predict(self, iEEG, ref, thresh=2.0):
        B = self.compute_biomarker(self.embed(self.compute_fc(iEEG)),
                                    self.embed(self.compute_fc(ref)))
        return 1/(1+np.exp(-(B-thresh))), B>thresh
```

---

## 参考文献

- arXiv:2505.00856
## Activation Keywords

- seizure-risk-forecasting
- seizure-risk-forecasting 技能
- seizure-risk-forecasting skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply Seizure Risk Forecasting - 癫痫发作风险预测 to my analysis.

**Agent:** I'll help you apply seizure-risk-forecasting. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for seizure-risk-forecasting?

**Agent:** Let me search for the latest research and best practices...
