# NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation
Skill for understanding and applying the NeuronSoup methodology from arXiv:2607.15217v1.

## Overview
NeuronSoup is a neural computation architecture that replaces synchronous layer-by-layer processing with asynchronous, delay-mediated signal propagation through a pool of shared neurons. The entire architecture is evolved via a genetic algorithm.

## Core Concepts
- **Asynchronous, delay-mediated signal propagation**: Signals propagate through shared neurons with time delays.
- **Shared neurons**: Neurons are reused across multiple paths, leading to interference based on signal timing and polarity.
- **Genetic algorithm optimization**: The topology, weights, delays, and connectivity are evolved using a genetic algorithm on a flat real-valued genome.
- **No backpropagation**: The system does not rely on gradient-based learning.
- **Adaptive computation depth**: The number of steps (path length) varies per input.
- **Lateral interactions**: The architecture discovers interactions between pathways that are hard to engineer in traditional networks.

## Applications
- Handwritten digit classification (MNIST) using frozen ResNet18 features.
- Potential for other domains by changing encoder and output structures.

## Implementation Steps
1. Define the input and output encoders for your domain.
2. Set up a pool of neurons with configurable delays.
3. Define a genotype that encodes the network topology, weights, delays, and connectivity as a flat real-valued vector.
4. Implement a genetic algorithm (selection, crossover, mutation) to evolve the genotype.
5. For each genotype, simulate the network: for each input, route signals through the shared neurons according to the topology, accumulating state at each neuron visit.
6. Evaluate fitness based on task performance (e.g., classification accuracy).
7. Iterate until convergence or generation limit.
8. Deploy the best individual for inference.

## Pseudocode
```
Initialize population of genotypes (random vectors)
For each generation:
    For each genotype:
        Decode genotype into network parameters (topology, weights, delays)
        For each input sample:
            Activate input neurons
            Propagate signals asynchronously through the network with delays
            Accumulate neuron states based on visitation order and signal polarity
            Read output from output neurons
        Compute fitness (e.g., classification accuracy)
    Select top performers
    Apply crossover and mutation to create next generation
```

## Parameters to Tune
- Population size
- Mutation rate
- Crossover strategy
- Number of generations
- Neuron pool size
- Delay values
- Signal encoding schemes

## Pitfalls
- The genotype space is huge (14,602 dimensions in the paper), requiring careful genetic algorithm design.
- Evaluating each individual requires simulating the network for all training samples, which can be slow.
- The asynchronous simulation must accurately model the accumulation of states.
- Genetic algorithms can be sensitive to hyperparameters.

## Activation Keywords
- asynchronous signal propagation
- shared neurons
- genetic algorithm
- no backpropagation
- temporal graphs
- neuroscience-inspired architecture
- evolution of neural topology

## References
- arXiv:2607.15217v1 - NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation

## Related Skills
- None yet