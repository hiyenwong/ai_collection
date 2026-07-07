---
name: cmms-edge-cluster-benchmark
description: "Continuous Multi-Mode Scheduling（CMMS）基准测试平台用于边缘集群调度算法公平比较。统一控制器接口、闭环负载驱动、双指标SLO评分（原始SLO vs 稳态SLO），揭示控制器排名的配置依赖性和切换成本。Activation: edge cluster scheduling, heterogeneous scheduling, SLO benchmark, CMMS, RL scheduling, adaptive benchmark, edge-cloud continuum."
category: systems-engineering
metadata:
  arxiv_id: "2606.12343"
  authors: "Zihang Wang, Boris Sedlak, Juan Luis Herrera, Schahram Dustdar"
  published_date: "2026-06-10"
---

## Context

现代AI工作负载部署在边缘-云端续体的异构层级上，需满足多维SLO（延迟、吞吐、输出质量）。调度器为每个任务选择目标节点和处理模式（如全精度或低精度推理）。传统调度算法比较方法存在三大缺陷：（1）各控制器单独评估；（2）单一负载模式；（3）无决策开销报告。CMMS基准平台填补这些空白。

## Core Methodology

### 1. CMMS问题定义

**调度决策空间**：
- 目标节点选择：$n \in \{1, ..., N\}$（异构节点池）
- 处理模式选择：$m \in \{full, reduced\}$（精度模式）

**决策向量**：$d = (n, m)$，组合空间大小 $|D| = N \times M$

**SLO约束**：
- 延迟：$\tau(d) \leq \tau_{max}$
- 吞吐：$T(d) \geq T_{min}$
- 质量：$Q(m) \geq Q_{min}$

### 2. 统一控制器接口

**接口规范**：
```python
class CMMSController:
    def decide(self, state: ClusterState) -> Decision:
        """
        输入：集群状态（负载、队列长度、节点状态）
        输出：调度决策（节点+模式）
        """
        pass
    
    def overhead(self) -> float:
        """
        返回：单次决策计算开销（毫秒）
        """
        pass
```

**状态表示**：
- $L(t)$：当前负载水平
- $Q_i(t)$：节点 $i$ 队列长度
- $S_i(t)$：节点 $i$ 服务状态（可用/过载）
- $H_i(t)$：节点 $i$ 硬件能力（CPU/GPU/FPGA）

### 3. 闭环负载驱动

**负载模式**：
1. **Constant**：恒定负载率 $\lambda$
2. **Burst**：突发负载 $\lambda(t) = \bar{\lambda} + \Delta \sin(2\pi t / T)$
3. **Step**：阶跃负载 $\lambda(t) = \lambda_0 \rightarrow \lambda_1$（模拟工作日高峰）
4. **Sine**：正弦变化 $\lambda(t) = A \sin(\omega t)$
5. **Random Walk**：随机游走 $\lambda(t+1) = \lambda(t) + \epsilon$

**闭环反馈**：
```python
# 负载驱动器
class WorkloadDriver:
    def generate_load(self, pattern, t):
        if pattern == 'burst':
            return self.base_load + self.burst_amp * np.sin(2*np.pi*t/self.period)
        elif pattern == 'step':
            return self.step_high if t > self.step_time else self.step_low
        ...
    
    def observe_slo(self, decisions, outcomes):
        # 反馈：调整负载驱动参数
        slo_violation_rate = self.compute_violation(outcomes)
        self.adjust_load(slo_violation_rate)
```

### 4. 双指标SLO评分

**指标1：原始SLO（Raw SLO）**
$$SLO_{raw} = \frac{1}{T} \sum_{t=1}^T \mathbb{1}[C_t(d_t) \leq C_{max}]$$

其中 $C_t$ 为时刻 $t$ 的SLO成本。

**指标2：稳态SLO（Steady-State SLO）**
$$SLO_{ss} = \frac{1}{T - T_{switch}} \sum_{t=T_{switch}+1}^T \mathbb{1}[C_t \leq C_{max}]$$

排除切换瞬态（$T_{switch}$ 为切换窗口）。

**切换成本暴露**：
$$Cost_{switch} = SLO_{raw} - SLO_{ss}$$

反映控制器适应负载变化的过渡损失。

### 5. 实验设计矩阵

**变量维度**：
1. **集群配置**（5种）：单节点、同构集群、异构集群、分级集群、混合集群
2. **负载模式**（5种）：恒定、突发、阶跃、正弦、随机游走
3. **负载强度**（2种）：轻负载（$\lambda = 0.3\lambda_{max}$）、重负载（$\lambda = 0.8\lambda_{max}$）
4. **控制器类型**（6种）：Rule-based、Greedy、Round-robin、RL（DQN/PPO）、启发式、混合策略

**总实验数**：$5 \times 5 \times 2 \times 6 = 300$ episodes（实际424 episodes含重复验证）

### 6. 控制器排名分析

**核心发现**：
1. **配置依赖性**：同一控制器在不同配置下排名变化显著
2. **负载敏感性**：RL控制器轻负载下最优，重负载下降29个百分点
3. **开销差异**：RL开销 $\approx 500\times$ 启发式开销
4. **切换成本**：双指标分离暴露单指标掩盖的过渡损失

## Implementation Steps

### Step 1: 基准平台架构

```python
class CMMSBenchmark:
    def __init__(self, config):
        self.cluster = HeterogeneousCluster(config['nodes'])
        self.driver = WorkloadDriver(config['workload'])
        self.evaluator = SLOEvaluator(config['slo'])
        self.controllers = {}  # 统一接口注册
        
    def register_controller(self, name, controller):
        assert hasattr(controller, 'decide')
        assert hasattr(controller, 'overhead')
        self.controllers[name] = controller
```

### Step 2: 异构集群建模

```python
class HeterogeneousCluster:
    def __init__(self, node_configs):
        self.nodes = []
        for config in node_configs:
            node = Node(
                hardware=config['hw_type'],  # CPU/GPU/Edge_TPU
                capacity=config['capacity'],
                modes=config['modes']  # [full, reduced]
            )
            self.nodes.append(node)
    
    def get_state(self):
        return ClusterState(
            loads=[n.load for n in self.nodes],
            queues=[n.queue_length for n in self.nodes],
            capabilities=[n.hw_capability for n in self.nodes]
        )
```

### Step 3: 调度决策执行

```python
def execute_episode(cluster, driver, controller, T_episode=1000):
    outcomes = []
    overheads = []
    
    for t in range(T_episode):
        # 生成负载
        load = driver.generate_load(t)
        cluster.inject_load(load)
        
        # 调度决策
        state = cluster.get_state()
        decision = controller.decide(state)
        overhead = controller.overhead()
        
        # 执行任务
        outcome = cluster.process(decision)
        
        outcomes.append(outcome)
        overheads.append(overhead)
    
    return outcomes, overheads
```

### Step 4: 双指标SLO计算

```python
class SLOEvaluator:
    def compute_raw_slo(self, outcomes, slo_threshold):
        compliance = [1 if o['cost'] <= slo_threshold else 0 for o in outcomes]
        return np.mean(compliance)
    
    def compute_steady_state_slo(self, outcomes, slo_threshold, switch_window=50):
        # 排除切换瞬态
        steady_outcomes = outcomes[switch_window:]
        compliance = [1 if o['cost'] <= slo_threshold else 0 for o in steady_outcomes]
        return np.mean(compliance)
    
    def compute_switch_cost(self, raw_slo, steady_slo):
        return raw_slo - steady_slo
```

### Step 5: 控制器比较分析

```python
def compare_controllers(benchmark, controllers, configs, loads):
    results = {}
    
    for config in configs:
        for load in loads:
            for name, ctrl in controllers.items():
                outcomes, overheads = execute_episode(
                    benchmark.cluster, 
                    benchmark.driver, 
                    ctrl
                )
                
                raw_slo = benchmark.evaluator.compute_raw_slo(outcomes)
                ss_slo = benchmark.evaluator.compute_steady_state_slo(outcomes)
                avg_overhead = np.mean(overheads)
                
                results[(config, load, name)] = {
                    'raw_slo': raw_slo,
                    'steady_slo': ss_slo,
                    'switch_cost': raw_slo - ss_slo,
                    'overhead': avg_overhead
                }
    
    return results
```

## Pitfalls

### 1. 单一负载模式误导
- **症状**：控制器在单一负载下表现优异，实际部署失败
- **诊断**：检查负载模式覆盖率（需≥3种模式）
- **修复**：扩展负载模式库（增加突发、阶跃、正弦）

### 2. 决策开销忽略
- **症状**：RL控制器SLO达标但实际响应慢
- **诊断**：对比 overhead() 返回值（>10ms警告）
- **修复**：限制决策时间窗口（<1% SLO延迟预算）

### 3. 切换瞬态掩盖
- **症状**：单指标SLO显示稳定，实际切换时大幅违规
- **诊断**：比较 Raw vs Steady-State SLO差异
- **修复**：增加切换窗口 $T_{switch}$ 评估（默认50步）

### 4. 配置固定性偏差
- **症状**：最优控制器仅在特定配置下有效
- **诊断**：交叉验证多个集群配置（≥5种）
- **修复**：自适应控制器选择（根据配置切换策略）

### 5. 异构节点建模不准确
- **症状**：仿真结果与实测偏差大
- **诊断**：检查硬件能力向量 $H_i$ 测量精度
- **修复**：实测标定（使用真实基准任务）

## Verification

### 实验完整性验证
```python
def verify_experiment_coverage(results):
    # 检查配置覆盖
    configs_covered = set([k[0] for k in results.keys()])
    loads_covered = set([k[1] for k in results.keys()])
    controllers_covered = set([k[2] for k in results.keys()])
    
    assert len(configs_covered) >= 5, "Insufficient config coverage"
    assert len(loads_covered) >= 2, "Insufficient load coverage"
    assert len(controllers_covered) >= 6, "Insufficient controller coverage"
    
    return True
```

### 排名稳定性检验
```python
def verify_ranking_stability(results, threshold=0.05):
    # Kruskal-Wallis检验：排名是否统计显著
    from scipy.stats import kruskal
    
    slo_scores = [r['raw_slo'] for r in results.values()]
    H, p = kruskal(*slo_scores)
    
    if p < threshold:
        return True, f"Ranking significant (H={H}, p={p})"
    return False, f"Ranking not significant (H={H}, p={p})"
```

### 开销一致性验证
```python
def verify_overhead_consistency(controller, N_trials=100):
    overheads = []
    for _ in range(N_trials):
        overhead = controller.overhead()
        overheads.append(overhead)
    
    # 检验稳定性（方差<10%均值）
    if np.std(overheads) / np.mean(overheads) < 0.1:
        return True, overheads
    return False, overheads
```

## Activation

**触发词**：edge cluster scheduling, heterogeneous scheduling, SLO benchmark, CMMS, continuous multi-mode scheduling, RL scheduling, adaptive benchmark, edge-cloud continuum, scheduling algorithm comparison, dual-metric evaluation, switch cost analysis

**应用场景**：
- 边缘-云端续体调度算法评估
- 异构集群调度器设计与优化
- RL调度算法vs启发式算法比较
- 多维SLO约束调度系统测试
- 调度算法基准测试平台搭建