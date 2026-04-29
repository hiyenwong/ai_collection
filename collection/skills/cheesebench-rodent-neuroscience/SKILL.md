---
name: cheesebench-rodent-neuroscience
description: "CheeseBench - 基于经典啮齿动物行为神经科学范式的LLM评估基准。包含9个任务(水迷宫、T迷宫等)，跨越6个认知维度，评估空间导航、工作记忆等能力。Activation: rodent neuroscience, behavioral paradigm, cognitive benchmark, spatial navigation, LLM evaluation."
---

# CheeseBench 啮齿动物行为神经科学基准

## 描述
CheeseBench是一个基于经典啮齿动物行为神经科学范式的大型语言模型(LLM)评估基准。包含9个经典任务（Morris水迷宫、Barnes迷宫、T迷宫等），跨越6个认知维度。LLM通过ASCII文本观察环境和奖励信号来发现目标，类似于啮齿动物在不熟悉装置中的行为。

**来源论文:**
- arXiv:2604.10825v1 (2026-04-13)
- 作者: Zacharie Bugaud
- 领域: cs.AI (人工智能/行为神经科学)

## 核心概念

### 1. CheeseBench设计哲学
基于经典啮齿动物实验范式，为AI系统提供：
- **生态效度**: 模拟真实动物行为实验
- **标准化**: 统一的评估协议和基线
- **认知维度覆盖**: 空间、记忆、决策、学习等多维度
- **可比较性**: 与动物行为数据直接对比

### 2. 九大经典范式
涵盖啮齿动物神经科学的核心实验装置：
- **Morris水迷宫**: 空间学习与记忆
- **Barnes迷宫**: 空间导航与逃脱学习
- **T迷宫**: 工作记忆与空间选择
- **放射臂迷宫**: 工作记忆容量
- **星形迷宫**: 空间策略
- **操作性条件作用箱**: 工具性学习
- **穿梭箱**: 主动回避学习
- **条件性位置偏爱**: 动机与奖赏
- **延迟非匹配样本**: 识别记忆

### 3. 认知维度评估
六个核心认知能力维度：
1. **空间导航**: 理解空间关系、路径规划
2. **工作记忆**: 短期信息保持
3. **参考记忆**: 长期稳定信息
4. **学习速率**: 从经验中学习的速度
5. **决策制定**: 在不确定性下选择
6. **模式识别**: 识别环境规律

## 激活关键词
- rodent neuroscience
- behavioral paradigm
- cognitive benchmark
- spatial navigation
- working memory
- cheesebench
- 啮齿动物神经科学
- 行为范式
- 认知评估
- 空间迷宫

## 任务详解

### 1. Morris水迷宫 (Morris Water Maze)
```
场景描述:
圆形水池，水下隐藏平台，水浑浊不透明

任务目标:
学习平台位置，快速导航至平台

评估指标:
- 逃逸潜伏期: 找到平台所需时间
- 路径长度: 游动距离
- 目标象限停留时间: 记忆精度
- 穿越次数: 平台位置记忆

ASCII表示:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                            ~
~         [TARGET]           ~
~                            ~
~    @                       ~  @ = 代理位置
~                            ~
~                            ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

### 2. Barnes迷宫 (Barnes Maze)
```
场景描述:
圆形平台，周边20个洞，其中1个通向暗箱

任务目标:
学习逃脱洞位置

评估指标:
- 主错误数: 检查非目标洞的次数
- 潜伏期: 找到逃脱洞的时间
- 搜索策略: 随机 vs 系统化搜索

ASCII表示:
    [O] [O] [O] [O] [O]
   [O]               [O]
  [O]     ~~~~~~~     [O]
 [O]     ~       ~     [O]
[O]     ~   @    ~     [O]  @ = 代理
 [O]     ~       ~     [O]
  [O]     ~~~~~~~     [O]
   [O]               [O]
    [O] [O] [TARGET] [O]
```

### 3. T迷宫 (T-Maze)
```
场景描述:
T形通道，两臂中一侧有奖励

任务目标:
记忆奖励位置（空间交替任务）

评估指标:
- 正确选择率: 选择奖励臂的比例
- 自发交替率: 交替选择的自然倾向

ASCII表示:
    [GOAL A] [GOAL B]
         \   /
          \ /
           │
           │
           @     @ = 起始位置
```

### 4. 放射臂迷宫 (Radial Arm Maze)
```
场景描述:
中央平台，8条放射臂，部分臂有奖励

任务目标:
记住已访问的臂，避免重复进入

评估指标:
- 工作记忆错误: 重复进入有奖励臂
- 参考记忆错误: 进入无奖励臂
- 完成时间

ASCII表示:
        [ARM 1]
           │
           │
[ARM 8]────┼────[ARM 2]
           │
[ARM 7]─── @ ───[ARM 3]
           │
[ARM 6]────┼────[ARM 4]
           │
        [ARM 5]
```

### 5. 操作性条件作用 (Operant Chamber)
```
场景描述:
Skinner箱，杠杆、食物槽、刺激灯

任务目标:
学习杠杆按压与奖励的关联

评估指标:
- 反应率: 单位时间按压次数
- 消退曲线: 奖励停止后的行为变化
- 辨别学习: 区分刺激信号

ASCII表示:
┌─────────────────────┐
│  [LIGHT]   [LEVER]  │
│      O      [___]   │
│                     │
│         @           │  @ = 代理
│                     │
│     [FOOD TRAY]     │
│         U           │
└─────────────────────┘
```

## 方法论步骤

### Step 1: 环境构建

#### ASCII渲染系统
```python
class ASCIIRenderer:
    """ASCII环境渲染器"""
    
    def __init__(self, env_type, size=(20, 20)):
        self.env_type = env_type
        self.size = size
        self.agent_pos = (0, 0)
        self.goal_pos = None
        self.obstacles = []
        
    def render(self):
        """渲染当前环境状态"""
        grid = [[' ' for _ in range(self.size[1])] 
                for _ in range(self.size[0])]
        
        # 渲染边界
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if i == 0 or i == self.size[0]-1:
                    grid[i][j] = '~'
                elif j == 0 or j == self.size[1]-1:
                    grid[i][j] = '|'
        
        # 渲染目标
        if self.goal_pos:
            gx, gy = self.goal_pos
            grid[gx][gy] = 'G'
        
        # 渲染代理
        ax, ay = self.agent_pos
        grid[ax][ay] = '@'
        
        return '\n'.join([''.join(row) for row in grid])
    
    def move(self, direction):
        """移动代理"""
        moves = {
            'N': (-1, 0), 'S': (1, 0),
            'E': (0, 1), 'W': (0, -1)
        }
        dx, dy = moves.get(direction, (0, 0))
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy
        
        # 检查边界
        if 0 <= new_x < self.size[0] and 0 <= new_y < self.size[1]:
            self.agent_pos = (new_x, new_y)
            return True
        return False
```

#### 统一系统提示
```python
SYSTEM_PROMPT = """
You are an agent in a behavioral neuroscience experiment.
Your task is to learn from interactions with the environment.

You receive ASCII representations of the environment and reward signals.
You must discover the task goals through exploration and learning.

Actions:
- MOVE [N/S/E/W]: Move in the specified direction
- INTERACT: Interact with object at current location
- WAIT: Do nothing

You will receive:
- Current ASCII view
- Reward signal (0 = no reward, 1 = small reward, 10 = goal reached)
- Previous action outcome

Task: {task_description}

Remember:
1. Explore to understand the environment structure
2. Learn from reward signals
3. Develop efficient strategies
4. Adapt to changes in the environment
"""
```

### Step 2: 实验协议

#### 训练流程
```python
class CheeseBenchExperiment:
    def __init__(self, model, task):
        self.model = model
        self.task = task
        self.renderer = self.create_renderer(task)
        
    def run_trial(self, max_steps=100):
        """运行单个实验试次"""
        history = []
        total_reward = 0
        steps = 0
        
        # 初始化环境
        self.renderer.reset()
        
        for step in range(max_steps):
            # 观察
            observation = self.renderer.render()
            
            # LLM决策
            action = self.model.decide(
                system_prompt=SYSTEM_PROMPT.format(task=self.task),
                observation=observation,
                history=history
            )
            
            # 执行动作
            reward, done = self.renderer.execute(action)
            
            # 记录
            history.append({
                'step': step,
                'observation': observation,
                'action': action,
                'reward': reward
            })
            
            total_reward += reward
            steps += 1
            
            if done:
                break
        
        return {
            'history': history,
            'total_reward': total_reward,
            'steps': steps,
            'success': done
        }
    
    def run_session(self, n_trials=20):
        """运行完整实验会话"""
        results = []
        for trial in range(n_trials):
            result = self.run_trial()
            results.append(result)
        return results
```

### Step 3: 评估指标

#### 认知维度评估
```python
class CognitiveEvaluator:
    def __init__(self, results):
        self.results = results
        
    def spatial_navigation(self):
        """空间导航能力"""
        escape_latencies = [r['steps'] for r in self.results]
        path_lengths = self.calculate_path_lengths()
        
        return {
            'mean_latency': np.mean(escape_latencies),
            'learning_rate': self.calculate_learning_rate(escape_latencies),
            'path_efficiency': self.calculate_path_efficiency(path_lengths)
        }
    
    def working_memory(self):
        """工作记忆能力"""
        if self.task == 'radial_arm_maze':
            errors = self.count_reentry_errors()
            return {
                'reentry_errors': errors,
                'memory_span': self.estimate_memory_span()
            }
        return None
    
    def learning_rate(self):
        """学习速率"""
        # 拟合指数学习曲线
        from scipy.optimize import curve_fit
        
        def learning_curve(x, a, b, c):
            return a * np.exp(-b * x) + c
        
        trials = range(len(self.results))
        performance = [r['success'] for r in self.results]
        
        popt, _ = curve_fit(learning_curve, trials, performance)
        return popt[1]  # b = 学习速率
    
    def decision_making(self):
        """决策制定"""
        return {
            'exploration_exploitation': self.analyze_exploration(),
            'risk_preference': self.analyze_risk_preference(),
            'choice_consistency': self.analyze_consistency()
        }
```

## 关键发现

### 发现1: LLM与动物表现对比
```
总体成功率 (平均):

随机基线:           32.1%
Qwen2.5-VL-7B:      52.6%  (最佳LLM)
近似啮齿动物基线:    78.9%

结论: 当前开源LLM远低于啮齿动物表现
```

### 发现2: 任务特异性
```
各任务表现 (Qwen2.5-VL-7B):

Morris水迷宫:      45% (空间导航)
Barnes迷宫:        62% (逃脱学习)
T迷宫:             38% (工作记忆)
放射臂迷宫:        28% (工作记忆容量)
操作性条件作用:     71% (工具学习)
穿梭箱:            55% (回避学习)
条件位置偏爱:      48% (动机)
延迟非匹配:        33% (识别记忆)

发现: 工具学习(操作性条件作用)表现最佳
     需要复杂工作记忆的任务表现最差
```

### 发现3: 模型规模效应
```
模型参数 vs 性能:

3B:   41.2%
7B:   52.6% (峰值)
32B:  48.3% (下降)
72B:  46.1% (继续下降)

意外发现: 超过7B参数后性能下降
可能原因: 过拟合到训练数据中的特定模式
```

### 发现4: 界面参数影响
```
上下文长度影响:
- 1步历史:  48%
- 5步历史:  52% (最优)
- 10步历史: 44%
- 20步历史: 37%

发现: 过长上下文损害性能，最优约5步

提示策略影响:
- 无CoT:   52.6%
- 有CoT:   41.2%

发现: Chain-of-Thought反而损害性能
原因: 可能干扰即时反应学习
```

## 应用场景

### 1. AI系统认知评估
- **能力诊断**: 识别LLM在特定认知维度的强弱
- **基准测试**: 标准化比较不同模型
- **开发迭代**: 追踪训练过程中的能力变化

### 2. 神经科学模拟
- **计算模型**: 构建类动物认知模型
- **假说验证**: 测试认知理论
- **药物效应**: 模拟神经调节物质影响

### 3. 具身AI研究
- **感知-行动循环**: 研究感知与行动的关系
- **环境适应**: 测试适应性学习能力
- **迁移学习**: 跨任务知识迁移

## 代码示例

### 完整评估流程
```python
from cheesebench import CheeseBench

# 加载模型
model = load_model("Qwen2.5-VL-7B")

# 运行评估
benchmark = CheeseBench(model)

# 评估所有任务
all_results = {}
for task in ['morris', 'barnes', 't_maze', 'radial_arm', 
             'operant', 'shuttle', 'cpp', 'dnmts']:
    results = benchmark.evaluate(task, n_trials=20)
    all_results[task] = results
    
# 生成报告
report = benchmark.generate_report(all_results)
print(report.summary())

# 与动物基线比较
comparison = benchmark.compare_to_rodent_baselines(all_results)
print(comparison)
```

### 自定义任务
```python
class CustomMaze:
    def __init__(self):
        self.renderer = ASCIIRenderer()
        
    def reset(self):
        self.agent_pos = (5, 5)
        self.goal_pos = (15, 15)
        return self.renderer.render()
        
    def step(self, action):
        # 执行动作
        if action.startswith('MOVE'):
            direction = action.split()[1]
            success = self.renderer.move(direction)
        
        # 检查目标
        done = self.agent_pos == self.goal_pos
        reward = 10 if done else -0.1  # 时间惩罚
        
        return self.renderer.render(), reward, done
```

## 与其他工作的关联

- **Animal-AI Olympics**: 基于Unity的动物认知测试
- **PsychLab**: DeepMind的心理学测试环境
- **Animal-AI**: 具身认知测试平台
- **ARC**: 抽象推理语料库

## 引用

```bibtex
@article{bugaud2026cheesebench,
  title={CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms},
  author={Bugaud, Zacharie},
  journal={arXiv preprint arXiv:2604.10825},
  year={2026}
}

@article{morris1984developments,
  title={Developments of a water-maze procedure for studying spatial learning in the rat},
  author={Morris, Richard GM},
  journal={Journal of Neuroscience Methods},
  year={1984}
}
```

## 相关技能
- animal-ai-testing: 动物AI测试
- embodied-cognition: 具身认知
- spatial-reasoning: 空间推理
- reinforcement-learning: 强化学习

_Last updated: 2026-04-15_
