from BittrexM import Bittrex
from PoloniexM import Poloniex
import json

# Указываем собстенный публичный и приватный ключ биржи Bittrex
b_api_key = 'key'
b_secret_key = 'key'

# Указываем собстенный публичный и приватный ключ биржи Poloniex
pl_api_key = 'key'
pl_secret_key = 'key'

# Создаем объекты классов с указанием ключей
bt = Bittrex(b_api_key, b_secret_key)
pl = Poloniex(pl_api_key, pl_secret_key)

# Пример запроса баланса валюты GNT своем кошельке Bittrex
currency = 'GNT'
balance=bt.balance_info(currency)
print(balance)

# Пример запроса 3 первых ордеров 'из стакана' на бирже Poloniex для валютной пары BTC-ETH
pair='BTC_ETH'
depth=3
orderbook=pl.return_order_book(pair, depth)
print(json.dumps(orderbook, indent=1))