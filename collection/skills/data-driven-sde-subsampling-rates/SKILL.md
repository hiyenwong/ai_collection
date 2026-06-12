---
name: data-driven-sde-subsampling-rates
description: "Data-driven methodology for selecting optimal subsampling rates in SDE parameter estimation when data-model compatibility scales are unknown."
---

# Data-Driven SDE Subsampling Rates

## Description
Data-driven methodology for selecting optimal subsampling rates when estimating diffusion parameters for stochastic differential equation (SDE) models. Addresses the problem where data and model are compatible only on specific scales that have yet to be determined. Introduces a simple and efficient method for selecting suitable rates at which given time series data should be subsampled for consistent parameter estimation.

## Activation Keywords
- SDE parameter estimation
- 随机微分方程参数估计
- subsampling rate selection
- diffusion parameter estimation
- data-driven subsampling
- stochastic differential equation
- SDE 数据驱动子采样
- diffusion model scale selection
- 扩散模型尺度选择

## Tools Used
- terminal: Run Python scripts for SDE simulation and parameter estimation
- read_file: Read time series data
- write_file: Save estimation results
- patch: Modify estimation scripts

## Usage Patterns

### Pattern 1: Unknown Scale SDE Estimation
Given a time series believed to follow an SDE, determine the appropriate subsampling rate for consistent parameter estimation without prior knowledge of compatible scales.

### Pattern 2: Multi-Scale Data Analysis
When data exhibits behavior at multiple time scales, identify which scales are compatible with the assumed SDE model and select optimal subsampling rates.

### Pattern 3: Model-Data Compatibility Testing
Test whether a given SDE model is compatible with observed data at various subsampling rates.

## Instructions for Agents

### Step 1: Data Preprocessing
- Load the time series data
- Compute basic statistics (mean, variance, autocorrelation)
- Identify potential issues (missing data, outliers)

### Step 2: Subsampling Rate Selection
- Apply the data-driven method from the paper
- Compute the compatibility metric across different subsampling rates
- Identify the rate(s) where the metric indicates model-data compatibility

### Step 3: Parameter Estimation
- Subsample the data at the selected rate
- Apply standard SDE parameter estimation (e.g., MLE, method of moments)
- Validate the estimated parameters

### Step 4: Sensitivity Analysis
- Test estimation robustness across nearby subsampling rates
- Report confidence intervals for the estimated parameters

## Error Handling
- If no compatible rate is found, consider model misspecification
- For short time series, use larger subsampling windows
- If estimation is unstable, apply regularization or Bayesian methods

## Resources
- arXiv: 2606.13615 - "Data-driven subsampling rates for diffusion parameter estimation of SDEs"
- Categories: math.PR;stat.ME
- Key concepts: Stochastic differential equations, parameter estimation, subsampling, diffusion processes, scale compatibility

## Related Skills
- carleman-linearization-ode-solver
- sde-estimation (if exists)
