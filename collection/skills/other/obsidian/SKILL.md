---
name: obsidian
description: Read, search, and create notes in the Obsidian vault.
---

# Obsidian Vault

**Location:** `~/Library/Mobile Documents/iCloud~md~obsidian/Documents`

This is the iCloud-synced primary vault. The vault uses PARA organization method with the following structure:
- `00 - Inbox/` - Temporary notes
- `01 - Daily Notes/` - Daily notes organized by year
- `02 - Projects/` - Active projects
- `03 - Areas/` - Ongoing areas of responsibility (e.g., AI Agent Research)
- `04 - Resources/` - Reference materials (e.g., Papers)
- `05 - Archives/` - Completed/inactive items
- `99 - Meta/` - Templates, MOC, indexes
- `OpenAI Research/` - OpenAI-specific research
- `Research Tracking/` - Research tracking notes
- `engineering/` - Engineering notes
- `notes/` - General notes
- `stock/` - Stock-related notes

Note: Vault paths may contain spaces - always quote them.

## Read a note

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
cat "$VAULT/Note Name.md"
```

## List notes

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"

# All notes
find "$VAULT" -name "*.md" -type f

# In a specific folder
ls "$VAULT/Subfolder/"
```

## Search

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"

# By filename
find "$VAULT" -name "*.md" -iname "*keyword*"

# By content
grep -rli "keyword" "$VAULT" --include="*.md"
```

## Create a note

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
cat > "$VAULT/New Note.md" << 'ENDNOTE'
# Title

Content here.
ENDNOTE
```

## Append to a note

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
echo "
New content here." >> "$VAULT/Existing Note.md"
```

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## Activation Keywords

- "obsidian"
- "obsidian"
- "use obsidian"
- "obsidian help"
- "obsidian tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Obsidian usage
```
User: "Help me with obsidian"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed obsidian assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
