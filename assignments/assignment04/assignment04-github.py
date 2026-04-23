from github import Github, Auth
from github.GithubException import GithubException
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import os

# Load .env from the same folder as this script
load_dotenv(Path(__file__).with_name(".env"))

token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("PRIVATE_REPO_NAME")

if not token:
    raise SystemExit("Missing GITHUB_TOKEN in .env")
if not repo_name:
    raise SystemExit("Missing PRIVATE_REPO_NAME in .env")

g = Github(auth=Auth.Token(token))
repo = g.get_user().get_repo(repo_name)

file_path = "week05_created.txt"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = f"This file was created by [assignment04-github.py](http://_vscodecontentref_/2) on {now}\n"

try:
    existing = repo.get_contents(file_path)
    repo.update_file(
        path=file_path,
        message="Update week05_created.txt via API",
        content=content,
        sha=existing.sha,
    )
    print("File updated:", file_path)
except GithubException as e:
    if e.status == 404:
        repo.create_file(
            path=file_path,
            message="Create week05_created.txt via API",
            content=content,
        )
        print("File created:", file_path)
    else:
        raise

g.close()