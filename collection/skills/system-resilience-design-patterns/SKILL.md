---
name: system-resilience-design-patterns
description: "System resilience and robustness design patterns - analyzing temporal dynamics, cascading failures, and recovery mechanisms in complex systems. Based on recent research in resilience engineering and fault tolerance."
tags: ["resilience", "robustness", "fault-tolerance", "distributed-systems", "cascading-failures"]
---

# System Resilience Design Patterns

**系统韧性与鲁棒性设计模式**

## 概述

本技能提供系统韧性工程的设计模式和最佳实践，涵盖故障分析、级联故障预防、恢复机制和鲁棒性评估。基于韧性工程学和容错计算的最新研究。

## 核心概念

### 韧性定义 (Resilience Definition)

韧性是系统在扰动下保持功能并从中恢复的能力。包含四个关键维度：

1. **抵抗 (Robustness)**: 承受扰动的能力
2. **适应 (Adaptability)**: 调整以应对变化的能力
3. **恢复 (Recovery)**: 从故障中恢复的能力
4. **演化 (Evolution)**: 从经验中学习的能力

## 设计模式

### 1. 故障检测与隔离 (Fault Detection and Isolation)

```python
class FaultDetector:
    """
    故障检测器
    
    使用多种检测机制识别系统故障。
    """
    
    def __init__(self):
        self.heartbeat_interval = 5  # 秒
        self.timeout_threshold = 15  # 秒
        self.error_threshold = 0.1   # 错误率阈值
    
    def detect(self, component):
        """检测组件是否故障"""
        checks = {
            'heartbeat': self._check_heartbeat(component),
            'timeout': self._check_timeout(component),
            'error_rate': self._check_error_rate(component),
            'health_endpoint': self._check_health_endpoint(component)
        }
        
        # 多数表决
        failed_checks = sum(1 for v in checks.values() if not v)
        return failed_checks >= 2
    
    def _check_heartbeat(self, component):
        """检查心跳"""
        last_beat = component.last_heartbeat
        return (time.time() - last_beat) < self.timeout_threshold
    
    def _check_timeout(self, component):
        """检查响应超时"""
        return component.response_time < self.timeout_threshold
    
    def _check_error_rate(self, component):
        """检查错误率"""
        return component.error_rate < self.error_threshold
    
    def _check_health_endpoint(self, component):
        """检查健康端点"""
        try:
            response = requests.get(f"{component.url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
```

### 2. 级联故障预防 (Cascading Failure Prevention)

```python
class CascadingFailurePreventer:
    """
    级联故障预防器
    
    防止单个组件故障扩散到整个系统。
    """
    
    def __init__(self):
        self.load_shedder = LoadShedder()
        self.rate_limiter = RateLimiter()
        self.backpressure = BackpressureController()
    
    def protect(self, request, priority='normal'):
        """
        保护系统免受级联故障影响
        
        Args:
            request: 传入请求
            priority: 请求优先级 (critical, high, normal, low)
        """
        # 1. 检查系统负载
        if self._is_overloaded():
            if not self.load_shedder.should_accept(priority):
                raise ServiceUnavailable("System overloaded, request shedded")
        
        # 2. 速率限制
        if not self.rate_limiter.allow(request):
            raise RateLimitExceeded("Rate limit exceeded")
        
        # 3. 背压控制
        self.backpressure.apply(request)
        
        try:
            return self._process(request)
        except Exception as e:
            self._handle_failure(e)
            raise
    
    def _is_overloaded(self):
        """检查系统是否过载"""
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        queue_depth = self._get_queue_depth()
        
        return (cpu_usage > 80 or 
                memory_usage > 85 or 
                queue_depth > 1000)


class LoadShedder:
    """负载削减器"""
    
    def __init__(self):
        self.shedding_thresholds = {
            'critical': 0.95,  # 即使高负载也接受
            'high': 0.80,
            'normal': 0.60,
            'low': 0.40
        }
    
    def should_accept(self, priority):
        """根据优先级决定是否接受请求"""
        load = self._get_system_load()
        threshold = self.shedding_thresholds.get(priority, 0.5)
        return load < threshold


class BackpressureController:
    """背压控制器"""
    
    def __init__(self):
        self.downstream_latency = {}
    
    def apply(self, request):
        """应用背压"""
        for service, latency in self.downstream_latency.items():
            if latency > self._get_threshold(service):
                # 减慢请求速率
                time.sleep(self._calculate_delay(latency))
```

### 3. 优雅降级 (Graceful Degradation)

```python
class GracefulDegradation:
    """
    优雅降级策略
    
    当系统资源不足时，逐步降低服务质量以保持核心功能可用。
    """
    
    def __init__(self):
        self.degradation_levels = [
            self._level_0_normal,      # 正常模式
            self._level_1_cache_only,  # 仅缓存模式
            self._level_2_static_only, # 静态内容模式
            self._level_3_core_only    # 仅核心功能
        ]
        self.current_level = 0
    
    def handle_request(self, request):
        """根据当前降级级别处理请求"""
        handler = self.degradation_levels[self.current_level]
        return handler(request)
    
    def _level_0_normal(self, request):
        """正常模式：完整功能"""
        return self._full_service(request)
    
    def _level_1_cache_only(self, request):
        """降级级别1：仅使用缓存"""
        cached = self.cache.get(request.key)
        if cached:
            return cached
        return {'error': 'Data temporarily unavailable', 'fallback': True}
    
    def _level_2_static_only(self, request):
        """降级级别2：仅提供静态内容"""
        return self._serve_static_fallback(request)
    
    def _level_3_core_only(self, request):
        """降级级别3：仅核心功能"""
        if not self._is_core_functionality(request):
            return {'error': 'Service temporarily limited to core functions'}
        return self._minimal_service(request)
    
    def increase_degradation(self):
        """增加降级级别"""
        if self.current_level < len(self.degradation_levels) - 1:
            self.current_level += 1
            logger.warning(f"Degradation level increased to {self.current_level}")
    
    def decrease_degradation(self):
        """降低降级级别（恢复）"""
        if self.current_level > 0:
            self.current_level -= 1
            logger.info(f"Degradation level decreased to {self.current_level}")
```

### 4. 自动恢复机制 (Self-Healing)

```python
class SelfHealingSystem:
    """
    自愈系统
    
    自动检测故障并执行恢复操作。
    """
    
    def __init__(self):
        self.fault_detector = FaultDetector()
        self.recovery_strategies = {
            'restart': RestartStrategy(),
            'reconfigure': ReconfigureStrategy(),
            'failover': FailoverStrategy(),
            'scale': ScaleStrategy()
        }
        self.recovery_history = []
    
    def monitor_and_heal(self):
        """监控并执行自愈"""
        components = self._get_all_components()
        
        for component in components:
            if self.fault_detector.detect(component):
                logger.error(f"Fault detected in {component.name}")
                self._heal(component)
    
    def _heal(self, component):
        """执行恢复"""
        # 选择恢复策略
        strategy = self._select_recovery_strategy(component)
        
        try:
            result = strategy.execute(component)
            self.recovery_history.append({
                'component': component.name,
                'strategy': strategy.name,
                'timestamp': time.time(),
                'success': result
            })
            return result
        except Exception as e:
            logger.error(f"Recovery failed: {e}")
            # 尝试备选策略
            return self._try_fallback_strategies(component)
    
    def _select_recovery_strategy(self, component):
        """选择最合适的恢复策略"""
        # 基于故障类型和历史选择策略
        if component.fault_type == 'crash':
            return self.recovery_strategies['restart']
        elif component.fault_type == 'performance':
            return self.recovery_strategies['scale']
        elif component.fault_type == 'configuration':
            return self.recovery_strategies['reconfigure']
        else:
            return self.recovery_strategies['failover']


class RestartStrategy:
    """重启恢复策略"""
    
    name = 'restart'
    
    def execute(self, component):
        """执行重启"""
        logger.info(f"Restarting {component.name}")
        component.stop()
        time.sleep(2)  # 等待清理
        component.start()
        return self._verify_recovery(component)
    
    def _verify_recovery(self, component):
        """验证恢复成功"""
        for _ in range(5):  # 最多尝试5次
            if component.is_healthy():
                return True
            time.sleep(1)
        return False
```

### 5. 混沌工程 (Chaos Engineering)

```python
class ChaosEngineering:
    """
    混沌工程框架
    
    通过主动注入故障来验证系统韧性。
    """
    
    def __init__(self):
        self.experiments = []
        self.safety_checks = []
    
    def define_experiment(self, name, hypothesis, fault_injection, rollback):
        """
        定义混沌实验
        
        Args:
            name: 实验名称
            hypothesis: 预期结果假设
            fault_injection: 故障注入函数
            rollback: 回滚函数
        """
        experiment = {
            'name': name,
            'hypothesis': hypothesis,
            'inject': fault_injection,
            'rollback': rollback,
            'status': 'defined'
        }
        self.experiments.append(experiment)
        return experiment
    
    def run_experiment(self, experiment):
        """执行混沌实验"""
        # 1. 安全检查
        if not self._run_safety_checks():
            raise SafetyCheckFailed("Safety checks failed, aborting experiment")
        
        # 2. 记录基线指标
        baseline = self._collect_metrics()
        
        try:
            # 3. 注入故障
            experiment['status'] = 'injecting'
            experiment['inject']()
            
            # 4. 观察系统行为
            time.sleep(experiment.get('duration', 60))
            
            # 5. 验证假设
            metrics = self._collect_metrics()
            result = self._validate_hypothesis(
                experiment['hypothesis'], 
                baseline, 
                metrics
            )
            
            experiment['result'] = result
            experiment['status'] = 'completed'
            
        except Exception as e:
            experiment['status'] = 'failed'
            experiment['error'] = str(e)
        finally:
            # 6. 回滚
            experiment['rollback']()
        
        return experiment
    
    def _run_safety_checks(self):
        """运行安全检查"""
        for check in self.safety_checks:
            if not check():
                return False
        return True
    
    def create_latency_injection(self, service, latency_ms, duration_sec):
        """创建延迟注入实验"""
        def inject():
            service.add_latency(latency_ms)
        
        def rollback():
            service.remove_latency()
        
        return self.define_experiment(
            name=f"latency_injection_{service.name}",
            hypothesis="System maintains 99th percentile latency < 500ms",
            fault_injection=inject,
            rollback=rollback
        )
    
    def create_failure_injection(self, service, failure_rate):
        """创建故障注入实验"""
        def inject():
            service.set_failure_rate(failure_rate)
        
        def rollback():
            service.set_failure_rate(0)
        
        return self.define_experiment(
            name=f"failure_injection_{service.name}",
            hypothesis="Circuit breaker opens within 10 seconds",
            fault_injection=inject,
            rollback=rollback
        )
```

## 韧性评估指标

### 关键指标 (Key Resilience Metrics)

```python
class ResilienceMetrics:
    """韧性指标收集器"""
    
    def __init__(self):
        self.metrics = {
            'mtbf': [],  # Mean Time Between Failures
            'mttr': [],  # Mean Time To Recovery
            'availability': [],
            'error_rate': [],
            'recovery_success_rate': []
        }
    
    def calculate_mtbf(self, failure_times):
        """计算平均故障间隔时间"""
        if len(failure_times) < 2:
            return float('inf')
        intervals = [failure_times[i+1] - failure_times[i] 
                     for i in range(len(failure_times)-1)]
        return sum(intervals) / len(intervals)
    
    def calculate_mttr(self, recovery_times):
        """计算平均恢复时间"""
        if not recovery_times:
            return 0
        return sum(recovery_times) / len(recovery_times)
    
    def calculate_availability(self, uptime, downtime):
        """计算可用性"""
        total = uptime + downtime
        if total == 0:
            return 1.0
        return uptime / total
    
    def get_resilience_score(self):
        """计算综合韧性评分"""
        scores = {
            'mtbf': min(self.metrics['mtbf'][-1] / 3600, 1.0),  # 归一化到小时
            'mttr': 1.0 - min(self.metrics['mttr'][-1] / 300, 1.0),  # 5分钟内恢复为满分
            'availability': self.metrics['availability'][-1],
            'recovery_rate': self.metrics['recovery_success_rate'][-1]
        }
        
        # 加权平均
        weights = {'mtbf': 0.2, 'mttr': 0.3, 'availability': 0.3, 'recovery_rate': 0.2}
        return sum(scores[k] * weights[k] for k in scores)
```

## 最佳实践

### 1. 设计原则

- **假设故障必然发生**: 设计时假设任何组件都可能故障
- **快速失败**: 快速检测故障，避免资源浪费
- **优雅降级**: 保留核心功能，逐步降低非关键服务
- **自动恢复**: 减少人工干预，提高恢复速度

### 2. 实施步骤

1. **识别关键路径**: 确定系统的关键功能路径
2. **定义 SLO**: 为每个服务设定服务级别目标
3. **实施监控**: 建立全面的监控和告警系统
4. **演练故障**: 定期进行混沌工程实验
5. **持续改进**: 基于实验结果优化系统

### 3. 常见陷阱

- **过度工程**: 不要为不可能发生的场景设计
- **单点故障**: 避免任何单点故障
- **级联依赖**: 减少服务间的深度依赖
- **监控盲区**: 确保所有组件都可观测

## 相关研究

1. "Resilience Engineering: Concepts and Precepts" - Hollnagel, Woods & Leveson
2. "Chaos Engineering: System Resiliency in Practice" - Basiri et al.
3. "Site Reliability Engineering" - Google
4. "Building Microservices" - Sam Newman

---

**创建时间**: 2025-01-12
**版本**: 1.0
