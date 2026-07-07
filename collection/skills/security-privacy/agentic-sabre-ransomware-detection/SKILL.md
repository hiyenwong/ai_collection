---
name: agentic-sabre-ransomware-detection
description: "Uncertainty-aware neuro-symbolic multi-agent framework for adaptive ransomware detection. Fuses semantic representation evidence with behavioural forensic telemetry, using Monte Carlo Dropout for epistemic uncertainty quantification. A risk-uncertainty orchestrator triages cases: auto-contain high-confidence threats, escalate uncertain cases to humans. Includes post-hoc explainability (gradient saliency, permutation importance, counterfactual analysis). Activation: agentic SABRE, ransomware detection, neuro-symbolic, uncertainty quantification, Monte Carlo Dropout, multi-agent security, adaptive threat detection, concept drift, behavioural polymorphism."
version: 1.0.0
metadata:
  hermes:
    tags: [security-privacy, multi-agent, neuro-symbolic, ransomware, uncertainty-quantification, threat-detection]
    source_paper: "Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection (arXiv:2607.04292)"
    published: "2026-07-05"
    authors: "Henry Kabuye, Biju Issac, Jeyamohan Neera"
    arxiv_id: "2607.04292"
    utility: 0.90
---

# Agentic SABRE: Uncertainty-Aware Neuro-Symbolic Multi-Agent Ransomware Detection

## Overview

Agentic SABRE (Semantic-Behavioural Arbitration for Ransomware Evaluation) is an uncertainty-aware, neuro-symbolic, multi-agent framework for adaptive ransomware detection. It addresses the failure of static signatures and monolithic classifiers under concept drift, evasion, and behavioural polymorphism by fusing two complementary evidence streams and quantifying epistemic uncertainty per agent.

## Core Architecture

### Dual-Agent Evidence Fusion

1. **Semantic Agent**: Representation-based evidence from static/dynamic analysis features
2. **Behavioural Agent**: Time-window forensic telemetry (file system activity, process trees, network I/O patterns)

Each agent independently produces risk scores and uncertainty estimates. The orchestrator combines these into a triage decision.

### Monte Carlo Dropout Uncertainty Quantification

```python
import torch
import torch.nn as nn

class UncertaintyAwareAgent(nn.Module):
    """Agent with epistemic uncertainty via MC Dropout"""
    def __init__(self, input_dim, hidden_dim=256, n_dropout=5):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),  # Active at inference for MC sampling
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()
        )
        self.n_samples = n_dropout

    def predict_with_uncertainty(self, x):
        self.train()  # Keep dropout active
        samples = torch.stack([self.fc(x) for _ in range(self.n_samples)])
        mean = samples.mean(dim=0)
        variance = samples.var(dim=0)
        self.eval()
        return mean, variance
```

### Risk-Uncertainty Orchestrator

The decision-layer orchestrator uses two interpretable thresholds:

| Condition | Action |
|-----------|--------|
| High risk, low uncertainty | Auto-contain (quarantine) |
| High risk, high uncertainty | Escalate to human analyst |
| Low risk, low uncertainty | Pass (benign) |
| Low risk, high uncertainty | Monitor / log for review |

```python
def triage_decision(risk_score, uncertainty, risk_threshold=0.8, uncertainty_budget=0.15):
    """Risk- and uncertainty-aware triage."""
    if risk_score >= risk_threshold and uncertainty <= uncertainty_budget:
        return "auto_contain"
    elif risk_score >= risk_threshold and uncertainty > uncertainty_budget:
        return "escalate_human"
    elif risk_score < risk_threshold and uncertainty <= uncertainty_budget:
        return "pass"
    else:
        return "monitor"
```

## Post-Hoc Explainability

### Three-Pronged Explanation Suite

1. **Gradient Saliency**: Highlight which input features most influenced the agent's risk score
2. **Permutation Importance**: Global feature importance by measuring AUC degradation when each feature is shuffled
3. **Counterfactual Analysis**: Determine minimum perturbation cost to reverse the decision boundary

```python
def counterfactual_analysis(model, x, target_class, epsilon=0.01, max_iter=100):
    """Find minimum perturbation to flip decision."""
    x_cf = x.clone().requires_grad_(True)
    for _ in range(max_iter):
        output = model(x_cf)
        loss = -output[target_class]
        grad = torch.autograd.grad(loss, x_cf)[0]
        x_cf = x_cf - epsilon * grad.sign()
        if model(x_cf).argmax() == target_class:
            break
    perturbation_cost = torch.norm(x_cf - x).item()
    return x_cf, perturbation_cost
```

## Key Results

- **AUC = 1.0** on saturated semantic datasets (RDset, RanSMAP)
- **4.9% relative reduction** in false escalations at equal recall
- Calibrated predictive uncertainty (reliable uncertainty estimates)
- Counterfactual analysis confirms stable, interpretable decision boundaries (bounded perturbation cost for decision reversal)
- Robust under weak behavioural signals (concept drift scenarios)

## Use Cases

- **Ransomware detection pipelines** requiring adaptive, concept-drift-resistant classification
- **Security operations centers (SOC)** needing human-in-the-loop escalation for uncertain cases
- **Audit/compliance scenarios** requiring explainable threat detection decisions
- **Multi-agent security architectures** as a reference pattern for uncertainty-aware orchestration

## Activation Keywords

agentic SABRE, ransomware detection, neuro-symbolic security, Monte Carlo Dropout uncertainty, multi-agent threat detection, adaptive malware classification, concept drift, behavioural polymorphism, risk-uncertainty triage, post-hoc explainability, counterfactual security, gradient saliency, permutation importance
