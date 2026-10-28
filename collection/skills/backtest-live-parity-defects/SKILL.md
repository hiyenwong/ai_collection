---
name: backtest-live-parity-defects
description: Backtest-live parity QA for trading systems and simulators.
category: ai_collection
---

# Backtest–Live Parity Defects

**Source**: "Where Backtests and Live Trading Part Ways: Six Defects from One Intraday System" (Vidovich & Zerjal, arXiv:2610.21846, q-fin.TR/q-fin.ST, Oct 2026). A post-mortem of six implementation defects found by replaying live trading days through the backtest harness ("parity harness") of one intraday US-equity system (97–98 stocks, 1-minute bars, decisions shortly after the open).

**Core claim**: Backtest failure literature targets statistics (overfitting, multiple testing). These six defects are *implementation* defects — they bias a backtest **before any statistics run**, and the safeguards of the statistics literature (which assume correct inputs) cannot catch them. None was visible in summary statistics; every one was found by a narrow, concrete comparison of two paths that should agree.

## Activation

Use when: building or auditing a backtest harness for live trading; diagnosing divergence between simulated and real execution; designing regression tests for trading infrastructure; setting up paper-trading → real-money validation. Trigger words: backtest parity, slippage test, paper account, execution simulation, market data feed, dividend adjustment, timestamp timezone, config wiring.

## The Six Defects (each: symptom → magnitude → root cause → detection test)

### Defect 1 — Default data feed ≠ consolidated tape
- Historical bar requests without a pinned `feed` parameter returned single-exchange (IEX) data instead of the consolidated tape (SIP): opening-minute volume 0.1–2% of true. Full-day totals were *correct* — only the per-minute split at the open was thin. Live was unaffected (same-day fetches hit the right feed).
- Every feature built from opening-minute data was wrong; one month understated, one overstated, one losing trade flipped to winning — with nothing in summaries to say so.
- **Tests**: (a) request-recording test — fake session records every outgoing request, asserts every request pins `feed=sip` and `adjustment=raw`; (b) runtime check — at decision time, alarm if opening volume collapses across nearly the whole universe at once (never blocks trades).
- **Lesson**: pin every vendor parameter that changes what the data means, even when today's default looks right; then check, at the point of use, a property the bug would break.

### Defect 2 — Dividend-adjusted history vs unadjusted live fills
- A commit switched fetch adjustment from split-only to "all" (includes dividends). A bar from date D, fetched later, has all dividends after D subtracted. Harmless in live (same-day bars, fills at unadjusted prices), wrong in every backtest: one bar sat −0.68% off the live price basis; 37/98 symbols shifted, all dividend payers (range −0.68% to −1.65%). Entry unadjusted + exit adjusted made replay results far from live on the same trade.
- **Test**: same request-recording pattern asserts `adjustment=raw` everywhere. What actually caught it: the parity step — replay one live trade and match entry/exit to the real fill, to the cent.
- **Lesson**: adjusted prices answer "what was this worth in today's terms"; a backtest must answer "what price would my order have filled at that day". Use unadjusted prices for execution simulation.

### Defect 3 — Sizing step scaled past the binding limit
- Strategy code applied the buying-power limit correctly; a *later* step that can increase size multiplied the already-limited notional with no re-limit. Result: 20/61 simulated fills at notionals the live account can never take; ~18% too large; every dollar figure discarded. Live never exposed (it re-checks real buying power at order time; the late step's input field exists only in the backtest).
- **Test**: unit test builds a setup already at its limit, applies the size-increasing step, asserts ceiling/notional/share-count unchanged. Structural fix: each setup *carries its limit* so any later step re-applies it.
- **Lesson**: in a chain of sizing steps, apply the binding limit LAST, or re-apply after every step that can increase size. Test with a position already at the limit — that's the case that breaks.

### Defect 4 — UTC timestamps read as New York time
- Cache stores bar timestamps in UTC; a scan picked the opening bar with fixed key "13:30". 13:30 UTC = 9:30 ET only in daylight saving; in winter it's 8:30 ET, an hour before the open. 129 winter days (30% of sample): 16% of stock-mornings scored on a pre-market bar, 84% silently dropped by a completeness check. Second form: hour built as `13 + minutes//60` hard-codes the summer offset. A run fixing only the first form briefly printed a positive result that vanished with the second fix.
- **Control**: one shared helper converting cache timestamps to exchange time; rule: bare string slicing of a cache timestamp is a bug on sight. Missing test: one winter date + one summer date, both resolving 9:30 ET to the right bar. No verdict flipped, but almost every number moved — a reviewer checking only verdicts sees nothing.
- **Lesson**: never compare clock times as strings. Convert to the exchange's time zone once, in one function. Put a winter day AND a summer day in every time-dependent test.

### Defect 5 — Data the live path downloads and the replay did not
- Live fetches data from its own list of required inputs; the replay built its request from the *traded stocks* list. The lists drifted apart when the traded list changed. Missing input did not raise — it fell back silently to zero, for ~4 months, feeding several decision rules a wrong value. Restoring it changed 1-in-20 real-money decisions. An earlier unexplained live-vs-replay difference was re-attributed to this defect ("likely, not proven").
- **Tests** (written first, failed for the right reasons): harness warns and records the gap whenever a required input is missing; replay requests the live path's own list; a test asserts the extra data is in the request.
- **Lesson**: build the replay's data request from the live system's list of required inputs, never from the list of things it trades. Never let a missing input fall back silently to a neutral value — make it loud. Chase every unexplained parity divergence.

### Defect 6 — "Enabled in config" is not "connected in the execution path"
- Family of three: (1) an exit rule ON but ignored — live monitor honors only reasons in a fixed set; the new rule's reason wasn't there, AND the simulator ended at the ignored exit, hiding every later honored exit; (2) a sizing rule wired only into a backtest-only branch — live never used it; its "end-to-end confirmation" checked the flag loaded into config, not that orders changed; (3) invisible settings — 53 keys read by production code but undeclared; the execution ON/OFF switch existed only in the startup file, so shipping generated defaults would have silently dry-run the live system. One regression map was itself false assurance: it listed four keys the runtime never reads, so its test passed while guarding nothing.
- **Tests**: mapping test (every exit flag ON maps to a reason in the honored set) + key-really-read test + presence test (every key the code reads is declared) + neutrality test (loading declared values reproduces code defaults) + a preflight script run twice daily that checks *behavior in logs and output files, not settings*.
- **Lesson**: for every setting, test that it changes something observable in the path that places orders. Declare every key the code reads. Config file may not be the only place settings live.

## The Ten-Point Checklist (Table 4, each traced to a defect)

1. Pin the data feed in every request; test the parameter. (D1)
2. At decision time, alarm if opening volume collapses across the whole universe at once. (D1)
3. Use unadjusted prices for execution simulation; test the parameter. (D2)
4. Replay live trades regularly and match decisions, prices, sizes; after any data change, match one fill to the cent. (D2)
5. Re-apply the binding size limit after every step that can increase size; test at the limit. (D3)
6. Convert timestamps in one shared exchange-time helper, tested on a winter and a summer day. (D4)
7. Build the replay's data request from the live path's list of required inputs; make any missing input loud, never a silent default. (D5)
8. Chase every unexplained difference between replay and live to its root cause. (D5)
9. For every setting, test that it changes an observable action in the order path; declare every key the code reads. (D6)
10. Check live behavior in logs daily, not settings. (D6)

## Reusable Methodology Patterns

### 1. Parity-first testing
The first test a harness must pass: replay days the live system *actually traded* and compare decisions, prices, sizes. Distinctions that matter:
- Paper-account fills are simulated by the broker → a paper-fill match tests the harness against the *broker's simulator*, not the market. Real-money days count for more.
- Pre-register a slippage bar: same-trade replay vs live may differ by max(5% of replay result, small fixed floor).
- Matching decisions is necessary, not sufficient: the retired harness matched live on 7/8 real-money dates while misreading its inputs and dropping the trades that moved the total most.

### 2. Request-recording tests (record the request, not the response)
```
def test_every_bar_request_pins_feed_and_price_basis():
    recorded = []
    class RecordingSession:            # stands in for the HTTP client
        def get(self, url, params=None, timeout=None):
            recorded.append(dict(params or {}))
            return EmptyBarsResponse()  # no bars, no network needed
    fetch_bars(RecordingSession(), ["SYM1"], start, end)
    assert recorded, "no request was made"
    assert all(p.get("feed") == "sip" for p in recorded)
    assert all(p.get("adjustment") == "raw" for p in recorded)
```
Checks what the code *asks for*, not what the vendor sends back. Needs no network/credentials, fails the moment anyone drops a parameter, keeps working even if vendor defaults change. Same pattern covers D5: record requested symbols, assert they include every symbol on the live path's required-data list.

### 3. Narrow concrete looks beat summary-stat review
None of the six was found by reviewing summary results; all were found by: one live trade against the cache; one bar from four sources; one day's decision record re-read; one script's key checked before a new study; one unexplained real-money day chased to the end; the system's own logs on the first live session after a change. "A bug that makes results absurd gets caught. These made results look plausible." Once a defect class recurs, sweep for it systematically (the undeclared-keys audit found 53 after the third wiring instance).

### 4. Written lessons do not stop recurrence
The clock trap was logged months before it came back; the sizing-chain lesson recurred too. Lesson: convert lessons into automated tests at the moment they are learned; keep a research graveyard (one entry per rejected idea + the test that rejected it) — but remember a rejection is only as good as the harness that made it (every rejection recorded while a known defect was present is provisional until re-run).

### 5. Error-cancellation produces false passes
On one real-money day, Defect 5's fix exposed that live and replay applied a size cap at different points in the sizing chain; the two errors cancelled and produced a false parity pass. Fixing one defect can unmask another. Interactions of simultaneously-present defects were never measured.

## Magnitude Summary (Appendix A)

| Defect | Before fix | After fix | Lived |
|---|---|---|---|
| 1 Feed | open-minute volume 0.1–2% of consolidated | matches live to the share | ~11 weeks |
| 2 Adjustment | 37/98 symbols shifted; one bar −0.68% | entry/exit match to the cent | 3.5 weeks |
| 3 Size limit | 20/61 fills past live limit; ~18% too large | all fills within limit; same 61 fills | unknown start |
| 4 Clock | 129 winter days (30%) misread/dropped | NY keys; no verdict flipped | caught day-of in scans (trap logged months earlier) |
| 5 Missing data | one input read as zero; 1-in-20 decisions changed | replay requests live's list; gaps flagged | ~4 months |
| 6 Wiring | ignored exit; dead sizing rule; 53 undeclared keys | class-level tests; all keys declared; startup-file settings removed | exit 1 day; sizing rule 10 days live |

## Scope & Honest Limitations (per the authors)
One system, one vendor (Alpaca), one account; magnitudes do not transfer; classes are general. Every parity day fell in US summer time — no check has yet covered a winter day (D4's season). Defect 5's effect on all harness figures produced during those 4 months is unmeasured. Interactions unmeasured. Self-reported by the same team that made the errors. "We make no claim about whether the system is profitable."
