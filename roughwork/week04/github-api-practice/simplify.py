from github import Github
import os
from dotenv import load_dotenv

#load token from .env file
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

#connect to github using token
g = Github(token)

#get user info
user = g.get_user()
print("Authenticated as:", user.login)

#get private repo
repo = user.get_repo("privateapi")  # replace with your private repo name

#list contents of repo
print("\nFiles in privateapi:")
content = repo.get_contents("")

for item in content:
    print("-", item.path)

g.close()