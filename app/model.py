import re
""" creating users """
class User_class:


    def __init__(self):
        #,user_name,user_password,sign_up_date,email,phone_number,registered_date,user_type,user_id,user_list:
        self.user_name=None
        self.user_password=None
        self.email=None
        self.user_id= 0
        self.registered_date=None
        self.phone_number=None
        self.user_type=True
        self.increment=self.user_id+1 
        
        self.user_list=[]
        



    def user_id_setting(self,user_id):
        for user_id in self.user_list :
            if self.user_id != 1 and self.user_id >1:
                new_user_id=user_id+1
                return int(new_user_id)

    def user_type_setting(self,user_type):
        if user_type !=True:
            return 'Admin'
        else:
            return 'User'
        
    def user_password_setting(self,user_password):
        self.user_password=input('')
        for digit in self.user_password:
            if not isinstance (digit,str): #or if len(self.user_password) =< 5 :
                return "create another password that may contain both words and numbers",400

            if len(self.user_password) < 5 and len(self.user_password)>13:
                return "improve your password",400

          

    def user_mail_setting(self,email)  :
      email_pattern=re.compile(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$")
      if email_pattern:
          return True
      return False
    
    
    
    
    
    
    
    
    
    
    
  
