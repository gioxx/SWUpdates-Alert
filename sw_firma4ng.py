import hashlib
import os
from core.version_check import run_check, fetch_url

URL = "https://card.infocamere.it/infocard/FileDocManager/download?file=/firma4ng/Firma4ng_win.zip"


def fetch_firma4ng():
    data = fetch_url(URL, verify_ssl=False).content
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
