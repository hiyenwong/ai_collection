# QAOA Benchmark Methodology

## Problem Set
- MaxCut (unweighted graphs)
- Weighted MaxCut
- Maximum Independent Set (MIS)
- Weighted MIS
- Knapsack problems

## Metrics
- Decoded ratio: solution quality / optimal solution
- Win/tie/loss counts against standard QAOA
- Mean improvement over baseline

## Results Summary
- 1500 paired test cases across all problems
- MUB-XRot non-worse in 80.0% (1200/1500)
- Win: 829, Tie: 371, Loss: 300
- Mean decoded-ratio improvement: +0.1616

## QRAO MaxCut
- Bit-flip MUB-family search
- Mean relaxed ratio: 0.921
- Improvement over X-variational: +0.0608
