---
name: agentic-behavioral-modeling
description: "Agentic Behavioral Modeling (ABM) framework integrating theoretical neuroscience, decision theory, and probabilistic inference. Treats AI agents as latent generative hypotheses about cognitive mechanisms for explaining human behavior. Activation triggers: agentic modeling, behavioral modeling, cognitive agents, decision theory, Rescorla-Wagner learning, Bayesian inference."
---

# Agentic Behavioral Modeling Framework

> A framework for treating artificial agents as latent, generative hypotheses about cognitive mechanisms and evaluating them by statistical adequacy in explaining human behavior.

## Metadata
- **Source**: arXiv:2604.27894
- **Authors**: Dirk Ostwald, Rasmus Bruckner, Franziska Usée, Belinda Fleischmann, Joram Soch, Sean Mulready
- **Published**: 2026-04-30
- **Category**: Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation
ABM bridges agentic AI models and behavioral data analysis by formalizing task-agent-data systems as joint probability models. This enables rigorous model comparison through explicit conditional log-likelihoods and statistical validation.

### Theoretical Foundation

**Three Pillars:**
1. **Theoretical Neuroscience**: Mechanistic accounts of neural computation
2. **Decision Theory**: Normative frameworks for optimal choice
3. **Probabilistic Inference**: Statistical methods for model evaluation

**Core Principle:**
```
Artificial Agent → Latent Cognitive Hypothesis
       ↓
Generative Model of Behavior
       ↓
Statistical Evaluation via Likelihood
```

### Formal Framework

#### Joint Probability Model
```
p(a, d | θ, m) = p(a | d, θ, m) * p(d | θ, m)
```
Where:
- `a`: Agent parameters
- `d`: Behavioral data
- `θ`: Model parameters
- `m`: Model structure

#### Conditional Log-Likelihood
```
log L(θ | d, m) = Σ_i log p(d_i | θ, m)
```

## Implementation Examples

### Example 1: Perceptual Contrast Discrimination

**Task**: Binary perceptual decision

**Agent Model**: Signal Detection Theory (SDT) Agent
```python
class SDTAgent:
    def __init__(self, d_prime, criterion):
        self.d_prime = d_prime  # Sensitivity
        self.criterion = criterion  # Response bias
    
    def decision(self, stimulus_contrast):
        # Internal signal with noise
        signal = stimulus_contrast + np.random.normal(0, 1)
        # Decision rule
        return 1 if signal > self.criterion else 0
    
    def choice_probability(self, contrast):
        """Psychometric function."""
        from scipy.stats import norm
        return 1 - norm.cdf(self.criterion - self.d_prime * contrast)
```

**Agent-Centric Psychometric Function:**
```
P(choose_high | contrast c) = Φ(d' * c - λ)
```
Where Φ is the standard normal CDF, d' is sensitivity, and λ is the criterion.

### Example 2: Two-Armed Bandit Learning

**Task**: Sequential reward maximization

**Agent Models**:

1. **Rescorla-Wagner (RW) Learning**:
```python
class RescorlaWagnerAgent:
    def __init__(self, alpha, beta, n_arms=2):
        self.alpha = alpha  # Learning rate
        self.beta = beta    # Inverse temperature
        self.Q = np.zeros(n_arms)  # Action values
        
    def choose_action(self):
        # Softmax choice
        probs = np.exp(self.beta * self.Q)
        probs /= probs.sum()
        return np.random.choice(len(self.Q), p=probs)
    
    def update(self, action, reward):
        # Prediction error
        prediction_error = reward - self.Q[action]
        # Value update
        self.Q[action] += self.alpha * prediction_error
        return prediction_error
```

2. **Bayesian Optimal Agent**:
```python
class BayesianBanditAgent:
    def __init__(self, n_arms=2):
        # Prior: Beta(1, 1) for each arm
        self.alpha = np.ones(n_arms)
        self.beta = np.ones(n_arms)
        
    def choose_action(self):
        # Thompson sampling
        samples = [np.random.beta(self.alpha[i], self.beta[i]) 
                   for i in range(len(self.alpha))]
        return np.argmax(samples)
    
    def update(self, action, reward):
        # Bayesian update
        self.alpha[action] += reward
        self.beta[action] += (1 - reward)
```

**Key Result**: RW learning is equivalent to Bayesian inference in symmetric bandits under specific parameterizations.

## Model Recovery Validation

### Parameter Recovery
```python
def parameter_recovery(agent_class, true_params, n_trials=1000):
    """
    Validate that model parameters can be recovered from simulated data.
    """
    # Generate synthetic data with known parameters
    agent = agent_class(**true_params)
    data = simulate_behavior(agent, n_trials)
    
    # Fit model to synthetic data
    fitted_params = fit_model(agent_class, data)
    
    # Compare true vs. fitted
    return {k: (true_params[k], fitted_params[k]) 
            for k in true_params.keys()}
```

### Model Recovery
```python
def model_comparison(models, data):
    """
    Compare multiple agent models using information criteria.
    """
    results = {}
    for name, model_class in models.items():
        # Fit model
        fitted = fit_model(model_class, data)
        log_likelihood = fitted.log_likelihood
        n_params = len(fitted.params)
        
        # AIC
        aic = -2 * log_likelihood + 2 * n_params
        
        # BIC
        bic = -2 * log_likelihood + n_params * np.log(len(data))
        
        results[name] = {
            'log_likelihood': log_likelihood,
            'AIC': aic,
            'BIC': bic
        }
    
    return results
```

## Applications

### Cognitive Science
- Formal testing of cognitive theories
- Model-based analysis of decision-making
- Bridging computational and algorithmic levels

### Neuroscience
- Linking neural activity to computational models
- Understanding neural basis of decision-making
- Model-based fMRI/EEG analysis

### AI/Human-AI Interaction
- Evaluating AI agents against human behavior
- Designing human-like AI systems
- Understanding human-AI collaboration

### Clinical Psychology
- Computational phenotyping
- Psychiatric diagnosis support
- Treatment outcome prediction

## Pitfalls

### Model Selection
1. **Overfitting**: Complex agents may fit noise
2. **Identifiability**: Different parameters may produce similar behavior
3. **Model Misspecification**: True process not in model space

### Inference Challenges
1. **Local Minima**: Non-convex optimization landscapes
2. **Parameter Correlations**: Dependencies between parameters
3. **Individual Differences**: Group vs. individual-level inference

### Implementation Issues
1. **Numerical Stability**: Log-probability computations
2. **Convergence**: MCMC or optimization convergence
3. **Validation**: Need independent test data

## Related Skills
- reinforcement-learning-models
- bayesian-cognitive-modeling
- decision-theory-neuroscience
- model-based-fmri
- computational-psychiatry

## References

### Primary Source
- Ostwald, D., et al. (2026). On Agentic Behavioral Modeling. arXiv:2604.27894 [q-bio.NC].

### Key Background
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning.
- Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction.
- Daw, N. D. (2011). Trial-by-trial data analysis using computational models.

## Implementation Workflow

### Step 1: Define Task Structure
```python
task_spec = {
    'actions': ['left', 'right'],
    'observations': ['stimulus_left', 'stimulus_right'],
    'rewards': [0, 1],
    'trials': 100
}
```

### Step 2: Implement Agent
```python
class CustomAgent:
    def __init__(self, params):
        self.params = params
        
    def act(self, observation, history):
        # Compute action probabilities
        return action_probs
    
    def update(self, observation, action, reward):
        # Update internal state
        pass
```

### Step 3: Fit to Data
```python
from scipy.optimize import minimize

def negative_log_likelihood(params, agent_class, data):
    agent = agent_class(**params)
    nll = 0
    for trial in data:
        action_probs = agent.act(trial['obs'], trial['history'])
        nll -= np.log(action_probs[trial['action']])
        agent.update(trial['obs'], trial['action'], trial['reward'])
    return nll

result = minimize(negative_log_likelihood, 
                  x0=initial_params,
                  args=(CustomAgent, data))
```

### Step 4: Validate Model
```python
# Parameter recovery
recovery_results = parameter_recovery(CustomAgent, true_params)

# Model comparison
comparison = model_comparison({
    'CustomAgent': CustomAgent,
    'Baseline': RandomAgent
}, data)
```

## Keywords
agentic behavioral modeling, cognitive agents, decision theory, Rescorla-Wagner, Bayesian inference, psychometric function, reinforcement learning, model recovery, parameter estimation, computational cognitive science
