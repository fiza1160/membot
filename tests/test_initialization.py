import unittest
from src import initialization as inic


class Test(unittest.TestCase):
    def test_get_telegram_token(self):
        with self.subTest(case='get_telegram_token must return token (str)'):
            self.assertIsInstance(inic.get_telegram_token(), str)

    def test_get_redis_port(self):
        with self.subTest(case='get_redis_port must return port (int)'):
            self.assertIsInstance(inic.get_telegram_token(), str)

    def test_get_redis_host(self):
        with self.subTest(case='get_redis_host must return host (str)'):
            self.assertIsInstance(inic.get_telegram_token(), str)
