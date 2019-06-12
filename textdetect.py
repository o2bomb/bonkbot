import json
import requests

token = open("tokens/ocr_token.txt", "r").read()
base_url = "https://api.ocr.space/parse/image"


def get_parsed_text(url, language="eng"):
    # Returns the detected text from the specified
    # image URL and language to detect
    api_url = f"{base_url}url"
    payload = {
        'apikey': token,
        'url': url,
        'language': language
    }

    response = requests.get(api_url, params=payload)
    if response.status_code == 200:
        return text(response.content)
    else:
        print(f"Error: {response.content}")


def text(content):
    # Extract the parsed text from the imported content
    json_obj = json.loads(content.decode('utf-8'))
    parsed = json_obj["ParsedResults"][0]["ParsedText"]
    return parsed


def main():
    print(get_parsed_text("https://www.wikihow.com/images/thumb/2/21/Read-and-Write-Japanese-Fast-Step-12-Version-3.jpg/aid655240-v4-728px-Read-and-Write-Japanese-Fast-Step-12-Version-3.jpg ", "jpn"))
    # Language list:
    # Arabic = ara
    # Bulgarian = bul
    # Chinese(Simplified) = chs
    # Chinese(Traditional) = cht
    # Croatian = hrv
    # Czech = cze
    # Danish = dan
    # Dutch = dut
    # English = eng
    # Finnish = fin
    # French = fre
    # German = ger
    # Greek = gre
    # Hungarian = hun
    # Korean = kor
    # Italian = ita
    # Japanese = jpn
    # Polish = pol
    # Portuguese = por
    # Russian = rus
    # Slovenian = slv
    # Spanish = spa
    # Swedish = swe
    # Turkish = tur


if __name__ == "__main__":
    main()
