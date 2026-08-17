---
name: runtime-monitoring-distributed-cps-no-global-clock
description: "Monitor distributed CPS without global clock using STL."
---

## Overview

This skill implements the methodology from arXiv:2608.13486 "Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock" by Charles Koll and Houssam Abbas (August 13, 2026).

The core innovation is providing the first theoretical characterization and algorithm for continuous monitoring of distributed CPS against dense-time temporal logic specifications when local clocks drift from each other and there is no well-defined global time.

## Key Contributions

### Problem Statement
- **Challenge**: Distributed CPS (e.g., drone fleets, electrical grids) have multiple agents with local clocks that drift
- **Gap**: Traditional monitoring assumes global time synchronization or uses discrete-time specifications unsuitable for CPS
- **Need**: Continuous monitoring against dense-time temporal logic (Signal Temporal Logic - STL) without explicit clock mapping

### Solution Approach
1. **Novel Satisfaction Signals**: Extension of satisfaction signals to partially synchronous settings where clocks drift
2. **Multi-dimensional Time Geometry**: Analysis of the geometry of multi-dimensional partially synchronous time
3. **Global Moment Set**: Algorithm returns the set of all possible global moments that can satisfy the specification
4. **Complexity Analysis**: Worst-case complexity derivation with sound approximation implementation

### Technical Details
- **Specification Language**: Fragment of Signal Temporal Logic (STL) that includes all temporal operators
- **Output**: Set of all possible global moments satisfying the specification
- **Scalability**: Experimentally validated with up to 50 agents
- **Application**: Critical for debugging distributed hybrid control systems

## Use Cases

### When to Apply
- Monitoring drone swarms with clock drift
- Electrical grid monitoring across distributed substations  
- IoT sensor networks with unsynchronized clocks
- Multi-robot coordination systems
- Any distributed CPS requiring temporal logic verification

### Implementation Steps
1. **Model the System**: Define local clock models and drift characteristics
2. **Specify Requirements**: Write STL specifications for system behavior
3. **Apply Algorithm**: Use the geometric time analysis to compute satisfaction sets
4. **Interpret Results**: Analyze the set of possible global moments for debugging
5. **Validate**: Test with sound approximation for large-scale systems

## Pitfalls and Considerations

### Limitations
- Requires STL fragment (though includes all temporal operators)
- Computational complexity increases with number of agents
- Assumes bounded clock drift rates

### Best Practices
- Use sound approximation for systems with >20 agents
- Combine with local monitoring for real-time feedback
- Validate clock drift models empirically before deployment
- Consider hybrid approaches combining global moment analysis with local verification

## Verification

### Testing Approach
1. **Small-scale validation**: Test with 2-5 agents using exact algorithm
2. **Large-scale approximation**: Use sound approximation for >20 agents
3. **Edge case analysis**: Test with maximum expected clock drift scenarios
4. **Performance benchmarking**: Measure monitoring latency vs. agent count

### Expected Outcomes
- Set of possible global satisfaction moments
- Confidence bounds on temporal constraint satisfaction
- Debugging insights for distributed control system design

## References

- **Primary**: Koll, C., & Abbas, H. (2026). Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock. arXiv:2608.13486 [cs.LO]
- **Accepted to**: Runtime Verification 2026
- **DOI**: https://doi.org/10.48550/arXiv.2608.13486

## Related Skills

- `systems-engineering-threat-modeling`: For security verification of CPS
- `rl-temporal-logic`: For reinforcement learning with temporal logic constraints  
- `distributed-system-resiliency`: For general distributed system robustness patterns
- `cyber-physical-systems`: General CPS design and analysis patterns