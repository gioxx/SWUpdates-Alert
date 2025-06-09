import os
import requests
from core.version_check import fetch_json, run_check


URL = "https://update.filezilla-project.org/update.php?type=client&channel=release&format=1"


def fetch_filezilla():
    try:
        data = fetch_json(URL)
        return data.get("version")
    except requests.RequestException as e:
        print(f"Error fetching FileZilla update information: {e}")
        return None


if __name__ == "__main__":
    run_check(
        "FileZilla",
        fetch_filezilla,
        os.path.join("updates", "LATEST_FILEZILLA"),
        "\U0001F50C FileZilla: new version available! {version}\nDownload from " + URL,
    )
