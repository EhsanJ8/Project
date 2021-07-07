import requests
import json

from requests.models import Response

url="https://api.telegram.org/bot1848540350:AAG5JclNyx3863mB19cvYGlx5K8Adlcvge4/"

def get_all_updates():
    reponse=requests.get(url + "getUpdates")
    return reponse.json()

def get_last_update(allupdates):
    return allupdates["result"][-1]

data = get_last_update(get_all_updates())
# print(data)
def get_chat_id(update):
    return update['message']['chat']['id']

def send_message(chat_id , text):
    send = {
        'chat_id' : chat_id,
        'text' : text
            }
    respond = requests.post(url+"sendMessage" , send)
    return respond

# send_message(get_chat_id(data) , 'Hello')




