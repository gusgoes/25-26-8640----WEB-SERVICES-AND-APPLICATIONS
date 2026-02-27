from github import Github
from github import Auth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your credentials from .env
token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")
private_repo = os.getenv("PRIVATE_REPO_NAME")

print("=" * 50)
print("📦 USING PYGITHUB PACKAGE")
print("=" * 50)

# Check if token exists
if not token:
    print("❌ ERROR: GITHUB_TOKEN not found in .env file")
    print("   Make sure your .env file contains: GITHUB_TOKEN=your_token_here")
    exit()

# Authenticate with GitHub
auth = Auth.Token(token)
g = Github(auth=auth)

try:
    # Get authenticated user
    user = g.get_user()
    print(f"\n✅ Authenticated as: {user.login}")
    
    # Access private repository
    print(f"\n📁 Accessing private repo: {private_repo}")
    repo = user.get_repo(private_repo)
    
    # Get repository contents
    print(f"\n📄 Contents:")
    contents = repo.get_contents("")
    for i, content in enumerate(contents[:5], 1):
        emoji = "📄" if content.type == "file" else "📁"
        print(f"   {i}. {emoji} {content.path}")
    
    # Get latest commit - FIXED VERSION
    print(f"\n🔄 Latest commit:")
    commits = repo.get_commits()
    if commits and commits.totalCount > 0:
        commit = commits[0]
        message = commit.commit.message
        # Truncate message safely
        if len(message) > 50:
            message = message[:47] + "..."
        print(f"   Message: {message}")
        print(f"   Author: {commit.commit.author.name}")
        print(f"   Date: {commit.commit.author.date}")
    
    # Close connection
    g.close()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)