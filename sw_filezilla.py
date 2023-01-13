import urllib.request
import ssl
import os
import os.path
import re
from jsondiff import diff
from include_tgram import *

# New method credits: https://github.com/0install/apps/blob/master/gui/filezilla.watch.py

def sourceWeb(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(path).read().decode('utf-8')
    matches = re.findall(r'<h3>([0-9\.]+) \((....-..-..)\)</h3>', data)
    releases = [{'version': match[0], 'released': match[1]} for match in matches if int(match[1][0:4]) >= 2022]
    return releases[0]["version"]

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

fzversion = sourceWeb("https://filezilla-project.org/versions.php")
checkversion(fzversion)
