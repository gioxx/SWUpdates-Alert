import unittest
from unittest import mock

from sw_irfanview import fetch_irfanview


class IrfanViewFetchTests(unittest.TestCase):
    def test_version_parsed(self):
        html = "Welcome to IrfanView 4.99"
        mock_resp = mock.Mock(text=html)
        with mock.patch('sw_irfanview.fetch_url', return_value=mock_resp):
            self.assertEqual(fetch_irfanview()['version'], '4.99')

    def test_no_match_returns_none(self):
        mock_resp = mock.Mock(text='no version here')
        with mock.patch('sw_irfanview.fetch_url', return_value=mock_resp):
            self.assertIsNone(fetch_irfanview())


if __name__ == '__main__':
    unittest.main()
