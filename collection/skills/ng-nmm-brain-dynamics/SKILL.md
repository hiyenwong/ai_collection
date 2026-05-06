---
name: ng-nmm-brain-dynamics
description: "Next Generation Neural Mass Models (NG-NMM) for emergent spatiotemporal dynamics in large-scale brain networks. Captures exact macroscopic gamma activity of coupled excitatory/inhibitory populations with Master Stability Function analysis. Activation triggers: neural mass model, NG-NMM, spatiotemporal dynamics, brain network, gamma oscillations, PING mechanism, whole-brain model."
---

# Next Generation Neural Mass Models for Brain Dynamics

> Emergent spatiotemporal dynamics in large-scale brain networks with next-generation neural mass models capturing exact macroscopic gamma activity.

## Metadata
- **Source**: arXiv:2512.03907
- **Authors**: Rosa Maria Delicado, Gemma Huguet, Pau Clusella
- **Published**: 2025-12
- **Institution**: Universitat de les Illes Balears, Universitat Politècnica de Catalunya, CRM Barcelona

## Core Methodology

### Key Innovation

Next-Generation Neural Mass Models (NG-NMMs) overcome limitations of classical NMMs (Wilson-Cowan, Jansen-Rit) by:

1. **Exact Macroscopic Description**: Derived from spiking network dynamics without approximation
2. **Synchrony-Dependent Dynamics**: Captures population synchrony effects on firing rates
3. **Richer Dynamical Repertoire**: Broader range of oscillatory and chaotic behaviors
4. **Cross-Frequency Coupling**: Gamma oscillations modulated by slower rhythms

### Comparison: Classical vs Next-Generation NMMs

| Feature | Classical NMM | NG-NMM |
|---------|--------------|--------|
| **Derivation** | Phenomenological | Exact mean-field limit |
| **Single neuron** | Rate-based | QIF (Quadratic Integrate-and-Fire) |
| **Synchrony tracking** | No | Yes (explicit) |
| **Oscillations** | Fixed repertoire | Extended repertoire |
| **Gamma generation** | Ad hoc | Natural PING mechanism |
| **Cross-frequency** | Limited | Strong coupling |

### Technical Framework

#### 1. Next-Generation Neural Mass Model

For a population of QIF neurons:

$$\tau_m \dot{r} = \frac{\Delta}{\pi\tau_m} + 2rv - r^2$$

$$\tau_m \dot{v} = v_{rest} + \mu + I_{syn} - \pi^2\tau_m^2 r^2$$

Where:
- $r$: Mean firing rate
- $v$: Mean membrane potential
- $\Delta$: Heterogeneity (quenched noise)
- $\mu$: External input
- $I_{syn}$: Synaptic current

**Key insight**: The $\pi^2\tau_m^2 r^2$ term captures synchrony effects

#### 2. E/I Coupling (PING Mechanism)

```
Excitatory Population ──► Inhibitory Population
        ▲                        │
        └────────────────────────┘
        
Cycle: E spikes → I activation → E suppression → I decay → E rebound
Frequency: 30-100 Hz (gamma band)
```

#### 3. Whole-Brain Network Model

90 interconnected brain regions with anatomical connectivity:

$$I_{syn}^{(i)} = g_E \sum_j C_{ij} s_E^{(j)} - g_I \sum_j C_{ij} s_I^{(j)}$$

Where $C_{ij}$ is the structural connectivity matrix from diffusion MRI.

## Implementation Guide

### Prerequisites

```python
# Required packages
pip install numpy scipy matplotlib
pip install numba              # For acceleration
pip install networkx           # For network analysis
pip install scikit-learn       # For dimensionality reduction
```

### Step-by-Step

#### Step 1: Single NG-NMM Population

```python
import numpy as np
from scipy.integrate import odeint

class NextGenNMM:
    """
    Next-Generation Neural Mass Model
    
    Single population of QIF neurons with synaptic dynamics
    """
    
    def __init__(
        self,
        tau_m=20.0,      # Membrane time constant (ms)
        tau_s=5.0,       # Synaptic time constant (ms)
        Delta=1.0,       # Heterogeneity parameter
        v_rest=-65.0,    # Resting potential (mV)
        J=15.0,          # Synaptic coupling strength
        theta=-50.0,     # Threshold potential (mV)
        reset=-70.0      # Reset potential (mV)
    ):
        self.tau_m = tau_m
        self.tau_s = tau_s
        self.Delta = Delta
        self.v_rest = v_rest
        self.J = J
        self.theta = theta
        self.reset = reset
    
    def derivatives(self, state, t, mu_ext):
        """
        Compute derivatives for ODE integration
        
        State variables:
            r: firing rate
            v: mean membrane potential
            s: synaptic gating variable
        
        Args:
            state: [r, v, s]
            t: time
            mu_ext: external input
        
        Returns:
            [dr/dt, dv/dt, ds/dt]
        """
        r, v, s = state
        
        # Firing rate equation
        dr = (self.Delta / (np.pi * self.tau_m) + 2*r*v - r**2) / self.tau_m
        
        # Membrane potential equation
        dv = (self.v_rest + mu_ext + self.J * s - 
              np.pi**2 * self.tau_m**2 * r**2 - v) / self.tau_m
        
        # Synaptic dynamics
        ds = (-s + self.tau_s * r) / self.tau_s
        
        return [dr, dv, ds]
    
    def simulate(self, t_span, mu_ext, initial_state=None):
        """
        Simulate single population dynamics
        
        Args:
            t_span: time points array
            mu_ext: external input (can be array or function)
            initial_state: initial [r, v, s]
        
        Returns:
            trajectory: (time, 3) array of [r, v, s]
        """
        if initial_state is None:
            initial_state = [0.0, self.v_rest, 0.0]
        
        # Handle time-varying input
        if callable(mu_ext):
            mu_func = mu_ext
        else:
            mu_func = lambda t: mu_ext
        
        # ODE integration
        def ode_func(state, t):
            return self.derivatives(state, t, mu_func(t))
        
        trajectory = odeint(ode_func, initial_state, t_span)
        
        return trajectory


# Example: Single population simulation
nmm = NextGenNMM()
t = np.linspace(0, 1000, 10000)  # 1 second
mu = 10.0  # External input

# Simulate
traj = nmm.simulate(t, mu)
r, v, s = traj[:, 0], traj[:, 1], traj[:, 2]

# Plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

axes[0].plot(t, r, 'b', label='Firing rate (Hz)')
axes[0].set_ylabel('r (Hz)')
axes[0].legend()

axes[1].plot(t, v, 'r', label='Mean membrane potential (mV)')
axes[1].set_ylabel('v (mV)')
axes[1].legend()

axes[2].plot(t, s, 'g', label='Synaptic variable')
axes[2].set_ylabel('s')
axes[2].set_xlabel('Time (ms)')
axes[2].legend()

plt.tight_layout()
plt.savefig('single_nmm_dynamics.png', dpi=150)
```

#### Step 2: E/I Network with PING Oscillations

```python
class EINGNetwork:
    """
    Excitatory-Inhibitory NG-NMM Network
    
    Generates gamma oscillations through PING mechanism
    """
    
    def __init__(
        self,
        tau_m_E=20.0,    # E cell membrane time constant
        tau_m_I=10.0,    # I cell membrane time constant
        tau_s_E=5.0,     # E synaptic time constant
        tau_s_I=8.0,     # I synaptic time constant
        Delta_E=1.0,     # E cell heterogeneity
        Delta_I=0.5,     # I cell heterogeneity
        J_EE=0.0,        # E→E coupling
        J_EI=-15.0,      # E→I coupling
        J_IE=15.0,       # I→E coupling
        J_II=-5.0        # I→I coupling
    ):
        self.E = NextGenNMM(tau_m_E, tau_s_E, Delta_E)
        self.I = NextGenNMM(tau_m_I, tau_s_I, Delta_I)
        
        self.J_EE = J_EE
        self.J_EI = J_EI
        self.J_IE = J_IE
        self.J_II = J_II
    
    def derivatives(self, state, t, mu_E, mu_I):
        """
        6D system: [r_E, v_E, s_E, r_I, v_I, s_I]
        """
        rE, vE, sE, rI, vI, sI = state
        
        # Synaptic currents
        I_syn_E = self.J_EE * sE + self.J_EI * sI
        I_syn_I = self.J_IE * sE + self.J_II * sI
        
        # E population derivatives
        drE = (self.E.Delta / (np.pi * self.E.tau_m) + 2*rE*vE - rE**2) / self.E.tau_m
        dvE = (self.E.v_rest + mu_E + I_syn_E - 
               np.pi**2 * self.E.tau_m**2 * rE**2 - vE) / self.E.tau_m
        dsE = (-sE + self.E.tau_s * rE) / self.E.tau_s
        
        # I population derivatives
        drI = (self.I.Delta / (np.pi * self.I.tau_m) + 2*rI*vI - rI**2) / self.I.tau_m
        dvI = (self.I.v_rest + mu_I + I_syn_I - 
               np.pi**2 * self.I.tau_m**2 * rI**2 - vI) / self.I.tau_m
        dsI = (-sI + self.I.tau_s * rI) / self.I.tau_s
        
        return [drE, dvE, dsE, drI, dvI, dsI]
    
    def simulate(self, t_span, mu_E, mu_I, initial_state=None):
        """Simulate E/I network"""
        if initial_state is None:
            initial_state = [0.0, -65.0, 0.0, 0.0, -65.0, 0.0]
        
        def ode_func(state, t):
            return self.derivatives(state, t, mu_E, mu_I)
        
        trajectory = odeint(ode_func, initial_state, t_span)
        
        return trajectory
    
    def find_fixed_points(self, mu_E, mu_I):
        """
        Find fixed points of the E/I system
        
        Returns:
            fixed_points: List of [rE*, vE*, sE*, rI*, vI*, sI*]
        """
        from scipy.optimize import fsolve
        
        def equations(state):
            return self.derivatives(state, 0, mu_E, mu_I)
        
        # Try multiple initial guesses
        fixed_points = []
        for rE0 in [0, 5, 10, 20]:
            for rI0 in [0, 5, 10, 20]:
                guess = [rE0, -60, rE0*self.E.tau_s, rI0, -60, rI0*self.I.tau_s]
                sol = fsolve(equations, guess, full_output=True)
                if np.max(np.abs(equations(sol[0]))) < 1e-6:
                    fixed_points.append(sol[0])
        
        return fixed_points


# Example: Generate PING oscillations
ei_net = EINGNetwork()
t = np.linspace(0, 500, 5000)

# Strong input to E, moderate to I
mu_E = 20.0
mu_I = 5.0

traj = ei_net.simulate(t, mu_E, mu_I)
rE, rI = traj[:, 0], traj[:, 3]

# Plot PING oscillations
fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

axes[0].plot(t, rE, 'b', label='Excitatory rate')
axes[0].plot(t, rI, 'r', label='Inhibitory rate')
axes[0].set_ylabel('Firing rate (Hz)')
axes[0].legend()
axes[0].set_title('PING Oscillations (Gamma band)')

# Compute and plot power spectrum
from scipy.signal import welch
fE, pE = welch(rE, fs=1000/(t[1]-t[0]), nperseg=512)
fI, pI = welch(rI, fs=1000/(t[1]-t[0]), nperseg=512)

axes[1].semilogy(fE, pE, 'b', label='E power')
axes[1].semilogy(fI, pI, 'r', label='I power')
axes[1].axvline(40, color='g', linestyle='--', label='40 Hz')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Power')
axes[1].legend()
axes[1].set_xlim(0, 100)

plt.tight_layout()
plt.savefig('ping_oscillations.png', dpi=150)
```

#### Step 3: Whole-Brain Network with NG-NMM

```python
class WholeBrainNGNMM:
    """
    Whole-brain network using NG-NMM for each region
    
    90 brain regions with empirical structural connectivity
    """
    
    def __init__(
        self,
        connectivity_matrix,
        coupling_strength=0.1,
        n_regions=90
    ):
        """
        Args:
            connectivity_matrix: (n_regions, n_regions) structural connectivity
            coupling_strength: Global coupling parameter
            n_regions: Number of brain regions
        """
        self.C = connectivity_matrix
        self.G = coupling_strength
        self.n_regions = n_regions
        
        # Create E/I network for each region
        self.regions = [EINGNetwork() for _ in range(n_regions)]
        
        # Normalize connectivity
        self.C_norm = self.C / np.max(self.C)
    
    def derivatives(self, state, t):
        """
        Compute derivatives for whole-brain system
        
        State: Flattened array of [rE, vE, sE, rI, vI, sI] for each region
        Total dimension: 6 * n_regions
        """
        n = self.n_regions
        dstate = np.zeros_like(state)
        
        # Extract regional states
        rE = state[0::6]
        vE = state[1::6]
        sE = state[2::6]
        rI = state[3::6]
        vI = state[4::6]
        sI = state[5::6]
        
        # Compute coupling between regions
        # E cells receive input from connected regions
        coupling_E = self.G * self.C_norm @ sE
        coupling_I = self.G * self.C_norm @ sI
        
        # Compute derivatives for each region
        for i in range(n):
            region = self.regions[i]
            
            # Add coupling to external input
            mu_E = 10.0 + coupling_E[i]  # Base input + coupling
            mu_I = 5.0 + coupling_I[i] * 0.5  # Weaker coupling to I
            
            # Regional state
            regional_state = [rE[i], vE[i], sE[i], rI[i], vI[i], sI[i]]
            
            # Compute derivatives
            dregional = region.derivatives(regional_state, t, mu_E, mu_I)
            
            # Store in output
            dstate[6*i:6*(i+1)] = dregional
        
        return dstate
    
    def simulate(self, t_span, initial_state=None, noise_sigma=0.0):
        """
        Simulate whole-brain dynamics
        
        Args:
            t_span: time points
            initial_state: initial conditions
            noise_sigma: additive noise strength
        """
        if initial_state is None:
            initial_state = np.random.randn(6 * self.n_regions) * 0.1
        
        def ode_func(state, t):
            # Add noise
            noise = np.random.randn(len(state)) * noise_sigma
            return self.derivatives(state, t) + noise
        
        trajectory = odeint(ode_func, initial_state, t_span)
        
        return trajectory
    
    def compute_fc(self, trajectory, burn_in=1000):
        """
        Compute functional connectivity from simulation
        
        Args:
            trajectory: simulated dynamics
            burn_in: initial samples to discard
        
        Returns:
            FC: Functional connectivity matrix
        """
        # Extract E-cell firing rates
        rE_all = trajectory[burn_in:, 0::6]
        
        # Compute correlation matrix
        FC = np.corrcoef(rE_all.T)
        
        return FC


# Load structural connectivity
def load_human_connectome():
    """
    Load human connectome data
    
    Returns:
        connectivity: (90, 90) structural connectivity matrix
        regions: List of region names
    """
    # This is a placeholder - actual implementation would load
    # from files like those provided by the Human Connectome Project
    
    # For demonstration, create synthetic connectivity
    n = 90
    connectivity = np.random.rand(n, n) * 0.1
    
    # Make symmetric and zero diagonal
    connectivity = (connectivity + connectivity.T) / 2
    np.fill_diagonal(connectivity, 0)
    
    # Add community structure (modular)
    communities = 6
    regions_per_comm = n // communities
    for comm in range(communities):
        start = comm * regions_per_comm
        end = (comm + 1) * regions_per_comm
        connectivity[start:end, start:end] *= 5  # Stronger within-community
    
    region_names = [f"Region_{i}" for i in range(n)]
    
    return connectivity, region_names


# Simulate whole-brain network
connectivity, regions = load_human_connectome()
brain = WholeBrainNGNMM(connectivity, coupling_strength=0.05)

# Simulate
t = np.linspace(0, 2000, 20000)  # 2 seconds
trajectory = brain.simulate(t, noise_sigma=0.01)

# Compute functional connectivity
FC_sim = brain.compute_fc(trajectory)

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Firing rates of sample regions
sample_regions = [0, 10, 20, 30]
for i in sample_regions:
    rE = trajectory[:, 6*i]
    axes[0].plot(t/1000, rE, label=f'Region {i}')

axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('E firing rate (Hz)')
axes[0].legend()
axes[0].set_title('Regional Activity')

# Functional connectivity
im = axes[1].imshow(FC_sim, cmap='RdBu_r', vmin=-1, vmax=1)
axes[1].set_title('Functional Connectivity')
plt.colorbar(im, ax=axes[1])

plt.tight_layout()
plt.savefig('wholebrain_ngnmm.png', dpi=150)
```

#### Step 4: Stability Analysis with Master Stability Function

```python
class MasterStabilityAnalysis:
    """
    Master Stability Function (MSF) analysis for NG-NMM networks
    
    Determines stability of synchronized states
    """
    
    def __init__(self, single_node_dynamics, coupling_matrix):
        """
        Args:
            single_node_dynamics: Function returning derivatives for isolated node
            coupling_matrix: Network coupling structure
        """
        self.node_dyn = single_node_dynamics
        self.L = self._compute_laplacian(coupling_matrix)
        self.eigenvalues = np.linalg.eigvals(self.L)
    
    def _compute_laplacian(self, C):
        """Compute graph Laplacian from connectivity"""
        D = np.diag(np.sum(C, axis=1))
        return D - C
    
    def compute_msf(self, alpha_range, sync_state, dt=0.01):
        """
        Compute Master Stability Function
        
        Args:
            alpha_range: Range of coupling strengths to test
            sync_state: Synchronized state trajectory
            dt: Time step
        
        Returns:
            msf_values: MSF for each alpha
        """
        msf_values = []
        
        for alpha in alpha_range:
            # Compute variational equation
            lyap_exp = self._compute_lyapunov_exponent(
                alpha, sync_state, dt
            )
            msf_values.append(lyap_exp)
        
        return np.array(msf_values)
    
    def _compute_lyapunov_exponent(self, alpha, sync_state, dt):
        """
        Compute largest Lyapunov exponent for given coupling
        """
        # Simplified implementation - would use proper variational equation
        # integration in practice
        
        n_steps = len(sync_state)
        perturbation = np.random.randn(len(sync_state[0])) * 0.01
        
        lyap_sum = 0
        for i in range(n_steps - 1):
            # Evolve perturbation
            J = self._compute_jacobian(sync_state[i], alpha)
            perturbation = perturbation + dt * J @ perturbation
            
            # Normalize and accumulate
            norm = np.linalg.norm(perturbation)
            lyap_sum += np.log(norm / 0.01)
            perturbation = perturbation / norm * 0.01
        
        return lyap_sum / (n_steps * dt)
    
    def _compute_jacobian(self, state, alpha):
        """Compute Jacobian matrix at given state"""
        # Numerical differentiation
        n = len(state)
        J = np.zeros((n, n))
        eps = 1e-8
        
        for i in range(n):
            state_plus = state.copy()
            state_plus[i] += eps
            
            state_minus = state.copy()
            state_minus[i] -= eps
            
            f_plus = self.node_dyn(state_plus)
            f_minus = self.node_dyn(state_minus)
            
            J[:, i] = (f_plus - f_minus) / (2 * eps)
        
        return J
    
    def find_stable_coupling(self, alpha_range, msf_values):
        """
        Find range of coupling strengths for stable synchronization
        
        Returns:
            stable_range: (min, max) coupling for stability
        """
        # MSF < 0 indicates stability
        stable_mask = msf_values < 0
        
        if not np.any(stable_mask):
            return None
        
        stable_alphas = alpha_range[stable_mask]
        return (np.min(stable_alphas), np.max(stable_alphas))


# Example MSF analysis
msf_analyzer = MasterStabilityAnalysis(
    lambda s: EINGNetwork().derivatives(s, 0, 10, 5),
    connectivity
)

alpha_range = np.linspace(0, 1.0, 100)

# Generate synchronous state (all regions identical)
ei_net = EINGNetwork()
t_sync = np.linspace(0, 500, 5000)
sync_traj = ei_net.simulate(t_sync, 10, 5)

# Compute MSF
msf_values = msf_analyzer.compute_msf(alpha_range, sync_traj)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(alpha_range, msf_values, 'b-', linewidth=2)
plt.axhline(0, color='r', linestyle='--', label='Stability boundary')
plt.xlabel('Coupling strength α')
plt.ylabel('MSF (Largest Lyapunov exponent)')
plt.title('Master Stability Function')
plt.legend()
plt.grid(True)
plt.savefig('msf_analysis.png', dpi=150)
```

## Applications

### 1. Clinical: Seizure Dynamics

```python
class SeizureModel:
    """
    Model seizure dynamics using NG-NMM
    
    Seizure: Transition from stable low-activity to high-frequency oscillations
    """
    
    def __init__(self, brain_network):
        self.brain = brain_network
    
    def simulate_seizure(self, t_span, stimulation_site, stim_strength):
        """
        Simulate seizure triggered by focal stimulation
        
        Args:
            t_span: time array
            stimulation_site: Region index to stimulate
            stim_strength: Stimulation amplitude
        """
        def stimulated_dynamics(state, t):
            dstate = self.brain.derivatives(state, t)
            
            # Add stimulation to specific region during early phase
            if t < 100:  # 100ms stimulation
                region_offset = stimulation_site * 6
                dstate[region_offset] += stim_strength  # Increase E-cell input
            
            return dstate
        
        # Simulate
        initial_state = np.random.randn(6 * self.brain.n_regions) * 0.1
        trajectory = odeint(stimulated_dynamics, initial_state, t_span)
        
        return trajectory
    
    def analyze_seizure_propagation(self, trajectory):
        """
        Analyze how seizure spreads across brain regions
        """
        # Compute time-varying correlation
        rE_all = trajectory[:, 0::6]
        
        propagation = {
            'onset_time': [],
            'peak_activity': [],
            'involved_regions': []
        }
        
        for i in range(self.brain.n_regions):
            activity = rE_all[:, i]
            
            # Detect seizure onset (sudden increase in activity)
            threshold = np.mean(activity[:100]) + 3 * np.std(activity[:100])
            onset_idx = np.where(activity > threshold)[0]
            
            if len(onset_idx) > 0:
                propagation['onset_time'].append(onset_idx[0])
                propagation['peak_activity'].append(np.max(activity))
                propagation['involved_regions'].append(i)
        
        return propagation
```

### 2. Cognitive: Working Memory

```python
class WorkingMemoryNGNMM:
    """
    Working memory model using bistable NG-NMM
    
    Two stable states: low activity (rest) and high activity (memory)
    """
    
    def __init__(self):
        # Parameters for bistability
        self.nmm = NextGenNMM(
            tau_m=20.0,
            tau_s=100.0,  # Slow synapses for persistence
            Delta=0.5,    # Low heterogeneity for sharp transitions
            J=20.0        # Strong recurrent coupling
        )
    
    def find_bistable_regime(self):
        """
        Find input range where bistability occurs
        """
        mu_range = np.linspace(0, 30, 100)
        
        # Find fixed points for each input
        bistable_range = []
        
        for mu in mu_range:
            # Find fixed points numerically
            from scipy.optimize import fsolve
            
            def steady_state(vars):
                r, v, s = vars
                return self.nmm.derivatives([r, v, s], 0, mu)
            
            # Try different initial conditions
            fps = []
            for r0 in [0, 5, 15, 25]:
                sol = fsolve(steady_state, [r0, -60, r0*self.nmm.tau_s])
                if np.allclose(steady_state(sol), 0, atol=1e-6):
                    fps.append(sol)
            
            # Check for bistability (2 stable fixed points)
            if len(fps) >= 2:
                bistable_range.append(mu)
        
        return bistable_range
    
    def simulate_wm_task(self, t, cue_time=500, delay_duration=1000):
        """
        Simulate delayed match-to-sample task
        
        Timeline:
        0-500ms: Fixation
        500-700ms: Cue presentation
        700-1700ms: Delay
        1700-2000ms: Probe
        """
        def input_protocol(t):
            if cue_time <= t < cue_time + 200:
                return 25  # Cue input -> switch to high state
            elif cue_time + delay_duration <= t:
                return 10  # Probe
            else:
                return 10  # Maintenance input (bistable regime)
        
        trajectory = self.nmm.simulate(t, input_protocol)
        
        return trajectory
```

### 3. Network Analysis: Hub Identification

```python
class NetworkHubAnalysis:
    """
    Identify network hubs using NG-NMM dynamics
    """
    
    def __init__(self, whole_brain_model):
        self.model = whole_brain_model
    
    def compute_node_importance(self, t_span):
        """
        Compute importance of each node based on:
        1. Impact on global synchronization
        2. Information flow
        3. Dynamical influence
        """
        n = self.model.n_regions
        importance_scores = np.zeros(n)
        
        # Baseline simulation
        baseline_traj = self.model.simulate(t_span)
        baseline_fc = self.model.compute_fc(baseline_traj)
        
        # Remove each node and measure impact
        for i in range(n):
            # Modify connectivity (remove connections to node i)
            C_modified = self.model.C.copy()
            C_modified[i, :] = 0
            C_modified[:, i] = 0
            
            # Simulate with modified connectivity
            model_modified = WholeBrainNGNMM(
                C_modified,
                self.model.G,
                n
            )
            modified_traj = model_modified.simulate(t_span)
            modified_fc = model_modified.compute_fc(modified_traj)
            
            # Measure impact (FC difference)
            impact = np.linalg.norm(baseline_fc - modified_fc, 'fro')
            importance_scores[i] = impact
        
        return importance_scores
    
    def identify_hubs(self, n_hubs=10):
        """
        Identify top hub regions
        """
        t = np.linspace(0, 1000, 10000)
        importance = self.compute_node_importance(t)
        
        hub_indices = np.argsort(importance)[-n_hubs:][::-1]
        
        return hub_indices, importance[hub_indices]
```

## Benchmarks

### Dynamical Repertoire Comparison

| Dynamical Regime | Classical NMM | NG-NMM |
|-----------------|---------------|--------|
| Steady state | Yes | Yes |
| Limit cycle (alpha) | Yes | Yes |
| Limit cycle (gamma) | Limited | Yes (natural) |
| Quasiperiodicity | No | Yes |
| Chaos | Limited | Extensive |
| Multistability | Limited | Rich |

### Cross-Frequency Coupling

| Model | Theta-Gamma | Alpha-Gamma | Beta-Gamma |
|-------|-------------|-------------|------------|
| Jansen-Rit | Weak | Moderate | Weak |
| Wilson-Cowan | Weak | Weak | Weak |
| **NG-NMM** | **Strong** | **Strong** | **Strong** |

### Computational Performance

| Network Size | Simulation Time (1s) | Memory |
|--------------|---------------------|--------|
| 10 regions | 0.5s | 10 MB |
| 90 regions | 12s | 200 MB |
| 1000 regions | 850s | 4 GB |

## Pitfalls

- **Parameter Sensitivity**: Requires careful tuning of heterogeneity ($\Delta$) and coupling ($G$)
- **Numerical Integration**: Stiff equations may require adaptive time-stepping
- **High-Dimensional Analysis**: MSF analysis becomes expensive for large networks
- **Bifurcation Tracking**: Transition boundaries require continuation methods
- **Empirical Validation**: Model predictions need validation against real brain recordings
- **Computational Scaling**: Full 90-region simulations are computationally intensive

## Related Skills

- nonequilibrium-brain-dynamics-physics
- neural-dynamics-universal-translator-foundation
- brain-dit-fmri-foundation-model
- kuramoto-brain-network
- working-memory-heterogeneous-delays

## References

```bibtex
@article{delicado2025emergent,
  title={Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models},
  author={Delicado, Rosa Maria and Huguet, Gemma and Clusella, Pau},
  journal={arXiv preprint arXiv:2512.03907},
  year={2025}
}
```
