from flask import Flask, Blueprint
from .operations_views import RouteResponse, RouteResponseUser

route_feedback = RouteResponse()
responses_for_route = RouteResponseUser()

mod = Blueprint('api', __name__, url_prefix = '/api')


@mod.route('/')
def home(): 
    return 'You are welcome'


@mod.route('/v1/records/', methods = ['POST'])
def post_a_record(): 
    return route_feedback.post_record()


@mod.route('/v1/records/', methods = ['GET'])
def get_all_records():
    return route_feedback.return_all_records()


@mod.route('/v1/records/<int:record_no>/', methods = ['PUT'])
def update_record(record_no):
    return route_feedback.update_record(record_no)


@mod.route('/v1/records/<int:record_no>/', methods = ['GET'])
def get_one_record(record_no):
    return route_feedback.return_one_only(record_no)


@mod.route('/v1/records/<int:record_no>/', methods = ['DELETE'])
def delete_record(record_no):
    return route_feedback.delete_record(record_no)

# ----------------------------------USER-------------------------


@mod.route('/v1/users/signup/', methods = ['POST'])
def post_user():
    return responses_for_route.create_user()


@mod.route("/v1/users/login/", methods = ["POST"])
def login_user():
    return responses_for_route.login()


@mod.route("/v1/users/", methods = ["GET"])
def get_all_users():
    return responses_for_route.fetch_all_users()
