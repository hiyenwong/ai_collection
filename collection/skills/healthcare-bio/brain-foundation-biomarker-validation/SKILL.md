---
name: brain-foundation-biomarker-validation
description: "RE-CONFIRM framework for validating robustness of biomarkers discovered by brain foundation models from dynamic functional connectivity. Systematic evaluation of internal reliability, external reliability, and validity for clinical biomarkers. Activation: RE-CONFIRM, biomarker validation, brain foundation model, robust biomarkers, dynamic functional connectivity."
---

# RE-CONFIRM: Validating Robust Biomarkers from Brain Foundation Models

> Systematic framework (RE-CONFIRM) for validating biomarkers discovered by brain foundation models from dynamic functional connectivity, evaluating internal reliability, external reliability, and validity across datasets and populations.

## Metadata
- **Source**: arXiv:2604.22018v1
- **Authors**: Zijian Zeng, Yijie Dong, Zhenyu Liu, Jiaqi Wu, Xiaohan Cao, Xiao Xiang, Yijia Zhou, Xian Li, Shifu Chen, Qixiang Lin, Zexuan Zhu, Ziqiang Li, Zhongke Gao, Xiaowei Yu, Zhengqing Miao, Lianglong Sun, Hui Shen, Mingrui Xia, Yijun Zhang, Yong He, Jie Zhang
- **Published**: 2026-04-23
- **Categories**: q-bio.NC, cs.AI, cs.LG

## Core Methodology

### Problem Statement
Brain foundation models (FMs) show remarkable performance in predicting brain disorders from dynamic functional connectivity (FC), but discovered biomarkers often lack:
- **Internal Reliability**: Inconsistent across folds, subjects, or time
- **External Reliability**: Fail to generalize across datasets, sites, or scanners
- **Validity**: May not reflect true neurobiological phenomena

Existing validation approaches are ad-hoc, lacking systematic frameworks for FM-derived biomarkers.

### Key Innovation
RE-CONFIRM framework provides six validation criteria:
1. **Intra-Subject Reliability**: Consistency across multiple scans of same subject
2. **Cross-Fold Reliability**: Consistency across train/test splits
3. **Cross-Site Reliability**: Consistency across different imaging sites
4. **Cross-Dataset Reliability**: Consistency across independent datasets
5. **Construct Validity**: Correlation with known behavioral/clinical measures
6. **Biological Plausibility**: Alignment with established neurobiological knowledge

### Technical Framework

#### RE-CONFIRM Framework Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   RE-CONFIRM Framework                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Brain Foundation Model (FM)             │   │
│  │  ┌─────────────┐    ┌───────────────────────┐  │   │
│  │  │   Dynamic   │───→│   Latent Space        │  │   │
│  │  │   FC Input  │    │   (Biomarkers)        │  │   │
│  │  └─────────────┘    └───────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
│                           ↓                            │
│  ┌──────────────────────────────────────────────────┐   │
│  │           RE-CONFIRM Validation                  │   │
│  │                                                    │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │    Internal Reliability (3 criteria)       │  │   │
│  │  │  • Intra-Subject (ICC)                     │  │   │
│  │  │  • Cross-Fold (Stability)                   │  │   │
│  │  │  • Temporal (Test-Retest)                   │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                  │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │    External Reliability (2 criteria)       │  │   │
│  │  │  • Cross-Site (Scanner effects)            │  │   │
│  │  │  • Cross-Dataset (Generalization)          │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                  │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │    Validity (1 criterion)                  │  │   │
│  │  │  • Construct Validity (Behavioral corr)    │  │   │
│  │  │  • Biological Plausibility                 │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                    │   │
│  └──────────────────────────────────────────────────┘   │
│                           ↓                            │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Validation Report                     │   │
│  │  ✓ PASS / ✗ FAIL per criterion                     │   │
│  │  Reliability Score: [0-1]                          │   │
│  │  Recommendation: Accept / Reject / Refine          │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### Validation Criteria Details

**1. Intra-Subject Reliability (ICC)**
```python
ICC(2,1) = (BMS - WMS) / (BMS + (k-1)*WMS)

Where:
- BMS: Between-subject mean square
- WMS: Within-subject mean square
- k: Number of measurements per subject

Interpretation:
- ICC < 0.50: Poor
- 0.50 ≤ ICC < 0.75: Moderate
- 0.75 ≤ ICC < 0.90: Good
- ICC ≥ 0.90: Excellent
```

**2. Cross-Fold Reliability (Stability)**
```python
Stability = 1 - ||w_train - w_test|| / ||w_train||

Where w are model weights or feature importance scores
```

**3. Temporal Reliability (Test-Retest)**
```python
test_retest = corr(biomarker_session1, biomarker_session2)

Pearson or Spearman correlation across repeated measurements
```

**4. Cross-Site Reliability**
```python
Harmonized_biomarker = Combat(biomarker)  # Remove site effects
Site_effect = 1 - var(harmonized) / var(raw)

Lower site effect = better generalization
```

**5. Cross-Dataset Reliability**
```python
AUC_source = model.evaluate(dataset_source)
AUC_target = model.evaluate(dataset_target)
Generalization_gap = |AUC_source - AUC_target|

Gap < 0.05: Excellent
Gap < 0.10: Acceptable
Gap > 0.10: Poor
```

**6. Construct Validity**
```python
correlation(biomarker, clinical_score)
correlation(biomarker, cognitive_performance)

Significant correlations support validity
```

## Implementation Guide

### Prerequisites
- Python >= 3.8
- PyTorch or TensorFlow for FM implementation
- Nilearn (for fMRI/FC processing)
- Pingouin or SciPy (for ICC)
- neuroCombat (for harmonization)
- scikit-learn (for metrics)

### Step-by-Step Implementation

#### 1. Data Preparation

```python
import numpy as np
import pandas as pd
from nilearn.connectome import ConnectivityMeasure

class FCDataLoader:
    """
    Load and preprocess dynamic functional connectivity data
    """
    def __init__(self, atlas='schaefer', n_rois=400, window_length=30, step=15):
        self.atlas = atlas
        self.n_rois = n_rois
        self.window_length = window_length
        self.step = step
        self.correlation_measure = ConnectivityMeasure(
            kind='correlation',
            vectorize=True
        )
        
    def load_time_series(self, bold_file, confounds_file=None):
        """
        Load BOLD time series
        
        Args:
            bold_file: Path to preprocessed BOLD data
            confounds_file: Path to confound regressors
        
        Returns:
            time_series: [n_volumes, n_rois]
        """
        import nibabel as nib
        
        img = nib.load(bold_file)
        data = img.get_fdata()
        
        # Load atlas and extract ROIs
        # (Implementation depends on atlas)
        time_series = self._extract_roi_timeseries(data)
        
        # Regress confounds if provided
        if confounds_file:
            confounds = pd.read_csv(confounds_file, sep='\t')
            time_series = self._regress_confounds(time_series, confounds)
        
        return time_series
    
    def compute_dynamic_fc(self, time_series):
        """
        Compute dynamic FC using sliding window
        
        Args:
            time_series: [n_volumes, n_rois]
        
        Returns:
            dfc: [n_windows, n_rois*(n_rois-1)/2] vectorized FC
        """
        n_volumes = time_series.shape[0]
        n_windows = (n_volumes - self.window_length) // self.step + 1
        
        dfc_windows = []
        for i in range(n_windows):
            start = i * self.step
            end = start + self.window_length
            window_ts = time_series[start:end, :]
            
            # Compute correlation
            fc = np.corrcoef(window_ts.T)
            # Fisher z-transform
            fc = np.arctanh(np.clip(fc, -0.999, 0.999))
            
            # Vectorize (upper triangle, excluding diagonal)
            fc_vec = fc[np.triu_indices_from(fc, k=1)]
            dfc_windows.append(fc_vec)
        
        return np.array(dfc_windows)
    
    def prepare_dataset(self, file_list, labels=None, sessions=None, sites=None):
        """
        Prepare full dataset
        
        Args:
            file_list: List of BOLD file paths
            labels: List of labels (optional)
            sessions: Session identifiers for test-retest
            sites: Site identifiers for cross-site analysis
        
        Returns:
            dataset: Dictionary with all data
        """
        dataset = {
            'dfc': [],
            'labels': [],
            'sessions': [],
            'sites': [],
            'subjects': []
        }
        
        for i, bold_file in enumerate(file_list):
            time_series = self.load_time_series(bold_file)
            dfc = self.compute_dynamic_fc(time_series)
            
            dataset['dfc'].append(dfc)
            dataset['labels'].append(labels[i] if labels else None)
            dataset['sessions'].append(sessions[i] if sessions else 0)
            dataset['sites'].append(sites[i] if sites else 0)
            dataset['subjects'].append(i)
        
        return dataset
```

#### 2. Foundation Model Implementation

```python
import torch
import torch.nn as nn

class BrainFoundationModel(nn.Module):
    """
    Brain foundation model for dynamic FC analysis
    (Simplified example - actual FMs may be more complex)
    """
    def __init__(self, input_dim, latent_dim=128, n_classes=2):
        super().__init__()
        
        # Temporal encoder (process dynamic FC windows)
        self.temporal_encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=input_dim, nhead=8, dim_feedforward=512),
            num_layers=4
        )
        
        # Embedding layer
        self.embedding = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim)
        )
        
        # Biomarker discovery (attention-based feature selection)
        self.biomarker_attention = nn.MultiheadAttention(latent_dim, num_heads=4)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, n_classes)
        )
        
        self.latent_dim = latent_dim
        
    def forward(self, dfc, return_biomarkers=False):
        """
        Args:
            dfc: [batch, n_windows, n_features]
        
        Returns:
            logits: [batch, n_classes]
            biomarkers: [batch, latent_dim] (optional)
        """
        # Temporal encoding
        x = self.temporal_encoder(dfc)  # [batch, n_windows, n_features]
        
        # Pool across time (mean)
        x = x.mean(dim=1)  # [batch, n_features]
        
        # Embed to latent space
        biomarkers = self.embedding(x)  # [batch, latent_dim]
        
        # Classify
        logits = self.classifier(biomarkers)
        
        if return_biomarkers:
            return logits, biomarkers
        return logits
    
    def extract_biomarkers(self, dataloader):
        """Extract biomarkers for all samples"""
        self.eval()
        biomarkers = []
        labels = []
        
        with torch.no_grad():
            for batch in dataloader:
                dfc = batch['dfc']
                label = batch['label']
                
                _, bio = self.forward(dfc, return_biomarkers=True)
                biomarkers.append(bio.cpu().numpy())
                labels.append(label.cpu().numpy())
        
        return np.concatenate(biomarkers), np.concatenate(labels)
```

#### 3. RE-CONFIRM Validation

```python
import pingouin as pg
from scipy import stats
from neuroCombat import neuroCombat
from sklearn.metrics import roc_auc_score

class RECONFIRMValidator:
    """
    RE-CONFIRM validation framework
    """
    def __init__(self, model, threshold_icc=0.75, threshold_stability=0.8):
        self.model = model
        self.threshold_icc = threshold_icc
        self.threshold_stability = threshold_stability
        self.results = {}
        
    def validate_intra_subject(self, biomarkers, subject_ids):
        """
        Validate intra-subject reliability (ICC)
        
        Args:
            biomarkers: [n_samples, n_features]
            subject_ids: [n_samples] subject identifiers
        
        Returns:
            icc_scores: [n_features] ICC for each biomarker dimension
        """
        n_features = biomarkers.shape[1]
        icc_scores = []
        
        for i in range(n_features):
            data = pd.DataFrame({
                'subject': subject_ids,
                'measurement': biomarkers[:, i]
            })
            
            # Compute ICC
            try:
                icc_result = pg.intraclass_corr(
                    data=data,
                    targets='subject',
                    raters='measurement',
                    ratings='measurement'
                )
                icc = icc_result['ICC'].iloc[2]  # ICC(2,1)
            except:
                icc = 0.0
            
            icc_scores.append(icc)
        
        return np.array(icc_scores)
    
    def validate_cross_fold(self, dataloader, n_folds=5):
        """
        Validate cross-fold stability
        
        Args:
            dataloader: PyTorch DataLoader
            n_folds: Number of CV folds
        
        Returns:
            stability_score: Overall stability
        """
        from sklearn.model_selection import KFold
        
        # Get all data
        all_biomarkers = []
        for batch in dataloader:
            _, bio = self.model(batch['dfc'], return_biomarkers=True)
            all_biomarkers.append(bio.detach().cpu().numpy())
        
        all_biomarkers = np.concatenate(all_biomarkers)
        n_samples = len(all_biomarkers)
        
        # Cross-validation
        biomarker_folds = []
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
        
        for train_idx, test_idx in kf.split(all_biomarkers):
            # Train on fold
            train_bio = all_biomarkers[train_idx]
            train_mean = train_bio.mean(axis=0)
            
            # Test on fold
            test_bio = all_biomarkers[test_idx]
            test_mean = test_bio.mean(axis=0)
            
            biomarker_folds.append((train_mean, test_mean))
        
        # Compute stability
        stabilities = []
        for train_mean, test_mean in biomarker_folds:
            stability = 1 - np.linalg.norm(train_mean - test_mean) / np.linalg.norm(train_mean)
            stabilities.append(stability)
        
        return np.mean(stabilities), np.std(stabilities)
    
    def validate_cross_site(self, biomarkers, site_ids, subject_ids):
        """
        Validate cross-site reliability
        
        Args:
            biomarkers: [n_samples, n_features]
            site_ids: [n_samples] site identifiers
            subject_ids: [n_samples] subject identifiers
        
        Returns:
            harmonized_biomarkers: Site-effect removed
            site_effect: Variance explained by site
        """
        # Prepare data for ComBat
        data_df = pd.DataFrame(biomarkers)
        covars = pd.DataFrame({
            'subject': subject_ids,
            'site': site_ids
        })
        
        # Apply ComBat harmonization
        harmonized = neuroCombat(
            dat=data_df.T,
            covars=covars,
            batch_col='site',
            discrete_cols=None,
            continuous_cols=None
        )['data'].T
        
        # Compute site effect
        var_raw = np.var(biomarkers, axis=0)
        var_harmonized = np.var(harmonized, axis=0)
        site_effect = 1 - (var_harmonized / (var_raw + 1e-10))
        
        return harmonized, site_effect
    
    def validate_cross_dataset(self, model, dataset_source, dataset_target):
        """
        Validate cross-dataset generalization
        
        Args:
            model: Trained model
            dataset_source: Source domain data
            dataset_target: Target domain data
        
        Returns:
            generalization_gap: Performance difference
        """
        # Evaluate on source
        bio_source, labels_source = model.extract_biomarkers(dataset_source)
        # Train classifier on source
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression()
        clf.fit(bio_source, labels_source)
        auc_source = roc_auc_score(labels_source, clf.predict_proba(bio_source)[:, 1])
        
        # Evaluate on target
        bio_target, labels_target = model.extract_biomarkers(dataset_target)
        auc_target = roc_auc_score(labels_target, clf.predict_proba(bio_target)[:, 1])
        
        generalization_gap = abs(auc_source - auc_target)
        
        return {
            'auc_source': auc_source,
            'auc_target': auc_target,
            'gap': generalization_gap
        }
    
    def validate_construct_validity(self, biomarkers, clinical_scores):
        """
        Validate construct validity
        
        Args:
            biomarkers: [n_samples, n_features]
            clinical_scores: [n_samples] clinical/behavioral measures
        
        Returns:
            correlations: Correlation per biomarker
        """
        correlations = []
        p_values = []
        
        for i in range(biomarkers.shape[1]):
            corr, pval = stats.pearsonr(biomarkers[:, i], clinical_scores)
            correlations.append(corr)
            p_values.append(pval)
        
        return np.array(correlations), np.array(p_values)
    
    def full_validation(self, dataset, clinical_scores=None):
        """
        Run full RE-CONFIRM validation
        
        Args:
            dataset: Dictionary with all data
            clinical_scores: Optional clinical measures
        
        Returns:
            report: Validation results
        """
        biomarkers = dataset['biomarkers']
        subject_ids = dataset['subjects']
        sites = dataset.get('sites')
        
        report = {
            'criteria': {},
            'overall_score': 0.0,
            'recommendation': ''
        }
        
        # 1. Intra-Subject Reliability
        if 'test_sessions' in dataset:
            icc = self.validate_intra_subject(biomarkers, dataset['test_sessions'])
            report['criteria']['intra_subject'] = {
                'icc_mean': np.mean(icc),
                'icc_median': np.median(icc),
                'n_pass': np.sum(icc >= self.threshold_icc),
                'status': 'PASS' if np.median(icc) >= self.threshold_icc else 'FAIL'
            }
        
        # 2. Cross-Fold Stability
        # (Implementation depends on dataloader structure)
        
        # 3. Cross-Site Reliability
        if sites is not None and len(np.unique(sites)) > 1:
            _, site_effect = self.validate_cross_site(biomarkers, sites, subject_ids)
            report['criteria']['cross_site'] = {
                'site_effect_mean': np.mean(site_effect),
                'status': 'PASS' if np.mean(site_effect) < 0.2 else 'WARNING'
            }
        
        # 4. Construct Validity
        if clinical_scores is not None:
            corr, pval = self.validate_construct_validity(biomarkers, clinical_scores)
            significant = np.sum(pval < 0.05)
            report['criteria']['construct_validity'] = {
                'n_significant': significant,
                'mean_correlation': np.mean(np.abs(corr)),
                'status': 'PASS' if significant > len(corr) * 0.1 else 'FAIL'
            }
        
        # Compute overall score
        scores = [c.get('status') == 'PASS' for c in report['criteria'].values()]
        report['overall_score'] = np.mean(scores) if scores else 0
        
        # Recommendation
        if report['overall_score'] >= 0.8:
            report['recommendation'] = 'ACCEPT'
        elif report['overall_score'] >= 0.5:
            report['recommendation'] = 'REFINE'
        else:
            report['recommendation'] = 'REJECT'
        
        self.results = report
        return report
    
    def generate_report(self, output_file='reconfirm_report.txt'):
        """Generate validation report"""
        with open(output_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write("RE-CONFIRM VALIDATION REPORT\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"Overall Score: {self.results['overall_score']:.3f}\n")
            f.write(f"Recommendation: {self.results['recommendation']}\n\n")
            
            f.write("-"*60 + "\n")
            f.write("VALIDATION CRITERIA\n")
            f.write("-"*60 + "\n\n")
            
            for criterion, details in self.results['criteria'].items():
                f.write(f"\n{criterion.upper()}:\n")
                for key, value in details.items():
                    if isinstance(value, float):
                        f.write(f"  {key}: {value:.4f}\n")
                    else:
                        f.write(f"  {key}: {value}\n")
```

## Applications

1. **Clinical Biomarker Discovery**: Validate brain disorder biomarkers
2. **Multi-Site Studies**: Ensure reliability across imaging centers
3. **Longitudinal Tracking**: Monitor biomarker stability over time
4. **Model Selection**: Compare brain foundation models
5. **Regulatory Compliance**: Meet validation standards for clinical use

## Key Features

- **Six Validation Criteria**: Comprehensive reliability and validity assessment
- **Quantitative Scoring**: Objective pass/fail thresholds
- **Harmonization Support**: Built-in ComBat for site effects
- **Modular Design**: Can validate any brain FM
- **Report Generation**: Automated validation reports

## Pitfalls

1. **Data Requirements**: Needs test-retest data for intra-subject reliability
2. **Multi-Site Data**: Cross-site validation requires multiple sites
3. **Clinical Scores**: Construct validity needs behavioral/clinical data
4. **Computational Cost**: Running all criteria on large datasets is expensive
5. **Threshold Sensitivity**: Results depend on chosen ICC/stability thresholds

## Related Skills
- brain-dit-fmri-foundation-model
- brain-mri-foundation-clinical
- functional-connectome-fingerprint

## References
```
Zeng, Z., et al. (2026). RE-CONFIRM: Validating Robust Biomarkers Discovered 
by Brain Foundation Models from Dynamic Functional Connectivity. 
arXiv preprint arXiv:2604.22018v1.
```
