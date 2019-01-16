from flask import Flask,Blueprint
from .operations_views import route_response,route_response_user

route_class=route_response()
route_class_users=route_response_user()

mod=Blueprint('api',__name__,url_prefix='/api')

@mod.route('/')
def home():
    return 'You are welcome'

@mod.route('/v1/records/', methods=['POST'])
def post_a_record():
    return route_class.post_record()

@mod.route('/v1/records/',methods=['GET'])
def get_all_records():
    return route_class.return_all_records()

@mod.route('/v1/records/<int:record_no>/',methods=['PUT'])
def update_record(record_no):
    return route_class.update_record(record_no)

@mod.route('/v1/records/<int:record_no>/',methods=['GET'])
def get_one_record(record_no):
    return route_class.return_one_only(record_no)

@mod.route('/v1/records/<int:record_no>/', methods=['DELETE'])
def delete_record(record_no):
    return route_class.delete_record(record_no)

# ----------------------------------USER----------------------------------------------------------

@mod.route('/v1/users/signup/', methods=['POST'])
def post_user():
    return route_class_users.create_user()

@mod.route("/v1/users/login/",methods=["POST"])
def login_user():
    return route_class_users.login()

@mod.route("/v1/users/",methods=["GET"])
def get_all_users():
    return route_class_users.fetch_all_users()
