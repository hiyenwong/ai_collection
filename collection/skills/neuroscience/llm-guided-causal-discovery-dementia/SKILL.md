---
name: llm-guided-causal-discovery-dementia
description: LLM-guided causal discovery for epidemiology. Use when inferring causal pathways from high-dimensional biobank data.
category: ai_collection
trigger: LLM feature selection epidemiology, causal discovery biobank, PC algorithm mediation, dementia pathway analysis, UK Biobank causal inference
---

# LLM-Guided Causal Discovery for Epidemiological Pathway Analysis

Source: Khan, Benos, Wong, Fang, "Causal discovery identifies pathways linking physical activity to dementia risk in the UK BioBank", arXiv:2610.02221 (q-bio.NC, Sep 2026). 42,293 UK Biobank adults ≥60y, accelerometer-derived MVPA → incident dementia (647 cases, 1.5%).

## Core Pipeline (5 stages — the reusable method)

**Problem**: causal discovery on biobank-scale data fails because variable dictionaries have thousands of semantically heterogeneous fields; manual selection is biased and unscalable. Solution: LLM agents do knowledge-informed feature selection, then classical causal algorithms run on a tractable variable set.

1. **LLM preselection**: batch-classify every candidate variable (title + field description) as relevant / not relevant to the exposure→outcome pathway. UKB full dictionary → filtered pool.
2. **Multi-model relevance scoring**: 4 GPT-family models (gpt-4o-mini, gpt-4.1, gpt-oss-120b, gpt-5) each score retained variables s_j ∈ [0.1, 1.0]; aggregate mean, threshold at 0.60.
3. **Reviewer-agent stage**: multiple domain-expert personas (causal inference, epidemiology, neuroimaging, physical-activity science) independently re-score — multi-perspective mechanistic relevance, guards against single-model bias.
4. **Census ranking + aggregation agent**: consensus ranking; take top 500 → 250 → 100.
5. **Expert curation + preprocessing**: manual check of top 100; drop high-missingness variables; remove redundancy by pairwise correlation (multicollinearity); force-include known risk factors (hearing impairment, brain injury) derived from harmonized ICD-9/10 codes. Final: **39 variables**.

## Causal Discovery with Domain Constraints

- **Structural constraints from background knowledge B**: exogenous variables ℝ (demographics: sex, age, ethnicity, education, deprivation) forced `Parent(X_k) = ∅`; outcome (dementia) forced sink `Child(Y) = ∅`. This prevents implausible edges (dementia → age) without over-constraining.
- **PC algorithm** (constraint-based): conditional independence X_i ⊥ X_j | S tested via Fisher Z-transform of partial correlation, α = 0.05.
- **Nonparametric bootstrap**: re-estimate the DAG across resampled datasets; keep edges by structural-stability frequency. Report bootstrap stability alongside every edge — low-stability edges (0.07–0.10 for cardiometabolic chains) are flagged as weak, not presented as findings.
- **Reverse-causation control**: exclude incident dementia cases within 1/2/4/5-year windows after exposure assessment; track how the causal structure and mediation shares shift with window length.

## Chain Mediation Analysis (SEM)

- Causal pathway P = (X, M_1, …, M_k, Y); standardized path coefficients via DWLS estimation.
- β_indirect = product of chain coefficients; β_total = β_direct + β_indirect; **% mediated = β_indirect / β_total × 100**.
- Adjust for a-priori covariates (age, sex, education, ethnicity, deprivation, smoking, alcohol).

## Key Findings (the case study)

- **Depression is the central modifiable pathway**: MVPA → depression → dementia mediates **15.06%** (β_indirect = −0.0028 of β_total = −0.0183). Males 19.31% vs females 12.27%.
- **Exclusion-window dynamics**: with 5-year exclusion, % mediated rises to 23.8% overall and **60.8% in males** (females stable 11.6–13.0%); the direct MVPA→dementia path attenuates to non-significance — the association becomes almost fully mediated at long horizons.
- **Walking-pace chain** (MVPA → walking pace → depression → dementia) adds only 3.13%, stable across sexes and windows.
- **Sex-stratified structure**: females = metabolic-functional pathways (triglycerides, waist circumference, walking pace); males = behavioral + cardiometabolic cascades (smoking, PM10 exposure, hearing impairment, CVD, CKD).
- Longer exclusion windows surface additional multi-step cardiometabolic/neurological chains (hypertension, heart disease, brain injury, CKD) but with low bootstrap stability (0.07–0.10) — honest reporting distinguishes these from the robust depression pathway.

## Data-Quality Gates (accelerometer cohort)

Exclude: any missing hour in 24h cycle; nocturnal activity >10% of daily MVPA (01:00–04:00, sleep-disorder proxy); wear time <72h; uncalibrated/reused devices; >768 IQR anomalies; dementia diagnosis within 1y of assessment. MVPA quantified by Random Forest on 7-day wrist-worn data.

## Reuse Patterns

- **Any high-dimensional observational study** with a semantically rich data dictionary: swap the LLM preselection domain prompt, keep the 5-stage funnel (preselect → score → reviewer-ensemble → rank → curate).
- **LLM ensemble scoring > single LLM**: 4 models + expert personas reduced single-model idiosyncrasy; threshold 0.60 was the working point.
- **Always combine**: LLM selection (knowledge) + PC/constraint-based discovery (data) + bootstrap (stability) + mediation SEM (quantification) + exclusion windows (reverse causation). No single stage suffices.
- **Report bootstrap stability with every edge**; separate robust findings (depression, stability high) from suggestive ones (CKD chains, 0.07–0.10).
- Limitations to carry: observational data cannot exclude residual confounding; bidirectional depression↔MVPA possible; LLM selection reproducibility depends on model versions; short (7-day) exposure window.

## Related Skills

`agentic-evidence-seeking-clinical` (evidence retrieval), `polydag-efficient-causal-discovery` (acyclicity constraints), `gp-cake-brain-connectivity` (causal kernel modeling), `llm-claims-data-actuarial-analysis` (LLM variable extraction).
