---
name: secretary-problem-continued-fraction
description: "Secretary problem optimal stopping thresholds are exactly the convergents of 1/e via continued fractions. If p/q is a continued fraction convergent of 1/e with q at least 3, then for q applicants the optimal number to initially reject is p. Connects optimal stopping theory, continued fractions, and the mathematical constant e. Use when: optimal stopping problems, secretary problem analysis, continued fraction applications, 1/e thresholds, decision theory, sequential selection."
metadata:
  arxiv_id: "2606.19298"
  published: "2026-06-17"
  authors: "Unknown"
  tags: [number-theory, optimal-stopping, continued-fraction, secretary-problem, statistics, decision-theory]
---

# Secretary Problem Continued Fraction Thresholds

## Core Theorem

**Theorem**: If p/q is a continued fraction convergent of 1/e with q >= 3, then for the secretary problem with q applicants, the optimal number of initially rejected applicants is p.

This establishes an exact correspondence between:
- The **secretary problem** (classic optimal stopping: interview q candidates sequentially, reject the first k, then select the next candidate better than all rejected)
- The **continued fraction expansion of 1/e** (the irrational number ~0.3679)

## Mathematical Framework

### Secretary Problem Setup

- Interview q candidates in random order
- Must decide immediately after each interview
- Goal: maximize probability of selecting the best candidate
- Optimal strategy: reject first k candidates, then select next best-seen

### The 1/e Connection

The classical asymptotic solution rejects approximately q/e candidates (~36.8%).

The continued fraction of 1/e = [0; 2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]

Convergents (p/q):
- 0/1, 1/2, 1/3, 3/8, 4/11, 7/19, 32/87, 39/106, 71/193, 465/1264, ...

### Key Result

For each convergent p/q of 1/e (with q >= 3):
- The secretary problem with exactly q applicants
- Has optimal rejection threshold exactly k = p
- This is not approximate — it is exact

### Why This Works

The secretary problem's optimal threshold k*(q) is the integer that maximizes:
P(select best) = (k/q) * sum_{i=k+1}^{q} 1/(i-1)

The continued fraction convergents of 1/e provide the sequence of (p, q) pairs where p/q most closely approximates 1/e. The proof shows these approximations are precise enough that p is exactly the optimal k* for each q.

## Usage Patterns

### Optimal Stopping Analysis
1. Given q candidates for a sequential selection problem
2. Check if q appears in the convergent sequence of 1/e
3. If so, the optimal rejection count is the corresponding p
4. Otherwise, compute k*(q) = round(q/e) as approximation

### Continued Fraction Applications
1. Compute continued fraction convergents of 1/e
2. Each convergent (p, q) gives an exact secretary problem solution
3. Pattern: denominators grow as 1, 2, 3, 8, 11, 19, 87, 106, 193, 1264, ...

### Statistical Decision Theory
- Generalizes to other optimal stopping problems
- Connection between irrational constants and discrete optimization
- Provides exact solutions where classical methods only give asymptotics

## Implementation

```python
def continued_fraction_convergents_of_1_over_e(n_terms=10):
    """Generate convergents of 1/e continued fraction."""
    # 1/e = [0; 2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
    # Pattern: [0; 2, 1, 2k, 1, 1, 2(k+1), 1, 1, ...] for k=1,2,...
    import math
    
    e_inv = 1 / math.e
    
    # Generate CF terms
    terms = [0, 2]
    for k in range(1, n_terms):
        terms.extend([1, 2*k, 1])
    
    # Compute convergents
    convergents = []
    for n in range(1, len(terms)):
        cf = terms[:n+1]
        # Evaluate continued fraction
        num, den = 1, cf[-1]
        for a in reversed(cf[:-1]):
            num, den = den, a * den + num
        convergents.append((den, num))  # (numerator, denominator)
    
    return convergents

def secretary_optimal_threshold(q):
    """Find optimal k for secretary problem with q candidates."""
    import math
    best_p = 0
    best_prob = 0
    for k in range(1, q):
        prob = (k / q) * sum(1 / (i - 1) for i in range(k + 1, q + 1))
        if prob > best_prob:
            best_prob = prob
            best_p = k
    return best_p, best_prob
```

## Connections

- **Number Theory**: Continued fraction structure of e (transcendental number)
- **Statistics**: Optimal stopping theory, sequential analysis
- **Decision Theory**: Classic secretary/optimal stopping problems
- **Combinatorics**: Exact solutions from irrational approximations

## Pitfalls

- The exact correspondence only holds for convergents, not arbitrary rational approximations
- For non-convergent q values, round(q/e) is an approximation, not exact
- The theorem requires q >= 3; smaller cases are trivial
