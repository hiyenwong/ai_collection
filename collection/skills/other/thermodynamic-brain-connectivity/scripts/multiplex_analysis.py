#!/usr/bin/env python3
"""
Multiplex Brain Network Analysis Script

Implements thermodynamic connectivity analysis for brain networks,
revealing functional specialization across synaptic and extrasynaptic layers.

Based on: Sunil et al. (2026) arXiv:2604.02057
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class CommunicationRegime(Enum):
    """Four communication regimes in multiplex neural networks."""
    TOPOLOGY_DEPENDENT = "topology_dependent"  # Reinforces synaptic motor circuits
    TOPOLOGY_RESILIENT = "topology_resilient"  # Global regulation, behavioral state
    PURE_EXTRASYNAPTIC = "pure_extrasynaptic"  # Survival and homeostasis
    PURE_SYNAPTIC = "pure_synaptic"  # Rapid sensorimotor processing


@dataclass
class ThermodynamicProperties:
    """Thermodynamic properties of a neural network."""
    entropy: float
    free_energy: float
    temperature: float
    energy: float


@dataclass  
class MultiplexNetwork:
    """Multiplex network with synaptic and extrasynaptic layers."""
    synaptic_functional: np.ndarray
    extrasynaptic: np.ndarray
    node_labels: List[str]
    coupling: Optional[np.ndarray] = None


class ThermodynamicBrainAnalyzer:
    """
    Analyzer for thermodynamic connectivity in brain networks.
    
    Implements the framework from Sunil et al. (2026) for inferring
    functional connectivity from structural connectomes using
    statistical physics principles.
    """
    
    def __init__(self, temperature: float = 1.0):
        """
        Initialize analyzer.
        
        Parameters:
        -----------
        temperature : float
            Effective temperature parameter (default: 1.0)
        """
        self.temperature = temperature
    
    def infer_functional_connectivity(
        self, 
        synaptic_connectome: np.ndarray,
        method: str = "boltzmann"
    ) -> np.ndarray:
        """
        Infer functional connectivity from synaptic structure.
        
        Uses equilibrium principles from statistical physics to compute
        probabilistic maps of information flow.
        
        Parameters:
        -----------
        synaptic_connectome : ndarray
            Weighted adjacency matrix of synaptic connections
        method : str
            Inference method: "boltzmann" or "max_entropy"
        
        Returns:
        --------
        functional_connectivity : ndarray
            Probabilistic map of information flow
        """
        if method == "boltzmann":
            # Boltzmann-like distribution: P ~ exp(-E/kT)
            # Higher weights = lower energy = higher probability
            max_weight = np.max(synaptic_connectome)
            if max_weight > 0:
                energy = -synaptic_connectome / max_weight  # Normalize
                functional = np.exp(energy / self.temperature)
                # Normalize rows to get probability distribution
                row_sums = functional.sum(axis=1, keepdims=True)
                functional = functional / (row_sums + 1e-10)
            else:
                functional = np.eye(len(synaptic_connectome))
        
        elif method == "max_entropy":
            # Maximum entropy / Ising model approach
            # Simplified: use correlation-based functional connectivity
            functional = np.corrcoef(synaptic_connectome)
            functional = np.nan_to_num(functional, nan=0.0, posinf=0.0, neginf=0.0)
        
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return functional
    
    def build_multiplex_network(
        self,
        synaptic_structural: np.ndarray,
        extrasynaptic: np.ndarray,
        node_labels: Optional[List[str]] = None
    ) -> MultiplexNetwork:
        """
        Construct multiplex network from synaptic and extrasynaptic layers.
        
        Parameters:
        -----------
        synaptic_structural : ndarray
            Structural synaptic connectivity
        extrasynaptic : ndarray
            Extrasynaptic/modulatory connectivity
        node_labels : list, optional
            Names for each node
        
        Returns:
        --------
        MultiplexNetwork
            Combined multiplex network structure
        """
        # Infer functional connectivity from structural
        synaptic_functional = self.infer_functional_connectivity(synaptic_structural)
        
        # Compute inter-layer coupling
        coupling = self._compute_layer_coupling(
            synaptic_functional, 
            extrasynaptic
        )
        
        if node_labels is None:
            node_labels = [f"node_{i}" for i in range(len(synaptic_structural))]
        
        return MultiplexNetwork(
            synaptic_functional=synaptic_functional,
            extrasynaptic=extrasynaptic,
            node_labels=node_labels,
            coupling=coupling
        )
    
    def _compute_layer_coupling(
        self, 
        synaptic: np.ndarray, 
        extrasynaptic: np.ndarray
    ) -> np.ndarray:
        """Compute coupling strength between network layers."""
        # Mutual information approximation
        # Higher correlation between layers = stronger coupling
        synaptic_flat = synaptic.flatten()
        extrasynaptic_flat = extrasynaptic.flatten()
        
        # Correlation as proxy for mutual information
        correlation = np.corrcoef(synaptic_flat, extrasynaptic_flat)[0, 1]
        if np.isnan(correlation):
            correlation = 0.0
        
        return np.array([[1.0, correlation], [correlation, 1.0]])
    
    def classify_communication_regimes(
        self,
        multiplex: MultiplexNetwork,
        synaptic_threshold: float = 0.5,
        extrasynaptic_threshold: float = 0.3,
        correlation_threshold: float = 0.5
    ) -> Dict[CommunicationRegime, List[int]]:
        """
        Classify nodes into four communication regimes.
        
        Parameters:
        -----------
        multiplex : MultiplexNetwork
            The multiplex network to analyze
        synaptic_threshold : float
            Threshold for synaptic activity classification
        extrasynaptic_threshold : float
            Threshold for extrasynaptic activity classification
        correlation_threshold : float
            Threshold for structure-function correlation
        
        Returns:
        --------
        dict
            Mapping from regime to list of node indices
        """
        n_nodes = len(multiplex.node_labels)
        regimes = {regime: [] for regime in CommunicationRegime}
        
        for i in range(n_nodes):
            # Compute node strengths
            synaptic_strength = np.sum(multiplex.synaptic_functional[i])
            extrasynaptic_strength = np.sum(multiplex.extrasynaptic[i])
            
            # Compute structure-function correlation for this node
            structure_correlation = self._compute_node_correlation(
                multiplex.synaptic_functional, i
            )
            
            # Classify into regime
            if synaptic_strength > synaptic_threshold:
                if structure_correlation > correlation_threshold:
                    regimes[CommunicationRegime.TOPOLOGY_DEPENDENT].append(i)
                else:
                    regimes[CommunicationRegime.TOPOLOGY_RESILIENT].append(i)
            else:
                if extrasynaptic_strength > extrasynaptic_threshold:
                    regimes[CommunicationRegime.PURE_EXTRASYNAPTIC].append(i)
                elif synaptic_strength > extrasynaptic_threshold:
                    regimes[CommunicationRegime.PURE_SYNAPTIC].append(i)
        
        return regimes
    
    def _compute_node_correlation(self, connectivity: np.ndarray, node_idx: int) -> float:
        """Compute structure-function correlation for a node."""
        # Simplified: correlation between node's connections and global structure
        node_connections = connectivity[node_idx]
        mean_structure = np.mean(connectivity, axis=0)
        
        correlation = np.corrcoef(node_connections, mean_structure)[0, 1]
        return correlation if not np.isnan(correlation) else 0.0
    
    def compute_thermodynamic_properties(
        self, 
        connectivity: np.ndarray
    ) -> ThermodynamicProperties:
        """
        Compute thermodynamic properties of a neural network.
        
        Parameters:
        -----------
        connectivity : ndarray
            Connectivity matrix
        
        Returns:
        --------
        ThermodynamicProperties
            Entropy, free energy, temperature, and energy
        """
        # Shannon entropy of connectivity distribution
        probs = connectivity / (np.sum(connectivity) + 1e-10)
        entropy = -np.sum(probs * np.log(probs + 1e-10))
        
        # Energy (Hamiltonian analog)
        energy = -np.sum(connectivity * connectivity) / 2
        
        # Free energy: F = E - TS
        free_energy = energy - self.temperature * entropy
        
        return ThermodynamicProperties(
            entropy=entropy,
            free_energy=free_energy,
            temperature=self.temperature,
            energy=energy
        )
    
    def analyze_multiplex(
        self,
        synaptic_structural: np.ndarray,
        extrasynaptic: np.ndarray,
        node_labels: Optional[List[str]] = None
    ) -> Dict:
        """
        Complete multiplex network analysis.
        
        Parameters:
        -----------
        synaptic_structural : ndarray
            Structural synaptic connectivity
        extrasynaptic : ndarray
            Extrasynaptic/modulatory connectivity
        node_labels : list, optional
            Names for each node
        
        Returns:
        --------
        dict
            Complete analysis results
        """
        # Build multiplex network
        multiplex = self.build_multiplex_network(
            synaptic_structural, extrasynaptic, node_labels
        )
        
        # Classify regimes
        regimes = self.classify_communication_regimes(multiplex)
        
        # Compute thermodynamic properties
        synaptic_thermo = self.compute_thermodynamic_properties(
            multiplex.synaptic_functional
        )
        extrasynaptic_thermo = self.compute_thermodynamic_properties(
            multiplex.extrasynaptic
        )
        
        # Compute multiplex metrics
        multiplex_metrics = self._compute_multiplex_metrics(multiplex)
        
        return {
            'multiplex_network': multiplex,
            'regimes': regimes,
            'synaptic_thermodynamics': synaptic_thermo,
            'extrasynaptic_thermodynamics': extrasynaptic_thermo,
            'multiplex_metrics': multiplex_metrics
        }
    
    def _compute_multiplex_metrics(self, multiplex: MultiplexNetwork) -> Dict:
        """Compute multiplex network metrics."""
        n = len(multiplex.node_labels)
        
        # Multiplex participation coefficient
        # Measures how evenly a node distributes its connectivity across layers
        participation = []
        for i in range(n):
            synaptic_strength = np.sum(multiplex.synaptic_functional[i])
            extrasynaptic_strength = np.sum(multiplex.extrasynaptic[i])
            total = synaptic_strength + extrasynaptic_strength
            if total > 0:
                p_syn = synaptic_strength / total
                p_extra = extrasynaptic_strength / total
                # Participation: 1 - (p1^2 + p2^2) normalized
                part = 1 - (p_syn**2 + p_extra**2)
                participation.append(part)
            else:
                participation.append(0)
        
        # Inter-layer mutual information
        syn_flat = multiplex.synaptic_functional.flatten()
        extra_flat = multiplex.extrasynaptic.flatten()
        mutual_info = self._compute_mutual_information(syn_flat, extra_flat)
        
        return {
            'participation_coefficient': np.mean(participation),
            'inter_layer_mutual_info': mutual_info,
            'layer_coupling': multiplex.coupling[0, 1] if multiplex.coupling is not None else 0
        }
    
    def _compute_mutual_information(self, x: np.ndarray, y: np.ndarray) -> float:
        """Compute mutual information between two distributions."""
        # Simplified: use correlation as proxy
        correlation = np.corrcoef(x, y)[0, 1]
        if np.isnan(correlation):
            return 0.0
        # Approximate MI from correlation for Gaussian
        return -0.5 * np.log(1 - correlation**2) if abs(correlation) < 1 else 0.0


def generate_example_data(n_nodes: int = 100) -> Tuple[np.ndarray, np.ndarray]:
    """Generate example multiplex network data."""
    # Synaptic connectivity: sparse, structured
    synaptic = np.random.exponential(0.5, (n_nodes, n_nodes))
    synaptic = (synaptic + synaptic.T) / 2  # Symmetric
    np.fill_diagonal(synaptic, 0)
    
    # Extrasynaptic connectivity: more diffuse
    extrasynaptic = np.random.exponential(0.3, (n_nodes, n_nodes))
    extrasynaptic = (extrasynaptic + extrasynaptic.T) / 2
    np.fill_diagonal(extrasynaptic, 0)
    
    return synaptic, extrasynaptic


def main():
    """Example usage of the analyzer."""
    print("Thermodynamic Brain Connectivity Analysis")
    print("=" * 50)
    
    # Generate example data
    synaptic, extrasynaptic = generate_example_data(n_nodes=50)
    node_labels = [f"neuron_{i}" for i in range(50)]
    
    print(f"\nInput data:")
    print(f"  Synaptic connections: {np.sum(synaptic > 0.1)} non-zero")
    print(f"  Extrasynaptic connections: {np.sum(extrasynaptic > 0.1)} non-zero")
    
    # Run analysis
    analyzer = ThermodynamicBrainAnalyzer(temperature=1.0)
    results = analyzer.analyze_multiplex(synaptic, extrasynaptic, node_labels)
    
    # Print results
    print(f"\nCommunication Regimes:")
    for regime, nodes in results['regimes'].items():
        print(f"  {regime.value}: {len(nodes)} nodes")
    
    print(f"\nThermodynamic Properties (Synaptic Layer):")
    thermo = results['synaptic_thermodynamics']
    print(f"  Entropy: {thermo.entropy:.3f}")
    print(f"  Free Energy: {thermo.free_energy:.3f}")
    print(f"  Temperature: {thermo.temperature:.3f}")
    
    print(f"\nMultiplex Metrics:")
    metrics = results['multiplex_metrics']
    print(f"  Participation Coefficient: {metrics['participation_coefficient']:.3f}")
    print(f"  Inter-layer Mutual Info: {metrics['inter_layer_mutual_info']:.3f}")
    print(f"  Layer Coupling: {metrics['layer_coupling']:.3f}")


if __name__ == "__main__":
    main()
