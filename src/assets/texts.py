import config

ask_rate = """
Отправь максимальный курс покупки USDT/RUB.
Я сообщу тебе, когда появятся предложения ниже этого курса.
"""

offer_available = f"""
<a href="{config.OFFERS_PAGE_URL}">Доступно предложение по курсу {{rate}}</a>
"""
