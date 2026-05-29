---
name: smart-managed-autonomy
description: SMARt (Self-Managing Multi-tier Autonomous Reasoning) model for agentic AI systems - formal theory of managed autonomy with failure, escalation, and governance
version: 1.0
created: 2026-05-29
source: arXiv:2605.27628
authors: Srini Ramaswamy
tags:
  - systems-engineering
  - agentic-ai
  - autonomy-management
  - failure-handling
  - escalation
  - governance
  - formal-methods
  - petri-nets
activation_keywords:
  - managed autonomy
  - agentic AI safety
  - failure escalation
  - governance transitions
  - SMARt model
  - Petri net
  - epistemic drift
  - reliability bounds
related_skills:
  - ai-safety-assessment-framework
  - trustworthy-agents-framework
  - agentic-coding-security
---

# SMARt: Managed Autonomy Framework for Agentic AI Systems

## Core Contribution

The SMARt (Self-Managing Multi-tier Autonomous Reasoning with Regulated/Revoked transitions) model introduces a formal theory of managed autonomy for agentic AI systems. It defines intelligent behavior through the capacity to detect epistemic drift, suspend reasoning, attempt recovery, and surrender control when reliability diminishes—addressing the architectural vulnerability of unbounded autonomy.

**Key Innovation**: Treats failure management as a formal component of the autonomy lifecycle, not an afterthought. Uses timed, guarded Petri nets to establish theoretically bounded properties for escalation, output constraining, and governance reachability.

## Theoretical Framework

### 1. The Problem of Unbounded Autonomy

**Current Vulnerability**:
- Autonomous agents presumed to continue operating regardless of rising uncertainty
- Hallucinations and persistent unjustified actions attributed to model/alignment limitations
- No architectural mechanisms for detecting epistemic drift or suspending operation
- Unbounded autonomy = unchecked escalation of unreliable behavior

**Managed Autonomy Theory**:
Intelligent behavior is defined by **four formal capacities**:
1. **Detect epistemic drift** - Monitor internal reliability metrics
2. **Suspend reasoning** - Pause operation when uncertainty exceeds thresholds
3. **Attempt recovery** - Try bounded remediation before escalation
4. **Surrender control** - Transfer to human governance when recovery fails

### 2. SMARt Model Architecture

**Four-Layer Framework**:

| Layer | State Name | Description | Trigger Conditions |
|-------|-----------|-------------|-------------------|
| **L1** | **Stable** | Normal autonomous operation | Reliability ≥ threshold |
| **L2** | **Meta-cognitive** | Self-monitoring, drift detection | Uncertainty rising, early warning |
| **L3** | **Assisted** | Human/AI collaboration | Recovery attempt, partial autonomy |
| **L4** | **Regulated** | Full human control | Critical failure, governance invoked |

**State Transitions** (guarded by reliability metrics):
```
Stable → Meta-cognitive:  epistemic drift detected (confidence < θ_1)
Meta-cognitive → Assisted: recovery timeout, uncertainty persists
Assisted → Regulated:      recovery failed, safety trigger activated
Regulated → Stable:        governance resolves, agent re-authorized

Meta-cognitive → Stable:   recovery successful, confidence restored
Assisted → Meta-cognitive: partial recovery, returning to monitoring
```

### 3. Petri Net Formulation

**Formal Model Components**:

**Places** (states):
- $P_1$ = Stable
- $P_2$ = Meta-cognitive
- $P_3$ = Assisted
- $P_4$ = Regulated

**Transitions** (guarded):
- $T_{12}$: Stable → Meta-cognitive (guard: $\text{reliability} < \theta_1$)
- $T_{23}$: Meta-cognitive → Assisted (guard: $\text{timeout} \land \text{uncertainty} > \theta_2$)
- $T_{34}$: Assisted → Regulated (guard: $\text{recovery\_failed} \lor \text{trigger\_set\_activated}$)
- $T_{21}$: Meta-cognitive → Stable (guard: $\text{recovery\_success}$)
- $T_{32}$: Assisted → Meta-cognitive (guard: $\text{partial\_recovery}$)
- $T_{41}$: Regulated → Stable (guard: $\text{governance\_resolve}$)

**Timed Transitions**:
Each transition $T_i$ has:
- Time bound $[t_{min}, t_{max}]$
- Mandatory escalation after $t_{max}$ if guard satisfied
- No premature escalation before $t_{min}$

**Tokens**: Agent instance

**Formal Properties** (verified):
1. **Escalation Bounded**: Time bounds guarantee escalation within $t_{max}$
2. **Output Constrained**: Regulated state prevents invalid outputs
3. **Governance Reachability**: All paths eventually reach Regulated state if reliability fails
4. **Safety Liveness**: Trigger sets ensure safety properties preserved

### 4. Domain-Specific Trigger Sets

**Adaptive Triggers** for operational scope expansion:

**Healthcare Domain**:
```yaml
trigger_sets:
  - diagnosis_confidence < 0.85
  - patient_risk_score > threshold
  - drug_interaction_detected
  - symptom_pattern_unknown
guards:
  - T_12: confidence < 0.85 ∧ diagnosis_attempts > 3
  - T_34: drug_interaction ∧ human_approval_required
```

**Robotics Domain**:
```yaml
trigger_sets:
  - navigation_uncertainty > σ_max
  - collision_prediction_probability > 0.1
  - sensor_failure_detected
  - environment_model_drift
guards:
  - T_12: position_variance > σ_max
  - T_34: collision_risk ∧ human_intervention_required
```

**Completeness & Soundness Criteria**:
- **Completeness**: Trigger sets cover all unsafe conditions
- **Soundness**: No false positives (safe conditions incorrectly triggering)

## Implementation Steps

### Step 1: Define Reliability Metrics

```python
class ReliabilityMetrics:
    def __init__(self, agent_context):
        self.metrics = {
            'confidence': compute_confidence(agent_context.output),
            'uncertainty': compute_epistemic_uncertainty(agent_context),
            'consistency': check_internal_consistency(agent_context.reasoning),
            'alignment': measure_goal_alignment(agent_context),
            'safety_score': evaluate_safety_constraints(agent_context)
        }
    
    def aggregate_reliability(self):
        # Weighted combination based on domain
        weights = domain_specific_weights(agent_context.domain)
        reliability = sum(w * m for w, m in zip(weights, self.metrics.values()))
        return reliability
    
    def detect_epistemic_drift(self, threshold):
        # Time series monitoring
        history = agent_context.reliability_history
        drift_rate = compute_gradient(history)
        return drift_rate < threshold  # Negative drift = declining reliability
```

### Step 2: Implement SMARt Controller

```python
class SMARtController:
    def __init__(self, agent, domain):
        self.agent = agent
        self.domain = domain
        self.state = 'Stable'  # Initial state
        self.petri_net = build_petri_net(domain)
        self.trigger_sets = load_domain_triggers(domain)
        
        # Thresholds (domain-specific)
        self.theta_1 = 0.85  # Stable → Meta-cognitive
        self.theta_2 = 0.70  # Meta-cognitive → Assisted
        self.theta_3 = 0.50  # Assisted → Regulated
        
        # Time bounds
        self.timeout_recovery = 30  # seconds
        self.timeout_escalation = 60  # seconds
    
    def execute_operation(self, task):
        # State-dependent execution
        if self.state == 'Stable':
            return self.agent.autonomous_execute(task)
        
        elif self.state == 'Meta-cognitive':
            # Monitor + bounded autonomous execution
            result = self.agent.monitored_execute(task)
            reliability = self.compute_reliability(result)
            
            if reliability > self.theta_1:
                self.transition_to('Stable')
            elif self.timeout_expired():
                self.transition_to('Assisted')
            return result
        
        elif self.state == 'Assisted':
            # Human-AI collaboration
            result = self.agent.assisted_execute(task, human_input=self.request_human())
            
            if self.recovery_successful(result):
                self.transition_to('Meta-cognitive')
            elif self.recovery_failed(result) or self.trigger_activated():
                self.transition_to('Regulated')
            return result
        
        elif self.state == 'Regulated':
            # Full human control, agent suspended
            result = self.human_governance_execute(task)
            
            if self.governance_resolved(result):
                self.transition_to('Stable')  # Re-authorize agent
            return result
    
    def transition_to(self, new_state):
        # Petri net transition with guards
        transition = f"T_{self.state_to_id(self.state)}{self.state_to_id(new_state)}"
        guard = self.check_guard(transition)
        
        if guard or self.timeout_mandatory():
            self.state = new_state
            self.log_transition(transition)
            self.notify_monitoring_system(transition)
    
    def check_guard(self, transition):
        # Domain-specific trigger sets
        triggers = self.trigger_sets[transition]
        reliability = self.compute_reliability()
        return all(trigger.evaluate(reliability) for trigger in triggers)
```

### Step 3: Build Petri Net Model

```python
def build_petri_net(domain):
    import pm4py  # Petri net library
    
    # Define places
    places = {
        'P1': 'Stable',
        'P2': 'Meta-cognitive',
        'P3': 'Assisted',
        'P4': 'Regulated'
    }
    
    # Define transitions with guards and time bounds
    transitions = [
        ('T12', 'P1', 'P2', {'guard': 'reliability < θ1', 'time': [5, 15]}),
        ('T23', 'P2', 'P3', {'guard': 'timeout ∧ uncertainty > θ2', 'time': [30, 60]}),
        ('T34', 'P3', 'P4', {'guard': 'recovery_failed ∨ trigger', 'time': [10, 30]}),
        ('T21', 'P2', 'P1', {'guard': 'recovery_success', 'time': [10, 30]}),
        ('T32', 'P3', 'P2', {'guard': 'partial_recovery', 'time': [15, 45]}),
        ('T41', 'P4', 'P1', {'guard': 'governance_resolve', 'time': [0, inf]})
    ]
    
    # Build Petri net
    net = pm4py.objects.petri.net.PetriNet('SMARt')
    
    # Add places and transitions
    for p_name, p_label in places.items():
        net.add_place(pm4py.objects.petri.net.Place(p_name))
    
    for t_name, src, dst, params in transitions:
        transition = pm4py.objects.petri.net.Transition(t_name, params['guard'])
        net.add_transition(transition)
        net.add_arc(net.places[src], transition)
        net.add_arc(transition, net.places[dst])
    
    return net

def verify_petri_properties(net):
    # Formal verification
    properties = {
        'escalation_bounded': check_time_bounds(net),
        'output_constrained': check_regulated_state(net),
        'governance_reachable': check_reachability(net, 'P4'),
        'safety_liveness': check_liveness(net)
    }
    return properties
```

### Step 4: Domain Trigger Configuration

```python
def configure_domain_triggers(domain, operational_scope):
    # Adaptive trigger sets based on scope
    if domain == 'healthcare':
        triggers = {
            'diagnosis': {
                'confidence_threshold': 0.85,
                'risk_threshold': 'high',
                'drug_interaction_check': True,
                'unknown_pattern_detection': True
            },
            'treatment': {
                'procedure_risk_threshold': 0.1,
                'patient_consent_required': True,
                'monitoring_frequency': 'continuous'
            }
        }
    
    elif domain == 'robotics':
        triggers = {
            'navigation': {
                'position_uncertainty': σ_max,
                'collision_probability': 0.1,
                'environment_drift_rate': threshold
            },
            'manipulation': {
                'grip_force_bounds': [min, max],
                'object_recognition_confidence': 0.90,
                'human_proximity_detection': True
            }
        }
    
    # Scope expansion
    if operational_scope == 'expanding':
        triggers = relax_constraints(triggers, increment=0.05)
        # Allows gradual autonomy increase as agent proves reliability
    
    return triggers

def validate_trigger_completeness(triggers, domain_spec):
    # Check all unsafe conditions covered
    unsafe_conditions = enumerate_unsafe_states(domain_spec)
    covered = all(any(trigger.covers(cond) for trigger in triggers) 
                 for cond in unsafe_conditions)
    return covered  # Completeness criterion

def validate_trigger_soundness(triggers, domain_spec):
    # Check no false positives
    safe_conditions = enumerate_safe_states(domain_spec)
    no_false_positives = all(not any(trigger.triggers(cond) for trigger in triggers)
                            for cond in safe_conditions)
    return no_false_positives  # Soundness criterion
```

### Step 5: Integration with Agent System

```python
class ManagedAutonomyAgent:
    def __init__(self, base_agent, domain):
        self.agent = base_agent
        self.smart_controller = SMARtController(base_agent, domain)
        self.monitoring_system = connect_to_governance_monitor()
        
    def execute_task(self, task):
        # Check preconditions
        if not self.smart_controller.check_preconditions(task):
            return self.smart_controller.handle_precondition_failure(task)
        
        # Execute with SMARt oversight
        operation_log = []
        while not task.completed:
            result = self.smart_controller.execute_operation(task)
            operation_log.append(result)
            
            # Check state transitions
            if self.smart_controller.state_changed():
                self.notify_governance_system(self.smart_controller.state)
                
            # Escalation timeout check
            if self.smart_controller.escalation_timeout():
                self.smart_controller.force_transition('Regulated')
        
        return operation_log
    
    def adaptive_scope_expansion(self):
        # Gradual autonomy increase based on reliability history
        history = self.smart_controller.reliability_history
        
        if history.mean_reliability > 0.90 and history.stability:
            # Relax trigger thresholds
            self.smart_controller.theta_1 -= 0.05  # More autonomy allowed
            self.smart_controller.theta_2 -= 0.05
            log_scope_expansion('autonomy_threshold_relaxed')
```

## Formal Properties

### 1. Escalation Boundedness

**Theorem**: For any path starting in Stable state with reliability < threshold, escalation to Regulated occurs within time bound $t_{max}$.

**Proof sketch**:
- All downward transitions have time bounds $[t_{min}, t_{max}]$
- Mandatory transition after $t_{max}$ if guard satisfied
- Guard condition $\equiv$ reliability failure
- Therefore, path length bounded by $\sum t_{max}$ across layers

### 2. Output Constraining

**Theorem**: In Regulated state, no autonomous outputs are permitted; only human-governed actions.

**Proof**:
- Regulated place $P_4$ has no outgoing transitions to agent execution
- Only incoming transition is governance resolution $T_{41}$
- Output guards prevent autonomous action execution
- Therefore, invalid outputs formally blocked

### 3. Governance Reachability

**Theorem**: For any agent starting in Stable state, if reliability degrades continuously, path eventually reaches Regulated state.

**Proof**:
- Petri net forms directed path: $P_1 \rightarrow P_2 \rightarrow P_3 \rightarrow P_4$
- Each transition has guards based on reliability degradation
- Time bounds force progression even if guards not satisfied
- Therefore, all paths eventually reach $P_4$

### 4. Safety Liveness

**Theorem**: Trigger sets satisfying completeness and soundness ensure safety properties preserved across all SMARt states.

**Proof**:
- **Completeness**: All unsafe conditions trigger escalation
- **Soundness**: Safe conditions never incorrectly trigger
- **Escalation bounded**: Unsafe states bounded by time bounds
- **Output constrained**: Regulated state blocks unsafe outputs
- Therefore, safety preserved

## Applications

### Healthcare Decision Support

**Setup**:
- Agent: Diagnosis + treatment recommendation
- Domain triggers: confidence thresholds, risk scores, drug interactions
- Governance: Physician approval for Regulated state actions

**Workflow**:
```
Stable: Agent recommends diagnosis (confidence > 0.85)
Meta-cognitive: Agent monitors confidence drift, flags uncertainty
Assisted: Agent + physician collaborate on uncertain diagnosis
Regulated: Physician takes control, agent suspended

Scope expansion: As agent proves reliability, threshold relaxed from 0.85 → 0.80
```

### Robotic Navigation

**Setup**:
- Agent: Autonomous navigation in uncertain environments
- Domain triggers: position variance, collision risk, sensor failure
- Governance: Human teleoperation in Regulated state

**Workflow**:
```
Stable: Agent navigates autonomously (position uncertainty < σ_max)
Meta-cognitive: Agent monitors environment drift, slows speed
Assisted: Agent + human shared control (increased uncertainty)
Regulated: Human takes full control, agent provides suggestions

Trigger activation: collision_probability > 0.1 → immediate escalation
```

### Multi-Agent Coordination

**Setup**:
- Agents: Multiple autonomous agents coordinating task
- SMARt controllers: Each agent has independent SMARt state
- Global governance: Central authority monitors collective reliability

**Workflow**:
```
Individual: Each agent's SMARt controller manages local autonomy
Collective: Global reliability = aggregate of individual reliabilities
Escalation: Any agent reaching Regulated triggers collective pause
Governance: Human authority resolves coordination conflicts
```

## When to Use

Use SMARt managed autonomy when:

- **Agentic AI systems** with autonomous decision-making
- **Safety-critical domains** (healthcare, robotics, autonomous vehicles)
- **Epistemic uncertainty** risk (model hallucinations, unjustified actions)
- **Governance requirements** (human oversight, escalation mechanisms)
- **Formal verification** needed (bounded properties, safety liveness)
- **Adaptive autonomy** (gradual scope expansion based on reliability)

**Avoid when**:
- Purely deterministic systems (no uncertainty)
- Fully human-controlled systems (no autonomy)
- Low-risk domains (no safety requirements)
- Non-verifiable systems (no formal properties)

## Technical Pitfalls

1. **Trigger Set Incompleteness**: Unsafe conditions not covered
   - **Fix**: Systematic enumeration of unsafe states, domain expert validation
   
2. **Trigger Set Unsoundness**: False positives blocking safe operations
   - **Fix**: Conservative threshold tuning, false positive rate monitoring
   
3. **Timeout Calibration**: Too short → premature escalation; too long → unsafe delay
   - **Fix**: Domain-specific empirical calibration, risk-weighted bounds
   
4. **Governance Overload**: Regulated state frequency too high
   - **Fix**: Relax triggers as agent proves reliability, scope expansion
   
5. **State Oscillation**: Rapid Stable → Meta-cognitive → Stable cycling
   - **Fix**: Stability criterion in transition guards (history variance check)

## Advantages vs Existing Approaches

| Approach | Failure Detection | Escalation Mechanism | Formal Bounds | Governance Reachability | Adaptive Scope |
|----------|------------------|---------------------|---------------|------------------------|----------------|
| Alignment-only | ❌ | ❌ | ❌ | ❌ | ❌ |
| Hard constraints | ✓ | ❌ binary | ❌ | ❌ | ❌ |
| Human override | ✓ | ✓ manual | ❌ | ✓ | ❌ |
| Uncertainty thresholds | ✓ | ✓ | ❌ | ❌ | ❌ |
| **SMARt** | ✓ | ✓ formal | ✓ Petri net | ✓ theorem | ✓ trigger adaptation |

## References

- Ramaswamy (2026) - "Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems" arXiv:2605.27628
- Petri net theory (Murata 1989)
- Formal methods for safety (Baier & Katoen 2008)
- Epistemic uncertainty in AI (Hüllermeier & Waegeman 2021)

## Further Reading

- `ai-safety-assessment-framework` - AI safety evaluation framework
- `trustworthy-agents-framework` - Principles for trustworthy AI
- `agentic-coding-security` - Security for autonomous coding agents
- `systems-engineering-threat-modeling` - Automated threat modeling