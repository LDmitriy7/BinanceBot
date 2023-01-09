from core import HandlerGroup
from .rub_to_kzt import RUB_TO_KZT
from .start import START
from .usd_to_rub import USDT_TO_RUB
from .usdt_to_kzt import USDT_TO_KZT

HANDLERS = HandlerGroup(
    START,
    USDT_TO_RUB,
    USDT_TO_KZT,
    RUB_TO_KZT,
)
