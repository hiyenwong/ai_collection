# SEval-NAS: A Search-Agnostic Evaluation for Neural Architecture Search

**arXiv ID:** 2603.00099
**Authors:** Atah Nuh Mih, Jianzhou Wang, Truong Thanh Hung Nguyen, Hung Cao
**Published:** 2026-02-17T15:02:02Z
**Abstract:**
Neural architecture search (NAS) automates the discovery of neural networks that meet specified criteria, yet its evaluation procedures are often hardcoded, limiting the ability to introduce new metrics. This issue is especially pronounced in hardware-aware NAS, where objectives depend on target devices such as edge hardware. To address this limitation, we propose SEval-NAS, a metric-evaluation mechanism that converts architectures to strings, embeds them as vectors, and predicts performance metrics. Using NATS-Bench and HW-NAS-Bench, we evaluated accuracy, latency, and memory. Kendall's $τ$ correlations showed stronger latency and memory predictions than accuracy, indicating the suitability of SEval-NAS as a hardware cost predictor. We further integrated SEval-NAS into FreeREA to evaluate metrics not originally included. The method successfully ranked FreeREA-generated architectures, maintained search time, and required minimal algorithmic changes. Our implementation is available at: https://github.com/Analytics-Everywhere-Lab/neural-architecture-search

## Skill Description

This skill is generated from the arXiv paper: SEval-NAS: A Search-Agnostic Evaluation for Neural Architecture Search (2603.00099).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2603.00099](http://arxiv.org/abs/2603.00099v1)
