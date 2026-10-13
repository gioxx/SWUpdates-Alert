import unittest
from unittest import mock

from check import fetch_putty


class PuttyFetchTests(unittest.TestCase):
    def test_version_from_redirect(self):
        with mock.patch('check.fetch_url', return_value=mock.Mock(url='https://the.earth.li/~sgtatham/putty/0.85/')):
            self.assertEqual(fetch_putty(), {'version': '0.85'})

    def test_no_redirect_returns_none(self):
        with mock.patch('check.fetch_url', return_value=mock.Mock(url='https://the.earth.li/~sgtatham/putty/latest/')):
            self.assertIsNone(fetch_putty())


if __name__ == '__main__':
    unittest.main()
