# Claude Code Timeout Recovery Patterns

## Core Insight
Claude Code frequently times out at the 600s default limit on complex multi-file tasks
(10+ new files, large refactors). **A timeout does NOT mean zero output.** Claude Code
writes files incrementally, so partial results are often 80-90% complete.

## Recovery Protocol

### Step 1: Assess what was produced
```bash
git status --short          # See modified/new files
git diff --cached --stat    # See staged changes
git diff src/<file>         # Inspect specific file
```

### Step 2: Fix common compilation errors

**Rust — Missing struct field initialization:**
Claude Code adds fields to structs but forgets constructors:
```rust
// Error: missing field `retrieval_weights` in initializer
pub fn open(path: P) -> Result<Self> {
    Ok(Self { conn })  // ← missing field
}
// Fix:
Ok(Self { conn, retrieval_weights: Cell::new(Default::default()) })
```

**Rust — rusqlite NULL handling:**
```rust
// Fails when column is NULL:
let val: String = row.get(3)?;  // InvalidColumnType

// Fix with Option:
let val: Option<String> = row.get(3)?;
let properties = match val {
    Some(json) => serde_json::from_str(&json).unwrap_or_default(),
    None => HashMap::new(),
};
```

**Rust — Dead code warnings on new fields:**
Add accessor methods (getter/setter) to make the field read.

### Step 3: Run tests
```bash
cargo test --no-default-features  # Skip async features if they have pre-existing issues
```

## Print Mode Tuning
- Multi-file tasks (3-10 files): `--max-turns 30`
- Large refactors (>10 files): prefer interactive tmux mode so you can monitor progress
- Use `--model sonnet` for coding tasks (best quality/speed tradeoff)
- For Rust projects: always run `cargo fmt` before committing Claude Code output

## Known Pre-existing Issues
- `src/async_kg/mod.rs` has a pre-existing edition parse error (`async fn not permitted in Rust 2015`) that does not affect `--no-default-features` builds. This is a known upstream issue, not caused by Claude Code edits.
