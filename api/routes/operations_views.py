"""
Module to handle url requests
"""
from api.controllers.sign_up_controller import Signup
from api.controllers.login_controller import Login 

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