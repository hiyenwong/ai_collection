---
name: surviving-by-serving-sbs
description: "Surviving by Serving (SBS) principle for self-organization in complex adaptive systems - components persist when their outputs are utilized by others, prolonged non-utilization promotes adaptation. Minimal multi-agent model where agents transform shared resources with local utilization feedback, spontaneously forming functional networks with core-periphery structure. Use for self-organization, multi-agent resource networks, functional emergence, pre-adaptive search. Activation: self-organization, multi-agent, resource transformation, functional utilization, core-periphery, complex adaptive systems, pre-adaptation, SBS."
license: MIT
metadata:
  arxiv_id: "2606.26733"
  published: "2026-06-25"
  authors: "Claus Metzner, Ali Ghebleh, Achim Schilling, Andreas Maier, Thomas Kinfe, Patrick Krauss"
  categories: ["q-bio.NC", "cs.NE", "nlin.AO"]
  tags: [self-organization, complex-adaptive-systems, multi-agent, resource-transformation, functional-relevance, core-periphery, pre-adaptation, emergence, neuroscience, systems-theory]
---

# Surviving by Serving (SBS): Functional Relevance Drives Self-Organization

## Paper
**arXiv: 2606.26733** — "Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems" (Metzner, Ghebleh, Schilling, Maier, Kinfe, Krauss, 2026-06-25)

## Core Principle

**Surviving by Serving (SBS)**: Components in a complex adaptive system persist as long as their outputs are utilized by other components. Prolonged non-utilization promotes adaptation and exploration. This is a **substrate-independent, local-feedback mechanism** for the emergence and stabilization of organized structure without centralized control.

### Contrast with Existing Principles

| Principle | Persistence Criterion | Feedback |
|-----------|-----------------------|----------|
| **Natural selection** | Differential reproduction | Global (fitness) |
| **Hebbian learning** | Correlated co-activation | Local pairwise |
| **Free energy minimization** | Surprise reduction | Global (variational) |
| **SBS** | **Functional utilization by others** | **Local (downstream consumption)** |

SBS uniquely requires only *local* feedback (is my output consumed downstream?) — no global fitness signal, no explicit reward, no variational objective.

## SBS Multi-Agent Model

### Setup

- **N agents** share a common resource pool
- Each agent has a **transformation rule**: maps an input resource state to an output state
- **Local feedback**: agent receives a "served" signal only when its output is subsequently utilized (consumed) by another agent
- **Persistence rule**: agents that are consistently served maintain their transformation; agents that are NOT served enter an **exploration phase** (randomly modify their transformation)

### Key Dynamics

1. **Spontaneous self-organization**: Without any global objective, agents spontaneously form stable interaction networks
2. **Transformation chains**: Sequential resource transformations emerge (agent A → agent B → agent C), creating functional processing pipelines
3. **Core-periphery structure**: A core of highly-utilized agents surrounded by a periphery of explorers
4. **Novel state generation**: Exploration by non-served agents discovers new resource states that were previously inaccessible
5. **Pre-adaptive search phase**: Self-sustaining interaction networks can arise even without external selection pressure — a "pre-adaptive" search from which later functional solutions emerge

### Pseudocode

```python
class SBSAgent:
    def __init__(self, agent_id, transform_fn):
        self.id = agent_id
        self.transform = transform_fn  # maps input state → output state
        self.served_count = 0
        self.exploration_mode = False

class SBSModel:
    def __init__(self, n_agents, resource_pool, threshold=5):
        self.agents = [SBSAgent(i, random_transform()) for i in range(n_agents)]
        self.resource = resource_pool  # shared resource state
        self.threshold = threshold  # non-served steps before exploration
    
    def step(self):
        # 1. Agents produce outputs from current resource
        outputs = {}
        for agent in self.agents:
            outputs[agent.id] = agent.transform(self.resource)
        
        # 2. Determine utilization: output consumed if another agent can use it as input
        utilization = {aid: 0 for aid in outputs}
        for producer_id, output in outputs.items():
            for consumer in self.agents:
                if consumer.id != producer_id and self._is_utilizable(output, consumer):
                    utilization[producer_id] += 1
        
        # 3. Update served counts and exploration mode
        for agent in self.agents:
            if utilization[agent.id] > 0:
                agent.served_count += 1
                agent.exploration_mode = False
            else:
                agent.served_count = 0
                if agent.served_count == 0:  # consecutive non-served
                    agent.exploration_mode = True
        
        # 4. Exploration: non-served agents randomize their transform
        for agent in self.agents:
            if agent.exploration_mode:
                agent.transform = random_transform()
        
        # 5. Update resource (consumption/production balance)
        self.resource = self._update_resource(outputs, utilization)
```

## Key Results

### Emergent Phenomena (all without global objectives)

| Phenomenon | Description |
|------------|-------------|
| **Stable transformation chains** | Sequential processing pipelines (A→B→C→...) emerge and persist |
| **Core-periphery organization** | Core agents (high utilization) + periphery agents (exploring) |
| **Novel state generation** | Explorers discover resource states enabling previously impossible targets |
| **Pre-adaptive search** | Self-sustaining networks form before external pressure creates functional demand |
| **Robustness** | Removing core agents triggers re-organization; periphery fills functional gaps |

### Substrate Independence

SBS applies across domains because the principle is substrate-independent:
- **Neural circuits**: neurons persist when their outputs drive downstream activity
- **Gene regulatory networks**: gene products persist when utilized in regulatory cascades
- **Ecosystems**: species persist when their ecological outputs (nutrients, habitat) support others
- **Social/technological systems**: organizational units persist when their outputs are consumed

## When to Use

- **Self-organization modeling**: systems where organized structure emerges without centralized control
- **Multi-agent resource networks**: transformation chains, supply networks, metabolic networks
- **Functional emergence analysis**: studying how functional roles arise from local interactions
- **Pre-adaptive search**: modeling exploration phases before selection pressure
- **Complex adaptive systems theory**: neural circuits, gene networks, ecological webs, social organizations
- **Neuroscience**: modeling neural circuit self-organization, synaptic pruning, functional module emergence

## Relation to Existing Frameworks

- **Autopoiesis**: SBS provides a mechanistic implementation of autopoietic self-maintenance (components that serve the system persist)
- **Free Energy Principle**: SBS can be seen as a local heuristic approximating global free energy minimization — utilization as a proxy for prediction-error reduction
- **Evolutionary dynamics**: SBS generalizes selection from "reproduction" to "functional utilization" — broader and more substrate-independent
- **Self-organizing maps (SOM) / Kohonen networks**: SBS complements competitive learning with utilization-based persistence
- **Network science**: Predicts core-periphery structure as an emergent property of utilization dynamics

## Pitfalls

- **Definition of "utilization"**: The model's behavior is sensitive to how utilization is defined (consumption threshold, specificity). Too permissive → all agents survive; too restrictive → collapse.
- **Resource conservation**: Without resource regeneration or conservation, systems can collapse. Model must include resource dynamics.
- **Timescale separation**: Exploration and utilization must operate on compatible timescales; if exploration is too fast, no stable networks form.
- **Scalability**: Chain length and network complexity scale with agent count, but convergence time grows superlinearly.
- **Measuring "functional"**: The paper demonstrates that self-organization produces functional networks, but "functional" is defined relative to target states. In domains without clear targets, functional relevance must be operationalized differently.

## References

- Metzner, C., et al. (2026). Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems. arXiv:2606.26733
- Maturana, H. R. & Varela, F. J. (1980). Autopoiesis and Cognition.
- Kauffman, S. (1993). The Origins of Order: Self-Organization and Selection in Evolution.
- See also: [[autopoiesis-self-evolving-systems]], [[self-organising-transformer]], [[functional-whole-brain-models]]
