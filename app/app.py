import requests
import dotenv
import os
dotenv.load_dotenv()



def call_api_and_return_json_data(api_url: str) -> dict:
    """
    Calls the Assabet calendar API and returns the response as a JSON object.
    """

    response = requests.get(api_url)
    return response.json()


events = call_api_and_return_json_data(os.getenv("API_ALL_BRANCHS"))