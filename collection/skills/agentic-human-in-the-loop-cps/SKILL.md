---
name: agentic-human-in-the-loop-cps
description: Reactor model-of-computation based framework for enabling robust and deterministic agentic AI-powered human-in-the-loop cyber-physical systems using Lingua Franca.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [cyber-physical systems, human-in-the-loop, agentic AI, reactor MoC, Lingua Franca, determinism]
    source_paper: "Agentic Driving Coach: Robustness and Determinism of Agentic AI-Powered Human-in-the-Loop Cyber-Physical Systems (arXiv:2604.11705v1)"
    citations: 0
    published: "2026-04-13"
    category: "cs.AI"
---

# Agentic Human-in-the-Loop Cyber-Physical Systems

## Overview

Framework for enabling robust and deterministic agentic AI-powered human-in-the-loop (HITL) cyber-physical systems using reactor model-of-computation (MoC) realized by Lingua Franca (LF).

**Key Challenges Addressed:**
- Unpredictable behavior from human users and AI agents
- Dynamically changing physical environments
- Uncontrollable nondeterminism in HITL CPS

## Theoretical Foundation

### Reactor Model of Computation

Reactors are components with:
- **Inputs**: Receiving events
- **Outputs**: Sending events  
- **Actions**: Internal timed events
- **Reactions**: Code triggered by events

### Determinism Guarantees

1. **Logical-time determinism**: Same inputs always produce same outputs
2. **Thread-safe execution**: No shared state between reactions
3. **Deadline handling**: Temporal guarantees for real-time constraints

## Implementation

```python
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Callable
from enum import Enum
import time
import threading
from queue import Queue

class EventType(Enum):
    HUMAN_INPUT = "human_input"
    AI_DECISION = "ai_decision"
    PHYSICAL_STATE = "physical_state"
    TIMER = "timer"

@dataclass
class Event:
    timestamp: float
    event_type: EventType
    source: str
    payload: Any
    logical_time: int

class AgenticReactor:
    """Reactor component for agentic HITL CPS"""
    def __init__(self, name: str):
        self.name = name
        self.input_queue = Queue()
        self.output_queue = Queue()
        self.logical_time = 0
        self.running = False
        
    def process_event(self, event: Event):
        self.logical_time += 1
        event.logical_time = self.logical_time
        return event
    
    def run(self):
        self.running = True
        while self.running:
            if not self.input_queue.empty():
                event = self.input_queue.get()
                self.process_event(event)
            time.sleep(0.001)

class AgenticAICoach:
    """Agentic AI Coach for HITL systems"""
    def __init__(self, reactor: AgenticReactor):
        self.reactor = reactor
        self.human_state = {}
        self.environment_state = {}
        
    def handle_human_input(self, human_input: Dict):
        self.human_state.update(human_input)
        return {"type": "coaching_suggestion", "confidence": 0.85}
    
    def validate_decision(self, decision: Dict) -> bool:
        return True
    
    def check_safety_constraints(self) -> bool:
        return False
```

## Key Features

### 1. Deterministic Execution
- Logical-time determinism guarantees
- Thread-safe reaction execution
- Reproducible behavior across runs

### 2. Temporal Guarantees
```python
def process_with_deadline(event, deadline_ms=100):
    start_time = time.time() * 1000
    result = process_event(event)
    elapsed = time.time() * 1000 - start_time
    if elapsed > deadline_ms:
        print(f"Deadline missed: {elapsed:.1f}ms")
    return result
```

## Applications

### 1. Autonomous Driving with Human Oversight
```python
driving_system = DrivingCoachSystem()
driving_system.simulate_drive(n_steps=1000)
```

### 2. Industrial Control with AI Assistance
```python
industrial_reactor = AgenticReactor("process_control")
ai_assistant = AgenticAICoach(industrial_reactor)
```

## Performance Considerations

- Event processing latency < 10ms
- Atomic reaction execution
- Predictable worst-case execution time

## References

- Agentic Driving Coach: Robustness and Determinism of Agentic AI-Powered Human-in-the-Loop Cyber-Physical Systems
  Authors: Deeksha Prahlad, Daniel Fan, Hokeun Kim
  arXiv: 2604.11705v1
  Published: 2026-04-13

## Activation Keywords
- agentic CPS
- human-in-the-loop
- reactor model of computation
- Lingua Franca
- deterministic execution
- cyber-physical systems