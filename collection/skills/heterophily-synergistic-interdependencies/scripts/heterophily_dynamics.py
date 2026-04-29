"""
Heterophily-driven Synergistic Dynamics Simulation

This script implements the heterophily mechanism for generating
self-organized synergistic interdependencies in adaptive networks.

Reference: arXiv:2604.11545v1
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict


class HeterophilyNetwork:
    """
    Adaptive network with heterophily-driven coupling dynamics.
    """
    
    def __init__(self, N: int, gamma: float = 0.1, epsilon: float = 0.01, 
                 beta: float = 1.0, seed: int = None):
        """
        Initialize heterophily network.
        
        Args:
            N: Number of nodes
            gamma: Heterophily strength
            epsilon: Learning rate for coupling updates
            beta: Inverse temperature for state updates
            seed: Random seed
        """
        if seed:
            np.random.seed(seed)
        
        self.N = N
        self.gamma = gamma
        self.epsilon = epsilon
        self.beta = beta
        
        # Initialize states (-1 or +1)
        self.s = np.random.choice([-1, 1], N)
        
        # Initialize symmetric coupling matrix
        self.J = np.random.randn(N, N) * 0.1
        self.J = (self.J + self.J.T) / 2
        np.fill_diagonal(self.J, 0)
        
        # History tracking
        self.history = {
            'states': [],
            'couplings': [],
            'pairwise_mi': [],
            'triple_corr': []
        }
    
    def update_states(self):
        """Update node states based on local field."""
        h = self.J @ self.s  # Local field
        # Probabilistic update with temperature
        p_flip = 1 / (1 + np.exp(-2 * self.beta * h))
        self.s = np.where(np.random.random(self.N) < p_flip, 1, -1)
    
    def update_couplings(self):
        """Update couplings with heterophily mechanism."""
        for i in range(self.N):
            for j in range(i + 1, self.N):
                # Base Hebbian learning
                delta_J = self.epsilon * (self.s[i] * self.s[j] - 0.1 * self.J[i, j])
                
                # Heterophily correction: strengthen different, weaken same
                if self.s[i] != self.s[j]:
                    delta_J += self.gamma * self.epsilon
                else:
                    delta_J -= self.gamma * self.epsilon * 0.5
                
                self.J[i, j] += delta_J
                self.J[j, i] = self.J[i, j]
    
    def compute_pairwise_mi(self) -> float:
        """Compute average pairwise mutual information proxy."""
        pairwise = 0
        count = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                pairwise += self.J[i, j] * self.s[i] * self.s[j]
                count += 1
        return pairwise / count if count > 0 else 0
    
    def compute_triple_correlation(self) -> float:
        """Compute average triple correlation (high-order)."""
        if self.N < 3:
            return 0
        triple = 0
        count = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                for k in range(j + 1, self.N):
                    triple += self.s[i] * self.s[j] * self.s[k]
                    count += 1
        return triple / count if count > 0 else 0
    
    def step(self):
        """Execute one simulation step."""
        self.update_states()
        self.update_couplings()
    
    def run(self, T: int, record_interval: int = 100) -> Dict:
        """
        Run simulation for T steps.
        
        Args:
            T: Number of time steps
            record_interval: Interval for recording history
        
        Returns:
            History dictionary with trajectories
        """
        for t in range(T):
            self.step()
            
            if t % record_interval == 0:
                self.history['states'].append(self.s.copy())
                self.history['couplings'].append(self.J.copy())
                self.history['pairwise_mi'].append(self.compute_pairwise_mi())
                self.history['triple_corr'].append(self.compute_triple_correlation())
        
        return self.history
    
    def compute_synergy_index(self) -> float:
        """
        Compute synergy index as ratio of high-order to total dependencies.
        
        Returns:
            Synergy index (0 to 1)
        """
        pairwise = np.abs(self.compute_pairwise_mi())
        triple = np.abs(self.compute_triple_correlation())
        
        total = pairwise + triple + 1e-8
        return triple / total


def analyze_heterophily_phase_transition(N: int = 20, 
                                         gamma_range: np.ndarray = None,
                                         T: int = 5000) -> Dict:
    """
    Analyze phase transition as function of heterophily strength.
    
    Args:
        N: Network size
        gamma_range: Range of gamma values to test
        T: Simulation steps per gamma
    
    Returns:
        Dictionary with phase transition data
    """
    if gamma_range is None:
        gamma_range = np.linspace(0, 0.5, 20)
    
    results = {
        'gamma': [],
        'pairwise_dep': [],
        'triple_corr': [],
        'synergy_index': []
    }
    
    for gamma in gamma_range:
        net = HeterophilyNetwork(N, gamma=gamma, seed=42)
        history = net.run(T, record_interval=T//10)
        
        # Average over last few recordings
        results['gamma'].append(gamma)
        results['pairwise_dep'].append(np.mean(history['pairwise_mi'][-5:]))
        results['triple_corr'].append(np.mean(history['triple_corr'][-5:]))
        results['synergy_index'].append(net.compute_synergy_index())
    
    return results


def plot_phase_transition(results: Dict):
    """Plot phase transition analysis."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    gamma = results['gamma']
    
    # Pairwise dependency
    axes[0].plot(gamma, results['pairwise_dep'], 'b-', linewidth=2)
    axes[0].set_xlabel('Heterophily Strength (γ)')
    axes[0].set_ylabel('Pairwise Dependency')
    axes[0].set_title('Pairwise Dependencies vs Heterophily')
    axes[0].grid(True, alpha=0.3)
    
    # Triple correlation
    axes[1].plot(gamma, results['triple_corr'], 'r-', linewidth=2)
    axes[1].set_xlabel('Heterophily Strength (γ)')
    axes[1].set_ylabel('Triple Correlation')
    axes[1].set_title('High-Order Dependencies vs Heterophily')
    axes[1].grid(True, alpha=0.3)
    
    # Synergy index
    axes[2].plot(gamma, results['synergy_index'], 'g-', linewidth=2)
    axes[2].set_xlabel('Heterophily Strength (γ)')
    axes[2].set_ylabel('Synergy Index')
    axes[2].set_title('Synergy Index vs Heterophily')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    # Example usage
    print("Running heterophily network simulation...")
    
    # Single simulation
    net = HeterophilyNetwork(N=30, gamma=0.15, seed=42)
    history = net.run(T=2000, record_interval=100)
    
    print(f"\nFinal synergy index: {net.compute_synergy_index():.3f}")
    print(f"Final pairwise dependency: {net.compute_pairwise_mi():.3f}")
    print(f"Final triple correlation: {net.compute_triple_correlation():.3f}")
    
    # Phase transition analysis
    print("\nRunning phase transition analysis...")
    results = analyze_heterophily_phase_transition(N=20, T=3000)
    
    # Find optimal heterophily for synergy
    max_synergy_idx = np.argmax(results['synergy_index'])
    optimal_gamma = results['gamma'][max_synergy_idx]
    print(f"\nOptimal heterophily strength: γ = {optimal_gamma:.3f}")
    print(f"Maximum synergy index: {results['synergy_index'][max_synergy_idx]:.3f}")
    
    # Plot results
    fig = plot_phase_transition(results)
    plt.savefig('heterophily_phase_transition.png', dpi=150)
    print("\nPhase transition plot saved to heterophily_phase_transition.png")
