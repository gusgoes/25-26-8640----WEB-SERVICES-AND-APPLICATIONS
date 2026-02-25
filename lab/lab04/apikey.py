from config import config as cfg
import requests
import urllib.parse

targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html" 
apikey = cfg["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate' 
 
params = {'url': targetUrl,'apiKey': apikey} 
parsedparams = urllib.parse.urlencode(params) 
requestUrl = apiurl +"?" + parsedparams  
 
response = requests.get(requestUrl) 
print (response.status_code) 
 
result =response.content