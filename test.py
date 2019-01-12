from flask import Flask,json,jsonify
import unittest
from app.controller import Record,User
from app.routes import app,create_user,fetch_all_users
from app.model import User_class
from app import app

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
        self.sample_list = [{'record_no':1,
        'record_title':'One',
        'record_type':'redflag',
        'record_geolocation':'000003445N 22222228S'
        },{'record_no':1,
        'record_title':'two',
        'record_type':'redflag',
        'record_geolocation':'00785949N 6666666S'
        }]
        self.empty_fields = {'record_no':1,
        'record_title':'',
        'record_type':'redflag',
        'record_geolocation':''
        }
        self.empty_list=[]
        self.user={'user_name':'user_name','user_password':'user_password',"email":'email',"user_id":'user_id'}
        self.object=User_class()
        self.controller=User()
        self.app=app
        self.client=self.app.test_client()
    
    @classmethod
    def tearDown(self):
        print ('Teardown')

    def post_record(self,record_no,record_title,record_geolocation,record_type):
        data_to_be_posted=self.client.post('/api/v1/records',data=json.dumps(self.sample_records), content_type=('application/json'))
        return data_to_be_posted

    def test_record_creation(self):
        self.assertIsInstance(self.record, Record)

    

    def test_home(self):
        index=self.client.get('/',content_type='application/json')
        return self.assertEqual(index.status_code,200)


    def test_post_record(self):
        i=self.client.post('/api/v1/records',data=json.dumps(self.sample_records), content_type=('application/json'))
        post_response = json.loads(i.data.decode())
        self.assertEqual(i.status_code,201)
        self.assertTrue(i.content_type, 'application/json')
        self.assertTrue(post_response['message'], 'record created successfully')
        self.assertTrue(post_response['record'])
        
       # i=self.client.get('/ft/v1/orders')
        #self.assertEqual(i.status_code,200)#to check if it was successfuly added to the list

    def test_invalid_post(self):
        i=self.client.post('/api/v1/records',data=json.dumps(self.empty_fields), content_type=('application/json'))
        post_response = json.loads(i.data.decode())
        self.assertEqual(i.status_code,400)
        self.assertTrue(i.content_type, 'application/json')
        self.assertTrue(post_response['message'], 'fill in these fields')
      


    def test_get_all_records(self): 
        # for record in self.record.records:
        self.list=self.record.get_all_records()

        if not self.list:
                item=self.client.get('/api/v1/records')
                # response_data= json.loads(item.data.decode())
                self.assertEqual(item.status_code,204, msg='no item has been returned')
                self.assertTrue(item.content_type, 'application/json')
                # self.assertTrue(response_data['message'],'This list is empty')
                

        else:
            item=self.client.get('/api/v1/records')
            # response_data= json.loads(item.data.decode())
            self.assertTrue(item.content_type, 'application/json')
            self.assertEqual(item.status_code,200)
            
            # self.assertTrue(response_data['message'],'What you requested for')
            # self.assertTrue(response_data['records'])
            # self.assertIsInstance(response_data['record_no'],int)

    def test_get_one_record(self):
        for record in self.record.records:

            if record['record_no'] is None:
                item=self.client.get('/api/v1/<int:record_no>/records')
                # post_response = json.loads(item.data.decode())
                self.assertEqual(item.status_code,404, msg='no item has been returned')
                # self.assertTrue(post_response['message'],'item not found')
            else:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,200,msg='It hasnt been displayed')

    # def test_get_one_from_list_that_doesnt_exist(self):
    #     self.item=({'record_no':2,'record_title':'rails','record_geolocation':'454663m','record_type':'intervention'})

    #     request_data = self.client.get('/api/v1/5/records',data=json.dumps(self.item), content_type=('application/json'))
    #     response_data = json.loads(request_data.data.decode())
    #     self.assertTrue(response_data['message'], 'item not found')
    #     self.assertEqual(request_data.status_code, 404)


    def test_modify_record(self):
        for record in self.record.records:
            if record['record_no'] is not None:
                item=self.client.post('/api/v1/<int:record_no>',data=json.dumps(self.sample_records), content_type=('application/json'))
                self.assertEqual(item.status_code,201)
            else:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,404)

    def test_update_record(self):
        self.post_record(3,'truce','2733883N 899000N','Redflag')
        request_data= self.client.put('/api/v1/records/3',
            data=json.dumps(dict(
                record_geolocation="0000000N 777777S"
            )),
            content_type='application/json'
        )

        response_data = json.loads(request_data.data.decode())
        self.assertTrue(response_data['message'], 'Record updated')
        self.assertTrue(request_data.content_type, 'application/json')
        self.assertEqual(request_data.status_code, 201)

    def test_update_non_existent_record(self):
        self.post_record(3,'truce','2733883N 899000N','Redflag')
        request_data= self.client.put('/api/v1/records/25',
            data=json.dumps(dict(
                record_geolocation="0000000N 777777S"
            )),
            content_type='application/json'
        )

        response_data = json.loads(request_data.data.decode())
        self.assertTrue(response_data['message'], 'record doesnt exist')
        self.assertTrue(request_data.content_type, 'application/json')
        # self.assertEqual(request_data.status_code, 400)

    

    
    def test_delete_post(self):
        for record in self.record.records:
            if record['record_no'] is None:
                item=self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,404)
            else:
                item=self.client.delete('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,200)




                """ users tests"""
    def post_user(self,user_name,user_password,email,user_id):
        data_to_be_posted=self.client.post('/api/v1/users',data=json.dumps(self.user), content_type=('application/json'))
        return data_to_be_posted

    def test_post_user(self):
        # post=self.post_user('ncncn','djjdjd','hdhhd@gmail.com',2)
        request_data=self.client.post('/api/v1/users/signup',data=json.dumps(self.user),content_type=('application/json'))
        response_data=json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,201)
        self.assertTrue(request_data.content_type, 'application/json')
        self.assertTrue(response_data['Message'],'New user registered successfully')

    def test_login_user(self):
        self.post_user('nicholas','nicksbro','nicks@gmail.com',1)
        request_data=self.client.post('/api/v1/users/login',data=json.dumps(dict(email='nicks@gmail.com',user_password='nicksbro')),content_type=('application/json'))
        response_data=json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,200)
        self.assertTrue(request_data.content_type, 'application/json')
        # self.assertTrue(response_data['message'],'you are successfully loged in')

    def test_get_all_users_in_empty_list(self):
        request_data=self.client.get('/api/v1/users',content_type='application/json')
        self.assertEqual(request_data.status_code,204)
        self.assertTrue(request_data.content_type, 'application/json')


    def test_get_all_users(self):
        self.list=self.controller.fetch_all_users()
        if self.list :
            self.post_user('nicholas','nicksbro','nicks@gmail.com',1)
            request_data=self.client.get('/api/v1/users',content_type='application/json')
            self.assertEqual(request_data.status_code,200)
            self.assertTrue(request_data.content_type, 'application/json')

        # else:
        #     request_data=self.client.get('/api/v1/users',content_type='application/json')
        #     self.assertEqual(request_data.status_code,204)
        #     self.assertTrue(request_data.content_type, 'application/json')


    # def test_missing_fields_login(self):
    #     # self.post_user('nicholas','nicksbro','nicks@gmail.com',1)
    #     request_data=self.client.post('/api/v1/users/login',data=json.dumps(dict(email='kkkkk',user_password='')),content_type=('application/json'))
    #     response_data=json.loads(request_data.data.decode())
    #     self.assertEqual(request_data.status_code,404)
    #     self.assertTrue(request_data.content_type, 'application/json')

    # def test_post_user_fields_missing(self):
    #     request_data=self.post_user('','','hdhhd@gmail.com',2)
    #     # request_data=self.client.post('/api/v1/users/signup',data=json.dumps(self.user),content_type=('application/json'))
    #     # response_data=json.loads(request_data.data.decode())
    #     self.assertEqual(request_data.status_code,400)
    #     self.assertTrue(request_data.content_type, 'application/json')
        # self.assertTrue(response_data['Message'],'New user registered successfully')


        
    


    
     





    

if __name__ == "__main__":
    unittest.main()


