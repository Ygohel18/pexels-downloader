import os
import requests
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("PEXELS_API_KEY")

if not API_KEY:
    print("Error: API key is missing!")
    exit(1)

collection_id = "ritss5w"
url = f"https://api.pexels.com/v1/collections/{collection_id}?per_page=2"
headers = {"Authorization": API_KEY}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
