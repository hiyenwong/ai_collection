---
name: hamilton-jacobi-reachability-analysis
description: "Use for Hamilton-Jacobi reachability analysis and GRA tasks."
---

# Hamilton-Jacobi Reachability Analysis Framework

This skill implements the methodology from the arXiv paper "Extending and Unifying the Fundamental Tasks of Hamilton-Jacobi Reachability Analysis" (arXiv:2608.18060v1). It provides a comprehensive framework for Hamilton-Jacobi Reachability (HJR) analysis using the Generalized Reach-Avoid (GRA) task formulation.

## Core Contributions

- **Generalized Reach-Avoid (GRA) Task**: Extends and unifies canonical HJR tasks into a single framework
- **Composite Task Decomposition**: Enables computation of value functions for complex tasks (including timed temporal logic) by decomposing into GRA primitives
- **PDE Perspective**: Shows GRA as a natural primitive for representing solutions of Hamilton-Jacobi PDEs
- **Theoretical Foundation**: Provides rigorous mathematical framework for HJR analysis

## Use Cases

- **Control Systems Verification**: Verify safety and reachability properties of dynamical systems
- **Autonomous Systems**: Analyze reachability for autonomous vehicles, robotics, and CPS
- **Formal Methods**: Integrate with formal verification tools for hybrid systems
- **Temporal Logic**: Handle complex specifications involving timed temporal logic
- **Safety-Critical Systems**: Ensure safety guarantees in critical applications

## Implementation Workflow

### Step 1: Problem Formulation
1. Define the dynamical system: $\dot{x} = f(x, u)$
2. Specify target sets, avoid sets, and time horizons
3. Formulate as a Generalized Reach-Avoid (GRA) task

### Step 2: Value Function Computation
1. Set up the Hamilton-Jacobi PDE corresponding to the GRA task
2. Compute the value function using numerical methods (level set methods, etc.)
3. Handle composite tasks by decomposing into GRA primitives

### Step 3: Analysis and Verification
1. Extract reachable sets from the value function
2. Verify safety and liveness properties
3. Generate certificates for formal verification

### Step 4: Integration with Temporal Logic
1. Decompose complex temporal logic specifications into GRA tasks
2. Compute value functions for each component
3. Combine results for overall system verification

## Mathematical Framework

### Generalized Reach-Avoid Task
The GRA task is defined by:
- Target set $\\mathcal{T}$
- Avoid set $\\mathcal{A}$  
- Time horizon $[t_0, t_f]$
- Cost function $l(x, u)$

### Hamilton-Jacobi PDE
The value function $V(t, x)$ satisfies:
$$
\\frac{\\partial V}{\\partial t} + \\min_{u \\in \\mathcal{U}} \\left\\{ \\nabla_x V \\cdot f(x, u) + l(x, u) \\right\\} = 0
$$
with appropriate boundary conditions.

### Composite Task Decomposition
For complex specifications $\\phi$, decompose into:
$$
\\phi = \\bigwedge_{i=1}^n \\text{GRA}_i
$$
Compute individual value functions $V_i$ and combine appropriately.

## Tools and Libraries

### Recommended Software
- **Level Set Toolbox**: MATLAB toolbox for level set methods
- **HJReachability.jl**: Julia package for Hamilton-Jacobi reachability
- **CORA**: MATLAB toolbox for reachability analysis of continuous and hybrid systems
- **SpaceEx**: Tool for verification of hybrid systems

### Python Implementation Outline
```python
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

class HamiltonJacobiReachability:
    def __init__(self, dynamics, target_set, avoid_set, time_horizon):
        self.dynamics = dynamics  # f(x, u)
        self.target_set = target_set
        self.avoid_set = avoid_set
        self.time_horizon = time_horizon
        
    def setup_pde(self):
        """Set up the Hamilton-Jacobi PDE"""
        # Implementation depends on specific dynamics and sets
        pass
        
    def compute_value_function(self, grid):
        """Compute value function on given grid"""
        # Use level set methods or other numerical schemes
        pass
        
    def extract_reachable_sets(self, value_function, threshold=0):
        """Extract reachable sets from value function"""
        return value_function <= threshold
```

## Best Practices

1. **Grid Resolution**: Use adaptive grid refinement for accuracy vs. computational cost trade-off
2. **Dimensionality**: For high-dimensional systems, consider decomposition or approximation methods
3. **Numerical Stability**: Ensure proper treatment of Hamiltonian terms for stability
4. **Verification**: Always validate results with simulation or alternative methods
5. **Composition**: Leverage GRA decomposition for complex specifications

## Pitfalls to Avoid

- **Curse of Dimensionality**: HJR scales poorly with state dimension; consider alternatives for high-D systems
- **Numerical Artifacts**: Level set methods can introduce numerical diffusion; use appropriate schemes
- **Boundary Conditions**: Incorrect boundary conditions lead to wrong value functions
- **Dynamics Assumptions**: Ensure dynamics satisfy required regularity conditions
- **Time Discretization**: Choose appropriate time step for stability and accuracy

## Related Research

- **Hamilton-Jacobi Reachability**: Original framework for reachability analysis
- **Level Set Methods**: Numerical methods for solving HJ PDEs
- **Hybrid Systems**: Extension to systems with discrete transitions
- **Temporal Logic**: Integration with formal specification languages
- **Robust Control**: Connection to robust and optimal control theory

## References

- Mitchell, I. M., Bayen, A. M., & Tomlin, C. J. (2005). A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games.
- Bokanowski, O., Cheng, Y., & Shu, C.-W. (2013). A multilevel discontinuous Galerkin method for Hamilton-Jacobi-Bellman equations.
- Chen, M., Herbert, S. L., & Tomlin, C. J. (2018). Fast reachable set approximations via implicit representations.

## Activation Keywords

- Hamilton-Jacobi reachability
- HJR analysis
- reachability analysis
- control systems verification
- GRA tasks
- generalized reach-avoid
- value function computation
- temporal logic verification
- safety verification
- autonomous systems analysis