from .inline_keyboard import InlineKeyboard, CallbackButton, UrlButton, InlineQueryButton
from .keyboard import Keyboard
from .removed_keyboard import RemovedKeyboard

AnyKeyboard = Keyboard | InlineKeyboard | RemovedKeyboard
