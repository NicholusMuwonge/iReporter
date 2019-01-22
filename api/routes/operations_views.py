"""
Module to handle url requests
"""
from api.controllers.sign_up_controller import Signup
from api.controllers.login_controller import Login
from api.controllers.intervention_record import RecordLogic

class Routes:
    """
        Class to generate urls
    """

    @staticmethod
    def generate(app):
        """
        This is where the urls are generated
        """
        app.add_url_rule('/api/v2/auth/signup/', view_func=Signup.as_view('register_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/login/', view_func=Login.as_view('login_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/', view_func=RecordLogic.as_view('post_record'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/', view_func=RecordLogic.as_view('get_all_records'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/record/<int:record_no>', 
                        view_func=RecordLogic.as_view('get_one_record'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/users/<int:user_id>/records/',
                         view_func=Login.as_view('get_specific_user_records'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/<int:record_no>/delete/',
                         view_func=RecordLogic.as_view('delete_record'),
                         methods=['DELETE'], strict_slashes=False)
        app.add_url_rule('/api/v2/record_no/<int:record_no>/',
                         view_func=Login.as_view('update_record_geolocation'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/record/<int:record_no>/status/',
                         view_func=RecordLogic.as_view('update_record_status'),
                         methods=['PUT'], strict_slashes=False)