---
name: reward-shaped-nonlinguistic-rule-codes
description: Reward vs gradient channels shape emergent rule codes differently.
category: ai_collection
trigger_words: emergent communication, signalling game, rule transmission, compositionality, aphasia, invented symbols, reward vs gradient, degenerate pooling equilibrium, non-linguistic code
---

# Learning Non-Linguistic Codes for Inferred Rules From Reward

Methodology from "Learning a non-linguistic code for inferred rules from reward" (arXiv:2609.31192, q-bio.NC, Sep 2026, Cristiano Capone).

## When to Use
- Modeling how rules/inference (not references) transmit between agents without a pre-shared language — computational model of aphasia patients conveying inferred rules by gesture/sketch (Kean et al.)
- Emergent-communication research beyond referential games: rule-execution games where a message must let a blind receiver *execute* a transformation on new input
- Designing multi-agent systems where a teacher must communicate skills/rules to a student through a narrow discrete channel
- Analyzing degenerate solutions (message collapse) in reward-trained communication

## Game Setup (Speaker–Executor)
- **Speaker** network: sees a few worked examples of a transformation; emits 8 symbols from a 32-symbol alphabet (nothing assigned in advance — no grammar, no supervision of meanings)
- **Executor** network: sees ONLY the symbols + a fresh input grid; must produce the correct output
- Three channels compared:
  1. **Reward**: speaker learns only from executor's success/failure
  2. **Gradient**: executor's error backpropagates through the symbols
  3. **Continuous**: real-valued vector replaces symbols (upper bound reference)
- Experience curricula: Staged (singles→pairs→triples), Joint (all at once), Reversed

## Five Core Findings
1. **A code emerges and composes**: it carries rules to held-out 3-step transformations training never computes, and new learners can acquire it. Critical methodology — held-out split audit: training episodes are rotated/reflected/recoloured, so most held-out *pairs* are transformations training already presents in disguise; only held-out *triples* (100 of 300) genuinely test composition.
2. **Discreteness costs little** — provided perception is learned outside the channel (encoder pretrained, frozen during code learning).
3. **Reward and gradient build different codes**: reward sorts many rules under a few fixed labels (pooling); gradient gives each rule its own region of similar messages (graded map). Gradient separates rules far better.
4. **Degenerate solution is measurable**: under reward alone, the speaker drifts to ONE message whatever the rule (analogous to human languages losing words in plain transmission). Staged experience or an information pressure against uninformative messages prevents collapse. Competence tracks **how much the message says about the rule** (mutual information), NOT message variety.
5. **Reward-driven naming saturates** as rules are added; neither tested capacity increase lifted the ceiling.

## Implementation Pattern
```python
# 1. Speaker: encoder(examples) -> discrete bottleneck (8 symbols, alphabet 32, straight-through Gumbel)
# 2. Executor: decoder(symbols, new_input) -> output grid
# 3. Channels:
#    reward-only: REINFORCE/PPO on executor success (exact match)
#    gradient: straight-through estimator lets executor loss flow to speaker
# 4. Metrics:
#    - exact-match accuracy on held-out TRIPLES (composition test)
#    - P(rule | message) — how often a rule is decoded from the message
#    - degeneracy check: entropy of speaker outputs across rules
#    - information pressure: penalize low MI(message; rule) or uniform messages
# 5. Held-out audit: verify test transformations are NOT reachable by composing
#    training programs under rotation/reflection/recolor equivalences.
```

## Design Lessons for Multi-Agent Rule Teaching
- Reward-only channels → pooling equilibria. If you need rule-specific messages, add gradient flow (differentiable channel) or explicit information pressure.
- Curriculum matters: staged (simple→composite) prevents degenerate collapse better than joint training; reversed curriculum is worse.
- Measure the *information content* of messages (MI with the rule), not their diversity — variety without relevance is worthless.
- When auditing generalization in compositional tasks, enumerate algebraic symmetries (rotation/reflection/recolor) of training data; test only on transformations unreachable from the training orbit.
- Discrete bottleneck is fine — put representational capacity in pretrained perception outside the channel, not in the code itself.
