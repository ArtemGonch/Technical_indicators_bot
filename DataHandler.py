from tradingview_ta import TA_Handler, Interval, Exchange
INTERVAL = Interval.INTERVAL_15_MINUTES

class DataHandler:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_data(self):
        out = TA_Handler(symbol=self.symbol, screener='Crypto', exchange='Binance', interval=INTERVAL)
        activ = out.get_analysis().summary
        activ['SYMBOL'] = self.symbol
        return activ