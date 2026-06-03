---
name: probabilistic-compositional-inference
description: Probabilistic Compositional Inference methodology for coupled engineered systems - graph-based architecture for uncertainty-aware inverse inference
version: 1.0
created: 2026-05-29
source: arXiv:2605.27544
authors: Esmaeil Ghorbani, Jürgen Hackl (Princeton University)
tags:
  - systems-engineering
  - digital-twins
  - uncertainty-quantification
  - distributed-inference
  - message-passing
  - coupled-systems
  - infrastructure
activation_keywords:
  - coupled systems
  - subsystem inference
  - distributed estimation
  - uncertainty propagation
  - digital twins
  - message passing
  - compositional inference
  - interface messages
related_skills:
  - digital-twin-multi-agent-consensus
  - distributed-control-prototyping-framework
  - equation-free-digital-twins
---

# Probabilistic Compositional Inference for Coupled Engineered Systems

## Core Contribution

Probabilistic Compositional Inference (PCI) is a graph-based architecture for solving inverse problems in coupled engineered infrastructure systems. It enables scalable, uncertainty-aware inference across heterogeneous subsystems by representing systems as directed graphs of interacting components, each maintaining local models and estimators while coupling is handled through probabilistic interface messages.

**Key Innovation**: Exploits subsystem structure as an inferential resource rather than treating it as a computational obstacle, transforming coupled inverse problems from monolithic global estimation to distributed message passing.

## Methodology

### 1. Graph-Based System Representation

**Directed Graph Structure**:
- **Nodes**: Subsystems with local models $\mathcal{M}_i$ and estimators maintaining posteriors over states and parameters
- **Edges**: Interface laws $h_{ji}$ transforming outgoing interface variables to incoming coupling effects
- Interface variables: physically meaningful quantities (forces, flows, currents, torques)

**Local Model Diversity**:
- Mechanistic models (physics-based equations)
- Data-driven surrogates (learned from data)
- Hybrid models (combining mechanistic + learned)
- Different estimator classes per subsystem (UKF, EKF, particle filters)

### 2. Probabilistic Interface Messages

**Three Interface Variants**:
1. **Deterministic**: Mean-only messages (uncertainty-blind)
2. **Probabilistic**: Mean + covariance (uncertainty-aware)
3. **Learned**: Data-driven interface laws when physics incomplete

**Uncertainty Propagation Mechanism**:
```python
# Interface force variance from posterior covariance
var(F_b) = a^T (P_s1 + P_s2) a

# Where:
# - a: interface coefficients (stiffness, damping)
# - P_s1, P_s2: interface-state covariance submatrices
# - F_b: coupling force exchanged across interface
```

**Key Insight**: Deterministic messages recover point estimates but yield miscalibrated posteriors; probabilistic messages restore calibration by propagating uncertainty through interface laws.

### 3. Message Passing Architecture

**Jacobi Schedule**:
- Each subsystem updates independently at each time step
- Exchanges posterior means AND covariances of interface variables
- Reconstructs coupling force with propagated uncertainty
- No global augmented state or system-wide covariance matrix

**Computational Scaling**:
- Centralized UKF: $O(n^3)$ where $n$ = total system size
- PCI: $O(N \cdot S_{max})$ where $N$ = subsystems, $S_{max}$ = max subsystem size
- Empirical scaling: approximately linear for infrastructure networks (9-300 buses)

### 4. Hierarchical Composition

**Multi-Level Graph Embedding**:
- Subsystem graphs can embed within larger system graph nodes
- Same Jacobi message-passing operates at all levels
- Intra-subsystem and inter-subsystem interfaces handled uniformly
- Cross-scale uncertainty propagation preserved

**Example Architecture**:
```
Level 1: Power grid network (generator buses as subsystems)
  └── Level 2: Each generator = turbine system (5 subsystems)
       ├── Hydraulic NARX surrogate
       ├── PID governor (deterministic)
       ├── EKF rotational dynamics
       ├── Kalman filter generator vibration
       └── UKF runner dynamics
```

## Implementation Steps

### Step 1: System Decomposition

1. Identify subsystem boundaries based on:
   - Physical interfaces (forces, flows, currents)
   - Computational boundaries (bounded state dimension)
   - Observational boundaries (sparse sensing locations)

2. Partition strategy:
   - Generator-seeded partitioning (for power grids)
   - Admittance-weighted greedy expansion
   - Max subsystem size constraint: $S_{max} \approx 5-15$ buses

### Step 2: Local Model Specification

For each subsystem $i$:
```python
class SubsystemModel:
    def __init__(self, physics_type):
        self.model_type = physics_type  # 'mechanistic', 'data-driven', 'hybrid'
        self.estimator_class = select_estimator(physics_type, data_availability)
        self.interface_vars = identify_interface_variables()
        
    def local_update(self, measurements, interface_messages):
        # 1. Predict using local model
        # 2. Incorporate interface messages as inputs
        # 3. Update posterior with local measurements
        # 4. Extract interface posterior (mean + covariance)
        return posterior_states, posterior_params, interface_posterior
```

### Step 3: Interface Law Specification

**Known Physics** (analytical interface law):
```python
# Linear spring-damper interface
def interface_force(s1_state, s2_state):
    # Relative displacement and velocity
    delta_x = s1_state.x_interface - s2_state.x_interface
    delta_v = s1_state.v_interface - s2_state.v_interface
    
    # Coupling force
    F_b = k * delta_x + c * delta_v
    return F_b

def interface_uncertainty(P_s1, P_s2, k, c):
    a = [k, c]  # Interface coefficients
    var_F = a^T @ (P_s1 + P_s2) @ a
    return var_F
```

**Incomplete Physics** (learned interface):
```python
# SINDy-based interface identification
def learn_interface(interface_data):
    library = ['linear', 'cubic', 'dissipative']
    sparse_model = SINDy(interface_data, library)
    dominant_coeffs = sparse_model.active_coefficients()
    # Returns: k_hat, c_hat, higher_order_corrections
    return interface_model
```

### Step 4: Message Passing Loop

```python
def probabilistic_compositional_inference(system_graph, measurements):
    # Initialize subsystem posteriors
    for subsystem in system_graph.nodes:
        subsystem.initialize_prior()
    
    # Jacobi iteration over time
    for t in time_steps:
        # Phase 1: Predict step
        for subsystem in system_graph.nodes:
            subsystem.predict()
        
        # Phase 2: Interface message exchange
        messages = {}
        for edge in system_graph.edges:
            sender = edge.source
            receiver = edge.target
            
            # Extract interface posterior from sender
            interface_mean = sender.interface_state_mean()
            interface_cov = sender.interface_state_covariance()
            
            # Apply interface law
            coupling_effect = edge.interface_law(interface_mean)
            coupling_uncertainty = propagate_uncertainty(interface_cov, edge.coefficients)
            
            messages[receiver] = {
                'mean': coupling_effect,
                'variance': coupling_uncertainty
            }
        
        # Phase 3: Update step
        for subsystem in system_graph.nodes:
            incoming_messages = messages[subsystem]
            subsystem.update(
                local_measurements[t],
                interface_input=incoming_messages['mean'],
                interface_noise_var=incoming_messages['variance']
            )
    
    return all_posteriors
```

### Step 5: Uncertainty Calibration Verification

```python
def check_calibration(posteriors, ground_truth):
    # Empirical coverage vs nominal credible level
    nominal_levels = [0.68, 0.95, 0.99]
    empirical_coverage = compute_coverage(posteriors, ground_truth, nominal_levels)
    
    # Well-calibrated: empirical ≈ nominal
    # Undercovered: empirical < nominal (deterministic messages)
    # Overconservative: empirical > nominal
    
    return calibration_metrics
```

## Validation Results

### Case Study 1: 4-DOF Mass-Spring-Damper Chain

**Setup**:
- Two subsystems connected by spring-damper interface
- Sparse boundary sensing (only boundary acceleration)
- Unknown parameter: $k_4$ stiffness

**Results** (three matched estimators):
| Metric | Centralized UKF | Deterministic Jacobi | Probabilistic Jacobi |
|--------|-----------------|---------------------|---------------------|
| State RMSE | 4.07e-5 | 2.02e-4 | 1.05e-4 |
| Parameter NRMSE | 2.47e-2 | 4.16e-3 | 4.65e-3 |
| 95% Coverage | 1.00 | 0.83 ⚠️ | 1.00 ✓ |
| 68% Coverage | 1.00 | 0.66 ⚠️ | 1.00 ✓ |
| Pred. NLL | -4.29e1 | 4.98e3 ⚠️ | -5.25e1 ✓ |

**Learned Interface**:
- SINDy recovery: $\hat{k} = 5.61 \times 10^4$ N/m (12.2% error), $\hat{c} = 3.31 \times 10^2$ Ns/m (10.3% error)
- Preserves calibration: 95% coverage = 1.00 ✓

### Case Study 2: IEEE Power Grid Benchmarks (9-300 buses)

**Partitioning**:
- Generator buses seed subsystems
- Greedy expansion up to $S_{max}=5$ buses
- Local UKF on 15-dimensional augmented state

**Results**:
- State/parameter accuracy matches centralized UKF across all sizes
- Runtime: centralized $O(n^3)$ vs distributed $O(N \cdot S_{max})$
- Parallel projection: sequential cost ÷ subsystem count

### Case Study 3: Multi-Physics Turbine + Grid

**Hierarchical Composition**:
- 5-subsystem turbine: hydraulic (NARX), governor (PID), rotation (EKF), vibration (KF), runner (UKF)
- Embedded in IEEE 9-bus network (replacing generator buses)
- Cross-scale disturbance propagation: load step → grid torque → turbine speed

**Results**:
- Embedded vs standalone trajectory RMSE: $1.02 \times 10^{-3}$
- Seal stiffness posterior indistinguishable ✓
- Calibrated uncertainty survives hierarchical embedding ✓

## Advantages vs Existing Methods

| Approach | Heterogeneity | Sparse Sensing | Distributed Uncertainty | Scalability | Inverse Inference |
|----------|---------------|----------------|------------------------|-------------|-------------------|
| Monolithic DA | ❌ | ✓ | ❌ (global) | ❌ $O(n^3)$ | ✓ |
| Co-simulation | ✓ | ❌ | ❌ | ✓ | ❌ forward only |
| Factor graphs | ❌ homogeneous | ✓ | ✓ | ✓ | ❌ fixed interactions |
| Graph NNs | ✓ | ✓ | ❌ | ✓ | ❌ no posteriors |
| **PCI** | ✓ | ✓ | ✓ | ✓ $O(N \cdot S_{max})$ | ✓ |

## Applications

### Digital Twins for Infrastructure

- Power grid state estimation + parameter identification
- Water distribution networks (flow + pressure inference)
- Transportation systems (traffic + control)
- Industrial process plants (multi-physics coupling)

### Key Benefits

1. **Real-time operation**: Linear scaling enables infrastructure-scale inference
2. **Heterogeneity**: Different physics domains coexist (hydraulic, electrical, mechanical)
3. **Calibration**: Uncertainty-aware predictions for risk assessment
4. **Modularity**: Plug-and-play subsystem models (mechanistic → learned → hybrid)
5. **Hierarchical**: Multi-scale systems compose without posterior collapse

## When to Use

Use probabilistic compositional inference when:

- **Coupled systems** with physically meaningful interfaces (forces, flows, currents)
- **Sparse sensing** leaving most states unobserved
- **Distributed uncertainty** across subsystem boundaries
- **Heterogeneous components** (different physics, model classes, fidelities)
- **Infrastructure scale** (hundreds to thousands of components)
- **Inverse problems** (state estimation, parameter identification, coupling inference)
- **Digital twin requirements** (uncertainty-aware, real-time, modular)

**Avoid when**:
- Single homogeneous system (use centralized methods)
- Dense sensing (global state observable)
- Forward simulation only (use co-simulation)
- No uncertainty requirement (use deterministic methods)

## Technical Pitfalls

1. **Interface Covariance Neglect**: Deterministic messages lose calibration
   - **Fix**: Always propagate variance through interface laws
   
2. **Cross-Covariance Assumption**: Jacobi assumes independent subsystem interface states
   - **Fix**: Accept approximation or use more sophisticated schedule
   
3. **Interface Law Completeness**: Unknown physics requires learned laws
   - **Fix**: SINDy, neural networks, or hybrid identification
   
4. **Partitioning Strategy**: Too large subsystems lose scalability
   - **Fix**: Bound $S_{max}$, use physics-guided partitioning
   
5. **Hierarchical Collapse**: Embedding can degrade local posteriors
   - **Fix**: Verify calibration at each level, use probabilistic messages

## References

- Ghorbani & Hackl (2026) - "Subsystem Structure as an Inferential Resource for Coupled Engineered Systems" arXiv:2605.27544
- Kapteyn et al. (2021) - "Probabilistic digital twins"
- Willcox (2021) - "Imperative for predictive digital twins"
- Brunton et al. (2016) - SINDy for sparse dynamics identification
- Julier & Uhlmann (2004) - Unscented Kalman Filter

## Further Reading

- `equation-free-digital-twins` - Koopman-based digital twin framework
- `distributed-control-prototyping-framework` - Multi-robot co-design
- `digital-twin-multi-agent-consensus` - Consensus control for digital twins
- `model-based-systems-engineering` - MBSE methodology