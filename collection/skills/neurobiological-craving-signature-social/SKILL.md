---
name: neurobiological-craving-signature-social
description: "Neurobiological Craving Signature (NCS) - predicts social craving and social reinstatement from neural activity patterns. Identifies biomarkers for social isolation effects on brain circuits involved in social motivation. Activation: neurobiological craving signature, social craving, NCS biomarker, social isolation neural, craving prediction, social neuroscience."
---

# Neurobiological Craving Signature (NCS) for Social Craving Prediction

> NCS is a neurobiological framework that predicts social craving and social reinstatement from neural activity patterns, identifying specific biomarkers for the effects of social isolation on brain circuits involved in social motivation and connection-seeking behavior.

## Metadata
- **Source**: arXiv:2604.11208v1
- **Authors**: Social neuroscience research team
- **Published**: 2026-04-13
- **Category**: Social Neuroscience, Neurobiological Biomarkers, Affective Neuroscience

## Core Methodology

### Key Innovation
Traditional social neuroscience relies on self-reported measures of loneliness and social desire. NCS introduces:

1. **Objective neural biomarkers**: Quantifiable neural signatures predicting social craving independent of self-report
2. **Circuit-specific markers**: Differentiates craving-related activity in distinct brain networks
3. **Predictive validity**: Neural patterns predict future social reinstatement behavior
4. **Cross-validation**: Replicated across multiple social isolation paradigms

### Technical Framework

#### NCS Components
The Neurobiological Craving Signature comprises:

1. **Mesolimbic Dopamine Circuit**
   - Ventral Tegmental Area (VTA) activation
   - Nucleus accumbens (NAcc) response
   - Dopaminergic prediction error signals

2. **Social Brain Network**
   - Medial prefrontal cortex (mPFC) social cognition
   - Temporoparietal junction (TPJ) mentalizing
   - Anterior cingulate cortex (ACC) social monitoring

3. **Homeostatic Regulation Circuit**
   - Hypothalamic responses to isolation
   - Stress system (HPA axis) markers
   - Autonomic nervous system measures

#### Feature Extraction

**Multi-Modal Neural Features**:
```python
class NCSDescriptor:
    """
    Neurobiological Craving Signature descriptor
    Extracts multi-modal neural features for craving prediction
    """
    def __init__(self, n_voxels=100000):
        self.n_voxels = n_voxels
        
        # Circuit-specific regions of interest
        self.rois = {
            'mesolimbic': ['VTA', 'NAcc', 'caudate', 'putamen'],
            'social_brain': ['mPFC', 'TPJ', 'ACC', 'precuneus'],
            'homeostatic': ['hypothalamus', 'amygdala', 'insula'],
            'default_mode': ['PCC', 'mPFC', 'angular_gyrus']
        }
    
    def extract_fmri_features(self, fmri_timeseries, event_onsets):
        """
        Extract fMRI-based NCS features
        
        Parameters:
        -----------
        fmri_timeseries : np.ndarray, shape (timepoints, voxels)
            Preprocessed BOLD signal
        event_onsets : list
            Timestamps of social stimuli presentations
        
        Returns:
        --------
        features : dict
            Circuit-specific activation patterns
        """
        features = {}
        
        for circuit_name, regions in self.rois.items():
            # Extract region time series
            circuit_ts = self._extract_roi_timeseries(fmri_timeseries, regions)
            
            # Event-related analysis
            epochs = self._create_epochs(circuit_ts, event_onsets)
            
            # Features: mean activation, variability, connectivity
            features[circuit_name] = {
                'mean_activation': epochs.mean(axis=(0, 1)),
                'peak_activation': epochs.max(axis=(0, 1)),
                'activation_variance': epochs.var(axis=(0, 1)),
                'temporal_derivative': np.gradient(epochs.mean(axis=0)).mean(),
            }
            
            # Functional connectivity within circuit
            connectivity = np.corrcoef(epochs.mean(axis=0).T)
            features[circuit_name]['fc_matrix'] = connectivity
            features[circuit_name]['fc_strength'] = connectivity.mean()
        
        return features
    
    def extract_eeg_features(self, eeg_data, channels):
        """
        Extract EEG-based NCS features (faster temporal resolution)
        
        Parameters:
        -----------
        eeg_data : np.ndarray, shape (channels, timepoints)
            Preprocessed EEG signals
        channels : list
            Channel names corresponding to rows
        
        Returns:
        --------
        eeg_features : dict
            Spectral and connectivity features
        """
        from scipy import signal
        
        eeg_features = {}
        
        # Frequency band power
        bands = {
            'delta': (1, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
        
        for band_name, (low, high) in bands.items():
            # Bandpass filter
            sos = signal.butter(4, [low, high], btype='band', fs=1000, output='sos')
            filtered = signal.sosfilt(sos, eeg_data, axis=1)
            
            # Power
            power = np.mean(filtered ** 2, axis=1)
            eeg_features[f'{band_name}_power'] = power
            
            # Frontal asymmetry (alpha)
            if band_name == 'alpha':
                frontal_left = ['Fp1', 'F3', 'F7']
                frontal_right = ['Fp2', 'F4', 'F8']
                
                left_idx = [channels.index(ch) for ch in frontal_left if ch in channels]
                right_idx = [channels.index(ch) for ch in frontal_right if ch in channels]
                
                if left_idx and right_idx:
                    asymmetry = np.log(power[left_idx].mean()) - np.log(power[right_idx].mean())
                    eeg_features['frontal_alpha_asymmetry'] = asymmetry
        
        # Event-related potentials (ERP) for social stimuli
        erp = self._compute_erp(eeg_data, event_onsets=...)
        eeg_features['erp_components'] = {
            'P300': erp[:, 300:500].mean(),  # 300-500ms post-stimulus
            'LPP': erp[:, 500:1000].mean(),  # Late positive potential
        }
        
        return eeg_features
```

#### NCS Prediction Model

**Multi-Level Neural Signature**:
```python
class NCSPredictor(nn.Module):
    """
    Neural network for predicting social craving from multi-modal NCS
    """
    def __init__(self, fmri_feature_dim=500, eeg_feature_dim=200):
        super().__init__()
        
        # Circuit-specific encoders
        self.mesolimbic_encoder = self._build_encoder(100, 64)
        self.social_encoder = self._build_encoder(100, 64)
        self.homeostatic_encoder = self._build_encoder(100, 64)
        
        # Cross-circuit integration
        self.cross_circuit_attention = nn.MultiheadAttention(
            embed_dim=64, num_heads=4
        )
        
        # EEG temporal encoder
        self.eeg_lstm = nn.LSTM(
            input_size=eeg_feature_dim,
            hidden_size=128,
            num_layers=2,
            batch_first=True,
            bidirectional=True
        )
        
        # Fusion layer
        self.fusion = nn.Sequential(
            nn.Linear(64 * 3 + 256, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU()
        )
        
        # Prediction heads
        self.craving_head = nn.Linear(128, 1)  # Continuous craving intensity
        self.reinstatement_head = nn.Linear(128, 1)  # Binary reinstatement prediction
        self.duration_head = nn.Linear(128, 1)  # Time to social seeking
    
    def forward(self, fmri_features, eeg_features, behavioral_context):
        """
        Parameters:
        -----------
        fmri_features : dict
            Circuit-specific fMRI features
        eeg_features : torch.Tensor
            [batch, time, eeg_dim] EEG features
        behavioral_context : torch.Tensor
            [batch, context_dim] Time since isolation, previous social history
        
        Returns:
        --------
        predictions : dict
            Craving intensity, reinstatement probability, duration estimate
        """
        # Encode each circuit
        meso = self.mesolimbic_encoder(fmri_features['mesolimbic'])
        social = self.social_encoder(fmri_features['social_brain'])
        homeo = self.homeostatic_encoder(fmri_features['homeostatic'])
        
        # Cross-circuit attention
        circuit_stack = torch.stack([meso, social, homeo], dim=0)
        attended, _ = self.cross_circuit_attention(
            circuit_stack, circuit_stack, circuit_stack
        )
        circuit_repr = attended.view(-1, 64 * 3)
        
        # EEG temporal encoding
        eeg_out, _ = self.eeg_lstm(eeg_features)
        eeg_repr = torch.cat([eeg_out[:, -1, :128], eeg_out[:, 0, 128:]], dim=1)
        
        # Fusion
        combined = torch.cat([circuit_repr, eeg_repr, behavioral_context], dim=1)
        fused = self.fusion(combined)
        
        # Predictions
        craving = torch.sigmoid(self.craving_head(fused))
        reinstatement = torch.sigmoid(self.reinstatement_head(fused))
        duration = torch.relu(self.duration_head(fused))
        
        return {
            'craving_intensity': craving,
            'reinstatement_probability': reinstatement,
            'seeking_duration': duration
        }
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- Nilearn for fMRI analysis
- MNE for EEG processing
- PyTorch for deep learning
- scikit-learn for baseline models

### Step-by-Step

1. **Data Preprocessing**
```python
from nilearn import image, signal
from nilearn.masking import apply_mask

def preprocess_fmri(fmri_file, confounds_file):
    """Preprocess resting-state or task fMRI"""
    # Load data
    fmri_img = image.load_img(fmri_file)
    confounds = pd.read_csv(confounds_file, sep='\t')
    
    # Confound regression
    fmri_clean = signal.clean(
        fmri_img,
        confounds=confounds[['trans_x', 'trans_y', 'trans_z',
                            'rot_x', 'rot_y', 'rot_z',
                            'white_matter', 'csf']].values,
        detrend=True,
        standardize=True,
        low_pass=0.1,
        high_pass=0.01,
        t_r=2.0
    )
    
    # Extract time series from ROIs
    from nilearn.maskers import NiftiLabelsMasker
    masker = NiftiLabelsMasker(
        labels_img='schaefer_400_7networks.nii.gz',
        standardize=True
    )
    time_series = masker.fit_transform(fmri_clean)
    
    return time_series, masker
```

2. **NCS Feature Extraction**
```python
def compute_ncs_signature(time_series, roi_labels):
    """
    Compute NCS from preprocessed time series
    
    Parameters:
    -----------
    time_series : np.ndarray, shape (n_timepoints, n_rois)
    roi_labels : dict
        Mapping from circuit names to ROI indices
    
    Returns:
    --------
    ncs_features : dict
        Circuit-specific NCS components
    """
    ncs = {}
    
    # Compute connectivity matrix
    connectivity = np.corrcoef(time_series.T)
    
    for circuit, rois in roi_labels.items():
        # Extract circuit-specific connectivity
        circuit_conn = connectivity[np.ix_(rois, rois)]
        
        ncs[circuit] = {
            'mean_fc': circuit_conn.mean(),
            'fc_variance': circuit_conn.var(),
            'fc_pattern': circuit_conn.flatten(),
            'node_strength': circuit_conn.sum(axis=1).mean(),
            'efficiency': compute_efficiency(circuit_conn)
        }
    
    return ncs
```

3. **Model Training**
```python
def train_ncs_model(train_data, validation_data, epochs=100):
    """
    Train NCS prediction model
    
    Parameters:
    -----------
    train_data : tuple
        (fmri_features, eeg_features, labels)
    validation_data : tuple
        Same format as train_data
    """
    model = NCSPredictor()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    criterion = nn.MSELoss()
    
    for epoch in range(epochs):
        model.train()
        for batch in train_loader:
            fmri, eeg, context, labels = batch
            
            optimizer.zero_grad()
            predictions = model(fmri, eeg, context)
            
            # Multi-task loss
            loss = criterion(predictions['craving_intensity'], labels['craving'])
            loss += 0.5 * nn.BCELoss()(predictions['reinstatement_probability'], 
                                       labels['reinstatement'])
            
            loss.backward()
            optimizer.step()
        
        # Validation
        if epoch % 10 == 0:
            validate(model, validation_data)
    
    return model
```

### Validation Metrics

**Primary Outcomes**:
- Correlation between predicted and self-reported craving
- AUC for reinstatement prediction
- Mean absolute error for seeking duration

**Cross-Validation**:
```python
from sklearn.model_selection import GroupKFold

def cross_validate_ncs(data, n_splits=5):
    """Leave-one-subject-out cross-validation"""
    gkf = GroupKFold(n_splits=n_splits)
    
    results = []
    for train_idx, test_idx in gkf.split(X, y, groups=subject_ids):
        model = train_ncs_model(
            (X[train_idx], y[train_idx]),
            (X[test_idx], y[test_idx])
        )
        
        predictions = model.predict(X[test_idx])
        results.append(evaluate(predictions, y[test_idx]))
    
    return aggregate_results(results)
```

## Applications
- **Social Isolation Research**: Quantify neural effects of loneliness and social deprivation
- **Addiction Studies**: Cross-species translation of craving mechanisms
- **Mental Health**: Early detection of social withdrawal in depression
- **Intervention Design**: Personalized timing of social reconnection interventions

## Pitfalls
- **Individual Variability**: NCS patterns vary significantly across individuals
- **State Dependence**: Signature may change with acute stress or mood
- **Self-Report Correlation**: Validation still relies partly on subjective craving reports
- **Cross-Modal Integration**: Combining fMRI and EEG requires careful temporal alignment
- **Cultural Factors**: Social craving expression varies across cultures

## Related Skills
- brain-network-controllability
- multi-view-o-information-brain-dynamics
- eeg-hopfield-emotion-energy
- neural-dynamics-decision-making

## References
```bibtex
@article{ncs2026,
  title={The Neurobiological Craving Signature (NCS) predicts social craving and social reinstatement},
  author={[Authors]},
  journal={arXiv preprint arXiv:2604.11208},
  year={2026}
}
```
