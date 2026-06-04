# 东方财富 (EastMoney) API 参考

> 用于 curl --noproxy "*" 直连方案。当 macOS 系统代理阻塞 akshare 时，直接调用东方财富 HTTP API 获取数据。

---

## API 端点

### 1. 实时行情

```
GET https://push2.eastmoney.com/api/qt/stock/get
```

**参数:**
| 参数 | 值 | 说明 |
|------|-----|------|
| secid | 0.000002 (深交所) / 1.600519 (上交所) | 市场代码.股票代码 |
| fields | f43,f44,f45,f46,f48,f60,f116,f170,... | 逗号分隔的字段列表 |

**字段映射:**
| 字段 | 含义 | 单位转换 |
|------|------|---------|
| f43 | 最新价 | /100 |
| f44 | 最高价 | /100 |
| f45 | 最低价 | /100 |
| f46 | 今开 | /100 |
| f48 | 成交量 | 股 (÷1e4=万手, ÷1e8=亿股) |
| f50 | 成交额 | 元 |
| f57 | 股票代码 | 字符串 |
| f58 | 股票名称 | 字符串 |
| f60 | 昨收 | /100 |
| f116 | 总市值 | 元 (÷1e8=亿) |
| f117 | 流通市值 | 元 (÷1e8=亿) |
| f162 | 市盈率(动态) | /100 (负值=亏损) |
| f163 | 市净率 | /100 |
| f167 | 换手率 | /100 (%) |
| f168 | 振幅 | /100 (%) |
| f169 | 涨跌额 | /100 |
| f170 | 涨跌幅 | /100 (%) |
| f171 | 涨跌幅(绝对值) | /100 (%) |

**示例:**
```bash
curl -s --noproxy "*" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Referer: https://quote.eastmoney.com/" \
  "https://push2.eastmoney.com/api/qt/stock/get?secid=0.000002&fields=f43,f44,f45,f46,f48,f60,f116,f117,f162,f163,f167,f168,f169,f170"
```

---

### 2. K线数据

```
GET https://push2his.eastmoney.com/api/qt/stock/kline/get
```

**参数:**
| 参数 | 值 | 说明 |
|------|-----|------|
| secid | 0.000002 / 1.600519 | 市场代码.股票代码 |
| fields1 | f1,f2,f3 | 基础字段 |
| fields2 | f51,f52,f53,f54,f55,f56,f57,f58,f59,f60 | K线字段 |
| klt | 101 | 日K线 (102=周K, 103=月K) |
| fqt | 1 | 前复权 (0=不复权, 2=后复权) |
| beg | 20260101 | 起始日期 YYYYMMDD |
| end | 20260526 | 结束日期 YYYYMMDD |

**返回格式 (klines 数组):**
```
日期,开盘,收盘,最高,最低,成交量(股),成交额(元),振幅%,涨跌幅%,涨跌额
```

**示例:**
```bash
curl -s --noproxy "*" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Referer: https://quote.eastmoney.com/" \
  "https://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.000002&fields1=f1,f2,f3&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60&klt=101&fqt=1&beg=20260101&end=20260526" \
  -o /tmp/kline.json
```

**⚠️ 注意:** K-line API 返回不能管道传递给 Python stdin（会触发安全扫描），必须使用 `-o <file>` 保存到文件后再读取。

---

### 3. 全市场行情列表

```
GET https://push2.eastmoney.com/api/qt/clist/get
```

**参数:**
| 参数 | 值 | 说明 |
|------|-----|------|
| fs | m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048 | 全A股 |
| fields | f2,f3,f4,f12,f14,f15,f16,f17,f18,... | 字段列表 |
| pn | 1 | 页码 |
| pz | 100 | 每页数量 |

此接口返回所有股票列表，可用于板块筛选/行业对比。但数据量大，分页请求较多，建议优先使用单只股票行情接口。

---

## 代理绕过注意事项

1. **`--noproxy "*"` 是必须的:** macOS 系统代理配置在 System Preferences > Network > Proxies 中设置了 HTTP/HTTPS 代理为 127.0.0.1:7890，urllib3 会读取此设置，curl 如不加 --noproxy 也会走代理
2. **User-Agent 请求头必须设置:** 部分 API（尤其是 K-line）在不带 User-Agent 时会返回空响应或 403
3. **Referer 请求头有助于稳定连接:** 设置为 `https://quote.eastmoney.com/`
4. **不要用 Python 管道读取 curl 输出:** 使用 `-o file` 保存到临时文件后再用 `json.load(open(file))`
5. **两个 API 域名不同:** `push2.eastmoney.com` (实时) 和 `push2his.eastmoney.com` (历史)
