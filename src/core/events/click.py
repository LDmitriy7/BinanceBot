from dataclasses import dataclass

from aiogram import Dispatcher

from .event import CallbackQueryEvent
from .. import filters
from ..keyboards import CallbackButton


@dataclass
class Click(CallbackQueryEvent):
    value: CallbackButton
    chat_type: str | list[str] = None
    state: str = None

    def as_decorator(self, dp: Dispatcher):
        return dp.callback_query_handler(
            filters.CallbackQueryButton(self.value),
            chat_type=self.chat_type,
            state=self.state,
        )
