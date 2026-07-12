# NSGA-II: Non-dominated Sorting Genetic Algorithm II

## Overview

NSGA-II is a multi-objective evolutionary algorithm that finds Pareto-optimal solutions by maintaining a population of candidate solutions and evolving them through selection, crossover, and mutation.

## Key Concepts

### Pareto Dominance

A solution **x1** dominates **x2** if:
- x1 is no worse than x2 in all objectives
- x1 is strictly better than x2 in at least one objective

**Pareto Front**: Set of non-dominated solutions.

### Non-dominated Sorting

Rank solutions by dominance level:
1. **Rank 1**: Non-dominated solutions (Pareto front)
2. **Rank 2**: Solutions dominated only by Rank 1
3. **Rank 3**: Solutions dominated by Rank 1 and Rank 2
...

### Crowding Distance

Measure density of solutions around each individual:
- Solutions with higher crowding distance are preferred
- Maintains diversity in Pareto front

## Algorithm Steps

### Step 1: Initialization

```python
population = initialize_population(pop_size)
fitness = evaluate_population(population)
```

### Step 2: Non-dominated Sorting

```python
def non_dominated_sort(population, fitness):
    fronts = []
    rank = {}
    
    for i in range(len(population)):
        dominated_by = []
        dominates = []
        
        for j in range(len(population)):
            if dominates(population[i], population[j]):
                dominates.append(j)
            elif dominates(population[j], population[i]):
                dominated_by.append(j)
        
        if len(dominated_by) == 0:
            rank[i] = 1
            fronts[1].append(i)
    
    # Continue sorting for subsequent fronts
    current_front = 1
    while fronts[current_front]:
        next_front = []
        for i in fronts[current_front]:
            for j in dominates[i]:
                # Check if j can be in next front
                ...
        current_front += 1
    
    return fronts, rank
```

### Step 3: Crowding Distance Calculation

```python
def calculate_crowding_distance(front, fitness):
    distance = [0] * len(front)
    
    for objective in range(num_objectives):
        # Sort front by objective value
        sorted_front = sort_by_objective(front, fitness, objective)
        
        # Boundary solutions get infinite distance
        distance[sorted_front[0]] = float('inf')
        distance[sorted_front[-1]] = float('inf')
        
        # Calculate distance for intermediate solutions
        for i in range(1, len(sorted_front) - 1):
            distance[sorted_front[i]] += (
                fitness[sorted_front[i+1]][objective] - 
                fitness[sorted_front[i-1]][objective]
            ) / (max_objective[objective] - min_objective[objective])
    
    return distance
```

### Step 4: Selection

```python
def tournament_selection(population, rank, crowding_distance):
    # Binary tournament
    candidates = random.sample(range(len(population)), 2)
    
    # Compare by rank first
    if rank[candidates[0]] < rank[candidates[1]]:
        return candidates[0]
    elif rank[candidates[0]] > rank[candidates[1]]:
        return candidates[1]
    else:
        # If same rank, compare by crowding distance
        if crowding_distance[candidates[0]] > crowding_distance[candidates[1]]:
            return candidates[0]
        else:
            return candidates[1]
```

### Step 5: Crossover and Mutation

```python
def crossover(parent1, parent2):
    # Simulated binary crossover (SBX)
    child1, child2 = sbx_crossover(parent1, parent2)
    return child1, child2

def mutation(individual):
    # Polynomial mutation
    mutated = polynomial_mutation(individual)
    return mutated
```

### Step 6: Create Offspring

```python
def create_offspring(parent_population, pop_size):
    offspring = []
    
    while len(offspring) < pop_size:
        # Selection
        parent1 = tournament_selection(parent_population)
        parent2 = tournament_selection(parent_population)
        
        # Crossover
        child1, child2 = crossover(parent1, parent2)
        
        # Mutation
        child1 = mutation(child1)
        child2 = mutation(child2)
        
        offspring.extend([child1, child2])
    
    return offspring[:pop_size]
```

### Step 7: Combine and Select

```python
def select_next_generation(parent_pop, offspring_pop):
    # Combine populations
    combined = parent_pop + offspring_pop
    
    # Evaluate combined population
    fitness = evaluate(combined)
    
    # Non-dominated sorting
    fronts, rank = non_dominated_sort(combined, fitness)
    
    # Select next generation
    next_gen = []
    for front in fronts:
        if len(next_gen) + len(front) <= pop_size:
            next_gen.extend(front)
        else:
            # Fill remaining slots using crowding distance
            remaining = pop_size - len(next_gen)
            front_with_distance = calculate_crowding_distance(front, fitness)
            sorted_front = sort_by_crowding_distance(front, front_with_distance)
            next_gen.extend(sorted_front[:remaining])
            break
    
    return next_gen
```

### Step 8: Iterate

```python
def nsga2(pop_size, generations):
    # Initialize
    population = initialize_population(pop_size)
    fitness = evaluate(population)
    
    for gen in range(generations):
        # Create offspring
        offspring = create_offspring(population, pop_size)
        
        # Evaluate offspring
        offspring_fitness = evaluate(offspring)
        
        # Select next generation
        population = select_next_generation(population, offspring)
        fitness = evaluate(population)
        
        # Log Pareto front
        pareto_front = get_pareto_front(population, fitness)
        log_generation(gen, pareto_front)
    
    return get_pareto_front(population, fitness)
```

## Hyperparameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Population Size | Number of individuals | 100-500 |
| Generations | Number of iterations | 50-200 |
| Crossover Probability | Probability of crossover | 0.9 |
| Mutation Probability | Probability of mutation | 0.1 |
| Crossover Distribution Index | SBX distribution | 20 |
| Mutation Distribution Index | Polynomial mutation distribution | 20 |

## Advantages

1. **Elitism**: Preserves best solutions across generations
2. **Diversity**: Crowding distance maintains Pareto front spread
3. **Fast Non-dominated Sorting**: O(MN^2) complexity
4. **No Sharing Parameter**: Self-adaptive diversity maintenance

## Limitations

1. **Computational Cost**: O(MN^2) per generation (M objectives, N population)
2. **Local Pareto Fronts**: May converge to local Pareto fronts
3. **Scaling Issues**: Performance degrades with many objectives (>3)

## Applications

- **Engineering Design**: Trade-off between cost, quality, reliability
- **Portfolio Optimization**: Risk vs. return vs. diversity
- **Machine Learning**: Accuracy vs. complexity vs. inference time
- **Quantum Circuit Design**: Accuracy vs. depth vs. noise (QNAS)

## Implementation Libraries

```python
# Python: DEAP
from deap import algorithms, base, creator, tools

# Python: pymoo
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.optimize import minimize

# MATLAB: gamultiobj (built-in)
```

---

*Reference: Deb, K., et al. "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II" (2002)*