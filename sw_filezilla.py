import feedparser
import re
import ssl
import os
import os.path
from jsondiff import diff
from include_tgram import *

def sourceWeb(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(path)
    if feed.entries:
        title = feed.entries[0].title
        match = re.search(r'FileZilla_(\d+\.\d+\.\d+)_', title)
        if match:
            latest_version = match.group(1)
            return latest_version
    return None

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(fzversion):
    if (fzversion != checkrepo(os.path.join("updates","LATEST_FILEZILLA"))):
        print("New version of FileZilla is available: %s, i'm updating version file." % fzversion)
        writenewversion(os.path.join("updates","LATEST_FILEZILLA"),fzversion)
        sendtotelegram("🔌 FileZilla: new version available! %s \nDownload from https://filezilla-project.org/download.php?show_all=1" % fzversion)
    else:
        print("Latest FileZilla is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

fzversion = sourceWeb("https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Ffilezilla-project.org%2Fdownload.php%3Fshow_all%3D1&in_id_or_class=downloadplatform&max=1&order=document&guid=0")
print(fzversion)
checkversion(fzversion)
