import unittest
from unittest import mock

from check import fetch_irfanview


class IrfanViewFetchTests(unittest.TestCase):
    def test_version_parsed(self):
        html = "<li>IrfanView 32-bit</li><h2>Get IrfanView (<strong>version 4.99</strong>)</h2>"
        mock_resp = mock.Mock(text=html)
        with mock.patch('check.fetch_url', return_value=mock_resp):
            self.assertEqual(fetch_irfanview()['version'], '4.99')

    def test_no_match_returns_none(self):
        mock_resp = mock.Mock(text='no version here')
        with mock.patch('check.fetch_url', return_value=mock_resp):
            self.assertIsNone(fetch_irfanview())


if __name__ == '__main__':
    unittest.main()
