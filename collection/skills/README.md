# Skills Collection

Automated skills collection from arXiv research and curated sources.

**Last Updated:** 2026-06-03

## Directory Structure

Skills are organized by topic into category subdirectories:

```
collection/skills/
├── agent-tools/              # Agent frameworks, CLI tools, dev utilities
├── ai-safety-eval/           # AI safety, alignment, evaluation, benchmarks
├── data-retrieval/           # Data pipelines, search, retrieval, RAG
├── deployment-optimization/  # MLOps, model serving, quantization, compression
├── general-ml/               # General ML/DL concepts, training, optimization
├── healthcare-bio/           # Medical AI, bioinformatics, drug discovery
├── knowledge-graph/          # KG construction, graph neural networks, ontology
├── multi-agent-rl/           # Multi-agent systems, reinforcement learning, robotics
├── neuroscience/             # Brain networks, EEG, cognitive science, neuroimaging
├── nlp-llm/                  # Language models, transformers, NLP tasks
├── other/                    # Uncategorized skills
├── physics-math/             # Physics-informed ML, mathematical methods, complex systems
├── quantum/                  # Quantum computing, quantum ML, quantum sensing
├── reasoning-bayesian/       # Bayesian inference, causal reasoning, uncertainty
├── security-privacy/        # Cryptography, privacy, adversarial ML, compliance
├── signal-control-systems/  # Signal processing, control theory, time series, MPC
├── software-engineering/     # Code generation, dev tools, testing, infrastructure
├── spiking-neuromorphic/     # SNNs, neuromorphic computing, spike-based models
├── vision-generative/        # Computer vision, generative models, GANs, diffusion
├── README.md                 # This file
└── SKILL.md                  # Skill specification
```

## Category Overview

| Category | Count | Description |
|----------|-------|-------------|
| `neuroscience` | ~700 | Brain networks, EEG/MEG, cognitive science, neuroimaging, connectomics |
| `quantum` | ~815 | Quantum computing, quantum ML, quantum sensing, QEC, quantum control |
| `spiking-neuromorphic` | ~300 | Spiking neural networks, neuromorphic hardware, event-driven computing |
| `nlp-llm` | ~130 | Language models, transformers, NLP tasks, retrieval-augmented generation |
| `multi-agent-rl` | ~120 | Multi-agent systems, reinforcement learning, robotics, game theory |
| `signal-control-systems` | ~119 | Signal processing, control theory, MPC, time series, dynamical systems |
| `general-ml` | ~90 | General ML/DL, training methods, representation learning, optimization |
| `other` | ~890 | Uncategorized or cross-disciplinary skills |
| `reasoning-bayesian` | ~57 | Bayesian inference, causal reasoning, uncertainty quantification |
| `ai-safety-eval` | ~33 | AI safety, alignment, evaluation, benchmarks, fairness |
| `software-engineering` | ~23 | Code tools, dev ops, testing, infrastructure |
| `physics-math` | ~47 | Physics-informed ML, mathematical methods, complex systems |
| `vision-generative` | ~37 | Computer vision, generative models, GANs, diffusion models |
| `healthcare-bio` | ~24 | Medical AI, bioinformatics, drug discovery, clinical NLP |
| `agent-tools` | ~20 | Agent frameworks, CLI tools, workflow utilities |
| `data-retrieval` | ~22 | Data pipelines, search engines, RAG, recommendation systems |
| `deployment-optimization` | ~11 | MLOps, model serving, quantization, edge deployment |
| `security-privacy` | ~11 | Cryptography, privacy-preserving ML, adversarial robustness |
| `knowledge-graph` | ~11 | Knowledge graphs, GNNs, ontology, entity linking |

## How Skills Are Created

Most skills are automatically generated from arXiv papers via the `arxiv-to-skill-research-workflow`. Each skill typically contains:

- `SKILL.md` — Skill definition with instructions, background, and references
- Supporting files (scripts, references, assets)

## Contributing New Skills

When adding a new skill:

1. Determine the appropriate category from the table above
2. Create the skill directory inside that category: `collection/skills/<category>/<skill-name>/`
3. Copy the template from `templates/skill-template.md` and fill in all sections
4. If the skill spans multiple categories, place it in the most specific one (e.g., `quantum` over `other` for quantum-brain topics)

## Browsing on GitHub

Each category directory contains fewer than 1,000 entries, so GitHub can display the full listing without truncation. Use the category that best matches your interest to browse skills.
