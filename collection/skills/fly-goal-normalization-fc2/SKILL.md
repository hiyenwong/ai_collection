---
name: fly-goal-normalization-fc2
description: "Analysis of Drosophila FC2 circuit mechanism showing that goal maintenance uses normalization rather than winner-take-all selection, with global inhibition from FB5A neurons keeping a single clean activity bump rather than actively choosing between competing goals."
metadata:
  arxiv_id: "2607.18969"
  published: "2026-07-22"
  authors: ["Gioele Nanni", "Christopher Lee"]
  tags: [neuroscience, drosophila, neural-circuits, ring-attractor, winner-take-all, normalization, fan-shaped-body, FC2, FB5A, hDelta, connectome, spiking-networks]
license: Complete terms in LICENSE.txt
---

# Fly Goal Maintenance via Normalization in Drosophila FC2

A detailed analysis of the neural circuit mechanism in Drosophila's fan-shaped body (FC2 neurons) that maintains a single goal direction during navigation, revealing that it uses normalization rather than winner-take-all selection.

## Core Idea

Walking flies maintain a goal direction as a bump of activity across FC2 neurons in the fan-shaped body. These neurons inhibit each other over distance, which was previously thought to implement a winner-take-all selection mechanism. However, connectome analysis reveals that the inhibition is almost entirely global (from four FB5A cells) rather than local recurrent excitation required for true winner-take-all dynamics. This means FC2 normalizes an externally set goal rather than selecting it actively.

## When to Use

- Studying neural mechanisms of goal maintenance vs. selection
- Analyzing ring-attractor networks and their limitations
- Understanding normalization circuits in neural systems
- Working with Drosophila connectome data and neural circuit tracing
- Modeling spiking networks based on real connectome constraints

## Key Findings

1. **Global inhibition dominates**: FC2 receives ~90% of its inhibition from four FB5A cells that inhibit all FC2 neurons roughly equally, not distance-dependent local inhibition.

2. **No local recurrent excitation**: The FC2 wiring lacks the local recurrent excitation required for ring-attractor winner-take-all dynamics (unlike the compass system).

3. **Normalization, not selection**: Across multiple dynamical models including spiking networks, the circuit cannot lock onto a winner at biologically realistic coupling strengths.

4. **Upstream goal setting**: The connectome identifies an upstream hDelta network as the likely source of goal setting, ruling out alternative proposals.

5. **Testable prediction**: Silencing FB5A while imaging FC2 should disrupt the clean single bump maintenance if the normalization hypothesis is correct.

## Methodology

1. **Connectome analysis**: Traced wiring in a single FlyWire brain to map all inputs to FC2 neurons.

2. **Circuit quantification**: Measured relative contributions of different inhibitory pathways (FB5A global, hDelta distance-dependent, direct FC2-FC2).

3. **Dynamical modeling**: Tested multiple network models (rate-based, spiking) with connectome-scaled coupling strengths.

4. **Comparative analysis**: Contrasted FC2 circuit architecture with known ring-attractor systems like the compass.

## Implementation Sketch

```python
# Simplified FC2 normalization model
class FC2NormalizationNetwork:
    def __init__(self, n_neurons=16):
        self.n = n_neurons
        # Global inhibition from FB5A (dominant)
        self.fb5a_weight = -0.8  
        # Distance-dependent inhibition from hDelta (minor)
        self.hdelta_weights = create_distance_dependent_inhibition(n_neurons, strength=0.15)
        # External goal input (from upstream hDelta network)
        self.goal_input = np.zeros(n_neurons)
        
    def update(self, dt=0.01):
        # Activity dynamics with global normalization
        total_activity = np.sum(self.activity)
        fb5a_inhibition = self.fb5a_weight * total_activity
        hdelta_inhibition = self.hdelta_weights @ self.activity
        total_inhibition = fb5a_inhibition + hdelta_inhibition
        
        # Update with external goal input
        self.activity += dt * (-self.activity + np.maximum(0, self.goal_input + total_inhibition))
```

## Interpretation

- Neural systems can maintain stable representations through normalization without implementing full winner-take-all selection.
- Global inhibition (like APL in mushroom body) is a common motif for maintaining sparse, clean activity patterns.
- Connectome-scale circuit analysis is essential for distinguishing between superficially similar computational mechanisms.
- Goal setting and goal maintenance can be implemented by separate neural subsystems.

## Pitfalls

- FB5A's inhibitory identity is a low-confidence prediction from the connectome's transmitter classifier, not yet experimentally verified.
- Mutual inhibition between competing goals via hDelta could theoretically implement selection at very strong coupling (though bounded as unlikely).
- Single-brain connectome analysis may miss inter-individual variability in circuit structure.

## Related Concepts

- Ring attractor networks
- Winner-take-all vs. normalization
- Global inhibition motifs
- Drosophila navigation circuits
- Fan-shaped body (central complex)
- Connectome-based circuit analysis
- Spiking network modeling
- Goal-directed behavior
- Neural bump attractors

## Activation

fly goal maintenance, Drosophila FC2, fan-shaped body, normalization circuit, global inhibition, FB5A, hDelta, ring attractor, winner-take-all, connectome analysis, neural bump attractor, goal setting vs maintenance, spiking network modeling