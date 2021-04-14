import requests
import sys


def Weather(name): 
    api_server = "http://www.last.fm/api/auth/"
    
    params = {
        "api_key": '3908d5de623b9e04c132d0808cc278fc'
    }
    response = requests.get(api_server, params=params)