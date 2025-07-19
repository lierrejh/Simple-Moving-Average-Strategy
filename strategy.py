import yfinance as yf
import backtrader as bt
import matplotlib
import backtrader.feeds as btfeeds
from datetime import datetime
import matplotlib.pyplot as plt

data = btfeeds.PandasData(dataname=yf.download('SPY', start='2024-01-01', end='2025-01-01',multi_level_index=False), plot = True)

cerebro = bt.Cerebro()
cerebro.adddata(data)

class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma50 = bt.indicators.SimpleMovingAverage(self.data.close, period=50)
        self.sma200 = bt.indicators.SimpleMovingAverage(self.data.close, period=200)
        self.sma50.plotinfo.plot = True
        self.sma200.plotinfo.plot = True
    
    def next(self):
        if not self.position:
            if self.sma50 > self.sma200:
                self.buy(size=1, exectype=bt.Order.StopTrail, trailamount=0.25)
        else:
            if self.sma50 < self.sma200:
                self.sell(size=1, exectype=bt.Order.StopTrail, trailamount=0.25)

cerebro.addstrategy(MyStrategy)
cerebro.broker.setcash(100000)
result = cerebro.run()
cerebro.plot(style='candlestick')
plt.show()



