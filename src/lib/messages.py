from assets import texts
from core import bot


async def send_buy_offer(chat_id: int, rate: float):
    text = texts.buy_offer_available.format(rate=rate)
    await bot.send_message(chat_id, text)


async def send_sell_offer(chat_id: int, rate: float):
    text = texts.sell_offer_available.format(rate=rate)
    await bot.send_message(chat_id, text)
