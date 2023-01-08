from abc import ABC, abstractmethod
from typing import Callable

from aiogram import Dispatcher

Decorator = Callable[[Callable], None]


class Event(ABC):

    @abstractmethod
    def as_decorator(self, dp: Dispatcher) -> Decorator:
        """ Return aiogram decorator """


class MessageEvent(Event, ABC):
    pass


class CallbackQueryEvent(Event, ABC):
    pass


class InlineQueryEvent(Event, ABC):
    pass
