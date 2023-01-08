from core import client

URL = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

HEADERS = {
    'content-type': 'application/json',
    'User-Agent': USER_AGENT,
}

BODY = {'page': 1, 'rows': 1, 'payTypes': ['TinkoffNew'], 'asset': 'USDT', 'fiat': 'RUB', 'tradeType': 'BUY'}


async def get_min_rate() -> float:
    resp = await client.post(URL, json=BODY, headers=HEADERS)
    json = resp.json()
    result = json['data']
    prices = [float(i['adv']['price']) for i in result]
    return min(prices)
