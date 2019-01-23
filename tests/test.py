from flask import Flask, json, jsonify
import unittest
from run import app
from flask_jwt_extended import get_csrf_token,jwt_refresh_token_required,jwt_required
# from api.models.database import DatabaseConnection

# db=DatabaseConnection()

class test_feature(unittest.TestCase):

    @classmethod
    def setUp(self):
        app.testing = True
        self.user = {'user_name':'nicholus','user_password':'user_password',\
        "email":'email@g.com'}
        self.other_user = {'user_name':'nichol','user_password':'great',\
        "email":'nichol@g.com'}
        self.faulty_user = {'user_name':'nichol','user_password':'',\
        "email":'nichol@g.com'}
        self.app = app
        self.client = self.app.test_client()
        self.client.post('/api/v2/auth/signup/',data = json.dumps(
            dict(user_name='geraldine',
                user_password='gerry1',
                email='gerry@gmail.com')
        ),\
        content_type = ('application/json'))
        login=self.client.post('/api/v2/auth/login/',\
        data = json.dumps({"user_name":"geraldine","user_password":'gerry1'}),\
        content_type = ('application/json'))
        login_decode_message= json.loads(login.data.decode())
        self.Token = login_decode_message.get('token')

    @classmethod
    def tearDown(self):
        # db.drop_tables('user_list')
        print('Teardown')


    def register_user(self, user_name=None, email=None,  user_password=None):
        return self.client.post(
            '/api/v2/auth/signup/',
            data=json.dumps(dict(
                user_name=user_name,
                email=email,
                user_password=user_password,
            )),
            content_type="application/json"
        )

    def login_user(self, user_name=None, user_password=None):
        return self.client.post(
            '/api/v2/auth/login/',
            data=json.dumps(dict(
                user_name=user_name,
                user_password=user_password,
            )),
            content_type='application/json'
        )

    def post_record(self, record_title=None, record_geolocation=None, record_type=None, token=None):
        return self.client.post(
            '/api/v2/records/',
            headers=dict(
                Authorization='Bearer' + token
            ),
            data=json.dumps(dict(
                record_title=record_title,
                record_geolocation=record_geolocation,
                record_type=record_type
            )),
            content_type="application/json"
        )
    # def post_record(self,record_no,record_title,record_geolocation,record_type):
    #     data_to_be_posted = self.client.post('/api/v1/records/',\
    #     data = json.dumps(dict(record_title = 'corruption',record_geolocation = '09494N 859494M')),\
    #     content_type = ('application/json'))
    #     return data_to_be_posted

    # def test_record_creation(self):
    #     self.assertIsInstance(self.record, Record)

    def test_home(self):
        index = self.client.get('/',content_type = 'application/json')
        return self.assertEqual(index.status_code,200)

    def test_post_user_who_exists(self):
        request_data = self.client.post('/api/v2/auth/signup/',data = json.dumps(
            dict(user_name='travispro',
                user_password='straightup',
                email='travispro@gmail.com')
        ),\
        content_type = ('application/json'))
        request_data = self.client.post('/api/v2/auth/signup/',data = json.dumps(
            dict(user_name='travispro',
                user_password='straightup',
                email='travispro@gmail.com')
        ),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        print (response_data)
        self.assertEqual(request_data.status_code,409)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['error_message'],'email already exists')


    def test_post_user_empty_fields(self):

        request_data = self.client.post('/api/v2/auth/signup/',data = json.dumps(self.faulty_user),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,400)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['error_message'],'password is required')

    def test_login_user(self):
        self.client.post(
            '/api/v2/auth/signup/',
            data = json.dumps(dict(user_name='jameson',email = 'jm@gmail.com',user_password='deezer')),
            content_type = ('application/json'))
        request_data = self.client.post('/api/v2/auth/login/',\
        data = json.dumps({"user_name":"jameson","user_password":'deezer'}),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        print(request_data)
        self.assertEqual(request_data.status_code,200)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['message'],'you are successfully loged in')

    def test_login_user_empty_fields(self):
        self.client.post('/api/v2/auth/signup/',data = json.dumps(self.other_user),content_type = ('application/json'))
        request_data = self.client.post('/api/v2/auth/login/',\
        data = json.dumps({"user_name":"nichol","user_password":''}),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        print (response_data)
        self.assertEqual(request_data.status_code,400)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['error_message'],'wrong password')

    # def test_get_all_users_in_empty_list(self):
    #     request_data = self.client.get('/api/v1/users/',content_type = 'application/json')
    #     self.assertEqual(request_data.status_code,204)
    #     self.assertTrue(request_data.content_type,'application/json')

    # test to fetch all users
    # def test_get_all_users(self):
    #         self.client.post('/api/v2/auth/signup/',\
    #         data = json.dumps(dict(user_name = 'nicholus',
    #         user_password = 'straightup',email = 'nicholus@gmail.com')),\
    #         content_type = ('application/json'))

    #         login = self.client.post(
    #         '/api/v2/auth/login/',
    #         data = json.dumps(self.other_user),
    #         content_type = ('application/json'))

            # request_data = self.client.get('/api/v2/redflags/', headers={'Authorization': 'Bearer ' + self.Token})
            # response_data= json.loads(request_data.data.decode())
            # print (response_data)
            # self.assertEqual(request_data.status_code,200)
            # self.assertTrue(request_data.content_type,'application/json')


    def test_non_registered_user_login(self):
        """
        Test for login of a non registered user
        :return:
        """
        login_user =  self.client.post(
            '/api/v2/auth/login/',
            data = json.dumps(dict(user_name='mastula',user_password= 'goodgirl')),
            content_type = ('application/json'))
        data = json.loads(login_user.data.decode())
        self.assertTrue(data['status'], 'fail')
        self.assertTrue(data['message'], 'User does not exist.')
        self.assertTrue(login_user.content_type, 'application/json')
        self.assertEqual(login_user.status_code, 404)

    def test_login_with_missing_fields(self):
        """
        Test for login with missing fields
        :return:
        """
        self.client.post('/api/v2/auth/signup/',\
            data = json.dumps(dict(user_name = 'habib',
            user_password = 'straightup',email = 'habib@gmail.com')),\
            content_type = ('application/json'))
        login_user = self.client.post(
            '/api/v2/auth/login/',
            data=json.dumps(dict(
                user_name="habib"
            )),
            content_type='application/json'
        )

        response_data = json.loads(login_user.data.decode())

        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'], 'some fields are missing')
        self.assertTrue(login_user.content_type, 'application/json')
        self.assertEqual(login_user.status_code, 400)

    def test_invalid_data_type(self):
        """
        Test user registration with invalid data-type
        :return:
        """
        register =  self.client.post('/api/v2/auth/signup/',\
            data = json.dumps(dict(user_name = '2000',user_password = 'straightup',email = 'n@gamil.com')),\
            content_type = ('application/json'))
        received_data = json.loads(register.data.decode())
        print (received_data)
        self.assertTrue(received_data['status'], 'fail')
        self.assertTrue(received_data['error_message'], 'Please use character strings')
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)


    def test_invalid_password(self):
        """
        Test for password less than 5 characters
        :return:
        """
        register = self.client.post('/api/v2/auth/signup/',\
            data = json.dumps(dict(user_name = 'milbeat',user_password = 'str',email = 'milly@gamil.com')),\
            content_type = ('application/json'))
        response_data = json.loads(register.data.decode())
        print (response_data)
        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'],
                        'Password is wrong. It should be \
            at-least 5 characters long, and alphanumeric.It shouldnt also be \
            longer than 13 characters')
        self.assertFalse(response_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)


    


    


if __name__  ==  "__main__":
    unittest.main()