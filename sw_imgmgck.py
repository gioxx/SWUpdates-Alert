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

def checkversion(imgmgckversion):
    if (imgmgckversion != checkrepo(os.path.join("updates","LATEST_IMGMGCK"))):
        print("New version of ImageMagick is available: %s, i'm updating version file." % imgmgckversion)
        writenewversion(os.path.join("updates","LATEST_IMGMGCK"),imgmgckversion)
        sendtotelegram("🖼️ ImageMagick: new version available! %s \nDownload from %s (or, as alternative, https://imagemagick.org/script/download.php)" % (imgmgckversion,imgmgckJson["html_url"]))
    else:
        print("Latest ImageMagick is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

imgmgckJson = sourceJson("https://api.github.com/repos/ImageMagick/ImageMagick/releases/latest") # Credits: https://stackoverflow.com/a/60716112/2220346
checkversion(imgmgckJson["tag_name"])
