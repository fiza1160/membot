import os


class Config(object):
    TELEGRAM_TOKEN_NAME = os.environ.get('MEM_BOT_TELEGRAM_TOKEN')
    REDIS_PORT = os.environ.get('MEM_BOT_REDIS_PORT')
    REDIS_HOST = os.environ.get('MEM_BOT_REDIS_HOST')
