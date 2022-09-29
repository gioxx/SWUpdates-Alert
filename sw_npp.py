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
    urllib.request.urlretrieve(path,"npp.json")
    with open("npp.json", 'r') as f:
        response = json.load(f)
    os.remove("npp.json")
    return response

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(nppversion):
    if (nppversion != checkrepo(os.path.join("updates","LATEST_NPP"))):
        print("New version of Notepad++ is available: %s, i'm updating version file." % nppversion)
        writenewversion(os.path.join("updates","LATEST_NPP"),nppversion)
        sendtotelegram("📝 Notepad%s%s: new version available! %s \nDownload from %s" % ("+","+",nppversion,nppJson["html_url"]))
    else:
        print("Latest Notepad++ is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

nppJson = sourceJson("https://api.github.com/repos/notepad-plus-plus/notepad-plus-plus/releases/latest") # Credits: https://stackoverflow.com/a/60716112/2220346
checkversion(nppJson["tag_name"])
