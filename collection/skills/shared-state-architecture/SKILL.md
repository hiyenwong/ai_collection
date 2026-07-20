---
name: shared-state-architecture
description: "PSI (Persistent Shared Interface): A shared-state architecture for coherent AI-generated instruments in personal AI agents. Addresses the problem of isolated AI tools by introducing a personal-context bus for cross-module reasoning and synchronized actions. Use when designing multi-agent systems, personal AI environments, tool orchestration, or building coherent AI software architectures."
---

# PSI: Shared State Architecture for Personal AI Agents

## Core Problem

AI-generated personal tools remain isolated after creation, lacking coordination mechanisms. Each tool operates independently without shared context, leading to fragmented user experiences.

## Key Innovation: Personal-Context Bus

PSI introduces a **shared-state layer** that transforms isolated AI modules into coherent instruments through:

1. **State Publication**: Modules publish current state to shared bus
2. **Write-back Affordances**: Modules expose editable state properties
3. **Cross-module Reasoning**: Chat agent can reason across module states
4. **Synchronized Actions**: Multiple modules can coordinate through shared state

## Architecture Components

### 1. Personal-Context Bus
- Central communication channel
- Publish/subscribe pattern for state updates
- Supports both read and write operations

### 2. State Contract
```python
class ModuleState:
    # Required properties
    module_id: str
    state_type: str
    current_state: dict
    writeable_properties: list[str]
    
    # Methods
    def publish_state() -> None
    def subscribe_to_state(module_id: str) -> None
    def write_state(property: str, value: Any) -> bool
```

### 3. Integration Pattern
- New modules automatically inherit shared-state contract
- Existing modules can be wrapped with state adapters
- Chat agent accesses all module states uniformly

## Design Principles

1. **Persistence**: State survives across sessions
2. **Coherence**: All modules see consistent view
3. **Chat-complementary**: Both GUI and chat interfaces work
4. **Automatic integration**: New tools join ecosystem seamlessly

## Use Cases

- Personal AI assistants with multiple tools
- Cross-tool workflow automation
- State-aware AI agents
- Multi-modal personal computing environments

## Implementation Considerations

- State conflict resolution (CRDTs, versioning)
- Privacy boundaries between modules
- Performance under high update frequency
- Backward compatibility with existing tools

## Paper Reference

**Title**: PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents
**Authors**: Zhiyuan Wang, Erzhen Hu, Mark Rucker, Laura E. Barnes
**arXiv**: 2604.08529
**Category**: cs.HC, cs.AI
**Published**: 2026-04-09

## Related Concepts

- Shared memory in multi-agent systems
- Event-driven architecture
- Actor model for state management
- Context-aware computing