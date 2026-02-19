# 技术指标参考

本文档提供股票分析中使用的所有技术指标的详细参考。

## 趋势指标

### MA (Moving Average) 移动平均线

**公式:**
```
MA(n) = (P1 + P2 + ... + Pn) / n
```

**参数:**
- MA5, MA10, MA20, MA30, MA60, MA120

**解读:**
- 价格位于 MA 之上 → 看涨
- 价格位于 MA 之下 → 看跌
- 短期 MA 上穿长期 MA → 金叉（买入）
- 短期 MA 下穿长期 MA → 死叉（卖出）

### EMA (Exponential MA) 指数移动平均

**公式:**
```
EMA(today) = (Price × K) + (EMA(yesterday) × (1 - K))
K = 2 / (n + 1)
```

**特点:** 对近期价格赋予更高权重，反应更快

### BOLL (Bollinger Bands) 布林带

**公式:**
```
中轨 = MA(20)
上轨 = 中轨 + 2 × SD(20)
下轨 = 中轨 - 2 × SD(20)
```

**解读:**
- 价格触及上轨 → 超买
- 价格触及下轨 → 超卖
- 布林带收窄 → 变盘前兆
- 突破上轨 → 强势信号

### MACD (Moving Average Convergence Divergence)

**公式:**
```
DIF = EMA(12) - EMA(26)
DEA = EMA(DIF, 9)
MACD = 2 × (DIF - DEA)
```

**解读:**
- DIF 上穿 DEA → 金叉买入
- DIF 下穿 DEA → 死叉卖出
- MACD 柱状图由负转正 → 买入信号
- 底部顶背离 → 反转信号

### SAR (Parabolic SAR) 抛物线转向

**公式:**
```
SAR(n) = SAR(n-1) + AF × (EP - SAR(n-1))
```

**解读:**
- 价格位于 SAR 之上 → 上升趋势
- 价格位于 SAR 之下 → 下降趋势
- SAR 翻转 → 趋势改变信号

## 震荡指标

### RSI (Relative Strength Index)

**公式:**
```
RSI = 100 - (100 / (1 + RS))
RS = 平均涨幅 / 平均跌幅
```

**参数:** RSI6, RSI12, RSI24

**解读:**
- RSI > 80 → 超买
- RSI < 20 → 超卖
- RSI 50 → 中性
- 顶/底背离 → 反转预警

### KDJ (Stochastic Oscillator)

**公式:**
```
RSV = (Close - Low(n)) / (High(n) - Low(n)) × 100
K = 2/3 × K(yesterday) + 1/3 × RSV
D = 2/3 × D(yesterday) + 1/3 × K
J = 3 × K - 2 × D
```

**参数:** (9, 3, 3)

**解读:**
- K > D → 多头
- K < D → 空头
- J > 100 → 超买
- J < 0 → 超卖

### CCI (Commodity Channel Index)

**公式:**
```
CCI = (TP - MA(TP, n)) / (0.015 × MD)
TP = (High + Low + Close) / 3
```

**参数:** CCI14

**解读:**
- CCI > +100 → 超买
- CCI < -100 → 超卖
- CCI 穿越 ±100 → 交易信号

### BIAS 乖离率

**公式:**
```
BIAS(n) = (Close - MA(n)) / MA(n) × 100%
```

**参数:** BIAS6, BIAS12, BIAS24

**解读:**
- 正乖离过大 → 回调风险
- 负乖离过大 → 反弹机会

### WR (Williams %R)

**公式:**
```
WR = (High(n) - Close) / (High(n) - Low(n)) × (-100)
```

**参数:** WR14

**解读:**
- WR > -20 → 超买
- WR < -80 → 超卖

## 量能指标

### VOL 成交量

**解读:**
- 价涨量增 → 健康上涨
- 价跌量增 → 抛压沉重
- 价涨量缩 → 上涨乏力
- 价跌量缩 -> 抛压减轻

### OBV (On-Balance Volume) 能量潮

**公式:**
```
If Close > Close(yesterday): OBV = OBV(yesterday) + Volume
If Close < Close(yesterday): OBV = OBV(yesterday) - Volume
```

**解读:**
- OBV 上升 → 资金流入
- OBV 下降 → 资金流出
- OBV 背离 → 趋势预警

### VR (Volume Ratio) 成交量比率

**公式:**
```
VR = (AV + UV) / (AV + DV + UV)
```

**解读:**
- VR > 400 → 强势
- VR 40-70 → 弱势
- VR < 40 → 严重超卖

### EMV (Ease of Movement) 简易波动

**公式:**
```
EMV = (High + Low)/2 - (High(yesterday) + Low(yesterday))/2
     × Volume差 / Volume和
```

**解读:**
- EMV > 0 → 买方占优
- EMV < 0 → 卖方占优

## 动量指标

### MOM (Momentum) 动量

**公式:**
```
MOM = Close - Close(n)
```

**解读:**
- MOM > 0 → 上涨动量
- MOM < 0 → 下跌动量

### ROC (Rate of Change) 变化率

**公式:**
```
ROC = (Close - Close(n)) / Close(n) × 100%
```

**解读:**
- ROC > 0 → 上涨趋势
- ROC < 0 → 下跌趋势

### ARBR (Altitude Ratio) 人气意愿

**公式:**
```
AR = (High - Open) Σ / (Open - Low) Σ × 100
BR = (High - Close(yesterday)) Σ / (Close(yesterday) - Low) Σ × 100
```

**解读:**
- AR > 150 → 活跃
- AR < 50 → 萎缩
- BR > 300 → 过热
- BR < 50 → 过冷

### CR (Capability Ratio) 能力指标

**公式:**
```
CR = (High - Close(yesterday)) Σ / (Close(yesterday) - Low) Σ × 100
```

**解读:**
- CR > 400 → 过买
- CR < 40 → 过卖
- CR 穿越 MA → 信号

## 评分模型

### 综合评分

```
综合分 = 趋势分 × 40% + 动量分 × 30% + 资金分 × 20% + 情绪分 × 10%
```

#### 趋势分 (40%)
- MA 排列: 多头 +20, 空头 -20
- MACD: 金叉 +10, 死叉 -10
- BOLL: 上轨 +5, 中轨 0, 下轨 -5
- 价格趋势: 上涨 +5, 下跌 -5

#### 动量分 (30%)
- RSI: 按位置打分 0-20
- KDJ: J值打分 0-15
- MOM: 正负打分 ±10
- ROC: 正负打分 ±5

#### 资金分 (20%)
- OBV: 趋势 ±10
- 成交量: 放量 +5, 缩量 -5
- 换手率: 活跃度 ±5

#### 情绪分 (10%)
- 涨跌天数: 连续 ±5
- 振幅: 波动性 ±5

### 评级标准

| 分数 | 等级 | 建议 | 颜色 |
|------|------|------|------|
| 90-100 | 极强 | 强力买入 | 🟢🟢 |
| 80-90 | 强 | 买入 | 🟢 |
| 70-80 | 偏强 | 逢低买入 | 🟡🟢 |
| 60-70 | 中性 | 观望 | 🟡 |
| 50-60 | 偏弱 | 谨慎 | 🟡🔴 |
| 40-50 | 弱 | 观望 | 🔴 |
| 0-40 | 极弱 | 规避 | 🔴🔴 |

## 形态识别

### K线形态

**看涨形态:**
- 锤子线
- 吞噬形态
- 刺透形态
- 早晨之星

**看跌形态:**
- 上吊线
- 乌云盖顶
- 黄昏之星
- 三只乌鸦

### 多K线组合

**反转形态:**
- 双底/双顶
- 头肩底/头肩顶
- 圆弧底/圆弧顶

**持续形态:**
- 上升三角形
- 下降三角形
- 矩形整理

## 参考资料

- [Technical Analysis from A to Z](https://www.investopedia.com/terms/t/technicalanalysis.asp)
- [Japanese Candlestick Charting](https://www.investopedia.com/trading/candlestick-charting-1485983)
- [MACD Analysis](https://www.school.stockcharts.com/doku.php?id=technical_indicators:moving_averages:macd)

---

*最后更新: 2026-02-19*
