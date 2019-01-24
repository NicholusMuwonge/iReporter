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
        get method to return a list of record  records
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
        Method to update the destination of a record  record
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
        return Error_message.no_items('record')