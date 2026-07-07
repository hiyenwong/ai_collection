# Agent Contract Reference

Quick reference for all 4 agent contract preconditions and postconditions. Source: `contracts/*.py`

## Research Agent (`contracts/research.py`)

### Preconditions (blocks LLM call if failed)
| Check | Field | Type | Requirement |
|---|---|---|---|
| `query_is_nonempty` | `query` | string | Must be non-empty |
| `knowledge_sources_exist` | `available_sources` | list | Must have ≥1 source |

### Postconditions
| Check | Field | Requirement | Severity |
|---|---|---|---|
| `output_has_sources` | `sources` | ≥3 sources | high |
| `sources_have_references` | `sources[].url` or `.path` | Every source must have url/path | critical |
| `confidence_is_valid` | `confidence` | "high" / "medium" / "low" | high |
| `gaps_present_if_not_high` | `gaps` | Non-empty if confidence ≠ high | high |

### Invariants
| Check | Requirement | Severity |
|---|---|---|
| `claims_have_sources` | Every claim must have `source_ref` | critical |
| `knowledge_sources_consulted` | Must consult knowledge sources first | high |
| `no_fabricated_urls` | No fabricated URLs | critical |
| `no_unverified_memory_writes` | No unverified memory writes | high |

---

## Planning Agent (`contracts/planning.py`)

### Preconditions (blocks LLM call if failed)
| Check | Field | Type | Requirement |
|---|---|---|---|
| `vision_exists` | `vision` | string | Must be non-empty |
| `research_findings_available` | `research_refs` OR `knowledge_sources` | list | At least one must be non-empty |

### Postconditions
| Check | Field | Requirement | Severity |
|---|---|---|---|
| `phases_present` | `phases` | ≥2 phases | critical |
| `phases_have_deliverables` | `phases[].deliverables` | Each phase must have deliverables | high |
| `dependencies_declared` | `dependencies` | ≥1 dependency | high |
| `risks_have_mitigations` | `risks[].mitigation` | Every risk must have mitigation | medium |
| `research_refs_present` | `research_refs` | Non-empty | high |

### Invariants
| Check | Requirement | Severity |
|---|---|---|
| `all_phases_have_estimates` | Every phase must have `estimate` | medium |
| `blocking_deps_declared` | Phase depends_on targets must exist | high |
| `no_scope_creep` | No phases out of scope | critical |

---

## Build Agent (`contracts/build.py`)

### Preconditions (blocks LLM call if failed)
| Check | Field | Type | Requirement |
|---|---|---|---|
| `plan_exists` | `plan` | dict | Must be non-empty |
| `task_id_provided` | `task_id` | string | Must be non-empty |

### Postconditions
| Check | Field | Requirement | Severity |
|---|---|---|---|
| `tests_passed` | `tests_passed` | `true` | critical |
| `lint_passed` | `lint_passed` | `true` | high |
| `coverage_sufficient` | `coverage` | ≥0.8 | high |
| `contract_compliant` | `contract_compliant` | `true` | critical |
| `task_id_in_plan` | `task_id` in `plan_tasks` | Must be in plan | high |
| `files_registered_in_spec` | `files_registered` | `true` (if new_files present) | medium |

### Invariants
| Check | Requirement | Severity |
|---|---|---|
| `no_secrets` | `has_secrets` must be `false` | critical |
| `no_skipped_tests` | `tests_skipped` must be 0 | critical |
| `files_within_size_limit` | No files > 800 lines | high |
| `no_todos_left` | `has_todos` must be `false` | medium |

---

## Eval Agent (`contracts/eval.py`)

### Preconditions (blocks LLM call if failed)
| Check | Field | Type | Requirement |
|---|---|---|---|
| `spec_file_exists` | `spec_path` | string | Must be non-empty |
| `output_provided` | `target_output` | any | Must not be None |

### Postconditions
| Check | Field | Requirement | Severity |
|---|---|---|---|
| `reasoning_present` | `reasoning` | Length > 20 chars | critical |
| `score_in_range` | `score` | 0.0 ≤ score ≤ 1.0 | critical |
| `feedback_when_below_threshold` | `feedback` | Length > 10 if score < threshold | high |
| `trace_recorded` | `trace_written` | `true` | high |
| `rubric_referenced` | `rubric_used` or `guidelines_referenced` | Non-empty | high |

### Invariants
| Check | Requirement | Severity |
|---|---|---|
| `no_build_context` | `has_build_context` must be `false` | high |
| `no_output_modification` | `has_write_operations` must be `false` | critical |
| `reasoning_is_specific` | Reasoning must not be vague phrases | high |
