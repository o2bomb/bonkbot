import requests
import time

token = open("tokens/tts_token.txt", "r").read()
base_url = "https://api.voicerss.org/"


def get_tts(source, language, speed):
    api_url = f"{base_url}"
    payload = {
        'key': token,
        'src': source,
        'hl': language,
        'r': speed,
        'c': 'MP3',
        'f': '48khz_16bit_stereo'
    }

    response = requests.get(api_url, params=payload)
    if response.status_code == 200:
        with open("temp/tts.mp3", "wb") as f:
            f.write(response.content)
    else:
        print(f"Error: {response.content}")


def main():
    get_tts("hello dude", "en-us", "-1")


if __name__ == "__main__":
    main()
