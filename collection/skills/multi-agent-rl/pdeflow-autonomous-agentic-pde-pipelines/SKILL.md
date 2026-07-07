---
name: pdeflow-autonomous-agentic-pde-pipelines
description: "PDEFlow: an autonomous agentic framework that turns user-level ODE/PDE descriptions into solver-backed neural-operator pipelines. Links problem specification, data generation, operator training, and checkpoint-based inference via a stateful input graph and registry-based interface. Instantiated with multi-branch Bayesian DeepONet. Activation: PDEFlow, autonomous PDE solver, neural operator, agentic pipeline, DeepONet, FEniCSx, ODE PDE automation, scientific workflow, Bayesian DeepONet, operator learning."
version: 1.0.0
metadata:
  hermes:
    tags: [multi-agent-rl, physics-math, agentic, neural-operator, pde, ode, scientific-computing, deep-operator-network, bayesian]
    source_paper: "PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solving (arXiv:2607.05134)"
    published: "2026-07-06"
    authors: "Akshat Jani, Prathamesh Gadekar, Sakhinana Sagar Srinivas, Venkataramana Runkana"
    arxiv_id: "2607.05134"
    utility: 0.85
---

# PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning

## Overview

PDEFlow is an autonomous agentic framework that converts user-level natural-language descriptions of ODEs and PDEs into complete solver-backed neural-operator pipelines. The workflow spans problem specification → data generation → operator training → checkpoint-based inference, minimizing manual intervention for repeatable scientific and engineering workflows.

## Architecture

### Four-Stage Agentic Pipeline

```
User NL Input → [Stateful Input Graph] → [Data Generation] → [Operator Training] → [Inference]
                      ↑                           ↑                  ↑                ↑
               Multi-turn edits           FEniCSx solver      Registry-based     Checkpoint
               + validation               + param sampling    operator interface  loading
```

### 1. Stateful Input Graph

Converts multi-turn natural-language input and user edits into validated problem specifications.

```python
class StatefulInputGraph:
    """Maintains state across multi-turn PDE specification conversations."""
    def __init__(self):
        self.state = {
            "equation": None,      # e.g., "u_t = D * u_xx"
            "domain": None,        # e.g., {"x": [0, 1], "t": [0, 10]}
            "bc": None,            # boundary conditions
            "ic": None,            # initial conditions
            "params": None,        # physical parameters (e.g., D=0.01)
            "validated": False
        }
        self.edit_history = []

    def update_from_nl(self, user_input):
        """Parse natural language and update graph state."""
        parsed = self.parse_pde_description(user_input)
        for key, value in parsed.items():
            if value is not None:
                self.state[key] = value
                self.edit_history.append((key, value, user_input))

    def validate(self):
        """Validate that the specification is complete and consistent."""
        required = ["equation", "domain", "bc", "ic", "params"]
        self.state["validated"] = all(self.state[k] is not None for k in required)
        return self.state["validated"]
```

### 2. Data Generation Module

Samples parameters, solves the configured governing equation with FEniCSx finite-element backend, and stores solutions as operator-ready tensors.

```python
import fenicsx  # FEniCSx backend

class DataGenerator:
    """Generate solver-backed training data for neural operators."""
    def __init__(self, spec, n_samples=1000):
        self.spec = spec
        self.n_samples = n_samples

    def generate(self):
        """Sample parameters, solve PDE, store as tensors."""
        dataset = []
        for _ in range(self.n_samples):
            params = self.sample_parameters()
            solution = self.solve_with_fenicsx(params)
            dataset.append({
                "params": params,
                "solution": solution.tensor(),
                "grid": solution.mesh()
            })
        return dataset

    def solve_with_fenicsx(self, params):
        """Solve PDE using FEniCSx finite element method."""
        mesh = self.create_mesh(self.spec["domain"])
        V = fenicsx.FunctionSpace(mesh, "P", 1)
        u = fenicsx.TrialFunction(V)
        v = fenicsx.TestFunction(V)
        # Set up variational problem from spec
        a, L = self.build_variational_form(u, v, params)
        # Apply BCs
        bcs = self.apply_boundary_conditions(V, self.spec["bc"])
        # Solve
        solution = fenicsx.Function(V)
        fenicsx.solve(a == L, solution, bcs)
        return solution
```

### 3. Training Stage — Registry-Based Operator Interface

A registry-based interface allows different neural operators to be trained and deployed without changing the surrounding pipeline.

```python
class OperatorRegistry:
    """Registry for pluggable neural operators."""
    _operators = {}

    @classmethod
    def register(cls, name):
        def decorator(op_class):
            cls._operators[name] = op_class
            return op_class
        return decorator

    @classmethod
    def get(cls, name):
        return cls._operators.get(name)

@OperatorRegistry.register("bayesian-deeponet")
class BayesianDeepONet:
    """Multi-branch Bayesian DeepONet with uncertainty quantification."""
    def __init__(self, branch_input_dim, trunk_input_dim, hidden_dim=128):
        self.branch = BayesianMLP(branch_input_dim, hidden_dim)
        self.trunk = BayesianMLP(trunk_input_dim, hidden_dim)

    def forward(self, branch_input, trunk_input):
        b = self.branch(branch_input)  # (batch, hidden)
        t = self.trunk(trunk_input)    # (batch, hidden)
        return torch.einsum("bi,bi->b", b, t)  # dot product

    def predict_with_uncertainty(self, branch_input, trunk_input, n_samples=10):
        """Bayesian inference with epistemic uncertainty."""
        preds = [self.forward(branch_input, trunk_input) for _ in range(n_samples)]
        mean = torch.stack(preds).mean(dim=0)
        std = torch.stack(preds).std(dim=0)
        return mean, std
```

### 4. Inference Stage — Checkpoint-Based

Loads saved checkpoints for solver-free predictions from new inputs.

```python
class InferenceEngine:
    """Solver-free prediction from trained neural operator checkpoints."""
    def __init__(self, checkpoint_path, operator_name="bayesian-deeponet"):
        self.operator = OperatorRegistry.get(operator_name)
        self.operator.load_state_dict(torch.load(checkpoint_path))

    def predict(self, input_params, query_points):
        """Predict solution at query points without running solver."""
        with torch.no_grad():
            branch_input = self.encode_params(input_params)
            trunk_input = self.encode_points(query_points)
            prediction, uncertainty = self.operator.predict_with_uncertainty(
                branch_input, trunk_input
            )
        return prediction, uncertainty
```

## Key Features

- **Multi-turn specification**: Stateful input graph handles iterative PDE description refinement
- **Solver-backed data**: FEniCSx finite-element solver generates ground-truth solutions
- **Pluggable operators**: Registry pattern allows swapping neural operators (DeepONet, FNO, etc.) without pipeline changes
- **Bayesian uncertainty**: Multi-branch Bayesian DeepONet provides epistemic uncertainty on predictions
- **Checkpoint persistence**: Trained operators saved/loaded for repeatable inference

## Experimental Validation

- Benchmark ODE and PDE tasks (steady-state and transient)
- PDEFlow successfully: constructs valid specifications → generates solver-backed datasets → trains neural operators → provides solver-free predictions from checkpoints
- Designed for repeatable scientific/engineering workflows where many related physics configurations must be specified, simulated, learned, and queried

## Use Cases

- **Scientific computing automation** — automate the PDE solve-train-deploy loop
- **Engineering design exploration** — rapidly test variations of a PDE configuration
- **Neural operator research** — benchmark different operators within a unified pipeline
- **Physics-informed ML pipelines** — as a reference architecture for agentic scientific workflows
- **Digital twin construction** — learn surrogate models from solver data with uncertainty

## Activation Keywords

PDEFlow, autonomous PDE pipeline, agentic scientific workflow, neural operator, DeepONet, Bayesian DeepONet, FEniCSx, PDE automation, ODE solving, operator learning, stateful input graph, registry-based operator, solver-free prediction, checkpoint inference, scientific computing agentic
