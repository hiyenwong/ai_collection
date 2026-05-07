# CI Validation Reference

## Pre-existing CI Failures (observed 2026-05-04 to 2026-05-05)

The `Validate Skills & Agents` workflow has been failing for 5+ consecutive pushes. These failures are **NOT caused by newly created skills** — they are pre-existing issues in the ai_collection repository.

### Failure Pattern

**1. Validate Skills** (`scripts/validate_skill.py`)
- ~37 out of 1816+ skills have warnings/errors
- Common issues:
  - Missing arXiv ID
  - Missing Abstract or Key Contributions section
  - Lines exceeding 120 characters
  - Uncommon tool entries (empty strings)
  - No code blocks in skills that need examples
- Exit code: 1 (treated as failure despite being warnings)

**2. Lint Python Scripts** (`ruff check`)
- 28 errors across old quantum skill scripts
- Error types:
  - F401: Unused imports (typing.Optional, typing.Union, numpy, sys, json, pennylane, etc.)
  - F541: f-string without placeholders (e.g., `f"Note: PDF extraction requires pdfplumber"`)
  - E722: Bare `except` clause
  - F841: Unused local variables
  - F821: Undefined name (`Tuple` used without importing from typing)
- 18 errors auto-fixable with `ruff --fix`
- 8 hidden fixes with `--unsafe-fixes`

### Newly Created Skills Status

New skills created via the research workflow consistently pass validation:
- `llm-agent-externalization` (arXiv: 2604.08224) — ✅ PASSED (May 2026)
- Other recent skills — ✅ PASSED

### Resolution Options

1. **Quick fix for ruff**: `ruff check --fix collection/skills/` to auto-fix 18+ errors
2. **Validator adjustment**: Modify `validate_skill.py` to exit 0 when only warnings exist
3. **Bulk skill repair**: Systematically fix the 37 skills with missing sections/arXiv IDs
4. **Ignore for now**: New skills pass validation; failures are in legacy content
