# Curl-Based EastMoney API (Proxy-Bypass)

Use when akshare fails due to macOS system proxy (ClashX etc. on 127.0.0.1:7890).

## Real-time Quote

```
GET https://push2.eastmoney.com/api/qt/stock/get
  ?secid=1.{code}
  &ut=fa5fd1943c7b386f172d6893dbfd32bb
  &fields=f43,f44,f45,f46,f47,f48,f50,f51,f57,f58,f60,f116,f162,f167,f168,f169,f170,f171
```

curl: `curl -s -x "" "https://push2.eastmoney.com/api/qt/stock/get?secid=1.600597&ut=fa5fd1943c7b386f172d6893dbfd32bb&fields=f43,f44,f45,f46,f47,f48,f50,f51,f57,f58,f60,f116"`

Key fields: f43=price, f44=max, f45=min, f46=open, f47=volume, f48=amount, f50=quantityRatio, f57=code, f58=name, f60=lastClose, f116=turnover

## K-Line History (日K)

```
GET https://push2his.eastmoney.com/api/qt/stock/kline/get
  ?fields1=f1,f2,f3,f4,f5,f6
  &fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f116
  &ut=7eea3edcaed734bea9cbfc24409ed989
  &klt=101        (101=daily, 102=weekly, 103=monthly)
  &fqt=1          (1=前复权, 0=不复权, 2=后复权)
  &secid={market}.{code}
  &beg=YYYYMMDD
  &end=YYYYMMDD
```

curl: `curl -s -x "" "https://push2his.eastmoney.com/api/qt/stock/kline/get?fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f116&ut=7eea3edcaed734bea9cbfc24409ed989&klt=101&fqt=1&secid=1.600597&beg=20260401&end=20260526"`

**Market mapping:** 上证=1, 深证=0, 创业板=0 (secid=1.600597, secid=0.000002)

## K-Line Data Format

Each kline entry: `date,open,close,high,low,volume,amount,amplitude,pct_chg,change,turnover`

- volume: 手 (1手=100股)
- amount: 元
- amplitude: % (振幅)
- pct_chg: % (涨跌幅)
- change: 元 (涨跌额)
- turnover: % (换手率)

## All Stocks Spot List (for batch)

```
GET https://82.push2.eastmoney.com/api/qt/clist/get
  ?pn=1&pz=100&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281
  &fltt=2&invt=2&fid=f12&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048
  &fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152
```

## Index Spot

```
GET https://48.push2.eastmoney.com/api/qt/clist/get
  ?pn=1&pz=100&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281
  &fltt=2&invt=2&fid=f12&fs=m:1+t:1
  &fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f33,f11,f62,f128,f136,f115,f152
```

## Bypass Important Rule

Always use `-x ""` in curl to bypass the macOS system proxy. Without it, curl defaults to the system proxy at 127.0.0.1:7890 which blocks eastmoney.com connections.

In Python, use `subprocess.run(["curl", "-s", "--connect-timeout", "10", "-x", "", url], ...)` — do NOT use `requests` or `urllib` directly for eastmoney calls on this machine.
