import unittest
from unittest import mock

from check import fetch_filezilla


class FilezillaFetchTests(unittest.TestCase):
    def test_version_parsed(self):
        html = '<meta name="description" content="Download FileZilla Client 3.71.1 for Windows (64bit x86)" />'
        with mock.patch('check.fetch_url', return_value=mock.Mock(text=html)):
            self.assertEqual(fetch_filezilla(), {'version': '3.71.1'})

    def test_no_match_returns_none(self):
        with mock.patch('check.fetch_url', return_value=mock.Mock(text='403 Forbidden')):
            self.assertIsNone(fetch_filezilla())


if __name__ == '__main__':
    unittest.main()
