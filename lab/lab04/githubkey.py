import requests
from config import config as cfg
import json

url = "https://github.com/gusgoes/privateapi"
apikey = cfg["githubkey"]
filename = "repo.json"
response = requests.get(url, auth=('token', apikey)) 
repoJSON = response.json() 
#print (response.json()) 
with open(filename, 'w') as fp: json.dump(repoJSON, fp, indent=4) 