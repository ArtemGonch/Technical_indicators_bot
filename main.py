from ChartHandler import ChartHandler
from ClientHandler import ClientHandler
from DataHandler import DataHandler
from TelegramHandler import TelegramHandler
import time
import yfinance as yf

symbols = ClientHandler().get_symbols()
longs = []
shorts = []
telegram_handler = TelegramHandler()
chart_handler = ChartHandler()

def first_data():
    print('Searching first data')
    telegram_handler.send_message('Searching first data')
    for i in symbols:
        try:
            data_handler = DataHandler(i)
            data = data_handler.get_data()
            if(data['RECOMMENDATION'] == 'STRONG_BUY'):
                longs.append(data['SYMBOL'])
            if(data['RECOMMENDATION'] == 'STRONG_SELL'):
                shorts.append(data['SYMBOL'])
            time.sleep(0.1)
        except:
            pass
    print('longs:')
    telegram_handler.send_message('longs:')
    print(longs)
    telegram_handler.send_message(', '.join(longs).replace('USDT', ''))
    print('shorts:')
    telegram_handler.send_message('shorts:')
    print(shorts)
    telegram_handler.send_message(', '.join(shorts).replace('USDT', ''))
    return longs, shorts

print('START')
telegram_handler.send_message('START')
first_data()

while True:
    print('____________NEW ROUND___________')
    telegram_handler.send_message('________NEW ROUND________')
    for i in symbols:
        try:
            data_handler = DataHandler(i)
            data = data_handler.get_data()
            if data['RECOMMENDATION'] == 'STRONG_BUY' and (i not in longs):
                telegram_handler.send_message(i.replace('USDT', '') + ' BUY')
                longs.append(i)
                binance_url = chart_handler.get_chart(i)
                telegram_handler.send_message(binance_url)
            if data['RECOMMENDATION'] == 'STRONG_SELL' and (i not in shorts):
                telegram_handler.send_message(i.replace('USDT', '') + ' SELL')
                shorts.append(i)
                binance_url = chart_handler.get_chart(i)
                telegram_handler.send_message(binance_url)
            time.sleep(0.1)
        except:
            pass