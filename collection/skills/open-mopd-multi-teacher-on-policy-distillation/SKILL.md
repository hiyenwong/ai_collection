---
name: open-mopd-multi-teacher-on-policy-distillation
description: "Open-MOPD framework for diagnosing and fixing capability imbalance in multi-teacher on-policy distillation. Use when consolidating domain-specialized RL experts into a single generalist student with balanced cross-domain performance."
metadata:
  arxiv_id: "2608.19098"
  authors: "Various Authors"
  published: "2026-08-21"
  tags: [multi-teacher, on-policy-distillation, capability-balance, reinforcement-learning, generalist]
license: Complete terms in LICENSE.txt
---

# Open-MOPD: Multi-Teacher On-Policy Distillation

## Overview
Open-MOPD addresses the capability integration gap in Multi-teacher On-Policy Distillation (M-OPD), where standard approaches capture only 35.6% of available headroom relative to domain-routed oracle ensembles. The framework diagnoses and fixes severe misallocation of token-level optimization budget caused by structural, dynamic, and temporal imbalances across domains.

## Problem Diagnosis

### Capability Integration Gap
- Standard M-OPD captures only **35.6% of available headroom**
- Concise tasks (e.g., instruction following) suffer **severe degradation and premature stagnation**
- Failure stems from **misallocation of token-level optimization budget**, not gradient conflict

### Root Causes
Three orthogonal factors drive the pathology:

1. **Structural sequence-length disparities**: Different domains have vastly different sequence lengths
2. **Dynamic convergence drift**: Non-uniform learning rates cause domains to converge at different speeds  
3. **Multi-step reward staleness**: Asynchronous policy updates create stale rewards

## Core Solutions

### Token-Share Balancing
Addresses structural sequence-length disparities by normalizing optimization budget per token:
```python
# Calculate token share for each domain
domain_token_shares = {}
total_tokens = sum(domain_sequence_lengths.values())
for domain, length in domain_sequence_lengths.items():
    domain_token_shares[domain] = length / total_tokens

# Apply balancing weights
balanced_weights = {domain: 1.0 / (token_share + epsilon) for domain, token_share in domain_token_shares.items()}
```

### Gap-Aware Dynamic Budget Allocation
Addresses dynamic convergence drift by allocating more budget to domains with larger performance gaps:
```python
# Track domain performance over time
domain_performance_history = defaultdict(list)

# Calculate performance gap relative to target
for domain in domains:
    current_perf = get_domain_performance(domain)
    target_perf = get_oracle_performance(domain)
    gap = target_perf - current_perf
    domain_performance_history[domain].append(gap)
    
    # Allocate budget proportional to gap
    gap_moving_avg = moving_average(domain_performance_history[domain][-k:])
    budget_allocation[domain] = gap_moving_avg / sum(all_gaps)
```

### Student Reward Refresh
Addresses multi-step reward staleness by refreshing student rewards more frequently:
```python
# Maintain separate student policy copies for reward calculation
student_reward_policies = {}

# Update reward policies more frequently than main policy
if step % reward_refresh_interval == 0:
    for domain in domains:
        student_reward_policies[domain] = copy.deepcopy(main_student_policy)
        
# Use refreshed policies for reward calculation
rewards = calculate_rewards(rollouts, student_reward_policies)
```

## Implementation Workflow

### Step 1: Establish Controlled Benchmark
Create oracle routing to isolate capability integration from routing ambiguity:
```python
# Oracle routing assigns each prompt to correct domain expert
def oracle_router(prompt):
    domain = classify_prompt_domain(prompt)
    return domain_experts[domain]

# Generate rollouts with oracle routing
oracle_rollouts = generate_rollouts_with_oracle_routing(prompts)
```

### Step 2: Diagnose Imbalance
Measure capability integration gap and identify problematic domains:
```python
# Calculate headroom recovery
oracle_performance = evaluate_oracle_ensemble(oracle_rollouts)
mopd_performance = evaluate_standard_mopd(rollouts)
headroom_recovery = (mopd_performance - random_baseline) / (oracle_performance - random_baseline)

# Identify degraded domains
domain_performances = evaluate_per_domain(rollouts)
degraded_domains = [domain for domain, perf in domain_performances.items() 
                   if perf < threshold * oracle_performances[domain]]
```

### Step 3: Apply Open-MOPD Mechanisms
Implement the three core solutions:

#### Token-Share Balancing Implementation
```python
def calculate_token_shares(rollout_groups):
    """Calculate token shares per domain for balancing."""
    domain_stats = defaultdict(lambda: {'tokens': 0, 'rollouts': 0})
    
    for group in rollout_groups:
        for rollout in group:
            domain = rollout.domain
            domain_stats[domain]['tokens'] += len(rollout.tokens)
            domain_stats[domain]['rollouts'] += 1
    
    total_tokens = sum(stats['tokens'] for stats in domain_stats.values())
    token_shares = {domain: stats['tokens'] / total_tokens 
                   for domain, stats in domain_stats.items()}
    
    return token_shares

def apply_token_share_balancing(losses, domains, token_shares):
    """Apply token-share balancing to losses."""
    balanced_losses = []
    for loss, domain in zip(losses, domains):
        balance_weight = 1.0 / (token_shares[domain] + 1e-8)
        balanced_losses.append(loss * balance_weight)
    return balanced_losses
```

#### Gap-Aware Dynamic Budget Allocation Implementation
```python
class GapAwareBudgetAllocator:
    def __init__(self, domains, window_size=10):
        self.domains = domains
        self.performance_history = {domain: [] for domain in domains}
        self.window_size = window_size
        
    def update_performance(self, domain, performance):
        """Update performance history for a domain."""
        self.performance_history[domain].append(performance)
        if len(self.performance_history[domain]) > self.window_size:
            self.performance_history[domain].pop(0)
            
    def get_budget_allocation(self, oracle_performances):
        """Get budget allocation based on performance gaps."""
        gaps = {}
        for domain in self.domains:
            if self.performance_history[domain]:
                current_perf = np.mean(self.performance_history[domain])
                gap = oracle_performances[domain] - current_perf
                gaps[domain] = max(0, gap)  # Non-negative gaps only
            else:
                gaps[domain] = 1.0  # Default allocation for new domains
                
        total_gap = sum(gaps.values())
        if total_gap == 0:
            # Equal allocation if no gaps
            return {domain: 1.0 / len(self.domains) for domain in self.domains}
            
        return {domain: gap / total_gap for domain, gap in gaps.items()}
```

#### Student Reward Refresh Implementation
```python
class StudentRewardManager:
    def __init__(self, base_policy, refresh_interval=10):
        self.base_policy = base_policy
        self.refresh_interval = refresh_interval
        self.reward_policies = {}
        self.last_refresh_step = {}
        
    def get_reward_policy(self, domain, current_step):
        """Get appropriate reward policy for domain."""
        if (domain not in self.last_refresh_step or 
            current_step - self.last_refresh_step[domain] >= self.refresh_interval):
            self.reward_policies[domain] = copy.deepcopy(self.base_policy)
            self.last_refresh_step[domain] = current_step
            
        return self.reward_policies[domain]
        
    def calculate_rewards(self, rollouts, current_step):
        """Calculate rewards using refreshed policies."""
        rewards = []
        for rollout in rollouts:
            policy = self.get_reward_policy(rollout.domain, current_step)
            reward = policy.calculate_reward(rollout)
            rewards.append(reward)
        return rewards
```

### Step 4: Training Loop Integration
Combine all mechanisms in the training loop:
```python
# Initialize components
budget_allocator = GapAwareBudgetAllocator(domains)
reward_manager = StudentRewardManager(student_policy, refresh_interval=5)

for epoch in range(num_epochs):
    # Generate rollouts
    rollout_groups = generate_rollout_groups(prompts, domains)
    
    # Calculate token shares
    token_shares = calculate_token_shares(rollout_groups)
    
    # Get budget allocation
    oracle_perfs = get_oracle_performances(domains)
    budget_alloc = budget_allocator.get_budget_allocation(oracle_perfs)
    
    # Calculate rewards with refresh
    rewards = reward_manager.calculate_rewards(
        flatten_rollouts(rollout_groups), current_step
    )
    
    # Apply balancing and budget allocation
    domain_list = get_domains_from_rollouts(rollout_groups)
    balanced_rewards = apply_token_share_balancing(rewards, domain_list, token_shares)
    
    # Train student
    loss = calculate_loss(student_predictions, balanced_rewards)
    loss.backward()
    optimizer.step()
    
    # Update performance tracking
    current_perfs = evaluate_current_performance(rollout_groups)
    for domain, perf in current_perfs.items():
        budget_allocator.update_performance(domain, perf)
```

## Performance Results
- **Headroom recovery improved from 35.6% to 83.4%** in a single deployable student
- **Significant improvements across all domains**, especially concise tasks that previously suffered degradation
- **Stable training dynamics** without premature stagnation

## Best Practices

### Oracle Routing Setup
- Use **domain classification** to route prompts to correct experts
- Ensure **clean separation** between domains to isolate capability integration effects
- **Validate oracle performance** before starting M-OPD experiments

### Hyperparameter Selection
- **Token-share balancing**: Usually doesn't require tuning (automatic normalization)
- **Budget allocation window**: Start with 10-20 steps, adjust based on convergence speed
- **Reward refresh interval**: Start with 5-10 steps, shorter intervals for faster-changing domains

### Monitoring and Debugging
- **Track per-domain performance** throughout training
- **Monitor token share distributions** to ensure proper balancing
- **Log budget allocations** to understand dynamic resource distribution

### Scaling Considerations
- **Memory overhead**: Student reward policies require additional memory
- **Computational cost**: Oracle routing and performance tracking add overhead
- **Domain count**: Framework scales well to many domains but monitor memory usage

## Activation Keywords
- open-mopd
- multi-teacher distillation
- capability imbalance
- on-policy distillation
- generalist student
- domain specialization

## References
- Original paper: https://arxiv.org/abs/2608.19098
- Related skills: on-policy-distillation-dlm-transformation, multi-teacher-opd-diagnosis