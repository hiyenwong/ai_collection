# kg_relations Schema Correction — SUPERSEDED 2026-06-09

**This document is superseded by `references/dual-kgdb-reality-2026-06-09.md`.**

## What Was Wrong

This doc stated that `~/.hermes/kg.db` `relationships` table has columns `(source_id, target_id, relation_type)`. This was **incorrect**. The actual columns in `~/.hermes/kg.db` are `(from_entity, to_entity, relationship_type, description, source, created_at)`.

## Root Cause

The confusion arose from mixing up two different databases:
- `~/.hermes/kg.db` (Hermes internal): uses `from_entity`/`to_entity`/`relationship_type`
- `kg.db` in other locations (e.g., wiki): may use `source_id`/`target_id`/`relation_type`

## Correct Reference

See `references/dual-kgdb-reality-2026-06-09.md` for the verified schema of both databases.
