from flask import request, jsonify
from flask.views import MethodView
from api.models.record_model import Record
from api.Error.responses import Error_message
from api.validation.verifications import Verification
from api.models.database import DatabaseConnection
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
    )

class Redflags(MethodView):

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
                all_redflags=self.data.get_one_redflags(record_no)
                return all_redflags, 200
            else:
                return Error_message.no_items('redflag')
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
            if self.data.delete_redflag(record_no):
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
            one=self.data.get_one_redflags(record_no)
            location = self.data.update_redflag_geolocation(record_no,record_geolocation)
            if one:
                self.data.update_redflag_geolocation(record_no,record_geolocation)
                response_object = {
                    'message': 'Record has been delete successfully'
                }
                return jsonify(response_object), 202
            return ('record not found'),404
        return Error_message.no_items('record')