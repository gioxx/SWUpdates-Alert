import requests
import json
import os
import os.path
from jsondiff import diff
from include_tgram import *

def sourceJson(path,channel):
    response = json.loads(requests.get(path).text)
    return response[channel]

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(fxversion,channel):
    if (fxversion != checkrepo(os.path.join("updates",channel))):
        print("New version of " + channel + " is available: %s, i'm updating version file." % fxversion)
        writenewversion(os.path.join("updates",channel),fxversion)
        if (channel == "FIREFOX_ESR"):
            sendtotelegram("👨🏽‍💻 Firefox ESR: new version %s now available! \nDownload from https://www.mozilla.org/firefox/enterprise/#download" % fxversion)
        elif (channel == "LATEST_FIREFOX_VERSION"):
            sendtotelegram("👨🏽‍💻 Firefox (Stable): new version %s available! \nDownload from https://www.mozilla.org/firefox/new/" % fxversion)
        else:
            sendtotelegram("👨🏽‍💻 %s: new version %s available! \nDownload from https://www.mozilla.org/firefox/browsers/" % channel,fxversion)
    else:
        print("Latest " + channel + " is the same of the repository, skip.")

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return

channel = "FIREFOX_ESR"
fxversion = sourceJson("https://product-details.mozilla.org/1.0/firefox_versions.json",channel)
checkversion(fxversion,channel)

channel = "LATEST_FIREFOX_VERSION"
fxversion = sourceJson("https://product-details.mozilla.org/1.0/firefox_versions.json",channel)
checkversion(fxversion,channel)
