from aiogram import types

import lib
from assets import commands
from core import Handler, events

event = events.Command(commands.USDT_TO_KZT, state='*')


async def callback(msg: types.Message):
    rate = await lib.binance.get_usdt_to_kzt_rate()
    await lib.messages.send_sell_offer(msg.chat.id, rate)


USDT_TO_KZT = Handler(event, callback)
