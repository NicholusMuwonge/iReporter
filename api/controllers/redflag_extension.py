from flask import request, jsonify
from flask.views import MethodView
from api.models.record_model import Record
from api.Error.responses import Error_message
from api.validation.verifications import Verification
from api.models.database import DatabaseConnection
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
    )
db = DatabaseConnection()


class Redflag(MethodView):


    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = user_id[0]
        admin= user_id[3]

        if admin == 'FALSE' or admin == 'TRUE' and user:

            all_records= db.get_all_redflags()
            return (all_records),200
        return Error_message.denied_permission()

        
        
