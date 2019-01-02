from flask import Flask,json,jsonify
import unittest
from app.controller import Record,User
from app.routes import app,create_user
from app.model import User_class

class test_feature(unittest.TestCase):
    @classmethod
    def setUp(self):
        app.testing=True
        self.record=Record()
        self.sample_records={'record_no':1,
        'record_title':'One',
        'record_type':'redflag',
        'record_geolocation':'000003445N 22222228S'
        }
        self.user={'user_name':"Nicks",'user_password':"nicholas","email":"nicklaus@home.com","user_id":1}
        self.object=User_class()
        self.controller=User()
        self.client=app.test_client()
    
    @classmethod
    def tearDown(self):
        print ('Teardown')

    def test_record_creation(self):
        self.assertIsInstance(self.record, Record)

    # def test_record_is_empty(self):
    #     self.assertEqual(len(self.sample_records),0)
    #     self.record.add_record(self.sample_records)
    #     self.assertEqual(len(self.sample_records),1)


    def test_post_record(self):
        i=self.client.post('/api/v1/records',data=json.dumps(self.sample_records), content_type=('application/json'))
        self.assertEqual(i.status_code,201)
        # self.assertEqual(i.content_type,'json')#check if it was successfully created
       # i=self.client.get('/ft/v1/orders')
        #self.assertEqual(i.status_code,200)#to check if it was successfuly added to the list


    def test_get_all_records(self): 
        for record in self.record.records:

            if record['record_no'] is None:
                    item=self.client.get('/api/v1/<int:record_no>')
                    self.assertEqual(item.status_code,204, msg='no item has been returned')
            else:
                item=self.client.get('/api/v1/records')
                self.assertEqual(item.status_code,200)

    def test_get_one_record(self):
        for record in self.record.records:

            if record['record_no'] is None:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,204, msg='no item has been returned')
            else:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,200,msg='It hasnt been displayed')



    def test_modify_record(self):
        for record in self.record.records:
            if record['record_no'] is not None:
                item=self.client.post('/api/v1/<int:record_no>',data=json.dumps(self.sample_records), content_type=('application/json'))
                self.assertEqual(item.status_code,201)
            else:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,404)
    
    def test_delete_post(self):
        for record in self.record.records:
            if record['record_no'] is None:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,404)
            else:
                item=self.client.delete('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,200)
"""
    def test_get_all_users(self):
        if self.object.user_list==[]:

            item=self.client.get('/api/v1/users')
            self.assertEqual(item.status_code,404, msg='no item has been returned')

        
        else:
            item=self.client.get('/api/v1/users')
            self.assertEqual(item.status_code,200,msg='The list has items')

    def test_user_signup(self,user_name,user_password,email,user_type,registered_date,user_id):
        for user in self.object.user_list:
            if user["user_name"] or user["user_password"]  is None:
                item=create_user()
                self.assertWarns(item['message'],"fill in missing fields")
"""


        

    
     





    

if __name__ == "__main__":
    unittest.main()


