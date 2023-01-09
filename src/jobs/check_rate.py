import config
import lib
from core import Job


async def callback():
    desired_rate = lib.rate.get()

    if desired_rate is None:
        return

    actual_rate = await lib.binance.get_usdt_to_rub_rate()

    if actual_rate <= desired_rate:
        await lib.messages.send_buy_offer(config.OWNER_ID, actual_rate)


CHECK_RATE = Job(callback, config.CHECK_INTERVAL)
