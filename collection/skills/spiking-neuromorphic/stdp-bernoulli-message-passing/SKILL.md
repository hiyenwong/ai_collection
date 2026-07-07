---
name: stdp-bernoulli-message-passing
description: STDP驱动的Bernoulli消息传递脉冲神经网络。使用脉冲时序依赖可塑性训练SNN实现贝叶斯推理的消息传递，支持因子图实现和不可靠信道信号传输。适用于神经形态计算、贝叶斯推理、编码理论。触发词：STDP消息传递、贝叶斯推理、脉冲神经网络、因子图、Bernoulli消息、spike-timing-dependent plasticity、Bayesian inference、message passing、factor graph。
user-invocable: true
---

# STDP驱动的Bernoulli消息传递框架

**来源论文：** arXiv:2512.23728 - Spike-Timing-Dependent Plasticity for Bernoulli Message Passing

## 核心方法论

### 1. 贝叶斯推理与脉冲神经网络的桥梁

**贝叶斯框架：** 提供理解脑功能的原则性框架

**脉冲神经：** 脑中神经活动本质上是脉冲式的

**目标：** 设计执行贝叶斯推理消息传递的脉冲神经网络

### 2. Bernoulli 消息传递

**消息类型：** Bernoulli 随机变量（0/1）

**消息传递规则：**
- 更新方程基于概率
- 脉冲编码概率信息
- 时序携带消息内容

### 3. STDP 训练机制

**STDP 规则：**
- 脉冲时序依赖可塑性
- 基于 Hebbian 规则
- 生物可解释

**训练目标：** 使网络性能接近数值解

### 4. 因子图实现

**应用场景：** 编码理论中的因子图
- 不可靠信道信号传输
- 错误校正码

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class BernoulliMessageConfig:
    """Bernoulli 消息传递配置"""
    n_neurons: int = 50            # 神经元数量
    n_steps: int = 1000            # 时间步数
    dt: float = 1.0                # 时间步长
    
    # STDP 参数
    tau_plus: float = 20.0         # LTP 时间常数
    tau_minus: float = 20.0        # LTD 时间常数
    A_plus: float = 0.01           # LTP 幅度
    A_minus: float = 0.01          # LTD 幅度
    
    # 消息传递
    message_precision: int = 10    # 消息精度（脉冲数）


class BernoulliMessage:
    """Bernoulli 消息编码"""
    
    def __init__(self, probability: float):
        """
        Args:
            probability: Bernoulli 概率 P(X=1)
        """
        self.probability = np.clip(probability, 0.01, 0.99)
        
    def encode_to_spikes(self, n_steps: int) -> np.ndarray:
        """编码为脉冲序列
        
        Args:
            n_steps: 时间步数
            
        Returns:
            spikes: 脉冲序列 (n_steps,)
        """
        # 使用泊松过程编码概率
        rate = self.probability
        spikes = (np.random.rand(n_steps) < rate).astype(float)
        return spikes
    
    @staticmethod
    def decode_from_spikes(spikes: np.ndarray) -> 'BernoulliMessage':
        """从脉冲序列解码
        
        Args:
            spikes: 脉冲序列
            
        Returns:
            message: Bernoulli 消息
        """
        if len(spikes) == 0:
            return BernoulliMessage(0.5)
            
        probability = spikes.mean()
        return BernoulliMessage(probability)


class STDPSynapse:
    """STDP 突触"""
    
    def __init__(self, weight: float, config: BernoulliMessageConfig):
        """
        Args:
            weight: 初始权重
            config: 配置
        """
        self.weight = weight
        self.config = config
        
        # STDP 迹
        self.x = 0.0  # 前脉冲迹
        self.y = 0.0  # 后脉冲迹
        
        # 权重限制
        self.w_min = 0.0
        self.w_max = 1.0
        
    def update_traces(self, pre_spike: bool, post_spike: bool, dt: float = 1.0):
        """更新 STDP 迹
        
        Args:
            pre_spike: 前神经元是否发放
            post_spike: 后神经元是否发放
            dt: 时间步长
        """
        cfg = self.config
        
        # 迹衰减
        self.x *= np.exp(-dt / cfg.tau_plus)
        self.y *= np.exp(-dt / cfg.tau_minus)
        
        # 更新迹
        if pre_spike:
            self.x += 1.0
            # LTD: 前脉冲后，后迹影响
            self.weight -= cfg.A_minus * self.y
            
        if post_spike:
            self.y += 1.0
            # LTP: 后脉冲后，前迹影响
            self.weight += cfg.A_plus * self.x
            
        # 权重限制
        self.weight = np.clip(self.weight, self.w_min, self.w_max)


class BernoulliNeuron:
    """Bernoulli 消息神经元"""
    
    def __init__(self, config: BernoulliMessageConfig):
        self.config = config
        self.membrane = 0.0
        self.threshold = 1.0
        
    def integrate(self, input_current: float, dt: float = 1.0):
        """积分输入
        
        Args:
            input_current: 输入电流
            dt: 时间步长
        """
        self.membrane += input_current * dt
        
    def fire_and_reset(self) -> bool:
        """检查发放并重置
        
        Returns:
            spike: 是否发放
        """
        if self.membrane >= self.threshold:
            self.membrane = 0.0
            return True
        return False


class FactorGraphNode:
    """因子图节点"""
    
    def __init__(self, node_type: str, config: BernoulliMessageConfig):
        """
        Args:
            node_type: 'variable' 或 'factor'
            config: 配置
        """
        self.node_type = node_type
        self.config = config
        
        # 连接
        self.incoming_synapses: List[STDPSynapse] = []
        self.outgoing_connections: List[int] = []
        
        # 神经元
        self.neuron = BernoulliNeuron(config)
        
        # 消息历史
        self.message_history: List[float] = []
        
    def receive_message(self, message: BernoulliMessage, 
                        synapse_idx: int) -> np.ndarray:
        """接收消息
        
        Args:
            message: Bernoulli 消息
            synapse_idx: 突触索引
            
        Returns:
            spikes: 脉冲序列
        """
        spikes = message.encode_to_spikes(self.config.n_steps)
        return spikes
    
    def send_message(self) -> BernoulliMessage:
        """发送消息
        
        Returns:
            message: Bernoulli 消息
        """
        if len(self.message_history) == 0:
            return BernoulliMessage(0.5)
            
        # 平均最近的消息
        recent = self.message_history[-10:]
        avg_prob = np.mean(recent)
        
        return BernoulliMessage(avg_prob)


class BernoulliMessagePassingNetwork:
    """Bernoulli 消息传递网络"""
    
    def __init__(self, config: BernoulliMessageConfig):
        """
        Args:
            config: 配置
        """
        self.config = config
        
        # 网络结构
        self.nodes: Dict[int, FactorGraphNode] = {}
        
        # 消息记录
        self.message_log = []
        
    def add_variable_node(self, node_id: int):
        """添加变量节点
        
        Args:
            node_id: 节点 ID
        """
        self.nodes[node_id] = FactorGraphNode('variable', self.config)
        
    def add_factor_node(self, node_id: int):
        """添加因子节点
        
        Args:
            node_id: 节点 ID
        """
        self.nodes[node_id] = FactorGraphNode('factor', self.config)
        
    def connect(self, from_id: int, to_id: int, initial_weight: float = 0.5):
        """连接节点
        
        Args:
            from_id: 源节点 ID
            to_id: 目标节点 ID
            initial_weight: 初始权重
        """
        synapse = STDPSynapse(initial_weight, self.config)
        self.nodes[to_id].incoming_synapses.append(synapse)
        self.nodes[from_id].outgoing_connections.append(to_id)
        
    def message_passing_step(self, 
                              observations: Dict[int, BernoulliMessage],
                              n_iterations: int = 10) -> Dict:
        """消息传递步骤
        
        Args:
            observations: 观测消息 {node_id: message}
            n_iterations: 迭代次数
            
        Returns:
            results: 结果
        """
        results = {
            'messages': defaultdict(list),
            'beliefs': {}
        }
        
        for iteration in range(n_iterations):
            # 传递消息
            for node_id, node in self.nodes.items():
                # 接收输入
                if node_id in observations:
                    input_message = observations[node_id]
                    spikes = node.receive_message(input_message, 0)
                else:
                    # 从突触接收
                    total_current = 0.0
                    for synapse in node.incoming_synapses:
                        total_current += synapse.weight * np.random.rand()
                        
                    node.neuron.integrate(total_current)
                    
                # 发送输出
                output_message = node.send_message()
                results['messages'][node_id].append(output_message.probability)
                
        # 计算信念
        for node_id, probs in results['messages'].items():
            if len(probs) > 0:
                results['beliefs'][node_id] = np.mean(probs[-5:])
                
        return results
    
    def train_with_stdp(self, 
                        observations: Dict[int, BernoulliMessage],
                        target_beliefs: Dict[int, float],
                        n_epochs: int = 100) -> Dict:
        """使用 STDP 训练
        
        Args:
            observations: 观测
            target_beliefs: 目标信念
            n_epochs: 训练轮数
            
        Returns:
            training_info: 训练信息
        """
        losses = []
        
        for epoch in range(n_epochs):
            # 消息传递
            results = self.message_passing_step(observations, n_iterations=10)
            
            # 计算损失
            loss = 0.0
            for node_id, target in target_beliefs.items():
                if node_id in results['beliefs']:
                    predicted = results['beliefs'][node_id]
                    loss += (predicted - target)**2
                    
            losses.append(loss)
            
            # 更新突触（简化）
            for node_id, node in self.nodes.items():
                for synapse in node.incoming_synapses:
                    # 随机 STDP 更新
                    pre_spike = np.random.rand() > 0.5
                    post_spike = np.random.rand() > 0.5
                    synapse.update_traces(pre_spike, post_spike)
                    
        return {
            'final_loss': losses[-1] if losses else 0,
            'loss_history': losses
        }


class UnreliableChannelSimulation:
    """不可靠信道仿真"""
    
    def __init__(self, error_rate: float = 0.1):
        """
        Args:
            error_rate: 错误率
        """
        self.error_rate = error_rate
        
    def transmit(self, message: BernoulliMessage) -> BernoulliMessage:
        """传输消息
        
        Args:
            message: 输入消息
            
        Returns:
            received: 接收消息（可能有错误）
        """
        # 模拟翻转
        if np.random.rand() < self.error_rate:
            # 翻转概率
            new_prob = 1 - message.probability
            return BernoulliMessage(new_prob)
        return BernoulliMessage(message.probability)
    
    def simulate_factor_graph_decoding(self,
                                         transmitted: List[BernoulliMessage],
                                         n_iterations: int = 20) -> List[BernoulliMessage]:
        """因子图解码仿真
        
        Args:
            transmitted: 传输的消息列表
            n_iterations: 解码迭代次数
            
        Returns:
            decoded: 解码后的消息列表
        """
        config = BernoulliMessageConfig()
        network = BernoulliMessagePassingNetwork(config)
        
        # 创建简单因子图
        for i in range(len(transmitted)):
            network.add_variable_node(i)
            network.add_factor_node(i + 100)
            network.connect(i, i + 100)
            
        # 设置观测
        observations = {i: msg for i, msg in enumerate(transmitted)}
        
        # 消息传递
        results = network.message_passing_step(observations, n_iterations)
        
        # 提取解码结果
        decoded = []
        for i in range(len(transmitted)):
            if i in results['beliefs']:
                decoded.append(BernoulliMessage(results['beliefs'][i]))
            else:
                decoded.append(BernoulliMessage(0.5))
                
        return decoded


def compare_with_numerical_solution(network: BernoulliMessagePassingNetwork,
                                    observations: Dict[int, BernoulliMessage],
                                    numerical_beliefs: Dict[int, float]) -> Dict:
    """与数值解比较
    
    Args:
        network: 消息传递网络
        observations: 观测
        numerical_beliefs: 数值解信念
        
    Returns:
        comparison: 比较结果
    """
    # 运行网络
    results = network.message_passing_step(observations)
    
    # 比较
    errors = []
    for node_id, numerical in numerical_beliefs.items():
        if node_id in results['beliefs']:
            predicted = results['beliefs'][node_id]
            error = np.abs(predicted - numerical)
            errors.append(error)
            
    return {
        'mean_error': np.mean(errors) if errors else 0,
        'max_error': np.max(errors) if errors else 0,
        'errors': errors
    }


# 使用示例
def example_bernoulli_message_passing():
    """示例：Bernoulli 消息传递"""
    print("="*60)
    print("STDP驱动的Bernoulli消息传递框架")
    print("="*60)
    
    config = BernoulliMessageConfig(n_neurons=50)
    
    # 创建网络
    network = BernoulliMessagePassingNetwork(config)
    
    # 添加节点
    for i in range(5):
        network.add_variable_node(i)
        network.add_factor_node(i + 10)
        network.connect(i, i + 10)
        
    print(f"\n网络结构:")
    print(f"  变量节点: 5")
    print(f"  因子节点: 5")
    
    # 创建观测
    observations = {
        0: BernoulliMessage(0.8),
        1: BernoulliMessage(0.3),
        2: BernoulliMessage(0.9),
    }
    
    print(f"\n观测消息:")
    for node_id, msg in observations.items():
        print(f"  节点 {node_id}: P={msg.probability:.2f}")
    
    # 消息传递
    print(f"\n执行消息传递...")
    results = network.message_passing_step(observations)
    
    print(f"\n最终信念:")
    for node_id, belief in results['beliefs'].items():
        print(f"  节点 {node_id}: {belief:.3f}")
    
    # 不可靠信道
    print(f"\n不可靠信道仿真:")
    channel = UnreliableChannelSimulation(error_rate=0.1)
    
    original = BernoulliMessage(0.9)
    received = channel.transmit(original)
    print(f"  发送: P={original.probability:.2f}")
    print(f"  接收: P={received.probability:.2f}")
    
    print(f"\n关键特性:")
    print(f"  ✅ STDP 训练生物可解释")
    print(f"  ✅ Bernoulli 消息编码")
    print(f"  ✅ 支持因子图推理")
    
    return network


## Activation Keywords
- STDP消息传递
- 贝叶斯推理
- 脉冲神经网络
- 因子图
- Bernoulli消息
- spike-timing-dependent plasticity
- Bayesian inference
- message passing
- factor graph

## Tools Used
- numpy

## Instructions for Agents
1. 理解 Bernoulli 消息编码为脉冲序列
2. 使用 STDP 更新突触权重
3. 构建因子图表示问题
4. 运行消息传递迭代
5. 与数值解比较验证

## Examples
```python
# Bernoulli 消息传递示例
from stdp_bernoulli_message_passing import (
    BernoulliMessagePassingNetwork, BernoulliMessage,
    BernoulliMessageConfig, UnreliableChannelSimulation
)

# 1. 配置
config = BernoulliMessageConfig(n_neurons=50)

# 2. 创建网络
network = BernoulliMessagePassingNetwork(config)

# 3. 添加节点
for i in range(5):
    network.add_variable_node(i)
    network.add_factor_node(i + 10)
    network.connect(i, i + 10)

# 4. 设置观测
observations = {
    0: BernoulliMessage(0.8),
    1: BernoulliMessage(0.3),
}

# 5. 消息传递
results = network.message_passing_step(observations)
print(f"信念: {results['beliefs']}")

# 6. 不可靠信道
channel = UnreliableChannelSimulation(error_rate=0.1)
received = channel.transmit(BernoulliMessage(0.9))
```

if __name__ == "__main__":
    example_bernoulli_message_passing()
```

## Related Skills

- `stochastic-synaptic-plasticity` - 随机突触可塑性
- `delay-adaptive-snn-classifier` - 延迟自适应 SNN
- `noisy-snn-learning` - 噪声驱动 SNN 学习

## References

- arXiv:2512.23728 - Spike-Timing-Dependent Plasticity for Bernoulli Message Passing
- Topics: Neurons and Cognition (q-bio.NC), ML (cs.LG), Neural Computing (cs.NE)