# Stock Analysis Skill - Usage Examples

## Example 1: Single Stock Analysis

### User Request
```
分析一下贵州茅台 (600519) 最近 60 天的走势，并给出操作建议
```

### Agent Response
```
Let me analyze Guizhou Moutai (600519) for the past 60 days...

Fetching data from AkShare...
Calculating technical indicators...
Generating charts...

📊 **Stock Analysis Report: 贵州茅台 (600519)**

## Current Price
¥1,780.50 (+2.3% today)

## Technical Indicators

### Trend
- MA5: 1,785.30 (↑)
- MA20: 1,765.20 (↑)
- MA60: 1,740.80 (↑)
- Signal: Bullish alignment

### MACD
- DIF: 12.50
- DEA: 10.20
- Signal: Golden cross 🟢

### KDJ
- K: 75, D: 70, J: 85
- Signal: Strong momentum

### RSI
- RSI6: 68
- Signal: Slightly overbought

## Composite Score: 79/100 🟡

### Recommendations
- **Short-term**: Wait for pullback
- **Medium-term**: Buy on dips near MA20
- **Long-term**: Hold

## Charts Generated
- kline_ma_600519.png
- macd_600519.png
- kdj_600519.png
```

---

## Example 2: Multi-Stock Comparison

### User Request
```
对比分析 贵州茅台、五粮液、泸州老窖最近 90 天的表现
```

### Agent Response
```
Comparing three liquor stocks over 90 days...

Fetching data for 600519, 000858, 000568...

📊 **Comparison Report: 白酒三巨头**

| Stock | Code | Score | Trend | Momentum | Money Flow | Recommendation |
|-------|------|-------|-------|----------|------------|----------------|
| 贵州茅台 | 600519 | 79 | 🟢 85 | 🟡 72 | 🟢 90 | 🟡 Hold |
| 五粮液 | 000858 | 72 | 🟢 78 | 🟡 65 | 🟡 68 | 🟡 Hold |
| 泸州老窖 | 000568 | 85 | 🟢 88 | 🟢 82 | 🟢 85 | 🟢 Buy |

**Summary:** 泸州老窖 shows the strongest momentum and money flow.
贵州茅台 has solid fundamentals but slightly elevated valuations.
```

---

## Example 3: Technical Indicator Query

### User Request
```
600519 的 MACD 和 KDJ 当前状态是什么？
```

### Agent Response
```
Checking MACD and KDJ indicators for 600519...

📈 **MACD (12, 26, 9)**
- DIF: 12.50
- DEA: 10.20
- MACD Bar: +2.30
- **Signal**: Golden cross (DIF > DEA) 🟢
- **Trend**: Bullish

📈 **KDJ (9, 3, 3)**
- K: 75
- D: 70
- J: 85
- **Signal**: Strong uptrend (K > D, J > 100) 🟢
- **Momentum**: High

**Overall**: Both indicators show bullish momentum. Short-term caution
needed as J value indicates potential overbought condition.
```

---

## Example 4: Scoring and Recommendation

### User Request
```
给 600547 山东黄金进行技术评分，并给出买入/持有/卖出建议
```

### Agent Response
```
Analyzing 600547 (Shandong Gold)...

📊 **Technical Analysis Report: 山东黄金 (600547)**

## Composite Score Breakdown

| Dimension | Score | Weight | Level | Grade |
|-----------|-------|--------|-------|-------|
| Trend | 82/100 | 40% | 🟢 Strong | Buy |
| Momentum | 68/100 | 30% | 🟡 Neutral | Hold |
| Money Flow | 75/100 | 20% | 🟢 Inflow | Buy |
| Sentiment | 60/100 | 10% | 🟡 Neutral | Hold |
| **Composite** | **74/100** | **-** | **🟡 Hold** | **Hold** |

## Key Levels
- **Support**: ¥35.20 (MA20), ¥33.80 (MA60)
- **Resistance**: ¥38.50 (recent high), ¥40.00 (psychological)

## Recommendation

### Short-term (1-5 days): 🟡 **Watch**
Wait for pullback to support levels before entering.

### Medium-term (5-20 days): 🟢 **Accumulate**
Gradually build position on dips near MA20.

### Long-term (20+ days): 🟢 **Hold**
Gold sector outlook remains positive due to safe-haven demand.

## Risk Warning
⚠️ Volatility may increase due to global economic uncertainty.
⚠️ Watch USD/CNY rate impact on gold prices.
```

---

## Example 5: Custom Indicator Query

### User Request
```
查看 600519 的布林带位置，判断是否超买
```

### Agent Response
```
Analyzing Bollinger Bands for 600519...

📊 **Bollinger Bands Analysis (20, 2)**

## Current Values
- Upper Band: ¥1,820.30
- Middle Band (MA20): ¥1,768.50
- Lower Band: ¥1,716.70
- Current Price: ¥1,780.50

## Position Analysis
```
┌─────────────────────────────────────┐
│           Upper Band: 1,820.30      │
│                                     │
│         Current: 1,780.50 📍        │ ← 73% position
│                                     │
│         Middle: 1,768.50            │
│                                     │
│           Lower: 1,716.70           │
└─────────────────────────────────────┘
```

## %B Indicator
- %B = (Price - Lower) / (Upper - Lower) = 0.73
- Interpretation: **Upper middle range**

## Interpretation
🟡 **Neutral to Slightly Bullish**
- Price is in upper half of the band
- Not yet overbought (%B < 0.8)
- Watch for break above upper band (overbought signal)
- Support at middle band (1,768.50)

## Bandwidth
- Bandwidth = (Upper - Lower) / Middle = 5.8%
- Squeeze detected → Low volatility
- Potential breakout expected soon
```

---

## Example 6: Error Handling

### User Request
```
分析 999999 这个股票
```

### Agent Response
```
Attempting to fetch data for 999999...

❌ **Error**: Stock code 999999 not found or invalid.

**Possible issues:**
1. Stock code doesn't exist
2. Market not open (check trading hours)
3. Network connection problem

**Suggestions:**
- Verify stock code is correct (6-digit for A-shares)
- Try a different stock code
- Check if market is open (Mon-Fri 9:30-15:00 CST)
- Try again in a few moments

Would you like me to try a different stock?
```

---

## Advanced Examples

### Batch Analysis
```
批量分析这些股票: 600519, 000858, 000568, 600809
```

### Sector Analysis
```
分析白酒行业最近的表现，找出龙头股
```

### Backtest Strategy
```
回测金叉策略在贵州茅台上的表现
```

---

## Tips for Best Results

1. **Use 6-digit codes**: For A-shares, use the 6-digit code (e.g., 600519)
2. **Specify period**: Default is 60 days, but you can ask for 30/90/180 days
3. **Compare stocks**: Use "对比" or "compare" to analyze multiple stocks
4. **Specific indicators**: Mention specific indicators if you only need those
5. **Timeframe matters**: Clarify short/medium/long term focus
