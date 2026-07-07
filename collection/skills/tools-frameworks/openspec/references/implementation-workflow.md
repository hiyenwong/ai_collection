# OpenSpec Implementation Workflow (Rust Project Pattern)

Discovered during the Migi symbiotic AI agent project — a reliable manual implementation 
workflow when Claude Code is unavailable, and a general pattern for spec-driven Rust projects.

## When to Use

- Claude Code returns 403 on Pro accounts (org policy blocks CLI API)
- You need deterministic, step-by-step quality-gated progress
- The project has detailed OpenSpec specs ready
- You want to avoid context-window degradation of long AI coding sessions

## Workflow (per phase)

### 1. Read the Spec

Read the spec file. Identify all requirements and `#### Scenario:` blocks.
Each scenario is a test case.

### 2. Implement One Phase at a Time

Start with the foundational layer, work upward following dependency chain:

```
config → error → observer → learner → intervener → trust → main
```

Layer dependency is ONE-WAY — never reverse-import.

Implementation pattern per file:
- Module doccomment with purpose and metaphor
- Public types with full doc
- Constructor + public API methods
- One `#[cfg(test)]` test per OpenSpec scenario

### 3. Quality Gates (per module, never skip)

```bash
cargo fmt
cargo clippy -- -D warnings
cargo test
```

Fix until all three pass before the next file. Clippy `-D warnings` is non-negotiable.

### 4. Atomic Commit with CHANGELOG

```bash
git add -A
git commit -m "feat: implement <feature> (Phase N)"

# Update CHANGELOG.md: list additions, note running test count
```

### 5. Convention: State Running Test Count

Each commit message and CHANGELOG entry includes the running test count. 
This gives immediate confidence that nothing regressed.

## Key Design Patterns from Migi

| Pattern | Description |
|---------|-------------|
| **Encrypted Secrets** | AES-256-GCM for API keys, separate CLI tool |
| **Sandbox Simulation** | Fake event sources + scenario engine to test lifecycle offline |
| **State Snapshots** | Periodic JSON snapshots to `var/` for external monitoring CLI |
| **`--monitor` flag** | CLI flag to produce snapshots for monitoring tools |
| **Monitoring CLI** | Separate binary reads snapshots from disk — zero IPC |

## When to Skip Claude Code

If Claude Code fails (403, timeout), the manual pipeline is faster:
- No dialog handling overhead
- No context window degradation
- Full commit granularity
- Verified: 7 phases, 79 tests, 10 commits in ~2 hours
