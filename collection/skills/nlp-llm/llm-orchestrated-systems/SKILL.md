---
name: llm-orchestrated-systems
description: "LLM-powered orchestration for complex engineering systems using Model Context Protocol (MCP). Enables natural language interaction with specialized engineering workflows including power grid simulation, quantum system management, and industrial control systems. Use when: (1) building LLM orchestrators for engineering tools, (2) integrating MCP with simulation software, (3) democratizing access to complex analysis workflows, (4) creating natural language interfaces for control systems, (5) automating multi-tool engineering pipelines. Activation: LLM orchestrator, MCP engineering, natural language simulation, automated engineering workflow, engineering tool orchestration, LLM grid simulation, 大语言模型编排, 工程系统编排"
---

# LLM-Orchestrated Engineering Systems

Design LLM-powered orchestration frameworks for complex engineering systems using the Model Context Protocol (MCP).

## Architecture Pattern (arXiv:2605.12728)

### Grid-Orch Framework Pattern

The Grid-Orch framework demonstrates how to bridge LLMs and specialized engineering tools:

```
Natural Language → LLM Orchestrator → MCP Server → Engineering Simulator → Results
         ↑                                                              ↓
         └───────────── Validation & Explanation ←───────────────────────┘
```

### Key Components

1. **LLM Orchestrator**: Decomposes user intent into tool-specific commands
2. **MCP Server Layer**: Standardized interface to engineering tools
3. **Domain Simulator**: Specialized computation engine (power grid, quantum system, etc.)
4. **Validation Layer**: Ensures simulation results are physically meaningful
5. **Explanation Generator**: Translates technical results into user-friendly reports

## Implementation Pattern

### Step 1: Define MCP Tools

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Engineering Orchestrator")

@mcp.tool()
async def run_power_flow(bus_data: str, line_data: str) -> dict:
    """Run power flow analysis on distribution grid."""
    # Call specialized simulator
    result = run_grid_simulation(bus_data, line_data)
    return validate_and_format(result)

@mcp.tool()
async def optimize_dispatch(load_forecast: str, gen_data: str) -> dict:
    """Optimize generator dispatch given load forecast."""
    result = run_optimization(load_forecast, gen_data)
    return result
```

### Step 2: LLM Prompt Design

```
You are an engineering system orchestrator. The user has requested: {user_query}

Available tools:
- run_power_flow: Analyze electrical grid power flow
- optimize_dispatch: Optimize generator scheduling
- check_constraints: Verify operational limits

Steps:
1. Parse the user query to identify parameters
2. Select appropriate tools and sequence
3. Execute with proper error handling
4. Validate results against physical constraints
5. Generate explanation for the user
```

### Step 3: Validation Layer

Critical for engineering systems — LLMs cannot guarantee physical correctness:

```python
def validate_power_flow(result: dict) -> tuple[bool, str]:
    """Validate power flow results against physical constraints."""
    checks = [
        check_voltage_limits(result.buses),
        check_thermal_limits(result.lines),
        check_power_balance(result),
    ]
    passed = all(c[0] for c in checks)
    message = "; ".join(c[1] for c in checks if not c[0])
    return passed, message
```

## Design Principles

1. **Separation of Concerns**: LLM handles intent parsing and orchestration; simulators handle computation
2. **Validation Gate**: Every simulation result must pass physical validation before being returned
3. **Error Recovery**: LLM should interpret error messages and suggest corrections
4. **Explainability**: Results must be accompanied by human-readable explanations
5. **Auditability**: All orchestration decisions should be logged for review

## Application Domains

| Domain | Simulation Tool | MCP Tool | Validation |
|--------|----------------|----------|------------|
| Power Grid | GridLAB-D, OpenDSS | run_power_flow | Voltage, thermal limits |
| Quantum Systems | Qiskit, Cirq | run_quantum_circuit | Fidelity, error rates |
| Chemical Process | ASPEN, DWSIM | run_process_sim | Mass/energy balance |
| Structural FEA | FEniCS, Abaqus | run_structural_analysis | Stress limits |

## Pitfalls

- **Hallucination in Parameters**: LLM may generate invalid simulation parameters; always validate inputs
- **Domain Gap**: LLM doesn't understand physics; delegate all computation to simulators
- **Tool Selection Errors**: LLM may pick wrong tools; provide clear tool descriptions
- **Result Misinterpretation**: LLM may misread simulation output; use structured result formats
- **Security**: MCP servers should not expose arbitrary code execution; sandbox simulators

## Related Skills

- `mcp` - Model Context Protocol configuration
- `quantum-control-systems` - Quantum system design
- `spec-driven-agent-architecture` - Workflow patterns for AI agents
