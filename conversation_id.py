import os
import requests
from dotenv import load_dotenv  # pip install python-dotenv

# Step 1: Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found! Please set ELEVENLABS_API_KEY in your .env file.")

CONVERSATION_ID = "conv_2401k3ckwkt9ecc99b12231eg3g8"

# Step 3: API Endpoint
url = f"https://api.elevenlabs.io/v1/convai/conversations/{CONVERSATION_ID}/audio"

headers = {
    "xi-api-key": API_KEY
}

# Step 4: Request audio file
response = requests.get(url, headers=headers, stream=True)

if response.status_code == 200:
    file_name = f"{CONVERSATION_ID}.mp3"
    with open(file_name, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f"Audio file downloaded successfully: {file_name}")
else:
    print(f"Failed to fetch audio. Status code: {response.status_code}")
    print(response.text)
