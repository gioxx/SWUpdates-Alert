import os
import re
import requests
from core.version_check import run_check


URL = "https://filezilla-project.org/download.php?show_all=1"


def get_latest_version_from_html(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html_content = response.text
        match = re.search(r'FileZilla_(\d+\.\d+\.\d+)_', html_content)
        if match:
            return match.group(1)
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
    return None


def fetch_filezilla():
    version = get_latest_version_from_html(URL)
    return {"version": version}


if __name__ == "__main__":
    run_check(
        "FileZilla",
        fetch_filezilla,
        os.path.join("updates", "LATEST_FILEZILLA"),
        "\U0001F50C FileZilla: new version available! {version}\nDownload from " + URL,
    )
