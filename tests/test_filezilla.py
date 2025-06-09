import unittest
from unittest import mock
import sys
import types

# Ensure a requests stub exists and provide minimal attributes needed for the
# modules under test.
requests_stub = sys.modules.get("requests")
if requests_stub is None:
    requests_stub = types.SimpleNamespace()
    sys.modules["requests"] = requests_stub

requests_stub.RequestException = Exception
requests_stub.get = getattr(requests_stub, "get", lambda *args, **kwargs: None)
requests_stub.packages = getattr(
    requests_stub,
    "packages",
    types.SimpleNamespace(
        urllib3=types.SimpleNamespace(
            disable_warnings=lambda *a, **k: None,
            exceptions=types.SimpleNamespace(InsecureRequestWarning=object),
        )
    ),
)

requests = requests_stub

from sw_filezilla import fetch_filezilla


class FilezillaFetchTests(unittest.TestCase):
    def test_success(self):
        with mock.patch('sw_filezilla.fetch_json', return_value={'version': '1.2.3'}):
            self.assertEqual(fetch_filezilla(), '1.2.3')

    def test_network_error_returns_none(self):
        with mock.patch('sw_filezilla.fetch_json', side_effect=requests.RequestException):
            self.assertIsNone(fetch_filezilla())


if __name__ == '__main__':
    unittest.main()
