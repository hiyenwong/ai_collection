---
name: spider-directed-connectivity
description: "SPIDER: non-parametric frequency-domain framework for inferring directed effective connectivity from incomplete, asynchronous recordings via stitched power-spectra and spectral factorization."
activation: effective connectivity, directed information flow, SPIDER, asynchronous recordings, spectral factorization, Granger causality alternative
tags: [neuroscience, effective-connectivity, signal-processing, spectral-methods]
arxiv_id: "2606.22695"
authors: ["Yisi S. Zhang", "Daniel Y. Takahashi"]
---

# SPIDER: Stitched Power-spectra for Directed Information Flow

## Problem
Established directed-connectivity methods (Granger causality, DCM, PDC) require **simultaneous recordings** of all regions with a **common clock**. Real-world neuroscience data is fragmented: different sessions, animals, and labs sample partially overlapping brain regions without shared temporal reference.

## Core Methodology

### Non-parametric Frequency-Domain Framework
1. **Stitching local power-spectra**: Combine spectral estimates from overlapping channel subsets into a global spectral matrix
2. **Canonical spectral factorization**: Decompose global spectral matrix to recover directed interactions
3. **PDC extraction**: Derive frequency-resolved directed interactions without temporal alignment
4. **Nuclear-norm completion**: Fill in never-co-observed region pairs via matrix completion

### Key Innovation
- **No temporal alignment required**: Works across asynchronous recordings
- **Handles missing data**: Nuclear-norm completion infers unobserved pairwise interactions
- **Frequency-resolved**: Preserves spectral specificity of directed interactions

## Activation Triggers
- "effective connectivity from incomplete data"
- "asynchronous neural recordings"
- "directed information flow without common clock"
- "Granger causality alternative for fragmented data"
- "spectral factorization connectivity"

## Related Methods
- Granger causality (requires simultaneous recordings)
- Dynamic causal modeling (DCM)
- Partial directed coherence (PDC)
- Transfer entropy

## Use Cases
- Cross-session/connectivity studies
- Multi-lab data integration
- Large-scale brain mapping with sparse sampling
- Developmental neuroscience (changing electrode placements)

## Reference
Zhang, Y. S., & Takahashi, D. Y. (2026). SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings. arXiv:2606.22695