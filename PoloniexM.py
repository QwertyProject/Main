import requests
from urllib.parse import urlencode
import hmac
import hashlib
import time


class Poloniex:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    # Получаем книгу ордеров требуемой глубины для выбранной валютной пары
    def return_order_book(self, pair, depth=10):
        url = 'https://poloniex.com/public?command=returnOrderBook'
        params = {'currencyPair': pair, 'depth': depth}
        try:
            return requests.get(url, params).json()
        except Exception:
            print('Проверьте соединение или указанные вами параметры')
            return None

    # Формируем запрос на сервер Poloniex используя собственный публичный и приватный ключ
    def trading(self, command, data):
        url = 'https://poloniex.com/tradingApi'
        data['command'] = command
        data['nonce'] = int(time.time() * 1000)
        d = urlencode(data).encode('utf-8')
        sign = hmac.new(self.secret_key.encode('utf-8'), d, hashlib.sha512).hexdigest()
        headers = {'Sign': sign, 'Key': self.api_key}
        try:
            return requests.post(url, data, headers=headers).json()
        except Exception:
            print('Проверьте соединение или указанные вами параметры')
            return None

    def buy(self, pair, rate, amount):
        data = {'currencyPair': pair, 'rate': rate, 'amount': amount}
        return self.trading('buy', data)

    def sell(self, pair, rate, amount):
        data = {'currencyPair': pair, 'rate': rate, 'amount': amount}
        return self.trading('sell', data)

    def move_order(self, order, rate):
        data = {'orderNumber': order, 'rate': rate}
        return self.trading('moveOrder', data)

    def order_info(self, order):
        data = {'orderNumber': order}
        return self.trading('returnOrderTrades', data)

    def balance_info(self):
        data = {}
        return self.trading('returnBalances', data)