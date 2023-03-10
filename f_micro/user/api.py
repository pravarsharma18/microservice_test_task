from flask_restful import Resource
from flask import request, jsonify
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .utils import save_user_data_in_dj_micro
from user.models import User
from dotenv import dotenv_values

config = dotenv_values('.env')
print(config.get("DATABASE_URL"))

engine = create_engine(config.get("DATABASE_URL"), pool_size=20, max_overflow=20, pool_recycle=3600)
Session = sessionmaker(bind=engine)


class UserView(Resource):
    def __init__(self):
        self.session = Session()

    def get(self):
        return {"detail": "hello"}

    def post(self):
        data = json.loads(request.data)
        try:
            if self.session.query(User.query.filter(User.username == data['username']).exists()).scalar():
                return {"username": "Usename already exists."}
        except Exception as error:
            return error

        try:
            user_create = User(username=data['username'], first_name=data['first_name'], last_name=data['last_name'])
            self.session.add(user_create)
            response = save_user_data_in_dj_micro(data)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return error

        result = {
            "django": {
                "username": response.get('username'),   # from django server
                "first_name": response.get('first_name'),
                "last_name": response.get('last_name'),
            },
            "flask": {
                "username": data.get('username'),   # from django server
                "first_name": data.get('first_name'),
                "last_name": data.get('last_name'),
            }
        }

        response = jsonify(result)
        response.status_code = 201
        return response
