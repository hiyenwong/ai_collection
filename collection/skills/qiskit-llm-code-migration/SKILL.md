---
name: qiskit-llm-code-migration
description: "LLM+RAG methodology for automated Qiskit code migration across versions. Uses taxonomy-based retrieval to reduce hallucinations and improve migration quality."
category: quantum
---

# qiskit-llm-code-migration

## Description
Hybrid LLM+RAG methodology for automated Qiskit code migration across SDK versions. Uses a taxonomy of migration scenarios as structured, version-specific knowledge source to guide LLMs, significantly reducing hallucinations and improving migration precision. Essential for maintaining quantum codebases amid rapidly evolving Qiskit APIs.

## Activation Keywords
- qiskit code migration
- Qiskit version migration
- quantum code migration LLM
- Qiskit API migration
- quantum SDK migration
- Qiskit refactoring
- quantum technical debt
- qiskit-llm migration
- 量子代码迁移
- Qiskit 版本升级

## Tools Used
- terminal: Run migration scripts, test migrated code
- web_search: Search for Qiskit version changelogs and migration guides
- write_file: Create migration taxonomy, SKILL.md
- read_file: Read Qiskit codebase and migration taxonomy
- web_extract: Extract Qiskit API documentation and migration scenarios

## Usage Patterns

### Pattern 1: Taxonomy-based RAG Migration
Automate Qiskit code migration using a structured taxonomy of migration scenarios as the retrieval knowledge source. The taxonomy maps version-specific API changes to refactoring patterns, enabling LLMs to produce accurate migration suggestions without hallucination.

### Pattern 2: Restrictive vs Unconstrained Retrieval
Two retrieval schemes for different migration complexity:
- **Restrictive**: Only retrieve from taxonomy entries matching the detected migration pattern. Reduces hallucinations but may miss edge cases.
- **Unconstrained**: Broader retrieval with LLM synthesis. Better for complex refactoring but higher hallucination risk.

### Pattern 3: Complex Refactoring Detection
Detect migration scenarios that require multi-step refactoring (e.g., API + parameter + import changes) using the taxonomy as a structured guide for LLMs.

## Instructions for Agents

### Step 1: Build Migration Taxonomy
1. Parse Qiskit version changelogs and API diffs
2. Categorize migration scenarios into a structured taxonomy:
   - **API changes**: renamed methods, removed functions, new signatures
   - **Parameter changes**: deprecated parameters, type changes, default value changes
   - **Import changes**: module reorganization, namespace changes
   - **Behavioral changes**: different output formats, changed semantics
3. For each scenario, document:
   - Pre-migration code pattern (old version)
   - Post-migration code pattern (new version)
   - Complexity level (simple rename vs multi-step refactor)

### Step 2: Detect Migration Needs
1. Analyze the target Qiskit codebase for API usage patterns
2. Match detected patterns against the taxonomy to identify required migrations
3. Classify each migration by complexity (simple/medium/complex)

### Step 3: Apply LLM+RAG Migration
1. **For simple migrations**: Use restrictive retrieval — fetch only the matching taxonomy entry and apply the known transformation
2. **For medium migrations**: Use constrained retrieval — fetch related taxonomy entries for context
3. **For complex migrations**: Use unconstrained retrieval — fetch broader context and let LLM synthesize multi-step refactoring
4. Generate migrated code with explanations of each change

### Step 4: Validate Migration
1. Run the migrated code against the target Qiskit version
2. Check for syntax errors, import errors, and runtime failures
3. Compare output behavior with original code (if possible)
4. Flag any remaining issues for manual review

### Step 5: Iterate and Update Taxonomy
1. Collect migration failures and edge cases
2. Add new entries to the taxonomy for future reuse
3. Update complexity classifications based on real-world results

## Error Handling

### LLM Hallucination
- **Symptom**: LLM generates code that uses non-existent APIs or incorrect signatures
- **Fix**: Switch to restrictive retrieval mode; use taxonomy entries as ground truth; validate all generated code against actual Qiskit API docs

### Complex Refactoring Missed
- **Symptom**: Simple pattern match misses multi-step refactoring needed
- **Fix**: Use unconstrained retrieval mode; enable LLM synthesis with broader context from taxonomy

### Taxonomy Outdated
- **Symptom**: Taxonomy doesn't cover latest Qiskit version changes
- **Fix**: Rebuild taxonomy from latest changelogs; use `web_extract` to fetch Qiskit release notes

### Version Ambiguity
- **Symptom**: Code uses deprecated APIs across multiple versions
- **Fix**: Run taxonomy-based detection for each version step; apply migrations sequentially (v1→v2, v2→v3, etc.)

## Best Practices

1. **Taxonomy-first approach**: Always build/update the taxonomy before migration — it's the single source of truth that prevents hallucination
2. **Restrictive by default**: Start with restrictive retrieval; only widen scope when migrations fail
3. **Validate every migration**: Never trust LLM output without running the migrated code
4. **Incremental migration**: For large codebases, migrate in small batches and validate each batch
5. **Document edge cases**: Every migration failure is a taxonomy entry waiting to be written

## Pitfalls

- **Qiskit API volatility**: Qiskit evolves rapidly — taxonomy must be updated frequently. Stale taxonomy entries may produce incorrect migrations.
- **LLM hallucination**: Without taxonomy grounding, general-purpose LLMs produce unreliable migration suggestions. The taxonomy is NOT optional — it's the core mechanism.
- **Google Gemini vs GPT performance**: Google Gemini Flash-2.5 shows superior performance in detecting complex refactoring scenarios compared to GPT-oss-20b. Prefer Gemini for complex migrations.
- **Restrictive scheme trade-off**: Restrictive retrieval reduces hallucinations but may miss complex multi-step refactoring. Use unconstrained for complex cases.
- **Testing coverage**: Migrated code may compile but produce different numerical results. Always validate output behavior, not just syntax.

## References
- arXiv: 2606.20173 — "Qiskit Code Migration with LLMs" (Sonawane et al., 2026)
- Qiskit SDK documentation: https://docs.quantum.ibm.com/
- Qiskit changelog: https://github.com/Qiskit/qiskit/releases

## Related Skills
- `automated-quantum-software-engineering` — broader QSE automation
- `quantum-program-linting` — quantum code quality analysis
- `quantum-program-analysis` — LLM-powered quantum code QA
