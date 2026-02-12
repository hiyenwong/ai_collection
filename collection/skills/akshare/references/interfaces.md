# AkShare Interface Catalog

This document provides a comprehensive catalog of AkShare interfaces organized by category.

## Table of Contents

- [Stock Market Data](#stock-market-data)
- [Futures Market Data](#futures-market-data)
- [Fund Data](#fund-data)
- [Macro Economic Data](#macro-economic-data)
- [Bond Market Data](#bond-market-data)
- [Foreign Exchange Data](#foreign-exchange-data)
- [Cryptocurrency Data](#cryptocurrency-data)
- [Option Data](#option-data)
- [Other Data](#other-data)

---

## Stock Market Data

### A-Share Data (A股数据)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_zh_a_hist` | A-share historical data (daily) | East Money |
| `stock_zh_a_hist_em` | A-share historical data (East Money) | East Money |
| `stock_zh_a_hist_tx` | A-share historical data (Tencent) | Tencent |
| `stock_zh_a_spot` | Real-time A-share quotes | Sina |
| `stock_zh_a_spot_em` | Real-time A-share quotes | East Money |
| `stock_sh_a_spot_em` | Shanghai A-share real-time quotes | East Money |
| `stock_sz_a_spot_em` | Shenzhen A-share real-time quotes | East Money |
| `stock_bj_a_spot_em` | Beijing A-share real-time quotes | East Money |
| `stock_new_a_spot_em` | New stock real-time quotes | East Money |
| `stock_kc_a_spot_em` | STAR Market real-time quotes | East Money |
| `stock_zh_b_spot_em` | B-share real-time quotes | East Money |
| `stock_zh_a_minute` | A-share intraday minute data | Sina |
| `stock_zh_a_hist_min_em` | A-share minute historical data | East Money |
| `stock_zh_a_hist_pre_min_em` | A-share pre-market minute data | East Money |
| `stock_zh_a_cdr_daily` | A-share CDR historical data | East Money |
| `stock_zh_ah_spot` | A+H stock real-time quotes | East Money |
| `stock_zh_ah_daily` | A+H stock historical data | East Money |
| `stock_zh_ah_name` | A+H stock code list | East Money |

### Hong Kong Stock Data (港股数据)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_hk_spot` | Hong Kong stock historical data | Sina |
| `stock_hk_daily` | Hong Kong stock real-time quotes | Sina |
| `stock_hk_spot_em` | Hong Kong stock real-time quotes | East Money |
| `stock_hk_main_board_spot_em` | Hong Kong main board quotes | East Money |
| `stock_hk_hist_min_em` | Hong Kong stock minute data | East Money |
| `stock_hk_daily_sina` | Hong Kong stock historical data | Sina |
| `stock_hk_index_spot_sina` | Hong Kong index real-time quotes | Sina |
| `stock_hk_index_daily_sina` | Hong Kong index historical data | Sina |
| `stock_hk_index_spot_em` | Hong Kong index real-time quotes | East Money |
| `stock_hk_index_daily_em` | Hong Kong index historical data | East Money |

### US Stock Data (美股数据)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_us_daily` | US stock historical data | Sina |
| `stock_us_spot` | US stock quotes | Sina |
| `get_us_stock_name` | Get all US stock symbols | Sina |
| `stock_us_hist_min_em` | US stock minute data | East Money |
| `stock_us_pink_spot_em` | US pink sheet stocks | East Money |
| `stock_us_famous_spot_em` | Famous US stocks | East Money |
| `stock_financial_us_report_em` | US stock financial statements | East Money |
| `stock_financial_us_analysis_indicator_em` | US stock financial indicators | East Money |
| `stock_us_valuation_baidu` | US stock valuation data | Baidu |

### Stock Index Data (股票指数数据)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_zh_index_daily` | Stock index historical data | East Money |
| `stock_zh_index_spot_em` | Stock index real-time quotes | East Money |
| `stock_zh_index_daily_em` | Stock index historical data | East Money |
| `stock_zh_index_daily_tx` | Stock index historical data (Tencent) | Tencent |
| `stock_zh_index_spot_sina` | Stock index real-time quotes (Sina) | Sina |
| `stock_zh_index_hist_csindex` | CSI Index historical data | CSI |
| `stock_zh_index_value_csindex` | CSI Index valuation | CSI |
| `index_zh_a_hist` | China stock index historical data | East Money |
| `index_zh_a_hist_min_em` | China stock index minute data | East Money |
| `index_all_cni` | China Securities Index (all) | CNI |
| `index_hist_cni` | China Securities Index history | CNI |
| `index_detail_cni` | China Securities Index details | CNI |
| `index_realtime_sw` | SW Index real-time quotes | SW |
| `index_hist_sw` | SW Index historical data | SW |
| `index_min_sw` | SW Index minute data | SW |
| `index_component_sw` | SW Index constituents | SW |

### Stock Board Data (股票板块数据)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_board_industry_name_em` | Industry board names | East Money |
| `stock_board_industry_spot_em` | Industry board real-time quotes | East Money |
| `stock_board_industry_hist_em` | Industry board historical data | East Money |
| `stock_board_industry_hist_min_em` | Industry board minute data | East Money |
| `stock_board_industry_cons_em` | Industry board constituents | East Money |
| `stock_board_concept_name_em` | Concept board names | East Money |
| `stock_board_concept_spot_em` | Concept board real-time quotes | East Money |
| `stock_board_concept_hist_em` | Concept board historical data | East Money |
| `stock_board_concept_hist_min_em` | Concept board minute data | East Money |
| `stock_board_concept_cons_em` | Concept board constituents | East Money |

---

## Futures Market Data (期货市场数据)

### Exchange Futures Data (交易所期货数据)

| Function | Description | Source |
|----------|-------------|--------|
| `get_cffex_daily` | CFFEX daily trading data | CFFEX |
| `get_cffex_rank_table` | CFFEX top 20 member position data | CFFEX |
| `get_czce_daily` | CZCE daily trading data | CZCE |
| `get_rank_table_czce` | CZCE top 20 member position data | CZCE |
| `get_dce_daily` | DCE daily trading data | DCE |
| `get_dce_rank_table` | DCE top 20 member position data | DCE |
| `get_shfe_daily` | SHFE daily trading data | SHFE |
| `get_shfe_rank_table` | SHFE top 20 member position data | SHFE |
| `get_ine_daily` | INE daily trading data | INE |
| `get_gfex_daily` | GFEX daily trading data | GFEX |
| `futures_settlement_price_sgx` | SGX futures settlement prices | SGX |

### Futures Quotes (期货行情)

| Function | Description | Source |
|----------|-------------|--------|
| `futures_zh_realtime` | Domestic futures real-time quotes | Sina |
| `futures_zh_spot` | Domestic futures spot quotes | Sina |
| `futures_zh_minute_sina` | Domestic futures minute data | Sina |
| `futures_foreign_realtime` | Foreign futures real-time quotes | Sina |
| `futures_foreign_hist` | Foreign futures historical data | Sina |
| `futures_foreign_detail` | Foreign futures contract details | Sina |
| `futures_hist_em` | Futures historical data | East Money |
| `futures_global_spot_em` | International futures real-time quotes | East Money |
| `futures_global_hist_em` | International futures historical data | East Money |

### Futures Position Data (期货持仓数据)

| Function | Description | Source |
|----------|-------------|--------|
| `futures_hold_pos_sina` | Futures position data | Sina |
| `get_rank_sum` | Top 5, 10, 15, 20 member positions | Aggregate |
| `get_rank_sum_daily` | Daily member position rankings | Aggregate |
| `futures_dce_position_rank` | DCE member position rankings | DCE |

### Futures Roll Yield (期货展期收益率)

| Function | Description | Source |
|----------|-------------|--------|
| `get_roll_yield_bar` | Futures roll yield bar chart | Aggregate |
| `get_roll_yield` | Futures roll yield data | Aggregate |

### Futures Receipt (期货仓单)

| Function | Description | Source |
|----------|-------------|--------|
| `get_receipt` | Commodity registered receipts data | Aggregate |
| `get_receipt_date` | Futures receipt validity period | Aggregate |
| `futures_warehouse_receipt_czce` | CZCE warehouse receipt data | CZCE |
| `futures_warehouse_receipt_shfe` | SHFE warehouse receipt data | SHFE |
| `futures_warehouse_receipt_dce` | DCE warehouse receipt data | DCE |
| `futures_warehouse_receipt_gfex` | GFEX warehouse receipt data | GFEX |
| `futures_stock_shfe_js` | SHFE inventory weekly report | SHFE |

### Futures Contract Info (期货合约信息)

| Function | Description | Source |
|----------|-------------|--------|
| `futures_contract_info_shfe` | SHFE futures contract info | SHFE |
| `futures_contract_info_ine` | INE futures contract info | INE |
| `futures_contract_info_dce` | DCE futures contract info | DCE |
| `futures_contract_info_czce` | CZCE futures contract info | CZCE |
| `futures_contract_info_gfex` | GFEX futures contract info | GFEX |
| `futures_contract_info_cffex` | CFFEX futures contract info | CFFEX |
| `futures_contract_detail` | Futures contract details | Sina |
| `futures_contract_detail_em` | Futures contract details | East Money |
| `futures_comm_info` | Futures commission info | Aggregate |
| `futures_fees_info` | Futures transaction fees | Aggregate |

---

## Fund Data (基金数据)

### Open-end Funds (开放式基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_name_em` | Fund basic information | East Money |
| `fund_open_fund_daily_em` | Open-end fund real-time data | East Money |
| `fund_open_fund_info_em` | Open-end fund historical data | East Money |
| `fund_purchase_em` | Fund purchase status | East Money |
| `fund_value_estimation_em` | Fund valuation | East Money |
| `fund_open_fund_rank_em` | Open-end fund rankings | East Money |

### ETF Funds (ETF基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_etf_fund_daily_em` | ETF real-time data | East Money |
| `fund_etf_fund_info_em` | ETF historical data | East Money |
| `fund_etf_spot_em` | ETF real-time quotes | East Money |
| `fund_etf_hist_em` | ETF historical data | East Money |
| `fund_etf_hist_min_em` | ETF minute data | East Money |
| `fund_etf_spot_ths` | ETF real-time quotes | Tonghuashun |
| `fund_etf_dividend_sina` | ETF dividend data | Sina |
| `fund_em_exchange_rank` | Exchange-traded fund rankings | East Money |
| `fund_etf_scale_szse` | Shenzhen ETF fund scale | SZSE |
| `fund_etf_scale_sse` | Shanghai ETF fund scale | SSE |

### Money Funds (货币基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_money_fund_daily_em` | Money fund real-time data | East Money |
| `fund_money_fund_info_em` | Money fund historical data | East Money |
| `fund_em_money_rank` | Money fund rankings | East Money |

### Financial Funds (理财基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_financial_fund_daily_em` | Financial fund real-time data | East Money |
| `fund_financial_fund_info_em` | Financial fund historical data | East Money |
| `fund_em_lcx_rank` | Financial fund rankings | East Money |

### Graded Funds (分级基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_graded_fund_daily_em` | Graded fund real-time data | East Money |
| `fund_graded_fund_info_em` | Graded fund historical data | East Money |

### LOF Funds (LOF基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_lof_spot_em` | LOF real-time quotes | East Money |
| `fund_lof_hist_em` | LOF historical data | East Money |
| `fund_lof_hist_min_em` | LOF minute data | East Money |

### Fund Manager (基金经理)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_manager_em` | Fund manager directory | East Money |

### Fund Scale (基金规模)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_aum_em` | Fund company scale rankings | East Money |
| `fund_aum_trend_em` | Fund market management scale trend | East Money |
| `fund_aum_hist_em` | Fund market management scale history | East Money |
| `fund_scale_open_sina` | Open-end fund scale | Sina |
| `fund_scale_close_sina` | Closed-end fund scale | Sina |
| `fund_scale_structured_sina` | Structured sub-fund scale | Sina |

### New Funds (新发基金)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_new_found_em` | New fund listings | East Money |

### Fund Ratings (基金评级)

| Function | Description | Source |
|----------|-------------|--------|
| `fund_rating_all` | Fund rating summary | Aggregate |
| `fund_rating_sh` | Shanghai Securities rating | Shanghai Securities |
| `fund_rating_zs` | China Merchants Securities rating | CMS |
| `fund_rating_ja` | Ji'anxin rating | Ji'anxin |

---

## Macro Economic Data (宏观经济数据)

### China Macro Data (中国宏观经济)

| Function | Description | Source |
|----------|-------------|--------|
| `macro_china_gdp_yearly` | China GDP yearly | Jin10 |
| `macro_china_gdp` | China GDP | Jin10 |
| `macro_china_cpi_yearly` | China CPI yearly | Jin10 |
| `macro_china_cpi_monthly` | China CPI monthly | Jin10 |
| `macro_china_cpi` | China CPI | Jin10 |
| `macro_china_ppi_yearly` | China PPI yearly | Jin10 |
| `macro_china_ppi` | China PPI | Jin10 |
| `macro_china_pmi_yearly` | China official manufacturing PMI | Jin10 |
| `macro_china_cx_pmi_yearly` | China Caixin manufacturing PMI | Jin10 |
| `macro_china_cx_services_pmi_yearly` | China Caixin services PMI | Jin10 |
| `macro_china_non_man_pmi` | China official non-manufacturing PMI | Jin10 |
| `macro_china_m2_yearly` | China M2 money supply yearly | Jin10 |
| `macro_china_shibor_all` | China SHIBOR | Jin10 |
| `macro_china_lpr` | China loan prime rate | Jin10 |
| `macro_china_fx_reserves_yearly` | China foreign exchange reserves | Jin10 |
| `macro_china_exports_yoy` | China exports year-over-year | Jin10 |
| `macro_china_imports_yoy` | China imports year-over-year | Jin10 |
| `macro_china_trade_balance` | China trade balance | Jin10 |
| `macro_china_industrial_production_yoy` | China industrial production YoY | Jin10 |
| `macro_china_unemployment` | China unemployment rate | NBS |
| `macro_china_urban_unemployment` | China urban unemployment rate | NBS |
| `macro_china_shrzgm` | China social financing scale | NBS |
| `macro_china_reserve_requirement_ratio` | Reserve requirement ratio | PBOC |
| `macro_china_consumer_goods_retail` | Retail sales | NBS |
| `macro_china_supply_of_money` | Money supply | NBS |
| `macro_china_foreign_exchange_gold` | Foreign exchange and gold reserves | NBS |
| `macro_china_bank_financing` | Bank wealth management product issuance | NBS |
| `macro_china_new_financial_credit` | New credit data | NBS |

### US Macro Data (美国宏观经济)

| Function | Description | Source |
|----------|-------------|--------|
| `macro_usa_gdp_monthly` | US GDP | Jin10 |
| `macro_usa_cpi_monthly` | US CPI monthly | Jin10 |
| `macro_usa_cpi_yoy` | US CPI year-over-year | East Money |
| `macro_usa_core_cpi_monthly` | US Core CPI monthly | Jin10 |
| `macro_usa_ppi` | US PPI | Jin10 |
| `macro_usa_core_ppi` | US Core PPI | Jin10 |
| `macro_usa_unemployment_rate` | US unemployment rate | Jin10 |
| `macro_usa_job_cuts` | US job cuts | Jin10 |
| `macro_usa_non_farm` | US non-farm payrolls | Jin10 |
| `macro_usa_adp_employment` | US ADP employment | Jin10 |
| `macro_usa_retail_sales` | US retail sales | Jin10 |
| `macro_usa_core_pce_price` | US Core PCE price | Jin10 |
| `macro_usa_trade_balance` | US trade balance | Jin10 |
| `macro_usa_pmi` | US Markit manufacturing PMI | Jin10 |
| `macro_usa_ism_pmi` | US ISM manufacturing PMI | Jin10 |
| `macro_usa_nahb_house_market_index` | US NAHB housing market index | Jin10 |
| `macro_usa_house_starts` | US housing starts | Jin10 |
| `macro_usa_new_home_sales` | US new home sales | Jin10 |
| `macro_usa_existing_home_sales` | US existing home sales | Jin10 |
| `macro_usa_eia_crude_rate` | US EIA crude oil inventory | Jin10 |
| `macro_usa_api_crude_stock` | US API crude oil stock | Jin10 |

### Central Bank Interest Rates (央行利率)

| Function | Description | Source |
|----------|-------------|--------|
| `macro_bank_usa_interest_rate` | Fed interest rate decisions | Jin10 |
| `macro_bank_euro_interest_rate` | ECB interest rate decisions | Jin10 |
| `macro_bank_japan_interest_rate` | Bank of Japan interest rate | Jin10 |
| `macro_bank_english_interest_rate` | Bank of England interest rate | Jin10 |
| `macro_bank_australia_interest_rate` | RBA interest rate | Jin10 |
| `macro_bank_switzerland_interest_rate` | SNB interest rate | Jin10 |
| `macro_bank_newzealand_interest_rate` | RBNZ interest rate | Jin10 |
| `macro_bank_russia_interest_rate` | Central Bank of Russia rate | Jin10 |
| `macro_bank_india_interest_rate` | RBI interest rate | Jin10 |
| `macro_bank_brazil_interest_rate` | BCB interest rate | Jin10 |

### Other Countries Macro Data (其他国家宏观经济)

| Function | Description | Source |
|----------|-------------|--------|
| `macro_germany_gdp` | Germany GDP | Jin10 |
| `macro_germany_cpi_yearly` | Germany CPI | Jin10 |
| `macro_germany_ifo` | Germany IFO business climate | Jin10 |
| `macro_uk_gdp_yearly` | UK GDP | Jin10 |
| `macro_uk_cpi_yearly` | UK CPI | Jin10 |
| `macro_uk_bank_rate` | UK bank rate | Jin10 |
| `macro_australia_cpi_yearly` | Australia CPI | Jin10 |
| `macro_australia_bank_rate` | Australia bank rate | Jin10 |
| `macro_japan_cpi_yearly` | Japan CPI | Jin10 |
| `macro_japan_bank_rate` | Japan bank rate | Jin10 |
| `macro_swiss_cpi_yearly` | Switzerland CPI | Jin10 |

### Commodity and Financial Indicators (商品和金融指标)

| Function | Description | Source |
|----------|-------------|--------|
| `macro_cons_gold` | SPDR Gold Trust holdings | SPDR |
| `macro_cons_silver` | iShares Silver Trust holdings | iShares |
| `macro_euro_lme_holding` | LME holdings report | LME |
| `macro_euro_lme_stock` | LME inventory report | LME |
| `macro_usa_cftc_nc_holding` | CFTC non-commercial holdings | CFTC |
| `macro_usa_cftc_c_holding` | CFTC commercial holdings | CFTC |
| `macro_fx_sentiment` | Currency pair sentiment report | Jin10 |

---

## Bond Market Data (债券市场数据)

| Function | Description | Source |
|----------|-------------|--------|
| `bond_zh_hs_daily` | Bond market historical data | East Money |
| `bond_zh_hs_spot` | Bond market real-time quotes | East Money |
| `bond_zh_hs_cov_daily` | Convertible bond historical data | East Money |
| `bond_zh_hs_cov_spot` | Convertible bond real-time quotes | East Money |
| `bond_zh_cov` | Convertible bond summary | East Money |
| `bond_cb_jsl` | Convertible bond data (Jisilu) | Jisilu |
| `bond_cb_adj_logs_jsl` | Convertible bond conversion price changes | Jisilu |
| `bond_cb_index_jsl` | Convertible bond equal-weight index | Jisilu |
| `bond_cb_redeem_jsl` | Convertible bond forced redemption | Jisilu |
| `bond_new_composite_index_cbond` | New composite bond index | CCBond |
| `bond_composite_index_cbond` | Composite bond index | CCBond |
| `bond_china_close_return` | Closing yield curve history | Aggregate |
| `bond_treasure_issue_cninfo` | Treasury bond issuance | CNINFO |
| `bond_local_government_issue_cninfo` | Local government bond issuance | CNINFO |
| `bond_corporate_issue_cninfo` | Corporate bond issuance | CNINFO |
| `bond_cov_issue_cninfo` | Convertible bond issuance | CNINFO |
| `bond_info_cm` | Bond information query | ChinaFXTC |
| `bond_info_detail_cm` | Bond details | ChinaFXTC |

---

## Foreign Exchange Data (外汇数据)

| Function | Description | Source |
|----------|-------------|--------|
| `get_fx_spot_quote` | RMB foreign exchange spot quotes | ChinaFXTC |
| `get_fx_swap_quote` | RMB foreign exchange forward quotes | ChinaFXTC |
| `get_fx_pair_quote` | Foreign currency pair spot quotes | ChinaFXTC |
| `fx_spot_quote` | FX spot quotes | ChinaFXTC |
| `fx_swap_quote` | FX swap quotes | ChinaFXTC |
| `fx_pair_quote` | FX pair quotes | ChinaFXTC |
| `currency_latest` | Latest currency quotes | Currencyscoop |
| `currency_history` | Historical currency data | Currencyscoop |
| `currency_time_series` | Currency time series | Currencyscoop |
| `currency_currencies` | Supported currency list | Currencyscoop |
| `currency_convert` | Currency conversion | Currencyscoop |
| `currency_pair_map` | Currency pair mapping | Currencyscoop |
| `currency_boc_sina` | Bank of China exchange rate history | Sina |
| `currency_boc_safe` | RMB exchange rate central parity | Bank of China |
| `fx_spot_em` | Foreign exchange real-time quotes | East Money |
| `fx_hist_em` | Foreign exchange historical data | East Money |
| `fx_quote_baidu` | Foreign exchange quotes | Baidu |

---

## Cryptocurrency Data (加密货币数据)

| Function | Description | Source |
|----------|-------------|--------|
| `crypto_js_spot` | Mainstream cryptocurrency quotes | Jinshang |
| `crypto_name_url_table` | Cryptocurrency names and URLs | Jinshang |
| `crypto_bitcoin_hold_report` | Bitcoin holdings report | Jinshang |
| `crypto_bitcoin_cme` | CME Bitcoin volume | CME |

---

## Option Data (期权数据)

### Stock Options (股票期权)

| Function | Description | Source |
|----------|-------------|--------|
| `option_finance_board` | Financial options data | East Money |
| `option_finance_minute_sina` | Financial stock options minute data | Sina |
| `option_current_em` | Options data (East Money) | East Money |
| `option_current_day_sse` | SSE daily contracts | SSE |
| `option_current_day_szse` | SZSE daily contracts | SZSE |

### Index Options (指数期权)

| Function | Description | Source |
|----------|-------------|--------|
| `option_cffex_sz50_list_sina` | SSE 50 options list | Sina |
| `option_cffex_sz50_spot_sina` | SSE 50 options real-time | Sina |
| `option_cffex_sz50_daily_sina` | SSE 50 options historical | Sina |
| `option_cffex_hs300_list_sina` | CSI 300 options list | Sina |
| `option_cffex_hs300_spot_sina` | CSI 300 options real-time | Sina |
| `option_cffex_hs300_daily_sina` | CSI 300 options historical | Sina |
| `option_cffex_zz1000_list_sina` | CSI 1000 options list | Sina |
| `option_cffex_zz1000_spot_sina` | CSI 1000 options real-time | Sina |
| `option_cffex_zz1000_daily_sina` | CSI 1000 options historical | Sina |

### Commodity Options (商品期权)

| Function | Description | Source |
|----------|-------------|--------|
| `option_sina_option_commodity_dict` | Commodity options dictionary | Sina |
| `option_sina_option_commodity_contract_list` | Commodity options contracts | Sina |
| `option_sina_option_commodity_hist` | Commodity options historical data | Sina |
| `option_hist_dce` | DCE commodity options | DCE |
| `option_hist_czce` | CZCE commodity options | CZCE |
| `option_hist_shfe` | SHFE commodity options | SHFE |
| `option_hist_gfex` | GFEX commodity options | GFEX |
| `option_vol_gfex` | GFEX implied volatility | GFEX |
| `option_vol_shfe` | SHFE implied volatility | SHFE |

### Option Volatility Index (期权波动率指数)

| Function | Description | Source |
|----------|-------------|--------|
| `index_option_50etf_qvix` | 50ETF option volatility index | SSE |
| `index_option_50etf_min_qvix` | 50ETF option volatility index minute | SSE |
| `index_option_300etf_qvix` | 300ETF option volatility index | SSE |
| `index_option_300etf_min_qvix` | 300ETF option volatility index minute | SSE |
| `index_option_500etf_qvix` | 500ETF option volatility index | SSE |
| `index_option_500etf_min_qvix` | 500ETF option volatility index minute | SSE |
| `index_option_cyb_qvix` | ChiNext option volatility index | SSE |
| `index_option_cyb_min_qvix` | ChiNext option volatility index minute | SSE |
| `index_option_kcb_qvix` | STAR Market option volatility index | SSE |
| `index_option_kcb_min_qvix` | STAR Market option volatility index minute | SSE |
| `index_option_100etf_qvix` | SZSE 100ETF option volatility index | SZSE |
| `index_option_100etf_min_qvix` | SZSE 100ETF option volatility index minute | SZSE |
| `index_option_300index_qvix` | CSI 300 index option volatility index | CFFEX |
| `index_option_300index_min_qvix` | CSI 300 index option volatility index minute | CFFEX |
| `index_option_1000index_qvix` | CSI 1000 index option volatility index | CFFEX |
| `index_option_1000index_min_qvix` | CSI 1000 index option volatility index minute | CFFEX |
| `index_option_50index_qvix` | SSE 50 index option volatility index | CFFEX |
| `index_option_50index_min_qvix` | SSE 50 index option volatility index minute | CFFEX |

---

## Other Data (其他数据)

### Movie Box Office (电影票房)

| Function | Description | Source |
|----------|-------------|--------|
| `movie_boxoffice_realtime` | Movie real-time box office | Maoyan |
| `movie_boxoffice_daily` | Movie daily box office | Maoyan |
| `movie_boxoffice_weekly` | Movie weekly box office | Maoyan |
| `movie_boxoffice_monthly` | Movie monthly box office | Maoyan |
| `movie_boxoffice_yearly` | Movie yearly box office | Maoyan |
| `movie_boxoffice_cinema_daily` | Cinema daily box office | Maoyan |
| `movie_boxoffice_cinema_weekly` | Cinema weekly box office | Maoyan |

### News Data (新闻数据)

| Function | Description | Source |
|----------|-------------|--------|
| `news_cctv` | CCTV news transcript | CCTV |
| `stock_news_em` | Individual stock news | East Money |
| `news_economic_baidu` | Economic news | Baidu |
| `futures_news_shmet` | Shanghai Metals Market news | SHMET |

### Air Quality (空气质量)

| Function | Description | Source |
|----------|-------------|--------|
| `air_quality_hist` | Air quality historical data | Aggregate |
| `air_quality_rank` | Air quality ranking | Aggregate |
| `air_quality_watch_point` | Air quality observation point | Aggregate |
| `air_city_table` | All cities list | Aggregate |
| `air_quality_hebei` | Hebei air quality | Aggregate |

### Weather Data (天气数据)

| Function | Description | Source |
|----------|-------------|--------|
| `weather_daily` | Daily sunrise and sunset | Timeanddate |
| `weather_monthly` | Monthly sunrise and sunset | Timeanddate |

### Fortune Rankings (财富榜单)

| Function | Description | Source |
|----------|-------------|--------|
| `fortune_rank` | Fortune Global 500 rankings | Fortune |
| `forbes_rank` | Forbes China rankings | Forbes |
| `xincaifu_rank` | New Wealth 500 rankings | New Fortune |
| `hurun_rank` | Hurun rankings | Hurun |
| `index_bloomberg_billionaires` | Bloomberg billionaires index | Bloomberg |
| `index_bloomberg_billionaires_hist` | Bloomberg billionaires history | Bloomberg |

### ESG Ratings (ESG评级)

| Function | Description | Source |
|----------|-------------|--------|
| `stock_esg_msci_sina` | MSCI ESG ratings | Sina |
| `stock_esg_rft_sina` | Refinitiv ESG ratings | Sina |
| `stock_esg_rate_sina` | ESG rating data | Sina |
| `stock_esg_zd_sina` | Zhiding ESG ratings | Sina |
| `stock_esg_hz_sina` | Huazheng ESG ratings | Sina |

### Carbon Emissions (碳排放)

| Function | Description | Source |
|----------|-------------|--------|
| `energy_carbon_domestic` | Domestic carbon emissions | Aggregate |
| `energy_carbon_bj` | Beijing carbon emissions | Beijing |
| `energy_carbon_sz` | Shenzhen carbon emissions | Shenzhen |
| `energy_carbon_eu` | International carbon emissions | Aggregate |
| `energy_carbon_hb` | Hubei carbon emissions | Hubei |
| `energy_carbon_gz` | Guangzhou carbon emissions | Guangzhou |

### Oil Prices (油价)

| Function | Description | Source |
|----------|-------------|--------|
| `energy_oil_hist` | Gasoline and diesel historical price | Aggregate |
| `energy_oil_detail` | Regional oil prices | Aggregate |

### AMAC Data (基金业协会数据)

| Function | Description | Source |
|----------|-------------|--------|
| `amac_member_info` | AMAC member information | AMAC |
| `amac_person_fund_org_list` | AMAC fund practitioners | AMAC |
| `amac_person_bond_org_list` | AMAC bond practitioners | AMAC |
| `amac_manager_info` | AMAC private equity managers | AMAC |
| `amac_fund_info` | AMAC private equity funds | AMAC |
| `amac_manager_cancelled_info` | AMAC cancelled managers | AMAC |

---

**Note**: This catalog is not exhaustive. AkShare provides hundreds of data interfaces. For the most complete and up-to-date information, please refer to the [official documentation](https://akshare.akfamily.xyz/).
