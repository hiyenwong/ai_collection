---
name: clawgui-unified-gui-agent-framework
description: "ClawGUI unified framework for training, evaluating, and deploying GUI agents. Open-source infrastructure with RL training (ClawGUI-RL), standardized evaluation (ClawGUI-Eval), and multi-platform deployment (ClawGUI-Agent). Activation: GUI agent, visual interface automation, RL training GUI, mobile agent deployment."
---

# ClawGUI: Unified Framework for GUI Agents

## Overview

ClawGUI is an open-source full-stack framework addressing three critical gaps in GUI agent research: training ecosystem closure, evaluation protocol inconsistency, and deployment barriers to real users. It unifies RL training, standardized evaluation, and multi-platform deployment in a single harness.

## Core Components

### 1. ClawGUI-RL: Scalable RL Training

**First open-source GUI agent RL infrastructure** with:
- Parallel virtual environments support
- Real physical device integration
- GiGPO (Generalized GUI Policy Optimization)
- Process Reward Model for dense step-level supervision
- No human annotation required

**Key Features**:
```python
# ClawGUI-RL Configuration
rl_config = {
    "environments": {
        "virtual": "android_emulator",
        "physical": "real_device_lab",
        "parallel_workers": 16
    },
    "algorithm": "GiGPO",
    "reward_model": "process_reward",
    "annotation": "none"  # Outcome-based rewards
}
```

### 2. ClawGUI-Eval: Standardized Evaluation

**Reproducible three-stage evaluation pipeline**:
- 6 benchmarks coverage
- 11+ models supported
- 95.8% reproduction rate against official baselines

**Evaluation Stages**:
1. **Grounding**: Element localization accuracy
2. **Navigation**: Task completion ability
3. **End-to-End**: Full task success rate

```python
# Evaluation pipeline
eval_pipeline = {
    "benchmarks": [
        "MobileWorld",
        "GUI-Only",
        "WebShop",
        "Mind2Web",
        "AITW",
        "OmniACT"
    ],
    "models": ["ClawGUI-2B", "MAI-UI-2B", "GPT-4V", "Gemini"],
    "metrics": ["success_rate", "step_accuracy", "efficiency"]
}
```

### 3. ClawGUI-Agent: Real-World Deployment

**Multi-platform deployment** to:
- Android
- HarmonyOS
- iOS

**Integration** with 12+ chat platforms:
- WeChat
- Slack
- Telegram
- Discord
- etc.

**Features**:
- Hybrid CLI-GUI control
- Persistent personalized memory
- Real-device operation

## Key Results

| Model | Benchmark | Success Rate | Improvement |
|-------|-----------|--------------|-------------|
| ClawGUI-2B | MobileWorld GUI-Only | 17.1% | +6.0% vs MAI-UI-2B |

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ClawGUI Framework                       │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ ClawGUI-RL   │→ │ ClawGUI-Eval │→ │ ClawGUI-Agent│      │
│  │   Training   │  │  Evaluation  │  │  Deployment  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         ↑                   ↓                   │            │
│    GiGPO + PRM       6 Benchmarks      Android/Harmony/iOS   │
│  Parallel Env        11+ Models        12+ Chat Platforms    │
└─────────────────────────────────────────────────────────────┘
```

## Process Reward Model (PRM)

**Dense step-level supervision** without human annotation:
- Analyzes each GUI action's contribution to task completion
- Provides fine-grained reward signals for RL training
- Eliminates need for expensive human reward labeling

## Activation Keywords

- GUI agent framework
- visual interface automation
- mobile agent training
- RL training GUI
- multi-platform agent deployment
- ClawGUI
- GUI agent evaluation
- Android Harmony iOS agent

## Tools Used

- Python 3.x
- PyTorch/TensorFlow
- Android Debug Bridge (ADB)
- Appium (for mobile automation)
- Docker (for virtual environments)
- OpenAI Gym/Gymnasium (RL interface)

## Instructions for Agents

### Setup ClawGUI

```bash
# Clone repository
git clone https://github.com/zju-real/ClawGUI
cd ClawGUI

# Install dependencies
pip install -r requirements.txt

# Setup Android emulator or connect physical device
adb devices
```

### Training Workflow

```python
# 1. Configure training environment
from clawgui import ClawGUI_RL

rl_trainer = ClawGUI_RL(
    env_type="android",
    algorithm="GiGPO",
    reward_model="PRM",
    num_workers=16
)

# 2. Start training
rl_trainer.train(
    task_suite="mobileworld",
    episodes=100000,
    save_interval=1000
)

# 3. Evaluate checkpoint
rl_trainer.evaluate(
    checkpoint="checkpoint_100k.pt",
    benchmark="mobileworld_gui_only"
)
```

### Evaluation Workflow

```python
from clawgui import ClawGUI_Eval

evaluator = ClawGUI_Eval(benchmarks=["mobileworld", "aitw"])

# Evaluate model across all benchmarks
results = evaluator.evaluate_model(
    model_path="clawgui_2b.pt",
    metrics=["success_rate", "step_accuracy"]
)

print(f"Success Rate: {results['mobileworld']['success_rate']:.1%}")
```

### Deployment Workflow

```python
from clawgui import ClawGUI_Agent

# Deploy to specific platform
agent = ClawGUI_Agent(
    model="clawgui_2b.pt",
    platform="android",
    chat_platform="wechat"
)

# Start serving
agent.serve()
```

## Error Handling

### Training Issues

1. **Environment Connection Failed**
   - Check ADB connection: `adb devices`
   - Verify emulator is running
   - Solution: Restart ADB server

2. **OOM During Training**
   - Reduce batch size
   - Decrease number of parallel workers
   - Solution: `num_workers = 8`

3. **Reward Model Divergence**
   - PRM may overfit on limited tasks
   - Solution: Increase task diversity

### Evaluation Issues

1. **Benchmark Not Reproducing**
   - Check environment version
   - Verify model checkpoint
   - Solution: Use ClawGUI-Eval's containerized environments

2. **Metrics Mismatch**
   - Different evaluation protocols across works
   - Solution: Use standardized ClawGUI-Eval pipeline

### Deployment Issues

1. **Permission Denied on Device**
   - Enable USB debugging
   - Grant accessibility permissions
   - Solution: `adb shell pm grant ...`

2. **Chat Platform Integration Failed**
   - Check webhook configuration
   - Verify API tokens
   - Solution: Use provided example configs

## Advantages

1. **Open Source**: First fully open GUI agent RL infrastructure
2. **Reproducible**: 95.8% baseline reproduction rate
3. **Scalable**: Parallel virtual + physical environments
4. **No Human Annotation**: Outcome-based PRM rewards
5. **Multi-Platform**: Android, HarmonyOS, iOS support
6. **Real Deployment**: 12+ chat platform integrations

## Limitations

- MobileWorld GUI-Only success rate still modest (17.1%)
- Requires physical device lab for realistic training
- Limited to GUI-based apps (not CLI tools)
- Process Reward Model may not capture all task nuances

## Applications

1. **Mobile App Testing**: Automated UI testing at scale
2. **Accessibility Tools**: Voice-controlled app navigation
3. **Digital Automation**: End-to-end task automation
4. **App Store Agents**: Autonomous app exploration
5. **E-commerce Automation**: Automated shopping workflows

## Reference

- **Paper**: ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents
- **Authors**: Fei Tang, Zhiqiong Lu, Boxuan Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- **arXiv**: [2604.11784](https://arxiv.org/abs/2604.11784) (2026-04-13)
- **GitHub**: https://github.com/zju-real/ClawGUI
- **Project Page**: https://zju-real.github.io/ClawGUI-Page/
- **Category**: cs.LG (Machine Learning)

## Related Skills

- mobile-agent-research
- rl-gui-training
- automated-ui-testing
- multi-platform-deployment
