---
name: psi-shared-state-architecture-v2
description: "PSI (Persistent Shared Interface): Shared-state architecture for coherent AI-generated instruments in personal AI agents. Transforms isolated AI-generated modules into persistent, connected, chat-complementary artifacts through a shared personal-context bus. Activation: PSI, shared state, personal AI, AI-generated instruments, coherent computing, context bus."
category: systems-engineering
---

# PSI: Shared-State Architecture for Coherent AI-Generated Instruments

基于论文 "PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents" (Wang et al., 2026) 的方法论技能。

## 核心思想

个人AI工具现在可以从自然语言请求生成，但它们在创建后往往保持孤立。PSI是一个**共享状态架构**，将独立生成的模块转变为**连贯的工具(instruments)**：持久、连接、与聊天互补的工件，可通过GUI和通用聊天代理访问。

通过将当前状态和写回功能发布到共享的个人上下文总线，模块实现跨模块推理和跨接口的同步操作。

## 核心概念

### Instrument（工具）定义

借用Beaudouin-Lafon的乐器交互模型，PSI定义**工具**为具有以下特性的生成工件：

1. **Persistent（持久）**：无需重新生成即可保持可用
2. **Connected（连接）**：将状态发布到共享个人上下文层，可暴露写回功能
3. **Chat-Complementary（聊天互补）**：支持一瞥式监控，同时聊天处理综合、歧义消解和有状态操作

### Module（模块）定义

**模块**是工具背后的完整软件包，包括：
- GUI界面
- 数据提供者(provider)
- 可选服务

## 问题背景

### 个人数据碎片化问题

人们越来越依赖个人数字工具生态系统：
- 健康应用（记录锻炼和睡眠）
- 停车服务（跟踪时间和支付）
- 日历、位置轨迹
- 可穿戴传感器
- 日常仪表板

**核心问题**：简单情境问题如"我现在的心率是否太高？"可能需要结合：
- 最近的锻炼活动
- 当前运动状态
- 睡眠质量
- 情境信号（是否正在走回即将过期的停车位）

困难不在于单个信号不可用，而在于这些信号分散在应用、服务和接口之间。

### 现有系统局限性

| 系统 | 对话AI | 持久GUI | 结构化上下文 | 跨模块综合 | 应用级写回 |
|------|--------|---------|--------------|------------|------------|
| ChatGPT/Claude | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| Siri/Google助手 | ✅ | ❌ | ⚠️ | ❌ | ❌ |
| Shortcuts/IFTTT | ❌ | ❌ | ❌ | ⚠️ | ⚠️ |
| Home Assistant | ⚠️ | ❌ | ✅ | ✅ | ✅ |
| v0/Lovable | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| M365 Copilot | ✅ | ❌ | ⚠️ | ✅ | ⚠️ |
| **PSI** | ✅ | ✅ | ✅ | ✅ | ✅ |

## PSI架构

### 系统概览

```
┌─────────────────────────────────────────────────────────────────┐
│                        PSI Architecture                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐    Generate      ┌─────────────────────────┐  │
│  │  User Intent │ ───────────────→ │   AI Generation Engine  │  │
│  │  (Natural    │                  │   (e.g., Claude, GPT)   │  │
│  │   Language)  │                  └───────────┬─────────────┘  │
│  └──────────────┘                              │                │
│                                                ▼                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Shared Personal-Context Bus                  │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │  │
│  │  │   BoBo      │  │   Health    │  │     Parking     │  │  │
│  │  │  (Timeline) │  │  (Workouts) │  │    (Status)     │  │  │
│  │  │             │  │             │  │                 │  │  │
│  │  │ State:      │  │ State:      │  │ State:          │  │  │
│  │  │ - motion    │  │ - heart_rate│  │ - location      │  │  │
│  │  │ - steps     │  │ - calories  │  │ - time_remaining│  │  │
│  │  │ - sleep     │  │ - duration  │  │ - cost          │  │  │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│              ┌───────────────┼───────────────┐                  │
│              ▼               ▼               ▼                  │
│  ┌─────────────────┐ ┌──────────────┐ ┌──────────────────┐     │
│  │   Persistent    │ │    Facai     │ │   Write-Back     │     │
│  │      GUIs       │ │  (Chat Agent)│ │   Affordances    │     │
│  │                 │ │              │ │                  │     │
│  │ - Glanceable    │ │ Cross-Module │ │ - Update parking │     │
│  │   dashboards    │ │ Reasoning    │ │ - Log workout    │     │
│  │ - Interactive   │ │ - Synthesis  │ │ - Set reminder   │     │
│  │   timelines     │ │ - Actions    │ │                  │     │
│  └─────────────────┘ └──────────────┘ └──────────────────┘     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 关键组件

#### 1. 共享个人上下文总线 (Shared Personal-Context Bus)

- **结构化状态发布**：模块以标准格式发布当前状态
- **Provider Contract**：提供者契约确保互操作性
- **实时同步**：所有接口访问同一状态

#### 2. 持久GUI (Persistent GUIs)

- **一瞥式监控**：无需打开聊天即可查看状态
- **可定制仪表板**：用户可自定义显示内容
- **交互式时间线**：纵向趋势监控

#### 3. 通用聊天代理 (Facai)

- **跨模块推理**：基于共享状态进行综合
- **情境感知回答**：结合多个模块的数据
- **有状态操作**：执行需要维护状态的任务

#### 4. 写回功能 (Write-Back Affordances)

- **双向操作**：不仅读取状态，还能修改
- **应用级集成**：与外部应用交互
- **同步动作**：跨接口同步操作

## 工作流程

### 1. 从用户意图生成

```
用户: "创建一个工具来跟踪我的日常时间线，
      使用手机和手表的传感器数据"
      
↓

AI生成引擎 → 创建BoBo模块
```

### 2. 状态发布到总线

```python
# BoBo模块发布状态
bobo_state = {
    "module": "BoBo",
    "timestamp": "2026-04-09T14:30:00Z",
    "state": {
        "motion": "walking",
        "steps": 8432,
        "heart_rate": 95,
        "sleep_quality": 0.72,
        "sleep_duration": 6.5
    },
    "affordances": ["log_workout", "set_reminder"]
}

publish_to_context_bus(bobo_state)
```

### 3. 跨模块查询处理

```
用户: "为什么我最近感觉这么疲惫？"

↓

Facai查询共享总线:
- BoBo: 睡眠质量(0.72), 睡眠时长(6.5h)
- Health: 最近锻炼(高强度), 心率变异性
- Calendar: 工作负载(高), 会议密度

↓

Facai综合回答:
"根据你的数据，可能原因包括：
1. 睡眠时长不足（平均6.5小时）
2. 最近高强度锻炼后恢复不足
3. 工作负载较重

建议：今晚尝试早点休息，明天进行轻度活动。"
```

### 4. 主动通知

```
BoBo检测到:
- 用户正在走回停车位
- 停车时间即将过期（剩余5分钟）
- 当前心率100（正常，考虑到刚锻炼完）

↓

主动通知:
"你的停车将在5分钟后过期，建议加快步伐。
你的心率100是正常的，考虑到你刚锻炼完。"
```

## 实现指南

### 步骤1：定义Provider Contract

```python
from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from datetime import datetime

@dataclass
class InstrumentState:
    """标准仪器状态格式"""
    module: str
    timestamp: datetime
    state: Dict[str, Any]
    affordances: List[str]
    metadata: Optional[Dict] = None

class ContextBus:
    """共享个人上下文总线"""
    
    def __init__(self):
        self._state = {}
        self._subscribers = []
    
    def publish(self, state: InstrumentState):
        """发布状态到总线"""
        self._state[state.module] = state
        self._notify_subscribers(state)
    
    def query(self, module: str = None, 
              state_key: str = None) -> Any:
        """查询总线状态"""
        if module:
            return self._state.get(module)
        return self._state
    
    def subscribe(self, callback):
        """订阅状态变化"""
        self._subscribers.append(callback)
    
    def _notify_subscribers(self, state):
        for callback in self._subscribers:
            callback(state)
```

### 步骤2：创建Instrument模块

```python
class Instrument:
    """PSI Instrument基类"""
    
    def __init__(self, name: str, context_bus: ContextBus):
        self.name = name
        self.bus = context_bus
        self.state = {}
        self.affordances = []
    
    def update_state(self, new_state: Dict):
        """更新并发布状态"""
        self.state.update(new_state)
        
        instrument_state = InstrumentState(
            module=self.name,
            timestamp=datetime.now(),
            state=self.state,
            affordances=self.affordances
        )
        
        self.bus.publish(instrument_state)
    
    def execute_affordance(self, action: str, params: Dict):
        """执行写回操作"""
        if action not in self.affordances:
            raise ValueError(f"Unknown affordance: {action}")
        
        # 执行具体操作
        return self._handle_action(action, params)
    
    def _handle_action(self, action: str, params: Dict):
        """子类实现具体操作"""
        raise NotImplementedError
```

### 步骤3：实现Chat Agent

```python
class FacaiAgent:
    """PSI通用聊天代理"""
    
    def __init__(self, context_bus: ContextBus, llm_client):
        self.bus = context_bus
        self.llm = llm_client
        self.bus.subscribe(self._on_state_update)
    
    def _on_state_update(self, state: InstrumentState):
        """监听状态更新"""
        # 可触发主动通知
        pass
    
    def process_query(self, user_query: str) -> str:
        """处理用户查询"""
        # 1. 获取当前上下文
        context = self._assemble_context()
        
        # 2. 构建prompt
        prompt = self._build_prompt(user_query, context)
        
        # 3. 调用LLM
        response = self.llm.generate(prompt)
        
        # 4. 解析并执行操作
        actions = self._parse_actions(response)
        self._execute_actions(actions)
        
        return response
    
    def _assemble_context(self) -> str:
        """组装跨模块上下文"""
        context_parts = []
        
        for module_name, state in self.bus.query().items():
            context_parts.append(
                f"[{module_name}]\n"
                f"{json.dumps(state.state, indent=2)}"
            )
        
        return "\n\n".join(context_parts)
```

### 步骤4：创建持久GUI

```python
class PersistentGUI:
    """持久GUI组件"""
    
    def __init__(self, context_bus: ContextBus):
        self.bus = context_bus
        self.instruments = {}
        self.bus.subscribe(self._on_state_update)
    
    def _on_state_update(self, state: InstrumentState):
        """更新GUI显示"""
        self.instruments[state.module] = state
        self._render()
    
    def _render(self):
        """渲染仪表板"""
        # 实现一瞥式监控界面
        pass
    
    def create_instrument_card(self, state: InstrumentState) -> Widget:
        """为仪器创建卡片视图"""
        card = Widget()
        card.title = state.module
        card.content = self._format_state(state.state)
        card.actions = state.affordances
        return card
```

## 设计原则

### 1. 本地集成义务

- 每个模块负责发布标准格式的状态
- 集成是模块的本地义务，而非成对问题
- 提供者契约确保互操作性

### 2. 分工明确

- **工具**：一瞥式监控和常规控制
- **聊天**：跨模块综合和有状态操作
- 两者操作同一共享状态

### 3. 渐进式集成

- 后期生成的仪器可通过相同契约自动集成
- 无需修改现有模块
- 向后兼容性

## 当前限制与未来工作

### 当前限制

1. **无条件注入**：提示长度随模块数量增长
2. **上下文污染**：过时或误导性摘要可能降低系统响应质量
3. **单用户验证**：当前证据来自单个技术熟练用户的三周部署

### 未来方向

- **大规模路由**：模块数量增长时的路由和选择策略
- **隐私和授权**：个人范围操作的隐私保护
- **非程序员可访问性**：使合规模块生成对非程序员可访问
- **上下文选择**：智能选择相关上下文子集

## 与现有架构比较

| 特性 | 传统MVC | 微前端 | 插件系统 | PSI |
|------|---------|--------|----------|-----|
| 状态共享 | ❌ | ⚠️ | ⚠️ | ✅ |
| 跨模块推理 | ❌ | ❌ | ❌ | ✅ |
| 自然语言生成 | ❌ | ❌ | ❌ | ✅ |
| 持久GUI | ✅ | ✅ | ✅ | ✅ |
| 聊天互补 | ❌ | ❌ | ❌ | ✅ |

## 应用场景

### 1. 个人健康助手
- 整合健康应用、可穿戴设备、日历
- 跨数据源综合健康洞察

### 2. 智能家居控制中心
- 统一控制不同厂商的智能设备
- 情境感知的自动化

### 3. 个人生产力套件
- 整合日历、任务、笔记、邮件
- 智能时间管理和提醒

### 4. 旅行助手
- 整合航班、酒店、地图、日历
- 实时行程调整和通知

## 触发词

- PSI
- shared state architecture
- personal AI
- AI-generated instruments
- coherent computing
- context bus
- persistent GUI
- chat-complementary
- cross-module reasoning
- 共享状态架构
- 个人AI
- 连贯计算

## 相关技能

- **discounted-mpc-robust-control**: 折扣MPC鲁棒控制
- **density-driven-multi-agent-control**: 多智能体密度控制
- **agent-memory-framework**: 代理记忆框架

## 参考文献

Wang, Z., Hu, E., Rucker, M., & Barnes, L. E. (2026). PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents. arXiv:2604.08529 [cs.HC].

## 实现注意事项

1. **状态格式标准化**：确保所有模块使用一致的状态格式
2. **实时性**：总线更新应及时传播到所有接口
3. **错误处理**：模块故障不应影响整个系统
4. **隐私保护**：敏感个人数据需要适当的访问控制
5. **可扩展性**：设计应支持模块数量的增长
