"""
Memristive Neuron Simulation with Multiple Spiking Modes

This script simulates Ag/HZO memristive neurons capable of:
- Time-to-First-Spike (TTFS) encoding
- Spike count coding
- Firing rate coding

Reference: arXiv:2604.11780v1
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class MemristorParams:
    """Parameters for Ag/HZO memristor."""
    Ron: float = 1000       # ON resistance (Ohms)
    Roff: float = 100000    # OFF resistance (Ohms)
    Vth_set: float = 0.8    # SET threshold voltage (V)
    Vth_reset: float = -0.5 # RESET threshold voltage (V)
    tau: float = 0.01       # Time constant (s)
    gamma: float = 0.1      # Nonlinearity parameter


class MemristiveNeuron:
    """
    LIF neuron implemented with Ag/HZO memristor.
    
    Circuit: Vdd --[R]-- Vout --[Memristor]-- Gnd
    """
    
    def __init__(self, params: MemristorParams = None, 
                 R_series: float = 10000, dt: float = 1e-4):
        """
        Initialize memristive neuron.
        
        Args:
            params: Memristor parameters
            R_series: Series current-limiting resistor (Ohms)
            dt: Simulation time step (s)
        """
        self.params = params or MemristorParams()
        self.R_series = R_series
        self.dt = dt
        
        # State variables
        self.V_mem = 0.0      # Membrane voltage
        self.R_mem = self.params.Roff  # Memristor resistance
        self.spike_count = 0
        self.last_spike_time = None
        self.first_spike_time = None
        
        # History
        self.V_history = []
        self.R_history = []
        self.spike_times = []
    
    def integrate(self, I_in: float, t: float) -> bool:
        """
        Integrate input current for one time step.
        
        Args:
            I_in: Input current (A)
            t: Current time (s)
        
        Returns:
            True if spike occurred
        """
        # Update membrane voltage (RC circuit)
        R_total = self.R_series + self.R_mem
        tau_eff = self.params.tau * (R_total / self.R_series)
        
        # Input voltage from current
        V_in = I_in * R_total
        
        # Leaky integration
        dV = (V_in - self.V_mem) / tau_eff * self.dt
        self.V_mem += dV
        
        # Check for threshold crossing (spike)
        spike = False
        if self.V_mem >= self.params.Vth_set and self.R_mem > self.params.Ron:
            # Memristor switches to low resistance (spike)
            self.R_mem = self.params.Ron
            self.spike_count += 1
            self.last_spike_time = t
            if self.first_spike_time is None:
                self.first_spike_time = t
            self.spike_times.append(t)
            spike = True
            
            # Reset voltage after spike
            self.V_mem = 0.0
        
        # Gradual return to high resistance (adaptation)
        if self.R_mem < self.params.Roff:
            self.R_mem += (self.params.Roff - self.R_mem) * 0.01
        
        # Store history
        self.V_history.append(self.V_mem)
        self.R_history.append(self.R_mem)
        
        return spike
    
    def reset(self):
        """Reset neuron state."""
        self.V_mem = 0.0
        self.R_mem = self.params.Roff
        self.spike_count = 0
        self.last_spike_time = None
        self.first_spike_time = None
        self.V_history = []
        self.R_history = []
        self.spike_times = []
    
    def get_ttfs(self) -> Optional[float]:
        """Get Time-to-First-Spike."""
        return self.first_spike_time
    
    def get_spike_count(self) -> int:
        """Get total spike count."""
        return self.spike_count
    
    def get_firing_rate(self, T: float) -> float:
        """Get firing rate in Hz."""
        return self.spike_count / T if T > 0 else 0


class SNNLayer:
    """Layer of memristive neurons."""
    
    def __init__(self, n_neurons: int, params: MemristorParams = None):
        """
        Initialize SNN layer.
        
        Args:
            n_neurons: Number of neurons
            params: Shared memristor parameters
        """
        self.neurons = [MemristiveNeuron(params) for _ in range(n_neurons)]
    
    def simulate(self, input_currents: np.ndarray, T: float) -> dict:
        """
        Simulate layer for duration T.
        
        Args:
            input_currents: [n_neurons, n_steps] input currents
            T: Total simulation time
        
        Returns:
            Dictionary with encoding results
        """
        n_steps = input_currents.shape[1]
        dt = T / n_steps
        
        # Reset all neurons
        for neuron in self.neurons:
            neuron.reset()
        
        # Simulation loop
        for step in range(n_steps):
            t = step * dt
            for i, neuron in enumerate(self.neurons):
                neuron.integrate(input_currents[i, step], t)
        
        # Collect results
        results = {
            'ttfs': [n.get_ttfs() for n in self.neurons],
            'spike_counts': [n.get_spike_count() for n in self.neurons],
            'firing_rates': [n.get_firing_rate(T) for n in self.neurons],
            'V_traces': [n.V_history for n in self.neurons],
            'spike_times': [n.spike_times for n in self.neurons]
        }
        
        return results


def demonstrate_encoding_modes():
    """Demonstrate different encoding modes."""
    # Create neuron
    neuron = MemristiveNeuron()
    
    # Test different input strengths
    input_strengths = [0.5e-6, 1.0e-6, 2.0e-6, 3.0e-6]  # Amps
    T = 0.1  # 100ms simulation
    dt = 1e-4
    n_steps = int(T / dt)
    
    results = []
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for idx, I_amp in enumerate(input_strengths):
        neuron.reset()
        
        # Constant input current
        I_in = np.ones(n_steps) * I_amp
        
        # Simulate
        for step in range(n_steps):
            t = step * dt
            neuron.integrate(I_in[step], t)
        
        # Plot
        ax = axes[idx]
        time = np.arange(n_steps) * dt * 1000  # Convert to ms
        
        ax.plot(time, np.array(neuron.V_history) * 1000, 'b-', label='Vmem (mV)')
        ax.axhline(y=neuron.params.Vth_set * 1000, color='r', 
                   linestyle='--', label='Vth')
        
        # Mark spikes
        for spike_t in neuron.spike_times:
            ax.axvline(x=spike_t * 1000, color='g', alpha=0.5)
        
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Voltage (mV)')
        ax.set_title(f'Input: {I_amp*1e6:.1f}μA | '
                     f'Spikes: {neuron.spike_count} | '
                     f'First: {neuron.first_spike_time*1000:.1f}ms' 
                     if neuron.first_spike_time else 'No spike')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        results.append({
            'input': I_amp,
            'ttfs': neuron.first_spike_time,
            'count': neuron.spike_count,
            'rate': neuron.get_firing_rate(T)
        })
    
    plt.tight_layout()
    plt.savefig('memristive_neuron_encoding.png', dpi=150)
    
    # Print summary
    print("\nEncoding Summary:")
    print("-" * 60)
    print(f"{'Input (μA)':<12} {'TTFS (ms)':<12} {'Count':<8} {'Rate (Hz)':<10}")
    print("-" * 60)
    for r in results:
        ttfs_str = f"{r['ttfs']*1000:.1f}" if r['ttfs'] else "N/A"
        print(f"{r['input']*1e6:<12.1f} {ttfs_str:<12} {r['count']:<8} {r['rate']:<10.1f}")
    
    return results


def compare_encoding_modes():
    """Compare different encoding modes for information transmission."""
    n_neurons = 10
    layer = SNNLayer(n_neurons)
    
    T = 0.5  # 500ms
    dt = 1e-4
    n_steps = int(T / dt)
    
    # Create varying inputs
    stimulus = np.linspace(0.5e-6, 3.0e-6, n_neurons)
    input_currents = np.array([
        np.ones(n_steps) * s for s in stimulus
    ])
    
    # Simulate
    results = layer.simulate(input_currents, T)
    
    print("\nEncoding Mode Comparison:")
    print("-" * 70)
    
    # TTFS encoding
    ttfs_values = [t for t in results['ttfs'] if t is not None]
    if ttfs_values:
        print(f"\n1. TTFS Encoding:")
        print(f"   Range: {min(ttfs_values)*1000:.1f} - {max(ttfs_values)*1000:.1f} ms")
        print(f"   Neurons responding: {len(ttfs_values)}/{n_neurons}")
    
    # Spike count encoding
    counts = results['spike_counts']
    print(f"\n2. Spike Count Encoding:")
    print(f"   Range: {min(counts)} - {max(counts)} spikes")
    print(f"   Average: {np.mean(counts):.1f} spikes")
    
    # Firing rate encoding
    rates = results['firing_rates']
    print(f"\n3. Firing Rate Encoding:")
    print(f"   Range: {min(rates):.1f} - {max(rates):.1f} Hz")
    print(f"   Average: {np.mean(rates):.1f} Hz")
    
    # Correlation with stimulus
    ttfs_corr = np.corrcoef(stimulus[:len(ttfs_values)], ttfs_values)[0,1] if len(ttfs_values) > 1 else 0
    count_corr = np.corrcoef(stimulus, counts)[0,1]
    rate_corr = np.corrcoef(stimulus, rates)[0,1]
    
    print(f"\nStimulus-response correlation:")
    print(f"   TTFS: {ttfs_corr:.3f}")
    print(f"   Count: {count_corr:.3f}")
    print(f"   Rate: {rate_corr:.3f}")


if __name__ == '__main__':
    print("=" * 60)
    print("Memristive Neuron Simulation")
    print("Ag/HZO-based LIF with Multiple Spiking Modes")
    print("=" * 60)
    
    print("\n1. Demonstrating encoding modes...")
    demonstrate_encoding_modes()
    
    print("\n2. Comparing encoding modes...")
    compare_encoding_modes()
    
    print("\n3. Plot saved to: memristive_neuron_encoding.png")
