---
name: making-claude-chemist
description: "Methodology from Anthropic research (Jun 2026) on benchmarking LLM capability for chemistry tasks, specifically NMR spectral analysis and molecular structure elucidation. Opus 4.7 achieves competitive accuracy with ChemDraw/MestReNova on hydrogen NMR (±0.079 ppm error), carbon NMR, peak shape prediction, and 1D inverse structure elucidation. Use when evaluating LLM performance for chemistry workflows, building AI-assisted molecular analysis tools, or understanding chemistry-specific AI benchmarks. Activation: Claude chemist, NMR spectral analysis, molecular structure elucidation, AI chemistry benchmark, Opus chemistry, Anthropic chemistry, chemical structure from spectra."
version: 1.0.0
author: Anthropic Research
date: 2026-06-05
source: https://www.anthropic.com/research/making-claude-a-chemist
category: ai_collection
tags: [chemistry, NMR, molecular-analysis, benchmark, spectral-analysis, structure-elucidation]
activation_keywords: [Claude chemist, NMR spectral analysis, molecular structure elucidation, AI chemistry benchmark, Opus chemistry, chemical NMR, Anthropic chemistry, 1D inverse elucidation, chemical structure from spectra]
---

# Making Claude a Chemist

## Core Problem

Chemistry involves translating between multiple molecular representations:
- **SMILES** (text strings encoding molecular graphs)
- **Chemical structures** (2D/3D drawings)
- **NMR spectra** (instrument readouts showing peak positions)
- **Molecular formulas** (elemental composition)
- **Journal figures** (visual representations in papers)

Translating between these formats is time-consuming and error-prone. AI tools have been positioned as transformative for chemistry but remained largely aspirational until recently.

## Key Finding

**Opus 4.7 is competitive with professional chemistry software** (ChemDraw, MestReNova) on NMR analysis tasks:

### Hydrogen NMR (¹H)
- **Opus 4.7 average error**: ±0.079 ppm (well under half the tolerance window)
- **Highest share** of peaks landing inside tolerance vs. alternatives
- Evaluated across 3 runs per compound with averaging

### Carbon NMR (¹³C)
- **Opus 4.7 and MestReNova** performed comparably
- ChemDraw showed wider gap

### Peak Shape & Coupling
- Opus 4.7 less accurate on predicting peak shapes and coupling distances
- These features are also harder for human chemists

### Structure Elucidation (1D Inverse)
- **8 simpler structures**: 100% recovery rate from spectra + formula
- **7 harder targets**: Correct structure recovered on all attempts (with starting-material hint)
- General-purpose LLM makes 1D inverse elucidation tractable

## Methodology

### 1. Multi-Tool Comparison Framework
- Query LLM 3 times per compound, average results (accounts for output variance)
- Compare against deterministic tools (ChemDraw, MestReNova run once each)
- Use ppm tolerance windows for peak position validation

### 2. Task Decomposition
- **Peak position prediction**: Chemical shift values in ppm
- **Peak shape prediction**: Multiplicity (singlet, doublet, etc.)
- **Coupling constant prediction**: Peak separation distances
- **Structure elucidation**: Given NMR + formula, deduce molecular structure

### 3. Benchmarking Protocol
- Test across diverse scaffold classes (20-30 recommended)
- Minimum 15 compounds per class for within-class variance separation
- Separate easy vs. hard targets (with/without starting material hints)

## Chemistry Bottlenecks Identified

Anthropic identified key bottlenecks that slow chemists:
1. **Representation translation**: Converting between SMILES, structures, spectra
2. **Spectral analysis**: Interpreting NMR, IR, MS data
3. **Retrosynthesis planning**: Planning synthetic routes (still being scoped)
4. **Instrument readout reconciliation**: Matching experimental data to proposed products
5. **Database querying**: Finding compounds in the right notation

## Architecture Pattern for AI Chemistry Tools

```
Input (SMILES/Spectrum/Image) → Multimodal LLM → Chemical Reasoning → Output (Structure/Analysis)
                                    ↑
                    Chemistry-specific prompt engineering
                    + domain knowledge injection
```

### Implementation Guidelines

1. **Use multimodal models**: Must read chemical structures from images
2. **Multi-run averaging**: LLM output varies; average 3+ runs for reliability
3. **Tolerance-based validation**: Use chemistry-specific ppm tolerances, not exact matches
4. **Task-specific prompting**: Separate peak prediction from structure elucidation prompts
5. **Hint provision**: Starting material hints significantly improve hard-target performance

## Limitations

- Assessment covers limited scaffold diversity; broader validation needed
- Peak shape prediction remains a gap
- Retrosynthesis capability not yet benchmarked
- No evaluation of reaction condition prediction
- Single-compound analysis only (no mixture analysis)

## Activation Triggers

Use when:
- Evaluating LLM capability for chemistry tasks
- Building AI-assisted NMR analysis tools
- Benchmarking molecular structure elucidation systems
- Designing chemistry-specific AI agent workflows
- Comparing AI vs. traditional chemistry software accuracy

## Key Metrics

| Task | Opus 4.7 | ChemDraw | MestReNova |
|------|----------|----------|------------|
| ¹H NMR error | ±0.079 ppm | ~0.16 ppm | ~0.09 ppm |
| ¹³C NMR error | Comparable | - | Comparable |
| Simple structure recovery | 100% (8/8) | - | - |
| Hard structure recovery | 100% (7/7, with hint) | - | - |

## Key References

- Original article: https://www.anthropic.com/research/making-claude-a-chemist
- ChemDraw: https://revvitysignals.com/products/informatics/chemdraw
- MestReNova: https://mestrelab.com/software/mestrenova/

## Pitfalls

- **Single-run evaluation**: LLM variance makes single-run results unreliable
- **Exact match validation**: Chemistry requires tolerance-based comparison
- **Ignoring scaffold diversity**: Performance varies significantly across molecule classes
- **Overgeneralizing from NMR**: NMR is one of many chemistry tasks; retrosynthesis, synthesis planning are separate challenges
