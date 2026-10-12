---
name: v1-feedback-eccentricity-magnification
description: Use when analyzing feedback-to-V1 anatomy, eccentricity-dependent projection ratios, or testing central-peripheral dichotomy predictions. Marmoset retrograde tracing methodology.
category: neuroscience
---

# V1 Feedback Eccentricity Magnification (Central-Peripheral Dichotomy Anatomical Test)

**Source**: Majka, Cho, Łabuszewska, Nguyen, Syc, Walkiewicz, Worthy, Zhaoping, Rosa. "Feedback to the primary visual cortex is highly concentrated on the central visual field representation." arXiv:2610.09983 (Oct 2026). Nencki Institute + Monash + Tübingen/MPI.

## Core Insight

The first direct anatomical evidence for the Central-Peripheral Dichotomy (CPD) theory's key prediction: feedback projections to primate V1 are power-law concentrated on the central visual field representation, while the classical "uniform V1 surface" view (cell densities, column sizes, LGN innervation approximately constant across V1) fails for the feedback circuit specifically. Retrograde tracer injections (12 V1 sites, 6 marmosets, E 2°–18°) show the feedback-to-feedforward ratio drops ~10× over that eccentricity range.

## Methodology

### 1. Normalized feedback measure (tracer-normalization)

Raw counts of retrogradely labeled neurons vary with injection spread/uptake chemistry. Normalize per source region:

```
N̂_region(E) = N_region(E) / N_LGN(E)
```

- N_region(E): labeled neurons in a source area (V2, ventral-stream pool, dorsal-stream pool) projecting to V1 injection at eccentricity E
- N_LGN(E): labeled LGN neurons (feedforward source) for the same injection
- Both numerator and denominator scale with tracer spread/uptake → ratio cancels injection-specific factors
- This ratio IS the feedback magnification factor M_feedback(E): feedback neurons per feedforward neuron

### 2. Power-law fits (the quantitative result)

Fit log(N̂) vs log(E): N̂(E) ≈ const · E^(−α)

| Feedback source | α (95% CI) | Interpretation |
|---|---|---|
| V2 → V1 | 1.5 (0.86, 2.1) | recognition-support feedback, steep central focus |
| Ventral stream pool → V1 | 1.6 (1.1, 2.1) | "what" stream dominates central-field feedback |
| Dorsal stream pool → V1 | 0.6 (0.13, 1.15) | weaker central concentration — "where"/gaze guidance present everywhere |
| N_ventral/N_dorsal ratio | 0.96 (0.26, 1.7) | ventral dominance flips with eccentricity: central field fed mainly by ventral, peripheral by dorsal |
| Non-visual cortex pool | α ≈ 0 | flat — no eccentricity trend (negative control) |

### 3. Combined magnification chain (why 10× becomes 1000×)

```
N_feedback(E) = M_feedback(E) · M_retina→V1(E) · d(E)
```

The feedback magnification MULTIPLIES the classical cortical magnification. If M_feedback(E1)/M_feedback(E2) = 10 and M_retina→V1(E1)/M_retina→V1(E2) = 100, then feedback neurons per square degree differ by ~1000× (LGN innervation density d is approximately uniform). Central-field feedback advantage is an order of magnitude beyond what cortical magnification alone predicts.

## Implementation Guidance

- **Data source**: marmosetbrain.org (Marmoset Brain Architecture Project) — unfolded cortex maps, per-injection labeled-neuron data public.
- **Tracer protocol**: cellular-resolution retrograde tracers injected at known retinotopic V1 sites; presynaptic uptake → monosynaptic projection labeling; count labeled somata per source region in flat maps.
- **Statistical treatment**: linear fit of log N̂ vs log E with 95% CI on slope α; power-law model validated across 12 injections spanning 2°–18°.
- **Reuse pattern for other systems**: whenever raw projection counts vary with injection efficacy, normalize by a feedforward benchmark source measured in the SAME injection (here LGN). This converts confounded absolute counts into a robust ratio index.

## Pitfalls

- **Do not read absolute counts across injections** — only within-injection ratios are comparable.
- **α for dorsal stream (0.6) has CI touching 0.13** — the ventral/dorsal asymmetry claim rests on non-overlapping CIs (1.1–2.1 vs 0.13–1.15); the weaker dorsal trend is real but noisy.
- **Extrapolation beyond 2°–18° untested** — foveal (<2°) and far-peripheral (>18°) regimes not sampled.
- **CPD is a theory, this is one prediction confirmed** — feedback concentration supports the recognition-query hypothesis, but "feedback = disambiguation query" remains a computational interpretation, not an anatomical fact.
- **Non-visual feedback flat (α≈0)** — parahippocampal/auditory/retrosplenial inputs do not follow the trend; don't pool them with visual feedback.

## Applications & Extensions

- Brain-inspired architectures: allocate top-down/recurrent connectivity with a central-field bias (α≈1.5–1.6 power law) rather than uniformly — foveated transformers / attention architectures get an anatomically-grounded connectivity prior.
- The central-peripheral dichotomy as an organizational axis COMPLEMENTING the classical feedforward hierarchy — two-axis view of visual cortex (hierarchical × central-peripheral).
- Explains peripheral-only visual illusions (reversed depth, flip tilt): visible peripherally because feedback query is absent there; appear centrally under backward masking that disrupts feedback.
- Cross-species test template: replicate tracer-ratio analysis in macaque/human post-mortem tracing data to test CPD generality.
- Related prior support: central bias in frontal↔V1 functional connectivity; Granger-inferred V4→V1 feedback foveal focus — this work upgrades those indirect signals to direct anatomy.

## arXiv Metadata

- **ID**: 2610.09983
- **Date**: 2026-10-07
- **Categories**: q-bio.NC
- **Authors**: Piotr Majka, Emmanuel K L Cho, Karolina Łabuszewska, Thuy Vy Nguyen, Marcin Syc, Tomasz Walkiewicz, Katrina H Worthy, Li Zhaoping, Marcello Rosa
