from dataclasses import dataclass

from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State

from .event import MessageEvent


@dataclass
class Command(MessageEvent):
    value: str
    chat_type: str | list[str] = None
    user_id: int | list[int] = None
    state: str | State = None

    def as_decorator(self, dp: Dispatcher):
        return dp.message_handler(
            commands=self.value,
            chat_type=self.chat_type,
            user_id=self.user_id,
            state=self.state,
        )
