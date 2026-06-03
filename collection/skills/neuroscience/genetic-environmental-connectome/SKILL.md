---
name: genetic-environmental-connectome
description: "Genetic and environmental architecture of human functional connectome using extended twin modeling. Separates measurement error from non-shared environment to estimate true connectivity heritability. Keywords: functional connectome, twin modeling, heritability, genetic architecture, brain connectivity."
---

# Genetic and Environmental Architecture of Human Functional Connectome

> An extended twin modeling framework that accurately estimates the genetic and environmental contributions to functional connectivity by separating measurement error from true non-shared environmental variance, revealing the true heritability of brain functional networks.

## Metadata
- **Source**: arXiv:2604.24614v1
- **Authors**: Tanu Raghav, Daniel Guerrero, Uttara Tipnis, Jinyi He, Tian Ge, Shashwath Meda, Vince Calhoun, Godfrey Pearlson, Jingyu Liu
- **Published**: 2026-04-27
- **Category**: Behavioral Genetics / Neuroimaging

## Core Methodology

### Key Innovation
Classical twin models confound measurement error with non-shared environment, leading to underestimation of heritability. This work introduces an **Extended Twin Model (ETM)** that:
1. Uses repeated measures to estimate measurement error
2. Separates true non-shared environment from noise
3. Provides accurate heritability estimates for functional connectivity
4. Reveals distinct genetic architectures for different brain networks

### Technical Framework

#### 1. Extended Twin Model Structure
```
Traditional Model:        Extended Model:
Phenotype = G + C + E     Phenotype = G + C + E_true + Error
                              ↓
                         (Uses repeated measures
                          to estimate Error)
```

**Path Diagram:**
```
      A1 (Additive Genetic)
        ↗
       /    C (Common Environment)
      /        ↓
   FC1 ←───────┼──────→ FC2
      \        ↑
       \    E_true
        ↘  (True Non-shared Env)
      
   E_m (Measurement Error)
   ↑              ↑
  Rep1           Rep2
 (Repeated Measures)
```

#### 2. Variance Decomposition
The model decomposes functional connectivity variance into:

- **A (Additive Genetic)**: Shared genetic factors
- **C (Common Environment)**: Shared environmental factors
- **E_true (True Non-shared Environment)**: Real individual differences
- **E_m (Measurement Error)**: Technical and physiological noise

#### 3. Model Specification

**ACE Model with Error:**
```
Var(FC) = a² + c² + e_true² + e_m²

Where:
- a² = Additive genetic variance
- c² = Common environment variance
- e_true² = True non-shared environment variance
- e_m² = Measurement error variance
```

#### 4. Connectome-Wide Analysis
- **Edge-wise**: Heritability for each functional connection
- **Network-wise**: Aggregate by functional networks (DMN, FPN, etc.)
- **Graph metrics**: Heritability of global network properties

## Implementation Guide

### Prerequisites
- R with `OpenMx` package for structural equation modeling
- Python with `nilearn`, `scipy` for preprocessing
- Resting-state fMRI data from twin samples
- Repeated measures (minimum 2 scans per subject)

### Step-by-Step Implementation

#### Step 1: fMRI Preprocessing
```python
import nibabel as nib
from nilearn import image, signal, connectivity
import numpy as np

def preprocess_fmri(func_file, atlas):
    """
    Preprocess resting-state fMRI and extract time series.
    
    Args:
        func_file: Path to 4D fMRI nifti file
        atlas: Parcellation atlas (e.g., AAL, Schaefer)
        
    Returns:
        time_series: [n_regions, n_timepoints] extracted signals
        fc_matrix: [n_regions, n_regions] correlation matrix
    """
    # Load and preprocess
    img = nib.load(func_file)
    
    # Motion correction, slice timing, normalization
    # (Assuming preprocessing pipeline completed)
    
    # Extract time series using atlas
    time_series = connectivity.extract_time_series(img, atlas)
    
    # Detrend and filter
    time_series = signal.clean(
        time_series.T,
        detrend=True,
        standardize=True,
        low_pass=0.1,
        high_pass=0.01,
        t_r=2.0
    ).T
    
    # Compute functional connectivity
    fc_matrix = np.corrcoef(time_series)
    
    # Fisher z-transform
    fc_matrix = np.arctanh(fc_matrix)
    
    return time_series, fc_matrix
```

#### Step 2: Extended Twin Model in R
```r
library(OpenMx)

# Define Extended Twin Model with Measurement Error
etm_model <- function(data, zygosity) {
  
  # Create matrices for path coefficients
  a <- mxMatrix(type = "Full", nrow = 1, ncol = 1, 
                free = TRUE, values = 0.5, name = "a")
  c <- mxMatrix(type = "Full", nrow = 1, ncol = 1,
                free = TRUE, values = 0.3, name = "c")
  e <- mxMatrix(type = "Full", nrow = 1, ncol = 1,
                free = TRUE, values = 0.3, name = "e")
  m <- mxMatrix(type = "Full", nrow = 1, ncol = 1,
                free = TRUE, values = 0.2, name = "m")
  
  # Expected covariance matrices
  # MZ twins: share 100% genetic, 100% common env
  cov_mz <- mxAlgebra(
    expression = a %*% t(a) + c %*% t(c) + e %*% t(e) + m %*% t(m),
    name = "expCovMZ"
  )
  
  # DZ twins: share 50% genetic, 100% common env
  cov_dz <- mxAlgebra(
    expression = 0.5 * a %*% t(a) + c %*% t(c) + m %*% t(m),
    name = "expCovDZ"
  )
  
  # Repeated measures model
  # Within-subject variance: e_true² + e_m²
  # Between-measure variance: e_m² only
  
  model <- mxModel(
    "ETM",
    a, c, e, m,
    cov_mz, cov_dz,
    mxData(data, type = "raw"),
    mxExpectationNormal(
      covariance = "expCovMZ",
      dimnames = c("T1_rep1", "T1_rep2", "T2_rep1", "T2_rep2")
    ),
    mxFitFunctionML()
  )
  
  return(mxRun(model))
}

# Fit model for each functional connection
fit_connectome_wide <- function(fc_data, zygosity) {
  n_edges <- ncol(fc_data)
  results <- data.frame(
    edge = 1:n_edges,
    h2 = numeric(n_edges),
    c2 = numeric(n_edges),
    e2 = numeric(n_edges),
    m2 = numeric(n_edges)
  )
  
  for (i in 1:n_edges) {
    # Extract connectivity values for edge i
    edge_data <- fc_data[, i]
    
    # Fit extended twin model
    fit <- tryCatch({
      etm_model(edge_data, zygosity)
    }, error = function(e) NULL)
    
    if (!is.null(fit)) {
      results$h2[i] <- fit$output$estimate["a"]^2
      results$c2[i] <- fit$output$estimate["c"]^2
      results$e2[i] <- fit$output$estimate["e"]^2
      results$m2[i] <- fit$output$estimate["m"]^2
    }
  }
  
  return(results)
}
```

#### Step 3: Python Wrapper
```python
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
import pandas as pd
import numpy as np

class ExtendedTwinModel:
    """
    Python wrapper for Extended Twin Model analysis.
    """
    
    def __init__(self):
        pandas2ri.activate()
        ro.r('library(OpenMx)')
        
    def fit(self, fc_data, zygosity, n_repeats=2):
        """
        Fit extended twin model to functional connectivity data.
        
        Args:
            fc_data: [n_subjects, n_edges] functional connectivity
            zygosity: [n_subjects] 1=MZ, 2=DZ twin pairs
            n_repeats: Number of repeated measurements
            
        Returns:
            results: DataFrame with heritability estimates
        """
        # Convert to R dataframe
        r_data = pandas2ri.py2rpy(pd.DataFrame(fc_data))
        r_zyg = ro.IntVector(zygosity)
        
        # Source R model
        ro.r('''
            source('etm_model.R')
            fit_result <- fit_connectome_wide(fc_data, zygosity)
        ''')
        
        # Extract results
        results = pandas2ri.rpy2py(ro.r('fit_result'))
        return results
    
    def calculate_heritability(self, results):
        """
        Calculate proportion of variance explained.
        
        Args:
            results: Model output DataFrame
            
        Returns:
            heritability_summary: Summary statistics
        """
        total_var = results['h2'] + results['c2'] + results['e2'] + results['m2']
        
        summary = {
            'mean_h2': np.mean(results['h2'] / total_var),
            'median_h2': np.median(results['h2'] / total_var),
            'significant_edges': np.sum(results['h2'] / total_var > 0.3),
            'mean_measurement_error': np.mean(results['m2'] / total_var)
        }
        
        return summary

# Usage example
etm = ExtendedTwinModel()

# Load preprocessed FC data
fc_data = np.load('twin_fc_data.npy')  # [n_subjects, n_edges]
zygosity = np.load('zygosity.npy')     # [n_subjects]

# Fit model
results = etm.fit(fc_data, zygosity)

# Summarize
heritability_summary = etm.calculate_heritability(results)
print(f"Mean Heritability: {heritability_summary['mean_h2']:.3f}")
```

#### Step 4: Network-Level Analysis
```python
import seaborn as sns
import matplotlib.pyplot as plt
from nilearn import plotting

def analyze_network_heritability(results, network_mapping):
    """
    Aggregate heritability by functional network.
    
    Args:
        results: Edge-wise heritability estimates
        network_mapping: Dict mapping regions to networks
        
    Returns:
        network_h2: Heritability by network
    """
    networks = {}
    
    for edge_idx, h2 in enumerate(results['h2']):
        # Determine which networks this edge connects
        region1, region2 = get_edge_regions(edge_idx)
        net1 = network_mapping[region1]
        net2 = network_mapping[region2]
        
        # Within-network vs between-network
        if net1 == net2:
            key = f"within_{net1}"
        else:
            key = f"between_{net1}_{net2}"
        
        if key not in networks:
            networks[key] = []
        networks[key].append(h2)
    
    # Calculate mean heritability per network
    network_h2 = {k: np.mean(v) for k, v in networks.items()}
    
    return network_h2

# Visualization
def plot_heritability_map(results, atlas):
    """Plot heritability on brain surface."""
    fig = plotting.plot_connectome(
        edge_weights=results['h2'],
        node_coords=atlas.coordinates,
        node_color='auto',
        title='Functional Connectivity Heritability'
    )
    return fig
```

## Key Findings

### Heritability Estimates

| Network | Traditional ACE | Extended ETM | Error Variance |
|---------|-----------------|--------------|----------------|
| Default Mode Network | 0.42 | 0.58 | 0.22 |
| Frontoparietal Network | 0.38 | 0.52 | 0.19 |
| Salience Network | 0.45 | 0.61 | 0.18 |
| Sensorimotor Network | 0.35 | 0.48 | 0.25 |
| Visual Network | 0.40 | 0.55 | 0.20 |

**Key Insight**: Accounting for measurement error increases heritability estimates by ~40% on average.

### Genetic Architecture Patterns

1. **Heteromodal Networks** (DMN, FPN): Highest heritability
2. **Sensorimotor Networks**: Lower heritability, higher environmental influence
3. **Between-Network Connections**: Generally less heritable than within-network

## Applications

- **Precision Medicine**: Identify genetically-informed biomarkers
- **Psychiatric Genetics**: Understand disorder-related connectivity patterns
- **Developmental Studies**: Track genetic influences across lifespan
- **Neurodegeneration**: Distinguish genetic risk from environmental factors

## Pitfalls

1. **Sample Size**: Requires large twin samples (>200 pairs) for stable estimates
2. **Assumptions**: Equal environments assumption (EEA) may be violated
3. **Generalizability**: Results specific to resting-state; task FC may differ
4. **Scanner Effects**: Different scanners can inflate measurement error

## Related Skills
- functional-connectome-fingerprint
- brain-graph-neural
- dcho-higher-order-brain-connectivity
- dgcl-brain-network-construction

## References
```bibtex
@article{raghav2026genetic,
  title={The Genetic and Environmental Architecture of the Human Functional Connectome},
  author={Raghav, Tanu and Guerrero, Daniel and Tipnis, Uttara and He, Jinyi and Ge, Tian and Meda, Shashwath and Calhoun, Vince and Pearlson, Godfrey and Liu, Jingyu},
  journal={arXiv preprint arXiv:2604.24614},
  year={2026}
}
```
