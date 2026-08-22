---
name: arxiv-2608-20240-quasar-a-quantum-classical-neural-network-for-sar
description: 'QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication (arXiv: 2608.20240)'
category: neuroscience
version: "1.0"
date: 2026-08-22
---

# QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication

**Authors:** Vincenzo Sammartino, Nathanael Denis, Roberto Di Pietro
**arXiv:** 2608.20240
**Utility:** 1.00
**Published:** 2026-08-20T16:31:01Z
**Link:** http://arxiv.org/abs/2608.20240

## Abstract

X-band SAR satellites (8-12 GHz) play a critical role in disaster response, environmental monitoring, and military intelligence. Yet, they lack robust physical-layer authentication (PLA), a security layer orthogonal to cryptographic solutions. Existing PLA systems, typically based on radio-frequency fingerprinting, are often limited to sub-6 GHz frequencies and rely on classical deep learning. However, this approach underfits the IQ phase nonlinearities that distinguish satellite hardware. In this paper, we present QUASAR, to the best of our knowledge the first quantum-classical hybrid architecture that fuses a CNN spectrogram encoder with a variational quantum circuit (VQC) to provide PLA to X-band SAR signals. Our solution enjoys two distinctive features: (i) it is markedly more data-efficient than classical machine learning, requiring only 10% of the training data to match the accuracy of classical baselines -- data collection being notoriously the most time-consuming phase of PLA; and, (ii) at an equal data budget, it improves classification accuracy over those baselines. In detail, we test our solution under three adversarial scenarios: replay, crafted-IQ injection, and space-borne spoofing. QUASAR rejects spoofed transmissions in 89.7%, 94.1%, and 81.3% of attempts, respectively, establishing the first quantum-enhanced physical-layer classifier for satellite constellations. The fully detailed framework and the supporting results, other than being interesting on their own, show a novel research avenue for physical-layer authentication.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "QUASAR: A Quantum-Classical Neural Network for SAR Satellite Physical-Layer Authentication". 
The paper presents novel ideas in neuroscience that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20240
