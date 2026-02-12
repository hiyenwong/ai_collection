# 股票模型分析 Agent + Skill 设计方案

## 设计目标

创建一个专业的股票分析系统，能够：
1. 获取股票数据（历史、实时）
2. 进行技术分析（K线、指标）
3. 执行量化模型策略
4. 生成分析报告和可视化
5. 支持多股票批量分析

## 架构设计

### 方案 A：单 Agent + 多 Skill
```
Stock Analysis Agent
├── AkShare Skill (数据获取)
├── Stock Technical Analysis Skill (技术分析)
├── Stock Visualization Skill (可视化)
└── Stock Report Skill (报告生成)
```

### 方案 B：单 Agent + 单综合 Skill（推荐）
```
Stock Analysis Agent
└── Stock Analysis Skill (综合能力)
    ├── 数据获取
    ├── 技术指标计算
    ├── 模型评分
    ├── 可视化生成
    └── 报告输出
```

**推荐方案 B** - 因为股票分析是紧密相关的流程，放在一个 skill 中更容易管理。

---

## Agent 设计：Stock Analysis Agent

### 基本信息
- **Agent ID:** `stock-analyst`
- **目的:** 股票数据获取、技术分析、模型评分、报告生成
- **模型:** claude-sonnet-4.5（平衡速度和推理能力）

### 核心能力
1. **数据获取:** 获取股票历史数据、实时行情
2. **技术分析:** 计算 KDJ, MACD, RSI, 布林带等指标
3. **模型评分:** 基于技术指标的综合评分
4. **可视化:** 生成 K 线图、指标图
5. **报告生成:** Markdown 格式的分析报告

### 工具依赖
- **AkShare:** 获取股票数据
- **Python (pandas, talib, mplfinance):** 数据处理和技术指标
- **Matplotlib/Plotly:** 数据可视化

---

## Skill 设计：Stock Analysis

### Skill 结构
```
collection/skills/stock-analysis/
├── SKILL.md              # 主文档
├── examples/             # 使用示例
│   ├── single-stock-analysis.md
│   ├── multi-stock-comparison.md
│   └── technical-indicators.md
├── scripts/              # Python 脚本
│   ├── fetch_data.py      # 获取股票数据
│   ├── indicators.py      # 计算技术指标
│   ├── scoring.py        # 模型评分
│   └── visualize.py     # 可视化生成
├── references/           # 参考资料
│   ├── technical-analysis.md
│   └── indicators-guide.md
└── assets/              # 示例图表
    └── sample-charts/
```

### 激活关键词
- stock analysis
- 股票分析
- technical analysis
- 技术分析
- stock indicators
- stock chart
- k-line
- kdj, macd, rsi
- 股票评分
- stock score

---

## 技术指标设计

### 基础指标
- **MA:** 移动平均线（5, 10, 20, 60日）
- **EMA:** 指数移动平均
- **VOL:** 成交量

### 趋势指标
- **MACD:** 异同移动平均线
- **BOLL:** 布林带
- **SAR:** 抛物线转向

### 震荡指标
- **RSI:** 相对强弱指标
- **KDJ:** 随机指标
- **CCI:** 顺势指标

### 动量指标
- **OBV:** 能量潮
- **BIAS:** 乖离率
- **MOM:** 动量指标

---

## 模型评分设计

### 综合评分模型

```python
def calculate_stock_score(df):
    """
    综合评分模型
    - 趋势分数: 40%
    - 动量分数: 30%
    - 资金面分数: 20%
    - 情绪分数: 10%
    """

    # 1. 趋势分数 (40%)
    trend_score = calculate_trend_score(df)
    # - MACD 金叉/死叉
    # - MA 多头/空头排列
    # - 股价在布林带位置

    # 2. 动量分数 (30%)
    momentum_score = calculate_momentum_score(df)
    # - RSI 超买/超卖
    # - KDJ 状态
    # - MOM 趋势

    # 3. 资金面分数 (20%)
    money_flow_score = calculate_money_flow_score(df)
    # - OBV 趋势
    # - 成交量变化
    # - 主力资金流向

    # 4. 情绪分数 (10%)
    sentiment_score = calculate_sentiment_score(df)
    # - 连续涨跌天数
    # - 振幅
    # - 换手率

    # 加权综合
    total_score = (
        trend_score * 0.4 +
        momentum_score * 0.3 +
        money_flow_score * 0.2 +
        sentiment_score * 0.1
    )

    return {
        'total_score': total_score,
        'trend_score': trend_score,
        'momentum_score': momentum_score,
        'money_flow_score': money_flow_score,
        'sentiment_score': sentiment_score
    }
```

### 评分等级
- **90-100:** 强烈买入 🟢
- **80-90:** 买入 🟢
- **60-80:** 持有 🟡
- **40-60:** 观望 🟡
- **0-40:** 卖出 🔴

---

## 使用流程设计

### 单股票分析
```
用户: "分析一下贵州茅台 (600519) 最近 60 天的走势"

Agent 流程:
1. 使用 AkShare 获取 600519 数据 (60 天)
2. 计算技术指标 (MA, MACD, KDJ, RSI, BOLL, OBV)
3. 计算综合评分
4. 生成 K 线图 + 指标图
5. 生成 Markdown 报告
6. 输出报告和图表
```

### 多股票对比
```
用户: "对比分析 贵州茅台、五粮液、泸州老窖"

Agent 流程:
1. 获取 3 只股票数据
2. 分别计算技术指标和评分
3. 生成对比表格
4. 生成对比图表
5. 输出对比报告
```

### 技术指标查询
```
用户: "600519 的 MACD 和 KDJ 是什么状态？"

Agent 流程:
1. 获取数据
2. 计算 MACD 和 KDJ
3. 解读指标状态
4. 给出操作建议
```

---

## 报告模板

### Markdown 报告格式
```markdown
# 股票分析报告

## 基本信息
- **股票代码:** 600519
- **股票名称:** 贵州茅台
- **分析日期:** 2026-02-04
- **分析周期:** 近 60 个交易日

## 综合评分
| 指标 | 分数 | 权重 | 状态 |
|------|------|------|------|
| 趋势 | 85/100 | 40% | 🟢 偏强 |
| 动量 | 78/100 | 30% | 🟡 中性 |
| 资金面 | 90/100 | 20% | 🟢 流入 |
| 情绪 | 65/100 | 10% | 🟡 中性 |
| **综合** | **82/100** | - | **🟢 买入** |

## 技术指标分析

### 趋势指标
- **MA (5, 10, 20, 60):** [图表和解读]
- **MACD (12, 26, 9):** [金叉/死叉状态]

### 震荡指标
- **RSI (14):** [超买/超卖状态]
- **KDJ (9, 3, 3):** [J 值状态]

### 其他指标
- **BOLL (20, 2):** [股价在布林带位置]
- **OBV:** [资金流向]

## 操作建议
1. **短期:** 建议 [买入/持有/卖出]
2. **中期:** 建议 [买入/持有/卖出]
3. **长期:** 建议 [买入/持有/卖出]

## 风险提示
- [风险点 1]
- [风险点 2]

## 图表
![K线图](kline.png)
![MACD](macd.png)
![RSI](rsi.png)
```

---

## 实施步骤

### Phase 1: 创建 Skill
1. 创建目录结构
2. 编写 SKILL.md 文档
3. 创建 Python 脚本（数据获取、指标计算）
4. 测试基本功能

### Phase 2: 创建 Agent
1. 创建 AGENT.md
2. 编写系统提示词
3. 配置工具和技能
4. 测试分析流程

### Phase 3: 优化和扩展
1. 添加更多技术指标
2. 优化评分模型
3. 添加可视化选项
4. 创建更多示例

---

## 预期效果

### 示例交互
```
用户: "分析一下 600547 山东黄金最近 30 天的走势，并给出操作建议"

Agent:
1. ✅ 获取数据: 从 AkShare 获取 600547 数据
2. ✅ 计算指标: MA, MACD, KDJ, RSI, BOLL, OBV
3. ✅ 评分计算: 趋势 85, 动量 72, 资金 78, 情绪 60
4. ✅ 综合评分: 76/100 🟡 持有
5. ✅ 生成报告: 完整的 Markdown 报告
6. ✅ 生成图表: K 线图、指标图

输出:
- 综合评分: 76/100 (持有)
- 趋势: 🟢 偏强 (MA 多头排列，MACD 金叉)
- 动量: 🟡 中性 (RSI 55，KDJ J 值 60)
- 资金面: 🟢 流入 (OBV 上升，放量)
- 情绪: 🟡 中性 (连续 3 天上涨)

建议:
- 短期: 观望，等待回调
- 中期: 可逢低买入
- 长期: 持有为主

风险提示:
- 近期涨幅较大，注意回调风险
- 关注成交量变化

[附图表]
```

---

## 扩展功能（未来）

1. **基本面分析:** 财务指标、市盈率、市净率
2. **新闻情感:** 抓取相关新闻，分析市场情绪
3. **板块分析:** 同板块股票对比
4. **回测系统:** 策略回测和优化
5. **预警系统:** 价格突破、指标异动提醒
6. **批量分析:** 一键分析多只股票

---

## 技术栈

### 必需依赖
- **Python 3.8+**
- **akshare:** 股票数据
- **pandas:** 数据处理
- **numpy:** 数值计算

### 可选依赖
- **talib:** 技术指标计算（更快）
- **mplfinance:** K 线图绘制
- **plotly:** 交互式图表
- **scikit-learn:** 机器学习模型

---

## 问题和建议

这个设计方案是否符合你的需求？需要调整的地方：

1. **技术指标:** 需要添加哪些特定指标？
2. **评分模型:** 是否需要自定义权重？
3. **输出格式:** Markdown 报告是否足够？是否需要 PDF/Excel？
4. **分析周期:** 默认 60 天是否合适？还是 30/90 天？
5. **其他功能:** 是否需要基本面、新闻情感等扩展功能？

请告诉我你的想法，我们可以进一步优化设计！
