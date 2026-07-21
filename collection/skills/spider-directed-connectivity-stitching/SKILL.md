---
name: spider-directed-connectivity-stitching
description: "SPIDER: Non-parametric frequency-domain framework for recovering directed brain connectivity from incomplete asynchronous recordings. Stitches power-spectra across sessions. Activation: effective connectivity, directed information flow, SPIDER, brain connectivity stitching, 脑连接拼接, 有效连接"
tags: [neuroscience, brain-networks, effective-connectivity, frequency-domain, multi-session]
---

# SPIDER: Stitched Power-spectra for Inferring Directed Information Flow

**arXiv**: 2606.22695  
**Authors**: Yisi S. Zhang, Daniel Y. Takahashi  
**Date**: 2026-06-21 (updated 2026-07-04)

## Core Methodology

### Problem Statement
Mapping directed information flow (effective connectivity) between brain regions is central to understanding brain function, but large-scale recordings sample only a fraction of the brain at a time. Sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established methods (Granger causality, DCM, PDC) require all regions recorded simultaneously with a common clock.

### Key Innovation
**SPIDER** (Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings):
- **Non-parametric, frequency-domain framework**
- Stitches local power-spectral estimates from overlapping channel subsets into a global spectral matrix
- Obtains frequency-resolved directed interactions via canonical spectral factorization and PDC
- **No temporal alignment required**
- Nuclear-norm completion fills in never-co-observed region pairs

### Technical Pipeline
1. **Local spectral estimation**: compute power-spectra from overlapping channel subsets
2. **Stitching**: assemble global spectral matrix from local estimates
3. **Completion**: nuclear-norm completion for unobserved region pairs
4. **Factorization**: canonical spectral factorization
5. **Direction inference**: Partial Directed Coherence (PDC)

## Mathematical Framework

### Spectral Matrix Stitching
```
S_global(f) = stitch({S_local^(i)(f)})
```
where each S_local^(i) comes from overlapping channel subset i.

### Nuclear-Norm Completion
For never-co-observed region pairs:
```
min ||S||_* subject to S_observed = S_global_observed
```

### Directed Connectivity via PDC
From spectral matrix factorization:
```
PDC_{i→j}(f) = |A_{ij}(f)|² / Σ_k |A_{kj}(f)|²
```
where A(f) is the transfer function from spectral factorization.

## Experimental Results

### Validation Datasets
1. **Simulations**: ground-truth directed connectivity
2. **Two-photon calcium imaging**: mouse brain
3. **IBL Neuropixels dataset**: 50 brain areas from 43 sessions across 12 laboratories (never recorded together)
4. **Human intracranial EEG**: 43 patients with non-overlapping coverage

### Key Findings
- **Brain-wide spontaneous flow is largely recurrent**
- **Theta band**: significant feedforward hierarchy with hippocampal formation at source
- **Cross-species consistency**: same theta-band hierarchy recovered in mouse and human
- **Cross-modality consistency**: calcium imaging and electrophysiology agree

### Scale Achievement
- Recovered directed flow among **50 areas** from **43 sessions** in **12 laboratories**
- Previously impossible with traditional methods

## Practical Applications

### For Brain Network Analysis
1. **Multi-session connectivity**: combine data across experimental sessions
2. **Cross-laboratory integration**: merge datasets from different labs
3. **Cross-species comparison**: compare connectivity patterns across species
4. **Large-scale brain mapping**: whole-brain effective connectivity from partial observations

### Implementation Guidelines

#### When to Use
- Multiple recording sessions with overlapping but incomplete coverage
- Cross-laboratory data integration
- Cross-species connectivity comparison
- Scenarios where simultaneous whole-brain recording is impossible

#### Requirements
- Overlapping channel subsets across sessions
- Frequency-domain data (power spectra)
- Sufficient overlap for stitching

### Pitfalls
- Requires overlapping channels between sessions
- Nuclear-norm completion assumes low-rank structure
- Frequency resolution affects temporal precision
- Validation requires ground-truth or strong assumptions

## Algorithm Steps

### Step 1: Local Spectral Estimation
```python
for session in sessions:
    S_local[session] = compute_power_spectrum(data[session])
```

### Step 2: Stitching
```python
S_global = stitch_local_spectra(S_local_list, overlap_info)
```

### Step 3: Completion
```python
S_completed = nuclear_norm_completion(S_global, observed_mask)
```

### Step 4: Factorization & PDC
```python
A = spectral_factorization(S_completed)
PDC = compute_pdc(A)
```

## Comparison with Traditional Methods

| Method | Requires Simultaneous Recording | Temporal Alignment | Handles Incomplete Data |
|--------|--------------------------------|-------------------|------------------------|
| Granger Causality | Yes | Yes | No |
| DCM | Yes | Yes | No |
| PDC | Yes | Yes | No |
| **SPIDER** | **No** | **No** | **Yes** |

## Related Concepts
- Effective connectivity
- Granger causality
- Dynamic causal modeling (DCM)
- Partial directed coherence (PDC)
- Spectral factorization
- Nuclear norm minimization
- Multi-session data integration

## References
- Paper: https://arxiv.org/abs/2606.22695
- PDF: https://arxiv.org/pdf/2606.22695
