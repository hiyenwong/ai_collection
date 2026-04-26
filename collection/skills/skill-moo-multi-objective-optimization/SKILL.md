---
name: skill-moo-multi-objective-optimization
description: "Multi-Objective Optimization of Agent Skills for Software Engineering (SkillMOO). Framework for evolving skill bundles using LLM-proposed edits and NSGA-II survivor selection. Activation: skill MOO, multi-objective optimization, agent skill evolution, NSGA-II optimization, skill bundle optimization."
---

# SkillMOO: Multi-Objective Skill Optimization

Multi-Objective Optimization of Agent Skills for Software Engineering - an automated framework that evolves skill bundles using LLM-proposed edits and NSGA-II survivor selection to balance success rate, cost, and runtime.

## Overview

Agent skills provide modular, task-specific guidance for LLM-based coding agents, but manually tuning skill bundles to balance multiple objectives is expensive and fragile. SkillMOO automates this process through:
- **LLM-proposed edits**: Intelligent skill bundle modifications
- **NSGA-II survivor selection**: Multi-objective evolutionary optimization
- **Three-way tradeoff**: Success rate, cost, and runtime

## Key Concepts

### 1. Skill Bundle Representation

**Structure**:
```python
class SkillBundle:
    """
    Represents a collection of agent skills.
    """
    def __init__(self):
        self.skills = []  # List of individual skills
        self.configuration = {}  # Skill parameters
        self.metadata = {
            'success_rate': 0.0,
            'cost': 0.0,
            'runtime': 0.0
        }
```

**Components**:
- **Skills**: Modular task-specific capabilities
- **Configuration**: Hyperparameters and settings
- **Metadata**: Performance metrics

### 2. Multi-Objective Optimization

**Objectives**:
1. **Success Rate**: Task completion accuracy
2. **Cost**: Token usage and API calls
3. **Runtime**: Execution time

**Pareto Optimality**:
- No objective can be improved without worsening another
- Maintains diverse tradeoff solutions
- Enables user selection based on priorities

### 3. NSGA-II Framework

**Algorithm**:
```
1. Initialize: Create random population of skill bundles
2. Evaluate: Run solver agent on SkillsBench tasks
3. Select: NSGA-II non-dominated sorting + crowding distance
4. Evolve: LLM proposes edits based on failure analysis
5. Repeat: Until convergence or budget exhausted
```

**Selection Criteria**:
- **Non-dominated sorting**: Rank by dominance
- **Crowding distance**: Maintain diversity
- **Elitism**: Preserve best solutions

## Implementation Guide

### Step 1: Population Initialization

```python
def initialize_population(size, skill_library):
    """
    Create initial population of skill bundles.
    
    Args:
        size: Population size
        skill_library: Available skills to combine
    
    Returns:
        List of SkillBundle objects
    """
    population = []
    for _ in range(size):
        bundle = SkillBundle()
        # Randomly select skills
        num_skills = random.randint(3, 10)
        bundle.skills = random.sample(skill_library, num_skills)
        # Random configuration
        bundle.configuration = {
            'temperature': random.uniform(0.1, 1.0),
            'max_tokens': random.choice([1024, 2048, 4096]),
            'skill_weights': random_weights(len(bundle.skills))
        }
        population.append(bundle)
    return population
```

### Step 2: Evaluation Pipeline

```python
class SolverAgent:
    """
    Evaluates skill bundles on coding tasks.
    """
    
    def __init__(self, benchmark):
        self.benchmark = benchmark  # SkillsBench dataset
    
    def evaluate(self, skill_bundle):
        """
        Evaluate skill bundle on benchmark tasks.
        
        Returns:
            metrics: Dict with success_rate, cost, runtime
        """
        results = []
        for task in self.benchmark:
            result = self.run_task(task, skill_bundle)
            results.append(result)
        
        metrics = {
            'success_rate': mean([r['success'] for r in results]),
            'cost': sum([r['tokens'] for r in results]),
            'runtime': sum([r['time'] for r in results])
        }
        return metrics
    
    def run_task(self, task, skill_bundle):
        """Execute task with given skill bundle."""
        # Apply skills to LLM
        # Run task
        # Collect metrics
        pass
```

### Step 3: Failure Analysis

```python
class FailureAnalyzer:
    """
    Analyzes failures to propose skill edits.
    """
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def analyze(self, skill_bundle, failures):
        """
        Analyze failures and propose edits.
        
        Args:
            skill_bundle: Current skill bundle
            failures: List of failed tasks with error info
        
        Returns:
            Proposed edits as structured modifications
        """
        prompt = f"""
        Analyze these task failures:
        {format_failures(failures)}
        
        Current skill bundle:
        {format_skills(skill_bundle)}
        
        Propose specific edits to improve performance:
        1. Skill modifications
        2. Configuration changes
        3. New skill additions
        4. Skill removals
        
        Format: JSON with edit operations
        """
        
        response = self.llm.generate(prompt)
        edits = parse_edits(response)
        return edits
```

### Step 4: NSGA-II Selection

```python
from deap import base, creator, tools

def nsga2_selection(population, offspring, pop_size):
    """
    NSGA-II selection with non-dominated sorting.
    
    Args:
        population: Current population
        offspring: New candidates
        pop_size: Target population size
    
    Returns:
        Selected individuals for next generation
    """
    # Combine populations
    combined = population + offspring
    
    # Non-dominated sorting
    fronts = sort_non_dominated(combined)
    
    # Select by fronts
    next_pop = []
    for front in fronts:
        if len(next_pop) + len(front) <= pop_size:
            next_pop.extend(front)
        else:
            # Use crowding distance for last front
            distances = calculate_crowding_distance(front)
            sorted_front = sort_by_distance(front, distances)
            remaining = pop_size - len(next_pop)
            next_pop.extend(sorted_front[:remaining])
            break
    
    return next_pop

def sort_non_dominated(population):
    """
    Fast non-dominated sorting algorithm.
    """
    fronts = [[]]
    domination_count = {}
    dominated_solutions = {}
    
    for p in population:
        domination_count[p] = 0
        dominated_solutions[p] = []
        
        for q in population:
            if p != q:
                if dominates(p, q):
                    dominated_solutions[p].append(q)
                elif dominates(q, p):
                    domination_count[p] += 1
        
        if domination_count[p] == 0:
            fronts[0].append(p)
    
    i = 0
    while len(fronts[i]) > 0:
        next_front = []
        for p in fronts[i]:
            for q in dominated_solutions[p]:
                domination_count[q] -= 1
                if domination_count[q] == 0:
                    next_front.append(q)
        i += 1
        fronts.append(next_front)
    
    return fronts[:-1]  # Remove empty last front
```

### Step 5: Evolution Loop

```python
class SkillMOO:
    """
    Main SkillMOO optimization loop.
    """
    
    def __init__(self, config):
        self.config = config
        self.solver = SolverAgent(config.benchmark)
        self.analyzer = FailureAnalyzer(config.llm)
        self.optimizer = NSGAII_Optimizer()
    
    def optimize(self, generations=50):
        """
        Run multi-objective optimization.
        
        Args:
            generations: Number of evolution generations
        
        Returns:
            Pareto-optimal skill bundles
        """
        # Initialize population
        population = initialize_population(
            self.config.pop_size,
            self.config.skill_library
        )
        
        # Evaluate initial population
        for bundle in population:
            bundle.metrics = self.solver.evaluate(bundle)
        
        # Evolution loop
        for gen in range(generations):
            print(f"Generation {gen + 1}/{generations}")
            
            # Generate offspring
            offspring = []
            for bundle in population:
                # Identify failures
                failures = self.get_failures(bundle)
                
                # Propose edits
                if failures:
                    edits = self.analyzer.analyze(bundle, failures)
                    new_bundle = apply_edits(bundle, edits)
                    offspring.append(new_bundle)
            
            # Evaluate offspring
            for bundle in offspring:
                bundle.metrics = self.solver.evaluate(bundle)
            
            # NSGA-II selection
            population = nsga2_selection(
                population, 
                offspring,
                self.config.pop_size
            )
        
        # Return Pareto front
        return get_pareto_front(population)
```

## Tools Used

- **deap**: Distributed Evolutionary Algorithms in Python
- **openai**: LLM API for edit proposals
- **pandas**: Metrics analysis
- **matplotlib**: Pareto front visualization
- **exec**: Run optimization experiments
- **read**: Load skill libraries
- **write**: Save optimized skill bundles

## Workflow

### Phase 1: Setup

1. **Define Objectives**:
   - Set target success rate
   - Define cost constraints
   - Specify runtime limits

2. **Prepare Benchmark**:
   - Load SkillsBench tasks
   - Define evaluation metrics
   - Set up test environment

3. **Initialize Library**:
   - Import available skills
   - Define skill templates
   - Set configuration ranges

### Phase 2: Optimization

1. **Run Evolution**:
   - Execute NSGA-II generations
   - Track Pareto front evolution
   - Monitor convergence

2. **Analyze Results**:
   - Visualize Pareto front
   - Compare tradeoffs
   - Identify knee points

3. **Select Solutions**:
   - Choose based on priorities
   - Validate on holdout set
   - Export final bundles

### Phase 3: Deployment

1. **Integration**:
   - Deploy to agent system
   - Monitor performance
   - Collect feedback

2. **Continuous Improvement**:
   - Retrain with new tasks
   - Update skill library
   - Refine objectives

## Activation Keywords

- skill MOO
- multi-objective optimization
- agent skill evolution
- NSGA-II optimization
- skill bundle optimization
- pareto optimization
- evolutionary skill design
- skillsbench evaluation

## Example Applications

### Example 1: Coding Agent Optimization

```python
config = {
    'skill_library': load_skill_library('coding_skills.json'),
    'benchmark': load_benchmark('skillsbench_v2'),
    'pop_size': 100,
    'generations': 50,
    'objectives': ['success_rate', 'cost', 'runtime']
}

# Run optimization
moo = SkillMOO(config)
pareto_front = moo.optimize()

# Select optimal bundle
for bundle in pareto_front:
    print(f"Success: {bundle.metrics['success_rate']:.2%}")
    print(f"Cost: {bundle.metrics['cost']:.0f} tokens")
    print(f"Runtime: {bundle.metrics['runtime']:.1f}s")
```

### Example 2: Domain-Specific Skills

```python
# Data science skill optimization
domain_config = {
    'skill_library': data_science_skills,
    'benchmark': data_science_tasks,
    'constraints': {
        'min_success_rate': 0.85,
        'max_cost': 10000
    }
}

moo = SkillMOO(domain_config)
optimized_skills = moo.optimize()
```

## Performance Results

**Baseline (Manual Tuning)**:
- Success rate: 65%
- Cost: 8,000 tokens/task
- Runtime: 45s/task

**SkillMOO Optimized**:
- Success rate: 78% (+13%)
- Cost: 5,200 tokens/task (-35%)
- Runtime: 32s/task (-29%)

## Research Source

**Paper**: SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering
- **arXiv**: 2604.09297
- **Authors**: Gong, Gu, Fei, Cao, Twist, et al.
- **Published**: April 2026
- **Category**: Software Engineering (cs.SE)

## Related Skills

- **skill-creator**: Skill creation guidelines
- **agent-coordinator**: Multi-agent systems
- **prompt-optimization**: Prompt engineering optimization
- **meta-cognitive-tool-optimization**: Tool use optimization

## References

- Gong et al., "SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering", arXiv:2604.09297, 2026.
- Deb et al., "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II", IEEE TEC 2002.
- SkillsBench: https://github.com/skills/skillsbench

---

_Last updated: 2026-04-13_
