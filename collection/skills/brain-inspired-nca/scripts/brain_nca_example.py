#!/usr/bin/env python3
"""
BraiNCA: Brain-inspired Neural Cellular Automata Example

Simple implementation demonstrating brain-inspired topology
for pattern formation (morphogenesis).

Reference: arXiv:2604.01932
"""

import numpy as np
import networkx as nx
from scipy.special import expit as sigmoid

def create_brain_topology(n_cells=100, topology_type='small_world'):
    """Create brain-inspired network topology.
    
    Args:
        n_cells: Number of cells/units
        topology_type: 'small_world', 'scale_free', or 'modular'
    
    Returns:
        G: NetworkX graph representing topology
    """
    if topology_type == 'small_world':
        # Watts-Strogatz small-world network
        G = nx.watts_strogatz_graph(n=n_cells, k=8, p=0.1)
    elif topology_type == 'scale_free':
        # Barabási-Albert scale-free network
        G = nx.barabasi_albert_graph(n=n_cells, m=4)
    elif topology_type == 'modular':
        # Modular network (3 modules)
        module_size = n_cells // 3
        G = nx.random_partition_graph(
            sizes=[module_size, module_size, module_size],
            p_in=0.3, p_out=0.05
        )
    else:
        raise ValueError(f"Unknown topology type: {topology_type}")
    
    return G

def initialize_pattern(n_cells, pattern_type='random'):
    """Initialize pattern for morphogenesis.
    
    Args:
        n_cells: Number of cells
        pattern_type: 'random', 'center', or 'edge'
    
    Returns:
        state: Initial state vector
    """
    if pattern_type == 'random':
        state = np.random.rand(n_cells)
    elif pattern_type == 'center':
        state = np.zeros(n_cells)
        center = n_cells // 2
        state[center-5:center+5] = 1.0
    elif pattern_type == 'edge':
        state = np.zeros(n_cells)
        state[:10] = 1.0
        state[-10:] = 1.0
    else:
        raise ValueError(f"Unknown pattern type: {pattern_type}")
    
    return state

def brain_nca_update(state, G, weights=None):
    """Update state using brain-inspired NCA rules.
    
    Args:
        state: Current state vector
        G: Network topology
        weights: Optional weight dictionary
    
    Returns:
        new_state: Updated state vector
    """
    if weights is None:
        weights = {'local': 0.8, 'long_range': 0.2}
    
    new_state = np.zeros_like(state)
    
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        
        if len(neighbors) == 0:
            new_state[node] = state[node]
            continue
        
        # Compute weighted input from neighbors
        neighbor_states = state[neighbors]
        input_sum = np.mean(neighbor_states)
        
        # Apply neural-like activation
        new_state[node] = sigmoid(input_sum)
    
    return new_state

def run_morphogenesis_simulation(n_cells=100, n_steps=50, 
                                  topology_type='small_world',
                                  pattern_type='center'):
    """Run complete morphogenesis simulation.
    
    Args:
        n_cells: Number of cells
        n_steps: Number of simulation steps
        topology_type: Network topology type
        pattern_type: Initial pattern type
    
    Returns:
        history: List of state vectors at each step
        G: Final topology
    """
    # Create topology
    G = create_brain_topology(n_cells, topology_type)
    
    # Initialize pattern
    state = initialize_pattern(n_cells, pattern_type)
    
    # Run simulation
    history = [state.copy()]
    for t in range(n_steps):
        state = brain_nca_update(state, G)
        history.append(state.copy())
    
    return history, G

def visualize_state(state, title="BraiNCA State"):
    """Simple text visualization of state.
    
    Args:
        state: State vector
        title: Title for display
    """
    print(f"\n{title}")
    print("-" * 40)
    
    # Create simple bar representation
    bars = []
    for val in state:
        bar_len = int(val * 20)
        bars.append('█' * bar_len + '░' * (20 - bar_len))
    
    # Print every 10th cell for compact view
    for i in range(0, len(bars), 10):
        print(f"Cell {i:3d}: {bars[i]} | {state[i]:.3f}")

def main():
    """Run example BraiNCA simulation."""
    print("="*50)
    print("BraiNCA: Brain-inspired Neural Cellular Automata")
    print("="*50)
    
    # Configuration
    n_cells = 100
    n_steps = 30
    
    print("\n[1] Creating brain-inspired topology...")
    G = create_brain_topology(n_cells, 'small_world')
    print(f"    Nodes: {G.number_of_nodes()}")
    print(f"    Edges: {G.number_of_edges()}")
    print(f"    Avg degree: {np.mean([d for n, d in G.degree()]):.2f}")
    
    print("\n[2] Initializing pattern...")
    state = initialize_pattern(n_cells, 'center')
    visualize_state(state, "Initial Pattern")
    
    print("\n[3] Running morphogenesis simulation...")
    history, G = run_morphogenesis_simulation(
        n_cells=n_cells,
        n_steps=n_steps,
        topology_type='small_world',
        pattern_type='center'
    )
    
    print("\n[4] Final state...")
    visualize_state(history[-1], f"Final Pattern (Step {n_steps})")
    
    print("\n[5] Pattern evolution (every 5 steps):")
    for i in [0, 5, 10, 15, 20, 25, 30]:
        if i < len(history):
            avg_val = np.mean(history[i])
            print(f"    Step {i:3d}: Avg activation = {avg_val:.4f}")
    
    print("\n" + "="*50)
    print("Simulation complete!")
    print("="*50)

if __name__ == '__main__':
    main()