---
name: overcoming-the-representational-limitations-of-amplitude
description: "Overcoming the Representational Limitations of Amp..."
tags: [quant-ph, cs.ET, cs.LG]
source: arxiv
arxiv_id: 2610.41824v1
utility: 0.89
published: 2026-10-30
---

# Overcoming the Representational Limitations of Amplitude Encoding for Quantum Neural Networks

**Authors:** Vincent Gurgul, David Prinz
**Published:** 2026-10-30
**arXiv:** [2610.41824v1](https://arxiv.org/abs/2610.41824v1)
**Categories:** quant-ph, cs.ET, cs.LG, math.OC
**Utility Score:** 0.89

## Abstract

Quantum Neural Networks (QNNs) offer a framework for learning functions from classical data, but their expressive power depends critically on how inputs are encoded into quantum states. Angle encoding can require resources that scale with the number of features, whereas amplitude encoding represents $d$ features using only $\mathcal{O}(\log_2 d)$ qubits. This compactness comes at a representational cost: normalization makes conventional amplitude encoding invariant to nonzero real rescaling of the input, up to an unobservable global phase. We show that this invariance induces an exact, architecture-independent restriction on the resulting hypothesis class. No downstream quantum circuit can distinguish inputs differing by nonzero real scaling. We develop a general condition under which deterministic preprocessing can remove this ambiguity and show that nonlinearity alone is insufficient. Based on this analysis, we introduce a fixed nonlinear feature map that provably distinguishes all real inputs under subsequent amplitude encoding, without adding trainable parameters and while retaining logarithmic qubit scaling. We evaluate the resulting QNN on three canonical classification benchmarks and a nonlinear synthetic dataset against conventional amplitude and angle encoding, as well as a classical neural network. Across these tasks, the proposed encoding consistently improves classification accuracy over both quantum encoding baselines by 21$-$44 %. Our results establish normaliza

## Key Contributions

- Novel research in quant-ph, cs.ET
- Published 2026-10-30

## Activation

overcoming, representational, limitations, amplitude, encoding, quantum, neural, networks
