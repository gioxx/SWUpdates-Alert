import ssl
import unittest
from unittest import mock
import sys
import types

# Provide a minimal requests stub so the module under test can be imported
requests_stub = types.SimpleNamespace()
requests_stub.packages = types.SimpleNamespace(
    urllib3=types.SimpleNamespace(
        disable_warnings=lambda *args, **kwargs: None,
        exceptions=types.SimpleNamespace(InsecureRequestWarning=object),
    )
)
requests_stub.get = lambda *args, **kwargs: None
sys.modules.setdefault("requests", requests_stub)

from core.version_check import fetch_url


class DummyResponse:
    def __init__(self):
        self.status_code = 200
        self.text = "ok"
        self.content = b"ok"

    def raise_for_status(self):
        pass


class FetchUrlSSLContextTest(unittest.TestCase):
    def _make_response(self):
        return DummyResponse()

    def test_context_restored_between_calls(self):
        original = ssl._create_default_https_context
        response = self._make_response()

        with mock.patch('requests.get', return_value=response) as mock_get:
            fetch_url('http://example.com', verify_ssl=False)
            mock_get.assert_called_once_with('http://example.com', verify=False)
            self.assertIs(ssl._create_default_https_context, original)

        with mock.patch('requests.get', return_value=response) as mock_get:
            fetch_url('http://example.com', verify_ssl=True)
            mock_get.assert_called_once_with('http://example.com', verify=True)
            self.assertIs(ssl._create_default_https_context, original)


if __name__ == '__main__':
    unittest.main()
