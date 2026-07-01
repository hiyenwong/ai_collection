---
name: spider-directed-connectivity
title: "SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings"
description: "Non-parametric frequency-domain framework for recovering directed brain connectivity from incomplete, asynchronous multi-session recordings without requiring simultaneous whole-brain measurement"
arxiv_id: "2606.22695"
authors: "Yisi S. Zhang, Daniel Y. Takahashi"
date: "2026-06-21"
categories: ["q-bio.NC", "stat.ME"]
trigger_words: ["effective connectivity", "directed information flow", "asynchronous recordings", "power spectral", "PDC", "spectral factorization", "nuclear norm completion", "brain-wide connectivity"]
---

# SPIDER: Directed Connectivity from Incomplete Asynchronous Recordings

## Summary

SPIDER is a non-parametric, frequency-domain framework that recovers directed information flow (effective connectivity) from incomplete, asynchronous brain recordings — where different sessions, animals, or laboratories cover partially overlapping brain regions without a shared temporal reference.

## Core Innovation

Traditional directed-connectivity methods (Granger causality, DCM, PDC) require **all regions recorded simultaneously with a common clock**. SPIDER breaks this constraint by:

1. **Spectral Stitching**: Stitches local power-spectral estimates from overlapping channel subsets into a global spectral matrix — no temporal alignment needed
2. **Canonical Spectral Factorization**: Obtains frequency-resolved directed interactions via PDC from the stitched spectral matrix
3. **Nuclear-Norm Completion**: Fills in never-co-observed region pairs using low-rank matrix completion

## Methodology

### Pipeline
```
Local Power Spectra (overlapping subsets)
    → Spectral Matrix Stitching
    → Nuclear-Norm Completion (unobserved pairs)
    → Canonical Spectral Factorization
    → Partial Directed Coherence (PDC)
    → Frequency-resolved Directed Connectivity
```

### Key Technical Components
- **Non-parametric**: No model assumptions about network dynamics
- **Frequency-resolved**: Captures direction-specific interactions per frequency band
- **Consistency guarantees**: Mathematically proven convergence properties
- **Cross-session**: Works across sessions, animals, and laboratories

## Validation

- **Simulations**: Validated on synthetic data with known ground truth
- **Two-photon calcium imaging**: Successfully recovered known connectivity
- **IBL Neuropixels dataset**: Recovered directed flow among **50 brain areas from 43 sessions in 12 laboratories** never recorded together
- **Human iEEG**: Applied to resting human intracranial EEG (43 patients, non-overlapping coverage)

## Key Findings

1. **Brain-wide spontaneous flow is largely recurrent** — confirming known recurrent dynamics
2. **Theta-band feedforward hierarchy**: In theta band, a significant feedforward hierarchy emerges with **hippocampal formation at its source**
3. **Cross-species conservation**: The same theta-band hierarchy is recovered across species (mouse → human) and modality (calcium imaging → iEEG)

## Implementation Considerations

### When to Use
- Multi-session datasets with partial region overlap
- Cross-laboratory data integration
- Meta-analysis of brain connectivity across studies
- When simultaneous whole-brain recording is impossible

### Requirements
- Overlapping channel subsets across sessions (for stitching)
- Sufficient sessions to cover target regions
- Stationarity assumption within each recording session

### Limitations
- Requires some overlap between sessions for stitching
- Nuclear-norm completion assumes low-rank structure in connectivity
- Does not capture time-varying connectivity within sessions

## Applications

1. **Large-scale brain mapping**: Integrate data from distributed labs
2. **Cross-species comparison**: Align connectivity across species
3. **Clinical neuroscience**: Combine patient data with non-overlapping coverage
4. **Meta-analysis**: Systematic integration of published connectivity studies

## References

- Paper: https://arxiv.org/abs/2606.22695
- Category: q-bio.NC, stat.ME
