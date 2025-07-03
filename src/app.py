import requests
import dotenv
import os
import json
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


def write_json_to_file(json_data: dict, file_path: str) -> bool:
    """
    Writes the JSON data to a file.
    Args:
        - json_data: dict containing the JSON data to write
        - file_path: str representing the path to the file where the data will be written
    Returns:
        - True if successful, False if not.
    """
    full_file_path = os.path.join(os.getcwd(), "src", "storage", file_path)
    file_exists = os.path.exists(full_file_path)

    if not file_exists:
        try:
            os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
            print(f"Directory created: {os.path.dirname(full_file_path)}")
        except OSError as e:
            print(f"An error occurred while creating the directory: {e}")
            return False

    try:
        with open(full_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        print(f"Data written to {full_file_path}")
        return True

    except OSError as e:
        print(f"An error occurred while writing to the file: {e}")
        return False

    finally:
        file.close()


def print_orderly_events(events: dict) -> None:
    for event in events:
        current_event = event[0]
        print(f"Event: {current_event['title']}")


def search_branch(event, search_branch: str) -> bool:
    """
    Searches for a branch in the API response dict and returns true if branch is found.
    Arguments: 
        - event: dict containing event details
        - search_branch: str representing the branch name to search for
    Returns: 
        - True if branch is included
        - False if not.
    """
    name_matches = False
    branch_name = event['locations'][0]['location_name']
    if branch_name.lower() == search_branch.lower():
        name_matches = True

    return name_matches


def display_event_info(event: dict) -> None:
    """
    Displays the event information in a readable format.
    Arguments:
        - event: dict containing event details
    Returns:
        - None
    """
    print(f"Title: {event['title']}")
    print(f"Date: {event['start_date']}")
    print(f"Time: {event['start_time']} - {event['end_time']}")
    print(f"Location: {event['locations'][0]['location_name']}")
    print("\n")


events = call_api_and_return_json_data(os.getenv("API_ALL_BRANCHES"))
write_json_to_file(events, "all-events.json")

for event in events:
    if search_branch(event[0], "West Meeting Room"):
        display_event_info(event[0])
