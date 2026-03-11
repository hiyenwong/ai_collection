---
name: cursor-rules-importer
description: Import and convert cursor.directory rules into AgentSkills. Use when user wants to import cursor rules, convert .cursorrules to skills, or mentions cursor.directory, cursor rules import.
---

# Cursor Rules Importer

Convert `.cursorrules` files from cursor.directory into AgentSkills format.

## Overview

cursor.directory is a community-driven collection of AI coding rules. This skill helps import and convert these rules into the AgentSkills format for use with OpenClaw, Claude Code, and other AI tools.

## Activation Keywords

- cursor rules import
- import cursor rules
- cursor.directory
- .cursorrules to skill
- convert cursor rules

## Tools Used

- `read`: Read existing rules or skill files
- `write`: Create new skill files
- `exec`: Run conversion scripts
- `browser`: Access cursor.directory

## Cursor Rules Format

Cursor rules are plain text/markdown files with a specific structure:

```text
You are an expert in [domain].

[Code Style and Structure]
- Rule 1
- Rule 2

[Naming Conventions]
- Convention 1

[Best Practices]
- Practice 1
```

## AgentSkills Format

AgentSkills use YAML frontmatter + Markdown:

```yaml
---
name: skill-name
description: When to use this skill and what it does.
---

# Skill Title

[Instructions in Markdown]
```

## Conversion Rules

### 1. Name Generation

| Cursor Rule | AgentSkill Name |
|-------------|-----------------|
| `react-component-catalog` | `react-components` |
| `accessibility-guard` | `accessibility-wcag` |
| `front-end-cursor-rules` | `frontend-best-practices` |
| `chrome-extension-development` | `chrome-extension` |
| `typescript-electron-desktop-app-cursor-rules` | `electron-typescript` |

### 2. Description Generation

Extract key topics and create a description:

```yaml
description: Expert guidance for [domain]. Use when working with [technologies] for [tasks]. Triggers on keywords: [keywords].
```

### 3. Content Mapping

| Cursor Section | AgentSkill Section |
|----------------|-------------------|
| "You are an expert in..." | Move to description |
| Code Style and Structure | ## Code Style |
| Naming Conventions | ## Naming Conventions |
| Best Practices | ## Best Practices |
| Performance | ## Performance |
| Security | ## Security |

### 4. Code Examples

Preserve code examples but format them properly:

````markdown
```typescript
// ✅ Good
const value = useWatch({ name: 'field', control });

// ❌ Bad
const value = methods.watch();
```
````

## Conversion Process

### Step 1: Identify the Rule

Browse https://cursor.directory/rules to find the desired rule.

### Step 2: Extract Content

Copy the rule content from the page or API.

### Step 3: Generate Skill

Use the conversion script:

```bash
python scripts/convert_cursor_rule.py --url "https://cursor.directory/react-component-catalog" --output skills/
```

Or manually convert:

1. Create skill directory: `skill-name/`
2. Create `SKILL.md` with frontmatter
3. Add content sections
4. Optionally add `references/` for detailed docs

### Step 4: Validate

Run validation:

```bash
python scripts/validate_skill.py skills/skill-name/
```

## Example Conversion

### Input (cursor.directory rule):

```text
You are an expert in React component architecture and maintainability.

## Component Size Limits
| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Lines of code | < 150 | 150-300 | > 300 |
| Imports | < 20 | 20-35 | > 35 |
```

### Output (AgentSkill):

```yaml
---
name: react-components
description: Expert guidance for React component architecture, maintainability, and best practices. Use when building React components, reviewing component structure, or optimizing component performance. Triggers on: React component, component architecture, React best practices, component size, React hooks.
---

# React Components

Expert guidance for React component architecture and maintainability.

## Component Size Limits

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Lines of code | < 150 | 150-300 | > 300 |
| Imports | < 20 | 20-35 | > 35 |
| useState calls | < 4 | 4-6 | > 6 |
| useEffect calls | < 3 | 3-5 | > 5 |

If exceeded: Stop and suggest decomposition.
```

## Popular Rules to Import

| Category | Rule | Skill Name |
|----------|------|------------|
| TypeScript | react-component-catalog | react-components |
| TypeScript | accessibility-guard | accessibility-wcag |
| TypeScript | front-end-cursor-rules | frontend-best-practices |
| TypeScript | chrome-extension-development | chrome-extension |
| TypeScript | typescript-electron-desktop-app | electron-typescript |
| React | expo-react-native-typescript | expo-react-native |
| Python | python-best-practices | python-best-practices |
| Next.js | nextjs-app-router | nextjs-app-router |

## Batch Import

Import all rules from a category:

```bash
python scripts/batch_import.py --category typescript --output skills/
```

Import specific rules:

```bash
python scripts/batch_import.py --rules react-component-catalog,accessibility-guard --output skills/
```

## Notes

- Always validate imported skills before use
- Consider merging similar rules into one skill
- Add project-specific customizations after import
- Keep skills under 500 lines (use references/ for detailed content)