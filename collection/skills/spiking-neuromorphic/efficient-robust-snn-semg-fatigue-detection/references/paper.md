# Paper Details

**Title**: Efficient and Robust Spiking Neural Networks for sEMG-Based Muscle Fatigue Detection
**Authors**: Kaiwen Tang, Jiaqi Dong, Zhanglu Yan, Weng-Fai Wong
**arXiv ID**: 2607.11065
**Published**: 2026-07-13T04:05:13Z
**URL**: https://arxiv.org/abs/2607.11065
**PDF**: https://arxiv.org/pdf/2607.11065.pdf

## Abstract

Detecting muscle fatigue via surface electromyography (sEMG) is essential for applications in sports, rehabilitation, and wearable health monitoring. Accurate and timely detection of fatigue is crucial for preventing injuries, optimizing physical performance, and ensuring user safety during prolonged activity. However, existing deep learning models are often unsuitable for this task due to their high computational cost and dependence on large-scale data. In this work, we propose an energy-efficient framework for muscle fatigue detection based on Spiking Neural Networks (SNNs), which exploit sparse, event-driven computation and temporal modeling. We further introduce a quantization-compatible training scheme (SDH) that combines multiple regularization terms to improve robustness under noisy conditions. Evaluated on two public sEMG datasets against a broad set of baselines and under seven noise conditions including physically motivated perturbations, our quantized SNNs match or exceed strong baselines while remaining more stable under diverse noise and reducing estimated energy consumption by up to 201.77x. These results demonstrate the framework's strong potential for real-time deployment in low-power wearable systems.

## Key Contributions
- Proposes an energy-efficient framework for muscle fatigue detection using Spiking Neural Networks (SNNs)
- Introduces quantization-compatible training scheme (SDH) combining multiple regularization terms
- Demonstrates robustness under seven noise conditions including physically motivated perturbations
- Shows up to 201.77x reduction in estimated energy consumption compared to baselines
- Validated on two public sEMG datasets against extensive baselines

## Methodology Summary
1. sEMG preprocessing: filtering, normalization, segmentation
2. Temporal encoding of features into spike trains
3. SNN with LIF neurons trained via surrogate gradients
4. SDH regularization for robustness and quantization compatibility
5. Evaluation under noise and energy consumption analysis
