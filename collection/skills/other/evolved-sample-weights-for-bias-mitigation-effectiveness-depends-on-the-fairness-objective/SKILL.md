# Evolved Sample Weights for Bias Mitigation: Effectiveness Depends on the Fairness Objective

**arXiv ID:** 2511.20909
**Authors:** Anil K. Saini, Jose Guadalupe Hernandez, Emily F. Wong, Debanshi Misra, Tiffani J. Bright, Jason H. Moore
**Published:** 2025-11-25T22:50:59Z
**Abstract:**
Machine learning models trained on real-world data may inadvertently make biased predictions that negatively impact marginalized communities. Reweighting, which assigns a weight to each data point used during model training, can mitigate such bias, though sometimes at the cost of predictive accuracy. In this paper, we investigated this trade-off by comparing three methods for generating these weights: (1) evolving them using a Genetic Algorithm (GA), (2) computing them using only dataset characteristics, and (3) assigning equal weights to all data points. Model performance under each strategy was evaluated using paired predictive and fairness metrics. We used two predictive metrics (accuracy and area under the Receiver Operating Characteristic curve) and two fairness metrics (demographic parity and subgroup false negative fairness). By conducting experiments on eleven publicly available datasets (including two medical datasets), we show that evolved sample weights can produce models that achieve better trade-offs between fairness and predictive performance than alternative weighting methods. However, the magnitude of these benefits depends strongly on the choice of fairness objective. Our experiments reveal that the evolved weights were most effective when optimizing for demographic parity-independent of choice of the performance objective-yielding better performance than other weighting strategies on the largest number of datasets.

## Skill Description

This skill is generated from the arXiv paper: Evolved Sample Weights for Bias Mitigation: Effectiveness Depends on the Fairness Objective (2511.20909).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2511.20909](http://arxiv.org/abs/2511.20909v2)
