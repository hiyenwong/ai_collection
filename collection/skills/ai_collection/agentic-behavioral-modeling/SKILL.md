---
name: agentic-behavioral-modeling
description: >
  Agentic Behavioral Modeling (ABM) — treating artificial agents as latent
  generative hypotheses about cognitive mechanisms, evaluating them by
  statistical adequacy in explaining human behavior. Bridges theoretical
  neuroscience, decision theory, and probabilistic inference with agentic AI.
version: 1.0.0
author: Hermes (Nous Research)
license: MIT
created: 2026-05-02
metadata:
  tags:
    - neuroscience
    - computational-psychiatry
    - decision-theory
    - probabilistic-inference
    - agent-modeling
    - cognitive-science
    - reinforcement-learning
    - bayesian-inference
  source_paper: "arXiv:2604.27894"
  source_title: "On Agentic Behavioral Modeling"
  source_authors: "Dirk Ostwald et al."
  source_date: "2026-04-30"
  source_category: "q-bio.NC"
---

# Agentic Behavioral Modeling (ABM)

## Overview

Agentic Behavioral Modeling (ABM) is a framework that treats **artificial agents as latent generative hypotheses** about the cognitive mechanisms underlying observed human behavior. Instead of asking whether an agent performs well on a task, ABM asks whether the agent **statistically adequately explains** how humans actually behave.

The framework formalizes a **task-agent-data system** as a joint probability model with explicit conditional log-likelihoods, enabling rigorous model comparison, parameter recovery, and agent-centric interpretation of behavioral data.

### Core Insight

> Artificial agents are not just tools for solving tasks — they are formal, computational hypotheses about *how* cognition works. Their adequacy is measured by their ability to generate behavior statistically indistinguishable from human data.

---

## Key Concepts

### 1. Task-Agent-Data System

The ABM framework defines three coupled components:

- **Task (T)**: Formal specification of environment dynamics, stimuli, rewards, and observation structure.
- **Agent (A)**: Policy π(a|s; θ) parameterized by θ, mapping states/observations to action probabilities.
- **Data (D)**: Observed behavior — sequences of stimuli, actions, and outcomes from human subjects.

The joint probability model:

```
p(D, θ | T) = p(D | θ, T) × p(θ | T)
```

where the likelihood `p(D | θ, T)` is computed by marginalizing over the agent's internal latent states.

### 2. Conditional Log-Likelihood

For a sequence of trials `t = 1, ..., N`:

```
LL(θ) = Σ_t log p(a_t | s_t, h_{t-1}; θ)
```

where `h_{t-1}` is the agent's internal history/state at trial `t-1`. This is the core evaluation metric — the log-probability the agent assigns to the actually-observed actions.

### 3. Agent-Centric Psychometric Function

The traditional psychometric function maps stimulus intensity → response probability. ABM reinterprets this: the psychometric function is the **marginal prediction** of a specific agent hypothesis, derived from its internal policy and belief state, rather than a generic sigmoidal curve fit.

### 4. Model & Parameter Recovery

ABM validates its approach through two simulation protocols:

- **Model recovery**: Generate data from each candidate agent, then recover the generating model via likelihood comparison. High diagonal accuracy indicates identifiability.
- **Parameter recovery**: Generate data from known parameters, then estimate them back. Strong correlation between true and recovered parameters validates the inference procedure.

---

## Implementation Patterns

### Pattern 1: Binary Perceptual Contrast-Discrimination Task

In this task, an agent decides which of two stimuli has higher contrast. The optimal policy depends on the agent's sensory noise model and decision threshold.

```python
import numpy as np
from scipy.stats import norm

class ContrastDiscriminationTask:
    """Binary perceptual contrast-discrimination task."""

    def __init__(self, contrast_levels, n_trials=100):
        self.contrast_levels = np.array(contrast_levels)
        self.n_trials = n_trials

    def generate_stimuli(self):
        """Generate stimulus pairs with given contrast differences."""
        contrasts = np.random.choice(self.contrast_levels, size=(self.n_trials, 2))
        return contrasts

    def optimal_policy(self, c1, c2, threshold=0.0, sensory_noise=0.1):
        """
        Optimal decision policy for contrast discrimination.
        Returns P(choose stimulus 1 | c1, c2).

        Derivation: agent forms noisy percepts x1 ~ N(c1, σ²), x2 ~ N(c2, σ²),
        and chooses stimulus 1 when x1 - x2 > threshold.
        """
        delta = c1 - c2
        z = (delta - threshold) / (sensory_noise * np.sqrt(2))
        return norm.cdf(z)


class AgentCentricPsychometricFunction:
    """
    Derive psychometric function from agent model rather than fitting a
    generic sigmoidal curve.
    """

    def __init__(self, task, sensory_noise, decision_noise):
        self.task = task
        self.sensory_noise = sensory_noise
        self.decision_noise = decision_noise

    def evaluate(self, contrast_diffs):
        """
        Compute P(choose 'higher') as a function of contrast difference,
        as predicted by the agent model.
        """
        probs = []
        for d in contrast_diffs:
            p = self.task.optimal_policy(
                d / 2, -d / 2,
                sensory_noise=self.sensory_noise
            )
            probs.append(p)
        return np.array(probs)

    def fit_to_data(self, contrast_diffs, observed_choices):
        """Fit agent parameters to behavioral data via maximum likelihood."""
        from scipy.optimize import minimize

        def neg_ll(params):
            sn, dn = params
            predicted = self.evaluate(contrast_diffs)
            # Binary cross-entropy log-likelihood
            ll = np.sum(
                observed_choices * np.log(predicted + 1e-10) +
                (1 - observed_choices) * np.log(1 - predicted + 1e-10)
            )
            return -ll

        result = minimize(neg_ll, [0.1, 0.1], bounds=[(0.01, 2.0), (0.01, 2.0)])
        return result.x, -result.fun
```

### Pattern 2: Symmetric Two-Armed Bandit Learning Task

In the symmetric two-armed bandit, two options yield rewards with probabilities p and (1-p). ABM shows the **equivalence between Rescorla-Wagner learning and Bayesian inference** in this setting.

```python
import numpy as np

class SymmetricTwoArmedBandit:
    """
    Symmetric two-armed bandit task.
    Rewards: arm A ~ Bernoulli(p), arm B ~ Bernoulli(1-p).
    """

    def __init__(self, p=0.7, n_trials=200):
        self.p = p
        self.n_trials = n_trials

    def sample_reward(self, action):
        """Sample reward for chosen action (0 or 1)."""
        prob = self.p if action == 0 else (1 - self.p)
        return np.random.binomial(1, prob)


class RescorlaWagnerAgent:
    """
    Rescorla-Wagner learning agent.
    Update rule: V(a) ← V(a) + α * δ, where δ = r - V(a)
    Action selection via softmax: π(a) ∝ exp(β * V(a))
    """

    def __init__(self, alpha=0.1, beta=3.0, n_actions=2):
        self.alpha = alpha   # learning rate
        self.beta = beta     # inverse temperature
        self.n_actions = n_actions
        self.values = np.zeros(n_actions)
        self.reset()

    def reset(self):
        self.values = np.zeros(self.n_actions)

    def choose_action(self):
        """Softmax action selection."""
        logits = self.beta * self.values
        # Subtract max for numerical stability
        logits = logits - np.max(logits)
        probs = np.exp(logits) / np.exp(logits).sum()
        return np.random.choice(self.n_actions, p=probs), probs

    def update(self, action, reward):
        """Rescorla-Wagner update."""
        prediction_error = reward - self.values[action]
        self.values[action] += self.alpha * prediction_error

    def log_likelihood(self, actions, rewards):
        """
        Compute conditional log-likelihood of observed action sequence.
        LL = Σ_t log π(a_t | h_{t-1}; α, β)
        """
        self.reset()
        ll = 0.0
        for a, r in zip(actions, rewards):
            _, probs = self.choose_action()
            ll += np.log(probs[a] + 1e-10)
            self.update(a, r)
        return ll


class BayesianInferenceAgent:
    """
    Bayesian inference agent for the symmetric two-armed bandit.
    Maintains Beta posterior over reward probabilities.
    In the symmetric case, this is equivalent to Rescorla-Wagner
    with specific parameter mappings.
    """

    def __init__(self, prior_alpha=1.0, prior_beta=1.0, beta=3.0, n_actions=2):
        self.prior_alpha = prior_alpha
        self.prior_beta_param = prior_beta
        self.beta_param = beta
        self.n_actions = n_actions
        self.reset()

    def reset(self):
        self.successes = np.full(self.n_actions, self.prior_alpha)
        self.failures = np.full(self.n_actions, self.prior_beta_param)

    def expected_value(self, action):
        """E[p] under Beta posterior."""
        return self.successes[action] / (
            self.successes[action] + self.failures[action]
        )

    def choose_action(self):
        """Choose action with highest expected value, with softmax noise."""
        ev = np.array([self.expected_value(a) for a in range(self.n_actions)])
        logits = self.beta_param * ev
        logits = logits - np.max(logits)
        probs = np.exp(logits) / np.exp(logits).sum()
        return np.random.choice(self.n_actions, p=probs), probs

    def update(self, action, reward):
        """Bayesian update of Beta posterior."""
        if reward == 1:
            self.successes[action] += 1
        else:
            self.failures[action] += 1

    def log_likelihood(self, actions, rewards):
        """Conditional log-likelihood under Bayesian model."""
        self.reset()
        ll = 0.0
        for a, r in zip(actions, rewards):
            _, probs = self.choose_action()
            ll += np.log(probs[a] + 1e-10)
            self.update(a, r)
        return ll
```

### Pattern 3: Model Comparison via Conditional Log-Likelihood

```python
def compare_agents(agents, data_actions, data_rewards, model_names=None):
    """
    Compare multiple agent models by their conditional log-likelihood
    on observed behavioral data.

    Returns ranked list of (model_name, log_likelihood).
    """
    if model_names is None:
        model_names = [f"agent_{i}" for i in range(len(agents))]

    results = []
    for agent, name in zip(agents, model_names):
        ll = agent.log_likelihood(data_actions, data_rewards)
        n_params = _count_parameters(agent)
        # BIC for model comparison
        n = len(data_actions)
        bic = -2 * ll + n_params * np.log(n)
        results.append({
            "model": name,
            "log_likelihood": ll,
            "n_parameters": n_params,
            "BIC": bic,
        })

    results.sort(key=lambda x: x["BIC"])
    return results


def _count_parameters(agent):
    """Count free parameters of an agent model."""
    count = 0
    if hasattr(agent, 'alpha'):
        count += 1
    if hasattr(agent, 'beta'):
        count += 1
    if hasattr(agent, 'beta_param') and not hasattr(agent, 'alpha'):
        count += 1
    if hasattr(agent, 'prior_alpha'):
        count += 1
    if hasattr(agent, 'prior_beta_param'):
        count += 1
    return count
```

### Pattern 4: Parameter Recovery Simulation

```python
def parameter_recovery(true_params, n_simulations=50, n_trials=200, p_bandit=0.7):
    """
    Validate parameter inference by checking if true parameters
    can be recovered from simulated data.

    Args:
        true_params: dict of true parameter values
        n_simulations: number of recovery runs
        n_trials: trials per simulation

    Returns:
        dict with correlations between true and recovered parameters.
    """
    from scipy.optimize import minimize

    recovered = {k: [] for k in true_params}

    for sim in range(n_simulations):
        # Generate data from true parameters
        agent = RescorlaWagnerAgent(
            alpha=true_params["alpha"],
            beta=true_params["beta"]
        )
        task = SymmetricTwoArmedBandit(p=p_bandit, n_trials=n_trials)

        actions, rewards = [], []
        for _ in range(n_trials):
            a, _ = agent.choose_action()
            r = task.sample_reward(a)
            agent.update(a, r)
            actions.append(a)
            rewards.append(r)

        # Recover parameters via maximum likelihood
        def neg_ll(params):
            a, b = params
            test_agent = RescorlaWagnerAgent(alpha=a, beta=b)
            return -test_agent.log_likelihood(actions, rewards)

        result = minimize(
            neg_ll,
            x0=[0.5, 2.0],
            bounds=[(0.01, 1.0), (0.1, 10.0)],
            method="L-BFGS-B"
        )
        recovered["alpha"].append(result.x[0])
        recovered["beta"].append(result.x[1])

    # Compute recovery quality
    correlations = {}
    for key in true_params:
        true_vals = np.full(n_simulations, true_params[key])
        r = np.corrcoef(true_vals, recovered[key])[0, 1]
        correlations[key] = r

    return {
        "recovered_means": {k: np.mean(v) for k, v in recovered.items()},
        "recovered_stds": {k: np.std(v) for k, v in recovered.items()},
        "correlations": correlations,
    }
```

### Pattern 5: Model Recovery Simulation (Confusion Matrix)

```python
def model_recovery(agent_classes, param_configs, n_simulations=30, n_trials=200):
    """
    Model recovery: generate data from each model, fit all models,
    check if the generating model is correctly identified.

    Returns confusion matrix: rows = generating model, cols = winning model.
    """
    n_models = len(agent_classes)
    confusion = np.zeros((n_models, n_models))

    for gen_idx, (AgentClass, params) in enumerate(zip(agent_classes, param_configs)):
        correct = 0
        for sim in range(n_simulations):
            # Generate data from generating model
            agent = AgentClass(**params)
            task = SymmetricTwoArmedBandit(n_trials=n_trials)

            actions, rewards = [], []
            for _ in range(n_trials):
                a, _ = agent.choose_action()
                r = task.sample_reward(a)
                agent.update(a, r)
                actions.append(a)
                rewards.append(r)

            # Fit all models and find best
            best_ll = -np.inf
            best_idx = 0
            for test_idx, (TestAgent, _) in enumerate(zip(agent_classes, param_configs)):
                test_agent = TestAgent()
                ll = test_agent.log_likelihood(actions, rewards)
                if ll > best_ll:
                    best_ll = ll
                    best_idx = test_idx

            confusion[gen_idx, best_idx] += 1

    confusion /= n_simulations  # Normalize to proportions
    return confusion
```

### Pattern 6: Optimal Policy Derivation

```python
def derive_optimal_policy_bandit(p, horizon=20, discount=1.0):
    """
    Derive optimal policy for symmetric two-armed bandit via
    dynamic programming / backward induction.

    The state is (n1, r1, n2, r2) — number of pulls and rewards for each arm.
    Optimal action maximizes expected cumulative reward.
    """
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def value(n1, r1, n2, r2, remaining):
        if remaining == 0:
            return 0.0

        # Expected value of pulling arm 0
        mu0 = (r1 + 1) / (n1 + 2)  # Beta posterior mean
        ev0 = mu0 + discount * (
            mu0 * value(n1 + 1, r1 + 1, n2, r2, remaining - 1) +
            (1 - mu0) * value(n1 + 1, r1, n2, r2, remaining - 1)
        )

        # Expected value of pulling arm 1
        mu1 = (r2 + 1) / (n2 + 2)
        ev1 = mu1 + discount * (
            mu1 * value(n1, r1, n2 + 1, r2 + 1, remaining - 1) +
            (1 - mu1) * value(n1, r1, n2 + 1, r2, remaining - 1)
        )

        return max(ev0, ev1)

    def optimal_action(n1, r1, n2, r2, remaining):
        mu0 = (r1 + 1) / (n1 + 2)
        ev0 = mu0 + discount * (
            mu0 * value(n1 + 1, r1 + 1, n2, r2, remaining - 1) +
            (1 - mu0) * value(n1 + 1, r1, n2, r2, remaining - 1)
        )
        mu1 = (r2 + 1) / (n2 + 2)
        ev1 = mu1 + discount * (
            mu1 * value(n1, r1, n2 + 1, r2 + 1, remaining - 1) +
            (1 - mu1) * value(n1, r1, n2 + 1, r2, remaining - 1)
        )
        return 0 if ev0 >= ev1 else 1

    return optimal_action, value
```

---

## Workflow

### End-to-End ABM Analysis Pipeline

```
1. TASK SPECIFICATION
   └─ Formalize task dynamics, stimuli, rewards

2. AGENT HYPOTHESES
   └─ Define candidate agent models with parameterized policies

3. OPTIMAL POLICY DERIVATION
   └─ Compute normative benchmark for the task

4. MODEL FITTING
   └─ Maximize conditional log-likelihood on human data

5. MODEL COMPARISON
   └─ Compare agents via LL, AIC, BIC

6. VALIDATION
   ├─ Model recovery (confusion matrix)
   └─ Parameter recovery (correlation analysis)

7. INTERPRETATION
   └─ Agent-centric psychometric function, parameter estimates
```

---

## When to Use This Skill

- **Computational modeling of human behavior** in decision-making tasks
- **Comparing cognitive theories** formalized as different agent architectures
- **Deriving normative benchmarks** for behavioral tasks
- **Fitting agent models to behavioral data** via maximum likelihood
- **Validating modeling approaches** through recovery simulations
- **Reinterpreting psychometric functions** through agent-specific predictions
- **Bridging RL agents and cognitive models** for neuroscience research

---

## Activation Keywords

### English
- agentic behavioral modeling
- agent as hypothesis
- cognitive model comparison
- conditional log-likelihood agent
- model recovery simulation
- parameter recovery simulation
- agent-centric psychometric function
- perceptual contrast discrimination
- two-armed bandit modeling
- Rescorla-Wagner vs Bayesian
- behavioral model fitting
- computational cognitive modeling
- agent model adequacy
- latent generative hypothesis
- normative policy derivation
- joint probability task-agent-data
- agent log-likelihood evaluation
- cognitive mechanism modeling
- decision theory agent
- probabilistic agent inference

### Chinese
- 代理行为建模
- 代理作为假设
- 认知模型比较
- 条件对数似然代理
- 模型恢复模拟
- 参数恢复模拟
- 代理中心心理测量函数
- 知觉对比辨别
- 双臂老虎机建模
- Rescorla-Wagner与贝叶斯
- 行为模型拟合
- 计算认知建模
- 代理模型充分性
- 潜在生成假设
- 规范策略推导
- 联合概率任务代理数据
- 代理对数似然评估
- 认知机制建模
- 决策理论代理
- 概率代理推断

---

## References

- **Source Paper**: Ostwald, D. et al. "On Agentic Behavioral Modeling." arXiv:2604.27894 [q-bio.NC], 30 Apr 2026.
- **Rescorla-Wagner Model**: Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning.
- **Bayesian Models of Cognition**: Tenenbaum, J. B. et al. (2011). How to grow a mind. *Science*, 331(6022), 1279-1285.
- **Computational Psychiatry**: Huys, Q. J. M. et al. (2016). Computational psychiatry as a mechanistic understanding of mental illness. *Nature Reviews Neuroscience*, 17, 409-419.
- **Model Comparison**: Wagenmakers, E.-J., & Farrell, S. (2004). AIC model selection using Akaike weights. *Psychonomic Bulletin & Review*, 11(1), 192-196.
