# Implementation: SNN Internal Noise Analysis

## LIF Neuron with Noise Injection

```python
import torch
import torch.nn as nn
import numpy as np

class NoisyLIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire neuron with configurable noise injection."""
    
    def __init__(self, tau_mem=20.0, v_threshold=1.0, v_reset=0.0, 
                 dt=1.0, noise_stage=None, noise_type=None, noise_scale=0.0):
        """
        Args:
            noise_stage: 'input_current', 'membrane_potential', or 'output_spike'
            noise_type: 'additive' or 'multiplicative'
            noise_scale: Standard deviation of noise (0.0 = no noise)
        """
        super().__init__()
        self.tau_mem = tau_mem
        self.v_threshold = v_threshold
        self.v_reset = v_reset
        self.dt = dt
        self.decay = np.exp(-dt / tau_mem)
        self.noise_stage = noise_stage
        self.noise_type = noise_type
        self.noise_scale = noise_scale
        
    def _add_noise(self, signal, noise_stage, noise_type, scale):
        """Apply additive or multiplicative noise to a signal."""
        if noise_stage is None or scale == 0:
            return signal
            
        if noise_type == 'additive':
            noise = torch.randn_like(signal) * scale
            return signal + noise
        elif noise_type == 'multiplicative':
            noise = torch.randn_like(signal) * scale
            return signal * (1.0 + noise)
        else:
            raise ValueError(f"Unknown noise_type: {noise_type}")
    
    def forward(self, input_current, v_mem):
        """Single step with noise at configurable stages."""
        
        # 1. Noise on input current
        input_noisy = self._add_noise(
            input_current, 'input_current',
            self.noise_type if self.noise_stage == 'input_current' else None,
            self.noise_scale if self.noise_stage == 'input_current' else 0
        )
        
        # 2. Leak and integrate
        v_mem = self.decay * v_mem + (1 - self.decay) * input_noisy
        
        # 3. Noise on membrane potential
        v_mem_noisy = self._add_noise(
            v_mem, 'membrane_potential',
            self.noise_type if self.noise_stage == 'membrane_potential' else None,
            self.noise_scale if self.noise_stage == 'membrane_potential' else 0
        )
        
        # 4. Spike generation (from noisy membrane)
        spikes = (v_mem_noisy >= self.v_threshold).float()
        
        # 5. Reset membrane potential after spike
        v_mem = v_mem * (1 - spikes) + self.v_reset * spikes
        
        # 6. Noise on output spikes
        spikes_noisy = self._add_noise(
            spikes, 'output_spike',
            self.noise_type if self.noise_stage == 'output_spike' else None,
            self.noise_scale if self.noise_stage == 'output_spike' else 0
        ).clamp(0, 1).round()  # Round back to binary spikes
        
        return v_mem, spikes_noisy
```

## Sigmoid-Based Input Pre-Filtering

```python
class SigmoidPreFilter(nn.Module):
    """
    Sigmoid-based input pre-filter that shifts inputs to strictly positive range.
    This is the most effective defense against multiplicative membrane noise.
    """
    
    def __init__(self, alpha=1.0, bias=0.5, trainable=False):
        """
        Args:
            alpha: Scaling factor for sigmoid input
            bias: Shift added after sigmoid (ensures strictly positive)
            trainable: Whether alpha and bias are learnable
        """
        super().__init__()
        if trainable:
            self.alpha = nn.Parameter(torch.tensor(alpha))
            self.bias = nn.Parameter(torch.tensor(bias))
        else:
            self.register_buffer('alpha', torch.tensor(alpha))
            self.register_buffer('bias', torch.tensor(bias))
    
    def forward(self, x):
        """Apply sigmoid filter: output is strictly positive."""
        return torch.sigmoid(self.alpha * x) + self.bias


class RobustInputPipeline(nn.Module):
    """Complete robust input pipeline with pre-filtering."""
    
    def __init__(self, n_features=64, filter_type='sigmoid', **filter_kwargs):
        super().__init__()
        if filter_type == 'sigmoid':
            self.filter = SigmoidPreFilter(**filter_kwargs)
        elif filter_type == 'none':
            self.filter = nn.Identity()
        else:
            raise ValueError(f"Unknown filter_type: {filter_type}")
            
    def forward(self, raw_input):
        return self.filter(raw_input)
```

## Multi-Layer SNN with Noise

```python
class NoisySNN(nn.Module):
    """Multi-layer SNN with configurable noise at each layer."""
    
    def __init__(self, n_input=64, n_hidden=256, n_output=10, 
                 noise_configs=None, dt=1.0):
        """
        Args:
            noise_configs: Dict with layer-wise noise settings
                e.g. {
                    'hidden': {'noise_stage': 'membrane_potential', 
                               'noise_type': 'multiplicative', 
                               'noise_scale': 0.3},
                    'output': {'noise_stage': 'input_current', 
                               'noise_type': 'additive', 
                               'noise_scale': 0.1}
                }
        """
        super().__init__()
        self.dt = dt
        
        # Weights
        self.W_in = nn.Linear(n_input, n_hidden, bias=False)
        self.W_rec = nn.Linear(n_hidden, n_hidden, bias=False)
        self.W_out = nn.Linear(n_hidden, n_output, bias=False)
        
        # Neurons
        hidden_cfg = noise_configs.get('hidden', {})
        output_cfg = noise_configs.get('output', {})
        
        self.hidden_neurons = NoisyLIFNeuron(dt=dt, **hidden_cfg)
        self.output_neurons = NoisyLIFNeuron(dt=dt, **output_cfg)
        
        # State
        self.register_buffer('v_hidden', torch.zeros(n_hidden))
        self.register_buffer('v_output', torch.zeros(n_output))
        self.register_buffer('spike_hidden', torch.zeros(n_hidden))
        self.register_buffer('spike_output', torch.zeros(n_output))
        
    def reset(self):
        self.v_hidden.zero_()
        self.v_output.zero_()
        self.spike_hidden.zero_()
        self.spike_output.zero_()
        
    def step(self, input_current):
        """One simulation step."""
        # Hidden layer
        rec_input = self.W_rec(self.spike_hidden)
        hidden_input = self.W_in(input_current) + rec_input
        self.v_hidden, self.spike_hidden = self.hidden_neurons(hidden_input, self.v_hidden)
        
        # Output layer
        output_input = self.W_out(self.spike_hidden)
        self.v_output, self.spike_output = self.output_neurons(output_input, self.v_output)
        
        return self.spike_output
    
    def forward(self, input_sequence, reset=True):
        """Run through full sequence."""
        if reset:
            self.reset()
            
        outputs = []
        for x in input_sequence:
            out = self.step(x)
            outputs.append(out.clone())
            
        return torch.stack(outputs)
```

## Common vs Uncommon Noise

```python
class CommonNoiseInjector:
    """
    Applies the SAME noise sample across all neurons in a population.
    SNNs are typically more robust to this than independent noise.
    """
    
    @staticmethod
    def additive_common(signal, scale):
        """Add the same noise value to all neurons."""
        if signal.dim() == 1:
            noise = torch.randn(1) * scale
            return signal + noise.expand_as(signal)
        else:
            noise = torch.randn(signal.shape[0], 1) * scale
            return signal + noise.expand_as(signal)
    
    @staticmethod
    def multiplicative_common(signal, scale):
        """Multiply all neurons by the same noise factor."""
        if signal.dim() == 1:
            noise = torch.randn(1) * scale
            return signal * (1.0 + noise.expand_as(signal))
        else:
            noise = torch.randn(signal.shape[0], 1) * scale
            return signal * (1.0 + noise.expand_as(signal))


class UncommonNoiseInjector:
    """
    Applies INDEPENDENT noise samples to each neuron.
    Typically more disruptive than common noise.
    """
    
    @staticmethod
    def additive_uncommon(signal, scale):
        return signal + torch.randn_like(signal) * scale
    
    @staticmethod
    def multiplicative_uncommon(signal, scale):
        return signal * (1.0 + torch.randn_like(signal) * scale)
```

## Robustness Evaluation Framework

```python
def evaluate_noise_robustness(model, task, noise_scales=np.linspace(0, 1.0, 11),
                               noise_stage='membrane_potential',
                               noise_type='multiplicative',
                               use_prefilter=False,
                               n_trials=100):
    """
    Comprehensive robustness evaluation across noise intensities.
    """
    results = {
        'noise_scales': noise_scales,
        'accuracies': [],
        'membrane_stats': []
    }
    
    for scale in noise_scales:
        # Configure noise
        model.hidden_neurons.noise_stage = noise_stage
        model.hidden_neurons.noise_type = noise_type
        model.hidden_neurons.noise_scale = scale
        
        accs = []
        mem_means = []
        mem_stds = []
        
        for _ in range(n_trials):
            x, y = task.get_sample()
            
            if use_prefilter:
                x = model.input_filter(x)
                
            output = model(x)
            pred = output.sum(dim=0).argmax().item()
            accs.append(pred == y)
            
            # Track membrane statistics
            mem_means.append(model.v_hidden.mean().item())
            mem_stds.append(model.v_hidden.std().item())
            
        results['accuracies'].append(np.mean(accs))
        results['membrane_stats'].append({
            'mean': np.mean(mem_means),
            'std': np.mean(mem_stds)
        })
        
    return results


def compare_noise_stages(model, task, scales=np.linspace(0, 1.0, 11)):
    """Compare all noise stage/type combinations."""
    combinations = [
        ('input_current', 'additive'),
        ('input_current', 'multiplicative'),
        ('membrane_potential', 'additive'),
        ('membrane_potential', 'multiplicative'),
        ('output_spike', 'additive'),
        ('output_spike', 'multiplicative'),
    ]
    
    all_results = {}
    for stage, ntype in combinations:
        key = f"{stage}_{ntype}"
        all_results[key] = evaluate_noise_robustness(
            model, task, scales, stage, ntype
        )
        
    return all_results


def compare_common_vs_uncommon(model, task, scales=np.linspace(0, 1.0, 11)):
    """Compare common vs uncommon noise effects."""
    common_results = []
    uncommon_results = []
    
    for scale in scales:
        # Common noise
        model.hidden_neurons.noise_scale = scale
        model.hidden_neurons.noise_type = 'multiplicative'
        model.hidden_neurons.noise_stage = 'membrane_potential'
        
        acc_common = evaluate_noise_robustness(
            model, task, [scale], use_prefilter=False, n_trials=100
        )['accuracies'][0]
        common_results.append(acc_common)
        
        # Uncommon noise (default in NoisyLIFNeuron)
        acc_uncommon = evaluate_noise_robustness(
            model, task, [scale], use_prefilter=False, n_trials=100
        )['accuracies'][0]
        uncommon_results.append(acc_uncommon)
        
    return {
        'scales': scales,
        'common': common_results,
        'uncommon': uncommon_results
    }
```

## Complete Analysis Pipeline

```python
def run_full_noise_analysis():
    """Run the complete noise analysis from the paper."""
    import matplotlib.pyplot as plt
    
    # 1. Create baseline model
    noise_configs = {
        'hidden': {'noise_stage': None, 'noise_type': None, 'noise_scale': 0},
        'output': {'noise_stage': None, 'noise_type': None, 'noise_scale': 0}
    }
    model = NoisySNN(noise_configs=noise_configs)
    
    # Train baseline first
    # model = train_baseline(model, task)
    
    # 2. Compare all noise stages
    scales = np.linspace(0, 1.0, 11)
    all_results = compare_noise_stages(model, task, scales)
    
    # 3. Evaluate with sigmoid pre-filtering
    model_prefiltered = NoisySNN(noise_configs=noise_configs)
    model_prefiltered.input_filter = SigmoidPreFilter()
    
    prefilter_results = {}
    for stage, ntype in [('membrane_potential', 'multiplicative'),
                          ('input_current', 'additive')]:
        key = f"{stage}_{ntype}"
        prefilter_results[key] = evaluate_noise_robustness(
            model_prefiltered, task, scales, stage, ntype,
            use_prefilter=True
        )
    
    # 4. Compare common vs uncommon
    common_results = compare_common_vs_uncommon(model, task, scales)
    
    # Print key findings
    print("=== Noise Impact Summary ===")
    for key, res in all_results.items():
        acc_at_1 = res['accuracies'][-1]  # accuracy at max noise
        print(f"  {key}: accuracy at max noise = {acc_at_1:.3f}")
        
    print("\n=== With Sigmoid Pre-filter ===")
    for key, res in prefilter_results.items():
        acc_at_1 = res['accuracies'][-1]
        print(f"  {key}: accuracy at max noise = {acc_at_1:.3f}")
        
    print("\n=== Common vs Uncommon Noise ===")
    print(f"  Common noise robustness:    {np.mean(common_results['common']):.3f}")
    print(f"  Uncommon noise robustness:  {np.mean(common_results['uncommon']):.3f}")
    
    return all_results, prefilter_results, common_results
```

## Visualization

```python
def plot_noise_results(all_results, prefilter_results, common_results):
    """Generate comprehensive noise analysis plots."""
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    scales = np.linspace(0, 1.0, 11)
    
    # Plot 1: All noise stages (no pre-filter)
    ax = axes[0, 0]
    for key, res in all_results.items():
        ax.plot(scales, res['accuracies'], '-o', label=key, markersize=4)
    ax.set_xlabel('Noise Scale')
    ax.set_ylabel('Accuracy')
    ax.set_title('Noise Impact by Stage (No Pre-filter)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Pre-filter comparison (worst-case noise)
    ax = axes[0, 1]
    for key in ['membrane_potential_multiplicative', 'input_current_additive']:
        if key in all_results:
            ax.plot(scales, all_results[key]['accuracies'], 
                   '--o', label=f'{key} (no filter)', markersize=4)
        if key in prefilter_results:
            ax.plot(scales, prefilter_results[key]['accuracies'], 
                   '-s', label=f'{key} (+ sigmoid filter)', markersize=4)
    ax.set_xlabel('Noise Scale')
    ax.set_ylabel('Accuracy')
    ax.set_title('Effect of Sigmoid Pre-filter')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Common vs Uncommon
    ax = axes[1, 0]
    ax.plot(scales, common_results['common'], '-o', label='Common noise')
    ax.plot(scales, common_results['uncommon'], '-s', label='Uncommon noise')
    ax.set_xlabel('Noise Scale')
    ax.set_ylabel('Accuracy')
    ax.set_title('Common vs Uncommon Noise')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Membrane potential statistics
    ax = axes[1, 1]
    key = 'membrane_potential_multiplicative'
    if key in all_results:
        stats = all_results[key]['membrane_stats']
        means = [s['mean'] for s in stats]
        stds = [s['std'] for s in stats]
        ax.errorbar(scales, means, yerr=stds, fmt='-o', markersize=4,
                    label='Membrane potential')
        ax.axhline(y=0, color='r', linestyle='--', alpha=0.5, 
                   label='Zero threshold')
    ax.set_xlabel('Noise Scale')
    ax.set_ylabel('Mean Membrane Potential')
    ax.set_title('Membrane Potential Under Multiplicative Noise')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('noise_analysis.png', dpi=150)
    plt.close()
```
