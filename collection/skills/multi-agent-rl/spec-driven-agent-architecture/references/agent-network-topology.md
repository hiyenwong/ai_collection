# Agent Network Topology Details

## Four-Agent Pipeline Architecture

The Super Factory agent network consists of 4 agents arranged in a directed acyclic graph with feedback loops.

### Node Details

| Agent | Tier | Model | Tools | Escalation Threshold |
|-------|------|-------|-------|---------------------|
| Research | 1 | claude-haiku-4-5 | web_search, file_read, github_search | 3 empty searches / all-low confidence / scope gap |
| Planning | 2 | claude-sonnet-4-6 | file_read | Insufficient research / ambiguous vision / missing deps |
| Build | 3 | claude-sonnet-4-6 | file_read, file_write, shell_exec, test_runner | 3 contract failures / dep install fail / out-of-scope |
| Eval | 4 | claude-sonnet-4-6 | file_read | Missing spec / unparseable output / score delta > 0.3 |

### Data Flow

1. **Research → Planning**: findings, sources, confidence ratings
2. **Research → Build** (indirect): context sources for implementation
3. **Planning → Build**: task plans with phases, deliverables, dependencies
4. **Planning → Eval**: task specs become eval criteria
5. **Build → Eval**: code output for validation
6. **Research → Eval** (indirect): sources for fact-checking
7. **Eval → Planning/Build** (feedback): retry signal on failure

### Topology Generation

From spec files in `specs/agents/*.yaml`, the network can be reconstructed by:
1. Parsing each YAML spec to extract role, tools, escalation_conditions
2. Building dependency graph from context_sources and pipeline definitions
3. Rendering as HTML/SVG or using Codex for runtime visualization

### Current Status (2026-05-06)

- Specs: ~80% complete (4 agents defined)
- Contracts: ~80% complete (4 contracts + shared.py)
- Eval engine: ~90% complete
- Knowledge: ~85% complete
- Orchestrator: ~75% complete
- Agent implementations: 0% (placeholder)
- Memory/Pipelines/Tools/Outputs: 0-10%
