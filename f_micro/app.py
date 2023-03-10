from flask import Flask
from user.blueprint import p_blueprint
from user.models import *
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)

app.register_blueprint(p_blueprint)

if __name__ == "__main__":
    app.run()
