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

---

## 2026-06-06 Update: Economics/Finance + Quantum Cross-Domain RSS Discovery

### RSS Feeds (Working on Saturday — returns Friday data)
- `https://rss.arxiv.org/rss/quant-ph+q-fin.PM+q-fin.TR+q-fin.MF+q-fin.ST`
- Yields ~30 items (Friday's data, as expected due to `<skipDays>Saturday, Sunday</skipDays>`)

### Verified Keyword Sets for Economics/Finance + Quantum Scoring

**Economics/Finance Keywords (54 terms)**:
economics, finance, financial, investment, market, portfolio, trading, pricing, option, risk, hedging, asset, return, derivative, volatility, arbitrage, hedge, insurance, actuary, revenue, profit, cost, utility, game theory, auction, economic, monetary, fiscal, wealth, capital, equity, bond, loan, credit, bank, fund, budget, forecasting, prediction, time series, stochastic, optimization, decision, reinforcement learning, multi-agent, hawkes, order flow, maker, informedness, profitability, greek, vega, delta, calibration, stress test, control, surrogate, operator learning

**Quantum Keywords (35 terms)**:
quantum, qubit, entanglement, superposition, hamiltonian, gate, fidelity, decoherence, quantum computing, quantum algorithm, qaoa, vqe, quantum machine, quantum neural, quantum state, quantum error, qec, quantum simulation, density matrix, wavefunction, measurement, quantum thermodynamics, quantum sensor, quantum metrology, quantum advantage, NISQ, quantum chemistry, quantum finance, quantum portfolio, quantum optimization, boson, fermion, photon, spin, operator

### Top Cross-Domain Papers (2026-06-06)
- **2606.05311** (E=4, Q=6): QAOA utility-scale angle setting — MPS/Pauli propagation, small→large transfer
- **2606.05387** (E=2, Q=6): QML feature encoding survey — 66 works, 5-regime decision framework
- **2606.05882** (E=6, Q=1): RL market making — MAPPO/CTDE, Hawkes process stability guarantees
- **2606.05900** (E=6, Q=0): Derivative-informed operator learning — 40% vega error reduction
- **2606.06062** (E=1, Q=6): Barbell qLDPC codes — superconducting hardware, trillion-cycle QEC

### Skills Created from This Session
1. `qaoa-utility-scale-angle-setting` — angle finding + transfer strategies
2. `derivative-informed-operator-learning-finance` — dual objective (value + derivatives)
3. `market-informedness-rl-market-making` — multi-agent RL market making

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
