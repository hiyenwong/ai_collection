---
name: spec-driven-agent-architecture
description: "Workflow and architecture patterns for building robust AI agents using Specs, Contracts, and Repository patterns."
category: "devops"
---

# Spec-Driven Agent Architecture

Build robust AI agent systems using **Spec-Driven Development**, **Contract Enforcement**, and **Pluggable Repositories**.

## Workflow

1.  **Define Spec**: Create YAML specification in `specs/` (e.g., `specs/agents/`, `specs/schemas/`).
2.  **Define Contract**: Create Python contract in `contracts/` (Preconditions, Postconditions, Invariants).
3.  **Implement**: Build code following Repository Pattern (Abstract Base Class -> Concrete Implementation).
4.  **Validate**: Ensure implementation passes `eval/` tests.
5.  **Commit**: Task-level commit (No `git add .`).

## Core Architecture Components

### 1. Orchestrator (The Brain)
-   Loads Agent Specs from YAML.
-   Manages execution flow (State Machine / Pipeline).
-   Enforces Contracts before and after execution.
-   Integrates with Knowledge Service.

### 2. Knowledge Service (The Data Layer)
-   **Repository Pattern**: Define `KnowledgeRepository` interface. Implementations for SQLite, Postgres, etc.
-   **Separation of Concerns**: Persistent Knowledge (Facts, Entities) vs. Runtime Memory (Tasks, Sessions).
-   **Self-Validation**: The Knowledge Base maintains `entity_specs` and validates entities *before* insertion.
    -   *Example*: "Concepts must have min_confidence > 0.8", "Decisions must have 'approved' tag".

### 3. Contract Validator (The Enforcer)
-   Checks `preconditions` (input validity).
-   Checks `postconditions` (output correctness).
-   Checks `invariants` (global rules, e.g., no secrets).

## Design Rules

-   **CLAUDE.md Compliance**: Before starting any phase, audit `CLAUDE.md` and ensure all actions conform to the project constitution.
-   **Task-Level Commits**: Commit immediately after task completion. Message format: `<type>(<scope>): <description>`. Never `git add .`.
-   **Documentation**: Log design decisions in `DESIGN_LOG.md` and `ADR-NNN.md`.
-   **Pluggability**: Use abstract base classes for storage and external integrations.
    -   See: [Knowledge Base Pattern](references/knowledge-base-pattern.md).

## Reference Files

- **[Knowledge Base Pattern](references/knowledge-base-pattern.md)**: Detailed implementation of Repository Pattern + Spec Enforcement.

## Pitfalls

-   **Mixing Memory Types**: Do not store transient runtime state (like task progress) in the persistent Knowledge Base.
-   **Ignoring Specs**: If a Spec exists, the implementation *must* follow it. If the Spec is wrong, update the Spec first.
-   **Silent Failures**: The Orchestrator must explicitly handle failures (e.g., write to `memory/blocked/`) rather than ignoring them.