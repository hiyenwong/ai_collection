---
name: conditional-brain-charts-transferable-norms
description: Site-transferable conditional normative brain models GAMLSS.
category: ai_collection
---

# Transferable Conditional Brain Charts (NormGAMLSS)

**Source**: Sharma et al. — "Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression" (arXiv: 2610.21660, 15 Oct 2026)

**Trigger words**: normative model, brain chart, GAMLSS, cortical thickness, subcortical volume, site transfer, harmonization, Alzheimer prediction, MCI conversion, structural dissociation, hippocampus, amygdala

## When to Use
- Building normative/reference-range models of brain MRI measures (thickness, volume) across the lifespan
- Transferring a fitted normative model to a new scanner site WITHOUT retraining and WITHOUT inheriting a proxy site's bias
- Extracting clinically prognostic deviation scores (z-scores) beyond cognitive testing
- Deciding how many healthy controls a new site must scan before valid scoring

## Core Ideas

1. **Conditional norms**: model regional cortical thickness (68 Desikan–Killiany regions) conditioned on a single subcortical structure's volume, added to the location parameter. Each deviation then reads "is this individual's cortex within the healthy range GIVEN their subcortical anatomy?" — not merely given age/sex/site/head size. GAMLSS with sinh-arcsinh (SHASH) outcome distribution fits all four distributional parameters (location, scale, skewness, kurtosis); base covariates: age spline, sex, site, Euler number (scan quality), intracranial volume.
2. **Structural dissociation**: the reduction in whole-brain mean absolute cortical deviation when the normative model is conditioned on subcortical volume. It is a per-individual, clinically interpretable quantity: how much of a patient's cortical deviation is accounted for by their subcortical anatomy.
3. **Intercept-only site transfer**: a new site contributes a small age-stratified healthy sample; refit ONLY the intercepts of the four distributional parameters (optionally with site-level covariates like field strength), leaving all learned effects intact. No retraining, no proxy-site bias.

## Key Results (n=21,351 healthy, 216 sites; external: 6 held-out sites + ADNI)

- **Conditioning improves out-of-sample log-score for ALL 10 subcortical structures** (679 structure×region combos: 73.2% positive). Ranking: amygdala (Δ=0.0033, 90% regions), hippocampus (0.0032, 82%), cerebellar cortex, caudate, accumbens, thalamus … cerebellar white matter last. Largest single region gain: hippocampus→right parahippocampal gyrus (Δ=0.032) — anatomically adjacent pairing. Amygdala gain ≈ 0.65% residual-variance reduction on average, up to 3.9% (7.2% hippocampus in best region).
- Subcortical volume on the SCALE parameter too: larger volume → narrower distribution; AIC improves in all 68 regions.
- **~20 age-stratified healthy individuals suffice for site transfer**: gains +1.0% to +12.3% already at 20 (positive at 5/6 sites); 100 individuals adds only 1.5–3.3pp more. Positive in 84–87% of repeated draws at 20; ~57% of the 100-individual gain. Prior art required 25–100+. Site effects are location-dominated: pre-transfer mean z was −0.19 to −0.89 at every site (model overestimates thickness) while SD was already ≈1 (0.896–1.031). With <30 individuals, refit the location intercept ONLY (full 4-parameter refit is unstable below ~5, matches location-only from ~50).
- **ADNI prognosis (Cox + classification, out-of-fold)**: whole-brain z-score + structural dissociation beat CDR-SB alone in ALL 20 structure×transition combos — CN→MCI concordance 0.602→up to 0.678; MCI→AD 0.697→0.740. Hippocampal dissociation adds beyond global z for dementia. Kaplan–Meier separation log-rank P=3.6×10⁻²³ (261/group; 46 vs 134 events); amygdala nearly identical (P=3.3×10⁻²²). Decision-curve net benefit > CDR-SB alone at 15–55% (3-yr) / 10–45% (2-yr) thresholds.
- **Signal lives in the mildest bins**: among individuals with similar CDR-SB (lowest bins), converters show higher z and higher dissociation — separation present at the earliest visit, strongest where the cognitive score is least informative, attenuating as CDR-SB takes over. Landmark analysis: +0.055 concordance at earliest landmark (95% CI 0.022–0.088). Within-CV structure selection confirms MCI→AD (+0.014, CI 0.002–0.028); CN→MCI does not persist — treat hippocampus/amygdala as robust and the CN→MCI claim as weaker.
- **What conditioning does NOT do**: it is not a more sensitive thinning detector — conditioning on a disease-affected covariate absorbs part of the disease effect (nearly all of it in dementia; only part in MCI). It redefines the question: is the cortex thinner than expected given THIS individual's subcortical volumes?

## Method Recipes

- Fit per-region GAMLSS/SHASH with four distributional parameters; per-parameter formulas are required for conditional models (NormGAMLSS Python package implements this + site transfer).
- Site transfer: draw ~20 age-stratified healthy controls spanning the site's age range; refit intercepts (location-only if n<30, all four if n≥50); include field strength on all four parameters when mixed scanners (substantial uncorrected bias otherwise).
- Clinical use: compute whole-brain z + dissociation, evaluate against CDR-SB out-of-fold; select the conditioning structure INSIDE cross-validation folds to avoid optimism.
- Software landscape: PCNtoolkit (Bayesian, transfer/extension/merging), Lifespan Brain Chart (pretrained, offset re-estimation), CentileBrain (harmonize-then-apply), Brain MoNoCle (no-code, mean/SD calibration ≥30). NormGAMLSS's edge: per-parameter formulas + any-subset intercept refit + field-strength covariates.

## Caveats
- Gains from conditioning are individually small (mean ΔLog-score ~0.001–0.003) but systematic; a conditional norm is a different clinical question, not a better thinning detector.
- Calibration gain magnitude varies considerably between sites; instability below ~5 individuals can make transfer WORSE than none.
- CN→MCI dissociation effect did not survive within-fold structure selection; strongest evidence is MCI→AD conversion.

**Activation**: normative model, brain chart, GAMLSS, site transfer, cortical thickness, hippocampus, structural dissociation, Alzheimer conversion, MCI, harmonization, SHASH