import os
import re
import ssl
import urllib.request
from core.version_check import run_check

URL = "https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html"
DOWNLOAD_URL = "https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"


def fetch_putty():
    if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(URL).read().decode('utf-8')
    excluded_versions = ['0.45', '0.46', '0.47', '0.48', '0.49', '0.50', '0.51']
    matches = re.findall(r'>([0-9.]+)<\/a>\n\(released (....-..-..)', data)
    releases = [m for m in matches if m[0] not in excluded_versions]
    return {"version": releases[0][0]}


if __name__ == "__main__":
    run_check(
        "PuTTY",
        fetch_putty,
        os.path.join("updates", "LATEST_PUTTY"),
        "\U0001F50C PuTTY: new version available! {version} \nDownload from " + DOWNLOAD_URL,
    )
