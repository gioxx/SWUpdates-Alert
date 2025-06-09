import os
from core.version_check import fetch_json, run_check

URL = "https://product-details.mozilla.org/1.0/firefox_versions.json"


def fetch_firefox(channel):
    data = fetch_json(URL)
    return {"version": data[channel]}


if __name__ == "__main__":
    run_check(
        "Firefox ESR",
        lambda: fetch_firefox("FIREFOX_ESR"),
        os.path.join("updates", "FIREFOX_ESR"),
        "\U0001F468\u200D\U0001F4BB Firefox ESR: new version {version} now available! \nDownload from https://www.mozilla.org/firefox/enterprise/#download",
    )
    run_check(
        "Firefox",
        lambda: fetch_firefox("LATEST_FIREFOX_VERSION"),
        os.path.join("updates", "LATEST_FIREFOX_VERSION"),
        "\U0001F468\u200D\U0001F4BB Firefox (Stable): new version {version} available! \nDownload from https://www.mozilla.org/firefox/new/",
    )
