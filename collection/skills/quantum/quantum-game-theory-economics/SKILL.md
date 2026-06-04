---
name: quantum-game-theory-economics
version: v1.0.0
last_updated: 2026-04-06
description: "Quantum game theory applications in economics and decision science. Use when analyzing quantum strategies in games, Nash equilibrium in quantum games, quantum entanglement in decision theory, quantum coins, quantum auctions, quantum bargaining. Keywords: quantum game theory, quantum economics, Nash equilibrium quantum, quantum strategy, quantum decision theory, quantum games, Bell inequality economics, quantum auction, quantum bargaining, 量子博弈, 量子经济学."
---

# Quantum Game Theory & Economics

Skill for analyzing quantum game theory applications in economics and strategic decision-making.

## Activation Keywords
- quantum game theory
- quantum economics
- Nash equilibrium quantum
- quantum strategy
- quantum decision theory
- quantum games
- Bell inequality economics
- quantum auction
- quantum bargaining
- 量子博弈
- 量子经济学
- quantum Nash
- Eisert Wilkens Lewenstein game

## Key Concepts

### 1. Quantum Game Theory Foundation

**Core Insight:** "Nashian game theory is incompatible with quantum physics" (arxiv:2112.03881)

The classical Nash equilibrium concept violates quantum mechanical principles:
- Quantum entanglement creates strategy correlations impossible in classical games
- Bell inequality violations show quantum games enable new equilibria
- Quantum superposition allows "mixed strategies" beyond classical probability

**Key Papers (kg.db):**
- `Nashian game theory is incompatible with quantum physics` (arxiv:2112.03881)
- `Quantum games and synchronicity` - Categorical quantum mechanics approach
- `Theory of Quantum Games and Quantum Economic Behavior` (arxiv:2010.14098)

### 2. Eisert-Wilkens-Lewenstein (EWL) Protocol

The foundational quantum game framework:

```
EWL Protocol Steps:
1. Prepare initial quantum state |00⟩
2. Apply entanglement operator J
3. Players apply quantum strategies U_A, U_B
4. Apply disentanglement operator J†
5. Measure final state
6. Payoff based on measurement outcome
```

**Quantum Strategies:**
- Classical moves correspond to specific unitary operators
- Quantum moves use full SU(2) space
- Quantum advantage from exploring strategy space beyond classical

### 3. Quantum Coin Flipping

**Application:** Fair coin flipping without trusted third party

```python
# Quantum coin flip protocol
def quantum_coin_flip():
    """
    Players: Alice and Bob
    Protocol:
    1. Alice prepares |0⟩ or |1⟩
    2. Bob measures or flips
    3. Check for cheating via quantum verification
    
    Quantum advantage: 
    - Detects cheating with higher probability
    - Uses entanglement for fairness
    """
    pass
```

### 4. Quantum Prisoner's Dilemma

**Quantum Advantage:**
- Classical dilemma: both defect (Nash equilibrium)
- Quantum: can achieve "Pareto optimal" mutual cooperation
- Entanglement creates new equilibrium "quantum cooperation"

**Payoff Matrix (Quantum):**
```
          Cooperate(Q)  Defect(D)
Cooperate  (3,3)        (0,5)
Defect     (5,0)        (1,1)
Quantum(Q) (3,3)        (0,5) ← new quantum strategy
```

### 5. Quantum Auctions

**Features:**
- Sealed-bid auctions with quantum bid encoding
- Privacy preserved through quantum mechanics
- Post-audit verification without revealing bids

```python
# Quantum sealed-bid auction
def quantum_auction():
    """
    1. Bidders encode bids in quantum states
    2. Auctioneer performs quantum operations
    3. Winner determined without revealing all bids
    4. Quantum verification for fairness
    
    Advantages:
    - Privacy: bids remain secret
    - Fairness: quantum mechanics prevents manipulation
    - Efficiency: single-round auction
    """
    pass
```

### 6. Quantum Bargaining

**Nash Bargaining Solution in Quantum:**
- Classical: maximize product of utilities
- Quantum: entangled utilities create new solution space
- Quantum entanglement as "bargaining chip"

### 7. Parameterized Quantum Game Circuits for Economic Modeling (arXiv:2605.18080)

**EWL circuit as economic recommender**: Real funding data (CORDIS Horizon Europe) weights parameterize local strategy rotations in 4-qubit EWL circuits.

- **Circuit**: 22 gates, depth 11 — NISQ compatible, O(n) scaling for n-round communications
- **Strategy tuning**: Each helix actor's rotation θ_i = w_i · π, where w_i is normalized dominance weight from real data
- **Output**: Measurement probabilities → recommender scores for disruptive vs sustaining innovation
- **Dirac-Solow-Swan integration**: Game probabilities map to diagonal Dirac potential; combined with classical growth model for capital accumulation simulation
- **Bifurcation detection**: Time-evolution reveals capital trajectory bifurcations under disruptive innovation

See also: `quantum-growth-modeling` skill for implementation details and code patterns.

### 8. Quantum Market Games

**Applications:**
- Quantum stock market models
- Quantum portfolio games
- Quantum trading strategies
- Quantum financial derivatives

## Instructions for Agents

### Analyzing Quantum Game Papers

1. **Identify game type:**
   - Prisoner's dilemma → EWL protocol
   - Coin flip → quantum cryptographic game
   - Auction → quantum sealed-bid
   - Bargaining → quantum Nash solution

2. **Extract quantum mechanisms:**
   - Entanglement operator J
   - Strategy space (SU(2) for 2-player)
   - Measurement operators
   - Payoff functions

3. **Compare classical vs quantum:**
   - Classical Nash equilibrium
   - Quantum equilibria (new strategies)
   - Quantum advantage (if exists)
   - Cheating detection probability

4. **Assess economic implications:**
   - Market efficiency gains
   - Privacy/fairness benefits
   - Strategic complexity
   - Implementation feasibility

## Knowledge Graph Integration

```bash
# Find quantum game papers
sqlite3 kg.db "SELECT name FROM kg_entities 
WHERE entity_type='paper' 
AND name LIKE '%quantum game%' OR name LIKE '%Nash%'"

# Find quantum economics keywords
sqlite3 kg.db "SELECT name FROM kg_entities 
WHERE entity_type='keyword' 
AND name LIKE '%quantum game%' OR name LIKE '%quantum economics%'"
```

## Mathematical Framework

### Quantum Strategy Operator

For 2-player games with 2 classical moves:
```
U(θ, φ) = [cos(θ/2)         -i·sin(θ/2)]
          [i·sin(θ/2)·e^iφ   cos(θ/2)·e^iφ]

θ ∈ [0, π], φ ∈ [0, π/2]

Classical strategies:
- Cooperate: θ = 0
- Defect: θ = π, φ = 0
```

### Entanglement Operator

```
J = 1/√2 · [1  1  1  1]
           [1 -1  1 -1]
           [1  1 -1 -1]
           [1 -1 -1  1]

Creates maximally entangled initial state
```

### Payoff Quantum Operator

```
Π = J†(U_A ⊗ U_B)† J† Π_classical J(U_A ⊗ U_B) J

Quantum payoff from classical payoff matrix Π_classical
```

## Related Skills

- **quantum-finance-analysis**: Portfolio and risk applications
- **quantum-mechanics-foundation**: Quantum physics basics
- **game-theory-classical**: Classical game theory comparison
- **quantum-cryptography**: Quantum cryptographic protocols

## Resources

- arxiv:2112.03881 - "Nashian game theory is incompatible with quantum physics"
- arxiv:2010.14098 - "Theory of Quantum Games and Quantum Economic Behavior"
- Eisert, Wilkens, Lewenstein (1999) - "Quantum Games and Quantum Strategies"
- kg.db: Quantum game theory papers (2 papers, 11 keywords)