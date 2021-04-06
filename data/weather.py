import requests
import sys


def Weather(name):
    pos = ['2', '2']
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        pos = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()    
    api_server = f"https://api.weather.yandex.ru/v2/forecast/"
    
    params = {
        "lat": pos[0],
        'long': pos[1]
    }
    headers = {
        'X-Yandex-API-Key': '060e0331-e92f-472e-9d90-30c2095d3e8b',
    }
    response = requests.get(api_server, params=params, headers=headers)
    print(response)
    if response:
        json_response = response.json()
        sl_weather = {}
        sl_weather['temp'] = json_response['fact']['temp']  # Градусы C*
        sl_weather['feels_like'] = json_response['fact']['temp']  # Ощущается
        sl_weather['condition'] = json_response['fact']['condition']
        sl_weather['wind_speed'] = json_response['fact']['wind_speed']
        return sl_weather
