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

def checkversion(xmlnpversion):
    if (xmlnpversion != checkrepo(os.path.join("updates","LATEST_XMLNP"))):
        print("New version of XmlNotepad is available: %s, i'm updating version file." % xmlnpversion)
        writenewversion(os.path.join("updates","LATEST_XMLNP"),xmlnpversion)
        sendtotelegram("📝 XmlNotepad: new version available! %s \nDownload from %s" % (xmlnpversion,xmlnpJson["html_url"]))
    else:
        print("Latest XmlNotepad is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

xmlnpJson = sourceJson("https://api.github.com/repos/microsoft/XmlNotepad/releases/latest") # Credits: https://stackoverflow.com/a/60716112/2220346
checkversion(xmlnpJson["tag_name"])
