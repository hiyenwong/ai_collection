# Saturday Economics/Investment + Quantum - Batch 2 (2026-06-06)

## RSS Feed Configuration
- **Feeds**: quant-ph + q-fin.PM + q-fin.TR + q-fin.MF + q-fin.ST
- **Total items**: 116 scored
- **Weekend note**: RSS has `<skipDays>Saturday, Sunday</skipDays>` — Saturday runs receive Friday's data

## RSS Parsing Fix
- First attempt with `curl ... | head -c 50000 > file` caused XML parse error (truncated mid-tag)
- Fix: `curl -s "https://rss.arxiv.org/rss/..." > /tmp/rss_full.xml` without size limit
- RSS uses `<item>` tags (RSS 2.0), NOT `<entry>` (Atom)

## Dual-Keyword Scoring Results
| arXiv | Econ | Quant | Total | Title |
|---|---|---|---|---|
| 2606.05900 | 22 | 3 | 25 | Derivative-Informed Operator Learning |
| 2606.05882 | 14 | 0 | 14 | Market Informedness on Market Makers |
| 2606.05387 | 3 | 8 | 11 | QML Feature Encoding Survey |
| 2606.05992 | 2 | 9 | 11 | GKP Boson Sampling ML Surrogate |
| 2606.05311 | 3 | 5 | 8 | QAOA Utility-Scale Angles |
| 2606.06413 | 8 | 0 | 8 | Dealer Market Competition |
| 2509.19663 | 8 | 0 | 8 | Long-Range Dependence Financial |
| 2606.05631 | 6 | 1 | 7 | ESG Joint Fragility |
| 2606.06062 | 0 | 7 | 7 | Barbell Codes qLDPC |

## Skills Created (5)
1. derivative-informed-operator-learning-finance
2. market-informedness-rl-market-making
3. dealer-market-competition-nash-equilibrium
4. esg-joint-fragility-equity-markets
5. long-range-dependence-financial-markets

## ai_collection Sync
- Branch: neuroscience-cron-2026-06-06
- Commit: fa73df14
- Skills placed under: collection/skills/finance/{skill-name}/

## Key Insights
- Econ score inflation from keyword-dense titles (up to 22 from title alone)
- All top papers already existed in kg.db from earlier sessions — no new imports needed
- Vector embeddings already existed for all papers
