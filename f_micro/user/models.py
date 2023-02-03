# import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

app = Flask(__name__)

config = dotenv_values('.env')
# Fetch DB URL from Docker_compose yaml file
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE_URL")
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))


app.app_context().push()
db.create_all()
