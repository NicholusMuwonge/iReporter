"""
Module to handle url requests
"""
from api.controllers.signup_controllers import Signup
from api.controllers.login_controllers import Login
from api.controllers.record_controller import Record_logic,Intervention,Extension
from api.controllers.red_flag import Redflags
from api.controllers.redflag_extension import Redflag

class Routes:
    """
        Class to generate urls
    """

    @staticmethod
    def generate(app):
        """
        Generate urls
        """
        app.add_url_rule('/api/v2/auth/signup/', view_func=Signup.as_view('register_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/login/', view_func=Login.as_view('login_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/', view_func=Record_logic.as_view('post_record'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/', view_func=Record_logic.as_view('get_all_records'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/record/<int:record_no>', view_func=Record_logic.as_view('get_one_record'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/users/<int:user_id>/records/',
                         view_func=Login.as_view('get_specific_user_records'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/records/<int:record_no>/delete/',
                         view_func=Record_logic.as_view('delete_record'),
                         methods=['DELETE'], strict_slashes=False)
        app.add_url_rule('/api/v2/record_no/<int:record_no>/',
                         view_func=Login.as_view('update_record_geolocation'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/record/<int:record_no>/status/',
                         view_func=Record_logic.as_view('update_record_status'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/redflag/<int:record_no>/',
                         view_func=Redflags.as_view('get one red flag'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/redflags/',
                         view_func=Redflag.as_view('get all red flags'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/redflag/<int:record_no>/',
                         view_func=Redflags.as_view('delete red flag'),
                         methods=['DELETE'], strict_slashes=False)
        app.add_url_rule('/api/v2/redflag/update/<int:record_no>/',
                         view_func=Redflags.as_view('update red flag'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/intervention/<int:record_no>/',
                         view_func=Intervention.as_view('get one intervention'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/interventions/',
                         view_func=Extension.as_view('get all interventions'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/interventions/<int:record_no>/',
                         view_func=Intervention.as_view('delete interventions'),
                         methods=['DELETE'], strict_slashes=False)
        app.add_url_rule('/api/v2/intervention/update/<int:record_no>/',
                         view_func=Intervention.as_view('update interventions'),
                         methods=['PUT'], strict_slashes=False)