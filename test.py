from flask import Flask,json,jsonify
import unittest
from app.model import Record
from app.routes import app

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
        self.client=app.test_client()
    
    @classmethod
    def tearDown(self):
        print ('Teardown')

    def test_record_creation(self):
        self.assertIsInstance(self.record, Record)

    #def test_record_is_empty(self):
      #  self.assertEqual(len(self.sample_records),0)
       # self.record.add_record(self.sample_records)
       # self.assertEqual(len(self.sample_records),1)


    def test_post_record(self):
        i=self.client.post('/api/v1/records',data=json.dumps(self.sample_records), content_type=('application/json'))
        self.assertEqual(i.status_code,201)#check if it was successfully created
       # i=self.client.get('/ft/v1/orders')
        #self.assertEqual(i.status_code,200)#to check if it was successfuly added to the list


    def test_get_all_records(self):
        item=self.client.get('/api/v1/records')
        self.assertEqual(item.status_code,200)





    

if __name__ == "__main__":
    unittest.main()


