---
name: arxiv-2610-10381-residualquant-kv-cache-quantization-for-looped-transformers-with-2-bit-residuals
description: 'ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals (arXiv: 2610.10381)'
metadata:
  {
    "arxiv_id": "2610.10381",
    "utility": 1.0,
    "title": "ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals",
    "authors": "Heejun Kim, Junyoung Lee, SangLyul Cho, Dongsu Han, Insu Han...",
    "url": "https://arxiv.org/abs/2610.10381v1",
    "categories": ["cs.LG"],
    "published": "2026-10-07"
  }
---

# ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals

**arXiv ID:** 2610.10381
**Authors:** Heejun Kim, Junyoung Lee, SangLyul Cho, Dongsu Han, Insu Han...
**URL:** https://arxiv.org/abs/2610.10381v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.LG

## Summary

Looped Transformers improve parameter efficiency by repeatedly applying shared Transformer blocks over multiple recurrent loops, increasing computational depth without increasing the parameter count. However, KV cache memory still scales with the number of loops, becoming a key memory bottleneck that limits batch size and inference throughput. KV cache quantization can alleviate this bottleneck, but existing methods often suffer substantial accuracy degradation at aggressive low-precision regimes. We observe that looped Transformers offer a unique opportunity: KV states across loops are highly similar. Based on this observation, we propose ResidualQuant, which uses the final-loop KV states as a reference and represents the remaining loops with low-precision residuals. Our method further combines least-square scaling and rotations applied to the residuals, as well as loop-wise mixed precision, to enable accurate quantization down to INT2 while retaining efficient reconstruction. Across multiple looped Transformer models and mathematical reasoning and code generation benchmarks, ResidualQuant consistently improves the accuracy-memory tradeoff over state-of-the-art rotation-based KV quantization. In particular, our method retains accuracy close to BF16 under mixed-precision settings while reducing theoretical KV storage by 80.7%, achieving up to 13.0% higher accuracy than the rotation-based baseline at the same memory budget. On an RTX 5090, the reduced KV memory traffic improves fixed-batch decode throughput by up to 2.73x, while the smaller memory footprint enables up to 2x larger batches, improving peak throughput by up to 4.15x.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10381v1
