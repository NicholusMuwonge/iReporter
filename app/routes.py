from flask import Flask,json,jsonify,request,make_response #MethodView,view_functions
from .controller import Record
from app import creat_app
from flask import Flask,json,jsonify,request,make_response #MethodView,view_functions
from .controller import User,User_class
import uuid
import jwt
from werkzeug.security import check_password_hash
import datetime
import re

record_object=Record() #create a record object.


""" we name the app,(create an instance of flask)"""

app=creat_app()
user_object=User()
i=User_class()

""" route for the home"""

@app.route('/')
def home():
    return 'You are welcome'

""" route for getting a record"""

@app.route('/api/v1/records', methods=['POST'])
def post_record():
    if request.method=='POST':
        
        result = request.data
        data=json.loads(result)
        record={
            'record_title':data['record_title'],
            'record_geolocation':data['record_geolocation']
            }


        if record['record_title']== '' or record['record_geolocation']=='':
            return jsonify({"message":'fill in these fields'}),400 #bad request
        
        else:

            new_record=record_object.add_record(record)
            return jsonify({'message':'record created successfully','record':new_record}),201


@app.route('/api/v1/records', methods=['GET'])
def return_all_records():
    list_of_orders=record_object.get_all_orders()
    if list_of_orders:
        response_object={'message':'all retrieved','records':list_of_orders}
        return jsonify(response_object),200
    else:
        response_object={'message':'no records to display'}
        return jsonify(response_object),204

    # if record_object.records==[]:
    #       return jsonify({'message':'This list is empty'}),204#no item found
    # else:
    #     list_of_orders=record_object.get_all_orders()
    #     return jsonify({'message':'What you requested for','records':list_of_orders}),200


@app.route('/api/v1/records/<int:record_no>', methods=['PUT'])
def update_record(record_no):
    if isinstance (record_no,int):

        #record_title=request.json["record_title"]
        record_geolocation=request.json["record_geolocation"]
        update_record=record_object.update_record(record_no,record_geolocation)
        return jsonify({'message':'Record updated',"records":update_record}),201

    else:
        return ({'message':'record doesnt exist'}),400



@app.route('/api/v1/<int:record_no>/records', methods=['GET'])
def return_one_only(record_no):
    if 'record_no'=='' or 'record_no' is None:
        return jsonify({'message':'item not found'}),404
    if record_object.records==[]:
        return jsonify({'message':'this list is empty'}),204
    if isinstance(record_no,str):
        return jsonify({'message':'not applicable'}),404
    list_of_orders=record_object.return_one(record_no)
    if list_of_orders:
        return jsonify({'message':'record retrieved','record':list_of_orders}),200

@app.route('/api/v1/<int:record_no>/records', methods=['DELETE'])
def delete_record(record_no):
    if 'record_no'=='' or 'record_no' is None:
        return 'item not found',404
    if record_object.records==[]:
        return 'this list is empty',404
    if isinstance(record_no,str):
        return 'not applicable',404

    if isinstance(record_no,int):

        list_of_orders=record_object.delete_record(record_no)
        if list_of_orders:
            return jsonify({'message':'this record has been deleted successfully'}),200





@app.route('/api/v1/users/signup', methods=['POST'])
def create_user():
    
    if request.method == 'POST':
        existing_user=user_object.user_list
        result = request.data
        data=json.loads(result)
        
        if not data:
            return jsonify({'error': 'unsupported Request'}), 400
        elif 'user_name' not in data:
            return jsonify({'error': 'username is requred'}), 400
        elif 'user_password' not in data:
            return jsonify({'error': 'password is required'}), 400
        elif 'email' not in data:
            return jsonify({'error':'email is missing'}),400
        

        user_name=data["user_name"]
        user_password=data['user_password']
        email=data['email']
        user_id=int(len(i.user_list))+1
        registered_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_type= 'user'
        
        # item=i.user_password_setting(user_password)
        for user in existing_user:
            if user['user_name']==user_name or user['email']==email:
                return jsonify ({'message':'the user exists'}),400
        if len(data['user_name']) is 0 or len(data['user_password']) is 0:
            return jsonify({"message": "fill in missing fields"}), 400

        elif len(data['user_password'])<5 or len(data['user_password'])>13 :
            # for user in i.user_list:
            #     if len(user['user_password']) is <5 or :
            password_check={'message':'improve password strength'}
            return jsonify(password_check)

        elif (data['email']) is i.user_mail_setting:
            return jsonify({'message':'invalid_email_format'})
        
        

            
        else:
            
            #phone_number=data['phone_number']
            
            
            
            user_object.register_user(user_name,user_password,email,user_type,registered_date,user_id)
            return jsonify({'Message': 'New user registered successfully'}), 201



@app.route("/api/v1/users",methods=["GET"])
def fetch_all_users():
    new_users_lists=user_object.fetch_all_users()
  
    return jsonify({ 'users':new_users_lists}),200


@app.route("/api/v1/users/login", methods=['POST'])
def login():
    cheker=user_object.login_user()
    return (cheker)









