---
name: interpretable-eeg-biomarkers-parkinsons
description: "Interpretable EEG biomarkers for Parkinson's disease detection using interpretable electrophysiological features of resting-state EEG. Captures cortical neural dynamics alterations for reliable non-invasive diagnosis and monitoring. Activation: EEG biomarker Parkinson's, interpretable EEG features, resting-state EEG, cortical neural dynamics, PD diagnosis."
---

# Interpretable EEG Biomarkers for Parkinson's Disease

> Interpretable electrophysiological features of resting-state EEG for Parkinson's disease detection and monitoring. Captures reliable cortical neural dynamics alterations for non-invasive clinical applications.

## Metadata
- **Source**: arXiv:2604.01475v2
- **Authors**: Clinical neuroscience research team
- **Published**: 2026-04-01
- **Category**: Clinical Neuroscience, EEG Biomarkers, Parkinson's Disease

## Core Methodology

### Key Innovation
Parkinson's disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive. This framework introduces:

1. **Interpretable EEG Features**: Features with clear neurophysiological meaning rather than black-box deep learning representations
2. **Resting-State Specificity**: Captures disease-related changes in spontaneous brain activity
3. **Multi-Domain Analysis**: Combines spectral, temporal, and connectivity features
4. **Clinical Reliability**: Validated across multiple clinical sites and patient populations

### Technical Framework

#### Feature Categories

**1. Spectral Features**
- Band-specific power (delta, theta, alpha, beta, gamma)
- Relative power ratios
- Spectral edge frequency
- Peak frequency analysis

**2. Temporal Features**
- Amplitude envelope fluctuations
- Burst dynamics
- Phase-amplitude coupling
- Event-related desynchronization/synchronization (ERD/ERS)

**3. Connectivity Features**
- Phase locking value (PLV)
- Weighted phase lag index (wPLI)
- Directed transfer function (DTF)
- Partial directed coherence (PDC)

**4. Complexity Features**
- Sample entropy
- Lempel-Ziv complexity
- Higuchi's fractal dimension
- Detrended fluctuation analysis (DFA)

#### Feature Extraction Pipeline

```python
import numpy as np
from scipy import signal
from scipy.stats import entropy
from sklearn.preprocessing import StandardScaler

class EEGFeatureExtractor:
    """
    Extract interpretable EEG features for Parkinson's disease detection
    """
    def __init__(self, fs=1000, channels=64):
        self.fs = fs
        self.channels = channels
        
        # EEG frequency bands (Hz)
        self.bands = {
            'delta': (1, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma_low': (30, 50),
            'gamma_high': (50, 100)
        }
        
        # Channel groupings for PD-specific analysis
        self.roi_groups = {
            'frontal': ['Fp1', 'Fp2', 'F3', 'F4', 'F7', 'F8', 'Fz', 'FC1', 'FC2', 'FC5', 'FC6'],
            'central': ['C3', 'C4', 'Cz', 'CP1', 'CP2', 'CP5', 'CP6'],
            'parietal': ['P3', 'P4', 'Pz', 'P7', 'P8'],
            'temporal': ['T7', 'T8', 'TP7', 'TP8'],
            'occipital': ['O1', 'O2', 'Oz']
        }
    
    def extract_all_features(self, eeg_data, channel_names):
        """
        Extract comprehensive feature set from EEG data
        
        Parameters:
        -----------
        eeg_data : np.ndarray, shape (n_channels, n_samples)
            Preprocessed EEG data (filtered, artifact-removed)
        channel_names : list
            Names corresponding to each channel
        
        Returns:
        --------
        features : dict
            Dictionary of interpretable features
        """
        features = {}
        
        # Spectral features
        features['spectral'] = self._extract_spectral_features(eeg_data, channel_names)
        
        # Temporal features
        features['temporal'] = self._extract_temporal_features(eeg_data)
        
        # Connectivity features
        features['connectivity'] = self._extract_connectivity_features(eeg_data, channel_names)
        
        # Complexity features
        features['complexity'] = self._extract_complexity_features(eeg_data)
        
        # ROI-specific features
        features['roi'] = self._extract_roi_features(eeg_data, channel_names)
        
        return features
    
    def _extract_spectral_features(self, eeg_data, channel_names):
        """Extract power spectral features"""
        spectral = {}
        
        for ch_idx, ch_name in enumerate(channel_names):
            ch_data = eeg_data[ch_idx]
            
            # Welch's method for power spectral density
            freqs, psd = signal.welch(ch_data, fs=self.fs, nperseg=self.fs*2)
            
            # Band power
            for band, (low, high) in self.bands.items():
                mask = (freqs >= low) & (freqs < high)
                band_power = np.trapz(psd[mask], freqs[mask])
                spectral[f'{ch_name}_{band}_power'] = band_power
            
            # Total power
            total_power = np.trapz(psd, freqs)
            spectral[f'{ch_name}_total_power'] = total_power
            
            # Spectral edge frequency (95% of total power)
            cumsum = np.cumsum(psd) / total_power
            sef95 = freqs[np.argmax(cumsum >= 0.95)]
            spectral[f'{ch_name}_sef95'] = sef95
            
            # Peak frequency (alpha band)
            alpha_mask = (freqs >= 8) & (freqs <= 13)
            if psd[alpha_mask].sum() > 0:
                peak_freq = freqs[alpha_mask][np.argmax(psd[alpha_mask])]
                spectral[f'{ch_name}_alpha_peak'] = peak_freq
        
        # Relative power ratios
        for ch_name in channel_names:
            alpha = spectral.get(f'{ch_name}_alpha_power', 0)
            theta = spectral.get(f'{ch_name}_theta_power', 0)
            beta = spectral.get(f'{ch_name}_beta_power', 0)
            
            if theta > 0:
                spectral[f'{ch_name}_alpha_theta_ratio'] = alpha / theta
            if beta > 0:
                spectral[f'{ch_name}_alpha_beta_ratio'] = alpha / beta
        
        return spectral
    
    def _extract_connectivity_features(self, eeg_data, channel_names):
        """Extract functional connectivity features"""
        connectivity = {}
        n_channels = len(channel_names)
        
        # Compute phase locking value (PLV)
        plv_matrix = np.zeros((n_channels, n_channels))
        
        # Band-pass filter for each band
        for band, (low, high) in self.bands.items():
            sos = signal.butter(4, [low, high], btype='band', fs=self.fs, output='sos')
            filtered = signal.sosfilt(sos, eeg_data, axis=1)
            
            # Hilbert transform for instantaneous phase
            analytic = signal.hilbert(filtered, axis=1)
            phases = np.angle(analytic)
            
            # PLV calculation
            for i in range(n_channels):
                for j in range(i+1, n_channels):
                    phase_diff = phases[i] - phases[j]
                    plv = np.abs(np.mean(np.exp(1j * phase_diff)))
                    plv_matrix[i, j] = plv
                    plv_matrix[j, i] = plv
            
            # Store PLV statistics
            connectivity[f'{band}_plv_mean'] = np.mean(plv_matrix[np.triu_indices_from(plv_matrix, k=1)])
            connectivity[f'{band}_plv_std'] = np.std(plv_matrix[np.triu_indices_from(plv_matrix, k=1)])
        
        # ROI connectivity patterns
        for roi, roi_channels in self.roi_groups.items():
            roi_indices = [channel_names.index(ch) for ch in roi_channels if ch in channel_names]
            if len(roi_indices) > 1:
                roi_plv = plv_matrix[np.ix_(roi_indices, roi_indices)]
                connectivity[f'{roi}_intra_plv'] = np.mean(roi_plv[np.triu_indices_from(roi_plv, k=1)])
        
        return connectivity
    
    def _extract_temporal_features(self, eeg_data):
        """Extract temporal dynamics features"""
        temporal = {}
        
        # Amplitude envelope
        for band, (low, high) in [('alpha', (8, 13)), ('beta', (13, 30))]:
            sos = signal.butter(4, [low, high], btype='band', fs=self.fs, output='sos')
            filtered = signal.sosfilt(sos, eeg_data, axis=1)
            envelope = np.abs(signal.hilbert(filtered, axis=1))
            
            # Burst analysis (signal > threshold)
            threshold = envelope.mean(axis=1, keepdims=True) + envelope.std(axis=1, keepdims=True)
            bursts = envelope > threshold
            
            temporal[f'{band}_burst_duration'] = np.mean([np.mean(np.diff(np.where(ch)[0])) 
                                                         for ch in bursts])
            temporal[f'{band}_burst_rate'] = np.mean([np.sum(np.diff(np.where(ch)[0]) > 1) 
                                                      for ch in bursts])
            
            # Fluctuation amplitude
            temporal[f'{band}_envelope_std'] = np.std(envelope, axis=1).mean()
        
        return temporal
    
    def _extract_complexity_features(self, eeg_data):
        """Extract signal complexity features"""
        complexity = {}
        
        for ch_idx in range(eeg_data.shape[0]):
            ch_data = eeg_data[ch_idx]
            
            # Sample entropy
            complexity[f'ch{ch_idx}_sampen'] = self._sample_entropy(ch_data, order=2, r=0.2)
            
            # Lempel-Ziv complexity
            complexity[f'ch{ch_idx}_lz'] = self._lempel_ziv(ch_data)
            
            # Higuchi's fractal dimension
            complexity[f'ch{ch_idx}_hfd'] = self._higuchi_fd(ch_data)
        
        return complexity
    
    def _extract_roi_features(self, eeg_data, channel_names):
        """Extract region-of-interest specific features"""
        roi = {}
        
        # Group channels by ROI
        roi_indices = {}
        for roi_name, roi_channels in self.roi_groups.items():
            indices = [channel_names.index(ch) for ch in roi_channels if ch in channel_names]
            if indices:
                roi_indices[roi_name] = indices
        
        # Compute ROI-averaged spectral features
        for band, (low, high) in self.bands.items():
            sos = signal.butter(4, [low, high], btype='band', fs=self.fs, output='sos')
            filtered = signal.sosfilt(sos, eeg_data, axis=1)
            
            for roi_name, indices in roi_indices.items():
                roi_power = np.mean([np.var(filtered[i]) for i in indices])
                roi[f'{roi_name}_{band}_power'] = roi_power
        
        # Frontal asymmetry (depression/anxiety marker)
        if 'frontal' in roi_indices:
            frontal_indices = roi_indices['frontal']
            # Split left/right
            left_frontal = [i for i, ch in enumerate(channel_names) 
                          if ch in ['F3', 'F7', 'FC1', 'FC5']]
            right_frontal = [i for i, ch in enumerate(channel_names)
                           if ch in ['F4', 'F8', 'FC2', 'FC6']]
            
            if left_frontal and right_frontal:
                sos = signal.butter(4, [8, 13], btype='band', fs=self.fs, output='sos')
                filtered = signal.sosfilt(sos, eeg_data, axis=1)
                
                left_power = np.mean([np.var(filtered[i]) for i in left_frontal])
                right_power = np.mean([np.var(filtered[i]) for i in right_frontal])
                
                roi['frontal_alpha_asymmetry'] = np.log(right_power) - np.log(left_power)
        
        return roi
    
    def _sample_entropy(self, signal, order=2, r=0.2):
        """Calculate sample entropy"""
        N = len(signal)
        r = r * np.std(signal)
        
        def _phi(m):
            x = np.array([signal[i:i+m] for i in range(N - m + 1)])
            C = np.sum(np.max(np.abs(x[:, None] - x[None, :]), axis=2) < r, axis=0) / (N - m + 1)
            return np.sum(np.log(C)) / (N - m + 1)
        
        return _phi(order) - _phi(order + 1)
    
    def _lempel_ziv(self, signal):
        """Lempel-Ziv complexity"""
        # Binarize signal
        median = np.median(signal)
        binary = (signal > median).astype(int)
        
        # Lempel-Ziv algorithm
        n = len(binary)
        i, c, l = 0, 1, 1
        while i + l < n:
            if binary[i:i+l] == binary[c:c+l]:
                l += 1
            else:
                i = c
                c += l
                l = 1
        if l != 1:
            c += 1
        
        return c * np.log2(n) / n
    
    def _higuchi_fd(self, signal, k_max=10):
        """Higuchi's fractal dimension"""
        N = len(signal)
        L = []
        x = np.arange(1, k_max + 1)
        
        for k in range(1, k_max + 1):
            L_m = []
            for m in range(1, k + 1):
                L_m_k = np.sum([np.abs(signal[m + i*k - 1] - signal[m + (i-1)*k - 1])
                               for i in range(1, int((N - m) / k))])
                L_m_k = L_m_k * (N - 1) / (int((N - m) / k) * k)
                L_m.append(L_m_k)
            L.append(np.mean(L_m))
        
        # Linear fit in log-log space
        log_x = np.log(x)
        log_L = np.log(L)
        slope, _ = np.polyfit(log_x, log_L, 1)
        
        return -slope
```

### Interpretable Classification

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import shap

class InterpretablePDClassifier:
    """
    Interpretable classifier for Parkinson's disease detection
    """
    def __init__(self, feature_names):
        self.feature_names = feature_names
        
        # Use ensemble of interpretable models
        self.rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,  # Limit depth for interpretability
            min_samples_leaf=10,
            random_state=42
        )
        
        self.lr = LogisticRegression(
            penalty='l1',  # L1 for feature selection
            C=1.0,
            solver='saga',
            max_iter=1000
        )
    
    def fit(self, X, y):
        """Train models with feature importance analysis"""
        self.rf.fit(X, y)
        self.lr.fit(X, y)
        
        # SHAP values for global interpretability
        self.explainer = shap.TreeExplainer(self.rf)
        self.shap_values = self.explainer.shap_values(X)
        
        return self
    
    def get_top_features(self, n=20):
        """Get most important features"""
        importance = pd.DataFrame({
            'feature': self.feature_names,
            'rf_importance': self.rf.feature_importances_,
            'lr_coef': np.abs(self.lr.coef_[0])
        })
        
        importance['combined'] = (importance['rf_importance'] / importance['rf_importance'].max() +
                                   importance['lr_coef'] / importance['lr_coef'].max()) / 2
        
        return importance.nlargest(n, 'combined')
    
    def explain_prediction(self, X_instance):
        """Explain a single prediction using SHAP"""
        shap_values = self.explainer.shap_values(X_instance.reshape(1, -1))
        
        # Create explanation plot
        plt.figure(figsize=(10, 6))
        shap.summary_plot(
            shap_values,
            X_instance.reshape(1, -1),
            feature_names=self.feature_names,
            show=False
        )
        plt.tight_layout()
        return plt
```

## Applications
- **PD Diagnosis**: Non-invasive screening for early Parkinson's detection
- **Disease Monitoring**: Track progression and treatment response
- **Differential Diagnosis**: Distinguish PD from other parkinsonian syndromes
- **Biomarker Discovery**: Identify novel neural signatures of PD
- **Clinical Trials**: Objective endpoint for therapeutic trials

## Pitfalls
- **Medication Effects**: Dopaminergic medications alter EEG signatures
- **Age Confounds**: Age-related EEG changes must be accounted for
- **Comorbidities**: Depression, anxiety affect EEG patterns
- **Movement Artifacts**: Patient tremor can contaminate recordings
- **Individual Variability**: Large inter-individual differences require careful normalization

## Related Skills
- brain-network-controllability
- eeg-structure-guided-diffusion
- geometric-brain-dynamics-mapping
- multi-view-o-information-brain-dynamics

## References
```bibtex
@article{eegpd2026,
  title={Interpretable Electrophysiological Features of Resting-State EEG Capture Parkinson's Disease},
  author={[Authors]},
  journal={arXiv preprint arXiv:2604.01475},
  year={2026}
}
```
