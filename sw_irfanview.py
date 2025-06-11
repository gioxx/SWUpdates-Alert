import os
import re
from core.version_check import fetch_url, run_check

URL = "https://www.irfanview.com/"


def fetch_irfanview():
    data = fetch_url(URL).text
    match = re.search(r"IrfanView\s*v?(\d+(?:\.\d+)*)", data, re.IGNORECASE)
    if match:
        return {"version": match.group(1), "url": URL}
    return None


if __name__ == "__main__":
    run_check(
        "IrfanView",
        fetch_irfanview,
        os.path.join("updates", "LATEST_IRFANVIEW"),
        "\U0001F5BC IrfanView: new version {version}! \nDownload from {url}",
    )
