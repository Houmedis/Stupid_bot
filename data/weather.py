import requests
import sys


def Weather():
    api_server = f"https://api.weather.yandex.ru/v2/forecast/"
    params = {
        "lat": '2',
        'long': '2'
    }
    headers = {
        'X-Yandex-API-Key': '060e0331-e92f-472e-9d90-30c2095d3e8b',
    }
    response = requests.get(api_server, params=params, headers=headers)

    if response:
        json_response = response.json()
        sl_weather = {}
        sl_weather['temp'] = json_response['fact']['temp']  # Градусы C*
        sl_weather['feels_like'] = json_response['fact']['temp']  # Ощущается
        sl_weather['condition'] = json_response['fact']['condition']
        sl_weather['wind_speed'] = json_response['fact']['wind_speed']
        return sl_weather