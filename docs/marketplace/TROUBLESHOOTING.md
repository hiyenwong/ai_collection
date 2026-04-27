---
title: Marketplace Troubleshooting Guide
date: 2026-04-27
---

# OpenClaw Marketplace Troubleshooting

Quick reference for common issues and solutions.

---

## For Users

### Installation Issues

#### ❌ `/plugin marketplace add` Command Not Found
**Symptoms:** `command not found: /plugin` or error when typing `/plugin`

**Causes:**
- Claude Code version too old (need v0.2.0+)
- Not in Claude Code editor (plugin commands only work in Claude Code)

**Solutions:**
1. Update Claude Code:
   ```bash
   claude update
   claude --version    # Should be 0.2.0+
   ```
2. Try from Claude Code editor (not terminal/chat)
3. Check if in correct environment: `which claude`

---

#### ❌ "Marketplace Not Found" Error
**Symptoms:** 
```
Error: Marketplace 'openclaw-ai-collection' not found
```

**Causes:**
- Typo in marketplace name
- Network issue preventing GitHub access
- Marketplace entry not yet published

**Solutions:**
1. Verify exact name:
   ```bash
   /plugin marketplace add hiyenwong/ai_collection
   ```
   (Use GitHub format if provided)

2. Check network connectivity:
   ```bash
   curl -I https://github.com/hiyenwong/ai_collection
   ```

3. Refresh marketplace cache:
   ```bash
   /plugin marketplace update openclaw-ai-collection
   ```

4. If still failing, use fallback:
   ```bash
   python scripts/install.py --scope user --skills --agents
   ```

---

#### ❌ Plugin Installation Hangs or Times Out
**Symptoms:** Command appears to run forever, no completion message

**Causes:**
- Large plugin (e.g., openclaw-neuroscience with 400+ skills)
- Network latency
- Symlinks being resolved during cache copy

**Solutions:**
1. **Wait longer** — Large plugins (400+ skills) take 30-60 seconds
   
2. **Cancel and retry:**
   ```bash
   # Press Ctrl+C to cancel
   /plugin cache clear
   /plugin install openclaw-core@openclaw-ai-collection  # Try smaller plugin first
   ```

3. **Check system resources:**
   ```bash
   df -h                    # Check disk space (need ~500MB for cache)
   ps aux | grep claude     # Verify Claude process running
   ```

4. **If stuck for >2 minutes:**
   ```bash
   killall -9 claude        # Force quit Claude
   /plugin cache clear
   # Try again
   ```

---

#### ❌ "Symlink Resolution Failed" During Installation
**Symptoms:**
```
Error: Failed to resolve symlink collection/skills/foo-skill
```

**Causes:**
- Symlink broken (target file moved/deleted)
- On Windows (symlinks need special permissions)
- Incomplete marketplace download

**Solutions:**
1. **Verify repository is complete:**
   ```bash
   cd ai_collection
   git status                    # Should show clean or expected changes
   git fetch origin main
   git reset --hard origin/main  # Reset to latest
   ```

2. **Check symlinks locally:**
   ```bash
   find plugins -type l -exec ls -l {} \;
   # Should show: plugins/openclaw-*/skills/foo -> ../../../collection/skills/foo
   ```

3. **On Windows (Windows Subsystem for Linux required):**
   - Use WSL: `wsl ubuntu`
   - Or copy files instead of symlinks (maintainer responsibility)

4. **Fallback to script:**
   ```bash
   /plugin uninstall openclaw-core@openclaw-ai-collection
   python scripts/install.py --scope user --skills
   ```

---

### Skill & Agent Discovery Issues

#### ❌ Skills Not Being Recognized
**Symptoms:** Trigger keywords don't activate skills; `/agent list` empty

**Causes:**
- Plugin not installed
- Skills not loaded after installation
- Trigger keywords spelled differently than documented

**Solutions:**
1. **Verify plugin is installed:**
   ```bash
   /plugin list
   # Should show: openclaw-core@openclaw-ai-collection (enabled)
   ```

2. **Force reload:**
   ```bash
   /plugin cache clear
   /plugin marketplace update openclaw-ai-collection
   # Restart Claude Code
   ```

3. **Check trigger keywords:**
   ```bash
   # Type the skill name directly in Claude Code, e.g.:
   @security-guardrails
   # Or use trigger keywords from SKILL.md
   ```

4. **Verify skill is in your plugin:**
   ```
   User: What skills are in openclaw-core?
   Expected: Lists security-guardrails, skill-extractor, etc.
   ```

---

#### ❌ Only Some Skills Visible
**Symptoms:** Some skills work, others don't; inconsistent availability

**Causes:**
- Mixed installation (some from marketplace, some from script)
- Partial download/cache corruption
- Skill conflict with same trigger keyword

**Solutions:**
1. **Clean installation:**
   ```bash
   /plugin uninstall openclaw-*@openclaw-ai-collection
   /plugin cache clear
   /plugin install openclaw-core@openclaw-ai-collection  # Start fresh
   ```

2. **Check for conflicts:**
   - Two plugins shouldn't have same skill
   - If they do, see PLUGIN_DECOMPOSITION.md conflict resolution

3. **Verify no mixed paths:**
   ```bash
   # If you have ~/.claude/skills/ from script, AND marketplace:
   # This is OK (they coexist), but can be confusing
   ```

---

### Update & Versioning Issues

#### ❌ Changes Not Appearing After Commit
**Symptoms:** Pushed new skills but they're not available in installed plugin

**Causes:**
- Cache not updated
- New commit on `main` not yet public
- Local cache is stale

**Solutions:**
1. **Force marketplace update:**
   ```bash
   /plugin marketplace update openclaw-ai-collection
   ```

2. **Clear cache:**
   ```bash
   /plugin cache clear
   /plugin install openclaw-core@openclaw-ai-collection
   ```

3. **Verify GitHub has latest:**
   ```bash
   git push origin main              # Ensure your commit is pushed
   git log origin/main --oneline -5  # Verify on GitHub
   ```

4. **Wait for GitHub:**
   - GitHub mirrors take ~1-2 minutes to sync
   - Try again in 5 minutes

---

#### ❌ Plugin Rolled Back or Reverted
**Symptoms:** Plugin version went backwards; skills disappeared

**Causes:**
- Maintainer did `git revert` to fix a bug
- Large commit was split into smaller ones
- Version based on commit SHA, not explicit version number

**Solutions:**
1. **This is expected behavior** — Plugins track commit SHA
   - If maintainer reverts, version goes back
   - This ensures you don't run broken code

2. **To get latest again:**
   ```bash
   /plugin marketplace update openclaw-ai-collection
   # Next session will have latest from main
   ```

3. **To stay on specific version** (not MVP):
   - Use stable channel (planned for v2.0)
   - Or manually install from Git tag

---

## For Maintainers

### Repository & Git Issues

#### ❌ Symlinks Appear as Text Files on Git
**Symptoms:** 
```
git diff shows:
- collection/skills/foo-skill/...
+ symlink -> ../../../collection/skills/foo-skill
```

**Causes:**
- Windows git config doesn't support symlinks
- Repository cloned with core.symlinks=false

**Solutions:**
1. **Enable symlinks in git config:**
   ```bash
   git config core.symlinks true
   ```

2. **Recreate symlinks:**
   ```bash
   git checkout plugins/
   ```

3. **For CI/CD on Windows:**
   - Add post-checkout hook to recreate symlinks
   - Or commit copies instead of symlinks (platform-specific)

---

#### ❌ Validation Fails: "Invalid plugin.json"
**Symptoms:**
```
Error: plugins/openclaw-core/.claude-plugin/plugin.json is invalid
```

**Causes:**
- JSON syntax error (missing quote, comma, bracket)
- Required field missing

**Solutions:**
1. **Validate JSON syntax:**
   ```bash
   python3 -m json.tool plugins/openclaw-core/.claude-plugin/plugin.json
   # Should print formatted JSON, not error
   ```

2. **Check required fields:**
   ```bash
   # Must have: name, description
   # Optional but recommended: version
   ```

3. **Fix common issues:**
   ```json
   // ❌ WRONG: Trailing comma
   { "name": "openclaw-core", }
   
   // ❌ WRONG: Single quotes
   { 'name': 'openclaw-core' }
   
   // ✅ RIGHT
   { "name": "openclaw-core" }
   ```

---

#### ❌ Marketplace.json Validation Fails
**Symptoms:**
```
Error: .claude-plugin/marketplace.json does not match schema
```

**Causes:**
- Missing required top-level fields
- Plugin source path doesn't exist
- Typo in field names

**Solutions:**
1. **Verify required fields:**
   ```json
   {
     "name": "...",           // ✅ required
     "owner": { ... },        // ✅ required
     "pluginRoot": "./plugins", // ✅ required
     "plugins": [ ... ]       // ✅ required
   }
   ```

2. **Check plugin source paths:**
   ```bash
   # Each plugin must have corresponding directory
   ls -la plugins/openclaw-core/.claude-plugin/plugin.json  # Must exist
   ```

3. **Use official template:**
   - Copy exactly from MARKETPLACE_BLUEPRINT.md section 4
   - Replace only values, not structure

---

### Symlink & Directory Issues

#### ❌ Broken Symlinks After Symlinking
**Symptoms:**
```
ls -l plugins/openclaw-core/skills/security-guardrails
# Shows: ... -> ../../../collection/skills/security-guardrails (broken)
```

**Causes:**
- Relative path calculation wrong
- Symlink created from wrong directory
- Target directory doesn't exist in collection/

**Solutions:**
1. **Verify correct relative path:**
   ```bash
   # If symlink in: plugins/openclaw-core/skills/
   # And target in: collection/skills/
   # Then symlink should be: ../../../collection/skills/foo
   
   # Test: cd plugins/openclaw-core/skills && ls -l ../../..
   # Should show collection/ directory
   ```

2. **Recreate symlink if wrong:**
   ```bash
   rm plugins/openclaw-core/skills/security-guardrails
   cd plugins/openclaw-core/skills
   ln -s ../../../collection/skills/security-guardrails
   cd ../../../
   ls -l plugins/openclaw-core/skills/security-guardrails  # Should now work
   ```

3. **Use absolute paths as fallback** (if relative fails):
   ```bash
   ln -s /absolute/path/to/ai_collection/collection/skills/security-guardrails
   # Then convert to relative (for portability)
   ```

---

#### ❌ Plugin Directory Missing Skills or Agents
**Symptoms:**
```
ls plugins/openclaw-neuroscience/skills/
# Shows only 5 files, expected 400+
```

**Causes:**
- Symlink creation script didn't complete
- Filtered wrong categories
- Repository wasn't pulled with latest skills

**Solutions:**
1. **Check if script ran successfully:**
   ```bash
   python scripts/create-marketplace-symlinks.py 2>&1 | tail -20
   # Should show "✓ Created: ..." for each skill
   ```

2. **Verify collection/ has skills:**
   ```bash
   ls collection/skills/ | wc -l  # Should show 966+
   ls collection/skills/ | grep -i snn  # Neuroscience test
   ```

3. **Rerun symlink creation:**
   ```bash
   # Clean up first
   find plugins -type l -delete
   # Recreate
   python scripts/create-marketplace-symlinks.py
   ```

---

### Validation & Testing Issues

#### ❌ `claude plugin validate` Fails
**Symptoms:**
```
Error: Validation failed (see details below)
```

**Causes:**
- Missing marketplace.json
- Broken JSON syntax
- Missing plugin.json files
- Symlinks invalid

**Solutions:**
1. **Run validation with verbose output:**
   ```bash
   claude plugin validate . --verbose
   # Shows exactly what failed
   ```

2. **Check all files exist:**
   ```bash
   test -f .claude-plugin/marketplace.json && echo "✓ marketplace.json"
   for dir in plugins/*/; do
     test -f "$dir/.claude-plugin/plugin.json" && echo "✓ $dir/plugin.json"
   done
   ```

3. **Fix one issue at a time:**
   - Fix first error, validate again
   - Repeat until all pass

---

#### ❌ Local Installation Test Fails
**Symptoms:**
```
/plugin marketplace add ./
# Error: Failed to add marketplace
```

**Causes:**
- Marketplace.json invalid
- Working directory not repo root
- Claude Code not recognizing local path

**Solutions:**
1. **Ensure in correct directory:**
   ```bash
   pwd                                      # Should end in: ai_collection
   test -f .claude-plugin/marketplace.json  # Should exist
   ```

2. **Use absolute path:**
   ```bash
   /plugin marketplace add /absolute/path/to/ai_collection
   ```

3. **Test marketplace.json first:**
   ```bash
   python3 -m json.tool .claude-plugin/marketplace.json  # Must succeed
   ```

4. **Try specific plugin instead:**
   ```bash
   /plugin install openclaw-core@openclaw-ai-collection
   # If this works, marketplace is OK
   ```

---

### Release & Distribution Issues

#### ❌ Changes Not Visible on GitHub
**Symptoms:**
```
git push succeeds, but GitHub page not updated
```

**Causes:**
- Push to wrong branch (not main)
- Browser cache (seeing old version)
- GitHub not refreshed

**Solutions:**
1. **Verify push target:**
   ```bash
   git push -u origin main
   git log origin/main --oneline -1  # Verify on GitHub
   ```

2. **Clear browser cache:**
   - Force refresh: Cmd+Shift+R (macOS) or Ctrl+Shift+F5 (Windows)
   - Or view raw: `https://raw.githubusercontent.com/hiyenwong/ai_collection/main/.claude-plugin/marketplace.json`

3. **Verify file is committed:**
   ```bash
   git ls-files .claude-plugin/
   # Should show: .claude-plugin/marketplace.json
   ```

---

#### ❌ Remote Installation Fails (But Local Works)
**Symptoms:**
```
Local: /plugin marketplace add ./           # ✅ Works
Remote: /plugin marketplace add hiyenwong/ai_collection  # ❌ Fails
```

**Causes:**
- GitHub URL format wrong
- Repository not public
- Network blocking GitHub

**Solutions:**
1. **Verify correct GitHub URL:**
   ```bash
   curl -I https://raw.githubusercontent.com/hiyenwong/ai_collection/main/.claude-plugin/marketplace.json
   # Should return HTTP 200
   ```

2. **Check repository is public:**
   - Go to `https://github.com/hiyenwong/ai_collection/settings`
   - Verify "Private" toggle is OFF

3. **Test network access:**
   ```bash
   ping github.com
   curl https://github.com/hiyenwong/ai_collection  # Should work
   ```

---

## Nuclear Option: Full Reset

If everything is broken:

### For Users
```bash
# 1. Uninstall everything
/plugin uninstall openclaw-*@openclaw-ai-collection

# 2. Clear cache completely
/plugin cache clear

# 3. Start fresh
/plugin marketplace add hiyenwong/ai_collection
/plugin install openclaw-core@openclaw-ai-collection

# 4. If still broken, revert to script
python scripts/install.py --scope user --skills --agents
```

### For Maintainers
```bash
# 1. Reset repository
git reset --hard origin/main
git clean -fd

# 2. Recreate marketplace from scratch
rm -rf .claude-plugin plugins
python scripts/create-marketplace-symlinks.py

# 3. Validate
claude plugin validate .

# 4. Test
/plugin marketplace add ./
/plugin install openclaw-core@openclaw-ai-collection

# 5. Push
git add .claude-plugin plugins
git commit -m "chore: rebuild marketplace from scratch"
git push origin main
```

---

## Getting Help

Still stuck? Open GitHub issue with:
- [ ] Output of `claude --version`
- [ ] Exact error message (copy-paste)
- [ ] Steps to reproduce
- [ ] Output of relevant commands above

Or ask in Discord/community channels.

---

**Last Updated:** 2026-04-27  
**Marketplace Version:** 1.0.0 (MVP)
