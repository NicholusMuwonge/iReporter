"""
Directors on what to do with data from the models
"""
from flask import request, jsonify
from flask.views import MethodView
from api.models.record_model import Record
from api.Error.responses import Error_message
from api.validation.verifications import Verification
from api.models.database import DatabaseConnection
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
    )

class Record_logic(MethodView):
    """
    Class with  methods to handle get, post and put methods
    """
    record_title = None
    record_geolocation = None
    record_type = None
    status='Pending'
    val = Verification()
    record_data = Error_message()
    data = DatabaseConnection()
    record=Record()

    @jwt_required
    def post(self):
        """
        post method to handle posting an record
        """
        user = get_jwt_identity()
        admin = user[3]
        user_id = user[0]

        if user_id and admin == "FALSE":

            post_data = request.get_json()
            keys = (
                "record_title", "record_geolocation", "record_type"
                )

            if not set(keys).issubset(set(post_data)):
                return Error_message.missing_fields(keys)

            try:
                self.record_title = post_data['record_title'].strip()
                self.record_geolocation = post_data['record_geolocation'].strip()
                self.record_type = post_data['record_type'].strip()

            except AttributeError:
                return Error_message.invalid_data_format()

            if not self.record_title or not self.record_geolocation or not self.record_type:
                return Error_message.empty_data_fields()
            # elif not isinstance(self.record_geolocation,float):
            #     return Error_message.invalid_input()
            new_record = self.record.post_record(self.record_type,self.record_geolocation,self.record_title,str(user_id))
            response_object = {
                'message': 'Successfully posted a new record',
                'data': new_record
            }
            return jsonify(response_object), 201
        return Error_message.permission_denied()

    @jwt_required
    def get(self, record_no=None):
        """
        get method to return a list of records
        """
        user = get_jwt_identity()
        user_id = user[0]
        admin = user[3]

        if admin == "FALSE" or  admin == "TRUE" and user_id:  # changed this authorization, please check it out.

            if record_no:
                return self.data.get_one_record_using_record_no(record_no)

            all_records = self.data.get_all_records()

            if all_records:
                records = []
                for record in all_records:

                    user = self.data.find_user_by_id(record['user_id'])
                    res_data = {
                        "user_name": user[1],
                        "record_title": record['record_title'],
                        "record_geolocation": record['record_geolocation'],
                        "record_type": record['record_type'],
                        "status": record['status'],
                        "record_no": record['record_no'],
                        "record_placement_date": record['record_placement_date']
                        
                    }
                    records.append(res_data)

                response_object = {
                    "msg": "Successfully got all record  records",
                    "data": records
                    }
                return jsonify(response_object), 200
            else:
                return Error_message.no_items('record')

        return Error_message.denied_permission()


    @jwt_required
    def put(self, record_no=None,record_geolocation=None):
        """
        Method to update the record  status
        """
        user = get_jwt_identity()
        admin = user[3]
        user_id = user[0]

        if admin == "TRUE" and user_id:

            post_data = request.get_json()

            # key = "status"
            statuses = ['Under Investigation','Denied','Resolved']

            # if key in post_data:
            try:
                self.status = post_data['status'].strip()
            except AttributeError:
                return Error_message.invalid_data_format()
            if not self.val.validate_string_input(self.status):
                return Error_message.invalid_input()
            if not self.status:
                return Error_message.empty_data_fields()
            for status in statuses:
                if self.status not in statuses:
                    return Error_message.record_status_not_found(self.status)
            updated_status = self.data.change_status(self.status, record_no)
            if isinstance(updated_status, object):
                response_object = {
                    'message': 'Status has been updated successfully'
                }
                return jsonify(response_object), 202
        return Error_message.denied_permission()


    @jwt_required
    def update_geolocation(self, record_geolocation, record_no):
        """
        Method to update the destination of a record  record
        """
        user = get_jwt_identity()
        admin = user[4]
        user_id = user[0]

        if admin != "TRUE" and user_id:
            if self.data.update_record_geolocation(record_geolocation,record_no):
                response_object = {
                    'message': 'Present location has been updated successfully'

                }
                return jsonify(response_object), 202

        return Error_message.no_items('record')

    @jwt_required
    def delete(self,record_no):
        """
        Method to update the destination of a record  record
        """
        user = get_jwt_identity()
        admin = user[4]
        user_id = user[0]

        if admin != "TRUE" and user_id:
            record_to_be_deleted = self.data.delete_record(record_no)
            if record_to_be_deleted:
                response_object = {
                    'message': 'Record has been deleted successfully'

                }
                return jsonify(response_object), 202
            else:
                return jsonify({
                    'message': 'record you are trying to delete is non existent',
                    "status":"fail",
                    "data":False
                }),404
                # return Error_message.no_items('record')
        return Error_message.permission_denied()


class Intervention(MethodView):
    record_title = None
    record_geolocation = None
    record_type = None
    status='Under Investigation'
    val = Verification()
    record_data = Error_message()
    data = DatabaseConnection()
    record=Record()

    
    @jwt_required
    def get(self, record_no):
        """
        get method to return a list of records
        """
        user = get_jwt_identity()
        user_id = user[0]
        admin = user[3]

        if admin == "FALSE" or  admin == "TRUE" and user_id:  # changed this authorization, please check it out.
            if record_no:
                all_redflags=self.data.get_one_Interventionn(record_no)
                return all_redflags, 200
            else:
                return Error_message.no_items('intervention')
        return Error_message.denied_permission()


    

    @jwt_required
    def delete(self,record_no):
        """
        method to  delete record
        """
        user = get_jwt_identity()
        admin = user[3]
        user_id = user[0]

        if admin != "TRUE" and user_id:
            if self.data.delete_intervention(record_no):
                response_object = {
                    'message': 'Record has been deleted successfully'
                }
                return jsonify(response_object), 202
            return ('record not found'),404
        return Error_message.no_items('record')

    @jwt_required
    def put(self,record_no,record_geolocation):
        """
        Method to update the record_geolocation
        """
        user = get_jwt_identity()
        admin = user[3]
        user_id = user[0]

        if admin != "TRUE" and user_id:
            post_data = request.get_json()
            # if key in post_data:
            try:
                self.record_geolocation = post_data['record_geolocation'].strip()
            except AttributeError:
                return Error_message.invalid_data_format()
            if not self.val.validate_string_input(self.record_geolocation):
                return Error_message.invalid_input()
            if not self.status:
                return Error_message.empty_data_fields()
            one=self.data.get_one_Interventionn(record_no)
            location = self.data.update_redflag_geolocation(record_no,record_geolocation)
            if one:
                self.data.update_redflag_geolocation(record_no,record_geolocation)
                response_object = {
                    'message': 'Record has been delete successfully'
                }
                return jsonify(response_object), 202
            return ('record not found'),404
        return Error_message.no_items('record')


class Extension(MethodView):
    record_title = None
    record_geolocation = None
    record_type = None
    status='Under Investigation'
    val = Verification()
    record_data = Error_message()
    data = DatabaseConnection()
    record=Record()

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = user_id[0]
        admin= user_id[3]

        if admin == 'FALSE' or admin == 'TRUE' and user:

            all_records= self.data.get_all_interventions()
            return (all_records),200
        return Error_message.denied_permission()
