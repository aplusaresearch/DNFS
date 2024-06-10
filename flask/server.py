import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!\n"


@app.route('/world')
def hello_w():
    return "Hello world!\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
