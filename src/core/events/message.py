from dataclasses import dataclass

from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State

from .event import MessageEvent


@dataclass
class Message(MessageEvent):
    chat_type: str | list[str] = None
    state: str | State = None

    def as_decorator(self, dp: Dispatcher):
        return dp.message_handler(
            content_types='any',
            chat_type=self.chat_type,
            state=self.state,
        )
