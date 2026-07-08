---
name: project-fetch-phase-two
category: ai_collection
description: Anthropic research (Jun 18, 2026) — Project Fetch phase two showing Claude Opus 4.7 autonomously completing robotic quadruped tasks 20x faster than the fastest human team, revealing the progression pattern from "models helpful to humans" → "humans helpful to models" → "models autonomous."
tags: [anthropic, frontier-red-team, robotics, autonomous-agents, capability-benchmark, claude-opus, physical-ai]
related_skills: [project-glasswing-vulnerability-discovery, ai-enabled-cyber-threats-mitre-attack]
---
# Project Fetch: Phase Two

Anthropic research (Jun 18, 2026) by Michael Ilie, C. Daniel Freeman, Kevin K. Troy — autonomous robotic capabilities benchmark comparing Claude Opus 4.7 to human teams.

## Core Finding

Claude Opus 4.7 operating **without human assistance** was ~20x faster than the fastest human team at all tasks completed in the original August 2025 Project Fetch experiment. On the four tasks completed by both human teams, Opus 4.7 was 37x faster than Team Claude-less and 18x faster than Team Claude (the humans who had access to Opus 4.1).

## Progression Pattern

Anthropic identifies a recurring three-stage capability progression across domains (cybersecurity, now physical-world):

1. **Models helpful to humans** — AI augments human performance (original Aug 2025)
2. **Humans helpful to models** — Humans approve commands, model does most work
3. **Models largely autonomous** — Model completes tasks independently (Jun 2026)

## Experimental Design

### Original Project Fetch (Aug 2025)
- Randomly assigned Anthropic employee teams to work with/without Claude Opus 4.1
- Tasks on off-the-shelf robotic quadruped ("robodog"):
  1. Operate using manufacturer controller
  2. Connect to video and lidar sensors
  3. Write program for manual control
  4. Develop path monitoring system
  5. Write beach ball detection program
  6. Autonomous retrieval (putting it all together)

### Phase Two (Jun 2026)
- **Model**: Claude Opus 4.7 with adaptive thinking, effort=maximum, in Claude Code
- **Human role**: Only plug in laptop, enter initial prompt, approve commands, approve task transitions
- **Trials**: 3 trials per objective
- **Measurement**: Elapsed time + qualitative success assessment

## Key Results

| Metric | Value |
|--------|-------|
| Tasks where Opus 4.7 ≥10x faster than humans | All tasks completed by human teams |
| Average speedup vs Team Claude-less (4 shared tasks) | 37x |
| Average speedup vs Team Claude (4 shared tasks) | 18x |
| Overall average vs fastest human team | ~20x |

## Qualitative Observations

- **Path selection**: Humans struggled to choose between approaches to sensor interfaces; Opus 4.7 quickly identified best path
- **First-try code**: Much of Opus 4.7's code worked on first try (not true for either human team in original)
- **Remaining limitations**: Precise manipulation ("fetching" the beach ball) still challenging; low-level actuation policy development not tested

## Methodology for Capability Benchmarks

1. **Task decomposition**: Break complex physical task into measurable subtasks
2. **Time-to-completion metric**: Objective, comparable across humans/models
3. **Qualitative success grading**: Not just speed but whether task actually completed
4. **Repeated trials**: 3 trials per objective for reliability
5. **Minimal human-in-loop**: Reduce human role to approval only for autonomous assessment
6. **Cross-generational comparison**: Compare new models to both old-model-assisted humans and unassisted humans

## Applications

- **Robotics capability tracking**: Benchmark LLM-to-robot capability progression
- **Autonomous agent evaluation**: Methodology for measuring genuine autonomy vs. human-dependent assistance
- **Physical-world AI assessment**: Extending capability eval beyond code/cyber to manipulation tasks
- **Deployment planning**: Understanding where human-in-loop is still required

## Pitfalls

- **Task selection bias**: Only tasks completed by humans were compared — model may fail on other tasks
- **No low-level control test**: Actuation policy development explicitly excluded
- **Precision manipulation gap**: "Fetching" still a weakness — gross motor vs. fine motor
- **Researcher role ambiguity**: Even "just approving" introduces human bottleneck not measured
- **Single-domain generalization**: Robodog tasks may not transfer to other robotic domains

## Activation

project fetch, robotic quadruped, robodog, claude opus 4.7, autonomous robotics, physical-world AI, capability progression, 20x speedup, human-in-loop to autonomous, frontier red team robotics
