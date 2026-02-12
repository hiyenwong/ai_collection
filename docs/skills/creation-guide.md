# Skill Creation Guide

This guide walks you through creating a custom OpenClaw skill.

## Prerequisites

- OpenClaw installed and configured
- A clear understanding of the task type to automate
- External tools or APIs ready (if applicable)

## Step 1: Define Skill Purpose

Start by answering these questions:

1. **What task type does this skill handle?**
2. **What triggers should activate the skill?**
3. **What tools or external dependencies does it use?**
4. **What instructions does the agent need?**
5. **Are there common edge cases to handle?**

### Example: Slack Integration Skill

**Purpose:** Handle Slack API operations for sending messages, creating channels, and managing users

**Triggers:** "slack", "send to slack", "slack channel", "slack message"

**Tools:** exec (for slack CLI), web_fetch (for API docs)

**Instructions:** How to use Slack CLI, API endpoints, authentication, error handling

**Edge Cases:** Rate limiting, permission errors, invalid channels

## Step 2: Create Skill Directory

```bash
mkdir -p collection/skills/slack
cd collection/skills/slack
```

## Step 3: Create SKILL.md

Create the main skill definition file:

```markdown
# Slack Integration

## Description
Manage Slack workspaces via Slack CLI and API. Supports sending messages, creating channels, inviting users, and workspace management.

## Activation Keywords
- slack
- send to slack
- slack channel
- slack message
- slack invite
- slack workspace

## Tools Used
- exec: Run slack CLI commands
- web_fetch: Reference Slack API documentation
- read: Read skill configuration and templates

## Installation

### Install Slack CLI
```bash
# Via npm
npm install -g slack-cli

# Or via Homebrew
brew install slack-cli

# Verify installation
slack --version
```

### Authenticate
```bash
slack login
# Follow browser authentication flow
```

### Verify Setup
```bash
slack workspaces list
slack channels list
```

## Usage Patterns

### Sending Messages

**Simple Message:**
```bash
slack message send --channel "#general" --text "Hello team!"
```

**Message with Attachments:**
```bash
slack message send \
  --channel "#updates" \
  --text "Weekly report" \
  --file report.pdf
```

**DM to User:**
```bash
slack message send --user "@john" --text "Meeting at 3pm"
```

### Channel Management

**Create Channel:**
```bash
slack channel create --name "project-alpha" --private
```

**Invite to Channel:**
```bash
slack channel invite --channel "#project-alpha" --user "@jane,@mike"
```

**List Channels:**
```bash
slack channels list
```

### User Management

**Invite User to Workspace:**
```bash
slack invite --email "newuser@company.com" --channel "#general"
```

**List Users:**
```bash
slack users list
```

## Instructions for Agents

When user mentions Slack operations:

1. **Verify Authentication**
   - Run `slack workspaces list` to check auth
   - If not authenticated, instruct user to run `slack login`

2. **Determine Operation**
   - Identify if user wants to send message, manage channels, or other action
   - Ask for missing required parameters (channel, message, etc.)

3. **Execute Command**
   - Construct appropriate slack CLI command
   - Use `exec` with pty=true for interactive prompts

4. **Handle Errors**
   - Rate limiting: Wait and retry
   - Permission errors: Check workspace permissions
   - Invalid channel: List available channels

5. **Confirm Success**
   - Verify operation completed
   - Provide feedback to user

## Context Files

The skill uses these context files when available:

### SLACK_SETTINGS.md
```markdown
# Slack Settings

## Default Channel
#general

## Default Workspace
acme-corp

##常用 Channels
- #general: General discussion
- #announcements: Company announcements
- #engineering: Engineering team
```

## Error Handling

### Rate Limiting
```
If you see "rate_limited" error:
  Wait 60 seconds
  Retry the command
  Inform user about delay
```

### Authentication Issues
```
If you see "not authenticated" error:
  Ask user to run: slack login
  Wait for authentication to complete
  Retry the command
```

### Invalid Channel
```
If channel not found:
  Run: slack channels list
  Show available channels to user
  Ask user to select correct channel
```

### Permission Errors
```
If permission denied:
  Explain the permission needed
  Suggest contacting workspace admin
  Or ask user to try with different scope
```

## Configuration

### Environment Variables (Optional)
```bash
export SLACK_DEFAULT_CHANNEL="#general"
export SLACK_DEFAULT_WORKSPACE="my-workspace"
export SLACK_TIMEOUT=30
```

### Workspace Config
```bash
# Set default workspace
slack workspaces set-default my-workspace
```

## Advanced Usage

### Webhooks
For more advanced integration, use Slack webhooks:

```bash
# Create webhook
slack webhook create --channel "#alerts" --name "monitoring"

# Use webhook
curl -X POST $SLACK_WEBHOOK_URL \
  -H 'Content-Type: application/json' \
  -d '{"text":"Alert: Server down"}'
```

### Bulk Operations
Send messages to multiple channels:

```bash
for channel in #general #engineering #support; do
  slack message send --channel $channel --text "Important update"
done
```

## Limitations

- Rate limits: Slack API has strict rate limits
- Permissions: Some operations require workspace admin
- Channels: Cannot DM users not in workspace
- Files: Large files may fail to upload

## Best Practices

1. **Always verify authentication** before operations
2. **Ask before destructive actions** (delete channel, kick user)
3. **Check permissions** if operations fail
4. **Provide feedback** on all operations
5. **Handle rate limits** gracefully

## Examples

### Example 1: Send Announcement
```
User: "Send an announcement to all team channels about the new feature launch"

Agent Process:
1. Identify: Message send operation
2. Check auth: slack workspaces list ✓
3. Get channels: slack channels list
4. Send to each channel:
   - #general ✓
   - #engineering ✓
   - #product ✓
5. Confirm: Sent to 3 channels
```

### Example 2: Create Private Channel
```
User: "Create a private channel for the alpha project team"

Agent Process:
1. Identify: Channel creation
2. Get details: Channel name "alpha-project", private
3. Execute: slack channel create --name alpha-project --private
4. Invite team members (if provided)
5. Confirm: Channel created and ready
```

## Troubleshooting

### CLI Not Found
```bash
# Install slack-cli
npm install -g slack-cli
```

### Authentication Issues
```bash
# Re-authenticate
slack login --reauth
```

### Channel Not Found
```bash
# List available channels
slack channels list
```

### Rate Limiting
Wait 60 seconds before retrying operations.

## Resources

- [Slack CLI GitHub](https://github.com/slackapi/slack-cli)
- [Slack API Docs](https://api.slack.com/docs)
- [Slack CLI Commands](https://github.com/slackapi/slack-cli#commands)

## Related Skills
- feishu: Feishu/Lark integration
- discord: Discord bot operations
- teams: Microsoft Teams integration
```

## Step 4: Add Reference Documentation

```bash
mkdir -p references
cat > references/api-endpoints.md << 'EOF'
# Slack API Endpoints Reference

## Chat API

### Post Message
```
POST /api/chat.postMessage
```

**Parameters:**
- channel: Channel ID or name
- text: Message text
- attachments: Array of attachments
- blocks: Block Kit blocks

**Example:**
```bash
curl -X POST https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer xoxb-token" \
  -d '{
    "channel": "#general",
    "text": "Hello, World!"
  }'
```
EOF
```

## Step 5: Add Examples

```bash
mkdir -p examples
cat > examples/basic-usage.md << 'EOF'
# Example: Basic Slack Integration

## Scenario
User wants to send a message to a Slack channel.

## Conversation
```
User: Send a message to #general saying "Welcome to the team!"

Agent: I'll send that message to #general for you.

[Executes: slack message send --channel "#general" --text "Welcome to the team!"]

Agent: ✓ Message sent successfully to #general.
```

## Command Executed
```bash
slack message send --channel "#general" --text "Welcome to the team!"
```

## Output
```
✓ Message sent to #general (Timestamp: 1234567890.123456)
```
EOF
```

## Step 6: Add Scripts (Optional)

```bash
mkdir -p scripts
cat > scripts/install.sh << 'EOF'
#!/bin/bash
# Slack Skill Installation Script

echo "Installing Slack CLI..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is required but not installed."
    echo "Install from https://nodejs.org/"
    exit 1
fi

# Install Slack CLI
npm install -g slack-cli

# Verify installation
if command -v slack &> /dev/null; then
    echo "✓ Slack CLI installed successfully"
    slack --version
else
    echo "✗ Installation failed"
    exit 1
fi

echo ""
echo "Next step: Run 'slack login' to authenticate"
EOF

chmod +x scripts/install.sh
```

## Step 7: Update Documentation

Update main SKILLS.md to include your new skill:

```markdown
## Available Skills

### Slack Integration
- **Location:** `collection/skills/slack/`
- **Purpose:** Slack workspace management
- **Triggers:** slack, send to slack, slack channel
- **Tools:** exec, web_fetch, read

[...other skills...]
```

## Step 8: Test Your Skill

1. **Trigger the skill:**
   ```
   User: "Send a test message to Slack"
   ```

2. **Verify activation:**
   - Check if agent reads SKILL.md
   - Confirm it follows instructions

3. **Test operations:**
   - Send a message
   - List channels
   - Try edge cases

4. **Iterate and refine:**
   - Add missing error handling
   - Improve instructions
   - Add more examples

## Skill Template

Use this template for new skills:

```markdown
# Skill Name

## Description
Brief description (1-2 sentences) of what this skill does.

## Activation Keywords
- keyword1
- keyword2
- keyword3

## Tools Used
- tool1: Description of usage
- tool2: Description of usage

## Installation (if applicable)
Instructions for installing dependencies.

## Usage Patterns

### Operation 1
```bash
# Command example
```

### Operation 2
```bash
# Command example
```

## Instructions for Agents
Step-by-step instructions for agents to follow.

## Context Files
Files the skill uses for configuration.

## Error Handling
How to handle common errors.

## Examples
Real-world usage examples.

## Resources
Links to documentation, APIs, etc.

## Related Skills
List of related skills.
```

## Best Practices

### 1. Clear Triggers
- Use specific, uncommon phrases
- Test triggers don't conflict with general conversation
- Include variations and synonyms

### 2. Comprehensive Instructions
- Cover common use cases
- Address edge cases
- Provide examples for each operation

### 3. Error Handling
- Document common errors
- Provide recovery steps
- Suggest user actions when needed

### 4. Testing
- Test with various prompts
- Verify edge cases work
- Get feedback from actual usage

### 5. Documentation
- Keep SKILL.md focused
- Put detailed info in references/
- Use examples/ for illustration

## Troubleshooting

### Skill Not Activating
- Check trigger keywords in user message
- Verify SKILL.md path is correct
- Check OpenClaw skill directories

### Agent Not Following Instructions
- Ensure instructions are clear and explicit
- Check for conflicting skills
- Simplify complex instructions

### Tools Failing
- Verify external tools are installed
- Check API keys and credentials
- Test tool usage manually

## Resources

- [OpenClaw Skills Guide](https://docs.openclaw.ai/skills)
- [Skill Hub](https://clawhub.com)
- [Creating Skills](https://docs.openclaw.ai/skills/creating)

---

Next: [Integration Guide](../integration/agents-skills.md)
