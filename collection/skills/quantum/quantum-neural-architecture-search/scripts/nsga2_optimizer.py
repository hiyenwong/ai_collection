#!/usr/bin/env python3
"""
NSGA-II optimizer for Quantum Neural Architecture Search.

Multi-objective evolutionary algorithm that finds Pareto-optimal
quantum circuit architectures balancing accuracy, efficiency, and
cutting overhead.
"""

import numpy as np
from typing import Dict, List, Tuple, Callable
from deap import base, creator, tools, algorithms
import random

class QNASOptimizer:
    """
    NSGA-II optimizer for QNAS.
    
    Optimizes three objectives:
    1. Validation error (accuracy)
    2. Runtime cost (efficiency)
    3. Cutting overhead (deployability)
    """
    
    def __init__(
        self,
        search_space: Dict,
        population_size: int = 100,
        generations: int = 50
    ):
        self.search_space = search_space
        self.population_size = population_size
        self.generations = generations
        
        # Initialize DEAP
        creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0))
        creator.create("Individual", Dict, fitness=creator.FitnessMulti)
        
        self.toolbox = base.Toolbox()
        
        # Register architecture generator
        self.toolbox.register("architecture", self._generate_architecture)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.architecture)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        
        # Register genetic operators
        self.toolbox.register("mate", self._crossover)
        self.toolbox.register("mutate", self._mutate)
        self.toolbox.register("select", tools.selNSGA2)
    
    def _generate_architecture(self) -> Dict:
        """
        Generate random architecture from search space.
        """
        return {
            'embedding': random.choice(self.search_space['embedding']),
            'cnot_pattern': random.choice(self.search_space['cnot_pattern']),
            'depth': random.randint(self.search_space['depth'][0], self.search_space['depth'][-1]),
            'qubits': random.randint(self.search_space['qubits'][0], self.search_space['qubits'][-1])
        }
    
    def _crossover(self, ind1: Dict, ind2: Dict) -> Tuple[Dict, Dict]:
        """
        Crossover two architectures.
        
        Strategy: Swap components between architectures.
        """
        # Swap embedding type
        if random.random() < 0.5:
            ind1['embedding'], ind2['embedding'] = ind2['embedding'], ind1['embedding']
        
        # Swap CNOT pattern
        if random.random() < 0.5:
            ind1['cnot_pattern'], ind2['cnot_pattern'] = ind2['cnot_pattern'], ind1['cnot_pattern']
        
        # Swap depth (blend)
        if random.random() < 0.5:
            ind1['depth'], ind2['depth'] = ind2['depth'], ind1['depth']
        
        # Swap qubits
        if random.random() < 0.5:
            ind1['qubits'], ind2['qubits'] = ind2['qubits'], ind1['qubits']
        
        return ind1, ind2
    
    def _mutate(self, architecture: Dict) -> Dict:
        """
        Mutate architecture.
        
        Strategy: Random component change.
        """
        # Mutate embedding type
        if random.random() < 0.2:
            architecture['embedding'] = random.choice(self.search_space['embedding'])
        
        # Mutate CNOT pattern
        if random.random() < 0.2:
            architecture['cnot_pattern'] = random.choice(self.search_space['cnot_pattern'])
        
        # Mutate depth
        if random.random() < 0.2:
            architecture['depth'] = random.randint(
                self.search_space['depth'][0],
                self.search_space['depth'][-1]
            )
        
        # Mutate qubits
        if random.random() < 0.2:
            architecture['qubits'] = random.randint(
                self.search_space['qubits'][0],
                self.search_space['qubits'][-1]
            )
        
        return architecture
    
    def optimize(
        self,
        evaluate_fn: Callable,
        verbose: bool = True
    ) -> List[Dict]:
        """
        Run NSGA-II optimization.
        
        Args:
            evaluate_fn: Function to evaluate architecture
                Returns: [validation_error, runtime_cost, cutting_overhead]
            verbose: Print progress
        
        Returns:
            Pareto front (list of non-dominated architectures)
        """
        # Initialize population
        population = self.toolbox.population(n=self.population_size)
        
        # Evaluate initial population
        fitnesses = map(evaluate_fn, population)
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit
        
        # Evolution loop
        for gen in range(self.generations):
            # Select parents
            offspring = tools.selTournamentDCD(population, len(population))
            offspring = [self.toolbox.clone(ind) for ind in offspring]
            
            # Crossover
            for i in range(0, len(offspring) - 1, 2):
                if random.random() < 0.9:
                    offspring[i], offspring[i+1] = self.toolbox.mate(offspring[i], offspring[i+1])
                    del offspring[i].fitness.values
                    del offspring[i+1].fitness.values
            
            # Mutation
            for ind in offspring:
                if random.random() < 0.1:
                    self.toolbox.mutate(ind)
                    del ind.fitness.values
            
            # Evaluate offspring
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(evaluate_fn, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit
            
            # Select next generation
            population = self.toolbox.select(population + offspring, self.population_size)
            
            if verbose and gen % 10 == 0:
                pareto_front = tools.sortNondominated(population, self.population_size)[0]
                print(f"Generation {gen}: Pareto front size = {len(pareto_front)}")
        
        # Get Pareto front
        pareto_front = tools.sortNondominated(population, self.population_size)[0]
        
        return pareto_front
    
    def analyze_pareto_front(self, pareto_front: List[Dict]) -> Dict:
        """
        Analyze Pareto front statistics.
        
        Returns:
            {
                'size': int,
                'best_accuracy': Dict,
                'best_efficiency': Dict,
                'best_deployability': Dict,
                'embedding_distribution': Dict,
                'cnot_distribution': Dict
            }
        """
        analysis = {
            'size': len(pareto_front)
        }
        
        # Find best for each objective
        architectures = list(pareto_front)
        
        # Sort by validation error (objective 0)
        best_accuracy = min(architectures, key=lambda x: x.fitness.values[0])
        analysis['best_accuracy'] = {
            'architecture': best_accuracy,
            'fitness': best_accuracy.fitness.values
        }
        
        # Sort by runtime cost (objective 1)
        best_efficiency = min(architectures, key=lambda x: x.fitness.values[1])
        analysis['best_efficiency'] = {
            'architecture': best_efficiency,
            'fitness': best_efficiency.fitness.values
        }
        
        # Sort by cutting overhead (objective 2)
        best_deployability = min(architectures, key=lambda x: x.fitness.values[2])
        analysis['best_deployability'] = {
            'architecture': best_deployability,
            'fitness': best_deployability.fitness.values
        }
        
        # Distribution analysis
        embedding_dist = {}
        cnot_dist = {}
        
        for arch in architectures:
            emb = arch['embedding']
            cnot = arch['cnot_pattern']
            
            embedding_dist[emb] = embedding_dist.get(emb, 0) + 1
            cnot_dist[cnot] = cnot_dist.get(cnot, 0) + 1
        
        analysis['embedding_distribution'] = embedding_dist
        analysis['cnot_distribution'] = cnot_dist
        
        return analysis


if __name__ == "__main__":
    # Example usage
    search_space = {
        'embedding': ['angle-y', 'angle', 'amplitude'],
        'cnot_pattern': ['sparse', 'full', 'linear'],
        'depth': [1, 2, 3, 4, 5],
        'qubits': [4, 6, 8]
    }
    
    optimizer = QNASOptimizer(
        search_space=search_space,
        population_size=50,
        generations=20
    )
    
    # Define evaluation function (placeholder)
    def evaluate(architecture):
        # Placeholder: random values for demo
        val_error = random.uniform(0.01, 0.1)
        runtime_cost = architecture['depth'] * architecture['qubits'] * 3
        cutting_overhead = 1 if architecture['qubits'] <= 8 else 4**(architecture['qubits'] - 8)
        
        return (val_error, runtime_cost, cutting_overhead)
    
    # Run optimization
    pareto_front = optimizer.optimize(evaluate, verbose=True)
    
    # Analyze results
    analysis = optimizer.analyze_pareto_front(pareto_front)
    
    print("\n=== Pareto Front Analysis ===")
    print(f"Size: {analysis['size']}")
    print(f"Best Accuracy: {analysis['best_accuracy']}")
    print(f"Best Efficiency: {analysis['best_efficiency']}")
    print(f"Best Deployability: {analysis['best_deployability']}")
    print(f"Embedding Distribution: {analysis['embedding_distribution']}")
    print(f"CNOT Distribution: {analysis['cnot_distribution']}")