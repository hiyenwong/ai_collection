---
name: cold-atom-reservoir-computing
description: >
  Cold-atom (neutral-atom) reservoir computing methodology for efficient machine learning tasks.
  Uses Rydberg atom arrays as physical reservoirs, encoding input data into Hamiltonian parameters
  and reading out via quantum measurements. Use when implementing reservoir computing on quantum
  hardware, exploring neutral-atom ML platforms, or building energy-efficient quantum-inspired
  classifiers. Triggers: cold atom reservoir, neutral atom computing, Rydberg reservoir,
  quantum reservoir machine, atom array ML, physical reservoir computing quantum.
---

# Cold-Atom Reservoir Computing

## Core Methodology

Neutral-atom reservoir computing for efficient ML:

1. **Input encoding**: Map data to Rydberg Hamiltonian parameters (detuning, Rabi frequency)
2. **Reservoir evolution**: Let atom array evolve under Hamiltonian dynamics
3. **Measurement readout**: Extract expectation values as high-dimensional features
4. **Linear readout**: Train simple linear classifier on reservoir states

## Rydberg Hamiltonian

```
H(t) = sum_i [Omega(t)/2 * sigma_x_i - Delta_i(t) * n_i] + sum_{i<j} V_{ij} * n_i * n_j
```

- Input data encoded in Delta_i (detuning) and Omega (Rabi frequency)
- V_{ij} = C_6 / |r_i - r_j|^6 (van der Waals interaction)
- Natural nonlinear dynamics from Rydberg blockade

## Advantages Over Classical Reservoir Computing

- **High dimensionality**: N atoms provide 2^N dimensional Hilbert space
- **Natural nonlinearity**: Rydberg blockade creates intrinsic nonlinear response
- **Energy efficiency**: Physical computation without digital simulation overhead
- **Parallelism**: All atoms evolve simultaneously

## Implementation Pattern (PennyLane)

```python
import pennylane as qml

def rydberg_reservoir(n_atoms, input_data):
    dev = qml.device('default.qubit', wires=n_atoms)
    
    @qml.qnode(dev)
    def circuit(inputs):
        # Encode inputs into Hamiltonian
        for i in range(n_atoms):
            qml.RY(inputs[i], wires=i)
        
        # Rydberg interaction (entangling layer)
        for i in range(n_atoms - 1):
            qml.CNOT(wires=[i, i + 1])
        
        # Readout
        return [qml.expval(qml.PauliZ(i)) for i in range(n_atoms)]
    
    return circuit(input_data)

# Linear readout training
from sklearn.linear_model import Ridge
reservoir_states = [rydberg_reservoir(4, x) for x in X_train]
clf = Ridge(alpha=1.0)
clf.fit(reservoir_states, y_train)
```

## Hardware Platforms

- Neutral-atom arrays (QuEra, Pasqal)
- Rydberg atom platforms with programmable geometry
- Scalable to 100+ qubits with current technology

## Activation Keywords
- cold atom reservoir computing
- neutral atom machine learning
- Rydberg reservoir
- quantum reservoir computing
- atom array ML
- physical reservoir quantum
- Rydberg blockade computing
- neutral-atom classification
