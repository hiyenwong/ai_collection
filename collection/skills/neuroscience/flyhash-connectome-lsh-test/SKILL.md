---
name: flyhash-connectome-lsh-test
description: Use when testing bio-inspired LSH or connectome wiring against null models. Fly hash replication protocol.
category: ai_collection
trigger_words: fly hash, locality-sensitive hashing, connectome null model, degree-preserving rewiring, Kenyon cell fan-out, curveball randomization, sparse binary projection, winner-take-all hash
metadata:
  arxiv_id: "2610.09114"
  published: "2026-10-06"
  authors: "Sebastian Senge"
  tags: [connectomics, locality-sensitive-hashing, similarity-search, null-models, replication, drosophila]
---

# Fly Hash Connectome Test (arXiv 2610.09114)

Senge (independent researcher), "A Connectome Test of the Fly Hashing Algorithm" — a documented replication of Dasgupta/Stevens/Navlakha 2017 (Science) that substitutes four real EM connectomes for the random projection matrix and answers: does measured wiring actually matter for similarity search?

## Core Findings

1. **The 2017 pattern replicates** on SIFT, MNIST, odour mixtures (GloVe near chance at short codes for every method): sparse WTA hash beats k Gaussian projections at short hash lengths (3.1× AP@200 on MNIST at k=4). Advantage shrinks with k; on odours/GloVe LSH overtakes from k≈8–16.
2. **The advantage is per active cell, not per operation.** The 2017 comparison equates k active cells with k projections. At m=10d cells sampling d/10 inputs each, the fly hash spends ≈d² additions vs 2kd for LSH (~98× on MNIST k=4). Given the SAME projection arithmetic, real-valued Gaussian LSH retrieves better on every dataset and every input dimension tested. Against one-bit sign codes the comparison is closer (fly wins per active cell, ~parity at matched ops from k=32).
3. **Measured connectome pairing gives no consistent retrieval advantage over degree-preserving rewiring** — slightly worse (median −1.6% across 168 hemisphere×dataset×size combos; negative in 134, below every null draw in 59, above in 2). On odours at primary k=92: −2.06% (p=0.020), within ±5% equivalence margin but not ±2.5%. Odour deficit depends on how unmeasured DoOR entries are treated (imputation moves it to −0.7%…+0.6%).
4. **Fan-out skew costs retrieval and is conserved.** Equalising glomerular fan-out at fixed connection count improves AP in all 7 hemispheres (+3.9% to +6.4%); equalising inputs per cell lowers it (all 7 negative). Yet the fan-out profile is similar across four animals (between-animal Spearman ρ median 0.86, spanning ~17× from DP1m/DM1/DC1 top to DA4m/DA3/VL1 bottom), structural synapse counts correlate positively with fan-out (6/7 hemispheres — they AMPLIFY the skew rather than offset it), and relation to odour tuning is weak (ρ=+0.13–0.30 breadth).
5. **Practical takeaway**: a fly hash needs NO connectome data — random sparse wiring with even fan-out does at least as well. The biological skew may serve other ends (innate valence, novelty detection) that generic retrieval doesn't score.

## Methodology (replicable protocol)

### Protocol provenance discipline
- Every protocol element traced to source: 2017 main text / 2018 FlyLSH code / "ours" (Table I in paper). The 2017 paper reported "mean average precision" with NO formula — precision averaged over retrieved true neighbours reproduces the LSH baseline (0.159 vs 0.160) but not the fly score (0.365 vs 0.448). Use AP@n = (1/n)Σ prec@i·rel(i) over the n true neighbours so misses count, plus recall@n.
- Image/word datasets are PCA-reduced to one component per glomerulus (49–51), assigned to glomeruli by a fresh random permutation each trial — testing wiring STATISTICS, not odour-specific pairing.

### The hash
```
y = M^T x          # M ∈ {0,1}^{d×m}, binary glomerulus→Kenyon-cell matrix
tag = top-k(y)     # k most active cells; ties at threshold in index order (random tie priority = sensitivity analysis)
```
Retrieval scored by AP@200 + recall@200; LSH = k Gaussian projections kept as real values (or signs for bit codes). Budgets: per active cell, per stored bit, per operation (d mults + d adds per projection; one add per nonzero of M; winner selection excluded).

### Degree-preserving null (the key control)
- Curveball algorithm: uniform sampling over binary matrices with same row+column sums, 30 trades per cell. Co-occurrence Q = Σ_{j<l}(MM^T)²_jl stable from 1 sweep. Keeps BOTH degree sequences, randomises which glomeruli share a cell. Tests against it = approximate Monte Carlo randomization tests.
- Q-detected structure: 6 of 7 hemispheres depart from null (Qz 0.0–17.8, Holm-adjusted p≤0.010) — wiring IS structured, but that structure does not buy retrieval.
- hemibrain appears null-consistent ONLY because of weak connections: at ≥2-synapse threshold its Q rises above null (z=+2.9, p=0.002) in all 7 hemispheres. "Apparent exception is a property of its weakest connections."

### Equal-connection controls (one degree sequence at a time)
At exactly nnz(M) ones: even fan-out, even inputs-per-cell, both even, random pairing. Separates WHICH degree sequence drives effects — the null comparison cannot do this since connectome and null share both sequences.

### Odour pipeline
DoOR 2.0 consensus matrix, 35 glomeruli with ≥40 odorants measured, 172 odorants (28.7% unmeasured → zero). Benchmark: 4000 linear mixtures of 2–5 profiles, unit-mean normalised; ground truth = κ=10 nearest on raw responses. Primary k=92 (5% of cells). Two-stage bootstrap: resampled odorants, regenerated mixtures, 20 nulls per replicate × 200 replicates, ±5% equivalence margin. Pre-registered (PREREGISTRATION_2026-09-28.md) AFTER first results with 100 nulls — not preregistration of the hypothesis, only of ensemble sizes.

### Novelty detection surrogate (static, not dynamic)
Bloom-filter surrogate: after storing n items, cell j's output weight w_j = 1 − c_j/n (c_j = stored items activating it); query novelty = mean w_j over its k active cells. Classifier predicts class whose filter finds query least novel. Connectome again shows no advantage over null; even fan-out raises MNIST classification (+0.010 AUC).

## Critical Apparatus Worth Copying

- **Per-active-cell vs per-operation budget accounting** — apply to ANY bio-inspired algorithm claim: "beats X" must state which resource is equalised. Where arithmetic is cheap, dense real-valued projections win; where ACTIVE UNITS are the binding cost (neuromorphic/sparse hardware), the fly hash may win — a hypothesis the paper deliberately does not test.
- **Connectome availability changed the question**: 2017 used random wiring because the wiring was unknown; Zheng et al. 2022 showed structured sampling; this paper closes the loop for the retrieval task. Pattern: when a "random" idealisation in a classic result becomes measurable, re-run the original protocol with the measured quantity and degree-preserving nulls.
- **Descriptive counts vs independent replications**: 7 hemispheres from 4 animals are dependent (one male cannot separate sex from reconstruction differences). Holm adjustment across hemispheres; unadjusted p-values flagged as such.
- **Null ensembles sized after seeing first results** are honestly labelled: "this is not a preregistration". Pre-registration also held 3 theory experiments that FAILED their registered criterion — reported in OUTCOMES file, not buried.

## Implementation Notes

- Code: https://github.com/ssenge/FlyHash-Connectome (documented provenance, data checksums, supplement)
- Connectomes: MaleCNS v1.0 (male, both hemispheres), hemibrain v1.2 (female R), FlyWire v783 (female both), BANC v888 (female both). 49 shared glomeruli, 1761–2406 Kenyon cells, 5.00–6.05 inputs/cell. Primary: MaleCNS R (d=51, m=1886).
- Rule: uniglomerular olfactory PNs assigned by cell type (multiglomerular/thermo/hygro excluded), every reconstructed connection counts (no synapse threshold), cells without olfactory input dropped. Hemibrain glomerulus names mapped via cross-dataset matches.
- AP metric pitfall: conventions that ignore unretrieved true neighbours (misses) inflate fly-hash scores; always report a misses-counting metric alongside.

## Limitations (paper's own)

Four animals, one male; connectome differences mix biology and reconstruction. Reimplementation recovers published ORDERING but not absolute values; two protocol details from later code. Image/word input compressed to one PCA component per glomerulus with arbitrary assignment. Cross-connectome runs use 50 nulls (effect estimates). Odour deficit depends on zero-imputation of unmeasured DoOR entries. Model is binary, rate-free, ignores inhibition beyond WTA.

## Related Skills

- [[connectome-only-message-passing-fly-vision]] — companion result: structure alone supports fly visual computation (opposite conclusion for vision vs olfaction retrieval)
- [[connectome-wiring-specificity-null-models]] — nested rewired nulls methodology
- [[boundary-preserving-null-connectome]] — randomising connectomes as baselines
