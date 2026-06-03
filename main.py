import requests
from random import randint, choice
import os
import json
from time import sleep
from secrets import *


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)


def create_datatype(url, text):
  datatype = {
    "caption": text,
    "type": 'photo',
    "media": url
  }
  return datatype


cat_url = "https://api.thecatapi.com/v1/images/search"
joke_url = "http://shortiki.com/export/api.php"
clear_folder(folder_path = 'images')


parameters = {
    "format": "json",
    "type": "top",
    "amount": "100"
}
while True:

    esli =  randint(3, 6)

    response = requests.get(joke_url, params=parameters)
    response.raise_for_status()
    random_joke = choice(response.json())['content']


    #for i in range(1, esli + 1):
    #    response = requests.get(cat_url)
        # response.raise_for_status()
        # response2 = requests.get(response.json()[0]["url"])
        # with open(f'images/cat{i}.jpeg', "wb") as file:
        #     file.write(response2.content)


    list_datatype = []
    for i in range(1, esli + 1):
        response = requests.get(cat_url)
        datatype = create_datatype(response.json()[0]["url"], random_joke)
        list_datatype.append(datatype)

    list_datatype = json.dumps(list_datatype)


    url = f'https://api.telegram.org/bot{telegram}/sendMediaGroup'
    Params = {"chat_id":canal_id, "media":list_datatype}
    response = requests.post(url, Params)
    print(response.json())
    sleep(20)
  
  
