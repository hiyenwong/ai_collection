---
name: quantum-opinion-dynamics-networks
description: Quantum model of opinion dynamics on networks — represents agent cognitive states as density matrices encoding both expressed opinions and cognitive ambivalence, with survey questions as non-commuting self-adjoint operators explaining order effects.
trigger_words: quantum opinion dynamics, cognitive ambivalence, order effects, density matrix opinion, network opinion model, quantum cognition
---

# Quantum Opinion Dynamics on Networks

## Description

Models opinion dynamics on networks using quantum probability theory where each agent's cognitive state is represented by a density matrix encoding both expressed opinion and cognitive ambivalence. Survey questions become non-commuting self-adjoint operators, providing principled explanation for order effects. Based on arXiv:2607.01452 (Weiqi Chu, 2026).

## Activation Keywords

- quantum opinion dynamics
- cognitive ambivalence modeling
- quantum probability cognition
- order effects survey
- density matrix social dynamics
- quantum network model
- quantum cognition model

## Core Methodology

### 1. Density Matrix Cognitive State

Each agent's cognitive state is represented as:

```python
import numpy as np
from scipy.linalg import expm

class QuantumOpinionAgent:
    """Agent with quantum cognitive state."""
    
    def __init__(self, dim=2):
        """Initialize with maximally mixed state (no opinion)."""
        self.dim = dim
        # Density matrix: positive semi-definite, trace=1
        self.rho = np.eye(dim) / dim
        # Coherence: off-diagonal elements represent ambivalence
        self.coherence = np.zeros((dim, dim), dtype=complex)
    
    def set_opinion(self, eigenvalues):
        """Set diagonal elements (expressed opinion probabilities)."""
        self.rho = np.diag(eigenvalues)
        assert abs(np.trace(self.rho) - 1.0) < 1e-10, "Trace must equal 1"
    
    def add_coherence(self, off_diag):
        """Add quantum coherence (cognitive ambivalence)."""
        self.rho += off_diag
        self.rho = (self.rho + self.rho.conj().T) / 2  # Hermitian
        # Ensure positive semi-definite
        eigvals = np.linalg.eigvalsh(self.rho)
        if np.min(eigvals) < 0:
            self.rho -= np.min(eigvals) * np.eye(self.dim)
            self.rho /= np.trace(self.rho)
    
    def measure_opinion(self, observable):
        """Measure opinion along observable (survey question)."""
        # Observable must be Hermitian
        assert np.allclose(observable, observable.conj().T)
        eigvals, eigvecs = np.linalg.eigh(observable)
        # Born rule: p(i) = <v_i|rho|v_i>
        probs = np.array([
            np.real(np.vdot(v, self.rho @ v)) for v in eigvecs.T
        ])
        return eigvals, np.maximum(probs, 0)  # Ensure non-negative
    
    def update_from_neighbor(self, other_rho, coupling=0.1):
        """Friedkin-Johnsen quantum update."""
        self.rho = (1 - coupling) * self.rho + coupling * other_rho
        # Renormalize
        self.rho /= np.trace(self.rho)
```

### 2. Non-Commuting Survey Operators

Survey questions as non-commuting observables explain order effects:

```python
def create_survey_operators(dim=2):
    """Create non-commuting survey question operators."""
    # Question 1: economic policy (Pauli-Z basis)
    Q1 = np.array([[1, 0], [0, -1]], dtype=complex)
    # Question 2: social policy (Pauli-X basis) - does NOT commute with Q1
    Q2 = np.array([[0, 1], [1, 0]], dtype=complex)
    # Verify non-commutation: [Q1, Q2] = Q1@Q2 - Q2@Q1 ≠ 0
    commutator = Q1 @ Q2 - Q2 @ Q1
    assert not np.allclose(commutator, 0), "Operators must not commute"
    return Q1, Q2

def order_effect_demo():
    """Demonstrate order effects from non-commuting operators."""
    Q1, Q2 = create_survey_operators()
    
    # Agent state: slight preference for option 1
    agent_rho = np.array([[0.6, 0.1+0.1j], [0.1-0.1j, 0.4]])
    agent_rho /= np.trace(agent_rho)
    
    # Measure Q1 then Q2
    _, p1_first = measure_sequence(agent_rho, [Q1, Q2])
    # Measure Q2 then Q1
    _, p2_first = measure_sequence(agent_rho, [Q2, Q1])
    
    # Results differ due to non-commutation
    print(f"P(Q1=1 | Q2 measured first): {p2_first[0][0]:.4f}")
    print(f"P(Q1=1 | Q1 measured first): {p1_first[0][0]:.4f}")

def measure_sequence(rho, observables):
    """Sequential quantum measurement with state collapse."""
    results = []
    current_rho = rho.copy()
    for obs in observables:
        eigvals, eigvecs = np.linalg.eigh(obs)
        probs = np.array([np.real(np.vdot(v, current_rho @ v)) for v in eigvecs.T])
        results.append((eigvals, np.maximum(probs, 0)))
        # Collapse: Lüders rule
        # (simplified: update state to eigenstate weighted by probability)
        collapsed = sum(
            p * np.outer(v, v.conj()) for p, v in zip(probs, eigvecs.T)
        )
        current_rho = collapsed / np.trace(collapsed)
    return results, results
```

### 3. Quantum Network Opinion Dynamics

```python
class QuantumOpinionNetwork:
    """Network of quantum opinion agents."""
    
    def __init__(self, n_agents, adjacency_matrix):
        self.n = n_agents
        self.adj = adjacency_matrix
        self.agents = [QuantumOpinionAgent(dim=2) for _ in range(n_agents)]
    
    def step(self, coupling=0.1):
        """One iteration of quantum opinion dynamics."""
        new_states = []
        for i in range(self.n):
            new_rho = self.agents[i].rho.copy()
            for j in range(self.n):
                if self.adj[i, j] > 0:
                    new_rho += coupling * self.adj[i, j] * (
                        self.agents[j].rho - self.agents[i].rho
                    )
            new_rho /= np.trace(new_rho)
            new_states.append(new_rho)
        for i, rho in enumerate(new_states):
            self.agents[i].rho = rho
    
    def coherence_decay(self, rate=0.05):
        """Exponential coherence decay (independent of network)."""
        for agent in self.agents:
            agent.rho *= (1 - rate)
            # Restore diagonal
            diag = np.diag(np.diag(agent.rho))
            agent.rho = diag + (1 - rate) * (agent.rho - diag)
            agent.rho /= np.trace(agent.rho)
    
    def get_network_coherence(self):
        """Average quantum coherence across network."""
        coherences = []
        for agent in self.agents:
            # Coherence = sum of |off-diagonal|^2
            off_diag = agent.rho - np.diag(np.diag(agent.rho))
            coh = np.sum(np.abs(off_diag)**2)
            coherences.append(coh)
        return np.mean(coherences)
```

### 4. Key Properties

**Product State Approximation**: Under weak coupling, the quantum model reduces to classical Friedkin-Johnsen model.

**Quantum Coherence Decay**: Coherence decays exponentially at rate independent of network topology.

**Steady State Convergence**: Pairwise correlations converge to same steady state regardless of network structure.

**Transient Network Dynamics**: Pairwise opinion covariances follow network-dependent transient dynamics.

## Workflow for Agents

### Step 1: Define Cognitive State Space

```python
# Binary opinion: 2D Hilbert space
# Multi-option opinion: higher dimensional
dim = len(opinion_options)
agent = QuantumOpinionAgent(dim=dim)
```

### Step 2: Construct Survey Operators

```python
# Each survey question = Hermitian observable
# Non-commuting questions → order effects
operators = create_survey_operators(dim)
```

### Step 3: Build Network

```python
import networkx as nx
G = nx.erdos_renyi_graph(n=100, p=0.1)
adj = nx.to_numpy_array(G)
network = QuantumOpinionNetwork(n_agents=100, adjacency_matrix=adj)
```

### Step 4: Simulate Dynamics

```python
for t in range(100):
    network.step(coupling=0.1)
    network.coherence_decay(rate=0.05)
    coherence = network.get_network_coherence()
    print(f"t={t}: avg coherence = {coherence:.6f}")
```

### Step 5: Analyze Results

```python
# Check convergence
# Measure opinion distributions
# Compute pairwise covariances
# Verify coherence decay rate independence
```

## Error Handling

### Non-Positive Semi-Definite Density Matrix
```python
# Fix: project onto PSD cone
eigvals, eigvecs = np.linalg.eigh(rho)
eigvals = np.maximum(eigvals, 0)
rho_psd = eigvecs @ np.diag(eigvals) @ eigvecs.conj().T
rho_psd /= np.trace(rho_psd)
```

### Non-Hermitian Observable
```python
# Fix: symmetrize
obs = (obs + obs.conj().T) / 2
```

## Implementation Notes

- Density matrix must remain: positive semi-definite, trace = 1, Hermitian
- Coherence measures quantum-like cognitive ambivalence
- Non-commuting operators are essential for order effects
- Product state approximation bridges to classical models
- Coherence decay is network-independent (universal rate)

## Related Skills

- `quantum-cognition` - broader quantum cognition methodology
- `quantum-probability-statistics` - quantum probability framework
- `gskl-quantum-cognition` - GKSL master equation cognitive modeling

## References

- arXiv:2607.01452 - "A quantum model of opinion dynamics on networks" (2026)
- Friedkin & Johnsen (1990) - Social Influence Network Theory
- Busemeyer & Bruza (2012) - Quantum Models of Cognition and Decision
