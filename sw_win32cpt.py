import os
from core.version_check import fetch_json, run_check

URL = "https://api.github.com/repos/microsoft/Microsoft-Win32-Content-Prep-Tool/releases/latest"


def fetch_win32cpt():
    data = fetch_json(URL)
    return {"version": data["tag_name"], "url": data["html_url"]}


if __name__ == "__main__":
    run_check(
        "Win32 Content Prep Tool",
        fetch_win32cpt,
        os.path.join("updates", "LATEST_WIN32CPT"),
        "\U0001F4BB Win32 Content Prep Tool: new version available! {version} \nDownload from {url}",
    )
