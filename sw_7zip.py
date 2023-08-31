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

def cleanVersion(filename):
    first_slash_index = filename.index("/", 1) # Trova l'indice del primo e del secondo "/" che delimitano la versione
    second_slash_index = filename.index("/", first_slash_index + 1)
    version = filename[first_slash_index + 1:second_slash_index] # Estrae la versione dalla stringa
    return version

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(sevenzipVersion):
    if (sevenzipVersion != checkrepo(os.path.join("updates","LATEST_7ZIP"))):
        print("New version of 7-Zip is available: %s, i'm updating version file." % sevenzipVersion)
        writenewversion(os.path.join("updates","LATEST_7ZIP"),sevenzipVersion)
        sendtotelegram("🤐 7-Zip: new version %s available! \nDownload from %s" % (sevenzipVersion,sevenzipJson["release"]["url"]))
    else:
        print("Latest 7-Zip is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

sevenzipJson = sourceJson("https://sourceforge.net/projects/sevenzip/best_release.json") # Credits: https://github.com/UNT-CAS/SourceForge-API/blob/master/sourceforge.ps1
sevenzipCleanVersion = cleanVersion(sevenzipJson["release"]["filename"])
checkversion(sevenzipCleanVersion)
