from flask import Flask, json, jsonify
import unittest
from api.controller import Record, User
from api.routes import mod, post_user, get_all_users
from api.model import UserClass
from run import app
import re
EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')


class test_feature(unittest.TestCase):

    @classmethod
    def setUp(self):
        app.testing = True
        self.record = Record()
        self.user = {'user_name':'nicholus','user_password':'user_password',\
        "email":'email@g.com'}
        self.other_user = {'user_name':'nichol','user_password':'great',\
        "email":'nichol@g.com'}
        self.faulty_user = {'user_name':'nichol','user_password':'',\
        "email":'nichol@g.com'}
        self.object = UserClass()
        self.controller = User()
        self.app = app
        self.client = self.app.test_client()

    @classmethod
    def tearDown(self):
        print('Teardown')

    def post_record(self,record_no,record_title,record_geolocation,record_type):
        data_to_be_posted = self.client.post('/api/v1/records/',\
        data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')),\
        content_type = ('application/json'))
        return data_to_be_posted

    def test_record_creation(self):
        self.assertIsInstance(self.record, Record)

    def test_home(self):
        index = self.client.get('/api/',content_type = 'application/json')
        return self.assertEqual(index.status_code,200)

    def test_post_record(self):
        i = self.client.post('/api/v1/records/',data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')), content_type = ('application/json'))
        post_response = json.loads(i.data.decode())
        self.assertEqual(i.status_code,201)
        self.assertTrue(i.content_type, 'application/json')
        self.assertTrue(post_response['message'], 'record created successfully')
        self.assertTrue(post_response['record'])

    def test_invalid_post(self):
        i = self.client.post('/api/v1/records/',\
        data = json.dumps(dict(record_title = '',record_geolocation = '')),\
        content_type = ('application/json'))
        post_response = json.loads(i.data.decode())
        self.assertEqual(i.status_code,400)
        self.assertTrue(i.content_type,'application/json')
        self.assertTrue(post_response['message'],'fill in these fields')

    def test_get_all_records(self): 
        self.list = self.record.get_all_records()
        if not self.list:
                item = self.client.get('/api/v1/records/')
                self.assertEqual(item.status_code,204, msg = 'no item has been returned')
                self.assertTrue(item.content_type, 'application/json')
        else:
            item = self.client.get('/api/v1/records')
            response_data = json.loads(item.data.decode())
            self.assertTrue(item.content_type, 'application/json')
            self.assertEqual(item.status_code,200)

    def test_get_one_record(self):
        for record in self.record.records:
            if record['record_no'] is None:
                item = self.client.get('/api/v1/<int:record_no>/records')
                post_response = json.loads(item.data.decode())
                self.assertEqual(item.status_code,404, msg = 'no item has been returned')
                self.assertTrue(post_response['message'],'item not found')
            else:
                item = self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,200,msg = 'It hasnt been displayed')

    def test_modify_record(self):
        for record in self.record.records:
            if record['record_no'] is not None:
                item = self.client.post('/api/v1/<int:record_no>/',
                data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')),
                content_type = ('application/json'))
                self.assertEqual(item.status_code,201)
            else:
                item = self.client.get('/api/v1/<int:record_no>/records')
                self.assertEqual(item.status_code,404)

    def test_update_record(self):
        self.client.post('/api/v1/records/',
        data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')),\
        content_type = ('application/json'))
        self.client.post('/api/v1/records/',
        data = json.dumps(dict(record_title = 'theft',record_geolocation = '09494N 859494M')),\
        content_type = ('application/json'))
        self.client.post('/api/v1/records/',
        data = json.dumps(dict(record_title = 'burglary',record_geolocation = '09494N 859494M')),\
        content_type = ('application/json'))
        request_data =  self.client.put('/api/v1/records/3/',
            data = json.dumps(dict(record_geolocation = "0000000N 777777S")),\
            content_type = 'application/json')
        response_data  =  json.loads(request_data.data.decode())
        self.assertTrue(response_data['message'],'Record updated')
        self.assertTrue(request_data.content_type,'application/json')
        self.assertEqual(request_data.status_code,201)

    def test_update_non_existent_record(self):
        self.client.post('/api/v1/records/',
        data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')),
        content_type = ('application/json'))
        request_data =  self.client.put('/api/v1/records/1/',\
            data = json.dumps(dict(record_geolocation = "0000000N 777777S")),\
            content_type = 'application/json')
        response_data  =  json.loads(request_data.data.decode())
        self.assertTrue(response_data['message'],'record doesnt exist')
        self.assertTrue(request_data.content_type,'application/json')

    def test_delete_post(self):
        for record in self.record.records:
            if record['record_no'] is None:
                item = self.client.get('/api/v1/records/<int:record_no>/')
                self.assertEqual(item.status_code,404)
            else:
                item = self.client.delete('/api/v1/records/<int:record_no>/')
                self.assertEqual(item.status_code,200)

                # user_tests
    def post_user(self,user_name,user_password,email,user_id):
        data_to_be_posted = self.client.post('/api/v1/users/signup/',data = json.dumps(self.user),\
        content_type = ('application/json'))
        return data_to_be_posted

    def test_post_user(self):
        request_data = self.client.post('/api/v1/users/signup/',data = json.dumps(self.user),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,201)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['Message'],'New user registered successfully')

    def test_post_user_empty_fields(self):

        request_data = self.client.post('/api/v1/users/signup/',data = json.dumps(self.faulty_user),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,400)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['message'],'password is required')

    def test_login_user(self):
        self.client.post('/api/v1/users/signup/',data = json.dumps(self.other_user),content_type = ('application/json'))
        request_data = self.client.post('/api/v1/users/login/',\
        data = json.dumps({"user_name":"nichol","user_password":'great'}),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,200)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['message'],'you are successfully loged in')

    def test_login_user_empty_fields(self):
        self.client.post('/api/v1/users/signup/',data = json.dumps(self.other_user),content_type = ('application/json'))
        request_data = self.client.post('/api/v1/users/login/',\
        data = json.dumps({"user_name":"nichol","user_password":''}),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,400)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['Message'],'wrong password')

    def test_get_all_users_in_empty_list(self):
        request_data = self.client.get('/api/v1/users/',content_type = 'application/json')
        self.assertEqual(request_data.status_code,204)
        self.assertTrue(request_data.content_type,'application/json')

    # test to fetch all users
    def test_get_all_users(self):
        self.list = self.controller.fetch_all_users()
        if self.list:
            self.client.post('/api/v1/users/signup/',\
            data = json.dumps(dict(user_name = 'nicholus',user_password = 'straightup',email = 'nicholus@gmail.com')),\
            content_type = ('application/json'))
            request_data = self.client.get('/api/v1/users/',content_type = 'application/json')
            self.assertEqual(request_data.status_code,200)
            self.assertTrue(request_data.content_type,'application/json')

if __name__  ==  "__main__":
    unittest.main()