from aiogram import types

import lib
from assets import commands
from core import Handler, events

event = events.Command(commands.USDT_TO_RUB, state='*')


async def callback(msg: types.Message):
    rate = await lib.binance.get_usdt_to_rub_rate()
    await lib.messages.send_buy_offer(msg.chat.id, rate)


USDT_TO_RUB = Handler(event, callback)
