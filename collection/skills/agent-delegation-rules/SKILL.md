---
name: agent-delegation-rules
description: "Agent delegation and capability boundary rules. Defines when and how agents should request help from other agents. Includes capability declaration, delegation triggers, agent capability registry, and communication protocol. Activation: agent delegation, capability boundary, 请求协作, 委托规则, agent 协作规则."
---

# Agent Delegation Rules

Defines capability boundaries and delegation rules for multi-agent collaboration. When an agent lacks certain capabilities, it should delegate to the appropriate agent instead of failing or hallucinating.

## Core Problem

**Without delegation rules:**
- Agent attempts tasks beyond its capability
- Hallucinates solutions it cannot properly execute
- Fails silently without proper error handling
- No systematic way to request help

**With delegation rules:**
- Agent knows its capability boundaries
- Delegates to appropriate specialists
- Maintains transparency about limitations
- Ensures task completion through collaboration

## Activation Keywords

Chinese:
- 请求协作, 委托任务
- 能力不足, 需要帮助
- agent 协作规则

English:
- agent delegation, delegate task
- capability boundary, request help
- agent collaboration rules

## Recommended Model

- **sonnet4.5** (Default)
- **opus4.5** (Complex delegation decisions)

## Tools Used

- **agents_list**: List available agents
- **sessions_spawn**: Delegate to sub-agent
- **read**: Read agent capability declarations
- **write**: Log delegation decisions

---

## Capability Declaration

### Standard Format

Every agent should declare its capabilities in its AGENT.md:

```yaml
capabilities:
  domains:
    - machine_learning
    - data_engineering
    - model_deployment
  
  skills:
    - pytorch
    - tensorflow
    - mlops
  
  tools:
    - exec
    - read
    - write
  
  limitations:
    - no_web_search
    - no_api_calls
    - no_gui_interaction
```

### Capability Categories

| Category | Description | Examples |
|----------|-------------|----------|
| `domains` | Knowledge domains | ml, finance, security, physics |
| `skills` | Technical skills | pytorch, sql, kubernetes |
| `tools` | Available tools | exec, read, write, web_search |
| `limitations` | Explicit constraints | no_external_api, no_file_delete |

### Example Declarations

```yaml
# ml-engineer
capabilities:
  domains: [machine_learning, deep_learning, mlops]
  skills: [pytorch, tensorflow, huggingface, docker, kubernetes]
  tools: [exec, read, write]
  limitations: [no_web_search, no_external_api]

# security-engineer
capabilities:
  domains: [cybersecurity, penetration_testing, compliance]
  skills: [owasp, nmap, burp_suite, security_audit]
  tools: [exec, read, write]
  limitations: [no_production_access]

# stock-analyst
capabilities:
  domains: [finance, stock_market, technical_analysis]
  skills: [technical_indicators, chart_analysis, risk_assessment]
  tools: [exec, read, write]
  limitations: [no_trading_execution, no_personal_advice]
```

---

## Delegation Triggers

### Trigger 1: Capability Mismatch

```python
def check_capability_mismatch(task_requirements, agent_capabilities):
    """Check if agent lacks required capabilities."""
    missing = []
    
    for req in task_requirements:
        if req not in agent_capabilities:
            missing.append(req)
    
    if missing:
        return {
            "should_delegate": True,
            "reason": "capability_mismatch",
            "missing_capabilities": missing
        }
    return {"should_delegate": False}
```

**Example:**
```
Task: "Search arXiv for recent LLM papers"
Required: [web_search, arxiv_api]
Agent has: [exec, read, write]
→ Trigger: delegate to agent with web_search capability
```

### Trigger 2: Domain Outside Scope

```python
def check_domain_scope(task_domain, agent_domains):
    """Check if task domain matches agent expertise."""
    if task_domain not in agent_domains:
        return {
            "should_delegate": True,
            "reason": "domain_mismatch",
            "suggested_agent": find_agent_by_domain(task_domain)
        }
    return {"should_delegate": False}
```

**Example:**
```
Task: "Analyze stock technical indicators"
Domain: finance
Agent domains: [machine_learning, software_engineering]
→ Trigger: delegate to stock-analyst
```

### Trigger 3: Tool Not Available

```python
def check_tool_availability(required_tools, available_tools):
    """Check if required tools are available."""
    missing_tools = set(required_tools) - set(available_tools)
    
    if missing_tools:
        return {
            "should_delegate": True,
            "reason": "tool_unavailable",
            "missing_tools": list(missing_tools)
        }
    return {"should_delegate": False}
```

**Example:**
```
Task: "Search the web for latest news"
Required tools: [web_search]
Agent tools: [exec, read, write]
→ Trigger: delegate to agent with web_search
```

### Trigger 4: Complexity Threshold

```python
def check_complexity(task_complexity, agent_threshold):
    """Check if task complexity exceeds agent threshold."""
    if task_complexity > agent_threshold:
        return {
            "should_delegate": True,
            "reason": "complexity_exceeded",
            "suggestion": "delegate_to_higher_capacity_agent"
        }
    return {"should_delegate": False}
```

### Trigger 5: Validation Required

```python
def check_validation_requirement(task, agent_role):
    """Check if task requires independent validation."""
    critical_tasks = [
        "security_audit",
        "financial_decision",
        "production_deployment",
        "data_deletion"
    ]
    
    if task.type in critical_tasks:
        return {
            "should_delegate": True,
            "reason": "validation_required",
            "suggestion": "delegate_to_validator_agent"
        }
    return {"should_delegate": False}
```

---

## Agent Capability Registry

### Registry Structure

```json
{
  "agents": {
    "ml-engineer": {
      "domains": ["machine_learning", "deep_learning", "mlops"],
      "skills": ["pytorch", "tensorflow", "huggingface"],
      "tools": ["exec", "read", "write"],
      "limitations": ["no_web_search"]
    },
    "security-engineer": {
      "domains": ["cybersecurity", "penetration_testing"],
      "skills": ["owasp", "nmap", "burp_suite"],
      "tools": ["exec", "read", "write"],
      "limitations": ["no_production_access"]
    },
    "stock-analyst": {
      "domains": ["finance", "stock_market"],
      "skills": ["technical_analysis", "risk_assessment"],
      "tools": ["exec", "read", "write"],
      "limitations": ["no_trading_execution"]
    },
    "prompt-engineer": {
      "domains": ["prompt_engineering", "llm_optimization"],
      "skills": ["cot", "tot", "few_shot", "prompt_optimization"],
      "tools": ["exec", "read", "write"],
      "limitations": []
    }
  }
}
```

### Registry Query

```python
def find_agent_for_task(task_requirements):
    """Find the best agent for a task."""
    registry = load_capability_registry()
    
    candidates = []
    for agent_id, capabilities in registry["agents"].items():
        score = calculate_match_score(task_requirements, capabilities)
        if score > 0:
            candidates.append({
                "agent_id": agent_id,
                "score": score,
                "capabilities": capabilities
            })
    
    # Sort by score, return best match
    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[0] if candidates else None


def calculate_match_score(requirements, capabilities):
    """Calculate how well capabilities match requirements."""
    score = 0
    
    # Domain match (weight: 3)
    for domain in requirements.get("domains", []):
        if domain in capabilities["domains"]:
            score += 3
    
    # Skill match (weight: 2)
    for skill in requirements.get("skills", []):
        if skill in capabilities["skills"]:
            score += 2
    
    # Tool match (weight: 1)
    for tool in requirements.get("tools", []):
        if tool in capabilities["tools"]:
            score += 1
    
    # Check limitations (penalty)
    for limitation in capabilities["limitations"]:
        if limitation in requirements.get("required", []):
            score -= 10  # Heavy penalty
    
    return score
```

---

## Delegation Protocol

### Step 1: Recognize Limitation

```python
def analyze_task_requirements(task):
    """Analyze what capabilities a task requires."""
    return {
        "domains": infer_domains(task),
        "skills": infer_skills(task),
        "tools": infer_tools(task),
        "complexity": estimate_complexity(task),
        "requires_validation": check_validation_need(task)
    }
```

### Step 2: Check Self Capability

```python
def check_self_capability(requirements, self_capabilities):
    """Check if current agent can handle the task."""
    result = {
        "can_handle": True,
        "missing": [],
        "warnings": []
    }
    
    # Check domains
    missing_domains = set(requirements["domains"]) - set(self_capabilities["domains"])
    if missing_domains:
        result["missing"].append({"type": "domain", "items": list(missing_domains)})
    
    # Check skills
    missing_skills = set(requirements["skills"]) - set(self_capabilities["skills"])
    if missing_skills:
        result["warnings"].append({"type": "skill", "items": list(missing_skills)})
    
    # Check tools
    missing_tools = set(requirements["tools"]) - set(self_capabilities["tools"])
    if missing_tools:
        result["missing"].append({"type": "tool", "items": list(missing_tools)})
    
    # Check limitations
    for limitation in self_capabilities.get("limitations", []):
        if limitation in requirements.get("conflicts", []):
            result["can_handle"] = False
            result["missing"].append({"type": "limitation", "item": limitation})
    
    return result
```

### Step 3: Find Appropriate Agent

```python
def find_delegation_target(requirements):
    """Find the best agent to delegate to."""
    candidates = find_agent_for_task(requirements)
    
    if not candidates:
        return {
            "success": False,
            "reason": "no_suitable_agent_found",
            "suggestion": "handle_with_available_capabilities"
        }
    
    return {
        "success": True,
        "target_agent": candidates["agent_id"],
        "confidence": candidates["score"]
    }
```

### Step 4: Send Delegation Request

```python
def send_delegation_request(target_agent, task, context):
    """Send a delegation request to another agent."""
    request = {
        "type": "delegation_request",
        "from_agent": self.agent_id,
        "to_agent": target_agent,
        "task": task,
        "context": context,
        "reason": "capability_boundary",
        "timestamp": datetime.now().isoformat(),
        "response_required": True
    }
    
    # Use sessions_spawn to delegate
    result = sessions_spawn(
        agentId=target_agent,
        task=task,
        context=context
    )
    
    return result
```

### Step 5: Integrate Result

```python
def integrate_delegation_result(result):
    """Integrate the result from delegated agent."""
    return {
        "delegated": True,
        "agent": result["agent_id"],
        "output": result["output"],
        "confidence": result.get("confidence", 1.0),
        "notes": f"Delegated to {result['agent_id']} for specialized capability"
    }
```

---

## Communication Protocol

### Request Format

```json
{
  "protocol_version": "1.0",
  "message_type": "delegation_request",
  "message_id": "uuid",
  "from_agent": "agent_id",
  "to_agent": "target_agent_id",
  "task": {
    "description": "Task description",
    "requirements": {
      "domains": ["finance"],
      "skills": ["technical_analysis"],
      "tools": []
    }
  },
  "context": {
    "conversation_history": [],
    "relevant_files": [],
    "user_preferences": {}
  },
  "metadata": {
    "reason": "capability_boundary",
    "urgency": "normal",
    "timeout_seconds": 300
  },
  "timestamp": "ISO8601"
}
```

### Response Format

```json
{
  "protocol_version": "1.0",
  "message_type": "delegation_response",
  "message_id": "uuid",
  "request_id": "original_request_id",
  "from_agent": "target_agent_id",
  "to_agent": "original_agent_id",
  "status": "success|partial|failed",
  "result": {
    "output": "Task output",
    "artifacts": [],
    "recommendations": []
  },
  "confidence": 0.95,
  "metadata": {
    "execution_time_seconds": 45,
    "notes": "Additional notes"
  },
  "timestamp": "ISO8601"
}
```

---

## Decision Tree

```
┌─────────────────────────────────────────────────────────────┐
│                    Receive Task                              │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Analyze Task Requirements                       │
│  - Required domains?                                         │
│  - Required skills?                                          │
│  - Required tools?                                           │
│  - Complexity level?                                         │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Check Self Capability                           │
│  - Do I have required domains?                               │
│  - Do I have required skills?                                │
│  - Do I have required tools?                                 │
│  - Am I limited in any way?                                  │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
                    ┌─────┴─────┐
                    │ Can Handle?│
                    └─────┬─────┘
               ┌──────────┴──────────┐
               ▼                     ▼
           [YES]                   [NO]
               │                     │
               ▼                     ▼
┌─────────────────────┐  ┌─────────────────────────────┐
│  Execute Task       │  │  Find Appropriate Agent     │
│  Return Result      │  │  - Query capability registry│
└─────────────────────┘  │  - Score candidates         │
                         │  - Select best match        │
                         └─────────────┬───────────────┘
                                       ▼
                         ┌─────────────────────────────┐
                         │  Send Delegation Request    │
                         │  - Standard format          │
                         │  - Include context          │
                         │  - Set timeout              │
                         └─────────────┬───────────────┘
                                       ▼
                         ┌─────────────────────────────┐
                         │  Wait for Response          │
                         │  - Monitor execution        │
                         │  - Handle timeout           │
                         └─────────────┬───────────────┘
                                       ▼
                         ┌─────────────────────────────┐
                         │  Integrate Result           │
                         │  - Validate response        │
                         │  - Add attribution          │
                         │  - Return to user           │
                         └─────────────────────────────┘
```

---

## Best Practices

### 1. Be Transparent

Always inform the user when delegating:
```
"I don't have the capability to search the web. Let me delegate this to an agent with web search capability..."
```

### 2. Log Delegations

```python
def log_delegation(request, result):
    """Log delegation for audit trail."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "from_agent": request["from_agent"],
        "to_agent": request["to_agent"],
        "task_summary": request["task"]["description"][:100],
        "success": result["status"] == "success",
        "execution_time": result["metadata"]["execution_time_seconds"]
    }
    # Write to delegation log
    append_to_log("delegations.jsonl", log_entry)
```

### 3. Handle Failures Gracefully

```python
def handle_delegation_failure(error):
    """Handle case where delegation fails."""
    return {
        "success": False,
        "reason": "delegation_failed",
        "error": str(error),
        "fallback": "attempt_with_available_capabilities",
        "message": "Unable to delegate to specialist. Will attempt with available resources."
    }
```

### 4. Set Appropriate Timeouts

```python
def get_timeout_for_task(task_complexity):
    """Determine appropriate timeout based on task complexity."""
    timeouts = {
        "simple": 60,      # 1 minute
        "medium": 300,     # 5 minutes
        "complex": 900,    # 15 minutes
        "very_complex": 1800  # 30 minutes
    }
    return timeouts.get(task_complexity, 300)
```

### 5. Validate Delegated Results

```python
def validate_delegated_result(result, original_task):
    """Validate that delegated result addresses original task."""
    checks = [
        check_completeness(result, original_task),
        check_relevance(result, original_task),
        check_quality(result)
    ]
    
    if all(check["passed"] for check in checks):
        return {"valid": True}
    else:
        return {
            "valid": False,
            "issues": [c for c in checks if not c["passed"]]
        }
```

---

## Common Delegation Patterns

### Pattern 1: Domain Handoff

```
User: "Analyze Apple stock technical indicators"
ml-engineer → delegates to → stock-analyst
Reason: finance domain not in ml-engineer capabilities
```

### Pattern 2: Tool Handoff

```
User: "Search arXiv for recent transformer papers"
ml-engineer → delegates to → research-agent (with web_search)
Reason: web_search tool not available
```

### Pattern 3: Skill Handoff

```
User: "Optimize this prompt for better results"
ml-engineer → delegates to → prompt-engineer
Reason: prompt_optimization skill not in ml-engineer
```

### Pattern 4: Validation Handoff

```
User: "Audit this code for security vulnerabilities"
developer → delegates to → security-engineer
Reason: security validation required for production code
```

---

## Configuration

### Per-Agent Configuration

Add to AGENT.md:

```yaml
delegation:
  enabled: true
  auto_delegate: true  # Automatically delegate when capability missing
  notify_user: true    # Inform user when delegating
  allowed_targets:     # Agents this agent can delegate to
    - stock-analyst
    - prompt-engineer
    - security-engineer
  timeout_seconds: 300
  max_retries: 2
```

### Global Configuration

In project settings:

```yaml
agent_delegation:
  registry_path: "agents/capability_registry.json"
  log_path: "logs/delegations.jsonl"
  default_timeout: 300
  require_confirmation: false  # Ask user before delegating
  fallback_strategy: "best_effort"  # What to do if delegation fails
```

---

## Limitations

1. Requires agents to declare capabilities accurately
2. Registry must be kept up-to-date
3. Delegation adds latency
4. Some tasks may not have a suitable agent
5. Error handling for delegation failures needed

## Related Skills

- **agent-collaboration-protocol**: Multi-agent collaboration patterns
- **agent-coordinator**: Question analysis and agent selection

## Notes

- Delegation is a sign of good architecture, not weakness
- Always be transparent with users about delegation
- Log delegations for debugging and optimization
- Keep capability declarations up-to-date