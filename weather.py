import json
import requests

token = open("tokens/weather_token.txt", "r").read()
base_url = "https://api.openweathermap.org/data/2.5/"


def get_current_weather(city, country):
    api_url = f"{base_url}weather"

    if country:
        country = f",{country}"
    payload = {
        'APPID': token,
        'q': city + country
    }

    response = requests.get(api_url, params=payload)
    if response.status_code == 200:
        return response.content
        # return json.loads(response.content.decode('utf-8'))
    else:
        return response.content


def main():
    response = get_current_weather("perth", "au")
    print(response)


if __name__ == "__main__":
    main()
