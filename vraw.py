import json
import requests
from requests.auth import HTTPBasicAuth

token = open("tokens/streamable_token.txt", "r").read().splitlines()
base_url = "https://api.streamable.com/"


def get_streamable(url):
    api_url = f"{base_url}import"
    payload = {
        'url': url
    }

    response = requests.get(api_url, auth=HTTPBasicAuth(token[0], token[1]), params=payload)
    if response.status_code == 200:
        return video_url(response.content)
    else:
        print(f"Error: {response.content}")


def video_url(content):
    # Returns the url of the uploaded video
    # If an error occurred on Streamables end, return None
    json_obj = json.loads(content.decode('utf-8'))
    if json_obj["status"] != 1:
        result = None
    else:
        result = f"https://streamable.com/{json_obj['shortcode']}"
    return result


def main():
    get_streamable("https://www.reddit.com/r/recipes/comments/c02vpe/lemon_pie_french_chef_christophe_michalak/")


if __name__ == "__main__":
    main()
