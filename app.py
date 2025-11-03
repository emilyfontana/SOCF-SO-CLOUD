from flask import Flask

APP = Flask(__name__)

@APP.get("/")
def index():
    return "<h1>Helllo Emily </h1>"


if __name__ == '__main__':
    APP.run(host="0.0.0.0", port = 80)


#como testar aplicação no codespace
# gunicorn app:APP no terminal