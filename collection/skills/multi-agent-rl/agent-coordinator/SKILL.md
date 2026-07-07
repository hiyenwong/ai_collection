---
name: agent-coordinator
description: Agent coordinator for analyzing user questions, determining the most suitable agent or skill to answer, and coordinating multiple agents for complex tasks. Supports question classification, capability mapping, agent invocation, and result integration.
---

# Agent Coordinator

Intelligent agent coordinator for analyzing questions and selecting the most appropriate capabilities.

## Activation Keywords

Chinese:
- 使用 agent, 调用代理
- 最适合的 agent
- agent 协调, 多 agent 协作

English:
- use agent, call agent
- most suitable agent
- agent coordination
- multi-agent collaboration

## Tools Used

- agents_list: List available agents
- sessions_spawn: Call sub-agent or ACP
- read: Read agent and skill documentation
- memory_search: Search related knowledge

## Core Functionality

### 1. Question Analysis

**Analysis dimensions:**
- **Question type**: Knowledge query, data fetching, coding task, teaching task, analysis task, creative task
- **Domain**: Finance, programming, AI/ML, general
- **Complexity**: Simple (single step), Medium (multi-step sequential), Complex (multi-step with decisions)
- **Required capabilities**: Data fetching, data processing, code generation, visualization, analytical reasoning, teaching explanation

### 2. Capability Mapping

**Internal capabilities (Aerial itself):**
- Knowledge queries (general): Answer directly
- Self-improvement tasks: Answer directly
- Context management: Answer directly
- Communication collaboration: Answer directly
- Skill extraction: Answer directly
- Knowledge organization: Answer directly

**Skills (internal):**
- Chat history related: Session history priority check
- Agreements/commitments: Task commitment execution
- Execution priority: Immediate vs future configuration
- Unclear intent: Confirmation mechanism, paraphrase confirmation
- Complex tasks: Complete task lifecycle
- Code review: Teach Co-Founder
- Teaching/learning: Teach Co-Founder
- Skill pattern discovery: Skill Extractor
- History search: Chat History LanceDB

**External tools (via skills):**
- Stock data: akshare
- Stock analysis: stock-analysis
- Financial market: akshare + stock-analysis
- Stock technical indicators: stock-analysis

**Sub-agent / ACP invocation:**
- Coding tasks: coding-agent (ACP)
- Code review: github (gh)
- GitHub operations: github
- Complex code: copilot-cli
- Claude Code: claude-code
- OpenCode: opencode
- New feature development: coding-agent
- Large codebase refactoring: coding-agent
- PR review: github

### 3. Decision Process

```
User question
    ↓
Question analysis
    ├─ Question type?
    ├─ Domain?
    ├─ Complexity?
    └─ Required capabilities?
    ↓
Capability mapping
    ├─ Can I handle it?
    ├─ Is there a skill?
    ├─ Is there a tool?
    └─ Need to call agent?
    ↓
Select execution plan
    ├─ Plan 1: Answer myself (priority)
    ├─ Plan 2: Use skill
    ├─ Plan 3: Call tool
    └─ Plan 4: Call sub-agent
    ↓
Execute
    ├─ Execute according to selected plan
    ├─ Monitor execution process
    └─ Handle errors and exceptions
    ↓
Integrate results
    ├─ Organize execution results
    ├─ Explain analysis process
    └─ Provide follow-up suggestions
```

## Usage Patterns

### When to Enable This Skill

1. **Complex questions** that require multiple capabilities
2. **Cross-domain questions** that involve different areas
3. **Questions where the best approach is unclear**
4. **Requests that may benefit from specialized agents**

### Coordination Principles

#### 1. Prioritize self-handling
- Simple questions answered directly
- Use existing skills
- Avoid unnecessary agent calls

#### 2. Use skills appropriately
- Prioritize using existing skills
- Call agents when skills are insufficient
- Record skill usage

#### 3. Cautiously call sub-agents
- Complex coding tasks → coding-agent
- GitHub operations → github skill
- Large codebase tasks → specialized agent
- Monitor agent execution

#### 4. Integrate results
- Organize agent output
- Explain key parts
- Provide follow-up recommendations

## Decision Examples

### Example 1: Stock Analysis

**User**: "Help me analyze Ping An Bank (000001) recent performance"

**Analysis**:
- Type: Analysis task
- Domain: Finance
- Complexity: Medium
- Capabilities: Data fetching, data processing, analytical reasoning

**Decision**: Use akshare + stock-analysis skills

### Example 2: Code Review

**User**: "Review this code for issues"

**Analysis**:
- Type: Code task
- Domain: Programming
- Complexity: Medium
- Capabilities: Code understanding, problem identification

**Decision**: Use Teach Co-Founder skill (code review framework)

### Example 3: Coding Task

**User**: "Write a Python script to fetch data from API and save to database"

**Analysis**:
- Type: Code task
- Domain: Programming
- Complexity: High
- Capabilities: Code generation, API calls, database operations

**Decision**: Call coding-agent (ACP)

## Best Practices

1. **Avoid over-design** - Simple questions answered directly, don't over-analyze
2. **Monitor agent execution** - Monitor status when calling sub-agents
3. **Integrate output** - Organize agent output, don't just relay
4. **Record experience** - Record which situations require which agent
5. **Continuous optimization** - Optimize decision logic based on usage

## Limitations

- Limited to available agents and skills
- Agent execution may fail
- Integration of results may be incomplete
- Decision logic may need refinement

## Related Skills

- learned-skills: Skills extracted from events
- skill-extractor: Skill extraction capability
- teach-cofounder: Technical mentor skill

## References

- OpenClaw Agent Documentation
- ACP Harness Documentation

## Instructions for Agents

1. Read the task description carefully
2. Follow the step-by-step process
3. Use the appropriate tools
4. Verify the results

## Examples

### Example 1: Basic Usage

**User:** <example user request>

**Agent:** <example agent response>

### Example 2: Advanced Usage

**User:** <example user request>

**Agent:** <example agent response>
