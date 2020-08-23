import requests
import time

url = "http://127.0.0.1:5050"

responce = requests.get(url+"/ping", params={"Secret": "Boop!"})
print(responce.text.replace('"', ''))
