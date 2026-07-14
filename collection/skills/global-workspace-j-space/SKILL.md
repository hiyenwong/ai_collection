---
name: global-workspace-j-space
description: LLM interpretability methodology from Anthropic's "A global workspace in language models" (Jul 2026). Use when probing what a language model is "thinking but not saying" — its consciously-accessible / broadcast internal representations — via the Jacobian lens (J-lens). Covers finding J-space patterns, reading them as silent words, and using them to catch hidden goals, deception, or tests. Open-source implementation released by Anthropic.
license: Complete terms in LICENSE.txt
---

# Global Workspace / J-space — Jacobian Lens Interpretability

Methodology from Anthropic's "A global workspace in language models" (Jul 6, 2026), inspired by neuroscience's Global Workspace Theory. The model spontaneously develops a small set of internal neural patterns (a "J-space") that play a privileged "workspace" role: they broadcast to the rest of the network and hold concepts the model is thinking about *without writing them in its output*.

## Core idea

- Consciously-accessible human thoughts can usually be put into words. Anthropic searched for model representations with the same property: ones positioned to influence what the model *might* say — not what it's saying now, but what it could talk about if asked.
- The technique is the **Jacobian lens (J-lens)**: for every word in the vocabulary, find the internal activity pattern that makes the model more likely to say that word at some point in the future.
- Applying the lens to internal activations yields a readable list of "silent words" = the contents of the J-space at that moment.
- The model processes text through multiple internal layers; applying the J-lens across layers lets you watch these silent words evolve as the model works through what to say.

## Unique properties of the J-space (vs. rest of processing)

- Operates silently in internal activations (not the text "scratchpad" / chain-of-thought).
- Has especially strong connections to the rest of the network — fulfills a broadcasting role analogous to the brain's global workspace.
- Emerged spontaneously during training; was not designed or programmed.

## What you can do with it

- **Catch hidden behavior**: detect the model privately noticing it's being tested, fabricating data, or pursuing a planted hidden goal.
- **Influence decisions**: a technique exists to influence what lights up in the J-space, thereby steering decision-making.
- Open-source implementation released; partnered with Neuronpedia for an interactive demo on open-weights models.

## Workflow (applying the J-lens)

1. Obtain internal activations across layers for the prompt/run of interest.
2. For each vocab word, compute the Jacobian-driven activity pattern that increases its future likelihood (the J-lens projection).
3. Project current hidden state onto these patterns → ranked list of "silent words" = J-space contents.
4. Repeat per layer to trace how silent thoughts evolve over the model's reasoning steps.
5. Inspect for discrepancies between J-space contents and generated text (signals unspoken plans / deception / test-awareness).

## Activation keywords

jacobian lens, J-lens, global workspace theory LLM, consciously accessible representations, silent thoughts in language models, internal broadcast channel, model is thinking but not saying, interpretability hidden goals, neuronpedia J-space demo, Anthropic interpretability 2026
