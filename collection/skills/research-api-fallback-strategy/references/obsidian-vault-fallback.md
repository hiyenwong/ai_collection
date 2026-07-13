# Obsidian Vault Paper Notes Fallback

**Tier 0.5 fallback** for automated research when all external APIs fail. Use after checking workspace JSON caches, before falling to kg.db.

## When to Use

- Scheduled cron jobs with domain-specific focus (RL, quantum, neuroscience)
- All external APIs (arXiv, web_search, web_extract) are blocked or rate-limited
- Obsidian vault contains curated paper notes from past research sessions
- Need to integrate existing knowledge into domain-specific skill library

## Pattern (Verified 2026-06-09)

Search the Obsidian vault for existing paper notes in general directories (Deep Learning/, Quantum Computing/) that haven't been indexed in domain-specific subdirectories (reinforcement-learning/, quantum-ml/).

### Bash Pattern

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research"

# Search for domain keywords in general directories
# Example: RL papers in Deep Learning directory
search_files(
    path="$VAULT/Deep Learning",
    pattern="reinforcement|policy|reward|actor-critic|PPO|GRPO|Q-learning|DQN",
    target="content",
    file_glob="*.md"
)
```

### Workflow Steps

1. **Search vault** for domain keywords using `search_files(target="content")`
2. **Identify unindexed papers** — papers in general directories not yet in domain-specific subdirectories
3. **Score top papers** (3-5 candidates):
   - Innovation: new method/framework?
   - Practicality: reusable algorithm/pattern?
   - Relevance: fills skill gap?
4. **Create skills** — extract methodology, algorithms, key insights
5. **Create Obsidian notes** — move to domain directory with proper formatting
6. **Update INDEX.md** — add entries with arXiv ID, topic, skill link, note link

### Real-World Example (2026-06-09 RL Cron)

**Context**: RL paper research cron job, all APIs blocked (arXiv 429, web_search NoneType, execute_code blocked).

**Discovery**:
```bash
search_files(path="$VAULT/Deep Learning", pattern="reinforcement", target="content")
# Found 31 RL-related papers in Deep Learning/ directory
```

**Selection** (Top 3 scored by innovation + practicality):
1. **Performance Variation in Deep RL (2606.06746)** — percentile-based evaluation framework for run-to-run robustness
2. **Reward Hacking Prevention in Physical Control (2606.06227)** — deployment safety for physical control systems
3. **MA-AC-MPC Multi-Agent Hardware (2606.06011)** — 100% success rate on real hardware validation

**Output**:
- 3 new skills in `~/.hermes/skills/ai_collection/reinforcement-learning/`
- 3 new Obsidian notes in `VAULT/Research/reinforcement-learning/`
- INDEX.md updated with 2026-06-09 Papers section

**Time**: ~10 minutes total (no network dependency)

## Advantages vs Other Fallbacks

| Source | Metadata Quality | Network Dependency | Setup Required |
|--------|------------------|--------------------|-----------------|
| **Obsidian Vault Notes** | Full notes, abstracts, arXiv IDs, wikilinks | None | Vault exists (default) |
| Workspace JSON Caches | Paper metadata (id, title, abstract) | None | Cron job creates them |
| kg.db | Abstract + graph metrics | None | KG populated by past sessions |
| web_search | Live results | **Required** | Working HTTP client |
| arXiv API | Live results | **Required** | Working API endpoint |

**Key advantage**: Obsidian notes have richer context than kg.db — full paper notes with methodology, formulas, and wikilinks to related concepts.

## Integration with Other Fallbacks

Use Obsidian vault fallback in this sequence:

```
Tier 0: Workspace JSON caches (fastest)
Tier 0.5: Obsidian vault paper notes (this pattern) ← NEW
Tier 1: arXiv API (primary, when available)
Tier 2: web_search (secondary)
Tier 3: kg.db + kg_tool (deep analysis)
```

## Vault Path

Default Obsidian vault path (iCloud synced):
```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
```

The `~` in `iCloud~md~obsidian` is a literal tilde, not home-directory expansion.

## Pitfalls

### iCloud Path Space Handling

The vault path contains spaces. Always use double-quoted variables:

```bash
# ❌ Wrong: unquoted $VAULT
cat $VAULT/Research/INDEX.md

# ✅ Correct: quoted "$VAULT"
cat "$VAULT/Research/INDEX.md"
```

### search_files vs grep

Prefer `search_files` tool over `grep` in terminal — handles paths with spaces correctly and returns structured results.

### Terminal Heredoc for iCloud Paths

`write_file` may silently fail on iCloud paths with spaces. Use terminal heredoc for note creation:

```bash
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir -p "$VAULT/Research/reinforcement-learning"
cat > "$VAULT/Research/reinforcement-learning/Paper Name.md" << 'EOF'
# Paper content here
EOF
```

Always verify creation:
```bash
ls -la "$VAULT/Research/reinforcement-learning" | grep "Paper Name"
```

## Related Patterns

- `research-api-fallback-strategy` → Tier 0 JSON caches
- `kgdb-two-schemas.md` → kg.db fallback
- `obsidian` skill → Vault operations

## Activation Keywords

- obsidian vault fallback
- paper notes fallback
- zero-api research
- vault paper search
- obsidian 论文笔记备用策略