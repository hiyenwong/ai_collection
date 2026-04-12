#!/bin/bash

# Script to create multi-tool agent compatibility files for all agents
# in the AI Collection

BASE_DIR="/Users/hiyenwong/ai_github/ai_collection/collection/agents"

# Create INSTRUCTIONS files with agent-specific content
for agent_dir in "$BASE_DIR"/*/; do
    agent_name=$(basename "$agent_dir")
    
    # Skip template directory
    if [[ "$agent_name" == "template" ]]; then
        continue
    fi
    
    echo "Processing agent: $agent_name"
    
    # Create directories if they don't exist
    mkdir -p "$agent_dir/.claude"
    mkdir -p "$agent_dir/.hermes"
    mkdir -p "$agent_dir/.codex"
    mkdir -p "$agent_dir/.github"
    mkdir -p "$agent_dir/examples"
    
    # Check if AGENT.md exists
    if [[ ! -f "$agent_dir/AGENT.md" ]]; then
        echo "  Warning: No AGENT.md found for $agent_name"
        continue
    fi
    
    # Extract agent purpose from AGENT.md (first line after ---)
    agent_purpose=$(grep -A 1 "^description:" "$agent_dir/AGENT.md" 2>/dev/null | tail -1 | sed 's/.*description: *//')
    
    # If no description found, try to extract from first line
    if [[ -z "$agent_purpose" ]]; then
        agent_purpose="AI agent for specialized tasks"
    fi
    
    # Create Claude Code INSTRUCTIONS
    cat > "$agent_dir/.claude/INSTRUCTIONS.md" << EOF
# Claude Code Instructions

This agent is designed to work with Claude Code.

## Agent Details

- **Agent Name**: $agent_name
- **Purpose**: $agent_purpose
- **Key Tools**: exec, read, write, edit

## Usage

When user wants to use this agent with Claude Code:

1. Navigate to the agent directory
2. Use the AGENT.md file for context
3. Use soul.md for personality guidance
4. Check examples/ for use cases

## Integration

This agent is part of the AI Collection. To integrate:

\`\`\`bash
cd /path/to/ai_collection
# The agent is available at collection/agents/$agent_name/
\`\`\`

## Configuration

No special configuration needed. Claude Code will automatically use the AGENT.md and soul.md files.

---

*For more information, see the AI Collection README*
EOF

    # Create Hermes INSTRUCTIONS
    cat > "$agent_dir/.hermes/INSTRUCTIONS.md" << EOF
# Hermes Agent Instructions

This agent is designed to work with Hermes Agent.

## Agent Details

- **Agent Name**: $agent_name
- **Purpose**: $agent_purpose
- **Key Tools**: exec, read, write, edit

## Architecture

Hermes Agent uses this agent as a specialized worker. The agent should:

1. **Read the AGENT.md file** for context
2. **Read soul.md** for personality and voice
3. **Follow task instructions** from the planner

## Integration

This agent is part of the AI Collection. To integrate:

\`\`\`bash
# The agent is available at:
/path/to/ai_collection/collection/agents/$agent_name/

# Add to Hermes config:
{
  "agents": {
    "$agent_name": {
      "system_prompt": "Read /path/to/ai_collection/collection/agents/$agent_name/AGENT.md"
    }
  }
}
\`\`\`

## Best Practices

1. **Always read AGENT.md first** for context
2. **Use soul.md** to maintain consistent personality
3. **Check examples/** for task patterns
4. **Use read/write tools** for file operations

---

*For more information, see the AI Collection README*
EOF

    # Create Codex INSTRUCTIONS
    cat > "$agent_dir/.codex/INSTRUCTIONS.md" << EOF
# Codex Instructions

This agent is designed to work with OpenAI Codex.

## Agent Details

- **Agent Name**: $agent_name
- **Purpose**: $agent_purpose
- **Key Tools**: exec, read, write, edit

## Usage

When user wants to use this agent with Codex:

\`\`\`bash
codex "Use $agent_name to {task_description}"
\`\`\`

## Integration

This agent is part of the AI Collection. To integrate:

\`\`\`bash
cd /path/to/ai_collection
# The agent is available at collection/agents/$agent_name/
\`\`\`

---

*For more information, see the AI Collection README*
EOF

    # Create Copilot CLI INSTRUCTIONS
    cat > "$agent_dir/.github/copilot-instructions.md" << EOF
# GitHub Copilot CLI Instructions

This agent is designed to work with GitHub Copilot CLI.

## Agent Details

- **Agent Name**: $agent_name
- **Purpose**: $agent_purpose
- **Key Tools**: exec, read, write, edit

## Usage

When user wants to use this agent with Copilot CLI:

\`\`\`bash
copilot "{task_description} using $agent_name"
\`\`\`

## Configuration

Add this agent to Copilot CLI configuration:

\`\`\`json
{
  "agents": {
    "$agent_name": {
      "description": "$agent_purpose",
      "tools": "exec, read, write, edit"
    }
  }
}
\`\`\`

## Best Practices

1. **Use clear task descriptions**
2. **Reference agent purpose**
3. **Leverage agent's specialized tools**

---

*For more information, see the AI Collection README*
EOF

    # Create GEMINI.md
    cat > "$agent_dir/GEMINI.md" << EOF
# Gemini CLI Instructions

This agent is designed to work with Google Gemini CLI.

## Agent Details

- **Agent Name**: $agent_name
- **Purpose**: $agent_purpose
- **Key Tools**: exec, read, write, edit

## Usage

Use Gemini in one-shot mode:

\`\`\`bash
gemini "Use $agent_name to {task_description}"
\`\`\`

## Integration

This agent is part of the AI Collection. To integrate:

\`\`\`bash
cd /path/to/ai_collection
# The agent is available at collection/agents/$agent_name/
\`\`\`

### System Prompt

For advanced Gemini CLI use, set system prompt from AGENT.md:

\`\`\`bash
gemini --system-prompt "Read /path/to/ai_collection/collection/agents/$agent_name/AGENT.md" -- "{task_description}"
\`\`\`

---

*For more information, see the AI Collection README*
EOF

    echo "  Created multi-tool compatibility files for $agent_name"
done

echo ""
echo "Done! All agents now have multi-tool compatibility files."
