#!/usr/bin/env python3
"""
Neuromodulatory CPG Control Implementation

Implementation of neuromodulation-based control for robust rhythmic 
pattern transitions in degenerate CPGs with fixed connectivity.

Reference: "Neuromodulation supports robust rhythmic pattern transitions 
in degenerate central pattern generators with fixed connectivity"
arXiv: 2604.08312
"""

import numpy as np
from typing import Callable, List, Optional


class CPGNeuron:
    """
    Individual CPG neuron with neuromodulatory modulation.
    """
    
    def __init__(self, tau: float = 1.0, threshold: float = 0.0, 
                 gain: float = 1.0, adaptation_tau: float = 10.0):
        """
        Initialize CPG neuron.
        
        Args:
            tau: Membrane time constant
            threshold: Firing threshold
            gain: Activation gain
            adaptation_tau: Spike adaptation time constant
        """
        self.tau = tau
        self.threshold = threshold
        self.gain = gain
        self.adaptation_tau = adaptation_tau
        
        self.v = 0.0  # Membrane potential
        self.a = 0.0  # Adaptation current
        self.spike_history = []
        
    def activation(self, x: float) -> float:
        """
        Sigmoid activation function.
        
        Args:
            x: Input current
            
        Returns:
            Activation output
        """
        return 1.0 / (1.0 + np.exp(-self.gain * (x - self.threshold)))
    
    def update(self, input_current: float, neuromod: float, dt: float) -> float:
        """
        Update neuron state.
        
        Args:
            input_current: Synaptic input
            neuromod: Neuromodulatory input
            dt: Time step
            
        Returns:
            Output activity
        """
        # Modulated dynamics
        effective_tau = self.tau / (1.0 + 0.5 * neuromod)
        
        # Membrane dynamics
        dv = (-self.v + input_current - self.a) / effective_tau
        self.v += dv * dt
        
        # Adaptation dynamics
        da = (-self.a + self.v) / self.adaptation_tau
        self.a += da * dt
        
        # Output activity
        activity = self.activation(self.v)
        
        return activity


class DegenerateCPG:
    """
    Degenerate CPG with fixed connectivity and neuromodulatory control.
    """
    
    def __init__(self, n_neurons: int, connectivity_pattern: str = 'chain'):
        """
        Initialize degenerate CPG.
        
        Args:
            n_neurons: Number of neurons in CPG
            connectivity_pattern: Pattern of connectivity ('chain', 'ring', 'all_to_all')
        """
        self.n_neurons = n_neurons
        self.neurons = [CPGNeuron() for _ in range(n_neurons)]
        
        # Fixed connectivity matrix (degenerate structure)
        self.W = self._build_connectivity(connectivity_pattern)
        
        # Neuromodulatory parameters
        self.neuromod_base = 0.0
        self.neuromod_level = 0.0
        
        # Pattern tracking
        self.activity_history = []
        self.phase_history = []
        
    def _build_connectivity(self, pattern: str) -> np.ndarray:
        """
        Build degenerate connectivity matrix.
        
        Args:
            pattern: Connectivity pattern
            
        Returns:
            Weight matrix
        """
        W = np.zeros((self.n_neurons, self.n_neurons))
        
        if pattern == 'chain':
            # Chain-like connectivity with degenerate structure
            for i in range(self.n_neurons - 1):
                W[i, i+1] = 2.0  # Excitatory forward
                W[i+1, i] = -1.5  # Inhibitory backward
                
        elif pattern == 'ring':
            # Ring connectivity
            for i in range(self.n_neurons):
                W[i, (i+1) % self.n_neurons] = 2.0
                W[i, (i-1) % self.n_neurons] = -1.5
                
        elif pattern == 'all_to_all':
            # All-to-all with structured weights
            W = np.random.randn(self.n_neurons, self.n_neurons) * 0.5
            W = (W + W.T) / 2  # Symmetric
            
        # Ensure degeneracy: multiple eigenvalues with similar magnitude
        W = self._ensure_degeneracy(W)
        
        return W
    
    def _ensure_degeneracy(self, W: np.ndarray) -> np.ndarray:
        """
        Modify connectivity to ensure degenerate structure.
        
        Args:
            W: Original weight matrix
            
        Returns:
            Modified weight matrix with degenerate properties
        """
        # Add structured perturbations to create degeneracy
        eigenvalues, eigenvectors = np.linalg.eig(W)
        
        # Cluster similar eigenvalues
        for i in range(1, len(eigenvalues)):
            if abs(eigenvalues[i] - eigenvalues[i-1]) < 0.5:
                eigenvalues[i] = eigenvalues[i-1]
        
        # Reconstruct matrix
        W_degenerate = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)
        
        # Keep real part
        W_degenerate = np.real(W_degenerate)
        
        return W_degenerate
    
    def apply_neuromodulation(self, level: float):
        """
        Apply neuromodulatory input.
        
        Args:
            level: Neuromodulatory level
        """
        self.neuromod_level = level
    
    def step(self, external_input: Optional[np.ndarray] = None, 
             dt: float = 0.01) -> np.ndarray:
        """
        Advance CPG by one time step.
        
        Args:
            external_input: External drive (optional)
            dt: Time step
            
        Returns:
            Current activity
        """
        if external_input is None:
            external_input = np.zeros(self.n_neurons)
        
        # Get current activities
        activities = np.array([n.v for n in self.neurons])
        
        # Compute synaptic inputs
        synaptic_input = self.W @ activities + external_input
        
        # Update each neuron with neuromodulation
        new_activities = []
        for i, neuron in enumerate(self.neurons):
            activity = neuron.update(
                synaptic_input[i], 
                self.neuromod_level, 
                dt
            )
            new_activities.append(activity)
        
        activity_array = np.array(new_activities)
        self.activity_history.append(activity_array.copy())
        
        return activity_array
    
    def simulate(self, duration: float, dt: float = 0.01,
                 neuromod_func: Optional[Callable] = None) -> np.ndarray:
        """
        Simulate CPG dynamics.
        
        Args:
            duration: Simulation duration
            dt: Time step
            neuromod_func: Function defining neuromodulatory input over time
            
        Returns:
            Activity trace [time_steps, n_neurons]
        """
        n_steps = int(duration / dt)
        activities = np.zeros((n_steps, self.n_neurons))
        
        for t in range(n_steps):
            # Update neuromodulation
            if neuromod_func is not None:
                self.apply_neuromodulation(neuromod_func(t * dt))
            
            activities[t] = self.step(dt=dt)
        
        return activities
    
    def identify_pattern(self, activities: np.ndarray, 
                         window_size: int = 100) -> str:
        """
        Identify current rhythmic pattern.
        
        Args:
            activities: Activity trace
            window_size: Window for pattern analysis
            
        Returns:
            Pattern identifier
        """
        if len(activities) < window_size:
            return 'unknown'
        
        recent = activities[-window_size:]
        
        # Compute phase relationships
        phases = np.angle(np.fft.fft(recent, axis=0))
        
        # Count phase-locked relationships
        phase_diffs = []
        for i in range(self.n_neurons):
            for j in range(i+1, self.n_neurons):
                diff = np.abs(phases[:, i] - phases[:, j])
                phase_diffs.append(np.mean(diff))
        
        # Classify based on phase relationships
        avg_phase_diff = np.mean(phase_diffs)
        
        if avg_phase_diff < 0.5:
            return 'synchronous'
        elif avg_phase_diff < 2.0:
            return 'traveling_wave'
        else:
            return 'complex'
    
    def transition_pattern(self, target_pattern: str, 
                          transition_time: float = 2.0) -> Callable:
        """
        Generate neuromodulatory signal for pattern transition.
        
        Args:
            target_pattern: Target pattern to transition to
            transition_time: Duration of transition
            
        Returns:
            Neuromodulation function
        """
        # Define modulation parameters for different patterns
        modulation_profiles = {
            'synchronous': 2.0,
            'traveling_wave': -1.0,
            'complex': 0.5
        }
        
        target_level = modulation_profiles.get(target_pattern, 0.0)
        
        def neuromod_func(t: float) -> float:
            if t < transition_time:
                # Gradual transition
                return self.neuromod_base + (target_level - self.neuromod_base) * (t / transition_time)
            else:
                # Maintain target
                return target_level
        
        return neuromod_func


class PatternTransitionController:
    """
    Controller for robust pattern transitions in CPG.
    """
    
    def __init__(self, cpg: DegenerateCPG):
        """
        Initialize controller.
        
        Args:
            cpg: CPG network to control
        """
        self.cpg = cpg
        self.pattern_sequence = []
        self.transition_history = []
        
    def execute_transition(self, from_pattern: str, to_pattern: str,
                          transition_duration: float = 2.0) -> bool:
        """
        Execute pattern transition.
        
        Args:
            from_pattern: Starting pattern
            to_pattern: Target pattern
            transition_duration: Time for transition
            
        Returns:
            Success flag
        """
        # Generate neuromodulatory control signal
        neuromod_func = self.cpg.transition_pattern(to_pattern, transition_duration)
        
        # Pre-transition phase
        pre_duration = 1.0
        self.cpg.simulate(pre_duration, neuromod_func=lambda t: self.cpg.neuromod_base)
        
        # Transition phase
        activities = self.cpg.simulate(transition_duration, neuromod_func=neuromod_func)
        
        # Verify transition
        final_pattern = self.cpg.identify_pattern(activities)
        success = (final_pattern == to_pattern)
        
        # Record transition
        self.transition_history.append({
            'from': from_pattern,
            'to': to_pattern,
            'success': success,
            'duration': transition_duration
        })
        
        return success
    
    def sequence_transitions(self, pattern_sequence: List[str],
                            dwell_time: float = 3.0) -> List[bool]:
        """
        Execute sequence of pattern transitions.
        
        Args:
            pattern_sequence: Ordered list of patterns
            dwell_time: Time to maintain each pattern
            
        Returns:
            List of success flags
        """
        results = []
        
        for i in range(len(pattern_sequence) - 1):
            # Dwell in current pattern
            self.cpg.simulate(dwell_time)
            
            # Transition to next
            success = self.execute_transition(
                pattern_sequence[i],
                pattern_sequence[i+1]
            )
            results.append(success)
        
        return results


def example_usage():
    """
    Example usage of neuromodulatory CPG control.
    """
    print("Neuromodulatory CPG Control Example")
    print("=" * 50)
    
    # Create CPG
    cpg = DegenerateCPG(n_neurons=6, connectivity_pattern='chain')
    
    # Create controller
    controller = PatternTransitionController(cpg)
    
    # Test pattern transitions
    patterns = ['synchronous', 'traveling_wave', 'synchronous']
    
    print(f"\nExecuting pattern sequence: {' -> '.join(patterns)}")
    
    results = controller.sequence_transitions(patterns, dwell_time=2.0)
    
    print("\nTransition results:")
    for i, (from_p, to_p, success) in enumerate(
        zip(patterns[:-1], patterns[1:], results), 1
    ):
        status = "✓ Success" if success else "✗ Failed"
        print(f"  {i}. {from_p} -> {to_p}: {status}")
    
    print(f"\nTotal transitions: {len(results)}")
    print(f"Successful: {sum(results)}")
    print(f"Success rate: {100*sum(results)/len(results):.1f}%")


if __name__ == "__main__":
    example_usage()
