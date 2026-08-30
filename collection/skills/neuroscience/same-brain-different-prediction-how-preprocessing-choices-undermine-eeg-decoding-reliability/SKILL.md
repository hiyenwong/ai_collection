# Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability

**arXiv ID:** 2605.07212
**Authors:** Dengzhe Hou, Zihao Wu, Lingyu Jiang, Zirui Li, Fangzhou Lin, Kazunori D. Yamada
**Published:** 2026-05-08T03:58:58Z
**Abstract:**
Electroencephalography (EEG) is a cornerstone of brain-computer interfaces and clinical neuroscience, yet deep learning models are typically trained and evaluated under a single, unreported preprocessing pipeline. We formalize preprocessing choices as a counterfactual intervention space and show that EEG predictions are surprisingly unstable under this space: across six datasets spanning four paradigms, up to 42% of trial-level predictions flip when only the preprocessing changes, a variability that standard uncertainty methods do not explicitly quantify because they condition on a fixed preprocessing pipeline. We provide three tools to make this instability measurable, decomposable, and reducible. First, a Walsh-Hadamard decomposition of the 2^7 pipeline space reveals that sensitivity is near-additive in practice under the binary intervention design, enabling efficient step-by-step optimization. Second, we introduce Preprocessing Uncertainty (PU), a per-trial diagnostic that captures a dimension of instability complementary to model-based confidence. Third, we study Normalized Adaptive PGI (NA-PGI), a graph-structured regularizer that exploits the compositional structure of preprocessing interventions as one mitigation strategy with clear scope conditions.

## Skill Description

This skill is generated from the arXiv paper: Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability (2605.07212).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.07212](http://arxiv.org/abs/2605.07212v1)
