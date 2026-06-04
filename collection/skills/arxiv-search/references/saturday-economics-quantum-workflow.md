# Saturday Economics + Quantum Discovery Reference (2026-05-30)

## Weekend Discovery Reality
- arXiv RSS: Empty on Sat/Sun (`<skipDays>` confirms intentional skip)
- arXiv API: Consistently 429 rate-limited
- Browser: 60s timeout on arxiv.org
- **Working fallback**: Query `kg.db` directly for pre-indexed papers

## Papers Found via kg.db (2026-05-29/30)
Total: 347 papers (303 from arXiv)

### Quantum Finance Papers (no existing skills → new skills created)
1. **2605.28950** — "Exponentially Fast Solution State Preparation for the Heat Equation and its use for Option Pricing" (quant-ph, q-fin.MF)
2. **2605.28327** — "Insurance Pricing Optimization via Off-Policy Evaluation" (stat.ML, cs.LG, q-fin.RM)

### Papers Already with Skills (duplicates avoided)
- 2605.28853 → deep-portfolio-optimization-framework
- 2605.29413 → bayesian-portfolio-integration  
- 2605.26610 → quantum-finance-economics, quantum-pde-option-pricing

## Weekend Cron Job Strategy
1. Check `weekly_topics.py` for today's topic
2. Try arXiv RSS first (will be empty on Sat/Sun)
3. **Immediately pivot to kg.db** if RSS empty or API 429
4. Query kg.db: `SELECT name, description FROM entities WHERE type='paper' AND (category LIKE '%quant%' OR name LIKE '%quantum%') ORDER BY created_date DESC`
5. Cross-reference against existing skills via `grep -rl "<arxiv_id>" ~/.hermes/skills/*/SKILL.md`
6. Create skills for uncovered papers
7. Sync to ai_collection

## kg_tool Reliability (2026-05-30 Confirmed)
- `kg_tool search --query` → returns empty even with relevant data
- `kg_tool generate-embeddings` → returns empty
- `kg_tool pagerank --limit 20` → **works reliably**
- `kg_tool communities --limit 20` → **works reliably**
- Use sqlite3 direct queries instead of kg_tool search for paper retrieval
