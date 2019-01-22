from api.models.sign_up_model import User
from werkzeug.security import generate_password_hash, check_password_hash


class AuthenticatePassword:

    myUser = User()

    @staticmethod
    def hash_password(user_password):
        """
        method to make the password unreadable (put in pattern)
        """
        try:
            return generate_password_hash(user_password, method="sha256")
        except ValueError:
            return False

    @staticmethod
    def verify_password(password_text, hashed):
        """
        verify stored password 
        """
        return check_password_hash(hashed, password_text)