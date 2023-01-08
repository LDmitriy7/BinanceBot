import mongoengine as me

from . import config


class Database:
    def __init__(self):
        self.name = config.MONGO_DB
        self.host = config.MONGO_HOST
        self.user = config.MONGO_USER
        self.password = config.MONGO_PASSWORD
        self._connect()

    def _connect(self):
        me.connect(
            db=self.name,
            host=self.host,
            username=self.user,
            password=self.password,
        )
