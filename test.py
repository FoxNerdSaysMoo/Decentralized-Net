import requests
from utils import ThreadHandler
import time

url = "http://127.0.0.1:5050"

#responce = requests.get(url+"/ping", params={"Secret": "Boop!"})
#print(responce.text.replace('"', ''))

handler = ThreadHandler(6)

def boop(request):
    print("Boop")
    time.sleep(0.25)

handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)
handler.on_ping("Hi", boop)