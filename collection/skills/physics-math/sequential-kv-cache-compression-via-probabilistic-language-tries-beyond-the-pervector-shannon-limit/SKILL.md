# Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit

**arXiv ID:** 2604.15356
**Authors:** Gregory Magarshak
**Published:** 2026-04-10T22:48:19Z
**Abstract:**
Recent work on KV cache quantization, culminating in TurboQuant, has approached the Shannon entropy limit for per-vector compression of transformer key-value caches. We observe that this limit applies to a strictly weaker problem than the one that actually matters: compressing the KV cache as a sequence. The tokens stored in a KV cache are not arbitrary floating-point data -- they are samples from the exact formal language the model was trained on, and the model is by construction a near-optimal predictor of that language. We introduce sequential KV compression, a two-layer architecture that exploits this structure. The first layer, probabilistic prefix deduplication, identifies semantically equivalent shared prefixes across sessions using the trie metric d_T(s, s') = -log_2 P_M(s ^ s') from Probabilistic Language Tries (PLTs). The second layer, predictive delta coding, stores only the residual of each new KV vector from the model's own prediction of it, achieving a per-token entropy bound of H(KV_{i+1} | KV_{<=i}) <= H(token_{i+1} | token_{<=i}). We prove that at typical language model perplexity -- approximately 10-20 for fluent English text -- this bound is 3.3-4.3 bits on average per token position, compared to TurboQuant's 3 bits per vector component (with typical attention heads having 64-128 components). The theoretical compression ratio over TurboQuant is approximately 914,000x at the Shannon limit. Even at 1000x above the entropy floor -- a deliberately pessimistic worst-case overhead, two orders of magnitude above the 2-5x typical of practical source coders -- the ratio remains approximately 914x over TurboQuant, with compression improving rather than degrading as context length grows. The two layers are orthogonal and compose with existing per-vector quantization methods including TurboQuant.

## Skill Description

This skill is generated from the arXiv paper: Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit (2604.15356).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.15356](http://arxiv.org/abs/2604.15356v1)
