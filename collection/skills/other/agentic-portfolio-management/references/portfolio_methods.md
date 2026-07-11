# Portfolio Construction Methods

Reference guide for 20+ portfolio construction methods used in agentic portfolio management.

## Classical Methods

### 1. Mean-Variance Optimization (Markowitz)

**Formula:**
```
minimize: w'Σw - λw'μ
subject to: w'1 = 1, w ≥ 0
```

**Parameters:**
- μ: Expected returns vector
- Σ: Covariance matrix
- λ: Risk tolerance parameter

**Strengths:**
- Mathematically rigorous
- Optimal for Gaussian returns

**Weaknesses:**
- Sensitive to input errors
- Concentrated portfolios
- Estimation risk

---

### 2. Black-Litterman Model

**Formula:**
```
Π = δΣw_mkt
E[R] = [(τΣ)^(-1) + P'Ω^(-1)P]^(-1) [(τΣ)^(-1)Π + P'Ω^(-1)Q]
```

**Parameters:**
- Π: Implied equilibrium returns
- Q: Investor views
- P: View matrix
- Ω: View confidence
- τ: Scaling factor

**Strengths:**
- Incorporates investor views
- Stable estimates
- Combines market equilibrium

**Weaknesses:**
- View specification complexity
- Requires market cap weights
- Subjective confidence levels

---

### 3. Risk Parity

**Formula:**
```
w_i ∝ 1/σ_i
or: w_i σ_i = w_j σ_j for all i,j
```

**Parameters:**
- σ_i: Individual asset risk
- Target: Equal risk contribution

**Strengths:**
- Diversified risk allocation
- No return forecasts needed
- Robust to estimation error

**Weaknesses:**
- Ignores return potential
- May overweight low-risk assets
- Leverage needed for returns

---

## Advanced Methods

### 4. Hierarchical Risk Parity (HRP)

**Algorithm:**
1. Compute correlation matrix
2. Cluster assets (hierarchical tree)
3. Allocate within clusters
4. Allocate across clusters

**Strengths:**
- No matrix inversion
- Handles ill-conditioned matrices
- Machine learning approach

**Weaknesses:**
- Cluster stability
- No return optimization
- Complexity

---

### 5. Factor-Based Allocation

**Formula:**
```
r_i = α_i + β_i'F + ε_i
w_opt = argmax w'(α + βF) - λw'Σw
```

**Parameters:**
- F: Factor returns
- β: Factor loadings
- α: Alpha (idiosyncratic return)

**Strengths:**
- Dimensionality reduction
- Factor-driven diversification
- Structured risk model

**Weaknesses:**
- Factor selection
- Factor model error
- Data intensive

---

### 6. Kelly Criterion

**Formula:**
```
f* = (p*b - q)/b
or continuous: f* = μ/σ²
```

**Parameters:**
- p: Win probability
- q: Loss probability
- b: Win/loss ratio
- μ: Expected return
- σ²: Return variance

**Strengths:**
- Growth-optimal
- Mathematically optimal for long-term
- Considers bet size

**Weaknesses:**
- Aggressive allocations
- Can exceed constraints
- Assumes known probabilities

---

### 7. Robust Optimization

**Formula:**
```
minimize: max_{μ∈U} w'μ - λw'Σw
U = {μ | ||μ - μ0|| ≤ δ}
```

**Parameters:**
- U: Uncertainty set
- δ: Uncertainty radius

**Strengths:**
- Handles estimation error
- Worst-case optimization
- Bounded performance

**Weaknesses:**
- Conservative allocations
- Uncertainty set design
- Complexity

---

## Goal-Based Methods

### 8. Goal-Based Allocation (Goals-Based Investing)

**Formula:**
```
minimize: P(goal shortfall)
subject to: budget constraints
```

**Parameters:**
- Goal: Target wealth
- Time horizon: Years to goal
- Probability: Required success rate

**Strengths:**
- Client-centered
- Multiple goals support
- Risk defined as goal failure

**Weaknesses:**
- Probability estimation
- Goal definition complexity
- Limited to defined goals

---

### 9. Liability-Driven Investment (LDI)

**Formula:**
```
w = w_deficit + w_growth
w_deficit: Match liability cash flows
w_growth: Growth component
```

**Parameters:**
- Liabilities: Cash flow schedule
- Duration: Liability duration
- Surplus: Assets - Liabilities

**Strengths:**
- Liability matching
- Risk reduction
- Pension fund appropriate

**Weaknesses:**
- Complex liability modeling
- Duration matching limits
- Opportunity cost

---

## Alternative Methods

### 10. Maximum Diversification

**Formula:**
```
maximize: D(w) = w'Σw / (Σ_i w_i σ_i)²
```

**Parameters:**
- D: Diversification ratio
- Σ: Covariance matrix

**Strengths:**
- Maximum diversification
- No return forecasts
- Robust

**Weaknesses:**
- Ignores returns
- Concentrated if assets similar
- No alpha consideration

---

### 11. Minimum Correlation

**Formula:**
```
minimize: Σ_i Σ_j w_i w_j ρ_ij σ_i σ_j
```

**Parameters:**
- ρ_ij: Correlation between i and j

**Strengths:**
- Low correlation focus
- Tail risk reduction
- Simple objective

**Weaknesses:**
- Ignores returns
- May underweight high-return assets
- Correlation instability

---

### 12. Entropy-Based Allocation

**Formula:**
```
maximize: H(w) = -Σ_i w_i log(w_i)
subject to: return/risk constraints
```

**Parameters:**
- H: Entropy (diversification measure)

**Strengths:**
- Maximum diversification
- Information theory basis
- Even allocation tendency

**Weaknesses:**
- Ignores asset differences
- No optimization
- Limited alpha

---

## Machine Learning Methods

### 13. Reinforcement Learning Portfolio

**Algorithm:**
```
state: Market features
action: Portfolio weights
reward: Portfolio return - risk penalty
policy: π(s) → a
```

**Strengths:**
- Adaptive to regimes
- Learns from data
- No explicit assumptions

**Weaknesses:**
- Training data needed
- Overfitting risk
- Explainability issues

---

### 14. Genetic Algorithm Optimization

**Algorithm:**
1. Generate random portfolios (population)
2. Evaluate fitness (Sharpe, utility)
3. Select best (selection)
4. Combine portfolios (crossover)
5. Mutate weights (mutation)
6. Iterate

**Strengths:**
- Global search
- Handles constraints
- Multi-objective

**Weaknesses:**
- Computational cost
- No guarantees
- Parameter tuning

---

### 15. Bayesian Optimization

**Formula:**
```
posterior: P(w | data)
predictive: P(return | w, data)
optimize: argmax E[utility | w]
```

**Strengths:**
- Uncertainty quantification
- Sequential optimization
- Few evaluations needed

**Weaknesses:**
- Gaussian process assumption
- Computation for large dimensions
- Hyperparameter tuning

---

## Specialized Methods

### 16. Sector Rotation

**Formula:**
```
w_sector(t) = f(economic_cycle(t))
```

**Parameters:**
- Economic cycle indicator
- Sector expected returns
- Cycle phase detection

**Strengths:**
- Macro-driven
- Cycle-based alpha
- Intuitive

**Weaknesses:**
- Cycle detection error
- Timing challenges
- Sector concentration

---

### 17. Tactical Asset Allocation (TAA)

**Formula:**
```
w = w_strategic + w_tactical
w_tactical: alpha signals
```

**Parameters:**
- Strategic weights (baseline)
- Tactical signals (adjustments)
- Signal strength

**Strengths:**
- Flexibility
- Alpha capture
- Risk control

**Weaknesses:**
- Signal decay
- Over-trading risk
- Transaction costs

---

### 18. Constant Proportion Portfolio Insurance (CPPI)

**Formula:**
```
exposure = m × cushion
cushion = portfolio - floor
floor: Minimum guarantee
```

**Parameters:**
- m: Multiplier (risk aversion)
- floor: Protected value
- exposure: Risky asset allocation

**Strengths:**
- Downside protection
- Dynamic risk management
- Guarantee mechanism

**Weaknesses:**
- Gap risk
- Multiplier sensitivity
- Cash drag

---

### 19. Option-Based Portfolio Insurance (OBPI)

**Formula:**
```
risky: Call options
safe: Bonds + put options
```

**Parameters:**
- Strike price: Protection level
- Option expiry: Horizon
- Option premium: Cost

**Strengths:**
- Defined protection
- Explicit insurance
- Payoff clarity

**Weaknesses:**
- Option cost
- Liquidity
- Complexity

---

### 20. Volatility Targeting

**Formula:**
```
w_vol_target = target_vol / realized_vol
```

**Parameters:**
- target_vol: Desired volatility
- realized_vol: Current volatility
- Leverage/deleverage

**Strengths:**
- Risk stabilization
- Vol control
- Adaptive leverage

**Weaknesses:**
- Volatility estimation
- Leverage limits
- Whipsaw risk

---

## Method Selection Guidelines

### Conservative Investors
- Risk parity
- Maximum diversification
- LDI

### Growth-Oriented
- Kelly (fractional)
- Mean-variance (high λ)
- Black-Litterman

### Goal-Based
- Goals-based investing
- CPPI/OBPI
- LDI

### Adaptive/Dynamic
- Reinforcement learning
- TAA
- Volatility targeting

### Robust/Stable
- HRP
- Robust optimization
- Bayesian

---

## Implementation Notes

1. **Run multiple methods** - Competitive testing
2. **Compare performance** - Backtest 5+ years
3. **Voting mechanism** - Weight by historical success
4. **Meta-agent review** - Adjust weights quarterly
5. **IPS constraints** - Filter method results

---

**Reference:** "The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management" (arXiv 2604.02279)