import requests
import os
from dotenv import load_dotenv

# Load your token from .env
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")
private_repo = os.getenv("PRIVATE_REPO_NAME")

print("=" * 50)
print("🔍 GITHUB API ACCESS TEST")
print("=" * 50)

# 1. Public Access (No Token)
print("\n📢 PUBLIC ACCESS (No Token):")
response = requests.get(f"https://api.github.com/users/{username}/repos")
if response.status_code == 200:
    repos = response.json()
    public_count = len([r for r in repos if not r['private']])
    print(f"✅ Found {public_count} public repositories")
    print(f"   Sample: {[r['name'] for r in repos[:3]]}")
else:
    print(f"❌ Error: {response.status_code}")

# 2. Try accessing private repo WITHOUT token
print("\n🔒 Attempting private repo WITHOUT token:")
url = f"https://api.github.com/repos/{username}/{private_repo}/contents"
response = requests.get(url)
print(f"   Status: {response.status_code}")
if response.status_code == 404:
    print("   ✅ Correct! Cannot access private repo without token")
    print(f"   Message: {response.json().get('message', 'Not found')}")

# 3. Access WITH token
print("\n🔓 Attempting private repo WITH token:")
headers = {"Authorization": f"token {token}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ SUCCESS! Accessed private repository")
    contents = response.json()
    print(f"\n📁 Contents of '{private_repo}':")
    for item in contents[:5]:  # Show first 5 items
        item_type = "📄" if item['type'] == 'file' else "📁"
        print(f"   {item_type} {item['name']}")
else:
    print(f"❌ Failed: {response.status_code}")
    print(f"   Message: {response.json().get('message', 'Unknown error')}")

print("\n" + "=" * 50)