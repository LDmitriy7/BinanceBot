import config

ask_rate = """
Отправь максимальный курс покупки USDT/RUB.
Я сообщу тебе, когда появятся предложения ниже этого курса.
"""

buy_offer_available = f"""
<a href="{config.BUY_OFFERS_URL}">Доступно предложение по курсу {{rate}}</a>
"""

sell_offer_available = f"""
<a href="{config.SELL_OFFERS_URL}">Доступно предложение по курсу {{rate}}</a>
"""
