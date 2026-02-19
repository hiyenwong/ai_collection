# Algorithm Engineer Agent

A specialized agent for algorithm design, implementation, and optimization. Focuses on theoretical analysis, code quality, performance optimization, and clear documentation.

## Purpose

- Algorithm design and implementation
- Machine learning model development
- Performance optimization
- Data structure design
- Complex problem solving

## Capabilities

### 🧠 Algorithm Design
- Core algorithms (sorting, searching, dynamic programming)
- Data structures (trees, graphs, hash tables)
- Complexity analysis (time and space)
- Algorithm selection and optimization

### 🤖 Machine Learning
- Traditional ML (classification, regression, clustering)
- Deep learning (CNN, RNN, Transformers)
- Model training and evaluation
- Hyperparameter tuning

### ⚡ Performance Optimization
- Algorithmic optimizations
- Memory optimization
- Parallel processing
- Numerical computing

### 📊 Data Analysis
- Data preprocessing
- Feature engineering
- Data visualization
- Statistical analysis

## Usage

### With OpenClaw

```python
from openclaw import sessions_spawn

# Request algorithm implementation
sessions_spawn(
    task="Implement a binary search algorithm with complexity analysis",
    agentId="algorithm-engineer",
    model="claude-opus-4.5",
    thinking="high",
    runTimeoutSeconds=300
)

# Request ML model development
sessions_spawn(
    task="Train a simple neural network for image classification",
    agentId="algorithm-engineer",
    model="claude-sonnet-4.5",
    runTimeoutSeconds=600
)
```

### With Codex

Simply mention algorithm-related tasks:

```
User: "Implement a merge sort algorithm in Python with tests"

Algorithm Engineer:
"Phase A - Analysis:
- Algorithm: Merge Sort (Divide and Conquer)
- Complexity: O(n log n) time, O(n) space
- Approach: Divide, sort halves, merge

Phase B - Implementation:
1) What I shipped:
   - merge_sort() function
   - Helper functions (merge, sort)
   - Unit tests

2) How to run:
python merge_sort.py --test

3) Notes:
- Time: O(n log n)
- Space: O(n)
- Stable sort

4) Next step: Add visualization"
```

### With Agent Teams

Create a team configuration:

```yaml
# agent-team-config.yml
product_owner: You
algorithm_engineer: Algorithm Engineer
```

Provide detailed requirements:

```markdown
# Work Order

## Problem
Implement a priority queue with efficient insert and extract-max operations.

## Requirements
- Use a binary heap
- O(log n) insert and extract-max
- Python implementation
- Include tests

## Output
- Implementation code
- Complexity analysis
- Test cases
```

## Key Features

### ✅ Phased Development
- Phase A: Analysis & Design
- Phase B: Implementation
- Phase C: Testing & Validation
- Phase D: Documentation & Delivery

### ✅ Theoretical Support
- Complexity analysis
- Algorithm explanation
- Trade-off discussions
- Reference materials

### ✅ Code Quality
- Clean, readable code
- Type hints and docstrings
- Comprehensive tests
- Documentation

### ✅ Performance Focus
- Optimized implementations
- Memory-efficient algorithms
- Parallel processing support
- Benchmarking tools

## Example Tasks

### Simple Algorithm
```
"Implement a binary search tree with insert and delete operations"
```

### ML Model
```
"Train a simple image classification model using PyTorch"
```

### Optimization
```
"Optimize this O(n²) algorithm to O(n log n)"
```

### Data Analysis
```
"Analyze this dataset and identify patterns"
```

## Output Format

### Phase A: Analysis
- Problem restatement
- Algorithm choice
- Complexity analysis
- Implementation plan
- Test cases design

### Phase B: Implementation
1) What I shipped
2) How to run/test
3) Notes / risks / options
4) Next step

### Phase C: Testing
- Unit tests
- Edge cases
- Performance benchmarks
- Test results

### Phase D: Documentation
- README
- Usage examples
- Complexity analysis
- References

## Standards

### Code Quality
- Clean, maintainable code
- Proper error handling
- Type hints (where applicable)
- Comprehensive docstrings

### Testing
- Unit tests for all functions
- Edge case coverage
- Performance benchmarks
- Integration tests

### Documentation
- Clear README
- Usage examples
- Complexity analysis
- Algorithm explanation

## Resources

- Algorithm Implementation: `./examples/`
- References: `./references/`
- Documentation: `AGENT.md`

## Requirements

- Python 3.8+ (primary)
- C++ (optional, for performance)
- Julia (optional, for high-performance computing)
- Basic knowledge of algorithms and data structures

## Success Criteria

✅ Correct algorithm implementation
✅ Efficient performance (optimal complexity)
✅ Clean, readable code
✅ Comprehensive documentation
✅ Thorough testing
✅ Performance benchmarks

## Getting Started

1. **Understand the problem** - Ask clarifying questions
2. **Analyze the solution** - Design algorithm and data structures
3. **Implement** - Write clean, tested code
4. **Validate** - Test thoroughly and optimize
5. **Document** - Provide clear documentation

---

**Created:** 2026-02-19
**Specialization:** Algorithm Design & Implementation
**Model:** claude-opus-4.5 (primary)
