---
name: arxiv-2610-10358-open-mmunlearning-unifying-methods-and-evaluation-for-mllm-unlearning
description: 'Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning (arXiv: 2610.10358)'
metadata:
  {
    "arxiv_id": "2610.10358",
    "utility": 0.94,
    "title": "Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning",
    "authors": "Junkai Chen, Yuhao He, Qianshan Wei, Junxiang You, Jingwen Shao...",
    "url": "https://arxiv.org/abs/2610.10358v1",
    "categories": ["cs.AI"],
    "published": "2026-10-07"
  }
---

# Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning

**arXiv ID:** 2610.10358
**Authors:** Junkai Chen, Yuhao He, Qianshan Wei, Junxiang You, Jingwen Shao...
**URL:** https://arxiv.org/abs/2610.10358v1
**Utility Score:** 0.94
**Published:** 2026-10-07
**Categories:** cs.AI

## Summary

As multimodal large language models (MLLMs) become more capable and widely deployed, concerns about privacy and safety have become increasingly pressing. Machine unlearning offers one approach to addressing these concerns by removing designated information from trained models while preserving unrelated capabilities. However, fragmented implementations and evaluation protocols, incomplete robustness testing, and limited understanding of metric reliability make progress in MLLM unlearning difficult to assess systematically. We introduce Open-MMUnlearning, an open-source, extensible framework that integrates target-model preparation, multimodal data processing, unlearning, and evaluation through shared interfaces and structured configurations. The framework supports five benchmarks spanning privacy, safety, and copyright, eight MLLMs from four model families, and twelve unlearning methods. Its evaluation suite jointly assesses forgetting effectiveness, retained utility, and robustness to model interventions, adversarial inputs, and membership inference attacks. Using a common evaluation protocol, we compare ten representative unlearning methods. In this comparison, GD and MIP-Editor tie for the highest overall score: GD achieves the highest Forget Quality, while MIP-Editor preserves more Model Utility. We further introduce a metric meta-evaluation protocol that tests faithfulness using models with controlled exposure to target knowledge and robustness under quantization and relearning. Among the thirteen evaluated metrics, BLEU achieves the highest aggregate reliability score. KS-Test attains the highest faithfulness AUC but performs less well on robustness. Together, the framework and these findings support reproducible comparison of MLLM unlearning methods and systematic assessment of evaluation reliability.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10358v1
