from binance.um_futures import UMFutures

class ClientHandler:
    def __init__(self):
        self.client = UMFutures()

    def get_symbols(self):
        tickers = self.client.mark_price()
        symbols = []
        for i in tickers:
            ticker = i['symbol']
            symbols.append(ticker)
        return symbols