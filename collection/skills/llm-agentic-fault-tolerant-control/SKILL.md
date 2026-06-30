---
name: llm-agentic-fault-tolerant-control
description: >
  Agentic Large Language Model framework for active Fault-Tolerant Control (FTC) 
  in cyber-physical systems. Combines multi-agent LLM workflow with Digital Process 
  Plant Twin and Graph RAG (CPSMod ontology) to transform fault detection outputs 
  into constraint-aware recovery actions. Suitable for industrial control systems, 
  process automation, and safety-critical applications.
tags: [fault-tolerant-control, llm-agents, cyber-physical-systems, graph-rag, digital-twin, process-control]
created: 2026-06-30
source: arXiv:2606.28011
---

# LLM Agentic Fault-Tolerant Control (FTC)

## Core Contribution

This paper presents an agentic LLM framework that transforms fault detection outputs into constraint-aware recovery actions for industrial control systems. The approach bridges the gap between fault detection and validated corrective action through a multi-agent workflow.

## Architecture Components

### 1. Multi-Agent Workflow
The framework decomposes operator duties into specialized agents:
- **Monitoring Agent**: Observes system state and fault signals
- **Planning Agent**: Generates recovery strategies
- **Action Synthesis Agent**: Creates specific control commands
- **Simulation Agent**: Tests actions in Digital Twin before execution
- **Validation Agent**: Verifies actions against safety constraints
- **Reprompting Agent**: Refines actions based on feedback

### 2. Digital Process Plant Twin (DPPT)
Exposes plant capabilities through:
- Real-time plant data access
- Process models for simulation
- Simulation service for pre-execution testing
- Interlock and envelope validation

### 3. Graph RAG Layer (CPSMod Ontology)
Organizes plant knowledge into a graph structure:
- **Structure**: Physical components and relationships
- **Function**: Process functions and dependencies
- **Hybrid Dynamics**: Continuous/discrete state transitions
- **Control Context**: Operating modes and constraints
- **Fault Semantics**: Fault types and propagation paths

Supports relation-aware, multi-hop retrieval for agents.

## Recovery Action Generation

### Action Types
1. **State-machine recovery paths**: Minimal-risk sequences of state transitions
2. **Discrete commands**: Valve operations, mode switches, equipment activation
3. **Continuous setpoint adaptations**: Adjusted control targets

### Validation Pipeline
Before any actuation:
- **Interlock check**: Verify physical safety constraints
- **Envelope validation**: Ensure within operational limits
- **Dynamic feasibility**: Confirm temporal and rate constraints
- **Fallback trigger**: If no valid plan found, hand over to safety system

## Implementation Pattern

```python
# Simplified workflow
class FTCFramework:
    def __init__(self, dppt, graph_rag, llm_agents):
        self.dppt = dppt
        self.graph_rag = graph_rag
        self.agents = llm_agents
        
    def handle_fault(self, fault_signal):
        # 1. Monitor and diagnose
        diagnosis = self.agents.monitor(fault_signal)
        
        # 2. Plan recovery strategy
        strategy = self.agents.plan(diagnosis, self.graph_rag.query())
        
        # 3. Synthesize specific actions
        actions = self.agents.synthesize(strategy, self.dppt.get_constraints())
        
        # 4. Simulate and validate
        for action in actions:
            if self.dppt.simulate(action).is_safe():
                return action
        
        # 5. Fallback if no valid action
        return self.agents.fallback(diagnosis)
```

## Performance Characteristics

- **Latency**: Compatible with process dynamics (batch: minutes, continuous: seconds)
- **LLM Models**: Tested with lightweight models (GPT-4o-mini, GPT-4.1-mini)
- **Validation**: Deterministic constraint checking ensures safety
- **Applicability**: Both discrete (batch) and continuous (CSTR) processes

## Use Cases

1. **Chemical Process Control**: Reactor temperature/pressure fault recovery
2. **Batch Manufacturing**: Mixing module fault handling
3. **Power Systems**: Grid fault detection and reconfiguration
4. **Manufacturing**: Production line fault recovery
5. **Building Automation**: HVAC system fault management

## Integration Requirements

- **Graph Database**: For CPSMod ontology storage and querying
- **Digital Twin Platform**: Real-time simulation capability
- **LLM API**: For agent reasoning and decision making
- **Control System Interface**: For reading state and executing actions
- **Safety System**: For fallback and emergency shutdown

## Limitations and Considerations

- Requires comprehensive plant knowledge in CPSMod ontology
- LLM latency must be compatible with process dynamics
- Digital Twin accuracy affects validation reliability
- Graph RAG quality depends on ontology completeness
- Safety fallback must be independent of LLM decisions

## References

- Paper: arXiv:2606.28011v1
- Authors: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- Published: 2026-06-26
- Categories: eess.SY, cs.LG
