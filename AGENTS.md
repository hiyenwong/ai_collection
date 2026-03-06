# OpenClaw Agents

## What is an Agent?

An OpenClaw **agent** is an autonomous AI assistant that can be spawned as a sub-session to perform specific tasks. Agents run in isolated sessions and can use different models, thinking levels, and tools than the main session.

## How Agents Work

OpenClaw's `sessions_spawn` system allows you to:
1. **Spawn sub-agent sessions** with specific tasks
2. **Run background tasks** that continue independently
3. **Use different models** optimized for specific work
4. **Get results delivered** back to the requesting session

### Spawning an Agent

```python
sessions_spawn(
    task="Analyze this dataset and create visualizations",
    label="data-analyzer",         # Optional: session label
    agentId="data-analyst",         # Optional: specific agent ID
    model="claude-sonnet-4.5",     # Optional: override model
    thinking="high",                # Optional: thinking level
    runTimeoutSeconds=300,          # Optional: timeout
    cleanup="delete"                # Optional: delete after completion
)
```

## Agent Characteristics

### 1. Isolated Sessions
Each agent runs in its own isolated session with:
- Independent context window
- Separate tool permissions
- Custom model and settings
- Clean environment

### 2. Task-Oriented
Agents are designed for specific types of tasks:
- **Data Analyst**: Process and analyze data
- **Code Reviewer**: Review and improve code
- **Writer**: Create and edit content
- **Researcher**: Find and summarize information
- **Developer**: Implement features and fix bugs

### 3. Model Optimization
Different agents can use different models:
- **Fast models** (Haiku, GPT-4o-mini): Quick tasks, simple queries
- **Balanced models** (Sonnet, GPT-4o): General tasks
- **Powerful models** (Opus, GPT-4.1): Complex reasoning, research

### 4. Background Execution
Agents can run in the background without blocking:
- Long-running tasks
- Periodic checks
- Monitoring jobs
- Data processing pipelines

## Agent Types

### Predefined Agents
OpenClaw comes with predefined agents that can be referenced by `agentId`.

### Custom Agents
You can create custom agents by defining:
- **Purpose**: What the agent does
- **Capabilities**: What tools and skills it uses
- **Behavior**: How it responds and interacts
- **Prompts**: System instructions and personality

## When to Use Agents

Use agents when:
- ✅ Task can run independently in the background
- ✅ You need a different model than the main session
- ✅ Task requires specialized behavior or personality
- ✅ You want to keep the main context focused
- ✅ Multiple parallel tasks need different approaches

Don't use agents when:
- ❌ Quick, simple question is all you need
- ❌ Task requires real-time interaction with the user
- ❌ Main session model is already optimal for the task
- ❌ Task needs access to main session's full context

## Agent Lifecycle

```
Request → Spawn → Execute → Complete → Report → Cleanup
    ↓         ↓        ↓          ↓        ↓         ↓
sessions_spawn  Isolated  Task     Result   Message   Delete
                Session   Work     to      to        (optional)
                          Session  Main     Main
```

## Agent Configuration

### Basic Configuration
```python
{
    "agentId": "my-agent",
    "model": "default",          # Inherit default model
    "thinking": "medium",        # Thinking level
    "timeoutSeconds": 300        # Max execution time
}
```

### Advanced Configuration
```python
{
    "agentId": "research-agent",
    "model": "claude-opus-4.5",  # Powerful model
    "thinking": "high",           # Deep reasoning
    "tools": ["web_search", "web_fetch", "memory"],
    "skills": ["research", "summarize"],
    "systemPrompt": "You are a research specialist...",
    "cleanup": "keep",            # Keep session for reference
    "deliver": true               # Auto-deliver results
}
```

## Agent Best Practices

### 1. Clear Purpose
Define a clear, specific purpose for each agent. Avoid "do-everything" agents.

### 2. Appropriate Model
Match the model to the task complexity:
- Simple queries → Fast models
- Coding tasks → Balanced models
- Research/analysis → Powerful models

### 3. Timeout Management
Set reasonable timeouts based on expected task duration:
- Quick tasks: 60-120 seconds
- Medium tasks: 300-600 seconds
- Long tasks: 1800+ seconds

### 4. Cleanup Strategy
- **Delete** for one-off tasks to save storage
- **Keep** for research or debugging to reference later

### 5. Error Handling
Agents should handle errors gracefully and report issues back to the main session.

## Agent Communication

### Results Delivery
Agents can deliver results in several ways:

1. **Auto-deliver**: Automatic message back to main session
2. **File output**: Write results to workspace files
3. **Database**: Store results in a database
4. **API**: Call external APIs with results

### Inter-Agent Communication
Agents can spawn other agents:
```python
# Agent A spawns Agent B
sessions_spawn(task="Subtask for Agent B", agentId="agent-b")
```

## Example Agents

### Fullstack Engineer Agent
```python
sessions_spawn(
    task="Build a REST API with authentication and database integration",
    agentId="fullstack-engineer",
    model="claude-opus-4.5",
    thinking="high",
    runTimeoutSeconds=600
)
```

**Capabilities:** Frontend (React, Vue, TypeScript), Backend (Node.js, Python, Go), DevOps (Docker, K8s, CI/CD), Security, Performance
**Purpose:** Senior full-stack engineering with focus on production-ready code and scalable architecture
**Skills:** opencode (multi-agent orchestration, ultrawork mode, LSP integration), claude-code (Anthropic's official coding companion), openspec (specification-driven development with Gherkin syntax)

---

### Data Analyst Agent
```python
sessions_spawn(
    task="Analyze the sales data in data/sales.csv and identify trends",
    agentId="data-analyst",
    model="claude-sonnet-4.5",
    thinking="high"
)
```

### Code Reviewer Agent
```python
sessions_spawn(
    task="Review the code in src/ and provide improvement suggestions",
    agentId="code-reviewer",
    model="claude-opus-4.5",
    thinking="high",
    tools: ["read", "edit", "git"],
    skills: ["coding-agent"]
)
```

### Research Agent
```python
sessions_spawn(
    task="Research the latest developments in quantum computing",
    agentId="researcher",
    model="claude-opus-4.5",
    thinking="high",
    tools: ["web_search", "web_fetch", "memory"]
)
```

### Tech Co-Founder (Builder) Agent
```python
sessions_spawn(
    task="Build a REST API with authentication and database integration",
    agentId="tech-cofounder",
    model="claude-sonnet-4.5",
    thinking="high",
    runTimeoutSeconds=600
)
```

**Capabilities:** Product-focused development, rapid prototyping, full-stack implementation, documentation-first approach
**Purpose:** Technical co-founder that builds real, working products based on requirements. Prioritizes executable output over discussion.
**Skills:** opencode (multi-agent orchestration), claude-code (coding companion), general development skills

---

## Available Agents in This Collection

### Fullstack Engineer
- **Location:** `collection/agents/fullstack-engineer/`
- **Purpose:** Senior full-stack engineer focused on modern web development, scalable architecture, and production-grade code
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.6 (alternative)
- **Key Skills:** opencode, claude-code, openspec
- **Tools:** exec, read, write, edit, process, git, npm, uv, python

### Stock Analyst
- **Location:** `collection/agents/stock-analyst/`
- **Purpose:** Stock analyst focused on financial data analysis and market insights
- **Model:** claude-sonnet-4.5 (primary) / claude-opus-4.5 (complex analysis)
- **Key Skills:** akshare, stock-analysis
- **Tools:** exec (Python), read, write

### Tech Co-Founder (Builder)
- **Location:** `collection/agents/tech-cofounder/`
- **Purpose:** Technical co-founder that builds real products based on work orders
- **Model:** claude-sonnet-4.5 (balanced) / claude-opus-4.5 (complex tasks)
- **Key Skills:** opencode, claude-code
- **Tools:** Full development stack (exec, read, write, edit, git, npm, etc.)
- **Workflow:** Plan → Implement in Stages → Polish → Handoff

### Research Agent
- **Location:** `collection/agents/research-agent/`
- **Purpose:** Research specialist for deep investigation and information synthesis
- **Model:** claude-opus-4.5 (primary) for complex research
- **Tools:** web_search, web_fetch, memory, read, write
- **Output:** Comprehensive research reports with sources

### Neuroscientist
- **Location:** `collection/agents/neuroscientist/`
- **Purpose:** Neuroscience research synthesis, neural mechanism analysis, and experiment design support
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

### Computer Network Scientist
- **Location:** `collection/agents/computer-network-scientist/`
- **Purpose:** Computer network architecture and protocol behavior analysis with troubleshooting focus
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

### Computational Scientist
- **Location:** `collection/agents/computational-scientist/`
- **Purpose:** Computational modeling, simulation workflows, and reproducible scientific computing
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, exec

### Biologist
- **Location:** `collection/agents/biologist/`
- **Purpose:** Biological mechanism interpretation and experiment design reasoning
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

### Statistician
- **Location:** `collection/agents/statistician/`
- **Purpose:** Statistical inference, diagnostics, uncertainty quantification, and robust interpretation
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, exec

### Mathematician
- **Location:** `collection/agents/mathematician/`
- **Purpose:** Formal proof-oriented reasoning and structured mathematical derivation
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write

### Philosopher
- **Location:** `collection/agents/philosopher/`
- **Purpose:** Conceptual analysis, argument mapping, and ethical reasoning
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write

### Economist
- **Location:** `collection/agents/economist/`
- **Purpose:** Economic analysis, policy impact evaluation, and market reasoning
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

### Linguist
- **Location:** `collection/agents/linguist/`
- **Purpose:** Language structure analysis, semantics/pragmatics interpretation, and cross-linguistic comparison
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write

### Logician
- **Location:** `collection/agents/logician/`
- **Purpose:** Formal logic reasoning, validity checks, and consistency analysis
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write

### Applied Scientist
- **Location:** `collection/agents/applied-scientist/`
- **Purpose:** Practical science-driven solution design with experiment iteration
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, exec

### Geneticist
- **Location:** `collection/agents/geneticist/`
- **Purpose:** Genetic mechanism interpretation and inheritance/variant reasoning
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

### Population Dynamics Scientist
- **Location:** `collection/agents/population-dynamics-scientist/`
- **Purpose:** Group/population interaction modeling and scenario-based dynamics analysis
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, exec

### Psychologist
- **Location:** `collection/agents/psychologist/`
- **Purpose:** Cognition/behavior analysis and framework-based psychological reasoning
- **Model:** claude-opus-4.5 (primary) / claude-sonnet-4.5 (alternative)
- **Tools:** read, write, web_search

## Troubleshooting

### Agent Not Starting
- Check agent ID is valid and accessible
- Verify gateway is running
- Check agent configuration

### Agent Timeout
- Increase timeoutSeconds
- Break task into smaller chunks
- Use more efficient model

### Agent Not Delivering Results
- Check deliver setting
- Verify message channel is configured
- Check for errors in agent logs

## Resources

- [OpenClaw Docs - Agents](https://docs.openclaw.ai/agents)
- [OpenClaw Docs - Sessions](https://docs.openclaw.ai/sessions)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

---

See the [collection/agents/](./collection/agents/) directory for specific agent implementations.
