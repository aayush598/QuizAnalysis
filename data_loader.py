import os
import json
import requests

def load_json(source, from_link=False):
    """
    Load JSON data from either a local file or an API URL.
    
    :param source: File path (if local) or API URL (if link).
    :param from_link: Boolean flag, True to fetch from URL, False for local file.
    :return: Parsed JSON data or None if an error occurs.
    """
    try:
        if from_link:
            response = requests.get(source, verify=False)  # Disable SSL verification if needed
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Data successfully fetched from API: {source}")
                return data
            else:
                print(f"❌ Failed to fetch data. Status Code: {response.status_code}")
                return None
        else:
            if os.path.exists(source):  # Check if file exists
                with open(source, "r", encoding="utf-8") as file:
                    data = json.load(file)
                print(f"✅ Data successfully loaded from local file: {source}")
                return data
            else:
                print(f"❌ File not found: {source}")
                return None

    except Exception as e:
        print(f"⚠️ Error fetching data: {e}")
        return None
