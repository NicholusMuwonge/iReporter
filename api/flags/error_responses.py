"""
Module to handle all responses to errors
"""
from flask import jsonify, request


class Error_message:
    """
    Error handler to handle response errors.
    """

    @staticmethod
    def missing_fields(key):
        response_object = {
            "status": "fail",
            "error_message": "some fields are missing",
            "data": key}
        return jsonify(response_object), 400

    @staticmethod
    def invalid_data_format():
        response_object = {
            'status': 'fail',
            'error_message': 'Please use character strings',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
            'status': 'fail',
            'error_message': 'Some fields have no data',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key(keys):
        response_object = {
            'status': 'fail',
            'error_message': 'Missing key ' + keys,
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_password():
        response_object = {
            'status': 'fail',
            'error_message': 'Password is wrong. It should be \
            at-least 5 characters long, and alphanumeric.It shouldnt also be \
            longer than 13 characters',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_email():
        req = request.get_json()
        return jsonify({
            "status": "fail",
            "error_message": "User email {0} is wrong, \
            It should be in the format (xxxxx@xxxx.xxx).format(req['email']",
            "data": req

        }), 400

    @staticmethod
    def username_already_exists():
        response_object = {
            'status': 'fail',
            'error_message': 'Username already taken',
            'data': False
        }
        return jsonify(response_object), 409

    @staticmethod
    def email_already_exists():
        response_object = {
            'status': 'fail',
            'error_message': 'email already exists'

                }
        return jsonify(response_object), 409

    @staticmethod
    def invalid_name():
        return jsonify({
            "status": "fail",
            "error_message": "A name should consist of \
            only alphabetic characters",
            "data": request.get_json()
                   }), 400
