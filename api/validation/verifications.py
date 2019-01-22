import re
from api.models.database import DatabaseConnection


class Verification:
    """
    Class has methods to handle validation of data
    """
    data = DatabaseConnection()

    @staticmethod
    def validate_email(email):
        """
        ensure email address is of acceptable standards
        """
        pattern = re.compile(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$")
        if not pattern.match(email):
            return False
        return True

    @staticmethod
    def validate_username(user_name):
        """
        ensure user_name is of acceptable standards
        """
        username_regex = re.compile(r"^[A-Za-z\s]{4,30}$")
        if not username_regex.match(user_name):
            return False
        return True

    def check_if_user_name_exists(self, user_name):
        """
        Check if the username already exists
        """
        if self.data.find_user_by_username(user_name):
            return False
        return True


    @staticmethod
    def validate_password(password, length, length1):
        """
        password strength validator
        """
        if length > len(password) > length1:
            return False
        return password.isalnum()  # to return password with both alphabetic,numerical characters,and some special characters. 

    
    def check_if_email_exists(self, email):
        """
        Check if the email already exists
        """
        if self.data.find_user_by_email(email):
            return False
        return True