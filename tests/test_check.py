import os
import tempfile
import unittest
from unittest import mock

import check
from core import version_check

UPDATES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "updates")


class VersionFileContractTests(unittest.TestCase):
    """Files under updates/ are read by external tools: names and format must not change."""

    def test_every_version_file_has_a_check(self):
        self.assertEqual(sorted(os.listdir(UPDATES)), sorted(f for _, _, f, _ in check.CHECKS))

    def test_written_file_is_single_line_without_newline(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(version_check, 'notify_telegram') as notify:
            path = os.path.join(tmp, "LATEST_X")
            version_check.run_check("X", lambda: {"version": "v1.2", "url": "u"}, path, "{version} {url}")
            with open(path, 'rb') as fh:
                self.assertEqual(fh.read(), b"v1.2")
            notify.assert_called_once_with("v1.2 u")
            version_check.run_check("X", lambda: {"version": "v1.2"}, path, "{version}")
            notify.assert_called_once()
            with self.assertRaises(ValueError):
                version_check.run_check("X", lambda: None, path, "{version}")
            with open(path, 'rb') as fh:
                self.assertEqual(fh.read(), b"v1.2")


class MainTests(unittest.TestCase):
    def test_one_failure_does_not_stop_other_checks(self):
        calls = []

        def fake_run_check(name, *args):
            calls.append(name)
            if name == "PuTTY":
                raise OSError("Network is unreachable")

        with mock.patch.object(check, 'run_check', side_effect=fake_run_check):
            self.assertEqual(check.main(), 1)
        self.assertEqual(calls, [name for name, *_ in check.CHECKS])


if __name__ == '__main__':
    unittest.main()
