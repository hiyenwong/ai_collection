---
name: classical-disjunction-effect-model
description: "Classical probability model that reproduces the disjunction effect via expectation-parameter partitioning, proving classical and quantum-like models have equivalent expressiveness for decision rates."
---

# Classical Disjunction Effect Model

## Description
Methodology for modeling the disjunction effect in human decision making within classical probability theory, by introducing a continuous expectation parameter that partitions the participant pool by ambiguity level. Proves that classical and quantum-like models have equivalent observable expressiveness — their difference lies only in how ambiguity is represented. Based on arXiv:2603.23233.

## Activation Keywords
- disjunction effect modeling
- classical decision process model
- prisoner's dilemma disjunction
- quantum-like decision comparison
- ambiguity set modeling
- 析取效应经典模型
- 量子类决策比较
- expectation parameter partitioning

## Tools Used
- exec: Run Python simulations of classical vs quantum decision models
- write: Create model configuration and analysis reports
- read: Load experimental data for model fitting

## Core Concepts

### The Disjunction Effect
The disjunction effect violates the classical law of total probability in human decision making: people's choices differ when they know the outcome vs. when they don't. Classically, P(defect) should equal P(defect|coop)×P(coop) + P(defect|defect)×P(defect), but empirically it doesn't.

### Key Innovation: Expectation Parameter Model
Instead of the binary certainty assumption (opponent will definitely cooperate or definitely defect), introduce a continuous expectation parameter θ ∈ [0,1] representing the anticipated likelihood of opponent defection. The participant pool is partitioned by expectation level, and the ambiguity set is the union of interior expectation bins.

### Classical-Quantum Equivalence Theorem
**Proved**: Any triple of defection rates (cooperate-known, defect-known, unknown) achievable by a quantum-like model can be reproduced exactly by a classical instance of the expectation-parameter model. Both frameworks have identical expressive power for observable rates.

### Substantive Difference
The difference is NOT in probability theory breaking down, but in:
1. **Ambiguity representation**: Classical uses expectation partitions; quantum uses superposition states
2. **Event semantics**: Quantum ambiguous pure states are generic (dense, full measure); classical certainty states are exceptional

## Usage Patterns

### Pattern 1: Reproducing Disjunction Effect Data
Given empirical defection rates across three conditions:
1. Define expectation bins θ₁, θ₂, ..., θₙ
2. Assign population weights to each bin
3. Compute weighted defection rates
4. Verify classical law of total probability holds

### Pattern 2: Classical-Quantum Comparison
For any quantum-like model producing rates (r_coop, r_defect, r_unknown):
1. Extract the three observable rates
2. Construct classical expectation partition matching all three
3. Prove equivalence: same rates, different ambiguity semantics

### Pattern 3: Ambiguity Set Construction
1. Partition participants by expectation level θ
2. Define certainty bins (θ ≈ 0 and θ ≈ 1)
3. Ambiguity set = union of all interior bins
4. Disjunction effect emerges from ambiguity set weighting

## Instructions for Agents

### Step 1: Identify the Decision Scenario
- Prisoner's Dilemma? Ellsberg Paradox? Other decision-under-uncertainty?
- Identify the three information conditions: known-cooperate, known-defect, unknown

### Step 2: Extract Empirical Rates
- Collect defection rates for each condition: (d_C, d_D, d_U)
- Verify the disjunction effect: d_U ≠ d_C×P(C) + d_D×P(D)

### Step 3: Construct Classical Model
- Choose number of expectation bins (start with 5-10)
- Solve for bin weights that reproduce the three rates
- Verify all weights are non-negative and sum to 1

### Step 4: Compare with Quantum-Like Model
- Map quantum state amplitudes to expectation parameters
- Show rate equivalence but semantic difference
- Document which representation is more natural for the domain

## Error Handling

### No Disjunction Effect Observed
If d_U ≈ d_C×P(C) + d_D×P(D), the disjunction effect is absent. The model reduces to standard classical decision theory — no special modeling needed.

### Negative Bin Weights
If solving produces negative weights, increase the number of bins or relax the constraint. This indicates the data cannot be fit with the current granularity.

### Over-parameterization
With too many bins, the model becomes unidentifiable. Use minimum bins (typically 3-5) that reproduce the data. Apply regularization to prefer smoother distributions.

## Examples

### Example: Prisoner's Dilemma
Empirical rates: P(defect|coop) = 0.3, P(defect|defect) = 0.7, P(defect|unknown) = 0.55
Classical prediction: 0.3×0.5 + 0.7×0.5 = 0.5 ≠ 0.55 (disjunction effect!)
Expectation model: Partition population into low/high/medium expectation bins to reproduce 0.55 while maintaining LOTP within each bin.

## Resources
- arXiv:2603.23233 — "Modeling the Disjunction Effect within Classical Probability"
- Related: quantum-cognition (quantum-like decision modeling)
- Related: quantum-game-theory-economics (game theory under uncertainty)
