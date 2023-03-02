from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required
)

from passlib.hash import pbkdf2_sha256

from flask_restful_api.models import UserModel
from flask_restful_api.blocklist import BLOCKLIST

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "password", type=str, required=True, help="This field cannot be blank."
)


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username already exists"}

        user = UserModel(
            username=data["username"], password=pbkdf2_sha256.hash(data["password"])
        )
        user.save_to_db()
        return {"message": "User create successfully."}, 201


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data["username"])

        if user and pbkdf2_sha256.verify(data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": "Invalid Credentials!"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200


class User(Resource):
    """
    This resource can be userful when testing our Flask app.
    """
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_username(user_id)
        if not user:
            return {"message": "User Not found"}, 404
        user.delete_from_db()
        return {"message":"user deleted."}, 200

    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not Found"}, 404
        user.delete_from_db()
        return {"message": "user deleted."}


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
