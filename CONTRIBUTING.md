# Contributing to AI Collection

Thank you for your interest in contributing to the AI Collection! This repository is a community-driven collection of OpenClaw agents and skills.

## Types of Contributions

We welcome contributions in the following areas:

### 1. Adding New Agents
- Create a new agent with a specific purpose
- Document its capabilities and usage
- Provide examples and configuration

### 2. Adding New Skills
- Create a skill that extends OpenClaw capabilities
- Write comprehensive SKILL.md documentation
- Include examples and reference materials

### 3. Improving Documentation
- Fix typos or clarify existing docs
- Add tutorials or guides
- Translate documentation to other languages

### 4. Bug Reports
- Report issues with existing agents or skills
- Suggest improvements or new features

### 5. Examples and Templates
- Add real-world usage examples
- Create new templates for common use cases

### 6. Plugin Marketplace Improvements
- Improve plugin discovery and documentation
- Suggest new plugin domains
- Enhance marketplace metadata in `_INDEX.json`
- Submit feedback on the marketplace experience

**Note:** New agents and skills are automatically included in the plugin marketplace after merging to main. See [Marketplace Documentation](./docs/marketplace/) for details.

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/ai_collection.git
cd ai_collection
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

### 3. Make Your Changes

Follow the [Agent Creation Guide](./docs/agents/creation-guide.md) or [Skill Creation Guide](./docs/skills/creation-guide.md).

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add new data-analysis agent"

# Or for fixes
git commit -m "fix: correct skill activation keywords"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Contribution Guidelines

### Agents

**What makes a good agent contribution:**

- ✅ Clear, specific purpose
- ✅ Well-documented system prompt
- ✅ Tested with multiple tasks
- ✅ Examples of usage
- ✅ Appropriate model selection
- ✅ Error handling strategies

**Agent Checklist:**

- [ ] Created directory in `collection/agents/agent-name/`
- [ ] Created `AGENT.md` with all required sections
- [ ] Added usage examples in `examples/`
- [ ] Tested agent with `sessions_spawn`
- [ ] Updated main `AGENTS.md` with entry
- [ ] Added references if needed

### Skills

**What makes a good skill contribution:**

- ✅ Specific, uncommon activation keywords
- ✅ Comprehensive, step-by-step instructions
- ✅ Error handling for common issues
- ✅ Multiple usage examples
- ✅ Reference documentation
- ✅ Tested with various prompts

**Skill Checklist:**

- [ ] Determined the appropriate category from the table below
- [ ] Created directory in `collection/skills/<category>/<skill-name>/`
- [ ] Created `SKILL.md` with all required sections
- [ ] Added usage examples in `examples/`
- [ ] Added reference docs in `references/` if needed
- [ ] Added helper scripts in `scripts/` if applicable
- [ ] Updated main `SKILLS.md` with entry
- [ ] Tested skill activation with trigger keywords

### Skill Categories

Skills are organized into **31 category subdirectories** under `collection/skills/`. Each new skill MUST be placed in the appropriate category directory, not in the root `collection/skills/` directory.

#### Category Directory Structure

```
collection/skills/
├── neuroscience/          # Brain networks, EEG, cognitive science, neuroimaging
├── quantum/               # Quantum computing, quantum ML, quantum sensing
├── spiking-neuromorphic/  # SNNs, neuromorphic computing, spike-based models
├── ai-ml/                  # General AI/ML topics not covered by a specific category
├── general-ml/            # General ML/DL concepts, training, optimization
├── nlp-llm/               # Language models, transformers, NLP tasks
├── multi-agent-rl/        # Multi-agent systems, reinforcement learning, robotics
├── signal-control-systems/ # Signal processing, control theory, time series
├── physics-math/          # Physics-informed ML, mathematical methods, complex systems
├── reasoning-bayesian/    # Bayesian inference, causal reasoning, uncertainty
├── vision-generative/     # Computer vision, generative models, GANs, diffusion
├── ai-safety-eval/        # AI safety, alignment, evaluation, benchmarks
├── security-privacy/      # Cryptography, privacy, adversarial ML, compliance
├── healthcare-bio/        # Medical AI, bioinformatics, drug discovery
├── finance/               # Financial data, stock analysis, quantitative methods
├── data-retrieval/        # Data pipelines, search, retrieval, RAG
├── deployment-optimization/ # MLOps, model serving, quantization, compression
├── software-engineering/  # Code generation, dev tools, testing, infrastructure
├── tools-frameworks/      # CLI tools, IDE integrations, workflow utilities
├── knowledge-graph/       # KG construction, graph neural networks, ontology
├── systems-engineering/   # System design, MBSE, requirements engineering
├── control-systems/       # Control theory, MPC, feedback systems
├── reinforcement-learning/ # RL-specific skills (algorithms, training)
├── agent-tools/           # Agent frameworks, agent utilities
├── math-statistics/       # Pure math, statistics, probability
├── medical/               # Clinical AI, medical imaging, diagnostics
├── memory/                # Memory systems, continual learning, forgetting
├── continual-learning/    # Continual/lifelong learning methods
├── skill-rag-indexer/     # Skill indexing, RAG for skills
├── chat-history-lancedb/  # Chat history storage, vector DB
├── other/                 # Uncategorized or cross-disciplinary skills
└── README.md              # Skills documentation
```

#### Category Selection Rules

1. **Never place skills in the root `collection/skills/` directory.** Always use a category subdirectory.
2. **Use `scripts/classify_skills.py` to auto-classify** if unsure:
   ```bash
   python scripts/classify_skills.py  # runs classification on all flat skills
   ```
   The script uses keyword matching on the skill name to determine the category.
3. **First match wins.** The classification rules are ordered by specificity. For cross-disciplinary skills (e.g., quantum + neuroscience), the first matching category in the rules list takes precedence.
4. **Priority order** (most specific to least specific):
   - `neuroscience` > `quantum` > `spiking-neuromorphic` > `nlp-llm` > `multi-agent-rl` > `signal-control-systems` > `general-ml` > `physics-math` > `ai-safety-eval` > `vision-generative` > `reasoning-bayesian` > `security-privacy` > `healthcare-bio` > `finance` > `data-retrieval` > `deployment-optimization` > `software-engineering` > `tools-frameworks` > `knowledge-graph` > `other`
5. **If no category matches**, place in `other/`.
6. **For automated/cron jobs**: always classify the skill by its name keywords before creating the directory. See the keyword rules in `scripts/classify_skills.py` `CLASSIFICATION_RULES` list.

#### Category Reference Table

| Category | For skills about... | Example keywords |
|----------|-------------------|-----------------|
| `neuroscience` | Brain networks, EEG, cognitive science, neuroimaging | brain, neural, neuro, eeg, fmri, bci, cortex, synapt |
| `quantum` | Quantum computing, quantum ML, quantum sensing | quantum, qubit, qec, qaoa, vqe, qml, qnn, entanglement |
| `spiking-neuromorphic` | SNNs, neuromorphic computing, spike-based models | spiking, snn, neuromorphic, stdp, spike, lif |
| `general-ml` | General ML/DL concepts, training, optimization | deep-learning, gradient, moe, distillation, pruning |
| `nlp-llm` | Language models, transformers, NLP tasks | llm, transformer, gpt, bert, nlp, prompt, rag |
| `multi-agent-rl` | Multi-agent systems, reinforcement learning | multi-agent, reinforcement, agent, agentic, ppo, grpo |
| `signal-control-systems` | Signal processing, control theory, time series | control, mpc, kalman, feedback, cps, cyber-physical |
| `physics-math` | Physics-informed ML, mathematical methods | physics, pde, topology, chaos, stochastic, tensor |
| `reasoning-bayesian` | Bayesian inference, causal reasoning, uncertainty | bayesian, causal, probabilistic, monte-carlo, mcmc |
| `vision-generative` | Computer vision, generative models | vision, image, video, gan, diffusion, segmentation |
| `ai-safety-eval` | AI safety, alignment, evaluation, benchmarks | ai-safety, alignment, benchmark, eval, jailbreak |
| `security-privacy` | Cryptography, privacy, adversarial ML | security, privacy, encryption, cryptography, backdoor |
| `healthcare-bio` | Medical AI, bioinformatics, drug discovery | healthcare, biomedical, clinical, drug, genomics |
| `finance` | Financial data, stock analysis, quantitative | finance, portfolio, stock, trading, market, akshare |
| `data-retrieval` | Data pipelines, search, retrieval, RAG | data-retrieval, search, database, embedding, rag |
| `deployment-optimization` | MLOps, model serving, quantization | deployment, serving, mlops, quantization, vllm |
| `software-engineering` | Code generation, dev tools, testing | software-engineering, testing, code-review, docker |
| `tools-frameworks` | CLI tools, IDE integrations, workflow | claude-code, opencode, copilot, chrome-extension |
| `knowledge-graph` | KG construction, graph neural networks | knowledge-graph, gnn, ontology, graph-neural |
| `systems-engineering` | System design, MBSE, requirements | systems-engineering, mbse, sysml, sheaf |
| `other` | Uncategorized or cross-disciplinary skills | (fallback) |

## Code Style

### Markdown

- Use consistent heading hierarchy
- Include code fences for code blocks
- Add alt text for images
- Keep lines under 100 characters

### Python/Script Files

- Follow PEP 8 style guide
- Use descriptive variable names
- Add docstrings to functions
- Include error handling

### Comments

- Explain "why", not "what"
- Keep comments concise
- Use `#` for single-line comments
- Use `"""` for multi-line docstrings

## Documentation Standards

### AGENT.md Must Include

```markdown
# Agent Name

## Purpose
[Clear description]

## Model
- Primary: [model]
- Alternative: [model]

## Tools
- [tool]: [usage]

## Skills
- [skill]: [description]

## System Prompt
```
[Detailed prompt]
```

## Activation
[How agent is activated]

## Usage Examples
[Examples]

## Configuration
[JSON config]

## Best Practices
[List]
```

### SKILL.md Must Include

```markdown
# Skill Name

## Description
[Brief description]

## Activation Keywords
- [keyword1]
- [keyword2]

## Tools Used
- [tool]: [usage]

## Installation
[If applicable]

## Usage Patterns
[Examples]

## Instructions for Agents
[Step-by-step]

## Error Handling
[Common errors]

## Examples
[Real-world examples]

## Resources
[Links]
```

## Testing

### Testing Agents

1. **Manual Testing:**
```python
# Test with simple task
sessions_spawn(task="test task", agentId="your-agent")

# Test with complex task
sessions_spawn(task="complex task with parameters", agentId="your-agent", thinking="high")
```

2. **Check:**
- Agent follows system prompt
- Appropriate tools are used
- Results are delivered correctly
- Errors are handled gracefully

### Testing Skills

1. **Trigger Testing:**
```
User: "[use trigger keyword]"
```
2. **Verify:**
- Agent reads SKILL.md
- Instructions are followed
- Tools are used correctly
- Common errors are handled

## Pull Request Process

### PR Title Format

- **New Agent:** `feat(agent): add new data-analysis agent`
- **New Skill:** `feat(skill): add new slack-integration skill`
- **Bug Fix:** `fix(agent): resolve timeout issue in research-agent`
- **Documentation:** `docs: update agent creation guide`
- **Refactoring:** `refactor(skills): improve error handling`

### PR Description

```markdown
## Description
[Brief description of changes]

## Changes
- [ ] Added new agent/skill
- [ ] Updated documentation
- [ ] Added examples
- [ ] Fixed bugs

## Testing
[Describe how you tested your changes]

## Screenshots (if applicable)
[Attach screenshots]

## Related Issues
Closes #123
```

## Review Process

1. **Automated Checks:**
   - CI/CD tests pass
   - No linting errors

2. **Manual Review:**
   - Code quality
   - Documentation completeness
   - Examples accuracy
   - Overall usefulness

3. **Approval:**
   - At least one maintainer approval
   - Address all review comments

## Community Guidelines

### Be Respectful

- Welcome new contributors
- Provide constructive feedback
- Acknowledge good work
- Help others learn

### Be Collaborative

- Discuss ideas openly
- Seek consensus on big changes
- Credit contributors
- Share knowledge

### Be Patient

- Review may take time
- Maintainers are volunteers
- Ask questions if unclear

## Getting Help

If you need help contributing:

1. **Check Documentation:**
   - [Agent Creation Guide](./docs/agents/creation-guide.md)
   - [Skill Creation Guide](./docs/skills/creation-guide.md)
   - Existing examples in `collection/`

2. **Open an Issue:**
   - Describe your question clearly
   - Include what you've tried
   - Reference existing agents/skills

3. **Join the Community:**
   - [OpenClaw Discord](https://discord.gg/clawd)
   - Open an issue labeled "question"

## Recognition

All contributors will be credited in:

- This CONTRIBUTING.md file
- Project README.md
- Individual agent/skill documentation

## License

By contributing, you agree that your contributions will be licensed under the same license as the repository (MIT).

---

Thank you for contributing! 🚀
