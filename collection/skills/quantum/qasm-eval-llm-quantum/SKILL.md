---
name: qasm-eval-llm-quantum
description: "Benchmark methodology for training and evaluating LLMs on OpenQASM-3 hardware-facing features. First comprehensive dataset for LLM quantum programming beyond gate sequences, covering classical logic, timing scheduling, pulse control, and real-world workflows."
---

# QASM-Eval: LLM Evaluation for OpenQASM-3

## Description

Methodology from arXiv:2605.30358 (May 2026). In the NISQ era, quantum computing performance requires hardware-facing capabilities beyond gate-sequence specification: mid-circuit measurement, classical feedback for QEC, precise timing control for dynamical decoupling, and pulse-level waveform access for calibration. OpenQASM-3 exposes these capabilities but no dataset existed to train/evaluate LLMs on OpenQASM-3 with hardware-oriented features.

QASM-Eval fills this gap with:
- **Test set**: 100 expert-verified tasks
- **Training set**: 4,000 tasks
- **Coverage**: Classical logic, timing scheduling, pulse control, complex workflows
- **Validation**: Extended verifier checking syntax, quantum states, and program timeline

Key finding: State-of-the-art LLMs struggle heavily on OpenQASM-3 coding tasks, but targeted fine-tuning on QASM-Eval yields significant gains.

**Activation**: QASM-Eval, OpenQASM-3 LLM, quantum programming benchmark, LLM quantum coding, pulse-level quantum programming, hardware-facing quantum, 量子编程评估

## Core Methodology

### Step 1: Task Categorization

| Category | Description | Example |
|----------|-------------|---------|
| Classical logic | Conditional operations, classical registers | if-else based on measurement |
| Timing scheduling | Precise timing control, delays | Dynamical decoupling sequences |
| Pulse control | Waveform access, calibration | Custom pulse shapes |
| Complex workflows | Multi-component real-world tasks | Full QEC cycle |

### Step 2: Extended Verification Pipeline

```python
class QASMVerifier:
    def verify(self, generated_program, reference_program):
        """Extended verification beyond syntax."""
        results = {}
        
        # 1. Syntax check
        results['syntax'] = self.check_syntax(generated_program)
        
        # 2. Quantum state verification
        results['state'] = self.compare_quantum_states(
            generated_program, reference_program
        )
        
        # 3. Timeline verification
        results['timeline'] = self.verify_timing_constraints(
            generated_program
        )
        
        return results
    
    def check_syntax(self, program):
        """Parse and validate OpenQASM-3 syntax."""
        try:
            import openqasm3
            openqasm3.parse(program)
            return True
        except:
            return False
    
    def compare_quantum_states(self, gen_prog, ref_prog):
        """Simulate both programs and compare output states."""
        gen_state = self.simulate(gen_prog)
        ref_state = self.simulate(ref_prog)
        # Fidelity comparison
        fidelity = abs(np.vdot(gen_state, ref_state))**2
        return fidelity > 0.99  # Threshold
    
    def verify_timing_constraints(self, program):
        """Check that timing requirements are met."""
        # Parse duration declarations
        # Verify no timing conflicts
        # Check hardware constraints
        return True  # Simplified
```

### Step 3: LLM Evaluation Protocol

```python
def evaluate_llm_on_qasm(llm_client, tasks, n_samples=1):
    """Evaluate LLM on OpenQASM-3 tasks."""
    results = []
    verifier = QASMVerifier()
    
    for task in tasks:
        prompt = build_qasm_prompt(task)
        response = llm_client.generate(prompt, n=n_samples)
        
        for sample in response:
            verification = verifier.verify(sample, task.reference)
            results.append({
                'task_id': task.id,
                'category': task.category,
                'verified': verification['syntax'] and 
                           verification['state'] and 
                           verification['timeline'],
                'scores': verification
            })
    
    return results
```

### Step 4: Fine-Tuning Protocol

```python
def fine_tune_on_qasm_eval(model, training_data, epochs=3):
    """Fine-tune LLM on QASM-Eval training set."""
    # Standard instruction fine-tuning
    # Input: task description
    # Output: valid OpenQASM-3 program
    for epoch in range(epochs):
        for batch in training_data:
            loss = compute_loss(model, batch)
            loss.backward()
            optimizer.step()
```

## Key Findings

1. **LLMs struggle**: State-of-the-art models perform poorly on OpenQASM-3
2. **Fine-tuning works**: Targeted training yields significant gains
3. **Hardware features matter**: Existing benchmarks focus on gate sequences only
4. **Verification is multi-dimensional**: Syntax + states + timeline all needed

## Integration with Quantum Workflows

QASM-Eval enables:
- **Automated quantum programming**: LLM assistants for NISQ-era programming
- **QEC implementation**: LLM-generated error correction circuits
- **Pulse-level optimization**: Hardware-aware circuit compilation
- **Educational tools**: Automated quantum programming tutoring

## Related Skills
- pulse-level-quantum-computing: Pulse-level quantum programming
- quantum-compiler-routing: Qubit mapping and routing
- quantum-program-linting: Quantum program analysis

## References
- **Paper**: "QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits" (arXiv:2605.30358)
- **Authors**: Zhenxiao Fu, Lei Jiang, Fan Chen
- **Categories**: cs.LG, quant-ph
- **Date**: May 28, 2026
