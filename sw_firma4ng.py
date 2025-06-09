import hashlib
import os
import ssl
import urllib.request
from core.version_check import run_check

URL = "https://card.infocamere.it/infocard/FileDocManager/download?file=/firma4ng/Firma4ng_win.zip"


def fetch_firma4ng():
    if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(URL).read()
    md5 = hashlib.md5()
    md5.update(data)
    return {"version": md5.hexdigest()}


if __name__ == "__main__":
    run_check(
        "Firma4NG",
        fetch_firma4ng,
        os.path.join("updates", "LATEST_FIRMA4NG"),
        "\u270F\uFE0F Firma4NG: new version available! Updated MD5:{version} \nDownload from " + URL,
    )
