---
name: buildyn-thermal-dynamics-control
description: "Excitation-driven data generation framework for building thermal dynamics modeling and control. BuilDyn enables customizable excitation strategies for control-oriented data generation, supports sampling from representative building distributions, and provides Python interface for ML pipelines. Use when: (1) training data-driven building models, (2) ensuring sufficient state-space exploration, (3) preparing training data for building control applications, (4) generating excited vs stationary operation datasets, (5) developing building-specific foundation models."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29849"
  published: "2026-05-28"
  authors: "Felix Koch, Thomas Krug, Fabian Raisch, Benjamin Schäfer, Benjamin Tischler"
  tags: [building-thermal, excitation-driven, control-oriented, machine-learning, BuilDyn, foundation-models, systems-control]
---

# BuilDyn: Excitation-Driven Data Generation for Building Thermal Dynamics

Framework for generating control-oriented training data through systematic excitation of building thermal systems.

## Problem Context

**Challenge**: Existing building datasets and simulations reflect stationary operation under fixed control policies, leading to:
- Limited exploration of control-driven state space
- Poor generalization to unseen operating conditions
- Reduced robustness in downstream ML tasks (fault detection, energy-efficient control)

**Solution**: BuilDyn enables **excitation-driven data generation** to ensure sufficient state-space coverage.

## Core Concepts

### 1. Excitation Strategies

**Goal**: Explore control-driven system state space systematically.

**Types of excitation:**

- **Random excitation**: Stochastic control inputs
- **Periodic excitation**: Sinusoidal or square-wave signals
- **Step excitation**: Sudden control changes
- **Optimized excitation**: Design signals to maximize information gain

**Key parameters:**
- Excitation amplitude (Δu)
- Excitation frequency (f)
- Excitation duration (T)
- Coverage metrics (state-space volume)

### 2. Building Sampling

BuilDyn supports sampling from representative building distributions:

```python
# Sample buildings from distribution
building_params = {
    'thermal_mass': sample_thermal_mass(),
    'window_area': sample_window_area(),
    'insulation': sample_insulation(),
    'occupancy_patterns': sample_occupancy(),
    'climate_zone': sample_climate()
}
```

This enables:
- Training on diverse building characteristics
- Transfer learning across building types
- Foundation model development

### 3. Python Interface

Integration into ML pipelines:

```python
from buildyn import BuilDynGenerator

# Initialize generator
generator = BuilDynGenerator(
    building_distribution='representative_buildings.json',
    excitation_strategy='optimized',
    duration_hours=168
)

# Generate excited dataset
dataset = generator.generate(
    n_buildings=100,
    n_scenarios_per_building=10
)

# Export for ML training
dataset.save('excited_building_data.h5')
```

## Implementation Workflow

### Step 1: Define Excitation Strategy

```python
excitation_config = {
    'type': 'optimized',  # 'random', 'periodic', 'step', 'optimized'
    'control_variables': ['heating_power', 'cooling_power', 'ventilation_rate'],
    'amplitude_range': [0.0, 1.0],  # Normalized control range
    'duration': 168,  # Hours (1 week)
    'sampling_rate': 3600  # Seconds (1 hour intervals)
}
```

### Step 2: Sample Building Parameters

```python
building_distribution = {
    'thermal_mass': {
        'distribution': 'uniform',
        'range': [1e6, 5e7]  # J/K
    },
    'window_area_fraction': {
        'distribution': 'normal',
        'mean': 0.15,
        'std': 0.05
    },
    'insulation_R': {
        'distribution': 'lognormal',
        'mean': 2.5,  # m²·K/W
        'std': 0.5
    }
}
```

### Step 3: Generate Training Data

```python
# Generate excited data
excited_data = generator.generate_excited(
    n_samples=10000,
    excitation_config=excitation_config,
    building_distribution=building_distribution
)

# Generate baseline (non-excited) data for comparison
baseline_data = generator.generate_stationary(
    n_samples=10000,
    control_policy='fixed_setpoint',
    building_distribution=building_distribution
)
```

### Step 4: Train ML Models

```python
# Compare performance
model_excited = train_model(excited_data)
model_baseline = train_model(baseline_data)

# Evaluate on unseen operating conditions
test_scenarios = generate_challenging_scenarios()
performance_excited = evaluate(model_excited, test_scenarios)
performance_baseline = evaluate(model_baseline, test_scenarios)

# Expected: excited model > baseline model on unseen conditions
```

## Key Advantages

1. **State-space coverage**: Systematic exploration of control inputs
2. **Robustness**: Better generalization to unseen operating conditions
3. **Diversity**: Sampling from representative building distributions
4. **Integration**: Python interface for easy ML pipeline integration
5. **Foundation models**: Enables building-specific foundation model development

## Excitation Design Principles

### Maximizing Information Gain

Excitation signals should:
- Cover wide range of control inputs (heating, cooling, ventilation)
- Explore different thermal dynamics regimes
- Avoid redundant trajectories
- Maximize Fisher information or mutual information

### Coverage Metrics

Quantify state-space coverage:

```python
def compute_coverage(dataset):
    state_vectors = dataset['states']  # [temperature, humidity, CO2, etc.]
    
    # Volume coverage
    volume = convex_hull_volume(state_vectors)
    
    # Density coverage
    entropy = state_entropy(state_vectors)
    
    return {'volume': volume, 'entropy': entropy}
```

## Use Cases

- **Fault detection & diagnosis**: Training robust FDD models
- **Energy-efficient control**: Model predictive control (MPC) training data
- **Building energy simulation**: Validating simulation models
- **Transfer learning**: Pre-training foundation models for specific buildings
- **Climate adaptation**: Training models for diverse weather conditions

## Comparison: Excited vs Stationary Data

| Criterion | Stationary Operation | Excited Operation |
|-----------|---------------------|-------------------|
| State-space coverage | Limited (fixed setpoints) | Broad (variable inputs) |
| Generalization | Poor (unseen conditions) | Strong (diverse scenarios) |
| Robustness | Low (fragile to changes) | High (handles variations) |
| Information density | Sparse | Dense |
| Model performance | Suboptimal | Optimal |

## Practical Considerations

- **Excitation duration**: Balance exploration vs stability (1-2 weeks typical)
- **Sampling rate**: Match downstream model requirements (hourly for thermal dynamics)
- **Building diversity**: Sample from realistic distributions
- **Climate variation**: Include diverse weather scenarios
- **Occupancy patterns**: Account for usage variability

## Integration with Building Simulation

BuilDyn builds on **BuilDa** (Building Data simulator):

```python
# BuilDyn extends BuilDa
from builda import BuildingSimulator
from buildyn import ExcitationModule

simulator = BuildingSimulator(building_config)
exciter = ExcitationModule(strategy='optimized')

# Excited simulation
control_sequence = exciter.generate_controls(duration=168)
simulation_results = simulator.run(control_sequence)
```

## Research Directions

1. **Foundation models**: Building-specific foundation models via large-scale excited data
2. **Transfer learning**: Cross-building knowledge transfer
3. **Adaptive excitation**: Online excitation based on model uncertainty
4. **Multi-objective excitation**: Balance energy cost vs information gain

## Activation Keywords

- building thermal dynamics
- excitation-driven data
- control-oriented modeling
- building ML training data
- BuilDyn framework
- building foundation models
- thermal system excitation