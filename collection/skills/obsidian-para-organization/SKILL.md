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