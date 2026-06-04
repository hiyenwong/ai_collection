# Duplicate Skills Detected (2026-05-26 Cron Session)

During today's duplicate check (`grep -rl` across all skill directories), these overlapping skills were found:

| arXiv Paper | Duplicate Skills (all in ai_collection/) |
|------------|------------------------------------------|
| 2605.22097 (Q-PhotoNAS) | `q-photonas-quantum-nas` + `q-photonas-hybrid-arch-search` |
| 2605.21346 (QML Advantage) | `quantum-ml-advantage-noisy` + `coherent-quantum-inference` + `qml-advantage-noisy-qubits` |
| 2605.22922 (Photonic Hopfield) | `photonic-quantum-hopfield-memory` + `quantum-hopfield-associative-memory` + `quantum-associative-memory-photonic` |

**Action needed**: Merge duplicates. Keep the one with richer SKILL.md content, update its frontmatter to cover all arXiv IDs, delete the rest. Update INDEX.md entries to point to the retained skill.

## How to resolve
1. Compare SKILL.md content across duplicates
2. Pick the most comprehensive one
3. Add missing arXiv IDs to retained skill's metadata
4. Delete the others (with `absorbed_into=<retained-name>`)
5. Update INDEX.md entries
