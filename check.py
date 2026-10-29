"""Check every monitored software and update its file under updates/ when a new version is out."""
import hashlib
import os
import re
import sys
import traceback

from core.version_check import fetch_json, fetch_url, run_check

FILEZILLA_URL = "https://filezilla-project.org/download.php?type=client"
# The site answers 403 to non-browser clients (its update.php endpoint refuses third parties outright).
BROWSER_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"}
FIREFOX_URL = "https://product-details.mozilla.org/1.0/firefox_versions.json"
FIRMA4NG_URL = "https://card.infocamere.it/infocard/FileDocManager/download?file=/firma4ng/Firma4ng_win.zip"
IRFANVIEW_URL = "https://www.irfanview.com/"
# Official download mirror: /latest/ redirects to /<version>/. chiark itself is often unreachable from GitHub runners.
PUTTY_URL = "https://the.earth.li/~sgtatham/putty/latest/"
PUTTY_DOWNLOAD_URL = "https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"


def clean_version(filename):
    first_slash_index = filename.index("/", 1)
    second_slash_index = filename.index("/", first_slash_index + 1)
    return filename[first_slash_index + 1:second_slash_index]


def fetch_sevenzip():
    data = fetch_json("https://sourceforge.net/projects/sevenzip/best_release.json")
    return {"version": clean_version(data["release"]["filename"]), "url": data["release"]["url"]}


def fetch_filezilla():
    match = re.search(r"Download FileZilla Client (\d+(?:\.\d+)+)", fetch_url(FILEZILLA_URL, headers=BROWSER_UA).text)
    return {"version": match.group(1)} if match else None


def fetch_firefox(channel):
    return {"version": fetch_json(FIREFOX_URL)[channel]}


def fetch_firma4ng():
    # Streamed so the read timeout applies per chunk instead of the whole zip hanging the run.
    md5 = hashlib.md5()
    with fetch_url(FIRMA4NG_URL, verify_ssl=False, stream=True) as response:
        for chunk in response.iter_content(chunk_size=1 << 16):
            md5.update(chunk)
    return {"version": md5.hexdigest()}


def fetch_github_release(repo):
    data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
    return {"version": data["tag_name"], "url": data["html_url"]}


def fetch_irfanview():
    match = re.search(r"version\s+(\d+\.\d+)", fetch_url(IRFANVIEW_URL).text, re.IGNORECASE)
    if match:
        return {"version": match.group(1), "url": IRFANVIEW_URL}
    return None


def fetch_putty():
    match = re.search(r"/putty/(\d+(?:\.\d+)+)/$", fetch_url(PUTTY_URL).url)
    return {"version": match.group(1)} if match else None


# (name, fetch function, file under updates/ read by external tools: do not rename, Telegram message)
CHECKS = [
    ("7-Zip", fetch_sevenzip, "LATEST_7ZIP",
     "\U0001F910 7-Zip: new version {version} available! \nDownload from {url}"),
    ("FileZilla", fetch_filezilla, "LATEST_FILEZILLA",
     "\U0001F50C FileZilla: new version available! {version}\nDownload from " + FILEZILLA_URL),
    ("Firefox ESR", lambda: fetch_firefox("FIREFOX_ESR"), "FIREFOX_ESR",
     "\U0001F468‍\U0001F4BB Firefox ESR: new version {version} now available! \nDownload from https://www.mozilla.org/firefox/enterprise/#download"),
    ("Firefox", lambda: fetch_firefox("LATEST_FIREFOX_VERSION"), "LATEST_FIREFOX_VERSION",
     "\U0001F468‍\U0001F4BB Firefox (Stable): new version {version} available! \nDownload from https://www.mozilla.org/firefox/new/"),
    ("Firma4NG", fetch_firma4ng, "LATEST_FIRMA4NG",
     "✏️ Firma4NG: new version available! Updated MD5:{version} \nDownload from " + FIRMA4NG_URL),
    ("ImageMagick", lambda: fetch_github_release("ImageMagick/ImageMagick"), "LATEST_IMGMGCK",
     "\U0001F5BC️ ImageMagick: new version available! {version} \nDownload from {url} (or, as alternative, https://imagemagick.org/script/download.php)"),
    ("IrfanView", fetch_irfanview, "LATEST_IRFANVIEW",
     "\U0001F5BC IrfanView: new version {version}! \nDownload from {url}"),
    ("NAPS2", lambda: fetch_github_release("cyanfish/naps2"), "LATEST_NAPS2",
     "\U0001F5A8️ NAPS2: new version available! {version} \nDownload from {url}"),
    ("Notepad++", lambda: fetch_github_release("notepad-plus-plus/notepad-plus-plus"), "LATEST_NPP",
     "\U0001F4DD Notepad➕➕: new version available! {version} \nDownload from {url}"),
    ("PowerShell", lambda: fetch_github_release("PowerShell/PowerShell"), "LATEST_PWSH",
     "\U0001F41A PowerShell: new version available! {version} \nDownload from {url}"),
    ("PuTTY", fetch_putty, "LATEST_PUTTY",
     "\U0001F50C PuTTY: new version available! {version} \nDownload from " + PUTTY_DOWNLOAD_URL),
    ("Win32 Content Prep Tool", lambda: fetch_github_release("microsoft/Microsoft-Win32-Content-Prep-Tool"), "LATEST_WIN32CPT",
     "\U0001F4BB Win32 Content Prep Tool: new version available! {version} \nDownload from {url}"),
    ("XmlNotepad", lambda: fetch_github_release("microsoft/XmlNotepad"), "LATEST_XMLNP",
     "\U0001F4DD XmlNotepad: new version available! {version} \nDownload from {url}"),
]


def main(only=None):
    failed = []
    for name, fetch_fn, filename, message in CHECKS:
        if only and name.lower() not in only:
            continue
        try:
            run_check(name, fetch_fn, os.path.join("updates", filename), message)
        except Exception:
            traceback.print_exc()
            failed.append(name)
    if failed:
        print(f"Failed checks: {', '.join(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main([a.lower() for a in sys.argv[1:]]))
