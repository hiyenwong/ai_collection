---
name: psi-shared-state-architecture-v2
description: PSI (Persistent Shared Interface) shared-state architecture for coherent AI-generated instruments in personal AI agents. Use when designing modular AI systems that need cross-module communication, state sharing between GUI and chat interfaces, or creating personal computing environments with coherent AI-generated modules. Activation: PSI, shared state, personal AI, AI-generated instruments, modular agent system, cross-module reasoning.
---

# PSI: Shared State Architecture for Personal AI Agents

## Overview

PSI transforms isolated AI-generated modules into **coherent instruments** - persistent, connected, and chat-complementary artifacts accessible through both GUIs and conversational interfaces.

## Core Innovation

**Shared state is the missing systems layer** that transforms AI-generated personal software from isolated apps into coherent personal computing environments.

## Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERACTION LAYER                        │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │  Persistent │     │   Generic   │     │   Proactive │   │
│  │     GUI     │◄───►│ Chat Agent  │◄───►│   Nudges    │   │
│  └─────────────┘     └─────────────┘     └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              SHARED PERSONAL-CONTEXT LAYER                  │
│     Context Assembly Engine • Person-scoped State           │
│     Tagged Context Format • Write-back Affordances          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    GENERATION LAYER                         │
│         (AI-Powered Module Creation)                        │
│    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐         │
│    │ Module  │ │ Module  │ │ Module  │ │ Module  │         │
│    │    A    │ │    B    │ │    C    │ │    N    │         │
│    └─────────┘ └─────────┘ └─────────┘ └─────────┘         │
└─────────────────────────────────────────────────────────────┘
```

## Key Design Principles

1. **Integration as Local Obligation**: Each module implements one contract, not pairwise wiring
2. **Person-scoped Persistence**: State shared across sessions by GUI and chat
3. **Tagged Context Format**: Enables LLM-mediated cross-module reasoning
4. **Write-back Affordances**: Bidirectional actions from chat to GUI

## Provider Contract

```typescript
interface ContextProvider {
  readonly moduleId: string;
  readonly keywords: string[];
  
  // Returns tagged state summary
  buildContextSummary(): ContextSummary | null;
  
  // Expose write-back capabilities
  getWritebackAffordances(): WritebackAction[];
}

interface ContextSummary {
  module: string;
  timestamp: number;
  content: string; // Tagged, human-readable
  data?: Record<string, any>;
}
```

## Evaluation Results

- **Shared Context**: 88% fulfillment
- **Search-Only**: 63% fulfillment
- **Single-Module**: 27% fulfillment
- **Write-back Success Rate**: 95%

## Implementation Steps

1. **Define Provider Protocol**: Language-agnostic contract for all modules
2. **Implement Shared Context Bus**: Event-driven state aggregation
3. **Create Module Registry**: Dynamic registration and discovery
4. **Build Generic Chat Agent**: LLM-based cross-module reasoning
5. **Add Write-back Handlers**: Bidirectional state synchronization

## Tagged Context Format

```
[Personal Context]
[health-module]
Current blood pressure: 120/80 mmHg (measured 2 hours ago)
[End health-module]

[activity-module]
Daily steps: 7,532 / 10,000 goal (75% complete)
[End activity-module]
[End Personal Context]

User: What should I do to improve my health today?
```

## References

- **Paper**: "PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents" (arXiv:2604.08529)
- **Authors**: Zhiyuan Wang, Erzhen Hu, Mark Rucker, et al.
- **Published**: April 2026
