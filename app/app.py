import requests
import dotenv
import os
dotenv.load_dotenv()


def call_api_and_return_json_data(api_url: str) -> dict:
    """
    Calls the Assabet calendar API and returns the response as a JSON object.
    Args: A string representing the API URL.
    Returns: A dictionary containing the JSON response from the API.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
    }

    response = requests.get(api_url, headers=headers)
    return response.json()


events = call_api_and_return_json_data(os.getenv("API_ALL_BRANCHES"))
print(events)
