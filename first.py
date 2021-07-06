import requests
import json

url="https://api.telegram.org/bot1848540350:AAG5JclNyx3863mB19cvYGlx5K8Adlcvge4/"

def get_all_updates():
    reponse=requests.get(url + "getUpdates")
    return reponse.json()

def get_last_update(allupdates):
    return allupdates["result"][-1]


data=get_all_updates()
lastupdate=get_last_update(data)
print()
