---
name: obsidian-para-organization
description: Organize Obsidian vault using PARA method (Projects, Areas, Resources, Archives)
triggers:
  - user asks to organize obsidian
  - user wants to structure notes
  - PARA method mentioned
---

# Obsidian PARA Organization

Organize Obsidian vault using the PARA method for scientific research and knowledge management.

## Directory Structure

```
Vault/
├── 00 - Inbox/           # Temporary capture
├── 01 - Daily Notes/     # YYYY/MM-DD.md format
├── 02 - Projects/        # Active projects with goals
├── 03 - Areas/           # Ongoing responsibilities
├── 04 - Resources/       # Reference materials
├── 05 - Archives/        # Completed/inactive
└── 99 - Meta/            # Templates, MOC, config
```

## Core Files

### README.md (Vault Home)
- Welcome message
- Quick start guide
- Recent updates
- Navigation links

### MOC (Map of Content)
- Central navigation hub
- Links to all major sections
- Recently modified notes

### Templates/
- Daily Note Template
- Paper Note Template
- Project Template
- Meeting Template

## Navigation System

1. **Bidirectional Links**: `[[Note Name]]`
2. **Tags**: #paper #agent-memory #orchestration
3. **MOC**: Central map linking everything
4. **Indexes**: Paper Index, Project Index

## Workflow

1. Capture → 00-Inbox/
2. Process → Move to appropriate folder
3. Daily → 01-Daily Notes/YYYY/MM-DD.md
4. Papers → 04-Resources/Papers/Topic/
5. Projects → 02-Projects/Name/

## Backlinks

- Always add to existing notes when relevant
- Use MOC for high-level navigation
- Tag consistently for filtering

## Activation Keywords

- "obsidian", "PARA", "organize notes", "vault organization", "note structure"

## Tools Used

- `Read` - Read existing notes
- `Write` - Create and update notes
- `Glob` - Find notes by pattern
- `Grep` - Search note content

## Instructions for Agents

1. Assess current vault structure if it exists
2. Create PARA directory structure if missing
3. Create core templates (Daily, Project, Paper, Meeting)
4. Set up MOC (Map of Content) as navigation hub
5. Guide user on workflow and best practices

## Examples

### Organize existing vault
```
User: "Organize my Obsidian vault with PARA method"
→ Check existing structure → Create directories → Create templates → Set up MOC
```

### Create project note
```
User: "Create a new project note for my research"
→ Create in 02-Projects/ → Use Project template → Link to MOC
```