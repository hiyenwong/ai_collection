---
name: gas-pfn-graph-aware-spatiotemporal-prior
description: "Research paper: GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Tra"
tags: [arxiv, paper, cs.LG, cs.AI, cs.NE]
arxiv_id: "2610.37598"
utility: 0.89
---

# GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

**arXiv:** [2610.37598](https://arxiv.org/abs/2610.37598)
**Authors:** Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo...
**Published:** 2026-10-27
**Categories:** cs.LG, cs.AI, cs.NE
**Utility Score:** 0.89

## Abstract

Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. Existing forecasting PFNs, however, do not explicitly represent the graph-structured dependencies governing traffic dynamics. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN). GAS-PFN incorporates sampled road topology into its synthetic task prior through random-walk diffusion, teaching the model to learn graph-coupled dynamics during pretraining. Its co-designed inference architecture uses two mask-conditioned passes through a shared Transformer backbone to separately model sensor-specific temporal dynamics and spatiotemporal interactions among neighboring sensors before integrating their representations for prediction. This design enables GAS-PFN to use target-network structure and context without parameter updates. Across six benchmarks at the 90-minute horizon, GAS-PFN reduces MSE by 34.0% on average relative to TimePFN, its closest PFN-based predecessor. It also reduces MSE by 27.7% o

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG, cs.AI, cs.NE

## Potential Applications

- Research reference for vision generative domain
- Building block for future work in this area
