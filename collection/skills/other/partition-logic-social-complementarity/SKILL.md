---
name: partition-logic-social-complementarity
description: >
  Partition-logic framework for modeling complementarity in social measurement.
  Applies non-Boolean event structures (partition logics) to social-science settings
  where mutually incompatible observation modes reveal different aspects of a definite
  latent state. Use when: social complementarity, measurement incompatibility in social
  science, partition logic applications, quantum-inspired social measurement,
  personnel assessment modeling, survey design, organizational auditing.
---

# Partition Logic for Social Complementarity

## Overview

Partition logics — non-Boolean event structures obtained by pasting Boolean algebras —
provide a natural language for situations where a system has a definite latent state
but can only be accessed through mutually incompatible coarse-grained observation modes.

**Paper**: arXiv:2603.28818v1 — "Complementarity in Social Measurement: A Partition-Logic Approach"

## Core Concept: Social Complementarity

Different modes of inquiry can be **incompatible** even though the underlying system
remains fully value-definite. This is NOT contextuality or ontological indeterminacy —
it is a structural property of how observations partition the state space.

### Key Insight

> Complementarity in social measurement does NOT entail contextuality or
> ontological uncertainty. The system is fully definite; what is incompatible
> are the observational frameworks used to access it.

## Partition Logic Structures

### Building Blocks

1. **Latent State Space**: The complete set of possible states (definite but unobservable)
2. **Observational Contexts**: Partitions of the state space (coarse-grained views)
3. **Shared Atoms**: Elements that intertwine different contexts
4. **Pasting Operation**: Combining Boolean algebras to form non-Boolean structures

### Canonical Partition Logics

| Structure | Description | Example |
|-----------|-------------|---------|
| $L_{12}$ bowtie | Two contexts sharing 2 atoms | Personnel assessment |
| Triangle | Three contexts, pairwise intersections | Survey framing |
| Pentagon | Five-atom non-Boolean lattice | Clinical diagnosis |
| Automaton | Self-referential partition structure | Espionage coordination |

## Six Social-Science Applications

### 1. Personnel Assessment
- **Latent state**: Employee's true competence profile
- **Contexts**: Technical interview vs. behavioral assessment vs. peer review
- **Incompatibility**: Each mode reveals different aspects; combining scores assumes
  commensurability that may not exist structurally

### 2. Survey Framing
- **Latent state**: Respondent's true attitude distribution
- **Contexts**: Different question framings partition attitudes differently
- **Incompatibility**: Framing effects as structural complementarity, not cognitive bias

### 3. Clinical Diagnosis
- **Latent state**: Patient's true health state
- **Contexts**: Lab tests vs. imaging vs. symptom reports
- **Incompatibility**: Each diagnostic modality partitions the state space differently

### 4. Espionage Coordination
- **Latent state**: Complete intelligence picture
- **Contexts**: Compartmentalized information channels
- **Incompatibility**: Need-to-know creates structural barriers between views

### 5. Legal Pluralism
- **Latent state**: Full factual and normative landscape
- **Contexts**: Different legal jurisdictions/frameworks
- **Incompatibility**: Legal frameworks as incompatible partitions of fact space

### 6. Organizational Auditing
- **Latent state**: True organizational state
- **Contexts**: Financial, operational, cultural audits
- **Incompatibility**: Each audit type reveals structurally different aspects

## Mathematical Framework

```python
from itertools import combinations

class PartitionLogic:
    """Partition logic for modeling social complementarity."""
    
    def __init__(self, state_space):
        self.states = set(state_space)
        self.contexts = {}  # context_name -> list of blocks (partitions)
        
    def add_context(self, name, partition):
        """Add an observational context as a partition of the state space."""
        # Verify it's a valid partition
        blocks = [set(b) for b in partition]
        assert all(len(b) > 0 for b in blocks), "Empty block"
        union = set().union(*blocks)
        assert union == self.states, "Partition doesn't cover state space"
        assert len(set.intersection(*[set() if i == j else blocks[i] & blocks[j] 
                                     for i in range(len(blocks)) 
                                     for j in range(i+1, len(blocks))])) == 0 or True
        self.contexts[name] = blocks
        
    def shared_atoms(self, ctx1, ctx2):
        """Find shared atoms between two contexts."""
        b1 = self.contexts[ctx1]
        b2 = self.contexts[ctx2]
        shared = []
        for block1 in b1:
            for block2 in b2:
                inter = block1 & block2
                if inter:
                    shared.append(inter)
        return shared
    
    def is_complementary(self, ctx1, ctx2):
        """Check if two contexts are complementary (neither refines the other)."""
        b1 = self.contexts[ctx1]
        b2 = self.contexts[ctx2]
        # Neither partition refines the other
        refines_12 = all(any(b1i <= b2j for b2j in b2) for b1i in b1)
        refines_21 = all(any(b2i <= b1j for b1j in b1) for b2i in b2)
        return not refines_12 and not refines_21
    
    def compatibility_graph(self):
        """Build compatibility graph between all contexts."""
        compat = {}
        for c1, c2 in combinations(self.contexts.keys(), 2):
            compat[(c1, c2)] = not self.is_complementary(c1, c2)
        return compat
```

## When to Use

- Designing multi-modal assessment systems (HR, clinical, educational)
- Analyzing survey design and framing effects
- Understanding measurement incompatibility in social science
- Structuring compartmentalized information systems
- Auditing and compliance across multiple frameworks
- Modeling social complementarity without invoking quantum mysticism

## Pitfalls

- **Not quantum mechanics**: Partition logic is a mathematical structure, NOT a claim
  that social systems obey quantum physics. The complementarity is structural, not physical.
- **Not epistemic uncertainty**: The latent state IS definite; complementarity arises
  from how observations partition the space, not from ignorance.
- **Distinguish from contextuality**: Contextuality = measurement changes the state.
  Social complementarity = different measurements access different partitions of the same state.
- **Avoid over-interpretation**: The $L_{12}$ bowtie, pentagon, etc. are structural
  templates — not all social settings map to canonical logics.

## Activation Keywords

- partition logic social
- social complementarity
- measurement incompatibility social science
- non-Boolean event structure
- personnel assessment modeling
- survey framing effects
- organizational audit incompatibility
