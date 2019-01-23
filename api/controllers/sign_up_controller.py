"""
module to handle signup of the user
"""
from flask import request, jsonify
from flask.views import MethodView
from api.flags.error_responses import Error_message
from api.models.sign_up_model import User
from api.validation.verifications import Verification
from api.authentication.password_check import AuthenticatePassword
from flask_jwt_extended import jwt_required , jwt_manager
from api.models.database import DatabaseConnection

db=DatabaseConnection()



class Signup(MethodView):
    """
    Registering a new user
    """
    user_structure= User()
    val = Verification()

    def post(self):
        post_data = request.get_json()
        fields = ("user_name", "email", "user_password")
        if not set(fields).issubset(set(post_data)):
            return Error_message.missing_fields(fields)
        try:
            user_name = post_data.get('user_name').strip()
            email = post_data.get('email').strip()
            user_password = post_data.get('user_password').strip()

        except AttributeError:
            return Error_message.invalid_data_format()

        if not user_name or not email  or not user_password:
            return Error_message.empty_data_fields()
        elif not self.val.validate_password(user_password, 5, 13):
            return Error_message.invalid_password()
        elif not self.val.validate_email(email):
            return Error_message.invalid_email()
        elif not self.val.validate_username(user_name):
            return Error_message.invalid_name()
        elif not self.val.check_if_email_exists(email):
            return Error_message.email_already_exists()
        elif not self.val.check_if_user_name_exists(user_name):
            return Error_message.username_already_exists()

        self.user_structure.post_user(
            user_name, email,
            AuthenticatePassword.hash_password(user_password))
        response_object = {
            'status': 'success',
            'message': 'Your account has been created successfully'
            }
        return jsonify(response_object), 201

    @jwt_required
    def get(self):
        all_red_flags= db.get_all_redflags()
        if all_red_flags:
            return jsonify({'message':"successfully retrieved all redflags" ,
            "data" : all_red_flags,
            "status" : "success" }),200
        else:
            return jsonify({
                "message":"users not found",
                "data" : False,
                "status" : "Fail"
            }),404