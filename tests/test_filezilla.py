import unittest
from unittest import mock

import requests

from check import fetch_filezilla


class FilezillaFetchTests(unittest.TestCase):
    def test_success(self):
        with mock.patch('check.fetch_json', return_value={'version': '1.2.3'}):
            self.assertEqual(fetch_filezilla(), '1.2.3')

    def test_network_error_returns_none(self):
        with mock.patch('check.fetch_json', side_effect=requests.RequestException):
            self.assertIsNone(fetch_filezilla())


if __name__ == '__main__':
    unittest.main()
