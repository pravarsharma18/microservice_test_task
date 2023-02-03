from .api import UserView
from flask_restful import Api
from flask import Blueprint
from flask_cors import CORS

p_blueprint = Blueprint("p_blueprint", __name__)

CORS(p_blueprint, support_credentials=True, resources={
    r"/*": {
            "origins": "*",
            "allow_headers": "*"
        }
    }
)
p_api = Api(p_blueprint)
p_api.add_resource(UserView, "/users")
