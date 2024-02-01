import mplfinance as mpf
import yfinance as yf
class ChartHandler:
    @staticmethod
    def get_chart(symbol):
        url = f'https://www.binance.com/en/trade/{symbol}?theme=light&type=spot'
        return url

