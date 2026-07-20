# KG Research Workflow — Operational Pitfalls

## Arxiv API Rate Limiting (429 Errors)

The arxiv API (`export.arxiv.org/api/query`) consistently returns HTTP 429 (rate limited) errors, both with and without proxy. This happens even for single requests.

**Workaround**: Use `web_search` tool instead of direct API calls:
```
web_search(query="arxiv neuroscience brain neural 2025", limit=5)
web_search(query="arxiv quantum computing mechanics 2025", limit=5)
```

Extract arxiv IDs from the returned URLs (`arxiv.org/abs/XXXX.XXXXX`).

## web_extract Blocked on arxiv.org

The `web_extract` tool blocks arxiv.org URLs with error "Blocked: URL targets a private or internal network address". This is an agent-side security filter, not an arxiv issue.

**Workaround**: Use `web_search` for abstract snippets, or `kg_tool import-paper` with metadata obtained from search results.

## kg_tool Import Command

The Rust `kg_tool` binary uses this import format:
```bash
kg_tool import-paper --title "Paper Title" --url "https://arxiv.org/abs/XXXX.XXXXX" --abstract "Abstract text" --authors "Author names"
```

Note: The `--abstract` and `--authors` flags accept any string. Short abstracts work fine — the tool truncates internally.

## DB Path Discrepancy

The `kg_tool` binary at `scripts/kg_tool/target/release/kg_tool` has its DB path hardcoded to `/Users/hiyenwong/wiki/kg.db` (NOT the workspace kg.db). Always use the wiki path for kg_tool operations.

## Available kg_tool Commands

```
kg_tool import-paper  --title <t> --url <u> [--abstract <a>] [--authors <a>]
kg_tool generate-embeddings    # Generate embeddings for entities without them
kg_tool search        --query <q> [--limit <n>]
kg_tool pagerank      [--limit <n>]
kg_tool communities   [--limit <n>]
kg_tool stats                  # Show database statistics
```

Note: `generate-embeddings` only generates for entities MISSING embeddings. It does not regenerate existing ones.

## Vector Size Inconsistency in kg_vectors

**2026-05-21**: `kg_vectors.vector_data` BLOBs range from 64 to 6144 bytes across 20+ distinct sizes. Cannot assume uniform dimension for cosine similarity.

- Most common: 1024 bytes (1198 vectors), 512 bytes (79), 1536 bytes (51)
- Safe pattern: filter by `length(vector_data)` before comparing vectors
- Full analysis and safe cosine similarity code: [references/vector-embedding-pitfalls.md](references/vector-embedding-pitfalls.md)

## Arxiv ID Format in DB

The `arxiv_papers` table stores arxiv_id in full URL format: `http://arxiv.org/abs/2605.00038v1`. When checking for duplicates, query with the full URL format, not just the short ID.
