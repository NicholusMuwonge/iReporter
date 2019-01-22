import datetime
from flask import request, jsonify
from flask.views import MethodView
from api.flags.error_responses import Error_message
from api.authentication.password_check import AuthenticatePassword
from api.models.database import DatabaseConnection
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
    )
from api.validation.verifications import Verification


class Login(MethodView):
    """
    Login Logic
    """
    data = DatabaseConnection()
    auth = AuthenticatePassword()
    val = Verification()

    def post(self):
        post_data = request.get_json()
        keys = ('user_name', 'user_password')
        if not set(keys).issubset(set(post_data)):
            return Error_message.missing_fields(keys)
        try:
            user_name = post_data.get("user_name").strip()
            user_password = post_data.get("user_password").strip()
        except AttributeError:
            return Error_message.invalid_data_format()
        if not user_name or not user_password:
            return Error_message.empty_data_fields()
        user = self.data.find_user_by_username(user_name)

        if user and AuthenticatePassword.verify_password(
            user_password, user[4]
            ):
            response_object = {
                'status': 'success',
                'message': 'You are logged in',
                'access_token': create_access_token(
                    identity=user,expires_delta=datetime.timedelta(minutes=60)
                    ),
                'logged_in_as': str(user[1])
                }

            return jsonify(response_object), 200

        else:
            response_object = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(response_object), 404