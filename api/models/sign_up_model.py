
from api.models.database import DatabaseConnection


class User:
    db = DatabaseConnection()

    def __init__(self, user_name=None, email=None, user_password=None):

        """
        User  class initialisation and data structure
        """
        self.user_name = user_name
        self.email = email
        self.user_password = user_password
        self.user_id = None

    def post_user(
        self, user_name=None, email=None, user_password=None
        ):
        """
        Register new user
        """
        user = User(user_name, email, user_password)
        self.db.create_user(user_name, email,user_password)
        return user
