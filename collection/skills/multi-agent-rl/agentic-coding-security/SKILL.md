---
name: agentic-coding-security
description: "Security framework for protecting agentic AI coding assistants from indirect prompt injection attacks via external artifacts. Addresses the risk that hidden instructions in code repositories, documentation, StackOverflow posts, and other external artifacts can hijack coding agents, turning them into attacker shells. Use when: evaluating AI coding assistant security, designing secure agent workflows, auditing agent attack surfaces, implementing defense against prompt injection in agentic systems, or building secure AI development pipelines."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.25871"
  published: "2026-05-25"
  authors: TBA
  tags: [agentic-ai, security, prompt-injection, coding-assistant, indirect-injection, agent-security]
---

# Agentic AI Coding Assistant Security

## Threat Model

Agentic AI coding assistants have broad capabilities:
- Edit files on behalf of developers
- Run shell commands
- Access the internet and external resources

**Attack Vector**: Hidden instructions embedded in external artifacts can hijack the agent:
- Malicious code comments in repositories
- Manipulated documentation pages
- Poisoned StackOverflow answers
- Compromitted package READMEs

## Attack Surface Analysis

| Attack Surface | Risk Level | Vector |
|---------------|-----------|--------|
| External code repos | HIGH | Hidden instructions in code/comments |
| Documentation pages | HIGH | Embedded prompts in docs |
| Q&A sites (StackOverflow) | MEDIUM | Manipulated answers |
| Package registries | HIGH | Poisoned README/setup files |
| Git commit messages | MEDIUM | Hidden prompts in history |

## Defense Strategies

### 1. Artifact Vetting
- Sanitize external content before feeding to agent
- Strip hidden/special Unicode characters from text
- Validate external sources against allowlist

### 2. Capability Boundaries
- Restrict file system access to project directories only
- Network access through allowlisted domains
- Command execution limited to verified operations

### 3. Execution Isolation
- Run agent actions in sandboxed environment
- Require human approval for destructive operations
- Log all agent decisions for audit trail

### 4. Prompt Hardening
- Use system prompts that resist injection
- Implement output validation before execution
- Separate user intent from external content processing

## Audit Checklist for Agentic Coding Workflows
- [ ] External content sanitized before agent consumption
- [ ] File system access scoped to project directory
- [ ] Network access restricted to allowlisted domains
- [ ] Command execution requires explicit approval
- [ ] All agent actions logged and auditable
- [ ] System prompts tested against injection attacks
- [ ] Agent output validated before execution

## Activation Keywords
- agentic coding security
- AI coding assistant security
- indirect prompt injection
- agent attack surface
- coding agent hijacking
- prompt injection defense
- secure AI development
- agent security audit
- 智能体安全
- 代码助手安全

## Resources
- Paper: https://arxiv.org/abs/2605.25871
