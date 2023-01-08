_RATE = None


def parse(text: str):
    return float(text.replace(',', '.'))


def save(rate: float):
    global _RATE

    _RATE = rate
    print(f'Установлен новый курс: {rate}')


def get() -> float | None:
    return _RATE
