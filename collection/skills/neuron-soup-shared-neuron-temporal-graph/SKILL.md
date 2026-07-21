---
name: neuron-soup-shared-neuron-temporal-graph
description: A skill for understanding and applying the NeuronSoup architecture: an evolving asynchronous, shared-neuron temporal graph model that replaces backpropagation with genetic algorithms and delay-mediated signal processing.
tags: []
related_skills: []
content: |
  ## NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation

  **arXiv:2607.15217v1** – Subodh Kalia (2026-07-16)

  ### Core Idea
  NeuronSoup replaces synchronous layer‑by‑layer processing with asynchronous, delay‑mediated signal propagation through a pool of shared neurons. Each signal path routes a continuous‑valued signal from an input neuron to an output neuron via a variable number of intermediate hidden neurons. Hidden neurons are physically shared across paths: when two paths converge on the same neuron, the second arrival encounters the accumulated state left by the first, producing constructive or destructive interference that depends on signal polarity and arrival timing. The entire architecture—topology, weights, delays, and connectivity—is co‑evolved by a genetic algorithm operating on a flat real‑valued genome.

  ### Why It Matters
  - Eliminates the need for differentiable computation graphs and backpropagation.
  - Allows adaptive computation depth per sample (like biological brains).
  - Discovers latent lateral interactions between pathways without explicit wiring.
  - Demonstrates competitive performance (85.9% on MNIST) with a compact model (115 KB).

  ### Activation Phrases
  - neuron soup
  - asynchronous shared neuron
  - temporal graph
  - evolving neural architecture
  - genetic algorithm neural network

  ### How to Apply (Step‑by‑Step)

  1. **Conceptualize the substrate**
     - Define a pool of N shared neurons (each with a scalar state).
     - Define a set of directed paths from input features to output classes.
     - Each edge on a path carries three evolvable parameters:
       - `target_neuron` (index of the destination neuron in the pool)
       - `weight` (real‑valued scaling factor)
       - `delay` (non‑negative real, time‑step offset)

  2. **Encode the genome**
     - Flatten all path‑edge parameters into a single real‑valued vector.
     - For a network with P paths and average length L, genome length ≈ 3 × P × L.
     - In the paper: 14,602 genes for 204 paths through 266 hidden neurons.

  3. **Simulate signal propagation**
     - Maintain a priority queue ordered by simulation time.
     - Inject input signals at time = 0 on the first edge of each path.
     - When an event (signal + weight + source neuron state) is popped:
       - Update the target neuron’s state: `state += weight * signal`.
       - Schedule the next edge on the same path at `current_time + delay`.
       - If the edge leads to an output neuron, record the contribution.

  4. **Fitness evaluation**
     - Run the network on a batch of inputs.
     - Compare aggregated output signals to targets (e.g., cross‑entropy loss).
     - Fitness = negative loss (or accuracy).

  5. **Evolve with a genetic algorithm**
     - Selection: tournament or roulette‑wheel based on fitness.
     - Crossover: path‑aware crossover – exchange whole path segments between parents to preserve functional units.
     - Mutation: Gaussian perturbation of weights/delays; occasional random rewiring of target_neuron indices.
     - Elitism: keep the top‑k individuals unchanged.

  6. **Iterate until convergence**
     - Monitor validation accuracy; stop when improvement plateaus.
     - The evolved network exhibits heterogeneous path lengths and abundant shared‑neuron usage (e.g., 156/266 neurons shared, one neuron participating in 11 paths).

  7. **Deploy and analyze**
     - The final substrate can be frozen and used for inference.
     - Examine the distribution of delays and shared‑neuron participation to infer learned temporal and interaction patterns.

  ### Pitfalls & Mitigations
  - **Assuming differentiability** – NeuronSoup is inherently non‑differentiable; gradient‑based methods will fail. Use evolutionary or reinforcement‑learning optimizers.
  - **Expecting layer‑like behavior** – Computation depth varies per input; do not assume a fixed number of steps.
  - **Ignoring delay values** – Delays are the primary mechanism for ordering computations; setting them to zero collapses the model to a static weighted graph.
  - **Treating shared neurons as independent** – The hallmark of NeuronSoup is the interference via accumulated state; models that reset neuron state per path lose the core mechanism.
  - **Over‑specifying genome length** – Too few genes limit expressive power; too many increase search space unnecessarily. Start with a modest pool size and let evolution discover path reuse.

  ### References
  - arXiv:2607.15217v1 – NeuronSoup: Evolving Asynchronous, Shared‑Neuron Temporal Graphs without Backpropagation
    URL: http://arxiv.org/abs/2607.15217v1
  - Supplementary material (if available) – see arXiv page for code and detailed genome format.

  ### Related Concepts
  - Spiking Neural Networks (SNNs) with temporal coding
  - Reservoir Computing / Liquid State Machines
  - Neuroevolution (NEAT, HyperNEAT)
  - Asynchronous logic and delay‑insensitive circuits
  - Neuromorphic hardware that exploits temporal dynamics

  ### Usage Example (pseudo‑code)
  ```python
  # Pseudo‑code illustrating the core loop
  population = initialize_population(pop_size=100, genome_len=14602)
  for gen in range(max_generations):
      fitnesses = []
      for genome in population:
          substrate = decode_genome(genome)   # paths, weights, delays
          outputs   = simulate(substrate, batch_X)
          loss      = compute_loss(outputs, batch_y)
          fitnesses.append(-loss)            # higher is better
      population = evolve(population, fitnesses)  # select, crossover, mutate
  best_substrate = decode_genome(argmax(fitnesses))
  ```

  ### Extending the Skill
  - Replace the genetic algorithm with CMA‑ES, NEAT, or reinforcement learning.
  - Experiment with different neuron models (e.g., leaky integrate‑and‑fire) for richer dynamics.
  - Apply to temporal‑sequential tasks (speech, video) where inherent asynchrony matches the data.
  - Investigate hardware implementation on neuromorphic chips that support configurable delays.