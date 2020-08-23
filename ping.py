import time
from sanic import request
from sanic.response import text

class PingHandler:
    def __init__(self, maxpps, signature):
        self.maxpps = maxpps
        self.signature = signature
    
    def on_ping(self, request: request):
        print(request.ip)
        time.sleep(0.25)
        return text("Cool, See ya later")
