---
title: Plugin Marketplace MVP - Implementation Blueprint
date: 2026-04-27
status: Ready for Implementation
---

# OpenClaw Plugin Marketplace MVP - Complete Blueprint

**Scope:** Create a public Claude Code plugin marketplace distributing 3-5 domain-based plugins from the existing collection. First version uses git commit SHA for auto-updates (no explicit version field).

---

## 1. Scope & Compatibility Boundary

### Target Audience
- **Primary:** Public open-source community (Discord, GitHub, AI communities)
- **Secondary:** Internal teams using OpenClaw collection (optional `.claude/settings.json` integration)

### Compatibility Model
- **Non-destructive:** Existing `scripts/install.py` OpenClaw installation path remains unchanged
- **Additive:** New Claude Code marketplace is an additional distribution method
- **Parallel paths:**
  - Path A: OpenClaw users continue with existing tooling (no change)
  - Path B: Claude Code users can use `/plugin marketplace add` to discover & install
  - **Fallback:** If marketplace unavailable, users revert to Path A (documented)

### Constraints
- Do NOT modify `collection/skills/` or `collection/agents/` internal structure
- Do NOT add runtime dependencies to OpenClaw
- Plugins are snapshots of collection content; live instances in `~/.claude/plugins/cache/`
- Plugins cannot reference files outside their own directory (caching limitation)
- Plugin installation is ephemeral per Claude Code session (no persistent state)

### Files Preserved (NOT Modified)
- `scripts/install.py`
- `collection/skills/**`
- `collection/agents/**`
- Existing `README.md`, `SKILLS.md`, `AGENTS.md` (only supplemented with marketplace links)

---

## 2. Marketplace Information Architecture

### Marketplace Identity
```json
{
  "name": "openclaw-ai-collection",
  "owner": {
    "name": "OpenClaw Contributors",
    "email": "opensource@openclaw.ai"
  },
  "metadata": {
    "description": "Curated agents and skills from the OpenClaw AI Collection — neuroscience, coding, research, and infrastructure tools",
    "version": "1.0.0"
  },
  "pluginRoot": "./plugins"
}
```

### Classification Scheme: 5 Domain Plugins
| Plugin | Category | Focus | Size (est.) |
|--------|----------|-------|------------|
| **openclaw-core** | Core | foundational agents (fullstack, research, tech-cofounder) + base skills | ~20 skills, 3 agents |
| **openclaw-neuroscience** | Neuroscience | brain-focused skills (spiking nets, EEG, neural dynamics, foundation models) | ~150+ skills |
| **openclaw-coding** | Coding | coding-specific skills (Claude Code, OpenCode, OpenSpec, security) | ~25 skills |
| **openclaw-data** | Data & ML | data analysis, stock analysis, quantitative tools | ~15 skills |
| **openclaw-research** | Research & Science | applied science, computational science, neuroscience research, deep research | ~40+ skills |

**Rationale:** Domain split aligns with existing `_INDEX.json` categories, makes discovery manageable (~30-40 skills per plugin is optimal), and avoids monolithic 966-skill dump.

### Reserved Marketplace Names (CANNOT USE)
- `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`
- `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `knowledge-work-plugins`, `life-sciences`
- Names impersonating official marketplaces (e.g., `official-claude-plugins`, `anthropic-tools-v2`)

✅ Our choice `openclaw-ai-collection` is safe (not in reserved list, clearly branded).

---

## 3. Plugin Decomposition Rules

### Mapping Table: Skills & Agents → Plugins

| Component | Plugin | Notes |
|-----------|--------|-------|
| **Agents** | | |
| fullstack-engineer | openclaw-core | General-purpose; primary entry point |
| research-agent | openclaw-research | Research specialist |
| tech-cofounder | openclaw-core | Product/MVP building |
| algorithm-engineer | openclaw-neuroscience | Algorithm + neural models focus |
| applied-scientist | openclaw-research | Science-driven solutions |
| biologist | openclaw-neuroscience | Biology agent |
| computational-scientist | openclaw-neuroscience | Computational modeling |
| mathematician | openclaw-research | Formal reasoning |
| neuroscientist | openclaw-neuroscience | Primary neuroscience expert |
| psychologist | openclaw-research | Cognitive/behavior analysis |
| statistician | openclaw-data | Statistical methods |
| stock-analyst | openclaw-data | Financial analysis |
| **Skills** | | |
| claude-code | openclaw-coding | Core coding platform |
| opencode | openclaw-coding | OSS coding agent |
| openspec | openclaw-coding | BDD/specification-driven |
| security-guardrails | openclaw-core | Security (used by all agents) |
| akshare | openclaw-data | Chinese financial data |
| stock-analysis | openclaw-data | Stock indicators |
| consulting-report-search | openclaw-research | Research reports |
| skill-extractor | openclaw-core | Meta-skill |
| [966 neuroscience skills] | openclaw-neuroscience | All skills with "neuroscience", "brain", "snn", "eeg", "neural", "neuromorphic" tags |
| [150+ coding/dev skills] | openclaw-coding | All skills tagged "coding", "typescript", "react", "nodejs", "security", "testing" |
| [40+ data skills] | openclaw-data | "data", "ml", "quantitative", "analytics", "finance", "akshare" tagged |

### Conflict Resolution
- **Shared skills** (e.g., cloud infrastructure used by multiple plugins): Place in `openclaw-core` or replicate with `strict: false` override in marketplace entry
- **Trigger keyword collisions** (e.g., "brain" could activate both neuroscience and research agents): Document priority in skill docs; agent instructions take precedence over skill trigger keywords in Claude Code
- **Experimental skills**: Mark with `status: experimental` in frontmatter; include in docs but allow opt-in vs default install

### Naming Conventions
- Plugin ID: `openclaw-{domain}` (kebab-case, no underscores)
- Skill ID within plugin: Use existing skill directory name (no renaming)
- Agent ID within plugin: Use existing agent directory name

---

## 4. Directory Blueprint

### Root Marketplace Structure
```
ai_collection/
├── .claude-plugin/                           # ← NEW: Marketplace root manifest
│   └── marketplace.json                      # Main catalog (see template below)
│
├── plugins/                                  # ← NEW: Plugins directory
│   │
│   ├── openclaw-core/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json                   # Core plugin manifest
│   │   ├── skills/
│   │   │   ├── security-guardrails/          # Symlink or copy from collection/
│   │   │   ├── skill-extractor/
│   │   │   └── ...
│   │   ├── agents/
│   │   │   ├── fullstack-engineer/           # Symlink to collection/agents/
│   │   │   ├── tech-cofounder/
│   │   │   └── ...
│   │   └── README.md                         # Plugin-specific README
│   │
│   ├── openclaw-neuroscience/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── skills/
│   │   │   ├── snn-internal-noise-analysis/
│   │   │   ├── brain-to-speech-transformer-reconstruction/
│   │   │   └── [150+ neuroscience skills]
│   │   ├── agents/
│   │   │   ├── neuroscientist/               # Symlink
│   │   │   ├── biologist/
│   │   │   ├── computational-scientist/
│   │   │   └── algorithm-engineer/
│   │   └── README.md
│   │
│   ├── openclaw-coding/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── skills/
│   │   │   ├── claude-code/
│   │   │   ├── opencode/
│   │   │   ├── openspec/
│   │   │   └── [150+ coding skills]
│   │   ├── agents/
│   │   │   └── (optional: coding-specific agents from collection)
│   │   └── README.md
│   │
│   ├── openclaw-data/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── skills/
│   │   │   ├── akshare/
│   │   │   ├── stock-analysis/
│   │   │   ├── consulting-report-search/
│   │   │   └── [30+ data skills]
│   │   ├── agents/
│   │   │   └── stock-analyst/
│   │   └── README.md
│   │
│   └── openclaw-research/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── skills/
│       │   └── [40+ research/science skills]
│       ├── agents/
│       │   ├── research-agent/
│       │   ├── applied-scientist/
│       │   ├── mathematician/
│       │   ├── psychologist/
│       │   └── statistician/
│       └── README.md
│
├── collection/                               # UNCHANGED
│   ├── agents/
│   └── skills/
│
└── [existing files remain unchanged]
```

### File Strategy: Symlinks vs. Copies
- **Recommended: Symlinks** — Plugins reference `collection/` files via symlinks
- **Fallback: Copies** — For systems that don't support symlinks (Windows), maintain copies during release (CI step)
- **Cache behavior:** Claude Code copies plugin to `~/.claude/plugins/cache/` on install; symlinks are resolved at cache-copy time

### Template: .claude-plugin/marketplace.json
```json
{
  "name": "openclaw-ai-collection",
  "owner": {
    "name": "OpenClaw Contributors",
    "email": "opensource@openclaw.ai"
  },
  "metadata": {
    "description": "Curated agents and skills from the OpenClaw AI Collection — neuroscience, coding, research, and infrastructure tools",
    "version": "1.0.0"
  },
  "pluginRoot": "./plugins",
  "plugins": [
    {
      "name": "openclaw-core",
      "source": "./plugins/openclaw-core",
      "description": "Core agents and foundational skills (fullstack engineer, tech co-founder, research, security guardrails)",
      "author": { "name": "OpenClaw Contributors" },
      "homepage": "https://github.com/hiyenwong/ai_collection/tree/main/plugins/openclaw-core",
      "repository": "https://github.com/hiyenwong/ai_collection",
      "license": "MIT",
      "keywords": ["agents", "skills", "fullstack", "research", "security"],
      "category": "core"
    },
    {
      "name": "openclaw-neuroscience",
      "source": "./plugins/openclaw-neuroscience",
      "description": "Neuroscience agents and skills (brain modeling, EEG, spiking neural networks, fMRI)",
      "author": { "name": "OpenClaw Contributors" },
      "keywords": ["neuroscience", "brain", "spiking-neural-networks", "fmri", "eeg"],
      "category": "neuroscience"
    },
    {
      "name": "openclaw-coding",
      "source": "./plugins/openclaw-coding",
      "description": "Coding tools and developer skills (Claude Code, OpenCode, security, testing)",
      "author": { "name": "OpenClaw Contributors" },
      "keywords": ["coding", "typescript", "react", "security", "testing"],
      "category": "development"
    },
    {
      "name": "openclaw-data",
      "source": "./plugins/openclaw-data",
      "description": "Data analysis and quantitative tools (stock analysis, financial data, analytics)",
      "author": { "name": "OpenClaw Contributors" },
      "keywords": ["data", "finance", "analytics", "quantitative", "stock"],
      "category": "analytics"
    },
    {
      "name": "openclaw-research",
      "source": "./plugins/openclaw-research",
      "description": "Research and science agents (deep research, applied science, computational modeling)",
      "author": { "name": "OpenClaw Contributors" },
      "keywords": ["research", "science", "analytics", "academia"],
      "category": "research"
    }
  ]
}
```

### Template: plugins/openclaw-core/.claude-plugin/plugin.json
```json
{
  "name": "openclaw-core",
  "description": "Core agents and foundational skills for OpenClaw",
  "version": "1.0.0"
}
```

---

## 5. Versioning & Release Strategy

### Version Resolution (Claude Code Plugin System)
```
Order of precedence (highest → lowest):
1. version in plugin.json (if present)
2. version in marketplace.json entry (if present)
3. Git commit SHA (auto-derived)
```

### MVP Strategy: Commit SHA Auto-Update
- **Do NOT set `version` field** in `plugin.json` or marketplace entries
- Each commit to `main` automatically increments version (via commit SHA)
- Users run `/plugin update openclaw-{plugin}@openclaw-ai-collection` to get latest
- No manual version bumping required
- **Advantage:** Simple, release-on-commit workflow; no versioning gymnastics

### Release Cadence
1. **Continuous (main branch):** Every commit is a new version
2. **Quality gate:** All commits pass `claude plugin validate .` before merge
3. **Changelog:** Maintain `plugins/{plugin}/CHANGELOG.md` with commit-linked notes

### Example Release Flow
```bash
# Dev adds new skills to collection/skills/
# Dev creates PR to main
# CI runs: claude plugin validate .
# On merge to main:
#   - Version auto-increments to new commit SHA
#   - Users see update on next `/plugin marketplace update openclaw-ai-collection`
#   - No manual tag/release needed
```

### Future Enhancement (not MVP)
If stability needed later, add second marketplace for `stable` channel:
```json
{
  "name": "openclaw-ai-collection-stable",
  "pluginRoot": "./plugins",
  "plugins": [
    {
      "name": "openclaw-core",
      "source": {
        "source": "github",
        "repo": "hiyenwong/ai_collection",
        "ref": "release/v1.0"  # Pin to release branch
      }
    }
  ]
}
```

---

## 6. Quality Gates & Validation

### Pre-Release Validation (CI/CD)
1. **Syntax validation:** `claude plugin validate .`
   - Checks `marketplace.json` schema
   - Validates all `plugin.json` files
   - Checks YAML frontmatter in SKILL.md, AGENT.md
   - Validates hooks.json syntax

2. **Naming validation:**
   - Plugin names: kebab-case, no spaces, no reserved names
   - Skill/agent IDs: match existing collection names
   - Uniqueness: no duplicate plugin names

3. **Structure validation:**
   - Each plugin must have `.claude-plugin/plugin.json`
   - Each plugin must have at least 1 skill or agent
   - No `../` paths in source definitions (stays within plugin root)

4. **Content validation:**
   - SKILL.md has required sections: description, activation keywords, instructions
   - AGENT.md has required sections: purpose, model, system prompt
   - All referenced files exist (no broken symlinks)

5. **Installation test (local):**
   - `claude plugin marketplace add ./` succeeds
   - `/plugin install openclaw-core@openclaw-ai-collection` succeeds
   - Installed skills are discoverable and callable

6. **Regression test:**
   - Original `scripts/install.py` still works (backward compatibility)
   - No collection files were modified (only symlinks in plugins/)

### Manual QA Checklist (Before Release)
- [ ] All 5 plugins validate without errors
- [ ] Each plugin installs successfully locally
- [ ] Skills from each plugin are callable (test at least 1 per plugin)
- [ ] Skill triggers work (activation keywords recognized)
- [ ] No hardcoded paths or secrets in skill/agent docs
- [ ] All links in SKILL.md/AGENT.md are valid
- [ ] Plugin-level README.md exists and is clear
- [ ] Marketplace.json marketplace.json lists all plugins
- [ ] All original collection/ files unchanged
- [ ] Compatible with Claude Code latest version

### Continuous Validation (Pre-Commit Hook)
```bash
# .git/hooks/pre-commit
#!/bin/bash
set -e
echo "[Pre-commit] Validating marketplace structure..."
claude plugin validate .
echo "[Pre-commit] ✓ Passed"
```

---

## 7. Distribution & Team Onboarding

### GitHub Public Distribution
1. **Repository:** `https://github.com/hiyenwong/ai_collection`
2. **Branch:** `main` (always latest; no separate release branches in MVP)
3. **User discovery:**
   ```bash
   /plugin marketplace add hiyenwong/ai_collection
   ```
   Shorthand works because we're using GitHub source.

### Individual Plugin Installation
```bash
/plugin install openclaw-core@openclaw-ai-collection
/plugin install openclaw-neuroscience@openclaw-ai-collection
/plugin install openclaw-data@openclaw-ai-collection
# ... etc
```

### Team Onboarding: Auto-Enable Plugins
For teams that want to standardize on OpenClaw plugins, add to `.claude/settings.json`:
```json
{
  "extraKnownMarketplaces": {
    "openclaw-ai-collection": {
      "source": {
        "source": "github",
        "repo": "hiyenwong/ai_collection"
      }
    }
  },
  "enabledPlugins": {
    "openclaw-core@openclaw-ai-collection": true,
    "openclaw-coding@openclaw-ai-collection": true,
    "openclaw-research@openclaw-ai-collection": true
  }
}
```

### Discovery UX
- **From GitHub:** User discovers repo → sees README marketplace section → runs add command
- **From Claude Code:** User runs `/plugin search openclaw` → finds listed marketplace → adds
- **Community channels:** Announce in Discord, Reddit, X, community forums

---

## 8. Rollback & Parallel Coexistence

### Scenario: Marketplace unavailable / user wants to revert
```bash
# If marketplace broken or user prefers original path:
# Revert to existing installation method
python scripts/install.py --scope user --skills --agents

# Both paths can coexist:
# - Marketplace installations live in ~/.claude/plugins/cache/
# - Script installations live in ~/.claude/skills/ and ~/.claude/agents/
# - No file conflicts (separate directories)
```

### Fallback Documentation
Add section to `docs/MARKETPLACE_TROUBLESHOOTING.md`:

**Q: Marketplace add failed, what do I do?**
A: The marketplace is hosted on GitHub and requires internet. If unavailable, use the original installation method:
```bash
cd /path/to/ai_collection
python scripts/install.py --scope user --skills --agents
```

**Q: Can I use both marketplace and script installation together?**
A: Yes! They store plugins in different directories, so no conflicts. You can use either.

**Q: My installed plugin stopped working after marketplace update**
A: Rollback by:
1. Uninstall: `/plugin uninstall plugin-name@openclaw-ai-collection`
2. Revert to script: `python scripts/install.py --scope user --skills`

---

## 9. Documentation Landing Sites

### New Documentation to Create
1. **docs/marketplace/MARKETPLACE.md**
   - What is the marketplace?
   - How to discover plugins
   - Installation walkthrough
   - Comparison: marketplace vs. script installation

2. **docs/marketplace/TROUBLESHOOTING.md**
   - Common errors
   - Fallback paths
   - Validation errors

3. **plugins/{plugin}/README.md** (one per plugin)
   - Plugin purpose
   - Skills included (brief)
   - Agents included
   - How to use
   - Links to full documentation in `collection/`

4. **MARKETPLACE_QUICKSTART.md** (top-level)
   - 30-second setup
   - Copy-paste commands
   - Links to detailed docs

### Documentation Links to Update

**README.md (top-level)**
- Add new "Distribution Methods" section above "Quick Start"
- Link to marketplace docs
- Highlight both paths (marketplace + script)

**SKILLS.md (top-level)**
- Add note: "Also available via Claude Code plugin marketplace"
- Link to `docs/marketplace/MARKETPLACE.md`

**AGENTS.md (top-level)**
- Same: note availability via marketplace

**Collection README** (in each plugin dir)
- Auto-generated index of skills in that plugin
- Link back to full skill docs in `collection/`

### Example: Top-Level README.md Addition
```markdown
## Installation Methods

### Method 1: Claude Code Plugin Marketplace (Recommended)
For Claude Code users, install plugins from the marketplace:

```bash
/plugin marketplace add hiyenwong/ai_collection
/plugin install openclaw-core@openclaw-ai-collection
```

See [Marketplace Guide](./docs/marketplace/MARKETPLACE.md) for details.

### Method 2: Script Installation (OpenClaw/Manual)
For OpenClaw users or manual installation:

```bash
python scripts/install.py --scope user --skills --agents
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

Both methods can coexist — use whichever suits your workflow.
```

---

## Implementation Checklist

### Phase 1: Structure & Validation (Week 1)
- [ ] Create `.claude-plugin/` and `plugins/` directories
- [ ] Write `marketplace.json` template
- [ ] Create `plugins/{plugin}/.claude-plugin/plugin.json` stubs for all 5 plugins
- [ ] Set up symlinks from `plugins/*/skills/` → `collection/skills/`
- [ ] Set up symlinks from `plugins/*/agents/` → `collection/agents/`
- [ ] Run `claude plugin validate .` — should pass

### Phase 2: Documentation (Week 1)
- [ ] Write `docs/marketplace/MARKETPLACE.md`
- [ ] Write `docs/marketplace/TROUBLESHOOTING.md`
- [ ] Create `plugins/{plugin}/README.md` for each plugin
- [ ] Write `MARKETPLACE_QUICKSTART.md`
- [ ] Update top-level `README.md` with "Installation Methods" section

### Phase 3: Testing & Validation (Week 2)
- [ ] Local validation: `claude plugin marketplace add ./`
- [ ] Install each plugin: `/plugin install openclaw-{plugin}@openclaw-ai-collection`
- [ ] Test skill activation: verify triggers work for sample skills from each plugin
- [ ] Test agent invocation: verify agents are discoverable
- [ ] Regression test: confirm `scripts/install.py` still works
- [ ] Test fallback: document rollback process and verify it works

### Phase 4: Distribution & Release (Week 2)
- [ ] Push to GitHub `main` branch
- [ ] Verify GitHub shows symlinks correctly
- [ ] Test remote add: `/plugin marketplace add hiyenwong/ai_collection`
- [ ] Test remote install: verify remote plugins install same as local
- [ ] Document release in CHANGELOG.md
- [ ] Announce to community channels

### Phase 5: Monitoring (Ongoing)
- [ ] Monitor GitHub Issues for marketplace-related bugs
- [ ] Track marketplace add/install success rates (if analytics available)
- [ ] Gather feedback from early adopters
- [ ] Plan Phase 2 (stable channel, versioning enhancements)

---

## Success Criteria

1. ✅ **Usable:** Users can run `/plugin marketplace add hiyenwong/ai_collection` and get plugins
2. ✅ **Reliable:** Validation passes; install/uninstall works repeatably
3. ✅ **Compatible:** Original paths (script, manual) still work; no breaking changes
4. ✅ **Documented:** New users understand both distribution methods
5. ✅ **Discoverable:** Marketplace appears in Claude Code `/plugin search` and community channels
6. ✅ **Fallbackable:** If marketplace broken, users have clear path to revert
7. ✅ **Extensible:** Adding new plugins/skills to marketplace is straightforward

---

## Appendix: CLI Command Reference

### For Users
```bash
# Discover marketplace
/plugin marketplace add hiyenwong/ai_collection

# Install plugins
/plugin install openclaw-core@openclaw-ai-collection
/plugin install openclaw-neuroscience@openclaw-ai-collection
/plugin install openclaw-coding@openclaw-ai-collection
/plugin install openclaw-data@openclaw-ai-collection
/plugin install openclaw-research@openclaw-ai-collection

# Update plugins
/plugin marketplace update openclaw-ai-collection

# List installed
/plugin list

# Uninstall
/plugin uninstall openclaw-core@openclaw-ai-collection
```

### For Maintainers
```bash
# Validate locally
claude plugin validate .

# Test add marketplace
/plugin marketplace add ./

# Test install plugin
/plugin install openclaw-core@openclaw-ai-collection

# View known marketplaces
/plugin marketplace list
```

---

**End of Blueprint**
