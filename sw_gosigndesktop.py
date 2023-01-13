import urllib.request
import hashlib
import ssl
import os
import os.path
from include_tgram import *

def sourceWeb(path):
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): # Credits: https://moreless.medium.com/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c
        ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(path)
    data = response.read()
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(gsdmd5):
    if (gsdmd5 != checkrepo(os.path.join("updates","LATEST_GOSIGNDESKTOP"))):
        print("New version of GoSign Desktop is available: %s, i'm updating version file." % gsdmd5)
        writenewversion(os.path.join("updates","LATEST_GOSIGNDESKTOP"),gsdmd5)
        #sendtotelegram("✏️ GoSign Desktop: new version available! Updated MD5: %s \nDownload from https://rinnovofirma.infocert.it/gosign/download/win32/latest/" % gsdmd5)
    else:
        print("Latest GoSign Desktop is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

gsdmd5 = sourceWeb("https://rinnovofirma.infocert.it/gosign/download/win32/latest/")
checkversion(gsdmd5)