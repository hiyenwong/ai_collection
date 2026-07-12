# Medicine + Quantum Research Pipeline

This session produced a complete medicine+quantum discovery workflow. The key reusable patterns are:

## arXiv Search Pattern
- Use `all:quantum+AND+all:{medical_term}` syntax (NOT `+OR+`) with urllib + proxy
- 9 query variants cover medicine+quantum landscape
- Score papers using dual-keyword matching (26 medical + 20 quantum terms)

## Domain Saturation Pattern
- Medicine+quantum domain is HIGHLY saturated (>90% of top papers have skills)
- Check skill existence before creation: `grep -rl {keyword} ~/.hermes/skills/`
- When saturated, fall back to meta-analysis synthesis

## CovAngelo QM/QM/MM Pattern (arXiv: 2604.10487)
- Three-tier embedding: quantum hardware → classical QM → molecular mechanics
- Drug discovery use case: ligand-protein binding modeling
- Quantum-in-quantum-in-classical architecture

## kg.db Import Pattern (Verified 2026-06-10)
- arxiv_papers: `(id, title, authors, published, categories, summary, pdf_url, abs_url)`
- kg_entities: `(title, url, content, authors, published_date, category, source)` — NOT name/type/description
- kg_vectors: `(entity_id, vector_data BLOB)` — NOT embedding column
- Always PRAGMA verify before INSERT
