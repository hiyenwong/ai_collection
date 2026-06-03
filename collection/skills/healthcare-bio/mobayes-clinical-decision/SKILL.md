---
name: mobayes-clinical-decision
description: Modular Bayesian Framework (MoBayes) for separating reasoning from language in clinical decision support. Addresses the architectural limitation of LLMs conflating next-token prediction with probabilistic medical reasoning. Activation: clinical reasoning, medical LLM, Bayesian clinical, decision support, MoBayes, 临床决策.
---

# MoBayes: Modular Bayesian Clinical Decision Support

## Overview

MoBayes (arXiv:2604.20022) proposes a modular Bayesian framework that **separates language generation from clinical reasoning** in conversational healthcare systems. The core insight: LLMs conflate token prediction with probabilistic decision making, creating an architectural gap in clinical settings where accuracy matters more than fluency.

## Core Principles

### The Separation Problem

LLMs trained for conversational clinical support mix two distinct functions:
1. **Language generation** - producing fluent, contextually appropriate responses
2. **Probabilistic reasoning** - making accurate clinical inferences from symptoms and test data

This conflation means: (a) reasoning quality depends on language model training data, (b) fluent-sounding responses may mask poor reasoning, (c) no dedicated uncertainty quantification mechanism exists.

### MoBayes Architecture

```
User Query → [Language Module] → Clinical State → [Bayesian Reasoning Module] → [Language Module] → Response
```

- **Language Module**: LLM for interface — understanding queries, formatting outputs
- **Bayesian Reasoning Module**: Dedicated probabilistic model for clinical inference
  - Encodes medical knowledge as conditional probability distributions
  - Produces calibrated uncertainty estimates
  - Independent of language model training distribution

### Implementation Pattern

```python
class MoBayesClinical:
    def __init__(self, language_model, bayesian_network):
        self.llm = language_model
        self.bayes = bayesian_network
    
    def diagnose(self, patient_query):
        # Step 1: Extract clinical features via LLM
        features = self.llm.extract_clinical_features(patient_query)
        
        # Step 2: Reason via Bayesian network (separate from language)
        diagnosis, confidence, differential = self.bayes.infer(features)
        
        # Step 3: Generate response via LLM with reasoning results
        return self.llm.generate_response(diagnosis, confidence, differential)
```

### Key Advantages

1. **Calibrated uncertainty**: Bayesian module provides proper probability estimates, not token-level logits
2. **Knowledge updatability**: Medical knowledge can be updated without retraining the LLM
3. **Auditability**: Reasoning path is explicit and inspectable (vs. opaque LLM generation)
4. **Safety guarantees**: Hard constraints can be encoded in the Bayesian module
5. **Domain specialization**: Medical reasoning is decoupled from general language capabilities

## When to Use

- Clinical decision support systems using LLMs
- Medical triage chatbots requiring calibrated confidence
- Healthcare AI systems needing auditability
- Any domain where reasoning accuracy must be separated from language fluency

## Pitfalls

- LLM feature extraction must be validated against ground truth clinical annotations
- Bayesian network requires careful elicitation of conditional probabilities
- The interface between modules must handle uncertainty propagation correctly
- Not suitable for open-ended medical conversation without reasoning constraints

## Related Papers

- 2604.20022: MoBayes: A Modular Bayesian Framework for Separating Reasoning from Language in Conversational Clinical Decision Support
