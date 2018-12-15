from flask import Flask,json,jsonify,make_response,request
from flask import Flask,json,jsonify,make_response,request
from .model import User_class
from werkzeug.security import generate_password_hash, check_password_hash,safe_str_cmp
import uuid
import datetime




class_object=User_class()

class Record:
     #initialize record lists
    def __init__(self):
        self.records=[]
    

    def   add_record(self,record):#record is the new redflag being created.
        """creating fields that will be returned automatically"""
        record['record_no']= int(len(self.records) + 1 )
        record['record_type']= 'Redflag_record'
        self.records.append(record)
        return  record


    def    get_all_orders(self):
        return self.records


    def update_record(self,record_no,record_geolocation):

        update_record=[record for record in self.records if record['record_no']== record_no]
        if update_record:
            # update_record[0]['record_title']=record_title 
            update_record[0]['record_geolocation']=record_geolocation
            return update_record
        else:
            return ('this record doesnt exist')


    def return_one(self,record_no):
        if isinstance (record_no,int):

        
            for record in self.records:

                if record["record_no"] == record_no: 
                    return record

                #return make_response(jsonify({'records':records}))
        else:
            return('Input proper record_no'),204



    def delete_record(self,record_no):
        record_deleted=[record for record in self.records if record['record_no']==record_no]
        if record_deleted:
            

            deleted_records=self.records.remove(record_deleted[0])
            return (jsonify({'records':deleted_records}))


class User:
    def __init__(self):

        self.user_list=[]
        

    def register_user(self,user_name,user_password,email,user_type,registered_date,user_id):
        

        new_user=[class_object.user_name,class_object.user_password,class_object.email,class_object.user_id,class_object.user_type]

        for user in new_user:
            user={}
            # if user['user_name']==user_name:
            #     return 'user already exists'
            
            user['user_name']=user_name
            user['user_password']=(generate_password_hash(class_object.user_password,method='sha256'))
            user['email']=email
            user['user_id']=class_object.increment
            user['registered_date']=registered_date
            user['user_type']=user_type
            self.user_list.append(user)
            return jsonify(new_user)

    def fetch_all_users(self):
        users = self.user_list
        if users != []:
            return users ,200
        else:
            return jsonify({'message':'no user found'}),404


    def login_user(self):
        # auth=request.authorisation
        data=request.get_json()

        try:
            self.user_name =data.get('user_name').strip()
            self.user_password =data.get('user_password').strip()
        except:
            None

        current_user =User.fetch_all_users(self)
        for user in current_user:
            if user['user_name'] == self.user_name and user['user_password']==self.user_password:
                return jsonify(user),200
            elif user['user_password'] != self.user_password :
                return jsonify({"Message": "wrong password "}),400
            else:
                return jsonify({"Message": "No username  Found"}),404
