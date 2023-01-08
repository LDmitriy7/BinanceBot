from aiogram import types

import lib
from assets import states
from core import Handler, events

event = events.Message(state=states.Start.rate)


async def callback(msg: types.Message):
    try:
        rate = lib.rate.parse(msg.text)
    except ValueError:
        await msg.answer('Отправь только целое/дробное число')
        return

    lib.rate.save(rate)

    await lib.state.reset()
    await msg.answer('Курс установлен, ожидайте уведомления')


RATE = Handler(event, callback)
