import requests
import sys


def Chat_Bot(ask):
    api_server = "https://aiproject.ru/api/"
    params = {"ask":"Привет",
              "userid":"654321",
              "key":""
    }
    response = requests.post(api_server, params=params)
    if response:
        print(response.json())


Chat_Bot('a')