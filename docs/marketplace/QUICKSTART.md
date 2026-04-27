---
title: Marketplace Quick Start
date: 2026-04-27
---

# OpenClaw Marketplace — Quick Start (30 Seconds)

## For Users: Install & Use

### Step 1: Add Marketplace
```bash
/plugin marketplace add hiyenwong/ai_collection
```

### Step 2: Install a Plugin
```bash
# Install core agents (recommended first)
/plugin install openclaw-core@openclaw-ai-collection

# Or install by domain:
/plugin install openclaw-neuroscience@openclaw-ai-collection   # Brain science
/plugin install openclaw-coding@openclaw-ai-collection         # Dev tools
/plugin install openclaw-data@openclaw-ai-collection           # Data & finance
/plugin install openclaw-research@openclaw-ai-collection       # Research tools
```

### Step 3: Use Skills & Agents
- **Skills:** Type in Claude Code; trigger keywords activate automatically
- **Agents:** Available via `/agent list` or agent selector

### That's It! 🎉

---

## For Maintainers: Implement Marketplace

### Prerequisites
```bash
# Confirm Claude CLI installed
claude --version      # Must be 0.2.0+

# Verify you're in repo root
ls -la collection/skills collection/agents
```

### 3-Step Implementation

#### Step 1: Create Directory Structure (5 minutes)
```bash
# Clone/update repo
git clone https://github.com/hiyenwong/ai_collection.git
cd ai_collection
git checkout -b feat/plugin-marketplace

# Create plugins directory
mkdir -p .claude-plugin plugins

# Create 5 domain plugins
for plugin in openclaw-core openclaw-neuroscience openclaw-coding openclaw-data openclaw-research; do
  mkdir -p "plugins/$plugin/.claude-plugin"
  mkdir -p "plugins/$plugin/skills"
  mkdir -p "plugins/$plugin/agents"
done
```

#### Step 2: Symlink Skills & Agents (20 minutes)
```bash
# Run automation script (after it's created)
python scripts/create-marketplace-symlinks.py

# Or manually symlink key plugins:
cd plugins/openclaw-core/skills
ln -s ../../../collection/skills/security-guardrails
ln -s ../../../collection/skills/skill-extractor
cd ../../../

# Repeat for other plugins (see PLUGIN_DECOMPOSITION.md)
```

#### Step 3: Add Configuration Files (5 minutes)

**Create `.claude-plugin/marketplace.json`**
```bash
# Copy template from MARKETPLACE_BLUEPRINT.md section 4
# Save to .claude-plugin/marketplace.json
```

**Create plugin manifests**
```bash
for plugin in openclaw-core openclaw-neuroscience openclaw-coding openclaw-data openclaw-research; do
  cat > "plugins/$plugin/.claude-plugin/plugin.json" << EOF
{
  "name": "$plugin",
  "description": "$(grep -A1 "^| \*\*$plugin" docs/marketplace/PLUGIN_DECOMPOSITION.md | tail -1 | cut -d'|' -f3)",
  "version": "1.0.0"
}
EOF
done
```

### Validate Installation (2 minutes)
```bash
# Check syntax
claude plugin validate .

# Test locally
/plugin marketplace add ./

# Install a plugin to verify
/plugin install openclaw-core@openclaw-ai-collection

# Should see no errors ✅
```

### Push to Production (3 minutes)
```bash
git add .claude-plugin plugins docs/marketplace
git commit -m "feat: add claude code plugin marketplace"
git push origin feat/plugin-marketplace

# Create PR, get review, merge to main
# That's it! Auto-published on GitHub
```

**Total time:** ~40 minutes first run | ~2 minutes subsequent releases (just git push)

---

## Common Questions

### Q: Do users need to uninstall the old way?
**A:** No, both paths work in parallel. Users can use whichever they prefer.

### Q: How do I add new skills to the marketplace?
**A:** Just add to `collection/skills/` as usual. The marketplace automatically picks it up on next commit (no manual steps).

### Q: Can I update a plugin without updating all of them?
**A:** Yes, users can install/update individual plugins independently.

### Q: What if I make a mistake?
**A:** All changes are git commits. Just revert:
```bash
git revert <commit-hash>
git push
```
Users' plugins auto-update to the corrected version.

### Q: How do I roll back to script installation if marketplace breaks?
**A:** Users can uninstall and use original path:
```bash
/plugin uninstall openclaw-core@openclaw-ai-collection
python scripts/install.py --scope user --skills
```

---

## Need Help?

- **Implementation issues?** See [IMPLEMENTATION_CHECKLIST.md](./IMPLEMENTATION_CHECKLIST.md)
- **Design questions?** See [MARKETPLACE_BLUEPRINT.md](../MARKETPLACE_BLUEPRINT.md)
- **Plugin assignments?** See [PLUGIN_DECOMPOSITION.md](./PLUGIN_DECOMPOSITION.md)
- **Troubleshooting?** See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

## What's Next?

After launch (4-6 weeks):

- [ ] Gather user feedback
- [ ] Monitor for issues
- [ ] Plan Version 2.0
  - [ ] Semantic versioning
  - [ ] Stable channel
  - [ ] Custom CLI
  - [ ] Web discovery UI

See full implementation blueprint: [MARKETPLACE_BLUEPRINT.md](../MARKETPLACE_BLUEPRINT.md)
