import requests
TELEGRAM_TOKEN = '5827102177:AAFASeCombZVjRTjcE1Fkd3Eu8JMCrcPgjk'
TELEGRAM_USER = '1624701845'

class TelegramHandler:
    def __init__(self):
        self.token = TELEGRAM_TOKEN
        self.user = TELEGRAM_USER

    def send_message(self, text):
        res = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(self.token),
                           params=dict(chat_id=self.user, text=text))
