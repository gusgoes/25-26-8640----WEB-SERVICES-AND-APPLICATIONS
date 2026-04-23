import requests
import requests
from config import config as cfg

url = "https://api.github.com/repos/gusgoes/aprivateone"
headers = {
    "Authorization": f"Bearer {cfg['githubkey']}",
    "Accept": "application/vnd.github+json",
}

response = requests.get(url, headers=headers)

print("STATUS:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("First 300 chars of body:\n", response.text[:300])

if response.headers.get("Content-Type", "").startswith("application/json"):
    print("JSON message (if any):", response.json().get("message"))