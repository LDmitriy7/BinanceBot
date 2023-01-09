from core import client

URL = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

HEADERS = {
    'content-type': 'application/json',
    'User-Agent': USER_AGENT,
}

BUY_JSON = {'page': 1, 'rows': 1, 'payTypes': ['TinkoffNew'], 'asset': 'USDT', 'fiat': 'RUB', 'tradeType': 'BUY'}
SELL_JSON = {'page': 1, 'rows': 1, 'payTypes': ['KaspiBank'], 'asset': 'USDT', 'fiat': 'KZT', 'tradeType': 'SELL'}


async def get_usdt_to_rub_rate() -> float:
    resp = await client.post(URL, json=BUY_JSON, headers=HEADERS)
    json = resp.json()
    result = json['data']
    prices = [float(i['adv']['price']) for i in result]
    return min(prices)


async def get_usdt_to_kzt_rate() -> float:
    resp = await client.post(URL, json=SELL_JSON, headers=HEADERS)
    json = resp.json()
    result = json['data']
    prices = [float(i['adv']['price']) for i in result]
    return max(prices)


async def get_rub_to_kzt_rate() -> float:
    usdt_to_rub = await get_usdt_to_rub_rate()
    usdt_to_kzt = await get_usdt_to_kzt_rate()
    return usdt_to_kzt / usdt_to_rub
