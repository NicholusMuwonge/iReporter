import re
from werkzeug.security import generate_password_hash, check_password_hash
""" creating users """


class User_class:

    def __init__(self):
        #,user_name,user_password,sign_up_date,email,phone_number,registered_date,user_type,user_id,user_list:
        self.user_name = None
        self.user_password = None
        self.email = None
        self.user_id =  0
        self.registered_date = None
        self.phone_number = None
        self.user_type = True
        self.increment = self.user_id+1 
        self.user_list = []
        
    def user_mail_setting(self,email)  :
      email_pattern = re.compile(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$")
      if email_pattern:
          return True
      return False
    
    @staticmethod
    def verify_password(password_text, hashed):
        return check_password_hash(hashed, password_text)
    
    
    
    
    
    
    
    
    
    
  
