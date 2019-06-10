import json
import requests
import pyperclip

token = open("tokens/weather_token.txt", "r").read()
base_url = "https://api.openweathermap.org/data/2.5/"


def get_current_weather(city, country):
    api_url = f"{base_url}weather"

    if country:
        country = f",{country}"
    payload = {
        'APPID': token,
        'q': city + country,
        'units': 'metric'
    }

    response = requests.get(api_url, params=payload)
    if response.status_code == 200:
        return package(response.content)
    else:
        return response.content


def package(content):
    json_obj = json.loads(content.decode('utf-8'))
    json_obj.pop("coord")
    json_obj.pop("base")
    json_obj.pop("wind")
    json_obj.pop("clouds")
    json_obj.pop("dt")
    json_obj.pop("cod")
    return json_obj


def main():
    response = get_current_weather("perth", "au")
    pyperclip.copy(str(response))
    print(response)


if __name__ == "__main__":
    main()
