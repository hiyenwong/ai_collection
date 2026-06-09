# Skills Collection

Automated skills collection from arXiv research and curated sources.

**Last Updated:** 2026-06-08

## Directory Structure

Skills are organized by topic into 31 category subdirectories.
Each category contains fewer than 1,000 entries, so GitHub displays full listings without truncation.

```
collection/skills/
├── agent-tools/              # Agent frameworks, CLI tools, dev utilities
├── ai-ml/                    # AI/ML agent systems, multi-agent architectures
├── ai-safety-eval/           # AI safety, alignment, evaluation, benchmarks
├── continual-learning/       # Continual/lifelong learning, catastrophic forgetting
├── control-systems/          # Control theory, dynamical systems, optimal control
├── data-retrieval/           # Data pipelines, search, retrieval, RAG
├── deployment-optimization/  # MLOps, model serving, quantization, compression
├── finance/                  # Financial ML, portfolio optimization, trading
├── general-ml/               # General ML/DL, training methods, optimization
├── healthcare-bio/           # Medical AI, bioinformatics, drug discovery
├── knowledge-graph/          # KG construction, graph neural networks, ontology
├── math-statistics/          # Mathematical statistics, probability theory
├── medical/                  # Medical diagnosis, clinical AI, health analytics
├── memory/                   # Memory systems, retrieval, working memory
├── multi-agent-rl/           # Multi-agent systems, reinforcement learning
├── neuroscience/             # Brain networks, EEG, cognitive science, neuroimaging
├── nlp-llm/                  # Language models, transformers, NLP tasks
├── other/                    # Uncategorized or cross-disciplinary skills
├── physics-math/             # Physics-informed ML, mathematical methods
├── quantum/                  # Quantum computing, quantum ML, quantum sensing
├── reasoning-bayesian/       # Bayesian inference, causal reasoning, uncertainty
├── reinforcement-learning/   # RL algorithms, policy optimization, reward modeling
├── security-privacy/         # Cryptography, privacy, adversarial ML, compliance
├── signal-control-systems/  # Signal processing, control theory, time series
├── software-engineering/     # Code generation, dev tools, testing, infrastructure
├── spiking-neuromorphic/     # SNNs, neuromorphic computing, spike-based models
├── systems-engineering/      # Systems engineering, CPS, resilience
├── tools-frameworks/         # Development tools, framework-specific skills
├── vision-generative/        # Computer vision, generative models, GANs, diffusion
├── README.md                 # This file
└── SKILL.md                  # Skill specification
```

## Category Overview

| Category | Count | Description |
|----------|-------|-------------|
| `neuroscience` | 688 | Brain networks, EEG/MEG, cognitive science, neuroimaging, connectomics |
| `quantum` | 461 | Quantum computing, quantum ML, quantum sensing, QEC, quantum control |
| `spiking-neuromorphic` | 324 | Spiking neural networks, neuromorphic hardware, event-driven computing |
| `ai-ml` | 224 | AI/ML agent systems, architectures, and frameworks |
| `other` | 205 | Uncategorized or cross-disciplinary skills |
| `nlp-llm` | 142 | Language models, transformers, NLP tasks, retrieval-augmented generation |
| `multi-agent-rl` | 130 | Multi-agent systems, reinforcement learning, robotics, game theory |
| `signal-control-systems` | 129 | Signal processing, control theory, MPC, time series, dynamical systems |
| `general-ml` | 108 | General ML/DL, training methods, representation learning, optimization |
| `reasoning-bayesian` | 68 | Bayesian inference, causal reasoning, uncertainty quantification |
| `systems-engineering` | 67 | Systems engineering, cyber-physical systems, resilience |
| `reinforcement-learning` | 62 | RL algorithms, policy optimization, reward modeling |
| `physics-math` | 57 | Physics-informed ML, mathematical methods, complex systems |
| `vision-generative` | 48 | Computer vision, generative models, GANs, diffusion models |
| `control-systems` | 38 | Control theory, dynamical systems, optimal control |
| `ai-safety-eval` | 34 | AI safety, alignment, evaluation, benchmarks, fairness |
| `data-retrieval` | 34 | Data pipelines, search engines, RAG, recommendation systems |
| `software-engineering` | 31 | Code generation, dev tools, testing, infrastructure |
| `agent-tools` | 25 | Agent frameworks, CLI tools, workflow utilities |
| `tools-frameworks` | 25 | Development tools, framework-specific skills |
| `healthcare-bio` | 24 | Medical AI, bioinformatics, drug discovery, clinical NLP |
| `knowledge-graph` | 21 | Knowledge graphs, GNNs, ontology, entity linking |
| `math-statistics` | 18 | Mathematical statistics, probability theory |
| `security-privacy` | 16 | Cryptography, privacy-preserving ML, adversarial robustness |
| `finance` | 15 | Financial ML, portfolio optimization, trading, economics |
| `deployment-optimization` | 13 | MLOps, model serving, quantization, edge deployment |
| `medical` | 10 | Medical diagnosis, clinical AI, health analytics |
| `memory` | 6 | Memory systems, retrieval, working memory |
| `continual-learning` | 5 | Continual/lifelong learning, catastrophic forgetting |
| `chat-history-lancedb` | 4 | Chat history and conversation storage |
| `skill-rag-indexer` | 3 | Skill RAG indexing and retrieval |

**Total: 3,035 skills across 31 categories.**

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
