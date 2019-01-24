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
            headers=({'Authorization': 'Bearer' + 'token'}),
            content_type='application/json'
        )

    def post_record(self, record_title=None, record_geolocation=None, record_type=None, token=None):
        item = self.client.post(
            '/api/v2/records/',
            headers=dict(
                Authorization='Bearer' + 'token'
            ),
            data=json.dumps(dict(
                record_title=record_title,
                record_geolocation=record_geolocation,
                record_type=record_type
            )),
            content_type="application/json"
        )

        response = json.loads(item.data.decode())
        print (response)
        return response

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
        self.assertEqual(request_data.status_code,200)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['message'],'you are successfully loged in')

    def test_login_user_empty_fields(self):
        self.client.post('/api/v2/auth/signup/',data = json.dumps(self.other_user),content_type = ('application/json'))
        request_data = self.client.post('/api/v2/auth/login/',\
        data = json.dumps({"user_name":"nichol","user_password":''}),\
        content_type = ('application/json'))
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code,400)
        self.assertTrue(request_data.content_type,'application/json')
        self.assertTrue(response_data['error_message'],'wrong password')


    def test_non_registered_user_login(self):
        """
        Test for login of a non registered user
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
        """
        register =  self.client.post('/api/v2/auth/signup/',\
            data = json.dumps(dict(user_name = '2000',user_password = 'straightup',email = 'n@gamil.com')),\
            content_type = ('application/json'))
        received_data = json.loads(register.data.decode())
        self.assertTrue(received_data['status'], 'fail')
        self.assertTrue(received_data['error_message'], 'Please use character strings')
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)


    def test_invalid_password(self):
        """
        Test for password less than 5 characters
        """
        register = self.client.post('/api/v2/auth/signup/',\
            data = json.dumps(dict(user_name = 'milbeat',user_password = 'str',email = 'milly@gamil.com')),\
            content_type = ('application/json'))
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'],
                        'Password is wrong. It should be \
            at-least 5 characters long, and alphanumeric.It shouldnt also be \
            longer than 13 characters')
        self.assertFalse(response_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)

    def test_post_record_with_missing_fields(self):
        """
        Test for adding a record with missing fields
        """
        # sign up user
        self.register_user('steven', 'steven@gmail.com', 'straightup')

        # user login
        login = self.login_user('steven', 'straightup')

        create_record= self.client.post(
            '/api/v2/records/',
            headers=dict(
                Authorization='Bearer ' + json.loads(login.data.decode())['access_token']
            ),
            data=json.dumps(dict()),
            content_type="application/json"
        )

        data = json.loads(create_record.data.decode())
        self.assertTrue(data['status'], 'fail')
        self.assertTrue(data['error_message'], 'some fields are missing')
        self.assertTrue(data['data'])
        self.assertTrue(create_record.content_type, 'application/json')
        self.assertEqual(create_record.status_code, 400)

    # def test_get_one_user_reccord(self):
    #     login = self.login_user('steven', 'straightup')
    #     self.post_record("corruption", "redflag", "0.000004")
    #     get_user_record=self.client.get('/api/v2/auth/users/26/records/',
    #     headers=dict(
    #             Authorization='Bearer ' + json.loads(login.data.decode())['access_token']
    #         ),
    #                     content_type = 'application/json')
    #     data = json.loads(get_user_record.data.decode())
    #     self.assertTrue(get_user_record.content_type,'application/json')
    #     self.assertEqual(get_user_record.status_code, 200)       


    # def test_get_one_user_reccord_admin(self):
    #     login = self.login_user('Apple', 'acireba')
    #     self.post_record("corruption", "redflag", "0.000004")
    #     get_user_record=self.client.get('/api/v2/auth/users/26/records/',
    #     headers=dict(
    #             Authorization='Bearer ' + json.loads(login.data.decode())['access_token']
    #         ),
    #                     content_type = 'application/json')
    #     data = json.loads(get_user_record.data.decode())
    #     self.assertTrue(get_user_record.content_type,'application/json')
    #     self.assertEqual(get_user_record.status_code, 403)        


    def test_get_one_user_reccord_when_not_logged_in(self):
        
        self.post_record("corruption", "redflag", "0.000004")
        get_user_record=self.client.get('/api/v2/auth/users/26/records/'
            ,
                        content_type = 'application/json')
        data = json.loads(get_user_record.data.decode())
        self.assertTrue(get_user_record.content_type,'application/json')
        self.assertEqual(get_user_record.status_code, 401)


    def test_get_one_record(self):
        login = self.login_user('travis', 'straightup')
        self.post_record("corruption", "redflag", "0.000004")
        self.post_record('fire_breakout','intervention','-0.0008')
        get_user_record=self.client.get('/api/v2/auth/record/8'
            ,headers=dict(
                Authorization='Bearer ' + json.loads(login.data.decode())['access_token']
            ),
                        content_type = 'application/json'
            )
        data = json.loads(get_user_record.data.decode())
        self.assertTrue(get_user_record.content_type,'application/json')
        self.assertEqual(get_user_record.status_code, 200)


    # def test_get_one_record_not_loged_in(self):
        
    #     self.post_record("corruption", "redflag", "0.000004")
    #     self.post_record('fire_breakout','intervention','-0.0008')
    #     get_user_record=self.client.get('/api/v2/auth/record/8',
    #                     content_type = 'application/json'
    #         )
    #     data = json.loads(get_user_record.data.decode())
    #     self.assertTrue(get_user_record.content_type,'application/json')
    #     self.assertEqual(get_user_record.status_code, 401)
    
    # def test_get_one_record_by_admin(self):
    #     login = self.login_user('Apple', 'acireba')
    #     self.post_record("corruption", "redflag", "0.000004")
    #     self.post_record('fire_breakout','intervention','-0.0008')
    #     get_user_record=self.client.get('/api/v2/auth/record/8'
    #         ,headers=dict(
    #             Authorization='Bearer ' + json.loads(login.data.decode())['access_token']
    #         ),
    #                     content_type = 'application/json'
    #         )
    #     data = json.loads(get_user_record.data.decode())
    #     self.assertTrue(get_user_record.content_type,'application/json')
    #     self.assertEqual(get_user_record.status_code, 200)


    
if __name__  ==  "__main__":
    unittest.main()