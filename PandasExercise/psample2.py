# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from yahooquery import Ticker
import yfinance as yf
from yahoo_fin import stock_info as si

yf.pdr_override()
stock_list = si.tickers_nasdaq()
#print(stock_list[:10])

len(stock_list)

#tickers = Ticker(stock_list[:15])
tickers = Ticker(stock_list[:3])
print(tickers)
df_stats=pd.DataFrame.from_dict(tickers.key_stats)
print(df_stats.shape)
print(df_stats)
#tickers = Ticker('aaon', 'aapl')
df_financedt = pd.DataFrame.from_dict(tickers.financial_data)
#print(df_stats = tickers.option_chain)
#print(tickers.financial_data)
tickers_new = Ticker(['aapl', 'amzn'])
df_stats_new = pd.DataFrame.from_dict(tickers_new.key_stats)
print(df_stats_new)
#df_stats.T
df_stats = df_stats.T
print(df_stats)
print(df_stats["category"])
print(df_stats[["category", "fundFamily"]])

df_stats.to_csv("stklist.csv")
