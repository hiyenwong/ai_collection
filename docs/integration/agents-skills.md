# Agents and Skills Integration Guide

This guide explains how OpenClaw agents and skills work together to create powerful AI assistants.

## Relationship Between Agents and Skills

```
┌─────────────────────────────────────────────────────────┐
│                    Main Session                      │
│  (User → Agent → OpenClaw → Tools/Skills)        │
└─────────────────────────────────────────────────────────┘
                          │
                          │ sessions_spawn
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Sub-Agent Session (Isolated)              │
│  ┌─────────────────────────────────────────────────┐  │
│  │         Agent System Prompt                    │  │
│  │  (Role, behavior, instructions)              │  │
│  └─────────────────────────────────────────────────┘  │
│                          │                          │
│                          │ User message             │
│                          ▼                          │
│  ┌─────────────────────────────────────────────────┐  │
│  │    Skills (Triggered by keywords)             │  │
│  │  ┌──────────────┐  ┌──────────────┐        │  │
│  │  │ Skill A      │  │ Skill B      │  ...    │  │
│  │  │ (read SKILL) │  │ (read SKILL) │        │  │
│  │  └──────────────┘  └──────────────┘        │  │
│  └─────────────────────────────────────────────────┘  │
│                          │                          │
│                          ▼                          │
│  ┌─────────────────────────────────────────────────┐  │
│  │              Tools (Direct Use)                 │  │
│  │  exec, read, write, web_search, etc.          │  │
│  └─────────────────────────────────────────────────┘  │
│                          │                          │
│                          ▼                          │
│                    Results/Response                 │
└─────────────────────────────────────────────────────────┘
```

## How They Work Together

### 1. Agent Context
An agent provides:
- **System prompt**: Defines role and personality
- **Model selection**: Optimized for specific tasks
- **Default tools**: Core tools always available
- **Thinking level**: How deeply to analyze

### 2. Skill Triggers
Skills are activated when:
- User message contains trigger keywords
- Agent needs specialized behavior
- Task requires specific workflow

### 3. Tool Usage
Both agents and skills can:
- Use built-in tools directly
- Call external CLIs via `exec`
- Read/write files
- Make API calls

## Integration Patterns

### Pattern 1: Agent with Skills

**Use Case:** Agent has specialized capabilities

```python
# Spawn agent with specific skills
sessions_spawn(
    task="Create a comprehensive report on market trends",
    agentId="research-agent",
    model="claude-opus-4.5",
    skills=["summarize", "web-search"]  # Agent will use these skills
)
```

**Flow:**
1. Agent spawns with system prompt
2. User request triggers task
3. Agent detects "summarize" or "web-search" keywords
4. Relevant skills are loaded
5. Agent follows skill instructions
6. Results delivered

### Pattern 2: Agent with Tool Wrapper Skills

**Use Case:** Agent needs to use external tools

```python
# Agent uses apple-notes skill
sessions_spawn(
    task="Create a note about my meeting agenda",
    agentId="personal-assistant",
    skills=["apple-notes"]
)
```

**Flow:**
1. Agent receives task
2. "note" keyword triggers `apple-notes` skill
3. Agent reads skill instructions
4. Agent uses `exec` to run `memo` CLI
5. Agent confirms note creation

### Pattern 3: Skill Chaining

**Use Case:** Multiple skills for complex task

```python
# Research + Summarize + Write Report
sessions_spawn(
    task="""
    Research the latest AI developments,
    summarize key findings,
    and create a markdown report
    """,
    agentId="researcher",
    skills=["web-search", "summarize", "obsidian"]
)
```

**Flow:**
1. Agent identifies three subtasks
2. Each subtask triggers different skill
3. Skills are used sequentially or in parallel
4. Results combined into final report

### Pattern 4: Agent Spawning Agents

**Use Case:** Multi-agent orchestration

```python
# Main agent spawns specialized sub-agents
sessions_spawn(
    task="Manage project: research, code, and documentation",
    agentId="project-manager",
    thinking="high"
)
```

**In Project Manager Agent:**
```python
# Spawn research sub-agent
sessions_spawn(task="Research user authentication patterns", agentId="researcher")

# Spawn coding sub-agent
sessions_spawn(task="Implement authentication", agentId="developer", skills=["coding-agent"])

# Spawn documentation sub-agent
sessions_spawn(task="Document API", agentId="writer", skills=["obsidian"])
```

**Flow:**
1. Project Manager receives task
2. Breaks into subtasks
3. Spawns specialized agents for each
4. Each agent may use their own skills
5. Results collected and delivered

## Best Practices

### 1. Clear Separation

**Agents:** Define behavior and high-level instructions
**Skills:** Define specific, repeatable workflows

✅ Good:
```markdown
Agent: "You are a research specialist. Use research skills when gathering information."
Skill: "When researching, search multiple sources and cite everything."
```

❌ Bad:
```markdown
Agent: "You do research by searching web and citing sources."
Skill: "When researching, follow agent's instructions."
```

### 2. Skill Activation Triggers

Use specific, uncommon phrases:

✅ Good Triggers:
- `"create a note"` for apple-notes
- `"send to slack"` for slack
- `"extract frames"` for video-frames

❌ Bad Triggers:
- `"create"` - too common
- `"send"` - too common
- `"extract"` - too common

### 3. Agent Specialization

Create agents for specific domains:

✅ Good Agents:
- `research-agent`: Academic research
- `code-reviewer`: Code quality
- `data-analyst`: Data processing
- `writer`: Content creation

❌ Too Generic:
- `assistant`: Does everything
- `helper`: Not specific enough

### 4. Skill Granularity

Skills should be focused:

✅ Good Skills:
- `apple-notes`: Notes management
- `apple-reminders`: Reminders management
- `feishu-doc`: Document operations

❌ Too Broad:
- `apple-apps`: All Apple apps combined
- `productivity`: Too vague

### 5. Error Handling

Both agents and skills should handle errors:

**Agent Error Handling:**
```markdown
## Error Handling
If a sub-agent fails:
  1. Log the error
  2. Try alternative approach
  3. Report to user with clear message
```

**Skill Error Handling:**
```markdown
## Error Handling
If tool command fails:
  1. Check if tool is installed
  2. Verify permissions
  3. Suggest manual alternative
  4. Report specific error
```

## Example: Complete Workflow

Let's trace a complete workflow with agents and skills:

### User Request
```
"Research the latest in quantum computing,
summarize the findings,
and create a note with the summary."
```

### Step 1: Main Session
```python
sessions_spawn(
    task="Research quantum computing, summarize, and create a note",
    agentId="personal-researcher",
    model="claude-opus-4.5",
    thinking="high"
)
```

### Step 2: Personal Researcher Agent Activates
Agent reads system prompt:
```markdown
You are a Personal Researcher. You combine research, summarization,
and personal organization. Use research and summarization skills,
then create notes for personal reference.
```

### Step 3: Skill 1 - Research Skill Triggered
"research" keyword triggers research skill

Agent follows skill instructions:
```python
# Web searches
web_search(query="quantum computing 2025 developments")
web_search(query="quantum computing breakthroughs")

# Read articles
web_fetch(url="...")

# Synthesize findings
```

### Step 4: Skill 2 - Summarize Skill Triggered
"summarize" keyword triggers summarize skill

Agent follows skill instructions:
```markdown
1. Extract key points
2. Organize logically
3. Create executive summary
4. Include citations
```

### Step 5: Skill 3 - Apple Notes Skill Triggered
"note" keyword triggers apple-notes skill

Agent follows skill instructions:
```bash
# Create note
memo create "Quantum Computing Research" [summary content]
```

### Step 6: Deliver Results
Agent reports back:
```
✓ Researched 12 articles on quantum computing
✓ Created 3-page summary with 8 citations
✓ Saved note: "Quantum Computing Research"

Summary highlights:
- Recent breakthroughs in qubit stability
- New quantum algorithms announced
- Industry adoption timeline updated
```

## Testing Integration

### Test Agent-Skill Combination

```python
# Test research agent with summarization skill
sessions_spawn(
    task="Research AI ethics and create a summary",
    agentId="research-agent",
    skills=["summarize"]
)

# Verify:
# 1. Agent uses research patterns
# 2. Summarize skill is triggered
# 3. Summary follows skill guidelines
# 4. Results are delivered
```

### Test Multi-Skill Workflow

```python
# Test agent with multiple skills
sessions_spawn(
    task="Get weather, create a note about it",
    agentId="assistant",
    skills=["weather", "apple-notes"]
)

# Verify:
# 1. Weather skill gets weather
# 2. Note skill creates note
# 3. Both skills work together
```

### Test Agent Spawning

```python
# Test agent spawning sub-agents
sessions_spawn(
    task="Orchestrate a small project",
    agentId="project-manager",
    thinking="high"
)

# Verify:
# 1. Main agent breaks down task
# 2. Sub-agents are spawned correctly
# 3. Results are collected
# 4. Final report is delivered
```

## Common Pitfalls

### 1. Skill Conflicts
Two skills have similar trigger keywords

**Solution:** Make triggers more specific

### 2. Agent Overload
Agent tries to do too much

**Solution:** Create more specialized agents

### 3. Skill Dependency
Skill assumes agent has specific knowledge

**Solution:** Include context in SKILL.md

### 4. Tool Conflicts
Two skills use same tool differently

**Solution:** Document tool usage in skill

### 5. Memory Issues
Too many skills loaded at once

**Solution:** Only load relevant skills

## Advanced Patterns

### Pattern: Skill with Built-in Agent
Skill that temporarily spawns an agent

```markdown
## Instructions for Agents
When this skill is activated:
1. If task is complex, spawn specialized agent:
   sessions_spawn(task=subtask, agentId="specialized-agent")
2. Agent returns results
3. Continue with skill workflow
```

### Pattern: Conditional Skill Loading
Load skills based on task complexity

```python
# Simple task - no skills needed
if task_complexity == "low":
    sessions_spawn(task=simple_task, agentId="quick-assistant")

# Complex task - load multiple skills
else:
    sessions_spawn(
        task=complex_task,
        agentId="expert",
        skills=["research", "summarize", "coding-agent"]
    )
```

### Pattern: Skill Feedback Loop
Skill results trigger agent to load another skill

```
Task → Skill A → Results → Agent detects pattern → Loads Skill B
```

## Resources

- [OpenClaw Agents Documentation](https://docs.openclaw.ai/agents)
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/skills)
- [Agent Creation Guide](../agents/creation-guide.md)
- [Skill Creation Guide](../skills/creation-guide.md)

---

Happy agent and skill building! 🤖✨
