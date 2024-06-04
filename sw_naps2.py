import requests
import ssl
import json
import os
import os.path
from jsondiff import diff
from include_tgram import *

def sourceJson(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    response = json.loads(requests.get(path).text)
    return response

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(naps2version):
    if (naps2version != checkrepo(os.path.join("updates","LATEST_NAPS2"))):
        print("New version of NAPS2 is available: %s, i'm updating version file." % naps2version)
        writenewversion(os.path.join("updates","LATEST_NAPS2"),naps2version)
        sendtotelegram("🖨️ NAPS2: new version available! %s \nDownload from %s" % (naps2version,napsJson["html_url"]))
    else:
        print("Latest NAPS2 is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

napsJson = sourceJson("https://api.github.com/repos/cyanfish/naps2/releases/latest") # Credits: https://stackoverflow.com/a/60716112/2220346
checkversion(napsJson["tag_name"])
