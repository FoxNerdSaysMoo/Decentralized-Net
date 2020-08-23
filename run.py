from threading import Thread
from sanic import Sanic
from sanic.response import text
from ping import PingHandler

app = Sanic("Litenet")
app.config.from_envvar('MYAPP_SETTINGS')


@app.route("/ping")
async def ping(request):
    responce = pingroute.on_ping(request)
    return responce

def run(app, debug):
    global pingroute
    pingroute = PingHandler(100, "Z35527T3235542")
    app.run(host="127.0.0.1", port=5050, debug=debug)

if __name__ == "__main__":
    thread = Thread(target=run(app, debug=True))
    thread.start()
