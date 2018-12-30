from sanic import Sanic
from sanic.response import json
from config import DB_HOST, DB_NAME, DB_USER


app = Sanic()
app.config.DB_NAME = DB_NAME
app.config.DB_USER = DB_USER
app.config.DB_HOST = DB_HOST


@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
