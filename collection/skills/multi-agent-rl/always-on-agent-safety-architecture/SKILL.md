---
name: always-on-agent-safety-architecture
description: "Always-on agent safety: sandbox, auto-review, isolation"
---

# Always-On Agent Safety Architecture

Production safety architecture from OpenAI's dots (Sep 2026): how to delegate ongoing responsibility to persistent agents while containing mistakes, protecting credentials, and keeping humans in control. Use as a design template or review checklist for any always-on/autonomous agent system.

## When to Use

- Designing persistent/ambient agents (personal assistants, monitoring agents, workflow automation)
- Reviewing an agent product's safety claims (interview question bank)
- Hardening an agent stack against prompt injection and credential leakage
- Deciding where safety checks must live so the agent cannot disable them

## The Layers (bottom-up)

1. **Model layer**: train for intent understanding, scope adherence, and clarifying questions when answers change what should be done; refuse high-risk domains (bio/cyber misuse); continuous human+automated red teaming on instruction-change and permission-push attempts.
2. **Sandboxed per-agent workspace**: each agent gets its own cloud computer (maintained OS+browser); user environments isolated from each other; **code execution is separated from the systems that coordinate work and enforce safeguards** — the agent cannot use its tools to alter safety systems.
3. **Credential isolation (secure sign-in)**: during sign-in the model is paused; credentials go browser-direct via a dedicated encrypted credential service and never enter the model's context — so they cannot appear in answers or be shared by mistake. (Note: secrets in readable messages/documents remain visible — separate problem.)
4. **Auto-review (separate action checker)**: before consequential actions (send email, modify files), an independent system checks planned steps against user instructions, custom rules, and safety requirements. On block: return the reason to the agent, which may ask the user, try a permitted alternative, hand the step back, or stop. User approval cannot override core safety requirements. Enforcement lives outside any environment the agent can modify.
5. **Proactive/background research with code-enforced limits**: background tasks use read-only tools only, save to private notes, and are prevented (in code, not policy) from messaging people, modifying app content, or controlling a browser/desktop; any follow-up action passes the normal rules.
6. **Monitoring**: watch planning and execution for out-of-scope or safeguard-bypass behavior; on flag, pause work and surface a human review.

## Human-Control Surfaces
- Unified app/permission management; disconnect stops new sharing but learned context persists; full context reset available.
- Activity view: follow, correct, redirect, or stop ongoing work at any time.
- Delegation hygiene: sub-agents instructed to keep only task-necessary info.

## Pitfalls / Honest Limits
- Agents still make mistakes; consequential work always needs review — do not market the stack as safe, market the containment.
- Safety-monitor false positives slow legitimate long-running work; calibrate and give appeal paths.
- Prompt injection cannot be fully solved at one layer; combine model + tool + action + monitoring and keep red-teaming.

## Activation Keywords

- always-on agent safety
- auto-review action gating
- credential isolation secure sign-in
- sandbox agent workspace
- prompt injection containment
- agent permission boundaries
