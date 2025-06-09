import os
from core.version_check import fetch_json, run_check

URL = "https://api.github.com/repos/cyanfish/naps2/releases/latest"


def fetch_naps2():
    data = fetch_json(URL)
    return {"version": data["tag_name"], "url": data["html_url"]}


if __name__ == "__main__":
    run_check(
        "NAPS2",
        fetch_naps2,
        os.path.join("updates", "LATEST_NAPS2"),
        "\U0001F5A8\uFE0F NAPS2: new version available! {version} \nDownload from {url}",
    )
