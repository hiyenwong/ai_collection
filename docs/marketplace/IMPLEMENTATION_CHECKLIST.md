---
title: Marketplace Implementation Checklist
date: 2026-04-27
---

# OpenClaw Plugin Marketplace - Implementation Checklist

**Timeline Estimate:** 2-3 weeks (Part-time) | 1 week (Full-time)
**Owner:** Project maintainer + community contributors  
**Status:** Ready to implement (Blueprint complete)

---

## Phase 0: Preparation (Day 1)

### 0.1 Review & Approval
- [ ] Review MARKETPLACE_BLUEPRINT.md completely
- [ ] Review PLUGIN_DECOMPOSITION.md to understand skill assignments
- [ ] Verify team understanding of scope (non-destructive, parallel paths, commit-SHA versioning)
- [ ] Create GitHub issue tracking this implementation (link this checklist)
- [ ] Announce plan in community channel (Discord, GitHub discussions)

### 0.2 Verify Prerequisites
- [ ] Confirm `claude` CLI installed: `claude --version` (should be 0.2.0+)
- [ ] Confirm Python 3.8+ installed: `python3 --version`
- [ ] Confirm Git installed: `git --version`
- [ ] Clone repo fresh: `git clone https://github.com/hiyenwong/ai_collection.git`

### 0.3 Create Development Branch
```bash
git checkout -b feat/plugin-marketplace-mvp
```

---

## Phase 1: Directory Structure & Symlinks (Days 1-2)

### 1.1 Create Root Marketplace Directory
```bash
mkdir -p .claude-plugin
```

### 1.2 Create Plugins Root
```bash
mkdir -p plugins
```

### 1.3 Create Plugin Subdirectories
```bash
for plugin in openclaw-core openclaw-neuroscience openclaw-coding openclaw-data openclaw-research; do
  mkdir -p "plugins/$plugin/.claude-plugin"
  mkdir -p "plugins/$plugin/skills"
  mkdir -p "plugins/$plugin/agents"
  touch "plugins/$plugin/README.md"
done
```

### 1.4 Symlink Skills to Plugins (openclaw-core)
```bash
cd plugins/openclaw-core/skills
for skill in security-guardrails skill-extractor memory-retrieval indexed-memory ice-review self-challenge meta-cognitive-reflection; do
  ln -s ../../../collection/skills/$skill
done
cd ../../../
```

**✅ Verify:** `ls -la plugins/openclaw-core/skills/` should show symlinks

### 1.5 Symlink Agents to Plugins (openclaw-core)
```bash
cd plugins/openclaw-core/agents
for agent in fullstack-engineer tech-cofounder research-agent; do
  ln -s ../../../collection/agents/$agent
done
cd ../../../
```

**✅ Verify:** `ls -la plugins/openclaw-core/agents/` should show symlinks

### 1.6 Symlink Large Plugin (openclaw-neuroscience skills)

First, generate list of neuroscience skills from _INDEX.json:
```bash
python3 << 'EOF'
import json

# Load _INDEX.json
with open('_INDEX.json', 'r') as f:
    index = json.load(f)

# Extract neuroscience-tagged skills
neuro_skills = [
    skill for skill in index.get('skills', [])
    if any(cat in skill.get('categories', []) for cat in ['neuroscience', 'brain', 'snn', 'neural', 'eeg', 'neuromorphic'])
]

print(f"Found {len(neuro_skills)} neuroscience skills")
for skill in neuro_skills[:10]:
    print(f"  - {skill['id']}")
print("  ...")
EOF
```

Then create symlinks:
```bash
cd plugins/openclaw-neuroscience/skills

# Get list of neuroscience skills from _INDEX.json (programmatically or manually)
# For now, manually do top 10 as test:
for skill in snn-internal-noise-analysis brain-to-speech-transformer-reconstruction in-context-brain-decoding eeg-visual-attention-decoding eeg2vision-multimodal-framework brain-foundation-model-batch-effects meta-learning-in-context-brain-decoding multimodal-higher-order-brain-networks spiking-neural-network-training neural-connectivity-matrix-viewer; do
  if [ -d "../../../collection/skills/$skill" ]; then
    ln -s ../../../collection/skills/$skill
    echo "✓ Linked $skill"
  fi
done
cd ../../../
```

**Note:** For full 400+ skills, automate with Python script (see bonus script at end of this checklist)

### 1.7 Symlink Other Plugins
Repeat section 1.6 for:
- `openclaw-coding/skills/` (150 skills tagged coding/typescript/react/security/testing)
- `openclaw-data/skills/` (50 skills tagged data/finance/ml/analytics)
- `openclaw-research/skills/` (50 skills tagged research/science/arxiv)

And agents for each plugin (from PLUGIN_DECOMPOSITION.md)

---

## Phase 2: Marketplace Configuration Files (Days 2-3)

### 2.1 Create Root Marketplace Manifest

**File:** `.claude-plugin/marketplace.json`

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
      "repository": "https://github.com/hiyenwong/ai_collection",
      "license": "MIT",
      "keywords": ["neuroscience", "brain", "spiking-neural-networks", "fmri", "eeg"],
      "category": "neuroscience"
    },
    {
      "name": "openclaw-coding",
      "source": "./plugins/openclaw-coding",
      "description": "Coding tools and developer skills (Claude Code, OpenCode, security, testing)",
      "author": { "name": "OpenClaw Contributors" },
      "repository": "https://github.com/hiyenwong/ai_collection",
      "license": "MIT",
      "keywords": ["coding", "typescript", "react", "security", "testing"],
      "category": "development"
    },
    {
      "name": "openclaw-data",
      "source": "./plugins/openclaw-data",
      "description": "Data analysis and quantitative tools (stock analysis, financial data, analytics)",
      "author": { "name": "OpenClaw Contributors" },
      "repository": "https://github.com/hiyenwong/ai_collection",
      "license": "MIT",
      "keywords": ["data", "finance", "analytics", "quantitative", "stock"],
      "category": "analytics"
    },
    {
      "name": "openclaw-research",
      "source": "./plugins/openclaw-research",
      "description": "Research and science agents (deep research, applied science, computational modeling)",
      "author": { "name": "OpenClaw Contributors" },
      "repository": "https://github.com/hiyenwong/ai_collection",
      "license": "MIT",
      "keywords": ["research", "science", "analytics", "academia"],
      "category": "research"
    }
  ]
}
```

**✅ Verify:** `cat .claude-plugin/marketplace.json | python3 -m json.tool` (should be valid JSON)

### 2.2 Create Plugin Manifests

For each plugin, create `.claude-plugin/plugin.json`:

**File:** `plugins/openclaw-core/.claude-plugin/plugin.json`
```json
{
  "name": "openclaw-core",
  "description": "Core agents and foundational skills for OpenClaw",
  "version": "1.0.0"
}
```

**File:** `plugins/openclaw-neuroscience/.claude-plugin/plugin.json`
```json
{
  "name": "openclaw-neuroscience",
  "description": "Neuroscience agents and skills",
  "version": "1.0.0"
}
```

Repeat for `openclaw-coding`, `openclaw-data`, `openclaw-research`.

**✅ Verify:** `for dir in plugins/*/; do echo "=== $dir ==="; cat "$dir/.claude-plugin/plugin.json"; done`

---

## Phase 3: Plugin-Level Documentation (Days 3-4)

### 3.1 Create Plugin READMEs

**File:** `plugins/openclaw-core/README.md`
```markdown
# openclaw-core

Core agents and foundational skills for the OpenClaw AI Collection.

## Includes

### Agents
- **fullstack-engineer** — Senior full-stack engineering for modern web development
- **tech-cofounder** — Technical co-founder guidance for product building
- **research-agent** — Deep research specialist

### Skills
- security-guardrails — Prevent exposure of secrets and sensitive data
- skill-extractor — Extract reusable capabilities from code
- memory-retrieval — Indexed knowledge base access
- [see collection/skills/ for full list]

## Installation

```bash
/plugin install openclaw-core@openclaw-ai-collection
```

## Documentation

Full documentation available in the [OpenClaw Collection](https://github.com/hiyenwong/ai_collection).
```

Repeat for other plugins, adjusting descriptions and skills/agents list.

### 3.2 Update Top-Level README.md

Add new section to main `README.md`:

```markdown
## Installation & Distribution

### Option 1: Claude Code Plugin Marketplace ✨ (Recommended)

For Claude Code users:

```bash
/plugin marketplace add hiyenwong/ai_collection
/plugin install openclaw-core@openclaw-ai-collection
/plugin install openclaw-neuroscience@openclaw-ai-collection
```

[Full Marketplace Guide](./docs/marketplace/MARKETPLACE.md)

### Option 2: OpenClaw Installation Script (Manual)

For users preferring the traditional approach:

```bash
python scripts/install.py --scope user --skills --agents
```

Both methods can coexist. Choose the one that fits your workflow.
```

### 3.3 Create Marketplace Documentation

**File:** `docs/marketplace/MARKETPLACE.md`

```markdown
# Claude Code Plugin Marketplace

The OpenClaw collection is available via the official Claude Code plugin marketplace.

## Quick Start

1. **Add marketplace:**
   ```bash
   /plugin marketplace add hiyenwong/ai_collection
   ```

2. **Install plugin(s):**
   ```bash
   /plugin install openclaw-core@openclaw-ai-collection
   /plugin install openclaw-neuroscience@openclaw-ai-collection
   ```

3. **Use skills and agents:**
   - Skills activate automatically when trigger keywords match user input
   - Agents are available via `/agent list`

## Available Plugins

- **openclaw-core** — Core agents and security skills
- **openclaw-neuroscience** — Brain science and neural modeling
- **openclaw-coding** — Development tools and best practices
- **openclaw-data** — Data analysis and quantitative tools
- **openclaw-research** — Research and scientific computing

## Versioning

Plugins auto-update with each commit to `main`. No manual version management needed.

## Troubleshooting

See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues.
```

---

## Phase 4: Validation & Testing (Days 4-5)

### 4.1 Syntax Validation

```bash
claude plugin validate .
```

**Expected output:**
```
✓ marketplace.json is valid
✓ plugins/openclaw-core/.claude-plugin/plugin.json is valid
✓ plugins/openclaw-neuroscience/.claude-plugin/plugin.json is valid
✓ plugins/openclaw-coding/.claude-plugin/plugin.json is valid
✓ plugins/openclaw-data/.claude-plugin/plugin.json is valid
✓ plugins/openclaw-research/.claude-plugin/plugin.json is valid
✓ All validations passed
```

**If validation fails:**
- [ ] Check JSON syntax: `python3 -m json.tool {file}`
- [ ] Verify directory structure matches marketplace.json paths
- [ ] Check for broken symlinks: `find plugins -L -type l`

### 4.2 Local Installation Test

```bash
/plugin marketplace add ./
```

**Expected output:**
```
Added local marketplace: openclaw-ai-collection
```

### 4.3 Install Individual Plugins (Local)

```bash
/plugin install openclaw-core@openclaw-ai-collection
/plugin install openclaw-neuroscience@openclaw-ai-collection  # may take longer
/plugin install openclaw-coding@openclaw-ai-collection
/plugin install openclaw-data@openclaw-ai-collection
/plugin install openclaw-research@openclaw-ai-collection
```

**Expected:** All succeed without errors

### 4.4 Verify Skills Are Discoverable

```
User in Claude Code: @security-guardrails

Expected: Autocomplete suggests "security-guardrails" skill
```

### 4.5 Test Skill Activation (Sample)

```
User: "I need to make sure I'm not leaking API keys in my code"

Expected: Mentions security-guardrails skill availability
```

### 4.6 Regression Test: Original Installation Still Works

```bash
python scripts/install.py --scope user --skills
```

**Expected:** Install succeeds; original path unchanged

### 4.7 Directory Structure Spot Check

```bash
# Check symlinks are valid
find plugins -type l -exec ls -l {} \;

# Should show symlinks like:
# plugins/openclaw-core/skills/security-guardrails -> ../../../collection/skills/security-guardrails
```

**✅ Verify all symlinks resolve correctly**

---

## Phase 5: Distribution & Release (Days 5-6)

### 5.1 Prepare Release Branch

```bash
git add .claude-plugin/ plugins/ docs/marketplace/
git commit -m "feat: add claude code plugin marketplace

- Create 5 domain-based plugins (core, neuroscience, coding, data, research)
- Add marketplace.json with plugin manifests
- Add symlinks from collection/ to plugins/
- Add marketplace documentation
- All 966 skills + 27 agents now available via Claude Code plugins

Fixes: #<issue-number>"

git push origin feat/plugin-marketplace-mvp
```

### 5.2 Create Pull Request

```bash
# GitHub CLI
gh pr create --title "feat: add claude code plugin marketplace" \
  --body "Adds marketplace distribution for 966 skills and 27 agents" \
  --label "marketplace" \
  --label "documentation"
```

### 5.3 Code Review Checklist

- [ ] Marketplace.json is valid JSON
- [ ] All plugin.json files present and valid
- [ ] Symlinks point to correct collection/ paths
- [ ] No collection/ files were modified (only symlinks added)
- [ ] Documentation is clear and complete
- [ ] Validation passes locally
- [ ] Installation tests succeed
- [ ] Backward compatibility preserved (scripts/install.py still works)

### 5.4 Merge to Main

```bash
git checkout main
git pull origin main
git merge feat/plugin-marketplace-mvp
git push origin main
```

### 5.5 Verify Remote Distribution

```bash
# Clone repo fresh in temp directory
cd /tmp
git clone https://github.com/hiyenwong/ai_collection.git ai_test
cd ai_test

# Test adding remote marketplace
/plugin marketplace add hiyenwong/ai_collection

# Should succeed and find symlinks resolved
```

### 5.6 Tag Release (Optional for MVP)

```bash
git tag -a marketplace-v1.0 -m "First stable plugin marketplace release"
git push origin marketplace-v1.0
```

---

## Phase 6: Community Launch (Days 6-7)

### 6.1 Announce in Community Channels

- [ ] Discord: Post announcement with quick-start command
- [ ] GitHub Discussions: Create discussion for feedback
- [ ] Reddit: Post to relevant subreddits (r/ClaudeAI, r/MachineLearning, r/Python)
- [ ] Twitter/X: Share launch announcement
- [ ] Email: Send to newsletter subscribers (if applicable)

### 6.2 Example Announcement

```
🎉 OpenClaw Marketplace Launch!

966 skills + 27 agents now available via Claude Code plugins!

Quick start:
/plugin marketplace add hiyenwong/ai_collection

Install what you need:
- openclaw-core — Essential agents & security
- openclaw-neuroscience — Brain science tools
- openclaw-coding — Developer skills
- openclaw-data — Analytics & finance
- openclaw-research — Research & science

GitHub: https://github.com/hiyenwong/ai_collection
Docs: https://github.com/hiyenwong/ai_collection/tree/main/docs/marketplace
```

### 6.3 Monitor Feedback

- [ ] Watch GitHub Issues for bugs/feedback
- [ ] Respond to Reddit/Discord comments
- [ ] Gather usage metrics (if available)
- [ ] Plan Phase 2 enhancements based on feedback

---

## Phase 7: Documentation & Handoff (Days 7-8)

### 7.1 Update Main README

- [ ] Add marketplace section
- [ ] Link to marketplace docs
- [ ] Provide both installation paths clearly

### 7.2 Create Contributor Guide Update

**File:** `CONTRIBUTING.md` (add section)

```markdown
### Adding Skills to Marketplace

When adding a new skill to `collection/skills/`:

1. Skill must pass quality gates (see SKILLS.md)
2. Add entry to `_INDEX.json` with:
   - `categories`: domain tags (neuroscience, coding, research, data)
   - `trigger`: activation keywords
   - `description`: one-liner
3. Determine target plugin from PLUGIN_DECOMPOSITION.md
4. Next deploy: skill will auto-appear in that plugin

No manual marketplace update needed — git commit triggers deployment.
```

### 7.3 Create Troubleshooting Guide

**File:** `docs/marketplace/TROUBLESHOOTING.md`

```markdown
# Marketplace Troubleshooting

## Q: "Plugin not found" error

A: Try:
```bash
/plugin marketplace update openclaw-ai-collection
/plugin cache clear
/plugin install openclaw-core@openclaw-ai-collection
```

## Q: Skills aren't being recognized

A: Ensure plugin installed:
```bash
/plugin list
# Should show openclaw-core@openclaw-ai-collection, etc.
```

## Q: Want to revert to original installation?

A: 
```bash
# Uninstall marketplace plugins
/plugin uninstall openclaw-*

# Use original script
python scripts/install.py --scope user --skills --agents
```

## Q: How do I update plugins?

A:
```bash
/plugin marketplace update openclaw-ai-collection
# All plugins auto-update on next Claude Code session
```

See [MARKETPLACE.md](./MARKETPLACE.md) for more info.
```

### 7.4 Update SKILLS.md

Add section highlighting marketplace availability:

```markdown
## Distribution

OpenClaw skills are available via two methods:

1. **Claude Code Plugin Marketplace** — Recommended for Claude Code users
   ```bash
   /plugin marketplace add hiyenwong/ai_collection
   /plugin install openclaw-{category}@openclaw-ai-collection
   ```

2. **Script Installation** — For manual or OpenClaw users
   ```bash
   python scripts/install.py --scope user --skills
   ```

See [Marketplace Guide](./docs/marketplace/MARKETPLACE.md).
```

---

## Bonus: Automation Scripts

### Batch Symlink Creation (Python)

**File:** `scripts/create-marketplace-symlinks.py`

```python
#!/usr/bin/env python3
"""Create symlinks for marketplace plugins from _INDEX.json"""

import json
import os
from pathlib import Path

# Load index
with open('_INDEX.json', 'r') as f:
    index = json.load(f)

# Define category → plugin mappings
PLUGIN_CATEGORIES = {
    'openclaw-core': ['security', 'meta', 'memory', 'prompt'],
    'openclaw-neuroscience': ['neuroscience', 'brain', 'snn', 'eeg', 'fmri', 'neural'],
    'openclaw-coding': ['coding', 'typescript', 'react', 'security', 'testing'],
    'openclaw-data': ['data', 'finance', 'ml', 'quantitative', 'analytics'],
    'openclaw-research': ['research', 'science', 'arxiv', 'academic', 'physics'],
}

for plugin, categories in PLUGIN_CATEGORIES.items():
    plugin_skills_dir = f"plugins/{plugin}/skills"
    os.makedirs(plugin_skills_dir, exist_ok=True)
    
    for skill in index.get('skills', []):
        skill_categories = skill.get('categories', [])
        
        # Check if skill matches any category for this plugin
        if any(cat in skill_categories for cat in categories):
            skill_id = skill['id']
            symlink_path = f"{plugin_skills_dir}/{skill_id}"
            target_path = f"../../../collection/skills/{skill_id}"
            
            # Create symlink if it doesn't exist
            if not os.path.exists(symlink_path):
                os.symlink(target_path, symlink_path)
                print(f"✓ Created: {symlink_path} -> {target_path}")
            else:
                print(f"⊘ Exists: {symlink_path}")

print("\n✅ Symlinks created successfully")
```

**Usage:**
```bash
python scripts/create-marketplace-symlinks.py
```

### Validation Script (Bash)

**File:** `scripts/validate-marketplace.sh`

```bash
#!/bin/bash
set -e

echo "🔍 Validating marketplace structure..."

# Check marketplace.json
echo "Checking .claude-plugin/marketplace.json..."
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null && echo "✓ Valid JSON"

# Check all plugin.json files
for plugin_json in plugins/*/.claude-plugin/plugin.json; do
    echo "Checking $plugin_json..."
    python3 -m json.tool "$plugin_json" > /dev/null && echo "✓ Valid"
done

# Validate with Claude CLI
echo "Running Claude plugin validator..."
claude plugin validate . && echo "✓ Validation passed" || echo "✗ Validation failed"

# Check symlinks
echo "Checking symlinks..."
broken_links=$(find plugins -L -type l 2>/dev/null | wc -l)
if [ $broken_links -eq 0 ]; then
    echo "✓ All symlinks valid"
else
    echo "✗ $broken_links broken symlinks found"
    find plugins -L -type l 2>/dev/null
fi

echo "✅ Validation complete"
```

**Usage:**
```bash
bash scripts/validate-marketplace.sh
```

---

## Success Criteria Verification

Run this before Phase 5 (release):

- [ ] ✅ `claude plugin validate .` passes
- [ ] ✅ `/plugin marketplace add ./` succeeds locally
- [ ] ✅ `/plugin install openclaw-core@openclaw-ai-collection` succeeds
- [ ] ✅ All 5 plugins install without errors
- [ ] ✅ Skills are discoverable (trigger keywords work)
- [ ] ✅ `python scripts/install.py --scope user --skills` still works (backward compat)
- [ ] ✅ All symlinks are valid (no broken links)
- [ ] ✅ Documentation is complete and clear
- [ ] ✅ Community feedback positive (from Phase 6)

---

## Post-Launch Monitoring (Ongoing)

### Weekly Checks
- [ ] Monitor GitHub Issues for marketplace-related bugs
- [ ] Verify marketplace CI/CD status
- [ ] Spot-check random plugins still install correctly

### Monthly Review
- [ ] Gather community feedback
- [ ] Track plugin usage metrics (if available)
- [ ] Plan Phase 2 (stable channel, advanced versioning)

### Version 2.0 Planning
Once MVP is stable (4-6 weeks), consider:
- [ ] Semantic versioning instead of commit SHA
- [ ] `stable` marketplace channel
- [ ] Custom CLI: `openclaw install skill@category`
- [ ] Marketplace web UI for discovery
- [ ] Analytics dashboard (downloads, popular skills)

---

**✅ Checklist Complete**

All items checked = **Marketplace Ready for Production**

Questions? Open GitHub Issue or discussion in repository.
