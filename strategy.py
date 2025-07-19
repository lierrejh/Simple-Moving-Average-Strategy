import yfinance as yf
import backtrader as bt
import matplotlib
import backtrader.feeds as btfeeds
from datetime import datetime
import matplotlib.pyplot as plt

data = btfeeds.PandasData(dataname=yf.download('SPY', start='2010-01-01', end='2025-01-01',multi_level_index=False), plot = True)

cerebro = bt.Cerebro()
cerebro.adddata(data)

class MyStrategy(bt.Strategy):
    
    params = dict(
        risk_per_trade=0.01,
        stop_loss=0.01,
        take_profit=0.02,
    ) 

    def __init__(self):
        self.sma50 = bt.indicators.SimpleMovingAverage(self.data.close, period=50)
        self.sma200 = bt.indicators.SimpleMovingAverage(self.data.close, period=200)
        self.sma50.plotinfo.plot = True
        self.sma200.plotinfo.plot = True
    
    def next(self):

        price = self.data.close[0]


        if not self.position:
            if self.sma50 > self.sma200:
                sl_price= price * (1 - self.params.stop_loss)
                tp_price = price * (1 + self.params.take_profit)
                size = min((int((1000) / (price - sl_price))), 200)
                self.buy_bracket(size=size, stopprice=sl_price, limitprice=tp_price)

        else:
            if self.sma50 < self.sma200:
                sl_price = price * (1 + self.params.stop_loss)
                tp_price = price * (1 - self.params.take_profit)
                size = min((int((1000) / (sl_price - price)), 200))

                self.sell_bracket(size=size, stopprice=sl_price, limitprice=tp_price)

cerebro.addstrategy(MyStrategy)
cerebro.broker.setcash(100000)
cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='sharpe')
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)

result = cerebro.run()
strat = result[0]
print("Sharpe Ratio:", strat.analyzers.sharpe.get_analysis())
print("Drawdown:", strat.analyzers.drawdown.get_analysis())

cerebro.plot(style='candlestick')




