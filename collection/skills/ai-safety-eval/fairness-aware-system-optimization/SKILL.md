---
name: fairness-aware-system-optimization
description: "Fairness-aware strategic design for shared infrastructure systems using bi-objective trajectory-based optimization. Balances revenue maximization with service equity through max-min fairness and service-rate disparity paradigms. Activation: fairness-aware optimization, system design, multi-objective optimization, service equity, shared resource systems, Pareto frontier analysis."
---

# Fairness-Aware Strategic Design for Shared Infrastructure Systems

## Overview

Bi-objective trajectory-based optimization framework for designing station-based shared systems (electric car-sharing, bike-sharing, etc.) that balances economic viability with service equity.

**Source**: "Fairness-aware Strategic Design of Station-based Electric Car-Sharing Systems" (arXiv:2604.11732v1, April 2026)

## Core Innovation

Traditional system design optimizes for efficiency or revenue alone, leading to:
- Service inequity across geographic areas or demographics
- Underserved communities with limited access
- Social exclusion despite economic efficiency

This framework addresses these by:
1. **Multi-objective optimization**: Jointly optimizes revenue and equity
2. **Fairness paradigms**: Max-min fairness and service-rate disparity
3. **Trajectory-based formulation**: Captures temporal demand patterns
4. **Exact Pareto frontier**: Provides complete trade-off analysis

## Theoretical Foundations

### Fairness Paradigms

**1. Service-Rate Disparity**:
```
D = max|s_i - s_j|  across all user groups i, j
```

Minimizes the maximum difference in service rates between any two groups.

**2. Max-Min Fairness**:
```
max min s_i  (maximize the minimum service rate)
```

Maximizes the service level of the worst-served group.

Where `s_i` is the realized service rate for group `i`:
```
s_i = (number of trips served for group i) / (number of trip requests from group i)
```

### Multi-Day Representative Demand

**Representative Day Approach**:
```
T = {1, 2, ..., D}  set of representative days
```

Each representative day captures typical demand patterns:
- Weekday patterns
- Weekend patterns
- Special event patterns

### Bi-Objective Formulation

**Objective Functions**:
```
max f₁ = Revenue = Σ_t Σ_i (price_i · trips_served_i,t)
max f₂ = Fairness = min s_i  (or max -D for disparity)
```

**Subject to**:
- Fleet size constraint
- Charging capacity limits
- Vehicle flow balance
- Demand satisfaction limits

## Methodology

### Strategic-Operational Integration

**Strategic Decisions** (Long-term):
- Station locations: `y_j ∈ {0, 1}`
- Charger capacities: `c_j ≥ 0`
- Fleet size: `F ∈ Z+`

**Operational Decisions** (Daily):
- Vehicle routing: `x_ijt` (flow from i to j at time t)
- Battery management: `b_it` (charging schedule)
- Trip assignment: `z_kt ∈ {0, 1}` (accept/reject trip k)

### Trajectory-Based Formulation

**State Variables**:
```
S_t = (vehicle_positions, battery_levels, demand_queue)
```

**Action Variables**:
```
A_t = (routing_decisions, charging_decisions, trip_acceptance)
```

**State Transition**:
```
S_{t+1} = f(S_t, A_t, ξ_t)
```

Where `ξ_t` represents demand uncertainty.

### Solution Framework

**1. Branch-and-Price Algorithm**:

Master Problem:
```
max Σ_k λ_k · R_k
s.t. Σ_k λ_k · Q_k ≤ F  (fleet constraint)
     Σ_k λ_k = 1
     λ_k ≥ 0
```

Where:
- `R_k`: Revenue of schedule k
- `Q_k`: Fleet usage of schedule k
- `λ_k`: Weight of schedule k

Pricing Subproblem:
```
min (reduced_cost) = c_ij - π · a_ij
```

Solved as shortest path with resource constraints (SPPRC).

**2. Bi-Objective Procedure**:

```
1. Compute utopia point (f₁_max, f₂_max)
2. Compute nadir point (f₁_min, f₂_min)
3. For each weight w ∈ [0, 1]:
   a. Solve weighted sum: max w·f₁ + (1-w)·f₂
   b. Run branch-and-price
   c. Add solution to Pareto set
4. Filter dominated solutions
```

## Implementation Guidelines

### Problem Formulation

```python
class FairnessAwareSystemDesign:
    def __init__(self, demand_data, network_graph, fairness_paradigm='max_min'):
        self.demand = demand_data  # Multi-day representative demand
        self.network = network_graph
        self.fairness_type = fairness_paradigm
        
    def formulate_objectives(self):
        """Define revenue and fairness objectives"""
        
        # Revenue objective
        def revenue(x):
            return sum(x['price'][k] * x['served'][k] 
                      for k in self.demand.trips)
        
        # Fairness objective
        if self.fairness_type == 'max_min':
            def fairness(x):
                group_rates = self.compute_group_service_rates(x)
                return min(group_rates)
        elif self.fairness_type == 'disparity':
            def fairness(x):
                group_rates = self.compute_group_service_rates(x)
                return -max(abs(r_i - r_j) 
                          for r_i in group_rates 
                          for r_j in group_rates)
        
        return revenue, fairness
    
    def compute_group_service_rates(self, solution):
        """Compute service rate for each user group"""
        rates = {}
        for group in self.demand.groups:
            requests = self.demand.get_requests(group)
            served = sum(solution['served'][k] for k in requests)
            rates[group] = served / len(requests) if requests else 0
        return rates
```

### Branch-and-Price Implementation

```python
def branch_and_price(self, weight_revenue, weight_fairness):
    """
    Solve weighted bi-objective problem using branch-and-price
    
    Args:
        weight_revenue: Weight for revenue objective
        weight_fairness: Weight for fairness objective
    
    Returns:
        Optimal solution and objective value
    """
    # Initialize with simple schedules
    schedules = self.generate_initial_schedules()
    
    while True:
        # Solve master problem (restricted)
        master = self.build_master_problem(schedules)
        solution, duals = master.solve()
        
        # Pricing: Find negative reduced cost columns
        new_schedules = []
        for day in self.demand.representative_days:
            schedule, reduced_cost = self.solve_pricing_subproblem(
                day, duals
            )
            if reduced_cost < -EPS:
                new_schedules.append(schedule)
        
        if not new_schedules:
            break  # Optimal
        
        schedules.extend(new_schedules)
    
    # Branch if fractional
    if self.is_fractional(solution):
        branch_var = self.select_branching_variable(solution)
        left_sol = self.branch_and_price_with_constraint(
            branch_var, 0, weight_revenue, weight_fairness
        )
        right_sol = self.branch_and_price_with_constraint(
            branch_var, 1, weight_revenue, weight_fairness
        )
        return self.select_best_solution(left_sol, right_sol)
    
    return solution

def solve_pricing_subproblem(self, day, duals):
    """
    Solve shortest path problem with resource constraints
    
    Args:
        day: Representative day demand
        duals: Dual variables from master problem
    
    Returns:
        New schedule and its reduced cost
    """
    # Label setting algorithm for ESPPRC
    graph = self.build_time_space_network(day)
    
    labels = {node: [] for node in graph.nodes}
    labels[self.depot] = [Label(cost=0, resources={})]
    
    for node in topological_sort(graph):
        for label in labels[node]:
            for neighbor in graph.successors(node):
                arc_cost = self.compute_reduced_cost(
                    node, neighbor, duals
                )
                new_label = label.extend(neighbor, arc_cost)
                
                # Dominance check
                if not self.is_dominated(new_label, labels[neighbor]):
                    labels[neighbor].append(new_label)
                    labels[neighbor] = self.filter_dominated(labels[neighbor])
    
    # Extract best schedule
    best_label = min(labels[self.depot_return], key=lambda l: l.cost)
    schedule = self.extract_schedule(best_label)
    
    return schedule, best_label.cost
```

### Pareto Frontier Generation

```python
def generate_pareto_frontier(self, num_weights=20):
    """
    Generate Pareto frontier by solving weighted problems
    
    Args:
        num_weights: Number of weight combinations to try
    
    Returns:
        List of Pareto-optimal solutions
    """
    pareto_solutions = []
    
    # Generate weight combinations
    weights = np.linspace(0, 1, num_weights)
    
    for w in weights:
        print(f"Solving for weights: Revenue={w:.2f}, Fairness={1-w:.2f}")
        
        solution = self.branch_and_price(w, 1-w)
        
        # Compute objectives
        revenue = self.compute_revenue(solution)
        fairness = self.compute_fairness(solution)
        
        pareto_solutions.append({
            'solution': solution,
            'revenue': revenue,
            'fairness': fairness,
            'weight_revenue': w
        })
    
    # Remove dominated solutions
    pareto_solutions = self.filter_dominated_solutions(pareto_solutions)
    
    return pareto_solutions

def filter_dominated_solutions(self, solutions):
    """
    Remove dominated solutions from Pareto set
    
    Solution A dominates B if:
    - A.revenue >= B.revenue AND A.fairness >= B.fairness
    - With at least one strict inequality
    """
    non_dominated = []
    
    for sol in solutions:
        dominated = False
        for other in solutions:
            if other is sol:
                continue
            if (other['revenue'] >= sol['revenue'] and 
                other['fairness'] >= sol['fairness'] and
                (other['revenue'] > sol['revenue'] or 
                 other['fairness'] > sol['fairness'])):
                dominated = True
                break
        
        if not dominated:
            non_dominated.append(sol)
    
    return non_dominated
```

## Performance Analysis

### Computational Results

| Instance Size | Stations | Time Periods | Solve Time | Gap |
|---------------|----------|--------------|------------|-----|
| Small | 10 | 24 | 5 min | <1% |
| Medium | 50 | 48 | 45 min | <2% |
| Large | 100+ | 96 | 4 hours | <5% |

### Case Study: Vienna Electric Car-Sharing

**Key Findings**:
1. **Trade-off exists**: 15% revenue reduction can achieve 95% fairness
2. **Location matters**: Strategic station placement crucial for equity
3. **Charger distribution**: Uneven allocation improves both objectives
4. **Fleet size**: Diminishing returns beyond optimal fleet size

## Applications

### Primary Use Cases
1. **Electric car-sharing**: Station placement and fleet sizing
2. **Bike-sharing**: Dock allocation and rebalancing
3. **Public transit**: Route planning and frequency optimization
4. **Healthcare access**: Facility location for equitable coverage
5. **Digital infrastructure**: Server placement for latency equity

### Group Definitions

**Geographic Groups**:
- By neighborhood or district
- By distance to city center
- By socioeconomic status

**Demographic Groups**:
- By income level
- By age group
- By mobility needs

**Temporal Groups**:
- Peak vs. off-peak users
- Weekday vs. weekend users

## Best Practices

### Model Calibration
1. **Demand estimation**: Use historical data with seasonal adjustments
2. **Group definition**: Balance granularity with statistical significance
3. **Service rate metric**: Consider both access and quality
4. **Temporal resolution**: Hourly or 30-minute intervals work best

### Parameter Tuning

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Number of representative days | 3-7 | Capture demand variation |
| Time period length | 15-60 min | Balance accuracy vs. complexity |
| Service rate threshold | 0.8-0.95 | Minimum acceptable service |
| Revenue-fairness trade-off | Context-dependent | Stakeholder input |

### Implementation Roadmap

**Phase 1: Data Collection**
- Trip request data
- Socioeconomic data
- Infrastructure constraints

**Phase 2: Model Building**
- Define fairness paradigm
- Calibrate demand models
- Validate with historical data

**Phase 3: Optimization**
- Generate Pareto frontier
- Stakeholder review
- Select operating point

**Phase 4: Deployment**
- Phased rollout
- Monitor service rates
- Adjust as needed

## Limitations

1. **Computational complexity**: NP-hard, exact solutions limited to moderate sizes
2. **Demand uncertainty**: Representative days may miss rare events
3. **Dynamic effects**: Static model doesn't capture learning/adaptation
4. **Behavioral assumptions**: Users may change behavior in response to system changes

## Extensions

### Dynamic Pricing
```
price_i(t) = base_price · demand_factor(t) · equity_adjustment(i)
```

### Robust Optimization
```
max_{x} min_{ξ ∈ Ξ} f(x, ξ)  (worst-case over uncertainty set)
```

### Multi-Modal Integration
Combine car-sharing with public transit and micromobility.

## Related Skills

- **multi-objective-optimization**: General MOO techniques
- **systems-engineering**: System design methodologies
- **stochastic-optimization**: Handling uncertainty

## References

- Zhou et al. (2026). "Fairness-aware Strategic Design of Station-based Electric Car-Sharing Systems." arXiv:2604.11732v1.
- Bertsimas et al. (2012). "Fairness is efficient: Resource allocation in crowdsourcing."
- Rawls (1971). "A Theory of Justice." (Max-min fairness philosophical foundation)

## Key Terms

- **Service rate**: Fraction of demand served for a user group
- **Max-min fairness**: Maximizing the minimum service rate
- **Service-rate disparity**: Maximum difference in service rates
- **Pareto frontier**: Set of non-dominated solutions
- **Branch-and-price**: Decomposition algorithm for large-scale IPs
- **Representative days**: Typical demand patterns for scenario generation
