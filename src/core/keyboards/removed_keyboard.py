from aiogram.types import ReplyKeyboardRemove


class RemovedKeyboard:
    _raw = ReplyKeyboardRemove()

    def adapt(self) -> ReplyKeyboardRemove:
        return self._raw
