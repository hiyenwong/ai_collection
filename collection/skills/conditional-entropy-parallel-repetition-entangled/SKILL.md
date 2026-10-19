---
name: conditional-entropy-parallel-repetition-entangled
description: Entangled-game parallel repetition via conditional entropy.
category: ai_collection
---

# Conditional-Entropy Parallel Repetition for Entangled Games

**Source**: "Parallel Repetition for Entangled Games via Conditional Relative Entropy" (Rahul Jain, arXiv:2610.21410, quant-ph/cs.CC/cs.IT, Oct 2026). An alternative proof of the cubic parallel-repetition bound for finite two-player entangled games, using quantum conditional relative entropy.

## Activation

Use when: analyzing multi-round/multi-coordinate verifier games with shared entanglement; hardness-amplification arguments for multiprover interactive proofs (MIP*); information-theoretic proof design with chain rules and postselection; threshold/chernoff-style concentration for repeated games; quantum game theory in economics contexts (collusion-proofness, mechanism design with quantum agents). Trigger words: parallel repetition, entangled game, MIP*, free game, threshold repetition, correlated sampling, conditional relative entropy, information charge, Raz-Holenstein, JPY charge.

## The Result

For a finite two-player game G with question law µ, answer alphabets A, B, entangled value ω*(G) = 1 − ε < 1, and L := max{1, log(|A||B|)}:

**All-win repetition (Theorem 1.1)**: ω*(G^⊗n) ≤ exp[−Ω(ε³n/L)] for every n ≥ 1. Recovers Song's cubic rate for ARBITRARY question distributions (Raz/Holenstein cubic for classical; JPY for product questions; Chailloux-Scarpa for full-support correlated; OpenAI gap power 13 → Song power 3 → this paper).

**Threshold repetition (Corollary 5.2)**: for N = number of coordinates won and 0 < δ ≤ ε:
Pr[N ≥ ⌈(1−ε+δ)n⌉] ≤ exp[−Ω(δ⁵n/(ε²L))]. δ=ε gives the all-win event; δ=ε/2 tolerates an ε/2 failure fraction while keeping cubic ε-dependence. Improves OpenAI's universal threshold rate's gap dependence by a factor 1/ε².

Economics reading: an entangled collusion strategy cannot win even a small slack fraction of n independently-drawn auditing instances — decay is exponential in n with explicit gap powers. Cost of the proof: log-alphabet dependence L, so exponential decay survives only while ε³n/L is large.

## Proof Architecture (the reusable pattern)

### 1. Extraction objective
Turn high average success on UNCHECKED coordinates, conditioned on checked wins, into high single-game success. The extracted strategy receives fresh questions from µ and approximately prepares the conditional workspace of a uniformly chosen unchecked coordinate. Every legal single-game strategy rejects with probability ≥ ε, so sufficiently small preparation + question-law errors force mean unchecked rejection probability Ω(ε). Errors are controlled by the cost of conditioning on the checked wins and retaining the checked answers.

### 2. Preselection/postselection states
Fix a finite-dimensional repeated strategy; represent coherently with a purified shared resource, question amplitudes µ^⊗n(x,y), and local measurement isometries, retaining coherent basis copies of questions and checked answers → preselection state |ψ⟩. Project onto the event W_C that all checked coordinates are won: postselection state |ϕ⟩ = Π_C|ψ⟩/√p_C. Measured question-and-answer laws: P (of ψ) and Q = P(·|W_C) (of ϕ).

### 3. The conditional comparison states (the key novelty, Definition 2.6)
An Alice µ-conditional comparison has the form ν_A = C^µ_A(τ_A) := Σ_y |y⟩⟨y|_Y ⊗ K^µ_y τ_A K^µ_y† where K^µ_y := Σ_x √(µ(y|x)) |x⟩⟨x| (identity elsewhere). This attaches the prescribed conditional question law µ(y|x) coherently to Alice's question copy while keeping the coherent x,x′ blocks of τ_A. NOT a player operation on the protected reference — a proof device. **Crucial property**: the comparison preserves the ORIGINAL conditional question law, unlike prior charges that demanded independence from the remote question (which charges the prior correlation itself and blows up for correlated µ).

### 4. The information charge
Charge := decrease in relative entropy when a question reference is discarded (conditional relative entropy of the comparison states). A chain rule expresses each coordinate's charge as a difference of two successive relative entropies — summing cancels intermediate terms, leaving a single parent bound (Lemma 2.24): budget B_C := log(1/p_C) + |C|·L (conditioning cost + entropy of checked answers), allocated over unchecked coordinates.

### 5. Why the earlier charges fail (counterexamples worth remembering)
- **Classical Raz–Holenstein charge I(X:B|Y) misses phase dependence**: for the phase-CHSH family |ϕ_xy⟩ = (|00⟩ + (−1)^{xy}|11⟩)/√2, both players' workspace marginals are I/2 always, so I(X:B|Y) = 0, yet preparing the family locally would win CHSH with certainty. The coherent (JPY) charge detects it (1/2 bit).
- **JPY charge I(Ỹ:X̂X̂A) charges the prior correlation**: with correlated questions µ(0,0)=µ(1,1)=1/2 and fixed workspace, JPY charge = 1 bit although preparation needs no input-dependent operation — linear overhead even for the untouched source. Hence: the comparison must RETAIN the prior correlation, not demand independence from the remote question.
- **Naive conditioning I(X̂:B′|Y)** fails by local-copy padding: adding local question copies Ac, Bc makes the conditioned charge 0 while JPY charge stays 1/2 bit and preparation still approaches CHSH certainty — the charge is not stable under local isometries.

### 6. Local preparation from pure descriptions (Lemma 4.1, the technical heart)
For total charge s := b_A + b_B:
- (i) preparation error d_prep(q, ϕ) ≤ min{1, C_prep√s}, C_prep = 100·C_sm (Song's sampler constant).
- (ii) After finite pure padding there exist bipartite unit vectors |u_x⟩, |v_y⟩, Alice isometries J_x, Bob unitaries W_y (Alice's chosen from x only, Bob's from y only, ALL fixed before questions arrive) with E_q‖|u_x⟩−|v_y⟩‖² ≤ 4(ln2)(b_A+b_B) and E_q P²((J_x⊗W_y†)u_x(...), ψ_xy) ≤ (ln2)b_A.

Construction: Alice's alignment error e_A ≤ (ln2)b_A via constructive marginal replacement (Lemma 4.2(ii)) matching Alice's retained marginal in comparison form; Uhlmann's theorem applied to the WHOLE coherent x-ensemble at fixed y picks ONE Bob correction W_y for all components; Cauchy–Schwarz turns the coherent overlap into conditional-infidelity under q. Bob's variation error e_B := E_q P²(ψ_xy^B, ψ_y^B) ≤ (ln2)·I(X:B|Y) ≤ (ln2)b_B (Pinsker + chain rule).

### 7. Assembly: square-root rejection + budget balance
√ε ≤ √(A_C + √ē + t√(ln2 Σ D(q_i‖µ))): unchecked rejection A_C must be Ω(ε) once the checked set size t is ≤ a small universal multiple of ε². Greedy checking: each check reduces p_C by factor (1−Ω(ε)); balancing against B_C's growth gives exp[−Ω(ε³n/L)]. The three powers of ε: quadratic information threshold (ε²) × linear rejection threshold (ε) = ε³. Threshold version: A_C ≥ ε − δ/4 with t ≤ const·δ⁴/ε², then Rao's concentration gives the δ⁵/ε² rate.

## Reusable Lessons

1. **Charge design under postselection**: when proving decay-by-conditioning, choose a divergence-based charge measured against COMPARISON STATES that preserve the ambient prior law — never charges that implicitly demand independence from the prior (they tax the untouched source and destroy the budget).
2. **Chain rules telescope**: define per-coordinate charges as differences of successive relative entropies so summation cancels intermediates and the parent bound log(1/p_C) + |C|L falls out for free.
3. **Phase information requires coherent registers**: classical conditional mutual information on measured marginals can be exactly zero for states whose preparation is the whole difficulty (phase-CHSH). Keep question copies coherent in the analysis register.
4. **Charges must be stable under local isometry**: test any candidate charge against the padding trick (adjoin local question copies) — if the charge can be zeroed by local padding while the operational task remains hard, the charge is unusable.
5. **One correction per coherent slice**: Uhlmann applied to the whole x-ensemble at fixed y yields a single W_y per y, not per-(x,y) — this is what keeps Alice's and Bob's local corrections compatible with locality of the players.
6. **Exponent bookkeeping**: gap-power comes from multiplying the information threshold by the rejection threshold; a threshold result tolerating δ failures trades a δ⁴ checking budget for ε−δ/4 rejection, and Rao concentration converts conditional success to large-deviation decay.

## Context in the Literature

Raz '94 (classical), Holenstein '07 (information-theoretic, cubic), Rao '08 (concentration), CSUU '08 (XOR perfect), KRT '08 (unique), DSV '09 (projection), JPY '10 (product questions), Chailloux–Scarpa (quadratic free; full-support correlated exponential), Chung–Wu–Yuen (3/2 power, multi-player), Yuen (polynomial general), OpenAI (power 13 arbitrary; universal threshold), Song (power 3 arbitrary — this paper recovers it with a different proof). This proof's distinctive assets: µ-conditional comparisons (Def 2.6) + pure-description conversion (Lemma 4.1) + Song's smooth sampler (Fact 2.22).
