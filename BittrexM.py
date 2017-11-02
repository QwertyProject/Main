import requests
from urllib.parse import urlencode
import hmac
import hashlib
import time


class Bittrex:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    # Получаем книгу ордеров требуемой глубины для выбранной валютной пары
    def get_order_book(self, pair, type):
        url = 'https://bittrex.com/api/v1.1/public/getorderbook'
        params = {'market': pair, 'type': type}
        try:
            return requests.get(url, params).json()
        except Exception:
            print('Проверьте соединение или указанные вами параметры')
            return None

    # Формируем запрос на сервер Bittrex используя собственный публичный и приватный ключ
    def trading(self, optype, command, data):
        url = 'https://bittrex.com/api/v1.1/' + str(optype) + '/' + str(command)
        data['apikey'] = self.api_key
        data['nonce'] = int(time.time() * 1000)
        d = (url + '?').encode('utf-8') + urlencode(data).encode('utf-8')
        sign = hmac.new(self.secret_key.encode('utf-8'), d, hashlib.sha512).hexdigest()
        headers = {'apisign': sign}
        try:
            return requests.get(url, data, headers=headers).json()
        except Exception:
            print('Проверьте соединение или указанные вами параметры')
            return None

    def buy(self, pair, rate, amount):
        data = {'market': pair, 'rate': rate, 'quantity': amount}
        return self.trading('market', 'buylimit', data)

    def sell(self, pair, rate, amount):
        data = {'market': pair, 'rate': rate, 'quantity': amount}
        return self.trading('market', 'selllimit', data)

    def cancel(self, uuid):
        data = {'uuid': uuid}
        return self.trading('market', 'cancel', data)

    def get_open_orders(self, market):
        data = {'market': market}
        return self.trading('market', 'getopenorders', data)

    def balance_info(self, currency):
        data = {'currency': currency}
        return self.trading('account', 'getbalance', data)