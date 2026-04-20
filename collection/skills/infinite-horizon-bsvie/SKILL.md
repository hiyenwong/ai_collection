---
name: skill.md---infinite-horizon-bsvie-solver
description: Skill for AI agent capabilities
---

# SKILL.md - Infinite-Horizon BSVIE Solver

## Activation Keywords

- BSVIE, backward stochastic Volterra integral equation
- infinite-horizon stochastic equation
- Volterra integral equation, resolvent kernel
- Girsanov transformation, Hida-Malliavin calculus

## What It Does

Provides methodology for solving linear backward stochastic Volterra integral equations (BSVIEs) on infinite time horizon, with explicit solution formulas using resolvent kernels and stochastic transformations.

## When To Use

**Use this skill when:**
- Solving infinite-horizon stochastic integral equations
- Computing explicit solutions for BSVIEs with exponential decay
- Need resolvent kernel construction for Volterra equations
- Applying Girsanov transformation to stochastic equations
- Financial modeling with infinite-horizon backward equations

**Do NOT use for:**
- Finite-horizon BSVIEs (use standard BSVIE theory)
- Non-linear BSVIEs (requires different approach)
- Forward stochastic Volterra equations (different duality)

## How To Use

### Step-by-Step Workflow

1. **Problem Formulation**
   - Define the BSVIE: Y(t) = ξ(T) + ∫_t^T [f(s, Y(s), Z(s, s)) + K(s, t)] ds - ∫_t^T Z(s, t) dW(s)
   - Specify infinite horizon case: T → ∞
   - Identify exponential decay weight: e^(-λt)

2. **Weighted Function Spaces**
   - Introduce weighted space: L^2_λ([0,∞)) with norm ||f||_λ = ∫_0^∞ e^(-λt) |f(t)|^2 dt
   - Ensure adapted M-solutions exist in this space
   - Verify decay conditions on coefficients

3. **Resolvent Kernel Construction**
   - Construct infinite-horizon resolvent kernel R(s, t)
   - Solve resolvent equation: R(s, t) = K(s, t) + ∫_s^∞ K(u, t)R(u, s) du
   - Ensure unique resolvent exists under decay conditions

4. **Explicit Solution Formula**
   - Apply variation of constants formula
   - Compute Y(t) = ∫_t^∞ R(s, t) f(s) ds + boundary term
   - Derive Z(s, t) via Malliavin derivative
   - Apply Girsanov transformation for adapted solutions

5. **Verification**
   - Check adapted M-solution conditions
   - Verify integrability in weighted space
   - Confirm uniqueness via exponential decay

### Key Mathematical Tools

| Tool | Purpose |
|------|---------|
| Weighted L^2_λ space | Ensure existence/uniqueness |
| Resolvent kernel | Explicit solution representation |
| Girsanov transformation | Adapted solution construction |
| Hida-Malliavin calculus | Z-component derivation |

## Example Usage

### Financial Modeling Example

**Problem:** Infinite-horizon investment problem with backward stochastic dynamics

**Input:**
```
BSVIE: Y(t) = ∫_t^∞ [α Y(s) + β Z(s, s)] e^(-λs) ds - ∫_t^∞ Z(s, t) dW(s)
with exponential decay weight λ > 0
```

**Solution approach:**
1. Identify decay rate λ
2. Construct resolvent kernel R(s,t) = α e^(-λ(s-t))
3. Compute Y(t) explicitly via integral formula
4. Derive Z(s,t) via Malliavin calculus

**Output:** Explicit formulas for (Y, Z, K) components

## Description

SKILL.md - Infinite-Horizon BSVIE Solver

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Problem Formulation

### Step 2: Weighted Function Spaces

### Step 3: Resolvent Kernel Construction

### Step 4: Explicit Solution Formula

### Step 5: Verification

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Infinite-Horizon BSVIE Solver to my analysis.

**Agent:** I'll help you apply infinite-horizon-bsvie. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for infinite-horizon-bsvie?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **stochastic-control-hjb** - Hamilton-Jacobi-Bellman approach
- **forward-stochastic-volterra** - Forward SVIE theory
- **girsanov-measure-change** - Girsanov transformation details

## Source

- arXiv:2603.15479v1
- Title: Explicit Solution of Infinite-Horizon Linear Backward Stochastic Volterra Integral Equations
- Utility: 0.88
- Authors: (from arxiv)

## Notes

- Infinite-horizon case requires careful decay conditions
- Resolvent kernel is key to explicit representation
- Girsanov + Hida-Malliavin provide adapted solutions
- Applications: financial mathematics, infinite-horizon control

---

_Created: 2026-04-01_