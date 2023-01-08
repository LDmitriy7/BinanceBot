from dataclasses import dataclass
from typing import Callable, Coroutine

from .events import Event

Callback = Callable[[...], Coroutine]


@dataclass
class Handler:
    event: Event
    callback: Callback
