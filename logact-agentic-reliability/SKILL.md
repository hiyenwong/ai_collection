---
name: logact-agentic-reliability
description: "LogAct - enabling agentic reliability via shared logs. Deconstructed state machine architecture where agents play a shared log for reliable execution in production environments. Use for: agent reliability, shared log architectures, agentic state machines, production agent systems, async agent coordination. Activation: LogAct, agentic reliability, shared log agents, agent state machine, agent coordination logs."
---

# LogAct: Enabling Agentic Reliability via Shared Logs

LogAct is a shared-log abstraction for reliable agent execution where each agent is a deconstructed state machine playing a shared log.

## Overview

Agents are LLM-driven components that can mutate environments in powerful, arbitrary ways. Extracting guarantees for agent execution in production is challenging due to asynchrony and failures. LogAct addresses this by:

1. **Pre-execution Visibility**: Actions are visible in the shared log before execution
2. **Pluggable Voters**: Actions can be stopped prior to execution by decoupled voters
3. **Consistent Recovery**: Failed agents or environments recover consistently

## Core Concepts

### Agent as Deconstructed State Machine

Traditional state machines bundle state, transitions, and execution. LogAct deconstructs this:

```
Traditional State Machine:
  State + Transitions + Execution (bundled)

LogAct Deconstruction:
  - Shared Log: Persistent, ordered record of all actions
  - State Machine Logic: Deterministic transition function
  - Execution: Separate from state tracking
  - Voters: External validation before execution
```

### Shared Log Abstraction

```
Log Structure:
┌─────────────────────────────────────────────────────────────┐
│  Seq#  │  Action  │  Payload  │  Status  │  Votes         │
├─────────────────────────────────────────────────────────────┤
│  100   │  READ    │  file.txt │  PENDING │  [voter1: OK]  │
│  101   │  WRITE   │  data     │  BLOCKED │  [voter2: REJ] │
│  102   │  EXEC    │  cmd      │  COMMIT  │  [voter1: OK,  │
│        │          │           │          │   voter3: OK]  │
└─────────────────────────────────────────────────────────────┘
```

### Action Lifecycle

```
Proposed → Logged → Voted → {Committed | Blocked} → Executed
   │          │       │            │                  │
   │          │       │            │                  │
   └──────────┴───────┴────────────┴──────────────────┘
                    (Reversible until Committed)
```

1. **Proposed**: Agent generates action
2. **Logged**: Action written to shared log (visible to all)
3. **Voted**: Pluggable voters review and vote
4. **Committed/Blocked**: Based on voting policy
5. **Executed**: Action applied to environment

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────────┐
│                      LogAct System                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Agent 1  │    │ Agent 2  │    │ Agent N  │              │
│  │ (State   │    │ (State   │    │ (State   │              │
│  │ Machine) │    │ Machine) │    │ Machine) │              │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘              │
│       │               │               │                     │
│       └───────────────┼───────────────┘                     │
│                       │                                     │
│              ┌────────┴────────┐                           │
│              │   Shared Log    │                           │
│              │  (Persistent,   │                           │
│              │   Replicated)   │                           │
│              └────────┬────────┘                           │
│                       │                                     │
│       ┌───────────────┼───────────────┐                    │
│       │               │               │                    │
│  ┌────┴────┐    ┌────┴────┐    ┌────┴────┐               │
│  │ Voter 1 │    │ Voter 2 │    │ Voter N │               │
│  │ (Safety)│    │(Policy) │    │ (Rate)  │               │
│  └─────────┘    └─────────┘    └─────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Voter Types

| Voter | Purpose | Example |
|-------|---------|---------|
| Safety Voter | Prevent dangerous actions | Block `rm -rf /` |
| Policy Voter | Enforce business rules | Require approval for $>10k$ |
| Rate Voter | Limit action frequency | Max 100 API calls/min |
| Consistency Voter | Ensure invariants | Check balance ≥ 0 |

## Key Properties

### 1. Pre-execution Visibility

```python
# Action is visible BEFORE execution
log_entry = {
    "seq": next_sequence_number(),
    "action": "file_delete",
    "target": "/important/data",
    "proposed_by": "agent_1",
    "timestamp": now(),
    "status": "PENDING"  # Visible but not yet executed
}
```

### 2. Pluggable Voters

```python
class Voter:
    def vote(self, log_entry) -> Vote:
        """
        Return OK, REJECT, or ABSTAIN
        """
        if self.check_policy(log_entry):
            return Vote.OK
        return Vote.REJECT

# Voters are decoupled - can be added/removed dynamically
voters = [SafetyVoter(), PolicyVoter(), RateVoter()]
```

### 3. Consistent Recovery

```python
def recover_from_failure(last_known_seq):
    """
    On restart, replay log from last_known_seq
    """
    for entry in log.read_from(last_known_seq):
        if entry.status == "COMMITTED":
            # Re-execute to restore state
            execute(entry.action, entry.payload)
        # PENDING/BLOCKED entries don't affect state
```

## Implementation

### Basic Agent State Machine

```python
class LogActAgent:
    def __init__(self, agent_id, shared_log, voters):
        self.id = agent_id
        self.log = shared_log
        self.voters = voters
        self.state = {}
    
    def propose_action(self, action_type, payload):
        """
        Propose an action to the shared log.
        """
        entry = self.log.append({
            "agent": self.id,
            "action": action_type,
            "payload": payload,
            "status": "PENDING"
        })
        
        # Wait for voting
        votes = self.collect_votes(entry)
        
        if all(v == Vote.OK for v in votes):
            entry.status = "COMMITTED"
            self.execute(entry)
        else:
            entry.status = "BLOCKED"
            self.handle_rejection(entry, votes)
    
    def collect_votes(self, entry):
        """
        Collect votes from all registered voters.
        """
        return [voter.vote(entry) for voter in self.voters]
    
    def execute(self, entry):
        """
        Execute committed action.
        """
        # Update state
        self.state = self.transition(self.state, entry)
        
        # Apply to environment
        self.apply_to_environment(entry)
```

### Safety Voter Example

```python
class SafetyVoter:
    """
    Prevents dangerous operations.
    """
    DANGEROUS_PATTERNS = [
        r"rm\s+-rf\s+/",
        r"DROP\s+DATABASE",
        r".*--.*",
    ]
    
    def vote(self, entry):
        action = entry.get("action", "")
        payload = str(entry.get("payload", ""))
        
        # Check against dangerous patterns
        for pattern in self.DANGEROUS_PATTERNS:
            if re.search(pattern, action + " " + payload):
                return Vote.REJECT
        
        return Vote.OK
```

### Recovery Procedure

```python
def recover_agent(agent_id, shared_log):
    """
    Recover agent state from shared log.
    """
    agent = LogActAgent(agent_id, shared_log, voters=[])
    
    # Replay all committed actions
    for entry in shared_log.read_all():
        if entry["agent"] == agent_id and entry["status"] == "COMMITTED":
            agent.state = agent.transition(agent.state, entry)
    
    return agent
```

## Use Cases

### 1. Multi-Agent Coordination

Multiple agents share state through the log:
```
Agent A: READ file → Agent B: MODIFY file → Agent C: DELETE file
```
Log ensures ordering and prevents conflicts.

### 2. Human-in-the-Loop

Human voters review AI actions:
```python
class HumanVoter:
    def vote(self, entry):
        if entry["risk_score"] > THRESHOLD:
            return self.request_human_approval(entry)
        return Vote.OK
```

### 3. Audit and Compliance

Complete history of all actions:
```python
def audit_trail(start_date, end_date):
    return log.query(
        timestamp_range=(start_date, end_date),
        status="COMMITTED"
    )
```

### 4. Safe Experimentation

Test agents with strict voters:
```python
sandbox_voters = [
    ReadOnlyVoter(),  # Only allow reads
    RateLimitVoter(max_calls=10),  # Limit operations
    NoExternalCallsVoter()  # Block network access
]
```

## Advantages

| Property | Traditional Agents | LogAct Agents |
|----------|-------------------|---------------|
| Visibility | Post-hoc logging | Pre-execution |
| Control | Embedded | Pluggable voters |
| Recovery | Ad-hoc | Consistent replay |
| Audit | Best-effort | Complete history |
| Coordination | Custom protocols | Shared log |

## References

- **Paper**: "LogAct: Enabling Agentic Reliability via Shared Logs" by Balakrishnan et al. (arXiv:2604.07988v1, 2026)
- **Authors**: Mahesh Balakrishnan, Ashwin Bharambe, Davide Testuggine, et al.
- **Category**: cs.DC (Distributed Computing)

## Related Skills

- **psi-shared-state-architecture**: PSI shared-state architecture for personal AI agents
- **agent-memory-framework**: Memory-augmented AI agents
- **agentic-fast-slow-planning**: Bridging reasoning with real-time control

## Activation Keywords

- LogAct
- agentic reliability
- shared log agents
- agent state machine
- agent coordination logs
- production agent systems
- agent voters
- agent recovery
