# Self-Sustained Neuron Population Modeling — Implementation Patterns

## 1. Hodgkin-Huxley Neuron Model

```python
import numpy as np

class HodgkinHuxleyNeuron:
    """
    Hodgkin-Huxley neuron with intrinsic stochasticity.
    """
    def __init__(self, is_excitatory=True):
        # Membrane capacitance
        self.C_m = 1.0  # uF/cm^2
        
        # Max conductances
        self.g_Na = 120.0  # mS/cm^2
        self.g_K = 36.0    # mS/cm^2
        self.g_L = 0.3     # mS/cm^2
        
        # Reversal potentials
        self.E_Na = 50.0   # mV
        self.E_K = -77.0   # mV
        self.E_L = -54.387 # mV
        
        # Initial conditions
        self.V = -65.0     # mV
        self.m = 0.05
        self.h = 0.6
        self.n = 0.32
        
        self.is_excitatory = is_excitatory
        self.spike_threshold = 0.0  # mV crossing
        self.last_spike_time = -np.inf
    
    def gating_rates(self, V):
        """Compute alpha and beta rates for gating variables."""
        # Sodium activation (m)
        alpha_m = 0.1 * (25 - V) / (np.exp((25 - V) / 10) - 1)
        beta_m = 4.0 * np.exp(-V / 18)
        
        # Sodium inactivation (h)
        alpha_h = 0.07 * np.exp(-V / 20)
        beta_h = 1.0 / (np.exp((30 - V) / 10) + 1)
        
        # Potassium activation (n)
        alpha_n = 0.01 * (10 - V) / (np.exp((10 - V) / 10) - 1)
        beta_n = 0.125 * np.exp(-V / 80)
        
        return (alpha_m, beta_m), (alpha_h, beta_h), (alpha_n, beta_n)
    
    def step(self, I_ext, dt=0.05):
        """
        Advance neuron by one time step with stochastic ion channels.
        """
        (a_m, b_m), (a_h, b_h), (a_n, b_n) = self.gating_rates(self.V)
        
        # Deterministic gating updates
        dm = (a_m * (1 - self.m) - b_m * self.m) * dt
        dh = (a_h * (1 - self.h) - b_h * self.h) * dt
        dn = (a_n * (1 - self.n) - b_n * self.n) * dt
        
        # Add intrinsic stochasticity to gating variables
        noise_scale = 0.01
        dm += noise_scale * np.random.randn() * np.sqrt(dt)
        dh += noise_scale * np.random.randn() * np.sqrt(dt)
        dn += noise_scale * np.random.randn() * np.sqrt(dt)
        
        self.m = np.clip(self.m + dm, 0, 1)
        self.h = np.clip(self.h + dh, 0, 1)
        self.n = np.clip(self.n + dn, 0, 1)
        
        # Ionic currents
        I_Na = self.g_Na * self.m**3 * self.h * (self.V - self.E_Na)
        I_K = self.g_K * self.n**4 * (self.V - self.E_K)
        I_L = self.g_L * (self.V - self.E_L)
        
        # Membrane potential update
        dV = (I_ext - I_Na - I_K - I_L) / self.C_m * dt
        
        self.V += dV
        
        # Detect spike
        spike = False
        if self.V > self.spike_threshold and not hasattr(self, '_spiked'):
            spike = True
            self._spiked = True
            self.last_spike_time = self.V
        elif self.V < -40:
            self._spiked = False
        
        return spike
```

## 2. Recurrent Network with STDP and Stochastic Synapses

```python
class RecurrentHHNetwork:
    """
    Recurrent network of Hodgkin-Huxley neurons with:
    - 80/20 E/I ratio
    - 80% connection probability
    - Excitatory and inhibitory STDP
    - Probabilistic vesicle release
    - Probabilistic synapse formation
    - Receptor variability
    - Voltage-dependent inhibition
    """
    def __init__(self, n_exc=160, n_inh=40, connection_prob=0.8):
        self.n_exc = n_exc
        self.n_inh = n_inh
        self.n_neurons = n_exc + n_inh
        self.connection_prob = connection_prob
        
        # Create neurons
        self.neurons = []
        for i in range(n_exc):
            self.neurons.append(HodgkinHuxleyNeuron(is_excitatory=True))
        for i in range(n_inh):
            self.neurons.append(HodgkinHuxleyNeuron(is_excitatory=False))
        
        # Synaptic connectivity and weights
        self._build_connectivity()
        
        # STDP parameters
        self.stdp_tau_plus = 20.0   # ms
        self.stdp_tau_minus = 20.0  # ms
        self.stdp_eta_exc = 0.001   # excitatory learning rate
        self.stdp_eta_inh = 0.001   # inhibitory learning rate
        
        # Vesicle release probability
        self.p_release = 0.5
        
        # Spike trace for STDP
        self.spike_traces = np.zeros(self.n_neurons)
    
    def _build_connectivity(self):
        """Build recurrent connectivity with 80% probability."""
        self.adjacency = np.zeros((self.n_neurons, self.n_neurons))
        self.weights = np.zeros((self.n_neurons, self.n_neurons))
        
        for i in range(self.n_neurons):
            for j in range(self.n_neurons):
                if i != j and np.random.rand() < self.connection_prob:
                    self.adjacency[i, j] = 1.0
                    # Initialize with receptor variability
                    self.weights[i, j] = np.random.uniform(0.1, 0.5)
    
    def compute_synaptic_current(self, neuron_idx, V_pre, V_post):
        """
        Compute synaptic current with probabilistic release and 
        voltage-dependent inhibition.
        """
        I_syn = 0.0
        
        for j in range(self.n_neurons):
            if self.adjacency[neuron_idx, j] == 0:
                continue
            
            # Probabilistic vesicle release
            if np.random.rand() > self.p_release:
                continue
            
            w = self.weights[neuron_idx, j]
            
            if self.neurons[j].is_excitatory:
                # Excitatory synapse
                I_syn += w * (V_post - 0.0)  # E_rev = 0 mV
            else:
                # Voltage-dependent inhibition
                # Inhibition strength depends on postsynaptic voltage
                voltage_factor = 1.0 / (1.0 + np.exp((V_post + 60) / 5))
                I_syn -= w * voltage_factor * (V_post + (-80))  # E_rev = -80 mV
        
        return I_syn
    
    def apply_stdp(self, pre_idx, post_idx, dt):
        """
        Apply STDP rule for both excitatory and inhibitory synapses.
        """
        if self.adjacency[pre_idx, post_idx] == 0:
            return
        
        pre_is_exc = self.neurons[pre_idx].is_excitatory
        eta = self.stdp_eta_exc if pre_is_exc else self.stdp_eta_inh
        
        # Compute time difference
        delta_t = (self.neurons[post_idx].last_spike_time - 
                   self.neurons[pre_idx].last_spike_time)
        
        if delta_t > 0:
            # Pre before post: potentiation
            dw = eta * np.exp(-delta_t / self.stdp_tau_plus)
        else:
            # Post before pre: depression
            dw = -eta * np.exp(delta_t / self.stdp_tau_minus)
        
        self.weights[post_idx, pre_idx] += dw
        self.weights[post_idx, pre_idx] = np.clip(
            self.weights[post_idx, pre_idx], 0, 1.0)
    
    def step(self, I_ext, dt=0.05):
        """Advance the entire network by one time step."""
        spikes = []
        currents = []
        
        # Compute synaptic currents
        for i in range(self.n_neurons):
            V_pre = self.neurons[i].V
            I_syn = self.compute_synaptic_current(
                i, V_pre, self.neurons[i].V)
            currents.append(I_syn)
        
        # Update neurons
        for i in range(self.n_neurons):
            I_total = I_ext[i] + currents[i]
            spike = self.neurons[i].step(I_total, dt)
            spikes.append(spike)
        
        # Apply STDP for all spike pairs
        for i in range(self.n_neurons):
            if spikes[i]:
                for j in range(self.n_neurons):
                    self.apply_stdp(j, i, dt)
        
        return spikes
```

## 3. Initialization Stimulus and Autonomous Simulation

```python
def initialize_and_run(n_exc=160, n_inh=40, 
                       init_duration_ms=200, 
                       run_duration_ms=1_800_000,
                       dt=0.05):
    """
    Run network with brief initialization followed by autonomous operation.
    
    Args:
        init_duration_ms: Duration of initial stimulus (200 ms)
        run_duration_ms: Duration of autonomous simulation (1,800,000 ms = 1800 s)
        dt: Time step in ms
        
    Returns:
        raster: Spike raster array
        firing_rates: Mean firing rate per neuron
        fano_factors: Population Fano factors
    """
    network = RecurrentHHNetwork(n_exc=n_exc, n_inh=n_inh)
    
    total_steps = int((init_duration_ms + run_duration_ms) / dt)
    n_neurons = n_exc + n_inh
    
    raster = np.zeros((n_neurons, total_steps))
    init_steps = int(init_duration_ms / dt)
    
    # Apply brief stimulus to 30 excitatory neurons
    stimulus_strength = 10.0  # uA/cm^2
    
    for t in range(total_steps):
        I_ext = np.zeros(n_neurons)
        
        if t < init_steps:
            # Stimulate 30 randomly selected excitatory neurons
            stimulated = np.random.choice(n_exc, size=30, replace=False)
            I_ext[stimulated] = stimulus_strength
        
        # Run network step (no external input after initialization)
        spikes = network.step(I_ext, dt)
        raster[:, t] = spikes
    
    # Compute firing rates
    run_steps = total_steps - init_steps
    firing_rates = raster[:, init_steps:].mean(axis=1) / dt * 1000  # Hz
    
    # Compute Fano factors
    window_size = int(1000 / dt)  # 1 second windows
    spike_counts = []
    for start in range(init_steps, total_steps - window_size, window_size):
        counts = raster[:, start:start+window_size].sum(axis=1)
        spike_counts.append(counts)
    
    spike_counts = np.array(spike_counts)
    fano_factors = spike_counts.var(axis=0) / (spike_counts.mean(axis=0) + 1e-8)
    
    return {
        'raster': raster,
        'firing_rates': firing_rates,
        'fano_factors': fano_factors,
        'mean_rate': firing_rates.mean(),
        'std_rate': firing_rates.std(),
        'low_rate_fraction': (firing_rates < 1.0).mean(),  # Should be ~67%
    }
```

## 4. Analysis: Population Activity Patterns

```python
def analyze_autonomous_activity(results):
    """
    Analyze self-sustained activity patterns.
    
    Expected results:
    - 67% of neurons below 1 Hz
    - Population mean ~1.13 Hz
    - Fano factors near 1-2
    """
    rates = results['firing_rates']
    fano = results['fano_factors']
    
    print(f"Population mean firing rate: {rates.mean():.2f} ± {rates.std():.2f} Hz")
    print(f"Fraction of neurons < 1 Hz: {results['low_rate_fraction']:.1%}")
    print(f"Mean Fano factor: {fano.mean():.2f}")
    
    # Check for sparse, irregular activity
    is_sparse = results['low_rate_fraction'] > 0.5
    is_irregular = 1.0 <= fano.mean() <= 2.0
    is_self_sustained = rates.mean() > 0.5
    
    print(f"Sparse activity: {is_sparse}")
    print(f"Irregular spike timing: {is_irregular}")
    print(f"Self-sustained: {is_self_sustained}")
    
    return {
        'sparse': is_sparse,
        'irregular': is_irregular,
        'self_sustained': is_self_sustained
    }

def detect_pattern_reorganizations(raster, window_ms=10000, dt=0.05):
    """
    Detect spontaneous qualitative reorganizations in collective firing patterns.
    """
    window_steps = int(window_ms / dt)
    n_windows = raster.shape[1] // window_steps
    
    patterns = []
    for w in range(n_windows):
        start = w * window_steps
        end = (w + 1) * window_steps
        # Population firing pattern for this window
        pattern = raster[:, start:end].mean(axis=1)
        patterns.append(pattern)
    
    # Compute pairwise similarity between windows
    patterns = np.array(patterns)
    similarity = np.corrcoef(patterns)
    
    # Detect change points
    diff = np.diag(similarity, k=1)
    change_points = np.where(diff < np.percentile(diff, 10))[0]
    
    return {
        'patterns': patterns,
        'similarity': similarity,
        'change_points': change_points,
        'n_reorganizations': len(change_points)
    }
```

## References

- Paper: "Modeling of Self-sustained Neuron Population without External Stimulus" (2604.13719v1)
- Hodgkin, A.L. & Huxley, A.F. (1952), "A quantitative description of membrane current"
- STDP: Bi and Poo (2001), "Synaptic Modification by Correlated Activity"
