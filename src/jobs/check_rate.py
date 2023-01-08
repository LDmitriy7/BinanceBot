import config
import lib
from assets import texts
from core import Job, bot


async def callback():
    desired_rate = lib.rate.get()

    if desired_rate is None:
        return

    actual_rate = await lib.binance.get_min_rate()

    if actual_rate <= desired_rate:
        text = texts.offer_available.format(rate=actual_rate)
        await bot.send_message(config.OWNER_ID, text)


CHECK_RATE = Job(callback, config.CHECK_INTERVAL)
