import re
from contextlib import suppress
from dataclasses import dataclass

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State

from .event import MessageEvent


def via_bot_filter(message: types.Message):
    return bool(message.via_bot)


@dataclass
class Text(MessageEvent):
    value: str | list[str] = None
    chat_type: str | list[str] = None
    via_bot: bool = None
    state: str | State = None

    def as_decorator(self, dp: Dispatcher):
        custom_filters = []

        if self.via_bot:
            custom_filters.append(via_bot_filter)

        return dp.message_handler(
            *custom_filters,
            text=self.value,
            chat_type=self.chat_type,
            state=self.state,
        )


def text_template_filter(template: str):
    def inner(msg: types.Message):
        escaped_template = re.escape(template)
        regexp = re.sub(r'\\{(.+?)\\}', r'(?P<\1>.+)', escaped_template)

        with suppress(TypeError):
            if match := re.fullmatch(regexp, msg.text):
                return {'text_vars': match.groupdict()}

        return False

    return inner


@dataclass
class TextTemplate(MessageEvent):
    value: str
    chat_type: str | list[str] = None
    state: str | State = None

    def as_decorator(self, dp: Dispatcher):
        custom_filters = [text_template_filter(self.value)]

        return dp.message_handler(
            *custom_filters,
            chat_type=self.chat_type,
            state=self.state,
        )
