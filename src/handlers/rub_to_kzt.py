from aiogram import types

import lib
from assets import commands
from core import Handler, events

event = events.Command(commands.RUB_TO_KZT, state='*')


async def callback(msg: types.Message):
    rate = await lib.binance.get_rub_to_kzt_rate()
    await msg.answer(f'Курс самого выгодного обмена: <b>{rate:.2f}</b>')


RUB_TO_KZT = Handler(event, callback)
