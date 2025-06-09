import os
import ssl
import requests
from include_tgram import sendtotelegram


def fetch_url(url, verify_ssl=True):
    """Return a requests.Response object with optional SSL verification."""
    if (
        not verify_ssl
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning
        )
    response = requests.get(url, verify=verify_ssl)
    response.raise_for_status()
    return response


def fetch_json(url, verify_ssl=True):
    """Retrieve JSON data from URL with optional SSL verification."""
    response = fetch_url(url, verify_ssl=verify_ssl)
    return response.json()


def read_repo_version(filename):
    """Read first line of version file, return None if file missing."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as fh:
        content = fh.read()
        return content.split('\n', 1)[0]


def write_repo_version(filename, version):
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
