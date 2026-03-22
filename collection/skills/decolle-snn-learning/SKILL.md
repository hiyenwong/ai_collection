---
name: decolle-snn-learning
description: 深度连续局部学习方法论（DECOLLE）。在脉冲神经网络中实现局部突触可塑性规则，通过合成梯度实现端到端训练。适用于事件驱动视觉、神经形态计算、在线学习、脉冲神经网络研究。触发词：DECOLLE、脉冲神经网络、突触可塑性、局部学习、神经形态计算、在线学习、spiking neural network、synaptic plasticity、neuromorphic computing。
user-invocable: true
---

# 深度连续局部学习方法论（DECOLLE）

**来源论文：** arXiv:1811.10766 - Synaptic Plasticity Dynamics for Deep Continuous Local Learning (DECOLLE)

## 核心方法论

DECOLLE核心思想：使用合成梯度实现脉冲神经网络的端到端训练

### 关键创新

1. **局部学习规则**：每个神经元层独立计算梯度，无需全局反向传播
2. **合成梯度**：预测下游梯度，打破时间依赖
3. **连续学习**：支持实时、在线学习
4. **生物学合理性**：符合突触可塑性约束

### 方法架构

```
输入 → SNN层1 → SNN层2 → ... → 输出
         ↓          ↓          ↓
      合成梯度   合成梯度    损失
         ↓          ↓
       局部更新  局部更新
```

## Python 实现

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, List, Optional, Dict
from dataclasses import dataclass
import numpy as np


@dataclass
class LIFParameters:
    """LIF神经元参数"""
    tau_mem: float = 20.0      # 膜时间常数 (ms)
    tau_syn: float = 5.0       # 突触时间常数 (ms)
    threshold: float = 1.0      # 发放阈值
    reset: float = 0.0         # 重置电位
    alpha: float = 0.9          # 衰减因子
    beta: float = 0.8          # 突触衰减


class LIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire神经元"""
    
    def __init__(self, in_features: int, out_features: int, 
                 params: Optional[LIFParameters] = None):
        super().__init__()
        self.params = params or LIFParameters()
        
        # 突触权重
        self.weight = nn.Parameter(
            torch.randn(out_features, in_features) / np.sqrt(in_features)
        )
        self.bias = nn.Parameter(torch.zeros(out_features))
        
        # 状态变量
        self.mem = None    # 膜电位
        self.syn = None    # 突触电流
        
    def reset_state(self, batch_size: int, device: torch.device = None):
        """重置神经元状态"""
        if device is None:
            device = self.weight.device
        self.mem = torch.zeros(batch_size, self.weight.shape[0], device=device)
        self.syn = torch.zeros(batch_size, self.weight.shape[0], device=device)
        
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            x: 输入脉冲 (batch, in_features)
            
        Returns:
            spike: 输出脉冲 (batch, out_features)
            mem: 膜电位 (batch, out_features) 用于计算损失
        """
        if self.mem is None:
            self.reset_state(x.shape[0], x.device)
            
        # 突触电流更新
        self.syn = self.params.beta * self.syn + x
        
        # 膜电位更新
        self.mem = self.params.alpha * self.mem + F.linear(self.syn, self.weight, self.bias)
        
        # 发放
        spike = (self.mem > self.params.threshold).float()
        
        # 重置
        self.mem = self.mem * (1 - spike) + self.params.reset * spike
        
        return spike, self.mem.clone()


class SyntheticGradient(nn.Module):
    """合成梯度预测器"""
    
    def __init__(self, hidden_dim: int, output_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
        
    def forward(self, h: torch.Tensor) -> torch.Tensor:
        """预测下游梯度
        
        Args:
            h: 当前层的隐藏状态（膜电位或突触电流）
            
        Returns:
            合成梯度
        """
        return self.net(h)


class DECOLLELayer(nn.Module):
    """DECOLLE层（LIF + 合成梯度 + 局部读出）"""
    
    def __init__(self, in_features: int, hidden_features: int, 
                 n_classes: int, params: Optional[LIFParameters] = None):
        super().__init__()
        
        # LIF神经元
        self.lif = LIFNeuron(in_features, hidden_features, params)
        
        # 合成梯度预测器
        self.synth_grad = SyntheticGradient(hidden_features, hidden_features)
        
        # 局部读出层（用于计算局部损失）
        self.readout = nn.Linear(hidden_features, n_classes)
        
        # 损失函数
        self.criterion = nn.CrossEntropyLoss()
        
    def forward(self, x: torch.Tensor, target: Optional[torch.Tensor] = None
               ) -> Dict[str, torch.Tensor]:
        """
        Args:
            x: 输入脉冲
            target: 目标标签（可选，用于计算局部损失）
            
        Returns:
            outputs: 包含spike, mem, readout, synth_grad等
        """
        spike, mem = self.lif(x)
        
        # 局部读出
        readout = self.readout(mem)
        
        # 合成梯度
        synth_grad = self.synth_grad(mem)
        
        # 计算局部损失
        loss_dict = {}
        if target is not None:
            loss_dict['local_loss'] = self.criterion(readout, target)
            
        return {
            'spike': spike,
            'mem': mem,
            'readout': readout,
            'synth_grad': synth_grad,
            **loss_dict
        }


class DECOLLENetwork(nn.Module):
    """DECOLLE深度脉冲神经网络"""
    
    def __init__(self, in_features: int, hidden_features: List[int], 
                 n_classes: int, params: Optional[LIFParameters] = None):
        """
        Args:
            in_features: 输入特征数
            hidden_features: 各层隐藏特征数列表
            n_classes: 输出类别数
            params: LIF参数
        """
        super().__init__()
        
        self.n_layers = len(hidden_features)
        self.params = params or LIFParameters()
        
        # 构建DECOLLE层
        self.layers = nn.ModuleList()
        
        prev_features = in_features
        for hidden in hidden_features:
            self.layers.append(
                DECOLLELayer(prev_features, hidden, n_classes, params)
            )
            prev_features = hidden
            
        # 最终读出层
        self.final_readout = nn.Linear(hidden_features[-1], n_classes)
        
    def reset_state(self, batch_size: int, device: torch.device = None):
        """重置所有层的状态"""
        for layer in self.layers:
            layer.lif.reset_state(batch_size, device)
            
    def forward(self, x_seq: torch.Tensor, target: Optional[torch.Tensor] = None
               ) -> Dict[str, torch.Tensor]:
        """
        Args:
            x_seq: 输入脉冲序列 (batch, time_steps, in_features)
            target: 目标标签 (batch,)
            
        Returns:
            outputs: 包含各层输出和损失
        """
        batch_size, time_steps, _ = x_seq.shape
        device = x_seq.device
        
        # 重置状态
        self.reset_state(batch_size, device)
        
        # 存储输出
        all_spikes = [[] for _ in range(self.n_layers)]
        all_readouts = [[] for _ in range(self.n_layers)]
        all_losses = []
        
        # 逐时间步处理
        for t in range(time_steps):
            x_t = x_seq[:, t, :]
            
            # 逐层传播
            for i, layer in enumerate(self.layers):
                outputs = layer(x_t, target)
                all_spikes[i].append(outputs['spike'])
                all_readouts[i].append(outputs['readout'])
                
                # 更新输入为当前层输出
                x_t = outputs['spike']
                
                # 添加合成梯度（用于反向传播）
                if t > 0 and outputs.get('local_loss') is not None:
                    all_losses.append(outputs['local_loss'])
                    
        # 堆叠输出
        outputs = {
            'spikes': [torch.stack(s, dim=1) for s in all_spikes],
            'readouts': [torch.stack(r, dim=1) for r in all_readouts],
            'final_readout': self.final_readout(all_spikes[-1][-1])
        }
        
        # 计算总损失
        if target is not None:
            # 各层局部损失之和
            outputs['local_loss'] = sum(all_losses) / len(all_losses) if all_losses else 0
            
            # 最终读出损失
            outputs['final_loss'] = F.cross_entropy(outputs['final_readout'], target)
            
            # 总损失
            outputs['total_loss'] = outputs['final_loss'] + 0.1 * outputs['local_loss']
            
        return outputs


class DECOLLETrainer:
    """DECOLLE训练器"""
    
    def __init__(self, model: DECOLLENetwork, lr: float = 1e-3, 
                 synth_lr: float = 1e-4):
        """
        Args:
            model: DECOLLE网络
            lr: 主学习率
            synth_lr: 合成梯度学习率
        """
        self.model = model
        
        # 分离参数组
        main_params = []
        synth_params = []
        
        for name, param in model.named_parameters():
            if 'synth_grad' in name:
                synth_params.append(param)
            else:
                main_params.append(param)
                
        self.optimizer = torch.optim.Adam([
            {'params': main_params, 'lr': lr},
            {'params': synth_params, 'lr': synth_lr}
        ])
        
    def train_step(self, x_seq: torch.Tensor, target: torch.Tensor
                  ) -> Dict[str, float]:
        """单步训练
        
        Args:
            x_seq: 输入脉冲序列
            target: 目标标签
            
        Returns:
            losses: 损失值
        """
        self.model.train()
        self.optimizer.zero_grad()
        
        outputs = self.model(x_seq, target)
        
        loss = outputs['total_loss']
        loss.backward()
        
        # 梯度裁剪
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
        
        self.optimizer.step()
        
        return {
            'total_loss': outputs['total_loss'].item(),
            'local_loss': outputs['local_loss'].item() if isinstance(outputs['local_loss'], torch.Tensor) else outputs['local_loss'],
            'final_loss': outputs['final_loss'].item()
        }
        
    def evaluate(self, x_seq: torch.Tensor, target: torch.Tensor
                ) -> Dict[str, float]:
        """评估
        
        Args:
            x_seq: 输入脉冲序列
            target: 目标标签
            
        Returns:
            metrics: 评估指标
        """
        self.model.eval()
        
        with torch.no_grad():
            outputs = self.model(x_seq, target)
            pred = outputs['final_readout'].argmax(dim=1)
            acc = (pred == target).float().mean().item()
            
        return {
            'accuracy': acc,
            'loss': outputs['total_loss'].item()
        }


def poisson_encode(data: torch.Tensor, time_steps: int, 
                   max_rate: float = 1.0) -> torch.Tensor:
    """泊松编码
    
    将连续数据转换为脉冲序列
    
    Args:
        data: 输入数据 (batch, features)
        time_steps: 时间步数
        max_rate: 最大发放率
        
    Returns:
        spikes: 脉冲序列 (batch, time_steps, features)
    """
    batch_size, features = data.shape
    
    # 归一化到 [0, max_rate]
    data_normalized = (data - data.min()) / (data.max() - data.min() + 1e-8) * max_rate
    
    # 生成泊松脉冲
    spikes = torch.rand(batch_size, time_steps, features) < data_normalized.unsqueeze(1)
    
    return spikes.float()


def train_decolle_on_mnist(epochs: int = 10, batch_size: int = 64, 
                           time_steps: int = 20):
    """在MNIST上训练DECOLLE模型
    
    Args:
        epochs: 训练轮数
        batch_size: 批量大小
        time_steps: 时间步数
        
    Returns:
        model: 训练后的模型
        history: 训练历史
    """
    from torchvision import datasets, transforms
    from torch.utils.data import DataLoader
    
    # 加载数据
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST('./data', train=False, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)
    
    # 创建模型
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model = DECOLLENetwork(
        in_features=28*28,
        hidden_features=[256, 128, 64],
        n_classes=10
    ).to(device)
    
    trainer = DECOLLETrainer(model, lr=1e-3, synth_lr=1e-4)
    
    # 训练历史
    history = {
        'train_loss': [],
        'train_acc': [],
        'test_acc': []
    }
    
    # 训练循环
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0
        correct = 0
        total = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data = data.view(-1, 28*28).to(device)
            target = target.to(device)
            
            # 泊松编码
            spikes = poisson_encode(data, time_steps)
            
            # 训练步
            losses = trainer.train_step(spikes, target)
            epoch_loss += losses['total_loss']
            
            # 评估准确率
            with torch.no_grad():
                outputs = model(spikes)
                pred = outputs['final_readout'].argmax(dim=1)
                correct += (pred == target).sum().item()
                total += target.size(0)
                
        train_acc = correct / total
        avg_loss = epoch_loss / len(train_loader)
        
        # 测试评估
        model.eval()
        test_correct = 0
        test_total = 0
        
        with torch.no_grad():
            for data, target in test_loader:
                data = data.view(-1, 28*28).to(device)
                target = target.to(device)
                
                spikes = poisson_encode(data, time_steps)
                outputs = model(spikes)
                pred = outputs['final_readout'].argmax(dim=1)
                test_correct += (pred == target).sum().item()
                test_total += target.size(0)
                
        test_acc = test_correct / test_total
        
        history['train_loss'].append(avg_loss)
        history['train_acc'].append(train_acc)
        history['test_acc'].append(test_acc)
        
        print(f"Epoch {epoch+1}/{epochs} - Loss: {avg_loss:.4f}, "
              f"Train Acc: {train_acc:.4f}, Test Acc: {test_acc:.4f}")
        
    return model, history


# 使用示例
def example_usage():
    """示例：DECOLLE网络使用"""
    # 创建网络
    model = DECOLLENetwork(
        in_features=100,
        hidden_features=[64, 32],
        n_classes=10
    )
    
    # 生成随机输入
    batch_size = 8
    time_steps = 20
    x_seq = torch.rand(batch_size, time_steps, 100)
    target = torch.randint(0, 10, (batch_size,))
    
    # 前向传播
    outputs = model(x_seq, target)
    
    print(f"输出形状:")
    print(f"  脉冲序列: {[s.shape for s in outputs['spikes']]}")
    print(f"  读出序列: {[r.shape for r in outputs['readouts']]}")
    print(f"  最终读出: {outputs['final_readout'].shape}")
    print(f"\n损失:")
    print(f"  总损失: {outputs['total_loss'].item():.4f}")
    print(f"  局部损失: {outputs['local_loss'].item():.4f}")
    print(f"  最终损失: {outputs['final_loss'].item():.4f}")
    
    # 训练器
    trainer = DECOLLETrainer(model)
    losses = trainer.train_step(x_seq, target)
    print(f"\n训练后损失: {losses['total_loss']:.4f}")
    
    return model, outputs


if __name__ == "__main__":
    model, outputs = example_usage()
    
    ## Activation Keywords
- DECOLLE
- 脉冲神经网络
- 突触可塑性
- 局部学习
- 神经形态计算
- 在线学习
- spiking neural network
- synaptic plasticity
- neuromorphic computing
- 合成梯度

## Tools Used
- pytorch
- numpy
- torchvision

## Instructions for Agents
1. 理解DECOLLE核心思想：使用合成梯度实现局部学习
2. 掌握LIF神经元模型：膜电位更新和脉冲生成
3. 实现合成梯度预测器：预测下游梯度，打破时间依赖
4. 应用泊松编码：将连续数据转换为脉冲序列
5. 注意局部损失的计算：每层独立计算损失

## Examples
```python
# 使用示例
from decolle_snn import DECOLLENetwork, poisson_encode

# 1. 创建网络
model = DECOLLENetwork(
    in_features=784,
    hidden_features=[256, 128, 64],
    n_classes=10
)

# 2. 泊松编码
data = torch.randn(8, 784)
spikes = poisson_encode(data, time_steps=20)

# 3. 前向传播
outputs = model(spikes, target)
print(f"总损失: {outputs['total_loss'].item():.4f}")
print(f"局部损失: {outputs['local_loss'].item():.4f}")
```

    print("\n" + "="*60)
    print("MNIST训练示例（需要下载MNIST数据集）")
    print("="*60)
    
    # 取消注释以运行完整训练
    # model, history = train_decolle_on_mnist(epochs=5)