---
name: logact-agentic-reliability
description: "LogAct - enabling agentic reliability via shared logs. Deconstructed state machine architecture for LLM agents with pre-execution validation, failure recovery, and semantic introspection. Activation: agent reliability, agentic system, shared log, agent failure recovery, LogAct."
---

# LogAct: Agentic Reliability via Shared Logs

A reliability architecture for LLM-driven agents, using shared logs as the central abstraction for coordination, validation, recovery, and introspection.

## Core Concept

### Agent as Deconstructed State Machine

Traditional agents execute actions directly. LogAct deconstructs this into:

```
Agent = Action Proposal → Log Entry → Validation → Execution → Result

关键分离：提议 ≠ 执行
```

**Components**:
1. **Proposal Phase**: Agent proposes actions (writes to log)
2. **Validation Phase**: Voters check proposals before execution
3. **Execution Phase**: Validated actions are executed
4. **Result Phase**: Outcomes recorded back to log

### Shared Log as Central Abstraction

**Log Properties**:
- **Persistence**: Actions survive agent failures
- **Visibility**: All agents see proposed/executed actions
- **Ordering**: Causal ordering of operations preserved
- **Recovery**: Log enables consistent state reconstruction

```
Shared Log ≈ 分布式系统的真理源
```

## Architecture

### LogAct Agent Structure

```python
class LogActAgent:
    """
    Agent playing a shared log.
    Deconstructed state machine with pre-execution validation.
    """
    
    def __init__(self, agent_id: str, shared_log: SharedLog, voters: List[Voter]):
        self.agent_id = agent_id
        self.log = shared_log
        self.voters = voters
        self.state = AgentState()
    
    def propose_action(self, action: Action) -> LogEntry:
        """
        Phase 1: Propose action by writing to shared log.
        Action is NOT executed yet - only proposed.
        """
        entry = LogEntry(
            agent_id=self.agent_id,
            action=action,
            timestamp=time.now(),
            status="proposed",
            state_before=self.state.snapshot()
        )
        
        # Write to log (visible to all agents)
        self.log.append(entry)
        
        return entry
    
    def validate_action(self, entry: LogEntry) -> ValidationResult:
        """
        Phase 2: Voters validate proposed action.
        Actions can be STOPPED before execution.
        """
        votes = []
        for voter in self.voters:
            vote = voter.check(entry)
            votes.append(vote)
        
        # Consensus on action execution
        if all(v.approved for v in votes):
            entry.status = "validated"
            return ValidationResult(approved=True, votes=votes)
        else:
            entry.status = "rejected"
            return ValidationResult(approved=False, votes=votes)
    
    def execute_action(self, entry: LogEntry) -> ExecutionResult:
        """
        Phase 3: Execute validated action.
        Only executed if validation passed.
        """
        if entry.status != "validated":
            return ExecutionResult(success=False, error="not validated")
        
        # Execute action in environment
        result = entry.action.execute()
        
        # Record result back to log
        entry.status = "executed"
        entry.state_after = self.state.snapshot()
        entry.result = result
        
        self.log.update(entry)
        
        return ExecutionResult(success=True, result=result)
    
    def recover_from_failure(self):
        """
        Phase 4: Recovery from agent/environment failure.
        Log enables consistent state reconstruction.
        """
        # Replay log from last consistent state
        last_executed = self.log.get_last_executed(self.agent_id)
        
        # Reconstruct state from log entries
        self.state = self.reconstruct_state(last_executed)
        
        # Resume operation
        self.propose_next_action()
```

### Voter Abstraction

```python
class Voter:
    """
    Pluggable, decoupled validator for agent actions.
    Can STOP actions before execution.
    """
    
    def check(self, entry: LogEntry) -> Vote:
        """
        Check proposed action.
        Returns approve/reject vote.
        """
        # Different voter types have different criteria
        raise NotImplementedError

class SafetyVoter(Voter):
    """
    Safety checks: prevent harmful actions.
    """
    
    def check(self, entry: LogEntry) -> Vote:
        if self.is_safe(entry.action):
            return Vote(approved=True, reason="action safe")
        else:
            return Vote(approved=False, reason="action unsafe")

class ResourceVoter(Voter):
    """
    Resource checks: prevent resource exhaustion.
    """
    
    def check(self, entry: LogEntry) -> Vote:
        if self.resources_available():
            return Vote(approved=True, reason="resources available")
        else:
            return Vote(approved=False, reason="resources exhausted")

class SemanticVoter(Voter):
    """
    Semantic checks: prevent semantically invalid actions.
    Uses LLM to validate action intent.
    """
    
    def check(self, entry: LogEntry) -> Vote:
        # LLM-based semantic validation
        validation = self.llm_validate(entry.action)
        
        if validation.valid:
            return Vote(approved=True, reason=validation.reason)
        else:
            return Vote(approved=False, reason=validation.reason)
```

## Key Features

### Feature 1: Pre-Execution Visibility

Actions visible BEFORE execution:
- Other agents can see pending actions
- Voters can stop harmful actions
- System maintains control over execution

```
传统Agent: Decide → Execute (无法干预)
LogAct: Decide → Log → Validate → Execute (可干预)
```

### Feature 2: Consistent Recovery

**Failure Recovery**:
- Agent crashes → log preserved
- Environment fails → log enables replay
- Network partitions → log eventual consistency

**Recovery Modes**:
1. **Exact Recovery**: Replay log exactly
2. **Semantic Recovery**: LLM interprets intent, may adjust
3. **Skip Recovery**: Skip failed action, continue

```python
class SemanticRecovery:
    """
    Semantic variant of recovery using LLM introspection.
    Agent analyzes its own execution history.
    """
    
    def recover_with_introspection(self, agent: LogActAgent):
        """
        Agent uses LLM to analyze log and decide recovery strategy.
        """
        # Get log history
        history = agent.log.get_history(agent.agent_id)
        
        # LLM introspection
        analysis = self.llm_analyze(
            prompt="Analyze agent execution history and suggest recovery",
            context=history
        )
        
        # Semantic recovery decision
        if analysis.should_retry:
            agent.propose_action(analysis.retry_action)
        elif analysis.should_skip:
            agent.skip_failed_action()
        else:
            agent.propose_alternative(analysis.alternative_action)
```

### Feature 3: Agentic Introspection

Agents can analyze their own behavior:

```python
class AgenticIntrospection:
    """
    Agent analyzes its execution history via LLM inference.
    Enables self-debugging, optimization, learning.
    """
    
    def debug_performance(self, agent: LogActAgent):
        """
        Agent debugs its own execution issues.
        """
        recent_actions = agent.log.get_recent(agent.agent_id, limit=50)
        
        # Find problematic patterns
        issues = self.llm_analyze(
            prompt="Identify performance issues in recent actions",
            context=recent_actions
        )
        
        return issues
    
    def optimize_token_usage(self, swarm: List[LogActAgent]):
        """
        Swarm agents optimize collective token usage.
        """
        # Analyze swarm execution patterns
        swarm_log = self.get_swarm_log(swarm)
        
        optimization = self.llm_analyze(
            prompt="Optimize token usage across swarm execution",
            context=swarm_log
        )
        
        # Apply optimizations
        for agent in swarm:
            agent.apply_optimization(optimization[agent.id])
    
    def health_check(self, agent: LogActAgent):
        """
        Semantic health check using log introspection.
        """
        health = self.llm_analyze(
            prompt="Assess agent health from execution log",
            context=agent.log.get_history(agent.agent_id)
        )
        
        return health
```

## Benefits

### Reliability Benefits

| Issue | Traditional Agent | LogAct Agent |
|-------|------------------|--------------|
| Agent crash | State lost | Recover from log |
| Bad action | Already executed | Stopped before execution |
| Environment fail | Uncertain state | Consistent replay |
| Network issue | Inconsistent | Log eventual consistency |
| Resource exhaustion | Hard to prevent | Voter checks |

### Observability Benefits

- **Action Visibility**: All actions visible in log
- **Intent Preservation**: Proposals reveal agent intent
- **Validation Trail**: Voter decisions recorded
- **Execution History**: Complete audit trail

### Introspection Benefits

- **Self-Debugging**: Agent analyzes own errors
- **Semantic Recovery**: LLM-guided recovery decisions
- **Swarm Optimization**: Collective behavior optimization
- **Health Monitoring**: Semantic health checks

## Implementation Patterns

### Pattern 1: Multi-Agent Coordination

```python
class MultiAgentLogAct:
    """
    Multiple agents coordinated via shared log.
    """
    
    def __init__(self, agents: List[LogActAgent], shared_log: SharedLog):
        self.agents = agents
        self.log = shared_log
    
    def coordinate_task(self, task: Task):
        """
        Task split across agents, coordinated via log.
        """
        # Agent 1 proposes initial action
        a1_proposal = self.agents[0].propose_action(task.initial_action())
        
        # Other agents see proposal and react
        for agent in self.agents[1:]:
            # Agent can see a1's proposal
            if agent.should_follow_up(a1_proposal):
                agent.propose_action(agent.follow_up_action(a1_proposal))
        
        # Voters validate all proposals
        for entry in self.log.get_proposed():
            agent = self.find_agent(entry.agent_id)
            agent.validate_action(entry)
        
        # Execute validated actions in order
        for entry in self.log.get_validated_ordered():
            agent = self.find_agent(entry.agent_id)
            agent.execute_action(entry)
```

### Pattern 2: Action Interception

```python
class ActionInterceptor:
    """
    Stop unwanted actions before execution.
    """
    
    def __init__(self, rules: List[ActionRule]):
        self.rules = rules
    
    def check(self, entry: LogEntry) -> Vote:
        """
        Check action against rules.
        """
        for rule in self.rules:
            if rule.matches(entry.action):
                if rule.should_stop:
                    return Vote(
                        approved=False,
                        reason=f"stopped by rule: {rule.name}"
                    )
        
        return Vote(approved=True, reason="no rules matched")
```

### Pattern 3: Failure Recovery with Retry

```python
class RetryRecovery:
    """
    Retry failed actions with backoff.
    """
    
    def recover(self, entry: LogEntry, agent: LogActAgent):
        """
        Retry failed execution with exponential backoff.
        """
        if entry.status == "failed":
            retry_count = entry.retry_count or 0
            
            if retry_count < self.max_retries:
                # Exponential backoff
                delay = self.base_delay * (2 ** retry_count)
                time.sleep(delay)
                
                # Retry action
                new_entry = agent.propose_action(entry.action)
                agent.validate_action(new_entry)
                agent.execute_action(new_entry)
                
                new_entry.retry_count = retry_count + 1
            else:
                # Mark as permanently failed
                entry.status = "failed_final"
                agent.log.update(entry)
```

## Evaluation Results (from paper)

### Recovery Performance

| Scenario | Recovery Time | Correctness |
|----------|---------------|-------------|
| Agent crash | < 1s | 100% consistent |
| Environment fail | 2-5s | 100% recoverable |
| Network partition | Varies | Eventual consistency |

### Action Interception

- **Target model**: 100% unwanted actions stopped
- **Benign utility**: 3% drop (acceptable tradeoff)
- **Voter overhead**: < 100ms per action

### Swarm Optimization

- **Token usage**: 15-30% reduction via introspection
- **Coordination**: Log enables efficient swarm behavior
- **Scalability**: Tested up to 10 concurrent agents

## Design Considerations

### Log Implementation

**Options**:
1. **Centralized Log**: Simple, single point of failure
2. **Distributed Log**: Kafka-style, high availability
3. **Replicated Log**: Raft-style, strong consistency

**Recommendations**:
- For single-agent: Centralized log sufficient
- For multi-agent: Distributed log (Kafka/Pulsar)
- For strong consistency: Replicated log (Raft/Zab)

### Voter Design

**Voter Placement**:
- **Inline**: Validate immediately after proposal
- **Async**: Background validation, queued execution
- **Hybrid**: Fast safety checks inline, semantic checks async

**Voter Scaling**:
- Few voters: Simple coordination
- Many voters: Requires consensus mechanism
- Cross-cutting: Voter composition patterns

### Failure Modes

**Agent Failure**:
- Crash: Log preserved, state recoverable
- Hang: Timeout detection, recovery trigger
- Malfunction: Voters prevent bad actions

**Environment Failure**:
- External service: Retry with backoff
- Infrastructure: Semantic recovery decisions
- Data corruption: Log replay restores consistency

## Related Work

### Log-Based Systems
- Kafka: Distributed event log
- Raft: Replicated log consensus
- Event sourcing: State from event history

### Agent Reliability
- Actor model: Supervision trees (Akka/Orleans)
- Workflow engines: Saga pattern
- Process managers: Long-running processes

### LLM Agent Systems
- ReAct: Reasoning + acting framework
- AutoGPT: Goal-driven agent
- CrewAI: Multi-agent coordination

## Applications

### Application 1: Production LLM Agents

**Use Case**: Deploy agents in production with reliability guarantees

**Benefits**:
- Prevent harmful actions
- Recover from failures
- Maintain audit trail

### Application 2: Multi-Agent Workflows

**Use Case**: Complex workflows requiring coordination

**Benefits**:
- Shared log enables visibility
- Voters enforce workflow rules
- Recovery maintains workflow continuity

### Application 3: Agentic AI Systems

**Use Case**: Long-running autonomous agents

**Benefits**:
- Introspection enables self-improvement
- Optimization reduces resource usage
- Health checks maintain agent quality

## References

### Core Paper
- Balakrishnan et al. (2026): "LogAct: Enabling Agentic Reliability via Shared Logs" arXiv:2604.07988

### Related Work
- Kafka: Distributed log platform
- Raft: Consensus for replicated logs
- Akka: Actor model with supervision

### Agent Background
- ReAct framework
- Multi-agent systems
- Workflow patterns (Saga, orchestration)

## Activation Keywords

- agent reliability
- agentic system
- shared log architecture
- agent failure recovery
- LogAct
- pre-execution validation
- agent introspection
- semantic recovery
- multi-agent coordination
- action interception

## Recommended Model

- **sonnet4.5** (For practical implementation)
- **opus4.5** (For system design analysis)

## Tools Used

- **exec**: Run agent simulations
- **read**: Load log configurations
- **write**: Save agent specifications
- **cron**: Schedule periodic health checks

---

_This skill provides a reliability architecture for LLM agents, enabling production-grade deployment with safety guarantees, failure recovery, and semantic introspection._