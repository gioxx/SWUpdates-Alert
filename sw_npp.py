import os
from core.version_check import fetch_json, run_check

URL = "https://api.github.com/repos/notepad-plus-plus/notepad-plus-plus/releases/latest"


def fetch_npp():
    data = fetch_json(URL)
    return {"version": data["tag_name"], "url": data["html_url"]}


if __name__ == "__main__":
    run_check(
        "Notepad++",
        fetch_npp,
        os.path.join("updates", "LATEST_NPP"),
        "\U0001F4DD Notepad\u2795\u2795: new version available! {version} \nDownload from {url}",
    )
