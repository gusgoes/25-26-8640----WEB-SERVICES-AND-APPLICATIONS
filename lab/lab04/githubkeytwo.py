from github import Github
from config import config as cfg
apikey = cfg["githubkey"] 
g = Github(apikey)
repo = g.get_repo("yourccount/yourrepo") 
print(repo.clone_url) 
fileInfo = repo.get_contents("test.txt") 
urlOfFile = fileInfo.download_url 