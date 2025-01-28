import requests
import re
import os
from include_tgram import *

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
            latest_version = match.group(1)
            return latest_version
        else:
            print("No matching version found in the HTML.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def checkrepo(updates_file):
    if not os.path.exists(updates_file):
        return None
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(fzversion):
    if not fzversion:
        print("No valid version found. Exiting.")
        return
    updates_file = os.path.join("updates", "LATEST_FILEZILLA")
    repo_version = checkrepo(updates_file)

    if fzversion != repo_version:
        print(f"New version of FileZilla is available: {fzversion}, updating version file.")
        writenewversion(updates_file, fzversion)
        sendtotelegram(f"🔌 FileZilla: new version available! {fzversion}\nDownload from https://filezilla-project.org/download.php?show_all=1")
    else:
        print("Latest FileZilla is the same as the repository, skipping.")

def writenewversion(updates_file, newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

url = "https://filezilla-project.org/download.php?show_all=1"
fzversion = get_latest_version_from_html(url)
print(f"Latest version found: {fzversion}")
checkversion(fzversion)
