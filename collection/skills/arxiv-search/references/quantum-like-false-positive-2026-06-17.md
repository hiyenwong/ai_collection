# "Quantum-like" False Positive Pattern (2026-06-17 verified)

## Problem

When running keyword-based searches for quantum + medicine/healthcare/neuroscience papers, papers containing the term "quantum-like" are frequently matched by the keyword filter but do NOT involve actual quantum computing or quantum physics. Instead, they use "quantum-like" as a mathematical formalism (complex-valued state representations with phase) in classical computational models.

## Verified Example (2026-06-17)

**Paper**: arXiv:2606.12449 — "A quantum-like benchmark for context-sensitive associative memory with adaptive plasticity"
- **Category**: q-bio.NC (Neurons and Cognition) — NOT quant-ph
- **"Quantum-like" refers to**: Complex-valued states with phase dynamics, NOT quantum computation
- **Paper explicitly states**: "Here, 'quantum-like' refers to the modeling formalism, not to a biological claim about quantum computation."

## Detection Pattern

**Signals that "quantum-like" does NOT mean quantum computing:**
- Paper is NOT in quant-ph, cs.QC, or related quantum categories
- Paper uses "quantum-like" (with hyphen) or "quantum-like" in title but not "quantum computing", "qubit", "quantum circuit", etc.
- Paper is in biology/psychology/cognitive science categories (q-bio.NC, cs.CC, etc.)
- Paper mentions "complex-valued states", "phase", "interference" in a mathematical context
- Paper includes explicit disclaimer: "not a biological claim about quantum computation"

**Signals that DO indicate real quantum computing:**
- quant-ph, cs.QC, physics.quant-ph categories
- Mentions of qubits, quantum circuits, quantum gates, entanglement, superposition
- References to quantum hardware, quantum algorithms, quantum simulation

## Action

When scoring papers for Medicine+Quantum or Neuroscience+Quantum cron sessions:
1. Papers matching "quantum-like" keyword should be **deprioritized** unless they also match actual quantum computing keywords
2. Check the arXiv category — if NOT quant-ph/cs.QC/physics.quant-ph, it's likely a mathematical formalism
3. These papers can still be valuable (quantum-like models of memory/cognition), but should be scored and classified differently from quantum computing papers
