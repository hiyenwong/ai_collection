---
name: llm-benchmark-factor-analysis
description: Psychometric factor analysis of LLM benchmark scores.
category: ai_collection
tags: [llm-evaluation, psychometrics, factor-analysis, g-factor, omega-hierarchical, benchmark-super-sparsity, imputation, schmid-leiman, mutualism, machine-intelligence]
---

# Large-Scale Factor Analysis of LLM Benchmarks (g-factor audit)

**arXiv 2609.36515** (2026-09-29) — Haznitrama, Azizy, Ardi (KAIST). The widest-to-date psychometric analysis of machine intelligence: **13,251 evaluation scores × 1,618 models × 456 text-only benchmarks**, showing machine intelligence is only partially interpretable — a general factor accounts for at most 70.8% of variance (25.7% for the best imputer), domain-similar benchmarks don't cluster, and g is not well-proxied by standard "intelligence" benchmarks.

## When to Use
- Auditing whether a set of benchmarks actually measures a coherent latent capability
- Deciding whether to target a single "general intelligence" construct in training/eval programs
- Handling super-sparse model×benchmark score matrices (MNAR missingness) before factor analysis
- Designing evaluation suites: how to test if capability claims cluster

## Core Methodological Pattern

### 1. Super-sparse MNAR matrix pipeline (transferable!)
Raw matrix is 1,618 × 456 at ~1.8% density, missing-not-at-random (popular models/benchmarks over-observed).
- **Densification (peeling)** toward common target density (10%), three strategies that sacrifice different axes:
  - **C (column-primary)**: drop least-observed benchmarks → keeps famous benchmarks, wide model coverage
  - **R (row-primary)**: drop least-observed models → broad benchmark set over few heavily-evaluated models
  - **S (symmetric)**: drop whichever marginal has lowest fill-rate
  - After peeling: drop models/benchmarks with <3 observed scores; drop zero-variance columns
- **Deduplication**: average duplicate (model, benchmark) rows; two collapse strategies — **variant-level** (keeps versions/parameter counts, collapses reasoning-effort/knowledge-cutoff) vs **aggressive family-level** (all Claude/Llama generations → one row) to protect IID assumptions.
- **Metric selection**: one metric per benchmark (widest model coverage wins, with manual override list).
- **Imputation triangulation** (the key robustness move): full-dataset algorithms (SoftImpute, k-NN, missForest) + correlation-recovery (one-sided matrix completion, USVT, SoftImpute on correlation matrix with zero/mean fill + PSD smoothing). Gate: held-out R² ≥ 0.2 on ~20% column-stratified mask (baseline = column training mean), R² selects hyperparameters.

### 2. Hierarchical factor analysis
- **Exploratory FA (EFA)** with min-residual estimator + **oblique promax rotation** (factors allowed to correlate)
- **Schmid–Leiman bifactor transformation** → one general factor g influencing all extracted factors (more principled than "highest eigenvalue = g")
- **Parallel analysis** (Horn 1965) selects number of factors; cap at 20
- Report **ω_h** (omega hierarchical) = σ²_g/σ²_T — the share of indicator variance explained by g

### 3. Label cohesion analysis (is a claimed "capability" real?)
- Benchmark similarity = cosine distance between factor-loading vectors
- For each label (claimed capability family): compare **within-label mean pairwise distance** vs **coverage-quartile-stratified null** (2,000 permutation redraws) — coverage stratification is essential because coverage itself correlates with tightness
- Effect size A = 1 − within/null_mean (0 = no tighter than chance, negative = more spread than chance); empirical p-value; **Benjamini–Hochberg FDR q=0.05** within each axis

## Key Findings (what to replicate/check)
1. **ω_h range 0.20–0.71** across dataset-imputer combos; best imputer (SoftImpute on S Std.) gives only **25.7%**. Newer models score higher on g, but g's variance share shows no trend with release year.
2. **Content-similar benchmarks do NOT necessarily cluster** (math and coding can separate).
3. **g has no dominant common theme** — highest loadings often go to miscellaneous tasks; standard "reasoning" benchmarks are poor g-proxies.

## Interpretation Framework (three paradigms)
| Paradigm | Model of correlations | Verdict here |
|---|---|---|
| **Reflective** (latent g causes performance) | factor analysis assumed | structure incoherent → unsupported |
| **Formative** (PCA, no causal claim) | components w/o cause | compatible but uninformative |
| **Mutualist** (abilities mutually cause each other; Borsboom–Cramer network) | partial-correlation graph; no common cause | attractive alternative — reproduces positive manifold w/o g |

**Practical consequence**: if the mutualist view is right, "target g in training" is untenable — g is a summary scalar, not a targetable ability; generalization must come from brute-force task coverage, not silver-bullet constructs. Causal test: fine-tune on task A, measure transfer to task B (cf. Meng et al. 2026: input similarity predicts best transfer source for ≤2/8 tasks; **gradients predict transfer better than content**).

## Implementation Sketch
```python
# 1. Peel sparse matrix toward 10% density (3 strategies: C/R/S)
# 2. Impute with ≥6 methods; gate each by held-out R² ≥ 0.2 (col-stratified 20% mask)
# 3. For each passing solution:
fa = FactorAnalyzer(estimator='minres', rotation='promax', n_factors=parallel_analysis(X))
# 4. Schmid-Leiman bifactor → g loadings; report ω_h per solution
# 5. Label cohesion: cosine distance of loading vectors vs coverage-stratified null (2000 draws)
# 6. Triangulate: only claims stable across imputers/densifiers survive
```

## Related
- [[eeg-fm-audit-systematic-evaluation]] — same triangulate-across-preprocessing audit philosophy for EEG foundation models
- [[identical-twins-eeg-benchmark]] — benchmark-structure auditing
- [[heterogeneous-neural-predictivity-lm]] — LM evaluation methodology
- EveryEvalEver schema (Batzner et al. 2026) — unified eval-result schema used for collection

**Activation keywords**: LLM benchmark, factor analysis, g factor, general intelligence, omega hierarchical, Schmid-Leiman, bifactor, promax rotation, parallel analysis, MNAR, imputation, SoftImpute, missForest, USVT, matrix completion, label cohesion, mutualism, psychometrics, evaluation validity, benchmark design
