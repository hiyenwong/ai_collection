# Prompt Engineer Agent

A senior prompt engineer specialized in designing, optimizing, and evaluating prompts for AI systems. Expert in advanced prompting techniques including Chain-of-Thought (CoT), Tree-of-Thought (ToT), Few-shot learning, and systematic prompt optimization.

## Capabilities

- **Prompt Design**: Clear instructions, role definition, output formatting
- **Advanced Techniques**: CoT, ToT, Few-shot, Self-consistency
- **Optimization**: A/B testing, iterative refinement, template engineering
- **Evaluation**: Human and automated evaluation, quality metrics
- **Domain-Specific**: Code generation, reasoning, creative writing, data analysis

## Quick Start

Spawn the prompt engineer agent:
```python
sessions_spawn(
    task="Optimize this prompt for code generation tasks",
    agentId="prompt-engineer",
    model="claude-opus-4.5"
)
```

## Example Tasks

- Design prompts for specific tasks
- Optimize existing prompts
- Create prompt templates
- Evaluate prompt performance
- Apply advanced techniques (CoT, ToT, Few-shot)
- Debug prompt issues
- Create test suites for prompts

## Files

- `AGENT.md` - Agent configuration and documentation
- `soul.md` - Agent identity and values
- `prompt-engineer.agent.md` - Agent specification
- `prompt-engineer.agent.yaml` - Agent configuration

## Model

- **Primary:** claude-opus-4.5
- **Alternative:** claude-sonnet-4.5
- **Fallback:** claude-haiku-4.5

## ArXiv Classification

**cs.CL** - Computation and Language

## Author

- Created by: Hi Yen
- Created: 2026-03-10

## License

MIT