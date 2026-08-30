# KV Cache Recycling to Expand Usable Context Capacity in Low Parameter LLMs

**arXiv ID:** 2512.11851
**Authors:** Prashant Pandey
**Published:** 2025-12-04T17:04:43Z
**Abstract:**
Whether attention key value (KV) states computed for one prompt for a small LLM can be reused to accelerate inference on a new similar prompt, giving an increase to the space to its context memory using an approach called token recycling. Using a standard Hugging Face setup with DialoGPT-medium (a 345M parameter GPT-2 style decoder trained on 147M Reddit exchanges, 2005 to 2017) as the testbed, we build a cache of past activations and get entries by sentence embeddings, then reuse cached past key values when the cached prompt is an exact prefix of the new input. We compare recycled vs. baseline runs on latency and output fidelity, and log reuse depth in tokens. Reproducibility requires no model modifications, cached KVs are serialized to the CPU, reloaded, and supplied to the generate function to continue decoding from the cached prefix. In tests, we observe consistent speedups when prefix overlap exists, with no material degradation in output semantics, and when overlap is absent, behavior matches baseline.

## Skill Description

This skill is generated from the arXiv paper: KV Cache Recycling to Expand Usable Context Capacity in Low Parameter LLMs (2512.11851).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.11851](http://arxiv.org/abs/2512.11851v1)
