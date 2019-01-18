import re
from werkzeug.security import generate_password_hash, check_password_hash

# """ creating users """


class UserClass:

    def __init__(self):
        self.user_name = None
        self.user_password = None
        self.email = None
        self.user_id = 0
        self.registered_date = None
        self.user_type = None

    def user_mail_setting(self, email):
      email_pattern = re.compile(
            r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$"
          )
      if email_pattern:
          return True
      return False