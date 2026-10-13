import unittest
from unittest import mock

from core import version_check


class FetchUrlTests(unittest.TestCase):
    def test_timeout_and_verify_passed(self):
        with mock.patch.object(version_check.session, 'get') as mock_get:
            version_check.fetch_url('https://example.com', verify_ssl=False)
            mock_get.assert_called_once_with(
                'https://example.com', headers={}, verify=False, timeout=version_check.TIMEOUT, stream=False
            )
            mock_get.return_value.raise_for_status.assert_called_once()

    def test_github_token_only_sent_to_github_api(self):
        with mock.patch.dict('os.environ', {'GITHUB_TOKEN': 'abc'}), \
                mock.patch.object(version_check.session, 'get') as mock_get:
            version_check.fetch_url('https://api.github.com/repos/x/y')
            self.assertEqual(mock_get.call_args.kwargs['headers'], {'Authorization': 'token abc'})
            version_check.fetch_url('https://example.com')
            self.assertEqual(mock_get.call_args.kwargs['headers'], {})


if __name__ == '__main__':
    unittest.main()
