import os

TELEGRAM_TOKEN_NAME = 'MEM_BOT_TELEGRAM_TOKEN'
REDIS_PORT = 'MEM_BOT_REDIS_PORT'
REDIS_HOST = 'MEM_BOT_REDIS_HOST'


def get_telegram_token():
    if TELEGRAM_TOKEN_NAME not in os.environ:
        text_error = 'Environment variable {key} not found'.format(key=TELEGRAM_TOKEN_NAME)
        raise ValueError(text_error)

    return os.environ[TELEGRAM_TOKEN_NAME]


def get_redis_port():
    if REDIS_PORT not in os.environ:
        text_error = 'Environment variable {key} not found'.format(key=REDIS_PORT)
        raise ValueError(text_error)

    return os.environ[REDIS_PORT]


def get_redis_host():
    if REDIS_HOST not in os.environ:
        text_error = 'Environment variable {key} not found'.format(key=REDIS_HOST)
        raise ValueError(text_error)

    return os.environ[REDIS_HOST]
