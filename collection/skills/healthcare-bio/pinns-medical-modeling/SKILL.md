---
name: pinns-medical-modeling
description: "Physics-Informed Neural Networks (PINNs) for medical modeling and biomedical simulation. Solve differential equations governing physiological processes (cardiovascular, neural, pharmacokinetic) using neural networks that embed physical laws as constraints. Use when: (1) Modeling patient-specific physiology, (2) Solving inverse problems in biomechanics, (3) Drug pharmacokinetic modeling, (4) Cardiac or neural dynamics simulation with limited data."
---

# PINNs Medical Modeling

Physics-Informed Neural Networks for medical and biomedical simulation.

## Activation Keywords

- PINNs medical
- physics-informed neural network medical
- biomedical simulation
- physiological modeling neural network
- medical differential equations
- 物理信息神经网络医学
- 生物医学仿真
- cardiac PINNs
- pharmacokinetic neural network

## Tools Used

- `exec`: Run Python PINNs training scripts (PyTorch/JAX)
- `read`: Load physiological data, ODE/PDE specifications
- `write`: Generate PINNs model code and simulation results

## Core Workflow

### Step 1: Define Physical Laws
Specify the governing equations (ODEs/PDEs) for the physiological system:

```python
# Example: Hodgkin-Huxley neuron model
def physics_residual(t, V, m, h, n, params):
    """PDE residual for Hodgkin-Huxley equations."""
    C_m, g_Na, g_K, g_L = params
    dV_dt = (1/C_m) * (I_ext - g_Na*m**3*h*(V-E_Na) 
                        - g_K*n**4*(V-E_K) - g_L*(V-E_L))
    return dV_dt
```

### Step 2: Design Neural Network
Create network to approximate solution, with physics loss added to data loss:

```python
class PINNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 64), nn.Tanh(),
            nn.Linear(64, 64), nn.Tanh(),
            nn.Linear(64, 1)
        )

    def forward(self, t):
        return self.net(t)
```

### Step 3: Define Combined Loss
```python
loss = data_loss + lambda_physics * physics_loss + lambda_bc * boundary_loss
```

### Step 4: Train with Adaptive Sampling
Use collocation points in domain; add extra points near boundaries and discontinuities.

## Instructions for Agents

### Step 1: Identify Medical System
Determine physiological system: cardiovascular, neural, pharmacokinetic, or biomechanical.

### Step 2: Extract Governing Equations
From the medical/physics paper, extract ODEs/PDEs that govern the system.

### Step 3: Formulate PINN
Design neural network architecture; define physics residual loss; set boundary/initial conditions.

### Step 4: Train and Validate
Train with combined data + physics loss; validate against clinical measurements or analytical solutions.

### Step 5: Report
Report model accuracy, physics constraint satisfaction, and clinical relevance.

## Examples

### Example 1: Cardiac Electrophysiology Simulation

```
User: "Simulate cardiac action potential using PINNs"

Agent:
1. Extract governing equations: Hodgkin-Huxley or monodomain model
2. Design PINNs: input=time, output=membrane voltage
3. Define physics loss from action potential ODE
4. Train on sparse electrode measurements
5. Report simulated action potential vs clinical data
```

### Example 2: Pharmacokinetic Modeling

```
User: "Model drug concentration over time with limited patient data"

Agent:
1. Extract PK model: two-compartment ODE system
2. Design PINNs to approximate concentration curves
3. Embed ODE constraints as physics loss
4. Train on available blood samples
5. Predict drug concentration with uncertainty estimates
```

## Resources

- `references/`: PINNs implementation guides and medical domain references
- Related: `neural-dynamics-decision-making`, `jedi-neural-dynamics-inference`
