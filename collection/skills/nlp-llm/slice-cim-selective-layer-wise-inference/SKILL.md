---
name: slice-cim-selective-layer-wise-inference
description: "Research paper: SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based E"
tags: [arxiv, paper, cs.AR, cs.NE]
arxiv_id: "2610.37601"
utility: 0.92
---

# SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory

**arXiv:** [2610.37601](https://arxiv.org/abs/2610.37601)
**Authors:** Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma
**Published:** 2026-10-27
**Categories:** cs.AR, cs.NE
**Utility Score:** 0.92

## Abstract

Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register with Decoder (PR/PD), and a Bit-Serial Cycle Controller (CC), co-designed to minimize switching activity, wordline overhead, and leakage. Implemented in TSMC 65-nm CMOS at 335 MHz, the peripheral framework occupies 1769.760 μm2 post-synthesis and 1982.131 μm2 post-PnR. Gate-level VCD analysis reports 6.0706 μW leakage and 288.2902 μW (post-synthesis) / 322.8850 μW (post-PnR) dynamic power, totaling 328.9556 μW (0.2402% of system power). The EE module dominates dynamic power (58.2%), while WLG dominates area (58.1%). System evaluation on MobileNetV2 (CIFAR-100) shows efficiency scaling from 31.35 TOPS/W (8b/8b, 1.2 V) to 454.91 TOPS/W (2b/8b, 0.8 V), achieving 13.33x improvement without bitcell modification or retraining. The framework targets CNN workloads exploiting sparsity, with Transformer extension as future work.

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.AR, cs.NE

## Potential Applications

- Research reference for nlp llm domain
- Building block for future work in this area
