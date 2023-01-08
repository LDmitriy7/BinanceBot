import asyncio

import aiogram
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils import executor

from .bot import bot
from .database import Database
from .handler import Handler
from .handler_group import HandlerGroup
from .job import Job


class Dispatcher:
    def __init__(self, db: Database):
        self._db = db
        self._loop = asyncio.get_event_loop()

    def _create_raw(self) -> aiogram.Dispatcher:
        from . import middlewares

        storage = MongoStorage(
            host=self._db.host,
            db_name=self._db.name,
            username=self._db.user,
            password=self._db.password,
        )
        dp = aiogram.Dispatcher(bot, storage=storage, loop=self._loop)
        dp.setup_middleware(middlewares.AnswerAnyQuery())
        return dp

    def start_polling(self, handlers: HandlerGroup, middlewares: list[BaseMiddleware], jobs: list[Job]):
        dp = self._create_raw()
        self._setup_handlers(handlers, dp)
        self._setup_middlewares(middlewares, dp)
        self._schedule_jobs(jobs)
        executor.start_polling(dp)

    def _setup_handlers(self, handlers: HandlerGroup, dp: aiogram.Dispatcher):
        for handler in handlers:
            self._setup_handler(handler, dp)

    def _setup_middlewares(self, middlewares: list[BaseMiddleware], dp: aiogram.Dispatcher):
        for m in middlewares:
            self._setup_middleware(m, dp)

    def _schedule_jobs(self, jobs: list[Job]):
        for job in jobs:
            job.schedule(self._loop)

    @staticmethod
    def _setup_handler(handler: Handler, dp: aiogram.Dispatcher):
        decorator = handler.event.as_decorator(dp)
        decorator(handler.callback)

    @staticmethod
    def _setup_middleware(middleware: BaseMiddleware, dp: aiogram.Dispatcher):
        dp.setup_middleware(middleware)
