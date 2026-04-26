---
name: causal-stance-physical-vs-intentional
description: "Philosophical framework distinguishing Physical Stance from Causal Stance in explaining behavior, reconstructing Davidson's anomalous monism for computational neuroscience and AI alignment. Activation triggers: causal stance, physical stance, intentional stance, anomalous monism, Davidson, philosophy of mind, explanation levels, mental causation."
---

# Causal Stance: Physical Stance vs Causal Stance

> Distinguishes the Physical Stance (mechanistic explanation via physical laws) from the Causal Stance (explanation via rationalizing mental states), reconstructing Davidson's anomalous monism to resolve tensions between mechanistic and intentional explanation in neuroscience and AI.

## Metadata
- **Source**: arXiv:2604.05004
- **Authors**: David Papineau
- **Published**: 2026-04-05
- **Categories**: q-bio.NC, philosophy of mind

## Core Methodology

### Key Innovation
Introduces a clear distinction between Dennett's "Physical Stance" and a newly articulated "Causal Stance" — the latter explains behavior through rationalizing mental states while remaining causally grounded. This framework reconstructs Davidson's anomalous monism, providing a principled basis for when intentional explanations (beliefs, desires) are appropriate versus when purely mechanistic explanations suffice.

### Technical Framework

1. **Three Stances of Explanation**:
   - **Physical Stance**: Predict behavior from physical laws and initial conditions (neuron-level, synapse-level)
   - **Causal Stance**: Explain behavior via causally efficacious mental states (beliefs, desires, intentions)
   - **Design Stance** (Dennett): Predict from functional design assumptions

2. **Davidson's Anomalous Monism Reconstructed**:
   - Mental events ARE physical events (token identity)
   - But mental types cannot be reduced to physical types (anomalism of the mental)
   - Rationalizing explanations (Causal Stance) are autonomous — not translatable to Physical Stance
   - The Causal Stance explains WHY an agent acts, the Physical Stance explains HOW the action physically occurs

3. **Implications for Neuroscience**:
   - Neural correlates are NOT explanations of mental phenomena
   - Both stances are legitimate and complementary, not competing
   - "Explanation gap" is conceptual, not empirical
   - Resolving the gap requires philosophical clarity, not more data

4. **Implications for AI**:
   - AI systems may warrant Causal Stance explanations when behavior is rationally interpretable
   - The question "does AI have real beliefs?" is reframed: does the Causal Stance provide genuine explanatory power?
   - AI alignment requires understanding which stance to adopt and when

## Implementation Guide

### Prerequisites
- Familiarity with philosophy of mind (Dennett, Davidson, Fodor)
- Background in computational neuroscience or cognitive science

### Conceptual Application Steps
1. Identify the target behavior to explain
2. Determine the appropriate explanatory stance:
   - Is the behavior predictable from physical mechanisms alone? → Physical Stance
   - Does rationalizing via mental states add explanatory power? → Causal Stance
3. Apply the chosen stance consistently
4. If both stances apply, ensure they do not contradict (anomalous monism constraint)

### Code Example
```python
from enum import Enum
from dataclasses import dataclass

class ExplanationStance(Enum):
    PHYSICAL = "physical"      # Mechanistic, law-based
    CAUSAL = "causal"          # Rationalizing, mental-state-based
    DESIGN = "design"          # Functional, purpose-based

@dataclass
class BehaviorExplanation:
    """Framework for applying explanatory stances to behavior."""
    target_behavior: str
    available_data: dict
    
    def determine_stance(self):
        """Determine which explanatory stance is appropriate."""
        has_mechanistic_data = "neural_activity" in self.available_data
        has_rational_structure = self._behavior_is_rationally_interpretable()
        
        if has_rational_structure and has_mechanistic_data:
            return [ExplanationStance.PHYSICAL, ExplanationStance.CAUSAL]
        elif has_mechanistic_data:
            return [ExplanationStance.PHYSICAL]
        elif has_rational_structure:
            return [ExplanationStance.CAUSAL]
        else:
            return [ExplanationStance.DESIGN]
    
    def _behavior_is_rationally_interpretable(self):
        """Check if behavior can be rationalized via beliefs/desires."""
        # Heuristic: behavior shows goal-directedness, context-sensitivity,
        # and consistency with attributed mental states
        return (
            self.available_data.get("goal_directed", False) and
            self.available_data.get("context_sensitive", False)
        )
    
    def explain_physical(self):
        """Physical stance explanation: mechanisms and laws."""
        if "neural_activity" not in self.available_data:
            return "Insufficient physical data for mechanistic explanation."
        return f"Behavior '{self.target_behavior}' explained by neural mechanisms."
    
    def explain_causal(self, beliefs=None, desires=None):
        """Causal stance explanation: rationalizing mental states."""
        if beliefs is None or desires is None:
            return "Mental states required for causal stance explanation."
        return (
            f"Agent performed '{self.target_behavior}' because they "
            f"believed {beliefs} and desired {desires}."
        )
```

## Applications
- **Computational neuroscience**: Clarifying when neural vs. cognitive explanations are appropriate
- **AI alignment**: Determining whether AI behavior warrants intentional interpretation
- **Philosophy of cognitive science**: Resolving mechanistic vs. functional explanation debates
- **Clinical neuroscience**: Bridging neurobiological and phenomenological descriptions of disorders
- **Brain-computer interfaces**: Understanding whether decoded neural states are mental states

## Key Findings
1. The Causal Stance is a legitimate autonomous mode of explanation, not a shorthand for Physical Stance
2. Davidson's anomalous monism correctly captures the relationship between mental and physical
3. Neural correlates do not reduce or replace intentional explanations
4. The explanation gap between neuroscience and psychology is conceptual, not empirical
5. AI systems may merit Causal Stance explanations without having "real" mental states

## Pitfalls
- The framework does not resolve the hard problem of consciousness
- Anomalous monism remains controversial in philosophy of mind
- Practical application to specific neural data is non-trivial
- The distinction may seem semantic but has deep implications for scientific methodology
- AI interpretation risks anthropomorphism — not all rationalizable behavior implies genuine mental states

## Related Skills
- neuro-symbolic-cognitive-architectures
- representation-use-usability-framework
- iit-critical-review
