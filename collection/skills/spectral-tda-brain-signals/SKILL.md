---
name: spectral-tda-brain-signals
description: 'Analyze brain connectivity using spectral Topological Data Analysis (STDA). Apply coherence-based filtration across frequency bands. Generate spectral landscapes for frequency-specific topological features.'
---

# Spectral TDA for Brain Signals

## Description

A frequency-specific topological data analysis approach that uses coherence (spectral domain dependence measure) to evaluate functional brain connectivity. Overcomes arbitrary threshold selection in standard TDA by using filtration across frequency bands. Introduces spectral landscape (2D generalization of persistence landscape) for capturing frequency-specific topological differences.

**Source:** arXiv:2401.05343v1
**Utility:** 0.91

## Activation Keywords

- spectral TDA
- coherence brain connectivity
- spectral landscape
- topological data analysis EEG
- frequency-specific brain networks
- ADHD EEG analysis
- persistence landscape 2D
- filtration brain connectivity

## Core Concepts

### 1. Limitations of Standard TDA

**Traditional TDA Problems:**
- Uses arbitrarily chosen threshold values
- Relies on simplistic connectivity measures (Pearson correlation)
- No information about specific oscillators driving dependence
- Cannot capture frequency-specific differences

**STDA Solution:**
- Frequency-specific approach using coherence
- Filtration across range of frequency bands
- Spectral domain dependence measure
- 2D spectral landscape captures nuanced information

### 2. Coherence-Based Connectivity

**Coherence Definition:**
```
C_xy(f) = |P_xy(f)|^2 / (P_x(f) * P_y(f))

where:
- P_xy(f): Cross-spectral density at frequency f
- P_x(f), P_y(f): Auto-spectral densities
- Range: [0, 1] (0 = no dependence, 1 = perfect dependence)
```

**Advantages over Correlation:**
| Metric | Domain | Information |
|--------|--------|-------------|
| Pearson correlation | Time | Overall linear dependence |
| Coherence | Frequency | Frequency-specific dependence |
| STDA | Frequency + Topology | Frequency-specific topology |

### 3. Spectral Filtration

**Filtration Process:**
```
1. Compute coherence matrix for each frequency band
2. Apply filtration across threshold values
3. Track topological features across filtration
4. Generate spectral landscape
```

**Frequency Bands:**
- Delta (1-4 Hz)
- Theta (4-8 Hz)
- Alpha (8-13 Hz)
- Beta (13-30 Hz)
- Gamma (30-100 Hz)

### 4. Spectral Landscape

**Definition:**
- 2D generalization of persistence landscape
- Captures topological features across frequency bands
- Novel topological summary for frequency-specific analysis

**Properties:**
| Feature | Persistence Landscape | Spectral Landscape |
|---------|----------------------|-------------------|
| Dimension | 1D | 2D |
| Information | Threshold filtration | Frequency + Threshold |
| Application | Standard TDA | Frequency-specific TDA |
| Summary | Persistence diagrams | Spectral topology |

## Step-by-Step Instructions

### 1. Coherence Computation

```python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class CoherenceConnectivity:
    """
    Compute frequency-specific coherence between EEG channels.
    
    Args:
        data: EEG data (channels x time)
        fs: Sampling frequency (Hz)
        freq_bands: Dictionary of frequency band ranges
    """
    def __init__(self, data, fs, freq_bands=None):
        self.data = data
        self.fs = fs
        self.freq_bands = freq_bands or {
            'delta': (1, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
        
    def compute_coherence(self, channel1, channel2):
        """
        Compute coherence between two channels.
        
        Args:
            channel1: Index of first channel
            channel2: Index of second channel
        
        Returns:
            freqs: Frequency array
            coh: Coherence values
        """
        # Compute cross-spectral density
        f, Pxy = signal.csd(
            self.data[channel1], 
            self.data[channel2],
            fs=self.fs,
            nperseg=min(256, len(self.data[channel1]))
        )
        
        # Compute auto-spectral densities
        _, Px = signal.welch(
            self.data[channel1],
            fs=self.fs,
            nperseg=min(256, len(self.data[channel1]))
        )
        _, Py = signal.welch(
            self.data[channel2],
            fs=self.fs,
            nperseg=min(256, len(self.data[channel2]))
        )
        
        # Coherence
        coh = np.abs(Pxy)**2 / (Px * Py)
        
        return f, coh
    
    def coherence_matrix(self, freq_band):
        """
        Compute coherence matrix for frequency band.
        
        Args:
            freq_band: Frequency band name
        
        Returns:
            coh_matrix: Coherence matrix (channels x channels)
        """
        f_low, f_high = self.freq_bands[freq_band]
        n_channels = len(self.data)
        coh_matrix = np.zeros((n_channels, n_channels))
        
        for i in range(n_channels):
            for j in range(n_channels):
                if i == j:
                    coh_matrix[i, j] = 1.0
                else:
                    freqs, coh = self.compute_coherence(i, j)
                    # Average coherence in frequency band
                    band_mask = (freqs >= f_low) & (freqs <= f_high)
                    coh_matrix[i, j] = np.mean(coh[band_mask])
        
        return coh_matrix
    
    def all_frequency_bands(self):
        """
        Compute coherence matrices for all frequency bands.
        
        Returns:
            matrices: Dictionary of coherence matrices
        """
        matrices = {}
        
        for band in self.freq_bands:
            matrices[band] = self.coherence_matrix(band)
        
        return matrices
```

### 2. Spectral Filtration

```python
class SpectralFiltration:
    """
    Apply filtration across threshold values for each frequency band.
    
    Args:
        coherence_matrices: Dictionary of coherence matrices
        threshold_range: Range of threshold values
    """
    def __init__(self, coherence_matrices, threshold_range=None):
        self.matrices = coherence_matrices
        self.threshold_range = threshold_range or np.linspace(0.1, 0.9, 20)
        
    def filtration_single_band(self, coh_matrix, threshold):
        """
        Apply threshold to coherence matrix.
        
        Args:
            coh_matrix: Coherence matrix
            threshold: Threshold value
        
        Returns:
            binary_matrix: Binary connectivity matrix
        """
        binary_matrix = (coh_matrix >= threshold).astype(int)
        return binary_matrix
    
    def filtration_all_thresholds(self, coh_matrix):
        """
        Apply filtration across all thresholds.
        
        Args:
            coh_matrix: Coherence matrix
        
        Returns:
            filtration: List of binary matrices
        """
        filtration = []
        
        for thresh in self.threshold_range:
            binary = self.filtration_single_band(coh_matrix, thresh)
            filtration.append(binary)
        
        return filtration
    
    def filtration_all_bands(self):
        """
        Apply filtration for all frequency bands.
        
        Returns:
            filtrations: Dictionary of filtrations
        """
        filtrations = {}
        
        for band, matrix in self.matrices.items():
            filtrations[band] = self.filtration_all_thresholds(matrix)
        
        return filtrations
```

### 3. Spectral Landscape

```python
class SpectralLandscape:
    """
    Generate 2D spectral landscape from filtrations.
    
    Args:
        filtrations: Dictionary of filtrations for frequency bands
        threshold_range: Threshold values
    """
    def __init__(self, filtrations, threshold_range):
        self.filtrations = filtrations
        self.thresholds = threshold_range
        self.frequency_bands = list(filtrations.keys())
        
    def compute_persistence_features(self, filtration):
        """
        Compute topological features from filtration.
        
        Args:
            filtration: List of binary connectivity matrices
        
        Returns:
            features: Dictionary of features (Betti numbers, etc.)
        """
        features = {
            'connected_components': [],
            'cycles': [],
            'density': []
        }
        
        for binary_matrix in filtration:
            # Number of connected components
            n_components = self.count_components(binary_matrix)
            features['connected_components'].append(n_components)
            
            # Density
            density = np.sum(binary_matrix) / binary_matrix.size
            features['density'].append(density)
        
        return features
    
    def count_components(self, binary_matrix):
        """
        Count connected components using BFS.
        
        Args:
            binary_matrix: Binary connectivity matrix
        
        Returns:
            n_components: Number of connected components
        """
        n = len(binary_matrix)
        visited = [False] * n
        
        def bfs(start):
            queue = [start]
            visited[start] = True
            while queue:
                node = queue.pop(0)
                for neighbor in range(n):
                    if binary_matrix[node, neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        
        n_components = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                n_components += 1
        
        return n_components
    
    def generate_landscape(self):
        """
        Generate 2D spectral landscape.
        
        Returns:
            landscape: 2D array (frequency bands x thresholds)
        """
        n_freqs = len(self.frequency_bands)
        n_thresh = len(self.thresholds)
        
        # Landscape components
        landscape_components = np.zeros((n_freqs, n_thresh))
        landscape_density = np.zeros((n_freqs, n_thresh))
        
        for i, band in enumerate(self.frequency_bands):
            features = self.compute_persistence_features(self.filtrations[band])
            landscape_components[i] = features['connected_components']
            landscape_density[i] = features['density']
        
        return {
            'components': landscape_components,
            'density': landscape_density,
            'frequency_bands': self.frequency_bands,
            'thresholds': self.thresholds
        }
    
    def plot_landscape(self, landscape):
        """
        Plot spectral landscape.
        
        Args:
            landscape: Landscape dictionary
        
        Returns:
            fig: Matplotlib figure
        """
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Connected components landscape
        ax1 = axes[0]
        im1 = ax1.imshow(
            landscape['components'],
            aspect='auto',
            cmap='viridis',
            extent=[landscape['thresholds'][0], landscape['thresholds'][-1], 
                    len(landscape['frequency_bands']), 0]
        )
        ax1.set_yticks(range(len(landscape['frequency_bands'])))
        ax1.set_yticklabels(landscape['frequency_bands'])
        ax1.set_xlabel('Threshold')
        ax1.set_ylabel('Frequency Band')
        ax1.set_title('Connected Components Landscape')
        plt.colorbar(im1, ax=ax1)
        
        # Density landscape
        ax2 = axes[1]
        im2 = ax2.imshow(
            landscape['density'],
            aspect='auto',
            cmap='plasma',
            extent=[landscape['thresholds'][0], landscape['thresholds'][-1], 
                    len(landscape['frequency_bands']), 0]
        )
        ax2.set_yticks(range(len(landscape['frequency_bands'])))
        ax2.set_yticklabels(landscape['frequency_bands'])
        ax2.set_xlabel('Threshold')
        ax2.set_ylabel('Frequency Band')
        ax2.set_title('Density Landscape')
        plt.colorbar(im2, ax=ax2)
        
        plt.tight_layout()
        return fig
```

### 4. ADHD Analysis Application

```python
class ADHDConnectivityAnalysis:
    """
    Analyze ADHD vs control connectivity using spectral TDA.
    
    Args:
        control_data: Control group EEG data
        adhd_data: ADHD group EEG data
        fs: Sampling frequency
    """
    def __init__(self, control_data, adhd_data, fs):
        self.control = control_data
        self.adhd = adhd_data
        self.fs = fs
        
    def compare_groups(self):
        """
        Compare spectral landscapes between groups.
        
        Returns:
            comparison: Dictionary of comparison results
        """
        # Compute coherence for both groups
        control_coh = CoherenceConnectivity(self.control, self.fs)
        adhd_coh = CoherenceConnectivity(self.adhd, self.fs)
        
        control_matrices = control_coh.all_frequency_bands()
        adhd_matrices = adhd_coh.all_frequency_bands()
        
        # Filtration
        threshold_range = np.linspace(0.1, 0.9, 20)
        control_filt = SpectralFiltration(control_matrices, threshold_range)
        adhd_filt = SpectralFiltration(adhd_matrices, threshold_range)
        
        control_filtrations = control_filt.filtration_all_bands()
        adhd_filtrations = adhd_filt.filtration_all_bands()
        
        # Landscapes
        control_landscape = SpectralLandscape(control_filtrations, threshold_range)
        adhd_landscape = SpectralLandscape(adhd_filtrations, threshold_range)
        
        control_result = control_landscape.generate_landscape()
        adhd_result = adhd_landscape.generate_landscape()
        
        # Comparison
        diff_components = control_result['components'] - adhd_result['components']
        diff_density = control_result['density'] - adhd_result['density']
        
        comparison = {
            'control': control_result,
            'adhd': adhd_result,
            'diff_components': diff_components,
            'diff_density': diff_density,
            'frequency_bands': control_result['frequency_bands'],
            'thresholds': control_result['thresholds']
        }
        
        return comparison
    
    def identify_frequency_differences(self, comparison):
        """
        Identify frequency bands with significant differences.
        
        Args:
            comparison: Comparison results
        
        Returns:
            significant_bands: List of bands with significant differences
        """
        diff_components = comparison['diff_components']
        
        # Find bands with largest differences
        band_diffs = np.mean(np.abs(diff_components), axis=1)
        
        threshold = np.mean(band_diffs) + np.std(band_diffs)
        significant_bands = [
            comparison['frequency_bands'][i]
            for i in range(len(band_diffs))
            if band_diffs[i] > threshold
        ]
        
        return significant_bands
```

### 5. Complete Workflow

```python
def spectral_tda_workflow(eeg_data, fs, group_labels=None):
    """
    Complete spectral TDA workflow for EEG analysis.
    
    Args:
        eeg_data: EEG data (subjects x channels x time)
        fs: Sampling frequency
        group_labels: Group labels (e.g., 'control', 'adhd')
    
    Returns:
        results: Analysis results
    """
    results = {}
    
    if group_labels is None:
        # Single group analysis
        coh_conn = CoherenceConnectivity(eeg_data, fs)
        matrices = coh_conn.all_frequency_bands()
        
        filt = SpectralFiltration(matrices)
        filtrations = filt.filtration_all_bands()
        
        landscape = SpectralLandscape(filtrations, filt.threshold_range)
        landscape_result = landscape.generate_landscape()
        
        fig = landscape.plot_landscape(landscape_result)
        
        results = {
            'coherence_matrices': matrices,
            'filtrations': filtrations,
            'landscape': landscape_result,
            'figure': fig
        }
        
    else:
        # Group comparison
        control_idx = [i for i, g in enumerate(group_labels) if g == 'control']
        adhd_idx = [i for i, g in enumerate(group_labels) if g == 'adhd']
        
        control_data = np.mean(eeg_data[control_idx], axis=0)
        adhd_data = np.mean(eeg_data[adhd_idx], axis=0)
        
        analysis = ADHDConnectivityAnalysis(control_data, adhd_data, fs)
        comparison = analysis.compare_groups()
        
        significant_bands = analysis.identify_frequency_differences(comparison)
        
        results = {
            'comparison': comparison,
            'significant_bands': significant_bands
        }
    
    return results
```

## Tools Used

- `numpy` - Numerical computations
- `scipy.signal` - Coherence computation
- `matplotlib` - Landscape visualization
- `exec` - Run analysis scripts
- `read` - Load EEG data

## Example Use Cases

### 1. Basic Spectral TDA

```python
# Load EEG data
import numpy as np
eeg_data = np.random.randn(64, 1000)  # 64 channels, 1000 samples
fs = 250  # Hz

# Run spectral TDA
results = spectral_tda_workflow(eeg_data, fs)

# Plot landscape
results['figure'].show()
```

### 2. ADHD Analysis

```python
# Group comparison
eeg_data = np.random.randn(20, 64, 1000)  # 20 subjects
group_labels = ['control'] * 10 + ['adhd'] * 10

results = spectral_tda_workflow(eeg_data, fs, group_labels)

print(f"Significant frequency bands: {results['significant_bands']}")
```

### 3. Coherence Matrix Visualization

```python
# Compute coherence
coh = CoherenceConnectivity(eeg_data, fs)
alpha_matrix = coh.coherence_matrix('alpha')

# Plot
plt.imshow(alpha_matrix, cmap='viridis')
plt.colorbar()
plt.title('Alpha Band Coherence')
plt.show()
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Coherence Computation

## Examples

### Example 1: Basic Application

**User:** I need to apply Spectral TDA for Brain Signals to my analysis.

**Agent:** I'll help you apply spectral-tda-brain-signals. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for spectral-tda-brain-signals?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `brain-graph-augmentation-template` - Brain network analysis
- `eeg-brain-connectivity-bci` - EEG connectivity
- `time-varying-brain-connectivity` - Dynamic connectivity

## References

- El-Yaagoubi, A. B. et al. (2023). "Spectral Topological Data Analysis of Brain Signals" arXiv:2401.05343v1 [q-bio.NC]

---

**Created:** 2026-03-29 22:05
**Author:** Aerial (from arXiv:2401.05343v1)