# ai_collection Project Structure (Canonical)

Canonical project layout for skill/agent package collections. Used as the structural standard for all agent-related projects (e.g., super_factory).

## Directory Layout

```
ai_collection/
├── collection/
│   ├── agents/       # Agent packages (each: AGENT.md + optional assets/references/)
│   └── skills/       # Skill packages (each: SKILL.md + optional references/scripts/assets/)
├── docs/             # General documentation (guides, integration docs)
├── templates/        # New-item templates (agent-template.md, skill-template.md)
├── resources/        # External resources and links
├── knowledge/        # Knowledge base (papers, notes)
├── scripts/          # Utility scripts (CI, batch operations)
└── [root docs]       # README.md, AGENTS.md, SKILLS.md, STRUCTURE.md, CONTRIBUTING.md
```

## Key Rules

1. **No skill/agent dirs at root level.** All packages go under `collection/skills/` or `collection/agents/`.
2. **One directory per package.** Each skill is a self-contained directory with SKILL.md.
3. **Root only contains:** collection/, docs/, templates/, resources/, knowledge/, scripts/, and documentation files.
4. **Naming:** lowercase-with-hyphens for directories.

## Reorganization Procedure

When root-level skill directories accumulate (common during iterative development):

```bash
cd ai_collection
for d in $(ls -d */ | sed 's/\///' | grep -vE '^(collection|docs|knowledge|scripts|skills|templates)$'); do
    dest="collection/skills/$d"
    if [ -d "$dest" ]; then
        [ -f "$d/SKILL.md" ] && cp "$d/SKILL.md" "$dest/SKILL.md"  # merge newer
    else
        mv "$d" "$dest"
    fi
    [ -d "$d" ] && rm -rf "$d"
done
```

## Cross-Project Mapping

| super_factory dir         | ai_collection equivalent          |
|---------------------------|-----------------------------------|
| specs/agents/*.yaml       | collection/agents/*/AGENT.md      |
| agents/<role>/            | collection/agents/<role>/         |
| (future) skill definitions| collection/skills/*/SKILL.md      |
