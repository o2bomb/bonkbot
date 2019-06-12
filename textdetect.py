import json
import requests

token = open("tokens/ocr_token.txt", "r").read()
base_url = "https://api.ocr.space/parse/image"


def get_parsed_text(url, language):
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
    print(get_parsed_text("https://i.imgur.com/ezDZSkB.jpg", "eng"))


if __name__ == "__main__":
    main()
