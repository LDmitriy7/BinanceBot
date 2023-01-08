from aiogram import Dispatcher, types


async def reset():
    dp = Dispatcher.get_current()
    chat = types.Chat.get_current()
    user = types.User.get_current()
    await dp.storage.reset_state(chat=chat.id, user=user.id)
