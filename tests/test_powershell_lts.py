import unittest
from unittest import mock

from check import fetch_powershell_lts


class PowerShellLtsFetchTests(unittest.TestCase):
    def test_highest_lts_tag(self):
        metadata = {"StableReleaseTag": "v7.7.0", "LTSReleaseTag": ["v7.4.22", "v7.6.10"]}
        with mock.patch('check.fetch_json', return_value=metadata):
            self.assertEqual(fetch_powershell_lts(), {
                'version': 'v7.6.10',
                'url': 'https://github.com/PowerShell/PowerShell/releases/tag/v7.6.10',
            })

    def test_numeric_not_text_order(self):
        with mock.patch('check.fetch_json', return_value={"LTSReleaseTag": ["v7.10.0", "v7.9.3"]}):
            self.assertEqual(fetch_powershell_lts()['version'], 'v7.10.0')

    def test_no_lts_tag_returns_none(self):
        with mock.patch('check.fetch_json', return_value={"LTSReleaseTag": []}):
            self.assertIsNone(fetch_powershell_lts())


if __name__ == '__main__':
    unittest.main()
