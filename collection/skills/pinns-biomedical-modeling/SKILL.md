---
name: pinns-biomedical-modeling
description: Physics-informed Neural Networks (PINNs) for biomedical modeling and simulation. Use when working on physics-guided neural network approaches for hemodynamics, cardiovascular modeling, blood flow prediction, or inverse medical physics problems. Combines physical principles with neural networks for personalized medical predictions with minimal data requirements.
---

# PINNs for Biomedical Modeling

Physics-informed Neural Networks (PINNs) integrate physical laws (PDEs, conservation laws) directly into neural network training, enabling accurate predictions from sparse clinical data.

## Key Concepts

**Physics-Informed Loss Function:**
```
Loss = Data Loss + Physics Loss + Boundary Loss
```

- **Data Loss**: Matches neural network predictions to sparse observations
- **Physics Loss**: Enforces PDE residuals at collocation points
- **Boundary Loss**: Enforces boundary conditions

## Application Domains

### Hemodynamics
- Blood flow velocity and pressure prediction
- Arterial tree modeling (1-D, 3-D)
- Cardiac output estimation from cuff pressure
- Central systolic blood pressure (cSBP) prediction

### Cardiovascular
- Patient-specific arterial parameter estimation
- Terminal resistance (R_T) and compliance (C_T) tuning
- Virtual patient cohort generation
- Hemodynamic surrogate modeling

### General Medical Physics
- Inverse problem solving from minimal measurements
- Personalized medicine with sparse data
- Real-time prediction for wearable devices

## Workflow

### Step 1: Define Physical Model
1. Identify governing PDEs (e.g., Navier-Stokes for blood flow)
2. Define domain geometry (arterial network structure)
3. Specify boundary conditions (pressure, velocity profiles)

### Step 2: Configure Neural Network
1. Choose architecture (MLP with physics residuals)
2. Set collocation points for physics enforcement
3. Define trainable physics parameters (R_T, C_T)

### Step 3: Train with Minimal Data
1. Use sparse clinical measurements (e.g., cuff pressure only)
2. Train in 4000+ iterations (10x faster than traditional methods)
3. Learn physics parameters simultaneously

### Step 4: Validate
1. Compare with numerical solvers (1-D arterial model)
2. Clinical dataset validation (CO, cSBP correlation)
3. Target r > 0.85 for correlation metrics

## Key Advantages

- **Data Efficiency**: Works with minimal noninvasive measurements
- **Speed**: 10x faster than traditional iterative inverse methods
- **Personalization**: Learns patient-specific parameters
- **Physical Consistency**: Enforces biological constraints

## Reference Papers

- "Fast and Accurate Inverse Blood Flow Modeling from Minimal Cuff-Pressure Data via PINNs" (arXiv:2604.03221)
- "Real-Time Surrogate Modeling for Personalized Blood Flow Prediction" (arXiv:2604.03197)

## Tools Used

- Python: DeepXDE, PyTorch, TensorFlow
- exec: Run PINN training scripts
- write: Save model parameters and predictions

## Usage Examples

### Example 1: Blood Flow Prediction
```
User: "Estimate cardiac output from cuff pressure measurements"

Agent:
1. Load 1-D arterial tree model
2. Configure PINN with Navier-Stokes residuals
3. Train on cuff pressure data (5-10 min)
4. Predict CO and cSBP with correlation validation
```

### Example 2: Virtual Patient Cohort
```
User: "Generate synthetic hemodynamic dataset"

Agent:
1. Create parametric patient distribution (Asklepios correlations)
2. Use PINN surrogate for rapid screening
3. Reject non-physiological parameter combinations
4. Generate valid synthetic cohort
```

## Best Practices

1. **Start Simple**: Single artery before full arterial tree
2. **Validate Physics**: Compare with numerical solver first
3. **Parameter Bounds**: Enforce physiological ranges
4. **Convergence Check**: Monitor physics residual reduction

## Related Skills

- `neural-dynamics`: General neural dynamics analysis
- `hemodynamics`: Blood flow simulation
- `medical-ml`: Machine learning for medical applications