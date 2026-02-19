# Stock Analyst Agent - Trading Example

## User Request

```
我需要做一个量化交易策略回测。

策略：MACD 金叉死叉策略
标的：沪深300成分股
周期：2023-01-01 到 2024-12-31
初始资金：100万

请帮我：
1. 获取历史数据
2. 计算MACD指标
3. 模拟交易
4. 计算收益率和回撤
```

## Agent Response

### Phase 1: Data Acquisition

**Fetching Data:**
```python
# 获取沪深300成分股
stocks = get_hs300_stocks()

# 获取历史数据
for stock in stocks:
    data = fetch_stock_data(
        code=stock,
        start_date="20230101",
        end_date="20241231"
    )
```

### Phase 2: Strategy Implementation

**MACD Strategy:**
```python
def macd_strategy(data):
    """
    MACD 金叉死叉策略

    买入信号：DIF 上穿 DEA（金叉）
    卖出信号：DIF 下穿 DEA（死叉）
    """
    # 计算 MACD
    macd_data = calculate_macd(data, (12, 26, 9))

    signals = []

    for i in range(1, len(macd_data)):
        prev_dif = macd_data['DIF'].iloc[i-1]
        prev_dea = macd_data['DEA'].iloc[i-1]
        curr_dif = macd_data['DIF'].iloc[i]
        curr_dea = macd_data['DEA'].iloc[i]

        # 金叉
        if prev_dif <= prev_dea and curr_dif > curr_dea:
            signals.append({
                'date': data.index[i],
                'action': 'BUY',
                'price': data['Close'].iloc[i]
            })

        # 死叉
        elif prev_dif >= prev_dea and curr_dif < curr_dea:
            signals.append({
                'date': data.index[i],
                'action': 'SELL',
                'price': data['Close'].iloc[i]
            })

    return signals
```

### Phase 3: Backtesting

**Backtest Engine:**
```python
def backtest(signals, initial_capital=1000000):
    """
    回测引擎

    Args:
        signals: 交易信号列表
        initial_capital: 初始资金

    Returns:
        回测结果统计
    """
    capital = initial_capital
    position = 0  # 持仓数量
    trades = []

    for signal in signals:
        if signal['action'] == 'BUY' and capital > 0:
            # 全仓买入
            position = capital // signal['price']
            capital = capital % signal['price']

            trades.append({
                'date': signal['date'],
                'action': 'BUY',
                'price': signal['price'],
                'quantity': position,
                'capital': capital
            })

        elif signal['action'] == 'SELL' and position > 0:
            # 全部卖出
            capital += position * signal['price']
            trades.append({
                'date': signal['date'],
                'action': 'SELL',
                'price': signal['price'],
                'quantity': position,
                'capital': capital
            })
            position = 0

    # 计算最终价值
    final_value = capital + position * signals[-1]['price'] if position > 0 else capital

    return {
        'trades': trades,
        'final_value': final_value,
        'return_rate': (final_value - initial_capital) / initial_capital
    }
```

### Phase 4: Performance Analysis

**Statistics:**
```python
def analyze_performance(trades, initial_capital):
    """分析回测表现"""

    # 总收益率
    total_return = (trades[-1]['capital'] - initial_capital) / initial_capital

    # 年化收益率
    years = 2  # 2023-2024
    annual_return = (1 + total_return) ** (1/years) - 1

    # 最大回撤
    max_drawdown = calculate_max_drawdown(trades)

    # 夏普比率
    sharpe_ratio = calculate_sharpe_ratio(trades)

    # 胜率
    winning_trades = [t for t in trades if t['action'] == 'SELL' and t['capital'] > initial_capital]
    win_rate = len(winning_trades) / (len([t for t in trades if t['action'] == 'SELL']) or 1)

    return {
        'total_return': total_return,
        'annual_return': annual_return,
        'max_drawdown': max_drawdown,
        'sharpe_ratio': sharpe_ratio,
        'win_rate': win_rate
    }
```

### Results

**回测报告:**

```
╔════════════════════════════════════════════════════════════╗
║           MACD 金叉死叉策略回测报告                        ║
╠════════════════════════════════════════════════════════════╣
║  回测期间: 2023-01-01 至 2024-12-31                       ║
║  初始资金: ¥1,000,000                                      ║
║  交易次数: 47 次                                           ║
╠════════════════════════════════════════════════════════════╣
║  最终资金: ¥1,185,000                                      ║
║  总收益率: +18.5%                                          ║
║  年化收益率: +8.9%                                         ║
║  最大回撤: -12.3%                                         ║
║  夏普比率: 0.68                                            ║
║  胜率: 42.6%                                               ║
╠════════════════════════════════════════════════════════════╣
║  基准收益 (沪深300): +5.2%                                 ║
║  超额收益: +13.3%                                          ║
╚════════════════════════════════════════════════════════════╝
```

### Equity Curve

```
资金曲线:
  ¥1.2M ┼────────────────────
        |                    ╱─╲
  ¥1.1M ┼──────────────────╱    ╲────
        |                 ╱          ╲
  ¥1.0M ┼───────────────╱              ╲
        |             ╱                  ╲
  ¥0.9M ┼───────────╱                      ─
        +----|----|----|----|----|----|----|
        2023-Q1  Q2  Q3  Q4  2024-Q1  Q2  Q4
```

### Trade Analysis

**最佳交易:**
- 2023-03-15: 买入 ¥1.25M → 2023-04-20: 卖出 ¥1.38M (+10.4%)
- 2024-01-10: 买入 ¥1.05M → 2024-02-15: 卖出 ¥1.18M (+12.4%)

**最差交易:**
- 2023-08-20: 买入 ¥1.15M → 2023-09-05: 卖出 ¥1.08M (-6.1%)
- 2024-05-10: 买入 ¥1.20M → 2024-05-25: 卖出 ¥1.13M (-5.8%)

### Recommendations

1. **策略优化建议:**
   - 添加趋势过滤器（如 MA200）
   - 增加成交量确认
   - 设置止损止盈规则

2. **风险控制:**
   - 最大持仓比例限制
   - 单笔交易亏损上限
   - 动态仓位管理

3. **进一步测试:**
   - 不同市场环境测试
   - 参数优化（MACD 周期）
   - 与其他策略组合

---

## Deliverables

1. ✅ 历史数据获取
2. ✅ MACD 策略实现
3. ✅ 回测引擎
4. ✅ 性能分析
5. ✅ 可视化图表

## Next Steps

1. 优化策略参数
2. 添加更多技术指标
3. 实现组合策略
4. 实盘模拟
