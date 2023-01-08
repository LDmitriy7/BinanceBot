from dataclasses import dataclass

from aiogram import Dispatcher

from .event import InlineQueryEvent


@dataclass
class InlineQuery(InlineQueryEvent):
    value: str = None
    chat_type: str | list[str] = None

    def as_decorator(self, dp: Dispatcher):
        return dp.inline_handler(
            text=self.value,
            chat_type=self.chat_type,
        )
