# Anomaly Localization in Model Gradients Under Backdoor Attacks Against Federated Learning

**arXiv ID:** 2111.14683
**Authors:** Zeki Bilgin
**Published:** 2021-11-29T16:46:01Z
**Abstract:**
Inserting a backdoor into the joint model in federated learning (FL) is a recent threat raising concerns. Existing studies mostly focus on developing effective countermeasures against this threat, assuming that backdoored local models, if any, somehow reveal themselves by anomalies in their gradients. However, this assumption needs to be elaborated by identifying specifically which gradients are more likely to indicate an anomaly to what extent under which conditions. This is an important issue given that neural network models usually have huge parametric space and consist of a large number of weights. In this study, we make a deep gradient-level analysis on the expected variations in model gradients under several backdoor attack scenarios against FL. Our main novel finding is that backdoor-induced anomalies in local model updates (weights or gradients) appear in the final layer bias weights of the malicious local models. We support and validate our findings by both theoretical and experimental analysis in various FL settings. We also investigate the impact of the number of malicious clients, learning rate, and malicious data rate on the observed anomaly. Our implementation is publicly available\footnote{\url{ https://github.com/ArcelikAcikKaynak/Federated_Learning.git}}.

## Skill Description

This skill is generated from the arXiv paper: Anomaly Localization in Model Gradients Under Backdoor Attacks Against Federated Learning (2111.14683).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2111.14683](http://arxiv.org/abs/2111.14683v1)
