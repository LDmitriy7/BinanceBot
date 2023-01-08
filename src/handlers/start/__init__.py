from core import HandlerGroup
from .entry import ENTRY
from .rate import RATE

START = HandlerGroup(
    ENTRY,
    RATE,
)
