---
name: lvr-transaction-cost-amm
description: Use when pricing AMM liquidity under transaction costs.
category: ai_collection
---

# LVR with External Proportional Transaction Costs (Zero-LVR Band Theory)

**Source**: Masaaki Fukasawa, "Loss-versus-rebalancing with external proportional transaction costs", arXiv:2610.21057 (q-fin.MF/q-fin.PM, 15 Oct 2026). Extends Fukasawa–Maire–Wunsch (Digital Finance 2025) to external markets with proportional transaction costs.

## Core Framework

External market: bid/ask `Sb = (1−λ)S*`, `Sa = S*/(1−λ)` with cost parameter λ ∈ [0,1). Pool: CFMM with fee τ, two fee mechanisms:

- **Separate fees (Uniswap v3 type)**: active reserves stay on fixed curve `Y = f(X)`, `S = −f′(X)`, fee account outside. Pool ask/bid: `A = S/(1−τ)`, `B = (1−τ)S`.
- **Retained fees (Uniswap v2 type)**: full incoming payment stays in reserves, priced on utility level `u(X+(1−τ1{ΔX>0})ΔX, Y+(1−τ1{ΔY>0})ΔY) = u(X,Y)`; level ratchets up as fees accrue (`dH = τux dX↑ + τ/(1−τ) ux dX↓ ≥ 0`).

**No-arbitrage band** (both mechanisms): with `γ := (1−τ)(1−λ)`, arbitrage confines the internal price to `γS* ≤ S ≤ S*/γ`. Same band as frictionless market with effective fee `τ_eff = τ+λ−τλ` (band only — fee income still set by τ).

## Main Theorem (Thm 3.2): Zero Transaction-Cost LVR

Under continuous external prices, continuous finite-variation total holdings Q satisfying the cash identity `dC^LP = A dQ↓ − B dQ↑` and pure arbitrage (trades only at band boundaries: `(A−Sb)dQ↓ = 0`, `(Sa−B)dQ↑ = 0`):

**LVR_tc = V^R − V^LP = 0 whenever τ+λ > 0** — pool and the external self-financing strategy holding the same total inventory Q, trading at the external bid/ask, have identical liquidation wealth. Zero LVR even with zero pool fee, as long as the external spread is positive.

Proof is one line: `dLVR = (Sb−A)dQ↓ + (B−Sa)dQ↑ = 0` by boundary support. The mechanism: with any friction positive, reflected inventory is continuous **finite variation** (zero quadratic variation), so the Itô correction that generates the frictionless LVR `V^R−V^LP = ∫½f″(X)d⟨X⟩ ≥ 0` disappears. The point (τ,λ)=(0,0) is singular — the quadratic-variation loss is a discontinuous limit, not a small-friction approximation.

**Interpretation**: LP wealth = the external strategy's wealth. Liquidity provision is an investment strategy implemented via pricing rule — arbitrageurs execute its rebalancing at no cost relative to doing it yourself.

## Hedge Cost Identity (Prop 4.1)

Zero LVR ≠ costless hedging. External hedge holding −Q units bleeds: `dW = −(Sa−Sb) dTV(Q)` — the spread integrated against inventory turnover, nonincreasing. The frictionless super-hedge of impermanent loss fails under positive λ; the cost is shared by pool and benchmark and cancels in their comparison.

## Constructive Pool Design (Investment Implementation)

### 1. Prescribed inventory schedule (Props 5.1–5.2)
Any C¹ decreasing schedule `q: (0,∞)→(0,∞)` with `∫₀^{p₀} q < ∞` defines a reserve curve:

```
f(q(p)) = η + ∫₀^p q(r)dr − p·q(p),   f′(q(p)) = −p,  f″(q(p)) = −1/q′(p) > 0
```

Utility `u(x,y) = −exp{f(x)−y}` on D = I×(0,∞) gives a retained-fee pool where marginal price `S = u_x/u_y = −f′(X)` is **independent of numeraire level**, so fee accumulation preserves `X = q(S)` exactly. Excess numeraire `K = Y − f(X)` obeys `dK = τS dX↑ + τ/(1−τ) S dX↓ ≥ 0` (vertical translates of the curve). Power law `q(p) = c p^{−β}` (0<β<1) reproduces the geometric-mean curve with `k = (1−β)/β`. Global existence: reflect `log(S₀/S*)` on `[−h,h]` (Skorokhod, h = −log γ), then `Xₜ = q(Sₜ)`, `dX↑ = −q′(S)S dU`.

### 2. Constant no-trade weight boundaries (Sec 5.3)
For investment problems with optimal no-trade boundaries `0 < π− < π+ < 1` (Davis–Norman / Shreve–Soner type): use a retained-fee geometric-mean pool with weight

```
k = ab,  a = √(π−/(1−π−)),  b = √(π+/(1−π+)),  γ = a/b
```

Weight at band boundaries: `kγ/(1+kγ) = π−` (buy) and `k/(k+γ) = π+` (sell). Choose pool fee `τ = 1 − γ/(1−λ)`, feasible iff γ ≤ 1−λ — the external spread imposes a minimum band; narrower targets need rebates. Uniswap v2 constant-product (k=1) only implements symmetric boundaries; general targets need the tuned weight. (Verified numerically to 1e-12 across 5 boundary sets, incl. asymmetric π−=0.2/π+=0.6 → k=0.612.)

## Boundary Cases & Failure Modes

- **Interior (non-boundary) flow**: `dLVR ≤ 0` — uninformed/taker flow inside the band makes LP strictly outperform the benchmark; equality holds only for the arbitrage component.
- **Price jumps**: zero-LVR breaks — stale-quote exploitation loss funds arbitrage profit + external execution costs; boundary identities fail through a nonzero price range.
- **Separate fees**: total weight `(X+Xf)p / (Y+Yf+(X+Xf)p)` drifts from active-reserve fraction — exact implementation needs continuous management; retained fees make actual reserves the whole strategy portfolio (no fee-reinvestment rule needed).
- Excludes gas, contract risk, LP deposits/withdrawals, protocol fee cuts. Stateful strategies (time/path-dependent) need Uniswap v4-style hooks with separate analysis.

## Verification Anchors (all re-checked numerically 2026-10-17)

1. Band boundary identities: pool sells only when A=Sb → S = Sb(1−τ); buys only when B=Sa → S = Sa/(1−τ); both inside [γS*, S*/γ]. ✓ (λ=0.005, τ=0.02 → band [97.51, 102.55])
2. Schedule construction: f′(q(p)) = −p and closed form matches integral definition to 1e-6 for q(p)=2p^{−1/2}. ✓
3. Singular limit: frictionless LVR = ½∫f″(X)d⟨X⟩ > 0 collapses to 0 as soon as τ+λ>0 — never interpolate between regimes.

## Reusable Patterns

- **Friction-as-reflection**: any positive friction (pool fee OR external spread) converts reserve dynamics from semimartingale to reflected finite-variation — the general mechanism killing LVR-type drift.
- **Design-from-strategy inversion**: start from desired holdings q(S) or weight band (π−,π+), solve for curve/fee (η, f, k, τ) — pool design = strategy specification.
- **γ-composition rule**: frictions multiply through γ=(1−τ)(1−λ); target band γ sets feasible fee τ given λ.
- **Benchmark-alignment proof pattern**: to compare a pool against any benchmark, write both cash identities, subtract, and read off the sign of dLVR term by term (boundary support → zero; interior flow → negative).

## Related

- Milionis–Moallemi–Roughgarden–Zhang (arXiv:2208.06046) — original LVR definition, frictionless.
- Fukasawa–Maire–Wunsch (2024/2025) — fee-eliminated LVR (frictionless external), geometric-mean super-hedge.
- maker-spread-screening-vs-cadence-threshold (this collection) — maker break-even spread, complementary microstructure view.

**Activation**: LVR, loss-versus-rebalancing, AMM, automated market maker, CFMM, transaction costs, bid-ask spread, no-arbitrage band, Uniswap, liquidity provision, impermanent loss hedge, inventory schedule, no-trade boundary, Skorokhod reflection, DeFi pool design, portfolio weight band, rebalancing benchmark