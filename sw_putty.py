import urllib.request
import ssl
import os
import os.path
import re
from jsondiff import diff
from include_tgram import *

# New method credits: https://github.com/0install/apps/blob/master/gui/putty.watch.py

def sourceWeb(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(path).read().decode('utf-8')
    
    excluded_versions = ['0.45', '0.46', '0.47', '0.48', '0.49', '0.50', '0.51']

    data = urllib.request.urlopen(path).read().decode('utf-8')
    matches = re.findall(r'>([0-9.]+)<\/a>\n\(released (....-..-..)', data)
    releases = [{'version': match[0], 'released': match[1]} for match in matches if not match[0] in excluded_versions]

    return releases[0]["version"]

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(ptversion):
    if (ptversion != checkrepo(os.path.join("updates","LATEST_PUTTY"))):
        print("New version of PuTTY is available: %s, i'm updating version file." % ptversion)
        writenewversion(os.path.join("updates","LATEST_PUTTY"),ptversion)
        sendtotelegram("🔌 PuTTY: new version available! %s \nDownload from https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" % ptversion)
    else:
        print("Latest PuTTY is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

ptversion = sourceWeb("https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html")
checkversion(ptversion)
