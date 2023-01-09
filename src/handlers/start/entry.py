from aiogram import types

from assets import commands, texts, states
from core import Handler, events

event = events.Command(commands.START, state='*')


async def callback(msg: types.Message):
    await states.Start.rate.set()
    await msg.answer(texts.ask_rate)
    await commands.setup()


ENTRY = Handler(event, callback)
