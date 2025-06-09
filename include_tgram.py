#from dotenv import load_dotenv, find_dotenv
import os
import os.path
import requests

def sendtotelegram(message):
    #load_dotenv(find_dotenv())
    token = os.environ.get("TGRAMTOKEN")
    chatid = os.environ.get("TGRAMCHATID")

    if not token:
        raise EnvironmentError("TGRAMTOKEN environment variable is missing")
    if not chatid:
        raise EnvironmentError("TGRAMCHATID environment variable is missing")

    url = f"https://api.telegram.org/bot{token.strip()}/sendMessage"
    response = requests.post(url, data={"chat_id": chatid.strip(), "text": message})
    return response
