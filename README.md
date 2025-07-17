# Moving Average Crossover Strategy (Backtrader)

This repository demonstrates a simple moving average crossover strategy using the [Backtrader](https://www.backtrader.com/) backtesting framework and historical price data from [Yahoo Finance](https://pypi.org/project/yfinance/).

## 📚 Purpose

This project is purely for **educational purposes**, aimed at learning:
- The basics of strategy design and backtesting in Python
- Using the Backtrader framework (strategies, indicators, analyzers)
- Fetching financial data using `yfinance`

## ⚙️ Strategy Logic

The strategy uses two Simple Moving Averages (SMAs):
- **Fast SMA**: 50-day
- **Slow SMA**: 200-day

**Buy Signal:** When the fast SMA crosses above the slow SMA  
**Sell Signal:** When the fast SMA crosses below the slow SMA

## 📈 Features

- Backtests across multiple tickers
- Uses Yahoo Finance daily OHLCV data
- Performance metrics:
  - Sharpe Ratio
  - Max Drawdown

## 🛠 Requirements

- Python 3.8+
- `backtrader`
- `yfinance`
- `matplotlib`

Install with:

```bash
pip install backtrader yfinance matplotlib
