import os
from core.version_check import fetch_json, run_check

URL = "https://api.github.com/repos/microsoft/XmlNotepad/releases/latest"


def fetch_xmlnp():
    data = fetch_json(URL)
    return {"version": data["tag_name"], "url": data["html_url"]}


if __name__ == "__main__":
    run_check(
        "XmlNotepad",
        fetch_xmlnp,
        os.path.join("updates", "LATEST_XMLNP"),
        "\U0001F4DD XmlNotepad: new version available! {version} \nDownload from {url}",
    )
