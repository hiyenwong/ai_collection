# Agent Creation Guide

This guide walks you through creating a custom OpenClaw agent.

## Prerequisites

- OpenClaw installed and configured
- Basic understanding of OpenClaw sessions
- A clear purpose for your agent

## Step 1: Define Agent Purpose

Start by answering these questions:

1. **What problem does this agent solve?**
2. **What tasks will it perform?**
3. **What tools does it need?**
4. **What model is best suited?**
5. **How should it communicate results?**

### Example: Research Agent

**Purpose:** Research specific topics and provide comprehensive summaries

**Tasks:**
- Search the web for information
- Read and analyze documents
- Synthesize findings into reports
- Provide citations and sources

**Tools:** web_search, web_fetch, memory, read, write

**Model:** claude-opus-4.5 (for deep reasoning)

**Communication:** Auto-deliver results to main session

## Step 2: Create Agent Directory

```bash
mkdir -p collection/agents/research-agent
cd collection/agents/research-agent
```

## Step 3: Create AGENT.md

Create the main agent definition file:

```markdown
# Research Agent

## Purpose
An autonomous research agent that investigates topics, gathers information from multiple sources, and produces comprehensive reports with citations.

## Model
- **Primary:** claude-opus-4.5
- **Alternative:** claude-sonnet-4.5
- **Fallback:** claude-haiku-4.5

## Tools
- web_search: Search for information
- web_fetch: Fetch and extract content
- memory_search: Search memory for context
- memory_get: Retrieve specific memory entries
- read: Read local files
- write: Save reports and findings

## Skills
- summarize: Content summarization
- oracle: Advanced reasoning and analysis

## System Prompt
```
You are a Research Agent specializing in comprehensive investigation and synthesis of information.

Your process:
1. Analyze the research request thoroughly
2. Identify key questions and search terms
3. Search multiple sources for relevant information
4. Read and analyze documents in depth
5. Synthesize findings into a coherent report
6. Provide citations for all claims
7. Note conflicting information and uncertainties

Always:
- Use multiple sources to verify information
- Clearly distinguish between facts and opinions
- Provide timestamps and source URLs
- Highlight gaps or limitations in available information
- Organize findings logically with clear headings

Your reports should include:
- Executive summary
- Key findings
- Detailed analysis
- Sources and citations
- Conclusion and recommendations
```

## Activation
This agent is spawned manually via sessions_spawn with specific research tasks.

## Usage Examples

### Basic Research
```python
sessions_spawn(
    task="Research the latest developments in quantum computing and create a comprehensive report",
    agentId="research-agent",
    model="claude-opus-4.5",
    thinking="high",
    deliver=true
)
```

### Structured Research
```python
sessions_spawn(
    task="""
    Research the following topic with these parameters:

    Topic: Artificial Intelligence in Healthcare

    Focus areas:
    1. Current applications and use cases
    2. Major companies and startups in the space
    3. Regulatory landscape and ethical considerations
    4. Future trends and predictions

    Output format: Markdown report with citations
    """,
    agentId="research-agent",
    model="claude-opus-4.5",
    thinking="high",
    deliver=true
)
```

## Configuration
```json
{
    "agentId": "research-agent",
    "model": "claude-opus-4.5",
    "thinking": "high",
    "timeoutSeconds": 1800,
    "tools": ["web_search", "web_fetch", "memory", "read", "write"],
    "skills": ["summarize", "oracle"],
    "deliver": true,
    "cleanup": "keep"
}
```

## Best Practices
- Use multiple search terms for comprehensive coverage
- Verify information across sources
- Provide clear citations with URLs
- Structure reports with clear headings
- Note limitations and uncertainties
- Keep reports concise while being thorough

## Examples
See the `examples/` directory for sample research reports.

## Notes
- Research quality depends on source quality
- Some information may be outdated
- Always verify critical information
- Consider the timeliness of sources
```

## Step 4: Add Examples

Create example usage scenarios:

```bash
mkdir -p examples
cat > examples/basic-research.md << 'EOF'
# Example: Basic Research Request

## Task
"Research the history of renewable energy and create a summary"

## Agent Process
1. Analyzed request: History of renewable energy
2. Identified search terms: "renewable energy history", "solar power evolution", "wind energy timeline"
3. Searched multiple sources
4. Read 12 documents from academic, industry, and government sources
5. Synthesized findings into report

## Output
```
# Renewable Energy: A Historical Overview

## Executive Summary
Renewable energy has evolved from small-scale applications to a major global industry...

## Key Findings
- Solar photovoltaic technology originated in 1954 at Bell Labs
- First wind turbine for electricity generation built in 1887
- Global renewable capacity has grown 300% since 2010...

## Detailed Analysis
[...]

## Sources
- International Energy Agency (2024): [URL]
- NREL Historical Review: [URL]
- United Nations Climate Report: [URL]
```
EOF
```

## Step 5: Add Assets (Optional)

Include helpful resources:

```bash
mkdir -p assets
# Add research templates, citation guides, etc.
```

## Step 6: Update Documentation

Update the main AGENTS.md to include your new agent:

```markdown
## Available Agents

### Research Agent
- **Location:** `collection/agents/research-agent/`
- **Purpose:** Comprehensive research and reporting
- **Model:** claude-opus-4.5
- **Tools:** web_search, web_fetch, memory, read, write

[...other agents...]
```

## Step 7: Test Your Agent

```python
# Test with a simple task
sessions_spawn(
    task="Research the current state of electric vehicle adoption in China and provide a summary",
    agentId="research-agent",
    model="claude-opus-4.5",
    thinking="high",
    deliver=true
)
```

## Advanced: Agent Specialization

You can create specialized variants of agents:

### Research Agent Variants

**Industry Research Agent:**
- Focus on specific industries
- Use industry-specific databases
- Market analysis specialization

**Academic Research Agent:**
- Focus on academic sources
- Literature review expertise
- Citation formatting (APA, MLA, etc.)

**Technical Research Agent:**
- Deep technical documentation
- Code analysis capabilities
- API documentation research

## Agent Configuration Reference

### Model Selection
| Model | Use Case | Speed | Cost |
|-------|----------|-------|------|
| claude-haiku-4.5 | Simple queries, quick tasks | Fast | Low |
| claude-sonnet-4.5 | General tasks, balanced | Medium | Medium |
| claude-opus-4.5 | Complex reasoning, research | Slow | High |

### Thinking Levels
- **low:** Quick responses, minimal reasoning
- **medium:** Balanced reasoning and speed
- **high:** Deep analysis, thorough research

### Timeout Guidelines
- Quick tasks: 60-120 seconds
- Medium tasks: 300-600 seconds
- Research tasks: 1800+ seconds
- Long-running: 3600+ seconds

### Cleanup Strategy
- **delete:** Remove session after completion (saves storage)
- **keep:** Keep session for reference (useful for debugging)

## Troubleshooting

### Agent Not Starting
- Check agentId matches directory name
- Verify configuration is valid JSON
- Check gateway is running

### Agent Fails Tasks
- Review system prompt clarity
- Verify tool permissions
- Increase timeout if needed
- Check model availability

### Results Not Delivered
- Set `deliver=true` in configuration
- Verify message channel is configured
- Check agent logs for errors

## Resources

- [OpenClaw Sessions API](https://docs.openclaw.ai/sessions)
- [OpenClaw Agent Configuration](https://docs.openclaw.ai/agents/config)
- [Claude Model Comparison](https://claude.com/models)

---

Next: [Skill Creation Guide](../skills/creation-guide.md)
