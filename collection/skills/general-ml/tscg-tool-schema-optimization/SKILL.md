---
name: tscg-tool-schema-optimization
description: >
  Optimize tool/schema definitions for LLM agent deployments using TSCG principles.
  Converts JSON tool schemas into token-efficient structured text formats that small
  models (4B-14B parameters) can reliably interpret. Use when: (1) agent tool-use
  accuracy drops with many tools (>10), (2) deploying small/medium LLMs as agents,
  (3) optimizing MCP tool schemas for token efficiency, (4) diagnosing tool-use failures
  in production agent systems, (5) designing tool schemas for agentic LLM deployments.
  Based on arXiv:2605.04107 (TSCG paper).
---

# TSCG Tool Schema Optimization

Optimize tool schemas for agentic LLM deployments using the TSCG (Tool-Schema
Compilation Generator) methodology. JSON schemas are designed for machine parsing,
not LLM interpretation — this causes tool-use failures, especially for small models.

## Core Problem

Production agent frameworks (OpenAI Function Calling, Anthropic Tool Use, MCP)
transmit tool schemas as JSON. For small models (4B-14B), this protocol mismatch
causes the majority of tool-use failures at production catalog sizes.

## Key Findings from arXiv:2605.04107

- JSON-to-structured-text conversion restores Phi-4 14B from 0% to 84.4% accuracy at 20 tools
- Formal compression bound: >=51% token reduction on well-formed schemas
- 52-57% token savings persist on heavy production MCP schemas (~10,500 input tokens)
- Eight composable operators handle different schema transformations
- Per-model response profiles: operator-hungry (Opus 4.7), operator-sensitive (GPT-5.2), operator-robust (Sonnet 4)

## Transformation Operators

Apply these operators to convert JSON schemas into LLM-friendly formats:

### 1. Type Simplification
Convert verbose type descriptions to concise forms:
- `{"type": "string", "description": "..."}` → `name: string - description`
- `{"type": "integer", "minimum": 0, "maximum": 100}` → `count: int (0-100)`

### 2. Required Field Grouping
Group required vs optional parameters:
```
Required: user_id (string), query (string)
Optional: limit (int, default=10), sort (enum: asc|desc)
```

### 3. Enum Compression
Compress enum values when they follow patterns:
- `["monday","tuesday","wednesday",...]` → `day_of_week: enum(Mon-Sun)`

### 4. Nested Object Flattening
Flatten nested objects with dot notation:
- `config.filter.type` instead of nested JSON objects

### 5. Constraint Inline
Move constraints into parameter descriptions:
- `timeout: int (1-300 seconds, default=30)`

### 6. Cross-Reference Dedup
Remove redundant type definitions, use references:
- Define common types once, reference by name

### 7. Semantic Grouping
Group related parameters by function:
- `# Authentication: api_key, token, user_id`
- `# Pagination: page, limit, offset`

### 8. Example Inlining
Add minimal examples inline:
- `date: string (YYYY-MM-DD, e.g., "2026-05-07")`

## Output Format Template

```
## {tool_name}
{one-line description}

### Required Parameters
- {param}: {type} - {description} [{constraints}]

### Optional Parameters  
- {param}: {type} - {description} [{constraints}] [default: {value}]

### Returns
{return type and description}

### Example
{minimal usage example}
```

## When to Use

| Scenario | Apply TSCG |
|----------|-----------|
| < 5 tools | No — JSON is fine |
| 5-20 tools | Yes — significant accuracy gain |
| 20+ tools | Critical — small models fail without it |
| Small model (4B-14B) | Always |
| Frontier model (Opus/Sonnet) | Optional — models are robust |

## Model-Specific Guidance

- **Small models (4B-14B)**: Apply all 8 operators — essential for accuracy
- **Mid models (Sonnet 4)**: Apply operators 1-5 — model is robust
- **Large models (Opus 4.7)**: Apply operators 1-3 — model handles complexity

## Pitfalls

- Do not remove semantic information during compression
- Keep parameter names identical to original API (do not rename)
- Test with target model after transformation
- Maintain backward compatibility with JSON schema for non-LLM consumers
