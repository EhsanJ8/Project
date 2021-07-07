import requests
import json

url="https://api.telegram.org/bot1848540350:AAG5JclNyx3863mB19cvYGlx5K8Adlcvge4/"

guide_note= "This quiz has 30 question and After each question you should submit your Answer with sending a NUMBER from 1-4 of choices. "

def get_all_updates():
    response=requests.get(url + "getUpdates")
    return response.json()

def get_last_update(allupdates):
    return allupdates["result"][-1]

def get_chat_id(update):
    return update["message"]["chat"]["id"]

def sendMessage(chat_id , text):
    sendData={
        "caht_id" : chat_id,
        "text" : text
    }

    response = requests.post(url + "sendMessage",sendData)
    return response

data=get_all_updates()
lastupdate=get_last_update(data)
if lastupdate["message"]["text"]=="/start":
    sendMessage(get_chat_id(lastupdate),guide_note)



print()
