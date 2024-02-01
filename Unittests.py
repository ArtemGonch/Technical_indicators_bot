from main import DataHandler, ClientHandler, ChartHandler, TelegramHandler, first_data
import unittest
from unittest.mock import patch, MagicMock
TELEGRAM_TOKEN = '5827102177:AAFASeCombZVjRTjcE1Fkd3Eu8JMCrcPgjk'
TELEGRAM_USER = '1624701845'

class TestDataHandler(unittest.TestCase):
    def test_get_data(self):
        with patch('main.TA_Handler') as mock_TA_Handler:
            mock_analysis = MagicMock()
            mock_analysis.summary = {'RECOMMENDATION': 'STRONG_BUY', 'SYMBOL': 'BTCUSDT'}
            mock_TA_Handler.return_value.get_analysis.return_value = mock_analysis
            data_handler = DataHandler('BTCUSDT')
            data = data_handler.get_data()
            self.assertEqual(data['RECOMMENDATION'], 'STRONG_BUY')
            self.assertEqual(data['SYMBOL'], 'BTCUSDT')

class TestClientHandler(unittest.TestCase):
    def test_get_symbols(self):
        with patch('main.UMFutures') as mock_UMFutures:
            mock_client = MagicMock()
            mock_tickers = [{'symbol': 'BTCUSDT'}, {'symbol': 'ETHUSDT'}]
            mock_client.mark_price.return_value = mock_tickers
            mock_UMFutures.return_value = mock_client
            client_handler = ClientHandler()
            symbols = client_handler.get_symbols()
            self.assertEqual(symbols, ['BTCUSDT', 'ETHUSDT'])

class TestChartHandler(unittest.TestCase):
    def test_get_chart(self):
        chart_handler = ChartHandler()
        chart_url = chart_handler.get_chart('BTCUSDT')
        self.assertEqual(chart_url, 'https://charts.binance.org/chart/BTCUSDT')

class TestTelegramHandler(unittest.TestCase):
    def test_send_message(self):
        with patch('requests.get') as mock_requests:
            telegram_handler = TelegramHandler()
            telegram_handler.send_message('test message')
            mock_requests.assert_called_with('https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN),
                                             params=dict(chat_id=TELEGRAM_USER, text='test message'))


class TestFirstData(unittest.TestCase):
    def test_first_data(self):
        with patch('main.DataHandler') as mock_DataHandler, \
             patch('main.TelegramHandler') as mock_TelegramHandler:
            mock_data_handler = MagicMock()
            mock_data = {'RECOMMENDATION': 'STRONG_BUY', 'SYMBOL': 'BTCUSDT'}
            mock_data_handler.get_data.return_value = mock_data
            mock_DataHandler.return_value = mock_data_handler
            mock_telegram_handler = MagicMock()
            mock_TelegramHandler.return_value = mock_telegram_handler
            longs, shorts = first_data()
            self.assertEqual(longs, ['BTCUSDT'])
            self.assertEqual(shorts, [])
            mock_telegram_handler.send_message.assert_called_with('Searching first data')
            mock_telegram_handler.send_message.assert_called_with('longs:')
            mock_telegram_handler.send_message.assert_called_with('shorts:')
            mock_telegram_handler.send_message.assert_called_with('BTC BUY')

if __name__ == '__main__':
    unittest.main()