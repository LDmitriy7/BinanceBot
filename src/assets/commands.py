from aiogram.types import BotCommand, BotCommandScopeChat

import config
from core import bot

START = 'start'
USDT_TO_RUB = 'usdt_to_rub'
USDT_TO_KZT = 'usdt_to_kzt'
RUB_TO_KZT = 'rub_to_kzt'

USER_COMMANDS = [
    BotCommand(START, 'Установить желаемый курс'),
    BotCommand(RUB_TO_KZT, 'Курс RUB/KZT'),
    BotCommand(USDT_TO_RUB, 'Курс покупки USDT'),
    BotCommand(USDT_TO_KZT, 'Курс продажи USDT'),
]


async def setup():
    await bot.delete_my_commands(BotCommandScopeChat(config.OWNER_ID))
    await bot.set_my_commands(USER_COMMANDS)
