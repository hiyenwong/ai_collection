---
name: fast-and-accurate-neural-triage-decoding
description: "Fast and accurate neural triage decoding of ultra-..."
tags: [quant-ph, cs.AI, cs.IT]
source: arxiv
arxiv_id: 2610.40490v1
utility: 0.93
published: 2026-10-29
---

# Fast and accurate neural triage decoding of ultra-high-rate quantum LDPC codes

**Authors:** Hong-Ye Hu, Zhenlai Wang, Binzhao Luo, Tao Xiang, Chen Zhao
**Published:** 2026-10-29
**arXiv:** [2610.40490v1](https://arxiv.org/abs/2610.40490v1)
**Categories:** quant-ph, cs.AI, cs.IT, cs.LG
**Utility Score:** 0.93

## Abstract

Quantum error correction is essential for fault-tolerant quantum computing. High-rate quantum low-density parity-check (qLDPC) codes have emerged as a promising approach to reducing the substantial physical qubit overhead of quantum error correction, enabling encoding rates exceeding $1/2$ in blocks of approximately one thousand physical data qubits. However, their practical implementation requires decoders that combine high accuracy with low latency to keep pace with quantum hardware. Existing decoders of high-rate qLDPC codes can achieve high accuracy but often incur substantial computational latency, whereas neural network decoders have yet to be demonstrated for high-rate qLDPC codes. Here, we introduce \emph{neural triage decoding}, a framework that uses syndrome consistency to adaptively allocate neural computation. A local neural message-passing network rapidly predicts error corrections, additional iterations reduce residual syndrome violations, and a rarely invoked diversification stage searches for consistent corrections to the remaining shots. We demonstrate that the \texttt{Triage} decoder can decode ultra-high-rate qLDPC codes encoding a few hundred logical qubits, including lifted-product and Kasai codes, achieving state-of-the-art accuracy comparable to the near optimal algorithmic decoders while reducing decoding latency by approximately one to two orders of magnitude. Our framework is inspired by a rigorous analysis of the exact bitwise marginal decoder, reve

## Key Contributions

- Novel research in quant-ph, cs.AI
- Published 2026-10-29

## Activation

fast, accurate, neural, triage, decoding, ultrahighrate, quantum, ldpc, codes
