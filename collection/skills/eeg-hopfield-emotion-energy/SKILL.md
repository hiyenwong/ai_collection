---
name: eeg-hopfield-emotion-energy
description: "Quantifying brain network stability during emotional processing using EEG-based Hopfield energy. Applies continuous Hopfield network energy to functional connectivity matrices to measure emotional state stability. Use when working with: (1) EEG-based emotion analysis, (2) Brain network stability metrics, (3) Hopfield energy in neuroscience, (4) Affective computing with neural dynamics. Activation: emotion energy landscape, EEG Hopfield, brain stability, affective neuroscience."
---

# EEG-Based Hopfield Energy for Emotion Analysis

Quantifying brain network stability during emotional processing using EEG-based Hopfield energy. This framework applies continuous Hopfield network energy to empirically derived functional connectivity matrices to measure the dynamical stability of emotional brain states.

## Core Concept

Emotional states correspond to distinct attractor basins in the brain's functional landscape. By computing Hopfield energy from EEG functional connectivity, we can quantify the stability of these states and relate them to cognitive processing characteristics.

## Theoretical Background

### Hopfield Energy in Neural Networks

The continuous Hopfield network energy is defined as:

```
E = -0.5 * Σᵢ Σⱼ Wᵢⱼ * sᵢ * sⱼ
```

Where:
- `W`: Functional connectivity matrix (coupling weights)
- `s`: Neural activity state vector
- Lower (more negative) energy = more stable state

### Connection to Brain Networks

In the context of brain functional connectivity:
- **Functional connectivity matrix** serves as the coupling weights W
- **EEG channel activations** serve as the state vector s
- **Energy** quantifies the stability of the current network configuration

## Methodology

### Step 1: EEG Data Collection

```python
import numpy as np
from scipy.signal import welch

class EEGDataCollector:
    """Collect and preprocess EEG data for emotion analysis."""
    
    def __init__(self, sampling_rate: int = 500, n_channels: int = 64):
        self.fs = sampling_rate
        self.n_channels = n_channels
        
    def record_emotion_task(self, subject_id: str, emotion_condition: str):
        """
        Record EEG during emotion processing task.
        
        Task: Happy vs Sad facial expression discrimination
        Duration: ~30-60 minutes
        Trials: Multiple blocks with randomized emotional stimuli
        """
        # Setup EEG cap with high-density montage
        # Present facial expressions (happy/sad) via visual display
        # Record continuous EEG with markers for trial onsets
        pass
    
    def preprocess(self, raw_eeg: np.ndarray) -> np.ndarray:
        """
        Preprocess EEG data.
        
        Steps:
        1. Bandpass filter (0.5-100 Hz)
        2. Notch filter (50/60 Hz line noise)
        3. Artifact rejection (ICA for eye blinks, muscle noise)
        4. Re-reference to average or specific montage
        """
        from scipy.signal import butter, filtfilt
        
        # Bandpass filter
        lowcut, highcut = 0.5, 100
        nyquist = 0.5 * self.fs
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(4, [low, high], btype='band')
        filtered = filtfilt(b, a, raw_eeg, axis=1)
        
        return filtered
```

### Step 2: Functional Connectivity Estimation

```python
class FunctionalConnectivityEstimator:
    """Estimate functional connectivity from EEG using wPLI."""
    
    def __init__(self, fs: float = 500.0):
        self.fs = fs
        
    def compute_wpli(self, eeg_data: np.ndarray, fmin: float, fmax: float) -> np.ndarray:
        """
        Compute weighted Phase Lag Index (wPLI) connectivity matrix.
        
        wPLI is robust to volume conduction and zero-phase lag artifacts.
        
        Args:
            eeg_data: (n_channels, n_times) EEG data
            fmin, fmax: Frequency band limits
            
        Returns:
            connectivity: (n_channels, n_channels) connectivity matrix
        """
        from scipy.signal import hilbert, csd
        
        n_channels = eeg_data.shape[0]
        connectivity = np.zeros((n_channels, n_channels))
        
        # Bandpass filter to frequency band of interest
        from scipy.signal import butter, filtfilt
        nyquist = self.fs / 2
        low, high = fmin / nyquist, fmax / nyquist
        b, a = butter(4, [low, high], btype='band')
        filtered = filtfilt(b, a, eeg_data, axis=1)
        
        # Compute analytic signal
        analytic = hilbert(filtered, axis=1)
        
        # Compute wPLI for each channel pair
        for i in range(n_channels):
            for j in range(i+1, n_channels):
                # Cross-spectrum
                s_ij = analytic[i] * np.conj(analytic[j])
                
                # Imaginary part
                im_s = np.imag(s_ij)
                
                # wPLI
                wpli = np.abs(np.mean(im_s)) / np.mean(np.abs(im_s))
                
                connectivity[i, j] = wpli
                connectivity[j, i] = wpli
        
        return connectivity
    
    def compute_band_connectivity(self, eeg_data: np.ndarray) -> dict:
        """
        Compute connectivity for standard EEG frequency bands.
        
        Returns:
            Dictionary with connectivity matrices for each band
        """
        bands = {
            'delta': (0.5, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
        
        connectivity = {}
        for band, (fmin, fmax) in bands.items():
            connectivity[band] = self.compute_wpli(eeg_data, fmin, fmax)
        
        return connectivity
```

### Step 3: Hopfield Energy Computation

```python
class HopfieldEnergyAnalyzer:
    """Compute Hopfield energy from functional connectivity."""
    
    def __init__(self):
        self.connectivity = None
        self.energy_history = []
        
    def compute_energy(self, connectivity: np.ndarray, activity: np.ndarray = None) -> float:
        """
        Compute Hopfield energy from connectivity matrix.
        
        E = -0.5 * s^T * W * s
        
        Where:
        - W: Functional connectivity matrix (weights)
        - s: Activity state (if None, uses eigenvector centrality as proxy)
        
        Args:
            connectivity: (n_channels, n_channels) connectivity matrix
            activity: (n_channels,) activity vector (optional)
            
        Returns:
            energy: Scalar energy value (lower = more stable)
        """
        if activity is None:
            # Use leading eigenvector as activity proxy
            from numpy.linalg import eigh
            eigenvalues, eigenvectors = eigh(connectivity)
            activity = eigenvectors[:, -1]  # Leading eigenvector
        
        # Normalize activity
        activity = activity / np.linalg.norm(activity)
        
        # Compute energy: E = -0.5 * s^T * W * s
        energy = -0.5 * activity.T @ connectivity @ activity
        
        return energy
    
    def compute_trial_energy(self, eeg_trial: np.ndarray, 
                             estimator: FunctionalConnectivityEstimator) -> dict:
        """
        Compute Hopfield energy for a single trial across frequency bands.
        
        Args:
            eeg_trial: (n_channels, n_times) EEG data for one trial
            estimator: Connectivity estimator instance
            
        Returns:
            energies: Dictionary of energy values per frequency band
        """
        # Compute connectivity for each band
        band_connectivity = estimator.compute_band_connectivity(eeg_trial)
        
        # Compute energy for each band
        energies = {}
        for band, conn_matrix in band_connectivity.items():
            energies[band] = self.compute_energy(conn_matrix)
        
        return energies
    
    def analyze_emotion_trials(self, trials_happy: list, trials_sad: list,
                               estimator: FunctionalConnectivityEstimator) -> dict:
        """
        Compare Hopfield energy between happy and sad emotion conditions.
        
        Args:
            trials_happy: List of EEG trials for happy condition
            trials_sad: List of EEG trials for sad condition
            estimator: Connectivity estimator
            
        Returns:
            results: Dictionary with energy statistics and comparisons
        """
        # Compute energies for all trials
        happy_energies = {band: [] for band in ['delta', 'theta', 'alpha', 'beta', 'gamma']}
        sad_energies = {band: [] for band in ['delta', 'theta', 'alpha', 'beta', 'gamma']}
        
        for trial in trials_happy:
            trial_energies = self.compute_trial_energy(trial, estimator)
            for band, energy in trial_energies.items():
                happy_energies[band].append(energy)
        
        for trial in trials_sad:
            trial_energies = self.compute_trial_energy(trial, estimator)
            for band, energy in trial_energies.items():
                sad_energies[band].append(energy)
        
        # Statistical comparison
        from scipy import stats
        
        results = {}
        for band in happy_energies.keys():
            happy_vals = np.array(happy_energies[band])
            sad_vals = np.array(sad_energies[band])
            
            # t-test
            t_stat, p_value = stats.ttest_ind(sad_vals, happy_vals)
            
            # Effect size (Cohen's d)
            pooled_std = np.sqrt((np.std(happy_vals)**2 + np.std(sad_vals)**2) / 2)
            cohens_d = (np.mean(sad_vals) - np.mean(happy_vals)) / pooled_std
            
            results[band] = {
                'happy_mean': np.mean(happy_vals),
                'happy_std': np.std(happy_vals),
                'sad_mean': np.mean(sad_vals),
                'sad_std': np.std(sad_vals),
                't_statistic': t_stat,
                'p_value': p_value,
                'cohens_d': cohens_d
            }
        
        return results
```

### Step 4: Network Efficiency Analysis

```python
class NetworkEfficiencyAnalyzer:
    """Analyze global efficiency and its relation to Hopfield energy."""
    
    def compute_global_efficiency(self, connectivity: np.ndarray) -> float:
        """
        Compute global efficiency of the network.
        
        Global efficiency is the average inverse shortest path length.
        Higher efficiency = more integrated network.
        
        Args:
            connectivity: (n_channels, n_channels) connectivity matrix
            
        Returns:
            efficiency: Global efficiency value
        """
        from scipy.sparse.csgraph import shortest_path
        
        # Convert connectivity to distance (inverse)
        # Add small epsilon to avoid division by zero
        distance = 1.0 / (connectivity + 1e-10)
        np.fill_diagonal(distance, 0)
        
        # Compute shortest paths
        shortest_paths = shortest_path(distance, method='D', directed=False)
        
        # Global efficiency: average of inverse shortest paths
        n = len(connectivity)
        efficiency = (1.0 / (n * (n - 1))) * np.sum(1.0 / (shortest_paths + np.eye(n) * np.inf))
        
        return efficiency
    
    def correlate_energy_efficiency(self, energies: list, 
                                    connectivities: list) -> tuple:
        """
        Correlate Hopfield energy with global efficiency.
        
        Expected: Strong negative correlation (higher efficiency -> lower/more negative energy)
        
        Returns:
            correlation, p_value
        """
        efficiencies = [self.compute_global_efficiency(conn) for conn in connectivities]
        
        from scipy.stats import pearsonr
        correlation, p_value = pearsonr(energies, efficiencies)
        
        return correlation, p_value, efficiencies
```

## Complete Analysis Pipeline

```python
class EmotionEnergyLandscapeAnalysis:
    """Complete pipeline for EEG-based emotion energy analysis."""
    
    def __init__(self, fs: float = 500.0, n_channels: int = 64):
        self.fs = fs
        self.n_channels = n_channels
        self.connectivity_estimator = FunctionalConnectivityEstimator(fs)
        self.energy_analyzer = HopfieldEnergyAnalyzer()
        self.efficiency_analyzer = NetworkEfficiencyAnalyzer()
        
    def run_analysis(self, eeg_data: dict, condition_labels: list) -> dict:
        """
        Run complete analysis pipeline.
        
        Args:
            eeg_data: Dictionary with 'happy' and 'sad' trial lists
            condition_labels: List of condition labels for each trial
            
        Returns:
            results: Complete analysis results
        """
        # 1. Compute energies by condition
        energy_results = self.energy_analyzer.analyze_emotion_trials(
            eeg_data['happy'],
            eeg_data['sad'],
            self.connectivity_estimator
        )
        
        # 2. Compute global efficiency for correlation
        all_trials = eeg_data['happy'] + eeg_data['sad']
        all_connectivities = []
        all_energies = []
        
        for trial in all_trials:
            conn = self.connectivity_estimator.compute_wpli(trial, 8, 13)  # Alpha band
            all_connectivities.append(conn)
            energy = self.energy_analyzer.compute_energy(conn)
            all_energies.append(energy)
        
        corr, p_val, efficiencies = self.efficiency_analyzer.correlate_energy_efficiency(
            all_energies, all_connectivities
        )
        
        # 3. Reaction time correlation (if available)
        # rt_correlation = self.correlate_with_reaction_time(all_energies, reaction_times)
        
        return {
            'energy_by_condition': energy_results,
            'energy_efficiency_correlation': {'r': corr, 'p': p_val},
            'efficiencies': efficiencies,
            'energies': all_energies
        }
```

## Key Findings from Research

### 1. Emotion-Dependent Energy Differences

- **Sad processing**: Significantly lower (more negative) energy
- **Strongest effect**: Alpha band (Cohen's d ≈ 0.83, large effect)
- **Also significant**: Delta and theta bands

### 2. Energy-Efficiency Relationship

- Strong negative correlation (r ≈ -0.72)
- Hyperconnected, efficient networks → more stable states (lower energy)
- Supports attractor basin interpretation

### 3. Energy-Behavior Relationship

- Alpha-band energy correlates with reaction time during sad trials (r ≈ 0.61)
- Deeper network stability → increased cognitive effort
- Suggests sadness requires more processing resources

## Interpretation

### Attractor Basin Model

```
Emotional State Landscape:

Energy ↑
       |      ╱╲  Happiness (shallow basin)
       |     ╱  ╲___
       |    ╱        ╲
       |___╱          ╲___
       |   ╲    Sadness  ╲  (deep basin)
       |    ╲__ (stable) __╲
       |
       +----------------------→ State Space
```

- **Sadness**: Occupies a deeper, more stable attractor basin
- **Happiness**: Shallower basin, less stable configuration
- **Implication**: Sadness may be more "sticky" and harder to transition away from

## Applications

### 1. Clinical Assessment

```python
def assess_emotional_dysregulation(subject_eeg: np.ndarray, 
                                   baseline_energies: dict) -> dict:
    """
    Assess emotional dysregulation by comparing subject's energy profile
    to healthy baseline.
    
    Potential markers:
    - Atypical energy differences between emotions
    - Abnormal energy-efficiency relationships
    - Energy patterns that don't match behavioral responses
    """
    subject_analysis = EmotionEnergyLandscapeAnalysis()
    subject_results = subject_analysis.run_analysis(subject_eeg, [])
    
    # Compare to baseline
    deviations = {}
    for band in ['delta', 'theta', 'alpha']:
        baseline_diff = baseline_energies[band]['sad_mean'] - baseline_energies[band]['happy_mean']
        subject_diff = (subject_results['energy_by_condition'][band]['sad_mean'] - 
                       subject_results['energy_by_condition'][band]['happy_mean'])
        deviations[band] = subject_diff - baseline_diff
    
    return deviations
```

### 2. Brain-Computer Interfaces

- Real-time emotion state detection from EEG
- Neurofeedback for emotion regulation training
- Adaptive systems based on user's current emotional state stability

### 3. Cognitive Load Monitoring

- Energy metrics as proxy for cognitive effort
- Optimize task difficulty based on neural stability measures
- Fatigue detection in high-workload environments

## Best Practices

### Data Quality

1. **High-density EEG**: Use 64+ channels for accurate connectivity
2. **Artifact control**: Careful preprocessing to remove eye blinks, muscle noise
3. **Sufficient trials**: Minimum 20-30 trials per condition for statistical power
4. **Frequency specificity**: Analyze bands separately (delta, theta, alpha)

### Analysis Considerations

1. **Connectivity method**: wPLI recommended for artifact robustness
2. **Normalization**: Normalize activity vectors before energy computation
3. **Multiple comparisons**: Correct for testing across frequency bands
4. **Individual differences**: Consider baseline differences between subjects

### Limitations

1. **Spatial resolution**: EEG has limited spatial resolution compared to fMRI
2. **Volume conduction**: Use connectivity methods robust to zero-phase lag
3. **State interpretation**: Energy is a measure of stability, not valence directly
4. **Generalization**: Results may vary with different emotion induction methods

## References

- Paper: "Energy Landscapes of Emotion: Quantifying Brain Network Stability During Happy and Sad Face Processing Using EEG-Based Hopfield Energy" (arXiv:2603.27644v1, 2026)
- Authors: Barry Djibrina, Jiajia Li
- Related: Hopfield (1982), Stam et al. (wPLI), Rubinov & Sporns (network efficiency)

## Activation Keywords

- EEG Hopfield energy
- emotion energy landscape
- brain network stability
- affective neuroscience
- functional connectivity emotion
- wPLI emotion analysis
- neural attractor emotion
- emotional state dynamics
