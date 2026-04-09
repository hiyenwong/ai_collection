# SKILL.md - Spectral DCM Brain Connectivity Genetics

## Activation Keywords

- spectral DCM, dynamic causal modelling, resting-state fMRI
- effective connectivity, default mode network, DMN
- imaging genetics, SNP, Alzheimer's disease
- brain connectivity genetics, longitudinal fMRI

## What It Does

Provides a framework for relating effective brain connectivity (estimated via spectral Dynamic Causal Modelling) to genetic variants (SNPs) using longitudinal resting-state fMRI data. Applied to Alzheimer's disease and mild cognitive impairment research.

## When To Use

**Use this skill when:**
- Analyzing effective connectivity with DCM
- Relating brain connectivity to genetics
- Longitudinal resting-state fMRI analysis
- Alzheimer's disease / MCI research
- Imaging genetics studies

**Do NOT use for:**
- Functional connectivity only (no causal modelling)
- Cross-sectional analysis (no longitudinal data)
- Non-genetic studies

## How To Use

### Step-by-Step Workflow

1. **Collect Longitudinal rs-fMRI and Genetic Data**
   - Multiple timepoints per subject
   - Genetic data (SNPs, GWAS)
   - Example: ADNI database

2. **Define Brain Network (DMN)**
   - Select regions (4-region or 6-region DMN)
   - Extract time series from ROIs

3. **Apply Spectral DCM**
   - Fit DCM to rs-fMRI data
   - Estimate effective connectivity matrices
   - Cross-spectral density modelling

4. **Extract SNP Data**
   - Disease-constrained SNP set
   - Quality control and imputation

5. **Statistical Analysis**
   - Linear mixed effects (LME) models
   - Function-on-scalar regression (FSR)
   - Parametric bootstrap for significance

### Spectral DCM Overview

Spectral DCM models resting-state fMRI as:
- Neuronal dynamics: dz/dt = Az + Cu
- Hemodynamic forward model
- Cross-spectral density estimation

**Output:** Effective connectivity matrix A (directed)

### Key Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Network size | Number of regions | 4-6 (DMN) |
| Timepoints | Visits per subject | 2-4 |
| SNPs | Genetic variants | Disease-constrained set |

## Example Usage

### Longitudinal DCM Analysis

**Problem:** Relate DMN connectivity to Alzheimer's risk SNPs

**Pipeline:**
```python
import numpy as np
from statsmodels.regression.mixed_linear_model import MixedLM

class SpectralDCMGenetics:
    def __init__(self, n_regions, n_timepoints):
        self.n_regions = n_regions
        self.n_timepoints = n_timepoints
    
    def fit_dcm_longitudinal(self, fmri_data, subject_ids):
        """
        Fit spectral DCM to longitudinal rs-fMRI
        
        Parameters:
        -----------
        fmri_data : list of arrays
            ROI time series for each scan
        subject_ids : array
            Subject identifier for each scan
            
        Returns:
        --------
        connectivity_matrices : array (n_scans, n_regions, n_regions)
            Estimated effective connectivity
        """
        # In practice, use SPM or DCM toolbox
        # This is a simplified placeholder
        n_scans = len(fmri_data)
        connectivity = np.zeros((n_scans, self.n_regions, self.n_regions))
        
        for i, timeseries in enumerate(fmri_data):
            # Spectral DCM estimation
            connectivity[i] = self._estimate_dcm(timeseries)
        
        return connectivity
    
    def relate_to_snps(self, connectivity, snp_data, subject_ids, timepoints):
        """
        Relate effective connectivity to SNPs using LME
        
        Parameters:
        -----------
        connectivity : array (n_scans, n_regions, n_regions)
            Effective connectivity matrices
        snp_data : array (n_subjects, n_snps)
            SNP values (0, 1, 2)
        subject_ids : array (n_scans,)
            Subject identifier
        timepoints : array (n_scans,)
            Time since baseline
        """
        n_scans, n_regions, _ = connectivity.shape
        n_snps = snp_data.shape[1]
        
        results = {}
        
        for snp_idx in range(n_snps):
            # Flatten connectivity to vector
            conn_vector = connectivity.reshape(n_scans, -1)
            
            # LME model
            # conn_ij = β₀ + β₁*SNP + β₂*time + u_subject + ε
            for conn_idx in range(conn_vector.shape[1]):
                y = conn_vector[:, conn_idx]
                x = np.column_stack([
                    np.ones(n_scans),
                    snp_data[subject_ids, snp_idx],
                    timepoints
                ])
                
                model = MixedLM(y, x, subject_ids)
                result = model.fit()
                
                key = f"SNP_{snp_idx}_conn_{conn_idx}"
                results[key] = {
                    'beta_snp': result.params[1],
                    'p_value': result.pvalues[1]
                }
        
        return results
    
    def function_on_scalar_regression(self, connectivity, snp_data):
        """
        Function-on-scalar regression for connectivity-SNP analysis
        """
        from scipy import stats
        
        # Treat connectivity matrices as functional responses
        # SNP as scalar predictor
        
        n_scans = connectivity.shape[0]
        conn_flat = connectivity.reshape(n_scans, -1)
        
        # Fit regression for each connectivity element
        betas = []
        p_values = []
        
        for i in range(conn_flat.shape[1]):
            slope, intercept, r, p, se = stats.linregress(
                snp_data, conn_flat[:, i]
            )
            betas.append(slope)
            p_values.append(p)
        
        return np.array(betas), np.array(p_values)
```

### Parametric Bootstrap for Significance

**Analysis:**
```python
def bootstrap_snp_test(connectivity, snp_data, n_bootstrap=1000):
    """
    Parametric bootstrap for SNP coefficient testing
    """
    observed_beta = compute_snp_effect(connectivity, snp_data)
    
    # Generate null distribution
    null_betas = []
    for _ in range(n_bootstrap):
        # Shuffle SNP data
        shuffled_snp = np.random.permutation(snp_data)
        null_beta = compute_snp_effect(connectivity, shuffled_snp)
        null_betas.append(null_beta)
    
    null_betas = np.array(null_betas)
    
    # Compute p-value
    p_value = np.mean(np.abs(null_betas) >= np.abs(observed_beta))
    
    return observed_beta, p_value
```

## Application: ADNI Study

**Data:**
- 111 subjects, 319 rs-fMRI scans
- Longitudinal: 2-4 visits per subject
- 4-region and 6-region DMN networks
- Disease-constrained SNP set from 663 ADNI subjects

**Findings:**
- Effective connectivity changes with disease progression
- SNP associations with DMN connectivity
- Implications for AD genetics

## Related Skills

- **ccep-causal-brain-network** - Causal connectivity
- **time-varying-brain-connectivity** - Dynamic connectivity
- **task-aware-brain-connectivity** - Task-based connectivity

## Source

- arXiv:1901.09975v8
- Title: Spectral Dynamic Causal Modelling of Resting-State fMRI: Relating Effective Brain Connectivity in the Default Mode Network to Genetics
- Utility: 0.87
- Authors: Yunlong Nie, Eugene Opoku, et al.
- Data: ADNI database

## Notes

- Key innovation: Spectral DCM + imaging genetics
- Longitudinal analysis of effective connectivity
- Linear mixed effects and function-on-scalar regression
- Applications: Alzheimer's disease, MCI research
- Parametric bootstrap for significance testing
- 4-region and 6-region DMN networks

---

_Created: 2026-04-01_