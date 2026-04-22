import requests
import os
from lab import config

config()

# Public data - no token needed
username = os.getenv("GITHUB_USERNAME")

# Get user info
print(f"\n📊 Fetching public info for user: {username}")
response = requests.get(f"https://api.github.com/users/{username}")

if response.status_code == 200:
    user_data = response.json()
    print(f"Name: {user_data.get('name', 'N/A')}")
    print(f"Public Repos: {user_data.get('public_repos', 0)}")
    print(f"Followers: {user_data.get('followers', 0)}")
else:
    print(f"Error: {response.status_code}")

# Get public repositories
print(f"\n📚 Public repositories for {username}:")
repos_response = requests.get(f"https://api.github.com/users/{username}/repos")

if repos_response.status_code == 200:
    repos = repos_response.json()
    for repo in repos[:5]:  # Show first 5
        print(f"  - {repo['name']} ({repo.get('language', 'Unknown')})")
    print(f"  ... and {len(repos) - 5} more" if len(repos) > 5 else "")
else:
    print(f"Error: {repos_response.status_code}")