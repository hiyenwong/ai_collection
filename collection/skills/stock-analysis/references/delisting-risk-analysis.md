# A股退市风险分析框架

当用户询问某只股票「是否有退市风险」或「会不会退市」时，使用此框架系统评估。

## 退市类型与检查清单

### 1. 面值退市（最快触发）
- **规则：** 连续20个交易日收盘价 < **1元**
- **检查：** 当前股价是否接近1元
- **风险等级：**
  - 🟢 股价 > 3元：安全
  - 🟡 股价 1-3元：关注，仍在安全线之上
  - 🔴 股价 < 1.2元：高风险，随时可能触发

### 2. 市值退市
- **规则：** 连续20个交易日总市值 < **3亿元**
- **检查：** 当前市值（股价 × 总股本）
- **风险等级：**
  - 🟢 市值 > 10亿：安全
  - 🟡 市值 3-10亿：关注
  - 🔴 市值 < 3.5亿：高风险

### 3. 财务退市（*ST → 退市流程）
- **净利润为负 + 营收 < 1亿元**（交叉适用）
- **净资产为负**（触发*ST，次年仍为负则退市）
- **审计意见为无法表示/否定意见**
- **检查：**
  - 市盈率(动) 是否为负（亏损）
  - 每股净资产是否为正
  - 营业收入规模是否远大于1亿红线

### 4. 重大违法强制退市
- 欺诈发行、重大信息披露违法等
- 非常规风险，需查看近期公告

### 5. 主动退市（极少见）
- 公司主动申请私有化/退市
- 通常伴随要约收购

## 数据获取方法

使用东方财富API（需curl绕过代理，见 `references/curl-eastmoney-api.md`）：

### 实时财务/估值数据
```python
import subprocess, json

def get_realquote(code, market=1):
    """获取实时行情包括财务指标"""
    url = f"https://push2.eastmoney.com/api/qt/stock/get?secid={market}.{code}&ut=fa5fd1943c7b386f172d6893dbfd32bb&fields=f43,f44,f45,f46,f47,f48,f50,f51,f57,f58,f60,f116,f162,f167,f168,f169,f170,f171,f292"
    result = subprocess.run(["curl", "-s", "--connect-timeout", "10", "-x", "", url],
                          capture_output=True, text=True, timeout=10)
    data = json.loads(result.stdout)
    return data.get("data", {})

# 关键字段：
d = get_realquote("000002", 0)
price = d.get("f43", 0) / 100        # 最新价
pe_dynamic = d.get("f162", "N/A")    # 市盈率(动)，负值=亏损
pb = d.get("f167", "N/A")            # 市净率
nav_per_share = d.get("f292", 0)     # 每股净资产
market_cap = d.get("f116", 0)        # 总市值
```

**注意：** 深证/创业板 `market=0`，上证 `market=1`。某些字段值以整数形式返回（乘以100），需确认实际精度。

### 日K线价格走势
```python
def get_price_trend(code, market=1, months=6):
    from datetime import datetime, timedelta
    end = datetime.now().strftime("%Y%m%d")
    start = (datetime.now() - timedelta(days=months*31)).strftime("%Y%m%d")
    url = (f"https://push2his.eastmoney.com/api/qt/stock/kline/get?"
           f"fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f116"
           f"&ut=7eea3edcaed734bea9cbfc24409ed989&klt=101&fqt=1"
           f"&secid={market}.{code}&beg={start}&end={end}")
    result = subprocess.run(["curl", "-s", "--connect-timeout", "10", "-x", "", url],
                          capture_output=True, text=True, timeout=15)
    data = json.loads(result.stdout)
    return data.get("data", {}).get("klines", [])
```

## 分析报告输出模板

```
## 退市风险分析：{名称} ({代码})

### 基础检查
| 检查项 | 当前值 | 退市门槛 | 风险 |
|--------|--------|---------|:---:|
| 股价 | {price}元 | < 1元 | 🟢/🟡/🔴 |
| 总市值 | {mcap}亿 | < 3亿 | 🟢/🟡/🔴 |
| 市盈率(动) | {pe} | 负=亏损 | 🟢/🟡/🔴 |
| 每股净资产 | {nav}元 | 负→*ST | 🟢/🟡/🔴 |
| 营收规模 | {rev}亿 | < 1亿 | 🟢/🟡/🔴 |

### 综合判断
{summary}
```

## 行业特定风险参考

| 行业 | 常见非退市风险 |
|------|--------------|
| 房地产 | 债务违约/展期、ST、国资救援预期 |
| 生物医药 | 研发失败、监管否决 |
| ST/*ST公司 | 保壳动机强（卖资产、重组），需警惕 |

## 关键区分

- **退市风险** = 触及面值/市值/财务/违法退市红线的概率
- **财务危机/债务风险** ≠ 退市风险
  - 例：万科A股价3.39元、市值404亿，远离退市标准，但债务压力大
  - 不能因为股价暴跌就认定「有退市风险」
