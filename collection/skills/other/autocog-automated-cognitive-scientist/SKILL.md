---
name: autocog-automated-cognitive-scientist
description: |
  Paper analysis: AutoCog — an automated LLM-driven system for discovering cognitive theories. The system takes existing theories as seeds, generates novel hypotheses, tests them against data, and produces executable cognitive models. Validated with human participants showing superior performance over established theories. Source: arXiv:2606.26693 (q-bio.NC, cs.AI), 2026-06-24.
  Activation keywords: AutoCog, automated theory discovery, cognitive science, LLM-driven science, computational cognition, hypothesis generation, multi-cue decision-making, active inference, cognitive modeling, automated scientist, theory building, experimental psychology, decision theory, cognitive theory, machine discovery
date_added: 2026-06-29
arxiv_id: "2606.26693"
authors:
  - Akshay K. Jagadish
  - Younes Strittmatter
  - Nori Jacoby
  - George Kachergis
  - Eric Schulz
  - Nathaniel Daw
  - Suyog H. Chandramouli
  - Thomas L. Griffiths
---

# AutoCog: An Automated System for Discovering Cognitive Theories

## Paper Metadata
- **arXiv ID**: 2606.26693
- **Published**: 2026-06-24
- **Categories**: q-bio.NC, cs.AI
- **Comment**: 44 pages, 9 figures
- **Authors**: Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, George Kachergis, Eric Schulz, Nathaniel Daw, Suyog H. Chandramouli, Thomas L. Griffiths

## Abstract
AutoCog is a fully automated discovery system that leverages large language models to generate, refine, and test cognitive theories. Starting from established theories as seeds, the system proposes novel hypotheses, designs experiments to test them, and iteratively refines the theories based on experimental outcomes. When validated with human participants, AutoCog produced theories that outperformed the established theories it was seeded with and generalized to held-out studies across two different experimental settings. Notably, it surfaced a novel theory of multi-cue decision-making in which choices show diminishing sensitivity to feature values — a prediction confirmed in a preregistered study with new participants. The system demonstrates how automated discovery can transform cognitive theory-building into an explicit, executable, and cumulative science.

## Methodology

### Core Architecture
1. **Theory Representation**: Cognitive theories encoded as executable generative models
2. **Hypothesis Generation**: LLM-driven proposal of novel modifications to seed theories
3. **Automated Experimentation**: System designs and runs experiments on human participants
4. **Iterative Refinement**: Theories updated based on experimental data and model comparison

### Key Components
- **Seed theories**: Established cognitive theories serve as starting points
- **LLM as theorist**: GPT-class models propose theory modifications and experimental designs
- **Data-driven validation**: Theories evaluated against real experimental data
- **Cumulative refinement**: Each cycle produces improved theories grounded in evidence

### Experimental Design
- Theories tested on human participants via online platforms
- Compared against the seed theories they were derived from
- Generalization tested on held-out experimental datasets
- Preregistered confirmation study for the novel multi-cue theory

## Key Findings

1. **Superior performance**: AutoCog-generated theories outperformed established theories they were seeded from
2. **Generalization**: Theories transferred across different experimental settings
3. **Novel discovery**: Emergent multi-cue decision-making theory with diminishing sensitivity to feature values
4. **Data-driven**: Discoveries driven by data rather than LM priors alone
5. **Preregistered validation**: Novel predictions confirmed in independent sample

## Implications

### For Cognitive Science
- Transforms theory-building from artisanal to systematic science
- Enables cumulative, executable theory development
- Bridges computational modeling and experimental psychology

### For AI/ML
- Demonstrates LLMs as scientific discovery engines
- Shows value of data-grounded iterative refinement over pure generation
- Suggests framework for automated theory discovery in other domains

### For Neuroscience
- Potential application to neural mechanism discovery
- Framework for testing computational theories of brain function
- Could accelerate development of cognitive architectures

## Critical Analysis

### Strengths
- End-to-end automation from hypothesis to validation
- Rigorous preregistered confirmation
- Theories outperform human-crafted baselines
- Generalization across experimental contexts

### Limitations
- Relies on quality of seed theories
- LLM may amplify biases in training data
- Requires substantial human participant infrastructure
- Theory space may be constrained by representational format

## Connections
- [[computational-neuroscience-in-llm-era]] - related work on LLMs in neuroscience
- [[autocog-automated-cognitive-scientist]] - this paper
- [[research-paper-pattern-extractor]] - pattern extraction from research
- [[research-skill-extractor]] - skill extraction from papers
