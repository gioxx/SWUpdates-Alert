#from dotenv import load_dotenv, find_dotenv
import requests
import os
import os.path

def sendtotelegram(message):
    #load_dotenv(find_dotenv())
    token = os.environ.get("TGRAMTOKEN").strip()
    chatid = os.environ.get("TGRAMCHATID").strip()
    url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (token, chatid, message)
    response = requests.post(url)
    return response
