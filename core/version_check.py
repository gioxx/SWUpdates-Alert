import os
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from include_tgram import sendtotelegram

TIMEOUT = (10, 60)  # connect, read (seconds)

session = requests.Session()
session.mount(
    "https://",
    HTTPAdapter(max_retries=Retry(total=3, backoff_factor=5, status_forcelist=(429, 500, 502, 503, 504))),
)


def fetch_url(url, verify_ssl=True, stream=False):
    """Return a requests.Response, with retries, timeout and GitHub token support."""
    headers = {}
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token and urlparse(url).hostname == "api.github.com":
        headers["Authorization"] = f"token {github_token}"
    if not verify_ssl:
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    response = session.get(url, headers=headers, verify=verify_ssl, timeout=TIMEOUT, stream=stream)
    response.raise_for_status()
    return response


def fetch_json(url, verify_ssl=True):
    """Retrieve JSON data from URL."""
    return fetch_url(url, verify_ssl=verify_ssl).json()


def read_repo_version(filename):
    """Read first line of version file, return None if file missing."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as fh:
        content = fh.read()
        return content.split('\n', 1)[0]


def write_repo_version(filename, version):
    # Files under updates/ are read by external tools: one line, no trailing newline.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as fh:
        fh.write(version)


def notify_telegram(message):
    """Proxy include_tgram.sendtotelegram."""
    return sendtotelegram(message)


def run_check(name, fetch_fn, version_file, message_fmt):
    data = fetch_fn()
    if isinstance(data, dict):
        version = data.get('version')
    else:
        version = data
        data = {'version': version}
    if version is None:
        print(f"Warning: {name} version could not be determined, skipping check.")
        return
    repo_version = read_repo_version(version_file)
    if version != repo_version:
        print(f"New version of {name} is available: {version}, updating version file.")
        write_repo_version(version_file, version)
        notify_telegram(message_fmt.format(**data))
    else:
        print(f"Latest {name} is the same as the repository, skipping.")
