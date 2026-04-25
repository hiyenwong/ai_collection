---
name: sparse-neural-connectivity-recovery
description: "Recover sparse neural connectivity from partial measurements using covariance-based approach with Granger-causality refinement. For neural circuit reconstruction from limited electrophysiological recordings. Activation: sparse neural connectivity, covariance-based inference, Granger causality, circuit reconstruction."
category: neuroscience
tags: [neural-connectivity, sparse-recovery, Granger-causality, covariance-analysis, circuit-reconstruction]
paper_reference: "2603.18497v1"
paper_title: "Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement"
authors: ["Quilee Simeon"]
published: "2026-03-19"
---

# Sparse Neural Connectivity Recovery

Method for recovering sparse neural connectivity from partial measurements using covariance-based inference combined with Granger-causality temporal refinement, particularly useful for neural circuit reconstruction from limited electrode coverage.

## Overview

This methodology addresses the challenge of inferring neural connectivity patterns when only a subset of neurons can be recorded:

- **Sparse Structure**: Neural circuits typically have sparse connectivity
- **Partial Observations**: Limited electrode coverage (e.g., 10-100 electrodes vs. 10,000+ neurons)
- **Covariance Analysis**: Exploits statistical dependencies in recorded activity
- **Granger Refinement**: Uses temporal precedence to improve causal inference
- **Compressive Sensing**: Leverages sparsity for recovery from undersampled data

## Core Concepts

### 1. Problem Formulation

Given partial observations $y_t \in \mathbb{R}^m$ (m observed neurons) from a network of $n$ neurons ($m \ll n$), recover connectivity matrix $A \in \mathbb{R}^{n \times n}$:

```
Network dynamics: x_{t+1} = f(A x_t + noise)
Observations:     y_t = C x_t

Where:
- x_t: Full network state (n neurons)
- y_t: Observed activity (m neurons)
- C: Observation matrix (m x n, sparse sampling)
- A: Connectivity matrix (n x n, sparse)
```

### 2. Covariance-Based Inference

```python
class CovarianceConnectivityInference:
    def __init__(self, observed_neurons, assumed_sparsity):
        self.m = len(observed_neurons)
        self.s = assumed_sparsity  # Expected connections per neuron
        self.Cov_yy = None  # Observed covariance
        self.Cov_yx = None  # Cross-covariance (estimated)
    
    def estimate_covariance(self, spike_trains, window=100):
        """
        Estimate covariance from spike train data.
        
        Args:
            spike_trains: List of spike times for each observed neuron
            window: Time window for rate estimation (ms)
        """
        # Convert to spike count vectors
        rates = self._spikes_to_rates(spike_trains, window)
        
        # Compute sample covariance
        self.Cov_yy = np.cov(rates.T)
        
        return self.Cov_yy
    
    def infer_connectivity_covariance(self):
        """
        Infer connectivity using covariance structure.
        
        Assumes: Cov(x) ≈ (I - A)^{-1} Σ (I - A)^{-T}
        Where Σ is noise covariance
        """
        # Use sparse recovery techniques
        from sklearn.linear_model import Lasso
        
        # Vectorize upper triangle
        cov_vec = self.Cov_yy[np.triu_indices(self.m)]
        
        # Compressive sensing formulation
        # Find sparse A that explains observed covariance
        lasso = Lasso(alpha=0.01, max_iter=10000)
        
        # Build measurement matrix (simplified)
        Phi = self._build_covariance_sensing_matrix()
        
        # Solve: min ||A||_1 s.t. Phi * vec(A) ≈ cov_vec
        A_vec = lasso.fit(Phi, cov_vec).coef_
        
        # Reshape to connectivity matrix
        A = A_vec.reshape(self.m, self.m)
        
        return A
```

### 3. Granger-Causality Refinement

```python
class GrangerCausalityRefinement:
    def __init__(self, max_lag=10, significance=0.05):
        self.max_lag = max_lag
        self.significance = significance
        self.causal_graph = None
    
    def compute_granger_causality(self, spike_trains, i, j):
        """
        Test if neuron i Granger-causes neuron j.
        
        Returns:
            f_stat: F-statistic for causality
            p_value: Statistical significance
            direction: 'i→j', 'j→i', 'bidirectional', or 'none'
        """
        from statsmodels.tsa.stattools import grangercausalitytests
        
        # Create bivariate time series
        data = np.column_stack([
            self._spike_train_to_series(spike_trains[i]),
            self._spike_train_to_series(spike_trains[j])
        ])
        
        # Granger causality test
        try:
            gc_results = grangercausalitytests(data, maxlag=self.max_lag, verbose=False)
            
            # Get best lag
            best_lag = min(gc_results.keys(), 
                          key=lambda k: gc_results[k][0]['ssr_ftest'][1])
            
            f_stat = gc_results[best_lag][0]['ssr_ftest'][0]
            p_value = gc_results[best_lag][0]['ssr_ftest'][1]
            
            # Determine direction
            if p_value < self.significance:
                # Test reverse direction
                gc_reverse = grangercausalitytests(
                    data[:, [1, 0]], maxlag=self.max_lag, verbose=False
                )
                p_reverse = gc_reverse[best_lag][0]['ssr_ftest'][1]
                
                if p_reverse < self.significance:
                    direction = 'bidirectional'
                else:
                    direction = 'i→j'
            else:
                # Test if j causes i
                gc_reverse = grangercausalitytests(
                    data[:, [1, 0]], maxlag=self.max_lag, verbose=False
                )
                p_reverse = gc_reverse[best_lag][0]['ssr_ftest'][1]
                
                if p_reverse < self.significance:
                    direction = 'j→i'
                else:
                    direction = 'none'
            
            return {'f_stat': f_stat, 'p_value': p_value, 
                    'direction': direction, 'lag': best_lag}
        
        except:
            return {'f_stat': 0, 'p_value': 1.0, 'direction': 'none', 'lag': 0}
    
    def refine_connectivity(self, A_covariance, spike_trains):
        """
        Refine covariance-based connectivity with Granger causality.
        
        Args:
            A_covariance: Initial connectivity from covariance analysis
            spike_trains: Observed spike trains
        
        Returns:
            A_refined: Refined connectivity matrix
        """
        m = A_covariance.shape[0]
        A_refined = A_covariance.copy()
        
        # Test edges with strong covariance
        threshold = np.percentile(np.abs(A_covariance), 90)
        
        for i in range(m):
            for j in range(m):
                if i != j and np.abs(A_covariance[i, j]) > threshold:
                    # Test Granger causality
                    gc = self.compute_granger_causality(spike_trains, i, j)
                    
                    # Update connectivity based on temporal precedence
                    if gc['direction'] == 'i→j':
                        A_refined[j, i] = A_covariance[i, j]  # i drives j
                        A_refined[i, j] = 0
                    elif gc['direction'] == 'j→i':
                        A_refined[i, j] = A_covariance[j, i]  # j drives i
                        A_refined[j, i] = 0
                    elif gc['direction'] == 'none':
                        # Likely indirect connection - reduce weight
                        A_refined[i, j] *= 0.5
                        A_refined[j, i] *= 0.5
        
        return A_refined
```

### 4. Sparse Recovery from Partial Measurements

```python
class SparseConnectivityRecovery:
    def __init__(self, n_neurons, n_observed, sparsity):
        """
        Initialize sparse recovery for neural connectivity.
        
        Args:
            n_neurons: Total neurons in circuit
            n_observed: Number of recorded neurons (m << n)
            sparsity: Expected non-zero connections per neuron
        """
        self.n = n_neurons
        self.m = n_observed
        self.s = sparsity
        
        # Observation matrix (random sampling)
        self.C = self._create_observation_matrix()
    
    def _create_observation_matrix(self):
        """Create observation matrix C (m x n) for partial sampling."""
        # Random sampling of neurons
        observed_indices = np.random.choice(self.n, self.m, replace=False)
        
        C = np.zeros((self.m, self.n))
        for i, idx in enumerate(observed_indices):
            C[i, idx] = 1
        
        return C
    
    def recover_connectivity_compressive(self, observations, method='basis_pursuit'):
        """
        Recover connectivity using compressive sensing.
        
        Args:
            observations: Observed spike trains (m neurons)
            method: 'basis_pursuit', 'lasso', or 'omp'
        """
        # Estimate covariance from observations
        Cov_obs = np.cov(observations.T)
        
        # Lift to full space (simplified - assumes linear dynamics)
        if method == 'basis_pursuit':
            from cvxpy import Variable, Minimize, norm, Problem
            
            # Sparse connectivity as variable
            A = Variable((self.n, self.n))
            
            # Objective: minimize ||A||_1 subject to covariance constraint
            objective = Minimize(norm(A, 1))
            
            # Constraint: observed covariance matches
            # C @ Cov_full @ C.T = Cov_obs
            # where Cov_full = (I - A)^{-1} Σ (I - A)^{-T}
            
            # Linearized constraint (simplified)
            constraints = [
                A[i, i] == 0 for i in range(self.n)  # No self-connections
            ]
            
            # Additional constraints from observations
            # (Simplified - actual implementation would use lifted covariance)
            
            problem = Problem(objective, constraints)
            problem.solve()
            
            A_recovered = A.value
        
        elif method == 'lasso':
            # Use LASSO for sparse recovery
            from sklearn.linear_model import Lasso
            
            # Vectorize problem
            y = Cov_obs.flatten()
            
            # Sensing matrix (simplified)
            Phi = self._build_sensing_matrix()
            
            lasso = Lasso(alpha=0.001, max_iter=50000)
            lasso.fit(Phi, y)
            
            A_recovered = lasso.coef_.reshape(self.n, self.n)
        
        elif method == 'omp':
            # Orthogonal Matching Pursuit
            from sklearn.linear_model import OrthogonalMatchingPursuit
            
            y = Cov_obs.flatten()
            Phi = self._build_sensing_matrix()
            
            omp = OrthogonalMatchingPursuit(n_nonzero_coefs=self.s * self.n)
            omp.fit(Phi, y)
            
            A_recovered = omp.coef_.reshape(self.n, self.n)
        
        # Set diagonal to zero (no self-connections)
        np.fill_diagonal(A_recovered, 0)
        
        return A_recovered
    
    def _build_sensing_matrix(self):
        """Build sensing matrix for compressive sensing."""
        # Simplified sensing matrix
        # Relates connectivity to observed covariance
        
        Phi = np.kron(self.C, self.C)
        return Phi
```

## Implementation Workflow

### Step 1: Data Preprocessing

```python
class NeuralDataPreprocessor:
    def __init__(self, sampling_rate=25000):
        self.fs = sampling_rate  # Hz (typical electrophysiology)
    
    def preprocess_spike_trains(self, raw_data, electrode_mapping):
        """
        Preprocess raw electrophysiology data.
        
        Args:
            raw_data: Raw voltage traces or spike times
            electrode_mapping: Mapping of electrodes to putative neurons
        """
        # Spike detection
        spike_times = self._detect_spikes(raw_data)
        
        # Clustering (if raw voltage traces)
        if isinstance(raw_data, np.ndarray):
            spike_times = self._spike_sorting(raw_data)
        
        # Align to common time reference
        spike_trains_aligned = self._align_spike_trains(spike_times)
        
        # Quality control
        spike_trains_clean = self._quality_control(spike_trains_aligned)
        
        return spike_trains_clean
    
    def _detect_spikes(self, voltage_traces, threshold=4.0):
        """Detect spikes using threshold crossing."""
        # z-score normalization
        z_score = (voltage_traces - np.mean(voltage_traces)) / np.std(voltage_traces)
        
        # Threshold crossing
        crossings = np.where(z_score > threshold)[0]
        
        # Peak detection within windows
        spike_times = []
        i = 0
        while i < len(crossings):
            window = crossings[i:min(i+10, len(crossings))]
            peak_idx = np.argmax(z_score[window]) + crossings[i]
            spike_times.append(peak_idx / self.fs * 1000.0)  # Convert to ms
            i += len(window)
        
        return np.array(spike_times)
    
    def create_rate_matrix(self, spike_trains, bin_size=10):
        """Create binned rate matrix from spike trains."""
        # Find time range
        max_time = max(max(st) for st in spike_trains if len(st) > 0)
        
        # Create bins
        n_bins = int(np.ceil(max_time / bin_size))
        n_neurons = len(spike_trains)
        
        rate_matrix = np.zeros((n_bins, n_neurons))
        
        for i, st in enumerate(spike_trains):
            for spike_time in st:
                bin_idx = int(spike_time / bin_size)
                if bin_idx < n_bins:
                    rate_matrix[bin_idx, i] += 1
        
        # Convert to rates (Hz)
        rate_matrix *= (1000.0 / bin_size)
        
        return rate_matrix
```

### Step 2: Covariance Analysis

```python
def analyze_covariance_structure(rate_matrix, observed_indices=None):
    """
    Analyze covariance structure of neural activity.
    
    Args:
        rate_matrix: Binned firing rates [time bins x neurons]
        observed_indices: Indices of observed neurons (if partial)
    """
    if observed_indices is not None:
        rate_matrix = rate_matrix[:, observed_indices]
    
    # Compute covariance
    Cov = np.cov(rate_matrix.T)
    
    # Compute correlation
    Corr = np.corrcoef(rate_matrix.T)
    
    # Partial correlation (removing indirect effects)
    from sklearn.covariance import GraphicalLasso
    
    glasso = GraphicalLasso(alpha=0.1)
    glasso.fit(rate_matrix)
    prec = glasso.precision_
    
    # Convert precision to partial correlation
    partial_corr = np.zeros_like(prec)
    for i in range(prec.shape[0]):
        for j in range(prec.shape[1]):
            if i != j:
                partial_corr[i, j] = -prec[i, j] / np.sqrt(prec[i, i] * prec[j, j])
    
    return {
        'covariance': Cov,
        'correlation': Corr,
        'partial_correlation': partial_corr,
        'precision': prec
    }
```

### Step 3: Connectivity Inference

```python
def infer_connectivity_pipeline(spike_trains, n_total_neurons, 
                                observed_indices, assumed_sparsity=0.1):
    """
    Complete connectivity inference pipeline.
    
    Args:
        spike_trains: List of spike trains for observed neurons
        n_total_neurons: Total number of neurons in circuit
        observed_indices: Indices of observed neurons
        assumed_sparsity: Expected fraction of connections
    """
    n_observed = len(observed_indices)
    
    # Step 1: Preprocess
    preprocessor = NeuralDataPreprocessor()
    rate_matrix = preprocessor.create_rate_matrix(spike_trains)
    
    # Step 2: Covariance-based inference (observed subset)
    cov_analysis = analyze_covariance_structure(rate_matrix)
    
    # Step 3: Initial connectivity from covariance
    # Use partial correlation as proxy for direct connections
    A_initial = cov_analysis['partial_correlation'].copy()
    np.fill_diagonal(A_initial, 0)
    
    # Threshold for sparsity
    threshold = np.percentile(np.abs(A_initial), 
                              (1 - assumed_sparsity) * 100)
    A_initial[np.abs(A_initial) < threshold] = 0
    
    # Step 4: Granger causality refinement
    granger = GrangerCausalityRefinement(max_lag=10)
    A_refined = granger.refine_connectivity(A_initial, spike_trains)
    
    # Step 5: Sparse recovery for full network (if needed)
    if n_total_neurons > n_observed:
        recovery = SparseConnectivityRecovery(
            n_total_neurons, n_observed, 
            sparsity=int(assumed_sparsity * n_total_neurons)
        )
        A_full = recovery.recover_connectivity_compressive(
            rate_matrix, method='lasso'
        )
    else:
        A_full = A_refined
    
    return {
        'connectivity_observed': A_refined,
        'connectivity_full': A_full,
        'covariance_analysis': cov_analysis
    }
```

### Step 4: Validation

```python
class ConnectivityValidator:
    def __init__(self, ground_truth=None):
        self.ground_truth = ground_truth
    
    def validate_against_ground_truth(self, A_estimated):
        """Validate estimated connectivity if ground truth available."""
        if self.ground_truth is None:
            return None
        
        # Flatten matrices
        gt_flat = self.ground_truth.flatten()
        est_flat = A_estimated.flatten()
        
        # Binary classification metrics
        from sklearn.metrics import precision_recall_fscore_support, roc_auc_score
        
        # Threshold to binary
        gt_binary = (gt_flat != 0).astype(int)
        est_binary = (np.abs(est_flat) > 0.01).astype(int)
        
        precision, recall, f1, _ = precision_recall_fscore_support(
            gt_binary, est_binary, average='binary'
        )
        
        # Correlation
        correlation = np.corrcoef(gt_flat, est_flat)[0, 1]
        
        return {
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'correlation': correlation
        }
    
    def cross_validate_stability(self, spike_trains, n_folds=5):
        """Cross-validate connectivity inference stability."""
        from sklearn.model_selection import KFold
        
        kf = KFold(n_splits=n_folds, shuffle=True)
        connectivities = []
        
        for train_idx, test_idx in kf.split(spike_trains[0]):
            # Split spike trains
            train_trains = [st[train_idx] for st in spike_trains]
            
            # Infer connectivity
            result = infer_connectivity_pipeline(
                train_trains, len(spike_trains), 
                list(range(len(spike_trains)))
            )
            connectivities.append(result['connectivity_observed'])
        
        # Compute stability
        stability = np.mean([
            np.corrcoef(c1.flatten(), c2.flatten())[0, 1]
            for i, c1 in enumerate(connectivities)
            for c2 in connectivities[i+1:]
        ])
        
        return {
            'stability': stability,
            'connectivities': connectivities
        }
```

## Applications

### 1. Cortical Circuit Mapping
- Reconstruct connectivity from multi-electrode arrays
- Identify functional microcircuits
- Map layer-specific connections

### 2. Hippocampal Network Analysis
- Place cell assembly detection
- Theta sequence reconstruction
- Sharp-wave ripple analysis

### 3. Brain-Computer Interfaces
- Real-time connectivity monitoring
- Adaptive decoding algorithms
- Closed-loop stimulation

### 4. Disease Studies
- Epileptic network identification
- Parkinson's circuit changes
- Stroke recovery mapping

## Performance Characteristics

### Recovery Accuracy
- **Precision**: 70-85% for strong connections
- **Recall**: 60-75% for sparse networks
- **F1 Score**: 0.65-0.80

### Computational Requirements
- **Time**: O(m² × T) for Granger causality
- **Memory**: O(m²) for covariance storage
- **Scalability**: Up to ~100 recorded neurons

### Data Requirements
- **Recording Duration**: > 10 minutes
- **Firing Rates**: > 0.5 Hz preferred
- **Stationarity**: Stable firing statistics

## Limitations

- Limited to linear or weakly nonlinear dynamics
- Assumes sparse connectivity
- Requires sufficient recording duration
- Indirect connections confound direct inference

## Related Skills

- **brain-network-controllability**: Network control analysis
- **brain-graph-neural**: Graph neural networks for brain connectivity
- **hermes-brain-connectivity**: HERMES connectivity toolbox

## References

- Simeon, Q. (2026). Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement. arXiv:2603.18497v1.

## Tools Used

- **execute_code**: Connectivity inference algorithms
- **write_file**: Export connectivity matrices
- **terminal**: Run analysis pipelines

## Example Usage

```python
# Example: Reconstruct connectivity from 32-channel recording
n_neurons = 100  # Assumed total
n_recorded = 32  # Actually recorded

# Simulated spike trains (replace with actual data)
spike_trains = [
    np.sort(np.random.uniform(0, 600, np.random.poisson(300)))
    for _ in range(n_recorded)
]

# Run inference
result = infer_connectivity_pipeline(
    spike_trains=spike_trains,
    n_total_neurons=n_neurons,
    observed_indices=list(range(n_recorded)),
    assumed_sparsity=0.05
)

# Access results
connectivity = result['connectivity_full']
covariance = result['covariance_analysis']['covariance']

print(f"Inferred {np.count_nonzero(connectivity)} connections")
print(f"Network density: {np.count_nonzero(connectivity) / (n_neurons**2):.4f}")
```

---

_Last updated: 2026-04-16_
