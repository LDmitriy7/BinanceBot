import asyncio

from .logger import logger
from .types import AsyncFunction


class Job:
    def __init__(self, callback: AsyncFunction, interval: int = 0):
        self._callback = callback
        self._interval = interval

    async def _task(self):
        while True:
            try:
                await self._callback()
            except Exception as e:
                logger.exception(e)
            finally:
                await asyncio.sleep(self._interval)

    def schedule(self, loop: asyncio.AbstractEventLoop):
        loop.create_task(self._task())
