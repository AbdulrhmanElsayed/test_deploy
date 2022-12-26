from flask import Flask
from waitress import serve
app = Flask(__name__)


@app.route("/")
@app.route("/test")
def Hello_World():
    return {"message": "Hello World"}, 201


if __name__ == '__main__':
    app.config['Debug']=True
    #app.run(host='127.0.0.1', port=8080, debug=True)

    serve(app, host="0.0.0.0", port=8080)
