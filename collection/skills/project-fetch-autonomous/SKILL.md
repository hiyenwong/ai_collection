---
name: project-fetch-autonomous
description: Methodology for evaluating autonomous AI capability progression across phases — measuring when models transition from human-assisted to autonomous execution using robotics tasks as a benchmark.
category: ai_collection
trigger_words: project fetch, autonomous capability, robotics evaluation, capability progression, phase comparison, robodog, physical world agents
date: 2026-07-13
source: "Anthropic Research - Project Fetch: Phase two (Jun 18, 2026)"
url: "https://www.anthropic.com/research/project-fetch-phase-two"
---

# Project Fetch: Autonomous Capability Evaluation Framework

## Overview

A methodology for evaluating how AI model capabilities progress from human-assisted to autonomous execution, using robotics tasks as a benchmark. The core pattern observed: **first, models are helpful to humans. Then, humans are helpful to models. Finally, models are largely able to do things themselves.**

## Experimental Design

### Phase Structure
1. **Phase 1 (Human teams)**: Teams of non-expert employees perform tasks with/without AI assistance
2. **Phase 2 (Autonomous)**: Latest models attempt same tasks without human assistance, with researcher limited to:
   - Plugging in hardware
   - Entering initial prompt
   - Approving commands
   - Approving progression to next task

### Task Selection Criteria
- Tasks must be completable by at least one human team in Phase 1
- Tasks should NOT require physical manipulation (e.g., using a controller)
- Tasks should test programmatic control, not low-level robotic actuation

### Metrics
- **Speed comparison**: Time to complete tasks (autonomous vs. human teams)
- **Code efficiency**: Lines of code generated (autonomous vs. human teams)
- **Success rate**: Whether tasks are completed correctly on first try
- **Error recovery**: Ability to work around mistakes and find alternative solutions

## Key Findings Pattern

| Capability Stage | Characteristics |
|-----------------|-----------------|
| Stage 1: Human-helpful | Model assists humans, humans make key decisions |
| Stage 2: Human-helpful-to-model | Humans guide model through difficult steps |
| Stage 3: Autonomous | Model completes tasks independently, 10-37x faster than human teams |

## Application to Other Domains

This methodology has been applied to:
- **Robotics** (Project Fetch): robodog sensor connection, path monitoring, object detection
- **Cybersecurity**: Previously observed similar progression in red team exercises

The pattern suggests that domains following this progression will eventually see autonomous model capabilities, but NOT necessarily at the level of low-level physical control (e.g., developing specific actuation policies).

## Limitations

- Does NOT mean the model has "solved" the domain (e.g., robotics)
- Tasks tested are higher-level programmatic control, not low-level actuation
- Human researcher still provides hardware setup and command approval
- Success on structured tasks doesn't generalize to open-ended physical manipulation
