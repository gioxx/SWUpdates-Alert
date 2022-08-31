import requests
import urllib.request
import ssl
import base64
import json
import os
import os.path
import sys
from jsondiff import diff
from include_tgram import *

def sourceJson(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(path,"filezilla.json")
    with open("filezilla.json", 'r') as f:
        response = json.load(f)
    os.remove("filezilla.json")
    return response["version"]

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(fzversion):
    if (fzversion != checkrepo(os.path.join("updates","LATEST_FILEZILLA"))):
        print("New version of FileZilla is available: %s, i'm updating version file." % fzversion)
        writenewversion(os.path.join("updates","LATEST_FILEZILLA"),fzversion)
        sendtotelegram("🔌 FileZilla: new version available! %s" % fzversion)
        sendtotelegram("Download from https://filezilla-project.org/download.php?show_all=1")
    else:
        print("Latest FileZilla is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

fzversion = sourceJson("https://raw.githubusercontent.com/akirco/aki-apps/master/bucket/filezilla.json")
checkversion(fzversion)
