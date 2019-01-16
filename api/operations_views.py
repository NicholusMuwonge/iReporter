from flask import Flask, json, jsonify, request, make_response #MethodView,view_functions
from .controller import Record
from flask import Flask, json, jsonify, request, make_response #MethodView,view_functions
from .controller import User, User_class
import jwt
from werkzeug.security import check_password_hash
import datetime
import re

record_object = Record() #create a record object.
""" we name the app,(create an instance of flask)"""
user_object = User()
i = User_class()
""" route for the home"""


class route_response:
    """ route for getting a record"""
    def post_record(self):
        if request.method == 'POST':
            result = request.data
            data = json.loads(result)
            record = {
                'record_title':data['record_title'],\
                'record_geolocation':data['record_geolocation']}
            if (record['record_title'] or record['record_geolocation']) == '':
                return jsonify({"message":'fill in these fields'}),400 #bad request
            else:
                new_record = record_object.add_record(record)
                return jsonify({'message':'record created successfully','record':new_record}),201

    def return_all_records(self):
        list_of_orders = record_object.get_all_records()
        if list_of_orders:
            response_object = {'message':'all retrieved','records':list_of_orders}
            return jsonify(response_object),200
        else:
            response_object = {'message':'no records to display'}
            return jsonify(response_object),204

    def update_record(self,record_no):
        if isinstance (record_no,int):
            record_geolocation = request.json["record_geolocation"].strip()
            update_record = record_object.update_record(record_no,record_geolocation)
            return jsonify({'message':'Record updated',"records":update_record}),201
        else:
            return ({'message':'record doesnt exist'}),400

    def return_one_only(self,record_no):
        if 'record_no' is None:
            return jsonify({'message':'item not found'}),404
        if record_object.records == []:
            return jsonify({'message':'this list is empty'}),204
        if isinstance(record_no,str):
            return jsonify({'message':'not applicable'}),404
        list_of_orders = record_object.return_one(record_no)
        if list_of_orders:
            return jsonify({'message':'record retrieved','record':list_of_orders}),200

    def delete_record(self,record_no):
        if 'record_no' == '' or 'record_no' is None:
            return 'item not found',404
        if record_object.records == []:
            return 'this list is empty',404
        if isinstance(record_no,str):
            return 'not applicable',404
        if isinstance(record_no,int):
            list_of_orders = record_object.delete_record(record_no)
            if list_of_orders:
                return jsonify({'message':'this record has been deleted successfully'}),200
# -------------------------------------USERS---------------------------------------------------------------

class route_response_user:

    
    def create_user(self):
        if request.method == 'POST':
            existing_user = user_object.user_list
            result = request.data
            data = json.loads(result)
            if not data:
                return jsonify({'error':'unsupported Request'}), 400
            elif 'user_name' not in data:
                return jsonify({'error':'username is requred'}), 400
            elif 'user_password' not in data:
                return jsonify({'error':'password is required'}), 400
            elif 'email' not in data:
                return jsonify({'error':'email is missing'}),400
            user_name = data["user_name"].strip()
            user_password = data['user_password'].strip()
            email = data['email'].strip()
            user_id = int(len(i.user_list))+1
            registered_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_type = 'user'
            for user in existing_user:
                if ((user['user_name'] ),(user['email'])) == (user_name,email):
                    return jsonify ({'message':'the user exists'}),400
            if (len(data['user_name']) or len(data['user_password'])) is 0:
                return jsonify({"message": "fill in missing fields"}), 400
            elif len(data['user_password'])<5 or len(data['user_password'])>13 :
                password_check = {'message':'improve password strength'}
                return jsonify(password_check),400
            elif (data['email']) is i.user_mail_setting:
                return jsonify({'message':'invalid_email_format'}),400
            else:
                user_object.register_user(user_name,user_password,email,user_type,registered_date,user_id)
                return jsonify({'Message': 'New user registered successfully'}), 201

    def fetch_all_users(self):
        new_users_lists = user_object.fetch_all_users()
        if new_users_lists:
            response_object = {'message':'all retrieved','user':new_users_lists}
            return jsonify(response_object),200
        else:
            response_object = ('no users to display')
            return jsonify(response_object),204

    def login(self):
        cheker = user_object.login_user()
        return (cheker)