# Knowledge Graph Integration Issues

## Context
During the creation of this skill as part of automated neuroscience research (July 28, 2026), attempts to integrate the paper into the local knowledge graph (kg.db) failed due to schema incompatibilities.

## Error Details
- **Command attempted**: `./kg_tool add-paper --arxiv-id 2607.24519 [...]`
- **Error received**: `Unknown command: add-paper`
- **Available commands**: migrate, embed, search, stats, context, find-related, similar
- **Schema verification error**: `no such column: entity_type`

## Workaround Applied
- Paper metadata successfully captured in Obsidian note: `Neuroscience Research - July 28, 2026.md`
- Skill successfully created and synced to ai_collection repository
- Manual addition to knowledge graph required when schema issues are resolved

## Related Research Automation Notes
This issue affects the broader research automation pipeline. The paper should be manually added to kg.db once the schema/tool compatibility is resolved.

## Paper Metadata for Manual Addition
- **arXiv ID**: 2607.24519
- **Title**: Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls
- **Author**: Marzieh Zare
- **Category**: cs.LG (Machine Learning)
- **Date**: 2026-07-27
- **Key Topics**: EEG foundation models, stress testing, clinical decoding, dataset identity, negative controls, frozen linear probes